"""Agropecuaria TP 3.º medio: OAE-06 (sanidad vegetal), OAE-07 (registros) y OAE-08 (información remota e instrumental). Todo en papel, con datos de ejemplo; sin procedimientos operativos ni dosis."""
from __future__ import annotations

from tp_agro_common import AVISO, EMER, build

O6 = "TP-AGRO-3-OAE-06"
O7 = "TP-AGRO-3-OAE-07"
O8 = "TP-AGRO-3-OAE-08"

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Huerto Demo» es un predio ficticio de 5 hectáreas de hortalizas. Se observan pulgones (insectos pequeños que chupan la savia) en algunas plantas, manchas de un hongo en hojas y malezas entre las hileras. "
     "En la bodega hay productos de uso sanitario guardados, y una pulverizadora (equipo que esparce líquidos en gotas finas). Peligros anotados: contacto o inhalación de productos, viento que arrastra gotas hacia otros lugares, contaminación del canal cercano y daño a las abejas del huerto vecino.")
build(
    O6, 1, F,
    use="Aprenderé qué son las plagas, las enfermedades y las malezas, por qué los productos de uso sanitario exigen personal autorizado y norma vigente, y cuáles son sus peligros.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé que las plantas pueden enfermar o ser dañadas por insectos."],
    explain=[
        "La sanidad vegetal cuida la salud de los cultivos. Una plaga es un animal, como un insecto, que daña al cultivo; una enfermedad es un daño causado por hongos, bacterias o virus; una maleza es una planta que crece donde no se desea y compite por agua, luz y nutrientes. Los métodos de control pueden ser preventivos, que evitan el problema, o curativos, que lo corrigen; y pueden ser culturales, biológicos, orgánicos o químicos.",
        "Los productos químicos de uso sanitario, como los plaguicidas, son peligrosos para las personas, el ambiente y otros seres vivos. Por eso la legislación sanitaria, ambiental y laboral vigente exige que solo se usen productos autorizados por la autoridad sanitaria agrícola, según su etiqueta, y que los aplique personal capacitado y autorizado. Un producto se guarda cerrado, rotulado y fuera del alcance de personas no autorizadas.",
        f"La jerarquía de controles aplica: una bodega cerrada con llave es un control de ingeniería; una regla de aplicar solo con viento calmo es administrativa. El equipo de protección personal (EPP) es la última barrera. {EMER} {AVISO}",
    ],
    vocab=[("sanidad vegetal", "cuidado de la salud de los cultivos"), ("plaga", "animal, como un insecto, que daña al cultivo"), ("enfermedad", "daño causado por hongos, bacterias o virus"), ("maleza", "planta que crece donde no se desea"), ("plaguicida", "producto químico para controlar plagas, enfermedades o malezas"), ("etiqueta", "documento pegado al producto con su uso autorizado y sus peligros"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Clasificar un problema", "En un predio de ejemplo hay un hongo en las hojas de las plantas. ¿Es plaga, enfermedad o maleza?", ["El hongo es un microorganismo que daña a la planta.", "El daño causado por hongos es una enfermedad."], "Enfermedad"),
        ("Clasificar un control", "Un predio de ejemplo instala un piso con borde elevado que contiene los derrames dentro de la sala de productos. ¿Qué tipo de control es?", ["El borde elevado cambia físicamente el lugar.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que «natural» significa sin riesgo para las personas.", "Algunos productos orgánicos también tienen peligros.", "Todo producto se usa según su etiqueta y por personal autorizado."),
              ("Creer que leer sobre aplicaciones habilita para aplicar un producto.", "Aplicar productos exige capacitación, autorización y norma vigente.", "Aprende aquí el concepto y deja la aplicación a personal autorizado.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es una plaga del cultivo?", "Un animal, como un insecto, que daña al cultivo", "Un hongo que causa manchas en las hojas", "Una planta que crece donde no se desea", "La plaga es un animal; el hongo es enfermedad y la planta no deseada es maleza."),
        ("abc", "En Agropecuaria: ¿qué es una maleza?", "Una planta que crece donde no se desea y compite con el cultivo", "Un insecto que chupa la savia", "Un hongo que daña las hojas", "La maleza es una planta no deseada; los insectos y hongos son otros problemas."),
        ("abc", "En Agropecuaria: ¿qué indica la etiqueta de un producto de uso sanitario?", "Su uso autorizado y sus peligros", "El precio de venta del producto", "El nombre del agricultor que lo compró", "La etiqueta informa el uso y los peligros."),
        ("=", "{F} El huerto tiene 5 hectáreas y se divide en parcelas iguales de 1 hectárea. Se monitorea el 40 % de las parcelas, pero solo se pueden monitorear parcelas enteras. ¿Cuántas parcelas se monitorean?", "5*40//100", "Se calcula el porcentaje sobre el número de parcelas.", " parcelas"),
        ("abc", "{F} Guardar los productos de uso sanitario en una bodega cerrada con llave es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla", "De EPP, porque protege a quien aplica", "La bodega es una estructura física que limita el acceso."),
        ("abc", "{F} Una regla que dice «no se aplica con viento fuerte» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia la pulverizadora", "De sustitución, porque cambia el producto", "Una regla escrita es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al viento que arrastra gotas de un producto?", "Que el producto llegue a otras personas, al canal o a las abejas", "El producto guardado en la bodega", "Que la pulverizadora esté vacía", "El riesgo es el daño posible; el producto guardado es el peligro."),
        ("abc", "{F} Una estudiante dice: «ya entendí cómo se aplica, así que preparo el producto y lo aplico yo». ¿Qué respuesta es correcta?", "Es falso: preparar y aplicar productos exige capacitación, autorización y norma vigente", "Es cierto, si usa mascarilla", "Es cierto, si aplica poco producto", "El EPP o la cantidad pequeña no reemplazan la autorización."),
        ("abc", "{F} En una visita, una persona se siente mal cerca de la zona donde se aplica un producto. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a ayudarla sin protección", "Tomar un medicamento que tengas a mano", "Entrar a la zona puede intoxicarte a ti también."),
        ("abc", "En Agropecuaria: ¿por qué hay que guardar los productos de uso sanitario cerrados y rotulados?", "Para evitar que personas no autorizadas los usen o los confundan", "Para que se mantengan siempre tibios", "Para que ocupen menos espacio", "El rótulo y el cierre previenen confusiones y accidentes."),
        ("abc", "{F} Se propone solo entregar guantes para reducir el riesgo con los productos. ¿Qué medida es más efectiva?", "Controlar quién accede a los productos y guardarlos cerrados", "Entregar un segundo par de guantes", "Pedir que nadie los toque cuando pueda evitarlo", "Limitar el acceso actúa sobre el peligro; el guante es EPP."),
        ("=", "{F} En el monitoreo de ejemplo se revisan 10 plantas por cada hectárea del huerto. ¿Cuántas plantas se revisan en total?", "5*10", "Se multiplican las hectáreas por las plantas revisadas en cada una.", " plantas"),
        ("abc", "En Agropecuaria: ¿por qué un control preventivo es mejor que esperar a que el cultivo esté muy dañado?", "Porque evita el problema antes de que cause pérdidas", "Porque no necesita ningún registro", "Porque siempre usa productos químicos", "Prevenir cuesta menos y evita pérdidas."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por aplicar un producto de uso sanitario en su huerto «porque ya viste cómo se hace en clases». ¿Qué respondes?", "Que no, porque exige capacitación y autorización, y que lo consultarás con un adulto responsable", "Que sí, con mascarilla", "Que sí, si el huerto es pequeño", "Haber visto el concepto no habilita para aplicar; el tamaño del huerto o la mascarilla no cambian eso."),
    sc=[
        ("En Agropecuaria: ¿qué es una enfermedad del cultivo?", "Un daño causado por hongos, bacterias o virus", "Los microorganismos causan las enfermedades de las plantas."),
        ("En el trabajo agrícola: ¿qué es lo último en la jerarquía de controles?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En Agropecuaria: ¿quién aplica un plaguicida?", "Personal capacitado y autorizado", "La norma vigente exige capacitación y autorización."),
    ],
    op=("El «Huerto Demo 2» anota una tarea de ejemplo: guardar sin etiqueta unos envases de producto en un galpón abierto, al alcance de cualquier visitante. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves un derrame cerca del canal.",
        "(a) Peligro: productos sin etiqueta al alcance de cualquiera; riesgo: que alguien los confunda, los use mal o se intoxique. (b) Una regla de rotular todo y registrar quién retira cada producto. (c) Una bodega cerrada con llave. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no se acerca al derrame y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer limpiar el derrame sin formación"],
        "Pregunta: «¿qué control limita el acceso aunque alguien se olvide de la regla?». Si no responde, pídele que relea el tercer párrafo."),
    reinforce="Clasifica como plaga, enfermedad o maleza: un gusano que come hojas, un hongo en el tallo y una planta no deseada entre las hileras.",
    extend="Explica con un ejemplo por qué ser «natural» no significa que un producto no tenga riesgo.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (etiqueta y registro de ejemplo, inventados). Producto de ejemplo «Producto A»: uso en hortalizas contra pulgones; período de carencia 7 días (días que deben pasar entre la última aplicación y la cosecha); período de reingreso 1 día (tiempo antes de volver a entrar al lote). "
     "Registro de aplicaciones del Huerto Demo: lote 3, última aplicación el día 10 del mes; cosecha planificada el día 15 del mismo mes. Otros documentos: el registro de monitoreo (conteos de plagas), la hoja de datos de seguridad y la recomendación escrita del asesor.")
build(
    O6, 2, F,
    use="Aprenderé los conceptos de monitoreo, umbral, período de carencia y reingreso, métodos de control y los documentos y roles de la sanidad vegetal, sin aplicar ningún producto.",
    prior=["Sé qué son plaga, enfermedad y maleza.", "Sé leer una etiqueta y un registro.", "Sé restar enteros."],
    explain=[
        "El monitoreo es revisar el cultivo con regularidad y contar las plagas, enfermedades o malezas. El umbral de acción es el nivel de daño desde el cual conviene controlar. El manejo integrado de plagas combina varios métodos: el control cultural (como rotar cultivos y mantener limpio el predio), el control biológico (usar enemigos naturales de la plaga), el control orgánico (productos permitidos en la producción orgánica) y el control químico, que se usa solo si es necesario.",
        "Los productos tienen dos plazos de seguridad. El período de carencia es el tiempo mínimo entre la última aplicación y la cosecha, para que los residuos bajen a niveles permitidos. El período de reingreso es el tiempo antes de que las personas vuelvan a entrar al lote tratado. Ambos plazos están en la etiqueta y se cumplen siempre.",
        f"El asesor recomienda, el aplicador autorizado ejecuta y el jefe de campo registra. Nadie cambia una fecha para que el registro «cumpla». {EMER} {AVISO}",
    ],
    vocab=[("monitoreo", "revisión regular del cultivo para contar plagas o daños"), ("umbral de acción", "nivel de daño desde el cual conviene controlar"), ("control biológico", "uso de enemigos naturales de la plaga"), ("período de carencia", "tiempo mínimo entre la última aplicación y la cosecha"), ("período de reingreso", "tiempo antes de volver a entrar al lote tratado"), ("hoja de datos de seguridad", "documento con los peligros de un producto y su manejo"), ("asesor", "profesional que recomienda por escrito qué hacer")],
    worked=[
        ("Verificar la carencia", "Un producto de ejemplo tiene carencia de 5 días y se aplicó el día 20. ¿Cuál es el primer día en que se puede cosechar?", ["Se suman 5 días a la fecha de aplicación.", "20 más 5 es 25."], "El día 25"),
        ("Elegir el documento", "Un jefe de campo de ejemplo quiere saber cuántos pulgones por planta se contaron ayer. ¿Qué documento consulta?", ["Los conteos se anotan en un registro de monitoreo.", "No es la etiqueta, que describe el producto."], "El registro de monitoreo"),
    ],
    mistakes=[("Creer que se puede cosechar apenas se cumple el período de reingreso.", "El reingreso y la carencia son plazos distintos.", "La cosecha espera el período de carencia."),
              ("Cambiar la fecha de aplicación en el registro para cumplir la carencia.", "Un registro alterado falsea la información y pone en riesgo la salud.", "Se registra la fecha real y se pospone la cosecha.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es el período de carencia?", "El tiempo mínimo entre la última aplicación y la cosecha", "El tiempo antes de volver a entrar al lote tratado", "El tiempo que dura la aplicación", "La carencia protege al consumidor; el reingreso protege al trabajador."),
        ("abc", "En Agropecuaria: ¿qué es el período de reingreso?", "El tiempo antes de volver a entrar al lote tratado", "El tiempo mínimo entre la aplicación y la cosecha", "El tiempo en que el producto está guardado", "El reingreso protege a las personas que entran al lote."),
        ("abc", "En Agropecuaria: ¿qué es el monitoreo?", "La revisión regular del cultivo para contar plagas o daños", "La compra de productos de uso sanitario", "La limpieza de la bodega", "El monitoreo cuenta lo observado en el cultivo."),
        ("=", "{F} ¿En qué día del mes se puede cosechar, como mínimo, respetando la carencia del producto?", "10+7", "Se suman los días de carencia a la fecha de la última aplicación.", " (día del mes)"),
        ("abc", "{F} Con la cosecha planificada el día 15, ¿se respeta la carencia?", "No, porque pasan solo 5 días y la carencia pide 7", "Sí, porque pasan más de 7 días", "Sí, porque el reingreso es de 1 día", "Entre el 10 y el 15 pasan 5 días, menos que los 7 de carencia."),
        ("abc", "{F} ¿Qué documento tiene los peligros del producto y cómo manejarlo?", "La hoja de datos de seguridad", "El registro de aplicaciones", "El registro de monitoreo", "La hoja de datos trata de los peligros del producto."),
        ("abc", "{F} ¿Qué rol recomienda por escrito qué hacer ante la plaga?", "El asesor", "El aplicador autorizado", "El jefe de la bodega", "El asesor recomienda; el aplicador ejecuta."),
        ("=", "{F} Si se pospone la cosecha para cumplir la carencia, ¿cuántos días hay que esperar desde el día 15 para llegar al mínimo?", "(10+7)-15", "Se resta la fecha planificada al primer día permitido.", " días"),
        ("abc", "{F} El jefe de campo quiere cambiar en el registro la fecha de aplicación al día 5 «para cumplir». ¿Qué corresponde?", "Rechazarlo: se registra la fecha real y se pospone la cosecha", "Aceptarlo, porque lo importante es que el registro cumpla", "Aceptarlo, si lo firma el asesor", "Alterar la fecha falsea el registro y pone en riesgo al consumidor."),
        ("abc", "{F} Una estudiante dice: «pasó el día de reingreso, así que ya se puede cosechar». ¿Qué respuesta es correcta?", "Es falso: la cosecha espera la carencia de 7 días, no el reingreso", "Es cierto, porque el reingreso es lo único que importa", "Es cierto, si el lote se ve limpio", "Los dos plazos son distintos y cada uno protege a personas distintas."),
        ("=", "{F} Se contaron 3, 5 y 4 pulgones en tres plantas del lote. ¿Cuál es el promedio por planta?", "(3+5+4)//3", "Se suman los conteos y se divide entre el número de plantas.", " pulgones"),
        ("abc", "{F} El umbral de acción de ejemplo es 8 pulgones por planta. Con un promedio de 4, ¿qué corresponde?", "Seguir monitoreando, porque no se alcanzó el umbral", "Aplicar de inmediato un producto", "Cosechar el lote", "Bajo el umbral conviene seguir revisando y usar métodos preventivos."),
        ("abc", "En Agropecuaria: ¿qué es el control biológico?", "El uso de enemigos naturales de la plaga", "El uso de cualquier producto natural", "La quema de las plantas afectadas", "El control biológico aprovecha organismos que se alimentan de la plaga."),
    ],
    ctx=("abc", "Un conocido te pide que le «ajustes» la fecha de aplicación de su registro para vender antes. ¿Qué respondes?", "Que no, porque el registro anota lo real y la carencia protege a quien consume, y que consultarás con un adulto responsable", "Que sí, por un día", "Que sí, si el cliente no pregunta", "Alterar el registro engaña al cliente y puede dañar la salud."),
    sc=[
        ("En Agropecuaria: ¿qué protege el período de carencia?", "A quien consume el producto cosechado", "La carencia deja bajar los residuos antes de la cosecha."),
        ("En el trabajo agrícola: ¿quién registra las aplicaciones?", "El jefe de campo", "El jefe de campo deja evidencia de lo realizado."),
        ("En Agropecuaria: ¿qué es el umbral de acción?", "El nivel de daño desde el cual conviene controlar", "El umbral dice cuándo conviene empezar a actuar."),
    ],
    op=("Etiqueta de ejemplo del «Producto B»: carencia 10 días y reingreso 2 días. Registro de ejemplo del lote 4 del Huerto Demo: última aplicación el día 6 del mes; cosecha planificada el día 14. Conteo de pulgones en cuatro plantas: 6, 8, 4 y 6; umbral de ejemplo de 10 por planta. Escribe (a) el primer día permitido para cosechar, (b) si el día 14 es válido, (c) el promedio de pulgones por planta y si alcanza el umbral, (d) quién recomienda y quién aplica.",
        "(a) 6 + 10 = día 16. (b) No, porque faltan 2 días. (c) (6 + 8 + 4 + 6) ÷ 4 = 6; no alcanza el umbral de 10. (d) El asesor recomienda; el aplicador autorizado aplica.",
        ["calcula el primer día de cosecha", "concluye sobre el día 14", "calcula el promedio y compara", "distingue asesor y aplicador"],
        ["hoja con las cuatro respuestas"],
        ["confundir carencia con reingreso", "alterar la fecha", "aplicar sin asesor"],
        "Pregunta: «¿qué plazo se suma a la fecha de aplicación para cosechar?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Calcula el primer día de cosecha de un producto de ejemplo con carencia de 12 días aplicado el día 3.",
    extend="Explica con un ejemplo por qué el período de reingreso y el período de carencia protegen a personas distintas.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (monitoreo de ejemplo, inventado). Dos lotes del «Huerto Demo», conteo de pulgones en 5 plantas por lote. Lote 1: 2, 0, 3, 1, 4. Lote 2: 12, 10, 9, 14, 15. Umbral de acción de ejemplo: 8 pulgones por planta en promedio. "
     "Métodos posibles (conceptos): cultural (eliminar malezas hospederas), biológico (proteger enemigos naturales) y químico (solo con receta del asesor y aplicador autorizado).")
build(
    O6, 3, F,
    use="Aprenderé a analizar un caso de monitoreo con datos escritos, a comparar el promedio con el umbral y a decidir qué método conceptual conviene y quién lo ejecuta.",
    prior=["Sé qué es el monitoreo y el umbral.", "Sé calcular promedios de enteros.", "Sé qué métodos de control existen."],
    explain=[
        "Para analizar un caso de monitoreo se calcula el promedio de los conteos y se compara con el umbral de acción. Si el promedio es menor, se sigue monitoreando y se refuerzan los métodos preventivos, como el control cultural o la protección de enemigos naturales. Si el promedio supera el umbral, el asesor evalúa el método de control más adecuado, considerando el destino de la producción, el ambiente y las personas.",
        "Un buen análisis nombra los datos, el promedio, la comparación con el umbral y la decisión. El control químico no es la primera respuesta: se usa cuando los otros métodos no bastan, con una recomendación escrita y un aplicador autorizado. Los plazos de carencia y reingreso se respetan siempre. Si el cultivo tiene destino orgánico, solo se pueden usar productos permitidos para ese sistema.",
        f"Quien analiza el caso no decide ni aplica por cuenta propia: informa al asesor y deja el registro. {EMER} {AVISO}",
    ],
    vocab=[("hospedero", "planta donde viven o crecen las plagas"), ("enemigo natural", "organismo que se alimenta de una plaga"), ("manejo integrado", "combinación de varios métodos de control"), ("destino de la producción", "uso final de lo cosechado, como mercado nacional o producto orgánico"), ("receta del asesor", "recomendación escrita del asesor antes de aplicar")],
    worked=[
        ("Comparar con el umbral", "Un lote de ejemplo tiene un promedio de 5 pulgones por planta y el umbral es 8. ¿Se alcanza el umbral?", ["Se compara 5 con 8.", "5 es menor que 8."], "No, sigue monitoreando"),
        ("Elegir el primer método", "Un lote de ejemplo tiene muchas malezas hospederas de la plaga. ¿Qué método cultural conviene analizar?", ["Las malezas albergan a la plaga.", "Eliminar malezas hospederas es un control cultural."], "Eliminar las malezas hospederas, hecho por personal autorizado"),
    ],
    mistakes=[("Aplicar un producto apenas se ve una plaga, sin contar.", "No se sabe si se alcanzó el umbral.", "Se monitorea y se compara con el umbral."),
              ("Usar un producto no permitido en un cultivo de destino orgánico.", "El destino de la producción limita los productos.", "Se consulta al asesor el destino antes de decidir.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es un enemigo natural de una plaga?", "Un organismo que se alimenta de la plaga", "Un producto químico que la mata", "Una planta no deseada", "El enemigo natural es un organismo; el producto es químico."),
        ("abc", "En Agropecuaria: ¿qué es el manejo integrado de plagas?", "La combinación de varios métodos de control", "El uso de un solo producto químico", "La eliminación total de los insectos", "El manejo integrado combina métodos y busca no depender de uno solo."),
        ("abc", "En Agropecuaria: ¿qué es el destino de la producción?", "El uso final de lo cosechado, como mercado nacional o producto orgánico", "El lugar donde se guarda el producto", "El nombre de la pulverizadora", "El destino define qué productos se pueden usar."),
        ("=", "{F} ¿Cuál es el promedio de pulgones por planta en el Lote 1?", "(2+0+3+1+4)//5", "Se suman los conteos y se divide entre las 5 plantas.", " pulgones"),
        ("=", "{F} ¿Cuál es el promedio de pulgones por planta en el Lote 2?", "(12+10+9+14+15)//5", "Se suman los conteos y se divide entre las 5 plantas.", " pulgones"),
        ("abc", "{F} ¿Cuál lote supera el umbral de acción?", "El Lote 2, con promedio 12", "El Lote 1, con promedio 2", "Ambos lotes", "El Lote 2 tiene promedio 12, mayor que 8; el Lote 1 no llega."),
        ("abc", "{F} ¿Qué corresponde en el Lote 1?", "Seguir monitoreando y reforzar métodos preventivos", "Aplicar un producto de inmediato", "Cosechar todo el lote", "Bajo el umbral no se aplica; se sigue revisando."),
        ("abc", "{F} ¿Qué corresponde en el Lote 2 si los otros métodos no bastan?", "Pedir la recomendación del asesor y, si la receta lo indica, que aplique personal autorizado", "Aplicar el producto que haya en la bodega", "Pedir a un estudiante que lo aplique", "El control químico se decide con el asesor y lo ejecuta personal autorizado."),
        ("abc", "{F} Un compañero dice: «como el Lote 2 supera el umbral, aplico el producto que me quede». ¿Qué respuesta es correcta?", "Es falso: la aplicación exige receta del asesor y aplicador autorizado", "Es cierto, porque el umbral lo autoriza", "Es cierto, si lo hace de noche", "Superar el umbral no autoriza a nadie; hace falta la recomendación del asesor."),
        ("=", "{F} Si el promedio del Lote 2 baja en 4 pulgones tras otras medidas, ¿cuál sería el nuevo promedio?", "(12+10+9+14+15)//5-4", "Se resta la baja al promedio calculado.", " pulgones"),
        ("abc", "{F} Si el Lote 2 es de producción orgánica, ¿qué debe revisar el asesor antes de decidir?", "Qué productos están permitidos para producción orgánica", "El color de la etiqueta", "El número de plantas por hectárea", "El destino orgánico limita los productos que se pueden usar."),
        ("abc", "{F} Durante el monitoreo, una persona se marea cerca de un lote tratado hace un día. ¿Qué corresponde?", "No acercarte, avisar a un adulto responsable y a emergencias", "Quedarte a ayudar sin protección", "Seguir monitoreando", "Podría haber residuos; se avisa a quienes pueden actuar."),
        ("abc", "En Agropecuaria: ¿por qué no conviene aplicar productos sin haber contado la plaga?", "Porque no se sabe si hay daño suficiente para justificarlo", "Porque los conteos son obligatorios en invierno", "Porque contar mata a la plaga", "Sin conteo no hay forma de comparar con el umbral."),
    ],
    ctx=("abc", "Una conocida te muestra fotos de su cultivo con hojas comidas y te pide que le indiques el producto exacto. ¿Qué respondes?", "Que no puedes indicarlo y que un asesor debe evaluar el problema y recomendar", "Que use el más fuerte", "Que use el mismo del vecino", "La recomendación requiere diagnóstico del asesor, el destino y la norma vigente."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula el promedio de cinco conteos?", "Se suman los cinco conteos y se divide entre 5", "El promedio resume los datos para compararlos con el umbral."),
        ("En el trabajo agrícola: ¿cuándo se decide un control químico?", "Cuando lo recomienda el asesor y los otros métodos no bastan", "El control químico es una de las opciones y no la primera."),
        ("En Agropecuaria: ¿qué se compara con el umbral de acción?", "El promedio de los conteos", "Se compara el promedio con el umbral para decidir."),
    ],
    op=("Conteo de ejemplo en el «Huerto Demo 3»: Lote A: 1, 3, 2, 2, 2 pulgones por planta; Lote B: 9, 11, 8, 12, 10. Umbral de ejemplo: 7 por planta en promedio. Escribe (a) el promedio de cada lote, (b) cuál supera el umbral, (c) qué hacer en el que no lo supera, (d) quién decide el método en el que sí lo supera y quién aplica.",
        "(a) A: (1 + 3 + 2 + 2 + 2) ÷ 5 = 2; B: (9 + 11 + 8 + 12 + 10) ÷ 5 = 10. (b) El Lote B. (c) Seguir monitoreando y reforzar lo preventivo. (d) Decide el asesor; aplica personal autorizado, si se recomienda control químico.",
        ["calcula los promedios", "compara con el umbral", "propone qué hacer bajo el umbral", "distingue asesor y aplicador"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal", "aplicar bajo el umbral", "decidir por cuenta propia"],
        "Pregunta: «¿qué número de cada lote comparas con el umbral?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el promedio de este conteo inventado: 5, 7, 6, 8 y 9 pulgones por planta, y compáralo con un umbral de 6.",
    extend="Explica con un ejemplo por qué el control cultural puede reducir la necesidad de productos químicos.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Lote de 10 hectáreas del «Huerto Demo». Producción esperada sin control: 20.000 kg por hectárea; precio de ejemplo $200 por kilo. Si no se controla la plaga, se pierde 10 % de la producción. "
     "Costo de ejemplo del control recomendado por el asesor: $150.000 por hectárea. En una muestra de 50 plantas, 8 tienen daño visible.")
build(
    O6, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular la incidencia de un daño y comparar el costo del control con la pérdida que evita.",
    prior=["Sé calcular porcentajes enteros.", "Sé multiplicar y dividir enteros.", "Sé qué es el umbral de acción."],
    explain=[
        "La incidencia es el porcentaje de plantas con daño: se divide las plantas con daño por las revisadas y se multiplica por 100. Sirve para decidir si se actúa, junto con el umbral de acción. Un umbral económico compara dos números: el costo de controlar y la pérdida que se evita. Si el control cuesta menos que la pérdida evitada, conviene; si cuesta más, no conviene, salvo que haya otras razones, como proteger la salud o el destino de la producción.",
        "La pérdida evitada se calcula así: producción por hectárea por precio da el ingreso por hectárea; el porcentaje de pérdida da el valor que se perdería; y se multiplica por las hectáreas. El costo del control se calcula multiplicando su valor por hectárea por las hectáreas. Los números son de ejemplo y la decisión la toma el asesor.",
        f"Un criterio económico no reemplaza el criterio de seguridad: ningún ahorro justifica saltarse una carencia o un reingreso. {EMER} {AVISO}",
    ],
    vocab=[("incidencia", "porcentaje de plantas con daño"), ("pérdida evitada", "dinero que se deja de perder gracias al control"), ("ingreso", "producción multiplicada por el precio"), ("umbral económico", "punto en que el costo del control iguala la pérdida evitada"), ("muestra", "grupo de plantas revisadas que representa al lote")],
    worked=[
        ("Incidencia", "En una muestra de ejemplo de 40 plantas, 10 tienen daño. ¿Cuál es la incidencia?", ["Se divide 10 entre 40, que es un cuarto.", "Un cuarto es 25 %."], "25 %"),
        ("Comparar costo y pérdida", "Un control de ejemplo cuesta $50.000 y evita una pérdida de $80.000. ¿Conviene?", ["La pérdida evitada es mayor que el costo.", "80.000 menos 50.000 es 30.000 a favor."], "Conviene, con $30.000 a favor"),
    ],
    mistakes=[("Comparar el costo del control con la producción total en vez de con la pérdida evitada.", "El control no evita toda la producción perdida, solo la parte que se dañaría.", "Compara el costo con la pérdida que realmente se evita."),
              ("Decidir solo por el costo y saltarse el período de carencia.", "El ahorro no justifica un riesgo para la salud.", "Los plazos de seguridad se respetan siempre.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la incidencia de un daño en el cultivo?", "El porcentaje de plantas con daño", "La cantidad de producto aplicado", "El precio del cultivo por kilo", "La incidencia mide plantas dañadas sobre revisadas."),
        ("abc", "En Agropecuaria: ¿qué es la pérdida evitada de un control?", "El dinero que se deja de perder gracias al control", "El costo del producto usado", "La pérdida total de la producción", "La pérdida evitada es lo que se salva por controlar."),
        ("abc", "En Agropecuaria: ¿cuándo conviene económicamente un control?", "Cuando cuesta menos que la pérdida que evita", "Cuando cuesta más que la pérdida que evita", "Cuando no se mide el daño", "Si el costo es menor que lo que se salva, conviene."),
        ("=", "{F} ¿Cuál es la incidencia del daño en la muestra, en porcentaje?", "8*100//50", "Se divide las plantas con daño entre las revisadas y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos kilos se esperan en todo el lote sin control?", "20000*10", "Se multiplican los kilos por hectárea por las hectáreas.", " kg"),
        ("=", "{F} ¿Cuántos pesos de ingreso se esperan en todo el lote sin pérdidas?", "20000*10*200", "Se multiplican los kilos del lote por el precio de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuánto dinero se perdería en el lote si no se controla la plaga?", "20000*10*200*10//100", "Se calcula el 10 % del ingreso del lote.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta el control en todo el lote?", "150000*10", "Se multiplica el costo por hectárea por las hectáreas.", " pesos"),
        ("=", "{F} Si el control evita toda la pérdida, ¿cuántos pesos a favor deja respecto de su costo?", "20000*10*200*10//100-150000*10", "Se resta el costo del control a la pérdida evitada.", " pesos"),
        ("abc", "{F} Con esos números, ¿conviene económicamente el control?", "Sí, porque la pérdida evitada es mayor que su costo", "No, porque el control es muy caro", "No se puede saber sin aplicar el producto", "Ahorra 4.000.000 pesos frente a un costo de 1.500.000."),
        ("abc", "{F} Un jefe de campo propone cosechar antes de cumplir la carencia «para que el control convenga». ¿Qué corresponde?", "Rechazarlo: la carencia se respeta siempre, aunque cambie el cálculo económico", "Aceptarlo, porque el dinero es lo principal", "Aceptarlo, si nadie lo revisa", "El ahorro no justifica un riesgo para la salud de los consumidores."),
        ("abc", "{F} El asesor dice que el control no se justifica si la incidencia es baja. ¿Qué dato de la ficha usa para esa decisión?", "La incidencia de 16 % en la muestra, comparada con el umbral", "El precio de venta del kilo", "El número de hectáreas", "La incidencia mide el daño y se compara con el umbral."),
        ("abc", "En Agropecuaria: ¿por qué el criterio económico no es el único que se usa para decidir un control?", "Porque también hay que cuidar la salud, el ambiente y el destino de la producción", "Porque el dinero no importa", "Porque los números son siempre falsos", "La seguridad y el ambiente se consideran junto con el costo."),
    ],
    ctx=("abc", "Un conocido te pregunta si le conviene controlar la plaga de su campo y te da solo el costo del producto. ¿Qué respondes?", "Que faltan la pérdida esperada y la incidencia, y que la decisión la toma un asesor", "Que sí, siempre", "Que no, nunca", "Sin pérdida estimada ni incidencia no se puede comparar."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula la incidencia?", "Plantas con daño entre plantas revisadas, por 100", "La incidencia es un porcentaje de la muestra."),
        ("En el trabajo agrícola: ¿qué se compara en el umbral económico?", "El costo del control y la pérdida evitada", "Se decide si lo que se salva supera lo que se gasta."),
        ("En Agropecuaria: ¿qué plazo se respeta aunque cambie el cálculo económico?", "La carencia", "La carencia protege la salud y no se negocia."),
    ],
    op=("Datos de ejemplo del «Huerto Demo 4»: 5 hectáreas; 10.000 kg por hectárea; precio $100 el kilo; pérdida sin control del 20 %; control de $100.000 por hectárea; muestra de 20 plantas con 5 dañadas. Escribe (a) la incidencia, (b) el ingreso del lote, (c) la pérdida que se evitaría, (d) si conviene el control y qué plazo de seguridad se respeta.",
        "(a) 5 × 100 ÷ 20 = 25 %. (b) 10.000 × 5 × 100 = $5.000.000. (c) 20 % de 5.000.000 = $1.000.000. (d) El control cuesta $500.000, menos que la pérdida evitada; conviene. Se respeta la carencia.",
        ["calcula la incidencia", "calcula el ingreso", "calcula la pérdida evitada", "compara y menciona la carencia"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar por el precio", "comparar con la producción total", "saltarse la carencia"],
        "Pregunta: «¿qué porcentaje del ingreso se pierde sin control?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Calcula la incidencia en una muestra inventada de 25 plantas con 5 dañadas.",
    extend="Explica con un ejemplo por qué un control puede convenir económicamente y aun así no ser la mejor opción.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 5 (comparación y control de ejemplo, inventada). Para una plaga del «Huerto Demo» el asesor compara tres métodos con puntaje de ejemplo de 1 a 5 (5 es lo mejor). "
     "Cultural: efecto 2, seguridad para personas 5, cuidado del ambiente 5. Biológico: efecto 3, seguridad 5, ambiente 5. Químico: efecto 5, seguridad 2, ambiente 2. "
     "Control del registro de aplicaciones: se revisaron 8 puntos de ejemplo (fecha, producto, lote, responsable, carencia, reingreso, firma y receta) y 6 estaban completos.")
build(
    O6, 5, F,
    use="Aprenderé a comparar métodos de control con varios criterios y a verificar la calidad de un registro de aplicaciones, sin aplicar ningún producto.",
    prior=["Sé calcular promedios y porcentajes.", "Sé qué métodos de control existen.", "Sé qué es un registro de aplicaciones."],
    explain=[
        "Al comparar métodos de control se consideran varios criterios: qué tan bien controlan la plaga, qué tan seguros son para las personas y qué tan cuidadosos son con el ambiente. Un método puede ser muy efectivo y a la vez riesgoso; otro puede ser lento y muy seguro. Se suman los puntajes y se miran los criterios de seguridad: si un método tiene un valor muy bajo en seguridad, solo se elige con aplicador autorizado y receta, o se descarta.",
        "La calidad del registro de aplicaciones se verifica con una lista de puntos: fecha, producto, lote, responsable, carencia, reingreso, firma y receta del asesor. Cada punto se marca completo o incompleto; el porcentaje de cumplimiento es los completos entre el total, por 100. Un punto incompleto se corrige por quien corresponde, sin inventar el dato.",
        f"Los puntajes son de ejemplo: los reales los define el asesor con el cultivo y el destino. {EMER} {AVISO}",
    ],
    vocab=[("efecto", "qué tan bien controla el método la plaga"), ("puntaje", "número que mide qué tan bien cumple un método un criterio"), ("criterio de seguridad", "criterio que mide el riesgo para las personas"), ("cumplimiento", "porcentaje de puntos completos de una lista"), ("registro de aplicaciones", "documento que anota fecha, producto, lote y responsable de cada aplicación")],
    worked=[
        ("Sumar puntajes", "Un método de ejemplo obtiene 4 en efecto, 3 en seguridad y 5 en ambiente. ¿Cuál es su total?", ["Se suman los tres puntajes.", "4 más 3 más 5."], "12 puntos"),
        ("Cumplimiento", "En un registro de ejemplo se revisaron 5 puntos y 4 estaban completos. ¿Cuál es el cumplimiento?", ["4 de 5 es 4 quintos.", "4 quintos son 80 de cada 100."], "80 %"),
    ],
    mistakes=[("Elegir el método de mayor efecto sin mirar la seguridad.", "Un buen efecto no compensa un riesgo alto para las personas.", "Se revisan todos los criterios, en especial la seguridad."),
              ("Completar un punto faltante del registro con un dato inventado.", "Se falsea el registro.", "Se informa que falta y lo completa quien tiene el dato real.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué mide el criterio de seguridad al comparar métodos de control?", "El riesgo para las personas", "El precio del producto", "El tamaño de la plaga", "La seguridad mide el riesgo para quienes trabajan o consumen."),
        ("abc", "En Agropecuaria: ¿qué indica un registro de aplicaciones completo?", "Que tiene todos sus datos: fecha, producto, lote, responsable y plazos", "Que la plaga desapareció", "Que el producto fue barato", "Un registro completo permite verificar lo realizado."),
        ("abc", "En Agropecuaria: ¿qué hacer con un punto incompleto del registro?", "Informar que falta y completarlo con el dato real", "Inventar un dato parecido", "Borrar la línea completa", "Un registro se completa solo con datos reales."),
        ("=", "{F} ¿Cuál es el total de puntaje del método cultural?", "2+5+5", "Se suman sus puntajes de efecto, seguridad y ambiente.", " puntos"),
        ("=", "{F} ¿Cuál es el total de puntaje del método biológico?", "3+5+5", "Se suman sus puntajes de efecto, seguridad y ambiente.", " puntos"),
        ("=", "{F} ¿Cuál es el total de puntaje del método químico?", "5+2+2", "Se suman sus puntajes de efecto, seguridad y ambiente.", " puntos"),
        ("abc", "{F} ¿Qué método tiene el mayor puntaje total?", "Biológico", "Químico", "Cultural", "El biológico suma 13, más que el cultural con 12 y el químico con 9."),
        ("abc", "{F} ¿Qué método tiene el mayor efecto de control?", "Químico", "Cultural", "Biológico", "El químico tiene efecto 5, el más alto."),
        ("abc", "{F} Un compañero dice: «el químico es el mejor porque tiene el mayor efecto». ¿Qué respuesta es correcta?", "Es incompleto: tiene seguridad y ambiente bajos, y su total es el menor", "Es correcto, porque el efecto es lo único que importa", "Es correcto, si se usa con mascarilla", "Se comparan todos los criterios; el químico suma menos puntos."),
        ("=", "{F} ¿Qué porcentaje del registro de aplicaciones estaba completo?", "6*100//8", "Se dividen los puntos completos entre el total de puntos y se multiplica por 100.", " %"),
        ("abc", "{F} El jefe de campo marca como completos los 2 puntos faltantes para llegar a 100 %. ¿Qué corresponde?", "Rechazarlo: se informa lo que falta y se completa solo con el dato real", "Aceptarlo, porque 100 % se ve mejor", "Aceptarlo, si nadie lo revisa", "Marcar completo lo que no lo está falsea el registro."),
        ("abc", "{F} Un lote es de destino orgánico y la ficha incluye el método químico. ¿Qué corresponde?", "Consultar al asesor qué productos están permitidos para ese destino", "Usarlo igual, porque tiene el mayor efecto", "Quitar la palabra orgánico del registro", "El destino orgánico restringe los productos permitidos."),
        ("abc", "En Agropecuaria: ¿por qué un método de menor efecto puede ser una buena opción?", "Porque puede ser más seguro y cuidar el ambiente, y combinarse con otros", "Porque no necesita registro", "Porque elimina toda la plaga", "Un método seguro y combinable puede lograr el control con menos riesgos."),
    ],
    ctx=("abc", "Un conocido te pide que elijas, solo por el puntaje, un método de control para su cultivo y lo apliques mañana. ¿Qué respondes?", "Que el puntaje ayuda a analizar, pero decide un asesor y aplica personal autorizado", "Que aplique el de mayor puntaje sin más consulta", "Que aplique el más barato", "La comparación ordena la decisión, pero no habilita a aplicar ni reemplaza al asesor."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula el cumplimiento de una lista?", "Puntos completos entre el total, por 100", "El porcentaje resume qué parte de la lista está completa."),
        ("En el trabajo agrícola: ¿qué método combina bien con otros y es seguro?", "El biológico", "El biológico tiene puntajes altos de seguridad y ambiente."),
        ("En Agropecuaria: ¿quién completa un dato faltante del registro?", "Quien tiene el dato real", "No se inventan datos en un registro."),
    ],
    op=("Puntajes de ejemplo del «Huerto Demo 5»: método P (efecto 4, seguridad 5, ambiente 5), método Q (efecto 5, seguridad 1, ambiente 2), método R (efecto 3, seguridad 4, ambiente 4). El registro de aplicaciones revisó 10 puntos y 7 estaban completos. Escribe (a) el total de cada método, (b) cuál tiene el mayor total, (c) el porcentaje de cumplimiento del registro, (d) qué haces con los puntos incompletos.",
        "(a) P: 4 + 5 + 5 = 14; Q: 5 + 1 + 2 = 8; R: 3 + 4 + 4 = 11. (b) P. (c) 7 × 100 ÷ 10 = 70 %. (d) Informo lo que falta y lo completa quien tiene el dato real; no invento datos.",
        ["suma bien los totales", "elige el mayor", "calcula el cumplimiento", "no inventa datos"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal", "elegir por efecto solamente", "completar con datos inventados"],
        "Pregunta: «¿qué método suma más puntos?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Crea una matriz con dos métodos y tres criterios inventados, suma los totales y elige uno.",
    extend="Explica con un ejemplo por qué un registro incompleto dificulta la trazabilidad de un lote.",
)

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Predio Demo» lleva sus registros en un cuaderno de campo de papel y en una planilla de un computador compartido. El cuaderno tiene 120 páginas. "
     "Peligros y problemas anotados: se usa el celular caminando entre las hileras o cerca de maquinaria; el cuaderno se moja y se ensucia en el campo; la planilla tiene una sola clave que conocen todos; y en ella están los datos personales de los trabajadores, sin protección.")
build(
    O7, 1, F,
    use="Aprenderé qué es un registro productivo, por qué se llevan registros manuales y digitales, qué riesgos tiene registrar en terreno y cómo se protegen los datos.",
    prior=["Sé leer una ficha escrita.", "Sé que un registro anota lo que ocurrió.", "Sé dividir números enteros."],
    explain=[
        "Un registro productivo es un documento donde se anotan los manejos y la producción de un predio: qué labor se hizo, cuándo, dónde, con qué insumo y quién la hizo. Puede ser manual, como un cuaderno de campo, o digital, como una planilla en un computador. Sirve para el control de gestión, es decir, para saber cuánto cuesta y cuánto produce cada parte del predio, y para la trazabilidad, que es poder seguir la historia de un producto. Muchos compradores y normas exigen registros en un formato establecido.",
        "Registrar tiene riesgos. Usar el celular mientras se camina o se está cerca de maquinaria distrae y puede causar un accidente: el registro se hace en un lugar seguro y con la atención completa. Un cuaderno mojado pierde datos, y una planilla sin respaldo, es decir, sin copia en otro lugar, también. Los datos personales de las personas, como nombre o sueldo, se protegen: se comparten solo con quien corresponde, con claves individuales.",
        f"Una clave compartida es un riesgo; una clave propia, un control administrativo; y una copia de respaldo en otro lugar, un control de ingeniería. Un registro no se altera para que «se vea mejor». {EMER} {AVISO}",
    ],
    vocab=[("registro productivo", "documento donde se anotan los manejos y la producción del predio"), ("cuaderno de campo", "cuaderno donde se anotan a mano los manejos en terreno"), ("planilla", "tabla digital con filas y columnas para anotar datos"), ("control de gestión", "uso de los datos para saber cuánto cuesta y produce cada parte"), ("trazabilidad", "posibilidad de seguir la historia de un producto"), ("respaldo", "copia de los datos en otro lugar"), ("datos personales", "datos que identifican a una persona, como su nombre o su sueldo")],
    worked=[
        ("Elegir manual o digital", "Un encargado de ejemplo anota a mano en el campo y luego pasa los datos a una planilla. ¿El cuaderno es registro manual o digital?", ["Se escribe a mano en papel.", "Eso es un registro manual."], "Manual"),
        ("Clasificar un control", "Un predio de ejemplo guarda cada semana una copia de su planilla en otro computador. ¿Qué es esa copia?", ["Es una copia de los datos en otro lugar.", "Esa copia se llama respaldo."], "Un respaldo"),
    ],
    mistakes=[("Creer que anotar con el celular mientras se opera una máquina ahorra tiempo.", "La distracción puede causar un accidente.", "Se registra en un lugar seguro y sin operar nada."),
              ("Creer que compartir la clave con todos es práctico y seguro.", "Si todos usan una clave no se sabe quién cambió un dato, y los datos personales quedan expuestos.", "Cada persona usa su clave, y los datos personales se protegen.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es un registro productivo?", "Un documento donde se anotan los manejos y la producción del predio", "Un contrato de venta de un producto", "Un mapa de las rutas del campo", "El registro anota lo realizado y lo producido; el contrato y el mapa son otros documentos."),
        ("abc", "En Agropecuaria: ¿qué es la trazabilidad?", "La posibilidad de seguir la historia de un producto", "La velocidad con que se cosecha", "El precio de venta de la cosecha", "La trazabilidad permite saber de dónde viene y qué manejo tuvo un producto."),
        ("abc", "En Agropecuaria: ¿qué es un respaldo de datos?", "Una copia de los datos guardada en otro lugar", "Un cuaderno nuevo y vacío", "Una clave compartida por todos", "El respaldo evita perder datos si falla el original."),
        ("=", "{F} Si se usan 4 páginas del cuaderno por semana, ¿para cuántas semanas alcanza un cuaderno de 120 páginas?", "120//4", "Se divide el total de páginas entre las que se usan por semana.", " semanas"),
        ("abc", "{F} Una copia de la planilla guardada cada semana en otro lugar es un control de tipo:", "De ingeniería, porque protege los datos aunque falle el equipo", "Administrativo, porque es una regla escrita", "De EPP, porque protege a la persona", "El respaldo actúa aunque nadie se acuerde de otra cosa."),
        ("abc", "{F} Dar a cada persona una clave propia para la planilla es un control de tipo:", "Administrativo, porque ordena el acceso", "De ingeniería, porque cambia la planilla", "De EPP, porque protege al trabajador", "Las claves propias son una regla de acceso que permite saber quién cambió un dato."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a usar el celular entre las hileras cerca de maquinaria?", "Que la distracción cause un accidente", "El celular mismo", "Que el celular se quede sin memoria", "El riesgo es la posibilidad de accidente por distracción."),
        ("abc", "{F} Una compañera dice: «puedo anotar con el celular mientras me subo al tractor, es rápido». ¿Qué respuesta es correcta?", "Es peligroso: se registra en un lugar seguro y no se maneja con el celular", "Es correcto, si va despacio", "Es correcto, si usa auriculares", "La atención al manejar es indispensable; la velocidad o los auriculares no lo corrigen."),
        ("abc", "{F} Una persona queda atrapada en una máquina del predio mientras otra anotaba en su celular. ¿Qué corresponde?", "No acercarte a la máquina, avisar a un adulto responsable y a emergencias", "Intentar apagar la máquina tú", "Seguir registrando para tener el dato", "Acercarse sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "En Agropecuaria: ¿por qué conviene que cada persona tenga su clave?", "Porque se sabe quién cambió un dato y se protegen los datos personales", "Porque así se escribe más rápido", "Porque la planilla ocupa menos espacio", "La clave propia da responsabilidad y privacidad."),
        ("abc", "{F} Se propone solo pedir que las personas no usen el celular entre las hileras. ¿Qué medida es más efectiva?", "Destinar un lugar seguro para registrar, fuera del paso de máquinas", "Poner un recordatorio escrito en el celular", "Pedir que se anote más rápido", "Cambiar el lugar actúa sobre el peligro, más arriba que una regla."),
        ("=", "{F} Se reciben 3 registros nuevos por día en la planilla. ¿Cuántos registros hay después de 20 días?", "3*20", "Se multiplican los registros diarios por los días.", " registros"),
        ("abc", "En Agropecuaria: ¿por qué los datos personales de los trabajadores en la planilla deben protegerse?", "Porque identifican a las personas y no deben ser vistos por quien no corresponde", "Porque ocupan mucho espacio", "Porque son datos de la cosecha", "La privacidad de las personas es un deber de quien guarda sus datos."),
    ],
    ctx=("abc", "Un amigo te pide que le pases la planilla de su predio con los sueldos de los trabajadores «para mostrársela a un conocido». ¿Qué respondes?", "Que no, porque los datos personales se protegen, y que lo consultarás con un adulto responsable", "Que sí, si es un conocido", "Que sí, borrando solo los nombres", "Los datos personales no se comparten sin autorización; quitar los nombres no basta si hay otros datos."),
    sc=[
        ("En Agropecuaria: ¿qué es un registro manual?", "Uno que se anota a mano, como en un cuaderno de campo", "El registro manual se escribe en papel."),
        ("En el trabajo agrícola: ¿se registra con el celular al operar una máquina?", "No, porque la distracción puede causar un accidente", "Operar una máquina exige atención completa."),
        ("En Agropecuaria: ¿para qué sirve el respaldo?", "Para no perder los datos si falla el original", "El respaldo guarda una copia en otro lugar."),
    ],
    op=("El «Predio Demo 2» anota una tarea de ejemplo: un encargado anota los riegos en el celular mientras camina por una acequia sin tapa, y guarda la planilla sin copia en un computador con una clave que usan 5 personas. Escribe (a) el peligro de la acequia y su riesgo al registrar así, (b) un control administrativo para el registro, (c) un control de ingeniería para los datos, (d) qué haces si alguien cae a la acequia.",
        "(a) Peligro: la acequia sin tapa; riesgo: que el encargado se distraiga con el celular, caiga y se lastime. (b) Una clave propia para cada persona y una regla de registrar en un lugar seguro. (c) Una copia de respaldo en otro lugar. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer meterse a la acequia", "no mencionar el respaldo"],
        "Pregunta: «¿qué protege tus datos aunque falle el computador?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe una lista de cuatro datos que debería tener un registro de riego y di cuál de ellos identifica a una persona.",
    extend="Explica con un ejemplo por qué un registro digital sin respaldo puede ser más frágil que uno en papel.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (formato de ejemplo, inventado). Formato establecido de registro de labores del «Predio Demo», con columnas: fecha, potrero, labor, insumo, cantidad, unidad, responsable. "
     "Filas de ejemplo: (1) 12 de marzo, Potrero 2, siembra, semilla de maíz, 40, kg, Persona A; (2) 15 de marzo, Potrero 2, riego, agua, 200, m³, Persona B; (3) 20 de marzo, Potrero 3, siembra, semilla de maíz, 35, kg, Persona A. "
     "Registro de producción: Potrero 2, 4 hectáreas, 40.000 kg cosechados.")
build(
    O7, 2, F,
    use="Aprenderé qué datos mínimos debe tener un registro, cómo se lee un formato establecido, qué es el rendimiento y qué rol cumple cada persona en los registros.",
    prior=["Sé qué es un registro productivo.", "Sé leer una tabla de datos.", "Sé sumar, multiplicar y dividir enteros."],
    explain=[
        "Un formato establecido es la forma fija en que se registra: sus columnas, su orden y sus unidades. Un registro de labores bien hecho tiene siempre fecha, lugar, labor, insumo, cantidad con su unidad y responsable. La unidad es parte del dato: 40 sin unidad no dice si son kilos, litros o sacos. Si el formato cambia cada vez, los registros no se pueden comparar ni sumar.",
        "El rendimiento es lo que produce una superficie: se calcula dividiendo los kilos cosechados por las hectáreas. Sirve para comparar potreros. En una planilla, cada fila es un registro y cada columna un tipo de dato; una fórmula suma o calcula automáticamente con las celdas. El encargado de registros anota, el jefe de campo revisa que sean verdaderos y el administrador usa los datos para decidir y controlar costos.",
        f"Un registro se completa con datos reales; si falta uno, se informa. Una corrección se hace dejando visible el dato anterior y quién corrigió. {EMER} {AVISO}",
    ],
    vocab=[("formato establecido", "forma fija de registrar, con columnas, orden y unidades"), ("unidad", "medida con la que se expresa una cantidad, como kg o m³"), ("rendimiento", "kilos cosechados por hectárea"), ("fila", "línea horizontal de una planilla, que contiene un registro"), ("columna", "línea vertical de una planilla, que contiene un tipo de dato"), ("fórmula", "instrucción de una celda que calcula con otros datos")],
    worked=[
        ("Calcular el rendimiento", "Un potrero de ejemplo de 5 hectáreas produjo 30.000 kg. ¿Cuál es su rendimiento?", ["Se divide la producción entre las hectáreas.", "30.000 entre 5 es 6.000."], "6.000 kg por hectárea"),
        ("Dato incompleto", "Una fila de ejemplo dice «siembra, semilla, 50». ¿Qué le falta?", ["50 no dice si son kilos o sacos.", "También faltan la fecha y el responsable."], "La unidad, la fecha y el responsable"),
    ],
    mistakes=[("Anotar una cantidad sin unidad porque «todos saben cuál es».", "La unidad puede cambiar entre personas y predios.", "La unidad es parte del dato."),
              ("Cambiar el formato del registro cada temporada.", "Los datos dejan de ser comparables.", "Se mantiene el formato establecido, salvo que lo cambie quien corresponde.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la unidad de un dato en un registro?", "La medida con la que se expresa una cantidad, como kg o m³", "El nombre de la persona que lo anotó", "La fecha en que se anotó", "La unidad dice cómo se mide la cantidad."),
        ("abc", "En Agropecuaria: ¿qué es el rendimiento de un cultivo?", "Los kilos cosechados por hectárea", "Los kilos de insumo usados", "El precio por kilo del cultivo", "El rendimiento relaciona producción y superficie."),
        ("abc", "En Agropecuaria: ¿qué es una columna de una planilla?", "La línea vertical que contiene un tipo de dato", "La línea horizontal que contiene un registro", "La clave de acceso al archivo", "La columna contiene un tipo de dato; la fila, un registro."),
        ("=", "{F} ¿Cuántos kilos de semilla de maíz se anotaron en total en las dos siembras del registro?", "40+35", "Se suman las cantidades de las dos filas de siembra.", " kg"),
        ("=", "{F} ¿Cuál es el rendimiento del Potrero 2, en kilos por hectárea?", "40000//4", "Se divide los kilos cosechados entre las hectáreas.", " kg por hectárea"),
        ("abc", "{F} ¿Qué dato de la fila 2 indica la medida del agua?", "La unidad m³", "El potrero", "La fecha", "La unidad m³ expresa la medida de la cantidad de agua."),
        ("abc", "{F} ¿Quién aparece como responsable de las dos siembras?", "Persona A", "Persona B", "El jefe de campo", "La ficha anota a la Persona A en las filas 1 y 3."),
        ("abc", "{F} ¿Qué rol revisa que los registros sean verdaderos?", "El jefe de campo", "El encargado de las semillas", "El comprador", "El jefe de campo revisa que los registros reflejen lo realizado."),
        ("abc", "{F} Una compañera propone anotar en la fila 2 solo «200», sin unidad, «porque se entiende». ¿Qué respuesta es correcta?", "Es incorrecto: la unidad es parte del dato", "Es correcto, si todos lo saben", "Es correcto, si es agua", "Sin unidad, 200 puede ser litros, m³ o sacos."),
        ("abc", "{F} El encargado nota que anotó 400 kg en vez de 40 en la fila 1 y quiere borrarla. ¿Qué corresponde?", "Corregir dejando visible el dato anterior y quién corrigió", "Borrar la fila sin dejar rastro", "Dejar el error para no complicarse", "Una corrección transparente conserva la trazabilidad."),
        ("=", "{F} Si el Potrero 3 tiene 5 hectáreas y produjo 45.000 kg, ¿cuántos kilos por hectárea rindió?", "45000//5", "Se divide la producción entre las hectáreas del potrero.", " kg por hectárea"),
        ("abc", "{F} Entre el Potrero 2 con 10.000 kg por hectárea y el Potrero 3 con 9.000 kg por hectárea, ¿cuál rindió más?", "El Potrero 2", "El Potrero 3", "Rindieron igual", "El valor de 10.000 kg por hectárea es mayor que 9.000."),
        ("abc", "En Agropecuaria: ¿por qué conviene mantener un formato fijo de registro?", "Para que los datos sean comparables y se puedan sumar", "Para que los registros sean más cortos", "Para evitar anotar fechas", "Un formato estable permite comparar entre fechas y potreros."),
    ],
    ctx=("abc", "Una conocida te muestra un registro con cantidades sin unidades y te pide que le calcules el total. ¿Qué respondes?", "Que no se puede sumar sin saber las unidades y que debe completarlas quien anotó", "Que sume los números igual", "Que invente la unidad más común", "Sumar cantidades con unidades distintas o desconocidas da un resultado sin sentido."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula el rendimiento?", "Kilos cosechados entre hectáreas", "El rendimiento es la producción por unidad de superficie."),
        ("En el trabajo agrícola: ¿qué datos mínimos tiene un registro de labores?", "Fecha, lugar, labor, insumo, cantidad con unidad y responsable", "Esos datos permiten ubicar y verificar lo realizado."),
        ("En Agropecuaria: ¿cómo se corrige un registro?", "Dejando visible el dato anterior y quién corrigió", "La corrección transparente mantiene la trazabilidad."),
    ],
    op=("Formato del «Predio Demo 3» con las mismas columnas. Filas de ejemplo: (1) 5 de abril, Potrero 4, cosecha, —, 18.000, kg, Persona C; (2) 8 de abril, Potrero 4, cosecha, —, 12.000, kg, Persona C. El Potrero 4 mide 6 hectáreas. Escribe (a) cuántos kilos se cosecharon en total, (b) el rendimiento del potrero, (c) qué rol revisa los registros, (d) qué haces si ves que falta la unidad en una fila.",
        "(a) 18.000 + 12.000 = 30.000 kg. (b) 30.000 ÷ 6 = 5.000 kg por hectárea. (c) El jefe de campo. (d) Informo a quien anotó para que complete la unidad real, sin inventarla.",
        ["suma los kilos", "calcula el rendimiento", "nombra el rol", "no inventa la unidad"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre las filas en vez de las hectáreas", "inventar la unidad"],
        "Pregunta: «¿entre qué número divides los kilos para el rendimiento?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Calcula el rendimiento de un potrero inventado de 3 hectáreas que produjo 21.000 kg.",
    extend="Explica con un ejemplo por qué una cantidad sin unidad puede llevar a un error de cálculo.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (registro con errores de ejemplo, inventado). Extracto de un registro del «Predio Demo»: "
     "(a) 31 de febrero, Potrero 1, riego, agua, 150, m³, Persona A; (b) 3 de marzo, Potrero 1, siembra, semilla de maíz, 40, —, Persona B; (c) 5 de marzo, Potrero 2, cosecha, maíz, 4.000, kg, Persona C; "
     "(d) 5 de marzo, Potrero 2, cosecha, maíz, 4.000, kg, Persona C (idéntica a la anterior); (e) 9 de marzo, Potrero 3, riego, agua, 160, m³, sin responsable. Se sabe que el Potrero 2 produjo en total 4.000 kg esa semana.")
build(
    O7, 3, F,
    use="Aprenderé a analizar un registro con errores en papel, a identificar fechas imposibles, unidades faltantes, filas repetidas y responsables sin anotar, y a decidir cómo se corrigen sin alterar la verdad.",
    prior=["Sé qué datos mínimos tiene un registro.", "Sé qué es el formato establecido.", "Sé leer una tabla de datos."],
    explain=[
        "Analizar un registro es revisarlo fila por fila buscando errores comunes: fechas imposibles, como un 31 de febrero; datos sin unidad; filas duplicadas, que cuentan dos veces lo mismo; responsables sin anotar; y cantidades fuera de lo esperable. Cada error tiene un efecto: una fila duplicada hace que la producción aparezca el doble de grande, y una fecha imposible quita valor al documento.",
        "Corregir no es borrar. En un registro manual se tacha con una sola línea el dato errado, se escribe el correcto al lado, se anota la fecha y se firma. En una planilla se conserva el historial de cambios o se anota la corrección en una columna aparte. Si no se sabe el dato correcto, no se inventa: se pregunta a quien anotó. El jefe de campo aprueba las correcciones.",
        f"Un buen análisis nombra cada error, su efecto y su corrección, sin alterar los datos reales. {EMER} {AVISO}",
    ],
    vocab=[("fila duplicada", "fila idéntica que cuenta dos veces lo mismo"), ("fecha imposible", "fecha que no existe en el calendario"), ("corrección", "cambio de un dato errado dejando visible el dato anterior"), ("historial de cambios", "registro de qué se cambió y quién lo hizo"), ("verificar", "comprobar que un dato es verdadero")],
    worked=[
        ("Detectar un duplicado", "En un registro de ejemplo aparecen dos filas idénticas de cosecha de 2.000 kg. Si solo hubo una cosecha, ¿cuántos kilos aparecen de más?", ["La fila repetida cuenta dos veces.", "La cosecha real es 2.000 kg, no 4.000."], "2.000 kg de más"),
        ("Corregir a mano", "Un encargado de ejemplo anotó 50 en vez de 30. ¿Cómo corrige en un cuaderno?", ["Se tacha con una línea el dato errado.", "Se escribe 30 al lado, con fecha y firma."], "Tachar con una línea, escribir 30, fechar y firmar"),
    ],
    mistakes=[("Borrar con corrector la fila errada para que se vea limpia.", "Se pierde la evidencia del error y no se sabe qué se cambió.", "Se tacha con una línea, se corrige al lado y se firma."),
              ("Eliminar una fila repetida sin consultar.", "Podría ser un registro verdadero y no un duplicado.", "Se consulta a quien anotó y al jefe de campo antes de corregir.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es una fila duplicada en un registro?", "Una fila idéntica que cuenta dos veces lo mismo", "Una fila con un dato de más de dos cifras", "Una fila con el nombre de dos personas", "El duplicado repite un mismo hecho y lo cuenta doble."),
        ("abc", "En Agropecuaria: ¿qué es una fecha imposible?", "Una fecha que no existe en el calendario", "Una fecha muy antigua", "Una fecha futura", "Una fecha imposible no existe, como un 31 de febrero."),
        ("abc", "En Agropecuaria: ¿cómo se corrige un dato en un cuaderno de campo?", "Se tacha con una línea, se escribe el correcto y se firma", "Se borra con corrector y se escribe encima", "Se arranca la página", "La corrección debe dejar visible el dato anterior."),
        ("abc", "{F} ¿Qué fila tiene una fecha imposible?", "La fila (a), 31 de febrero", "La fila (b), 3 de marzo", "La fila (c), 5 de marzo", "El 31 de febrero no existe."),
        ("abc", "{F} ¿Qué fila no tiene unidad en la cantidad?", "La fila (b), con 40 sin unidad", "La fila (a), con m³", "La fila (c), con kg", "Solo la fila (b) tiene la unidad faltante."),
        ("abc", "{F} ¿Qué filas parecen una duplicada?", "Las filas (c) y (d)", "Las filas (a) y (b)", "Las filas (b) y (e)", "Son idénticas en todos sus datos."),
        ("abc", "{F} ¿Qué fila no tiene responsable?", "La fila (e)", "La fila (a)", "La fila (c)", "La ficha dice «sin responsable» solo en la fila (e)."),
        ("=", "{F} Si se suman las filas (c) y (d) tal como están, ¿cuántos kilos aparecen cosechados en el Potrero 2?", "4000+4000", "Se suman las cantidades de las dos filas idénticas.", " kg"),
        ("=", "{F} ¿Cuántos kilos aparecen de más por la fila duplicada, sabiendo que el Potrero 2 produjo en total 4.000 kg esa semana?", "4000+4000-4000", "Se resta la producción real a la suma de las dos filas.", " kg"),
        ("abc", "{F} El jefe de campo pide eliminar la fila (d) sin consultar. ¿Qué corresponde?", "Consultar a la Persona C antes de corregir y dejar constancia", "Eliminarla sin dejar rastro", "Cambiar la fecha de (d)", "Podría ser un dato verdadero; se consulta y se corrige con constancia."),
        ("abc", "{F} Un encargado quiere completar la fecha de la fila (a) con «28 de febrero» porque «seguro era ese día». ¿Qué corresponde?", "Preguntar a quien anotó la fecha real y corregir con constancia", "Poner 28 de febrero igual", "Borrar la fila entera", "Una fecha no se supone: se verifica con quien registró."),
        ("abc", "{F} Una compañera dice: «la fila (e) no necesita responsable porque se entiende quién fue». ¿Qué respuesta es correcta?", "Es incorrecto: el responsable es parte del dato y permite verificar", "Es correcto, si todos conocen el predio", "Es correcto, si el riego fue corto", "El responsable permite saber a quién consultar."),
        ("abc", "En Agropecuaria: ¿por qué una fila duplicada puede llevar a decisiones equivocadas?", "Porque hace parecer que se produjo el doble de lo real", "Porque ocupa más espacio en la hoja", "Porque obliga a cambiar el formato", "Contar dos veces un dato distorsiona los indicadores."),
    ],
    ctx=("abc", "Un conocido te muestra un registro con una fecha imposible y te pide que la cambies por «cualquier fecha parecida». ¿Qué respondes?", "Que no se inventa, que la fecha real se consulta con quien anotó, y que lo informarás a un adulto responsable", "Que sí, si es parecida", "Que sí, si nadie lo revisa", "Una fecha inventada falsea el registro."),
    sc=[
        ("En Agropecuaria: ¿qué efecto tiene una fila duplicada?", "Hace aparecer la producción más grande de lo real", "El duplicado cuenta dos veces lo mismo."),
        ("En el trabajo agrícola: ¿qué se hace si no se sabe el dato correcto?", "Se pregunta a quien anotó, sin inventar", "Un dato inventado falsea el registro."),
        ("En Agropecuaria: ¿quién aprueba las correcciones de un registro?", "El jefe de campo", "El jefe de campo revisa que el registro sea verdadero."),
    ],
    op=("Extracto de ejemplo del «Predio Demo 4»: (a) 10 de mayo, Potrero 1, riego, agua, 90, m³, Persona A; (b) 10 de mayo, Potrero 1, riego, agua, 90, m³, Persona A (idéntica); (c) 30 de febrero, Potrero 2, siembra, semilla, 25, kg, Persona B; (d) 12 de mayo, Potrero 3, riego, agua, 70, —, Persona C. Solo hubo un riego de 90 m³ en el Potrero 1. Escribe (a) cuántos m³ aparecen de más, (b) qué fila tiene fecha imposible, (c) qué fila no tiene unidad, (d) cómo corriges un dato a mano.",
        "(a) 90 + 90 − 90 = 90 m³ de más. (b) La fila (c). (c) La fila (d). (d) Tacho con una línea el dato errado, escribo el correcto al lado, anoto la fecha y firmo, con aprobación del jefe de campo.",
        ["calcula lo de más", "ubica la fecha imposible", "ubica la unidad faltante", "describe la corrección"],
        ["hoja con las cuatro respuestas"],
        ["borrar sin dejar rastro", "inventar la fecha o la unidad"],
        "Pregunta: «¿qué fila es idéntica a otra?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Escribe una fila de registro con tres errores inventados y luego escríbela corregida.",
    extend="Explica con un ejemplo por qué es mejor dejar visible el dato antiguo cuando se corrige.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Registros de dos potreros de maíz del «Predio Demo». Potrero 1: 4 hectáreas, 40.000 kg cosechados, costo total $2.000.000. Potrero 2: 5 hectáreas, 40.000 kg cosechados, costo total $3.000.000. "
     "Precio de venta de ejemplo: $150 por kilo.")
build(
    O7, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular rendimiento, costo por hectárea, costo por kilo, ingreso y margen a partir de registros.",
    prior=["Sé calcular el rendimiento.", "Sé multiplicar y dividir enteros.", "Sé leer una tabla de datos."],
    explain=[
        "El control de gestión usa los registros para calcular indicadores. El rendimiento es kilos entre hectáreas. El costo por hectárea es el costo total entre las hectáreas. El costo por kilo es el costo total entre los kilos cosechados. El ingreso es kilos por el precio, y el margen es el ingreso menos el costo. Con estos números se compara entre potreros, temporadas o manejos.",
        "Un indicador solo es confiable si los registros lo son: si faltan unidades, hay filas duplicadas o los datos son inventados, los resultados no sirven. Por eso se calcula con datos verificados. Ningún indicador explica por sí solo la causa de una diferencia: dos potreros con distinto rendimiento pueden diferir por el suelo, el riego, la sanidad o el manejo, y eso lo estudia el asesor.",
        f"Los números son de ejemplo; los reales dependen del predio y del mercado. {EMER} {AVISO}",
    ],
    vocab=[("costo por hectárea", "costo total entre las hectáreas"), ("costo por kilo", "costo total entre los kilos cosechados"), ("ingreso", "kilos vendidos por el precio de cada kilo"), ("margen", "ingreso menos costo"), ("indicador", "número que resume cómo va un proceso"), ("verificado", "comprobado como verdadero")],
    worked=[
        ("Costo por hectárea", "Un potrero de ejemplo de 3 hectáreas costó $900.000. ¿Cuánto costó por hectárea?", ["Se divide el costo total entre las hectáreas.", "900.000 entre 3."], "$300.000"),
        ("Margen", "Con un ingreso de ejemplo de $1.200.000 y un costo de $800.000, ¿cuál es el margen?", ["El margen es el ingreso menos el costo.", "1.200.000 menos 800.000."], "$400.000"),
    ],
    mistakes=[("Comparar el costo total de dos potreros de distinto tamaño.", "El costo total depende de la superficie.", "Se compara el costo por hectárea o por kilo."),
              ("Calcular indicadores con registros que tienen errores.", "Los resultados quedan equivocados.", "Primero se verifican y corrigen los registros.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es el margen de un potrero?", "El ingreso menos el costo", "El costo más el ingreso", "El precio de cada kilo", "El margen es la ganancia después de restar los costos."),
        ("abc", "En Agropecuaria: ¿qué es el costo por kilo?", "El costo total entre los kilos cosechados", "El costo total entre las hectáreas", "El precio de venta de cada kilo", "El costo por kilo relaciona costo y producción."),
        ("abc", "En Agropecuaria: ¿por qué hay que verificar los registros antes de calcular indicadores?", "Porque con errores los resultados salen equivocados", "Porque así se evita usar la calculadora", "Porque los indicadores no necesitan datos", "Datos errados producen indicadores errados y decisiones equivocadas."),
        ("=", "{F} ¿Cuál es el rendimiento del Potrero 1?", "40000//4", "Se divide los kilos cosechados entre las hectáreas.", " kg por hectárea"),
        ("=", "{F} ¿Cuál es el rendimiento del Potrero 2?", "40000//5", "Se divide los kilos cosechados entre las hectáreas.", " kg por hectárea"),
        ("=", "{F} ¿Cuál es el costo por hectárea del Potrero 1?", "2000000//4", "Se divide el costo total entre las hectáreas.", " pesos"),
        ("=", "{F} ¿Cuál es el costo por kilo del Potrero 2?", "3000000//40000", "Se divide el costo total entre los kilos cosechados.", " pesos"),
        ("=", "{F} ¿Cuál es el ingreso del Potrero 1?", "40000*150", "Se multiplican los kilos por el precio de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuál es el margen del Potrero 1?", "40000*150-2000000", "Se resta el costo total al ingreso.", " pesos"),
        ("=", "{F} ¿Cuál es el margen del Potrero 2?", "40000*150-3000000", "Se resta el costo total al ingreso.", " pesos"),
        ("abc", "{F} ¿Qué potrero tuvo mayor margen?", "El Potrero 1", "El Potrero 2", "Ambos tuvieron igual margen", "El Potrero 1 tuvo 4.000.000 y el 2 tuvo 3.000.000."),
        ("abc", "{F} Un encargado concluye que el Potrero 2 es peor «porque costó más en total». ¿Cuál es el error?", "Compara costos totales de superficies distintas en vez de costos por hectárea o por kilo", "Ninguno, porque el costo total es lo importante", "Usar el precio de venta", "Para comparar se normaliza por superficie o por producción."),
        ("abc", "En Agropecuaria: ¿por qué un indicador no explica por sí solo la causa de una diferencia?", "Porque varios factores, como suelo, riego o sanidad, pueden influir", "Porque los indicadores son siempre falsos", "Porque el rendimiento no se puede calcular", "Un indicador muestra una diferencia, pero la causa se estudia con el asesor."),
    ],
    ctx=("abc", "Un conocido te pide que, con solo el costo total de sus dos potreros, le digas cuál manejo es mejor. ¿Qué respondes?", "Que faltan las hectáreas y los kilos, y que la conclusión final la da un asesor", "Que el de menor costo total es mejor", "Que el de mayor costo es mejor", "Sin superficie ni producción no se puede normalizar la comparación."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula el margen?", "Ingreso menos costo", "El margen es lo que queda después de pagar los costos."),
        ("En el trabajo agrícola: ¿qué se verifica antes de calcular indicadores?", "Que los registros sean verdaderos y estén completos", "Los datos errados dan indicadores equivocados."),
        ("En Agropecuaria: ¿cómo se calcula el costo por hectárea?", "Costo total entre hectáreas", "El costo por hectárea permite comparar potreros de distinto tamaño."),
    ],
    op=("Datos de ejemplo del «Predio Demo 5»: Potrero A, 6 hectáreas, 60.000 kg, costo $3.000.000; Potrero B, 3 hectáreas, 24.000 kg, costo $1.800.000; precio $120 por kilo. Escribe (a) el rendimiento de cada potrero, (b) el costo por hectárea de cada uno, (c) el margen de cada uno, (d) por qué no basta con comparar el costo total.",
        "(a) A: 60.000 ÷ 6 = 10.000 kg por hectárea; B: 24.000 ÷ 3 = 8.000. (b) A: 3.000.000 ÷ 6 = $500.000; B: 1.800.000 ÷ 3 = $600.000. (c) A: 60.000 × 120 − 3.000.000 = $4.200.000; B: 24.000 × 120 − 1.800.000 = $1.080.000. (d) Porque los potreros tienen distinta superficie y hay que normalizar.",
        ["calcula rendimientos", "calcula costos por hectárea", "calcula márgenes", "explica por qué normalizar"],
        ["hoja con las cuatro respuestas"],
        ["no dividir entre hectáreas", "restar al revés el margen", "comparar costos totales"],
        "Pregunta: «¿qué superficie tiene cada potrero?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el margen de un potrero inventado con 5.000 kg, precio de $100 por kilo y costo de $200.000.",
    extend="Explica con un ejemplo por qué dos potreros con el mismo rendimiento pueden tener márgenes distintos.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Predio Demo» de 60 hectáreas usa tecnología de precisión: una estación meteorológica en un mástil metálico alto, sensores de humedad enterrados, imágenes de satélite y un dron de ejemplo con baterías de litio. "
     "Peligros anotados: el mástil metálico durante tormentas eléctricas, las hélices y las caídas del dron, baterías que se calientan, cables eléctricos aéreos cerca de un potrero, pozos y zanjas mientras se mira la pantalla, y la ubicación del predio y sus datos expuestos en una nube sin clave.")
build(
    O8, 1, F,
    use="Aprenderé qué es la agricultura de precisión, qué son los sensores, la estación meteorológica, la imagen satelital y el dron, y cuáles son sus peligros y sus normas.",
    prior=["Sé qué es un registro de datos.", "Sé leer una ficha escrita.", "Sé dividir números enteros."],
    explain=[
        "La agricultura de precisión usa tecnología para medir lo que pasa en el predio y manejar cada zona según lo que necesita. Un sensor es un instrumento que mide una variable, como la humedad del suelo. Una estación meteorológica mide temperatura, humedad del aire, viento y lluvia. Una imagen satelital es una fotografía del predio tomada desde un satélite. Un dron es una aeronave sin piloto a bordo, que se maneja a distancia. El sistema de posicionamiento (GPS) ubica un punto del predio en un mapa.",
        "Estos equipos tienen peligros. Un mástil metálico atrae rayos en una tormenta eléctrica; las hélices de un dron pueden herir y un dron puede caer; las baterías de litio pueden calentarse y prenderse fuego; y mirar una pantalla mientras se camina puede llevar a caer en un pozo. Volar un dron exige una persona capacitada y las autorizaciones que exige la norma vigente de la autoridad aeronáutica. Los datos del predio y de las personas se protegen con claves y se comparten solo con quien corresponde.",
        f"Un dato es un valor medido; transmitir es enviarlo a otro lugar, por ejemplo por la red del celular. {EMER} {AVISO}",
    ],
    vocab=[("agricultura de precisión", "manejo de cada zona del predio según los datos que se miden"), ("sensor", "instrumento que mide una variable, como la humedad del suelo"), ("estación meteorológica", "equipo que mide temperatura, humedad del aire, viento y lluvia"), ("imagen satelital", "fotografía del predio tomada desde un satélite"), ("dron", "aeronave sin piloto a bordo, que se maneja a distancia"), ("GPS", "sistema que ubica un punto del predio en un mapa"), ("transmitir", "enviar un dato a otro lugar")],
    worked=[
        ("Identificar el equipo", "Un instrumento de ejemplo mide cuánta agua hay en el suelo y está enterrado en el potrero. ¿Qué es?", ["Mide una variable del suelo.", "Un instrumento que mide una variable es un sensor."], "Un sensor de humedad"),
        ("Clasificar un control", "Un predio de ejemplo cubre con una tapa fija el pozo donde está enterrado un sensor. ¿Qué tipo de control es?", ["La tapa fija cambia físicamente el lugar.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que se puede volar un dron en cualquier lugar si uno sabe manejarlo.", "La norma vigente exige autorizaciones y zonas permitidas.", "El dron lo vuela solo personal capacitado y autorizado."),
              ("Creer que revisar una estación con tormenta es seguro si se usan guantes.", "El mástil atrae rayos y los guantes no protegen.", "No se acerca: se espera a que termine y lo revisa personal autorizado.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la agricultura de precisión?", "Manejar cada zona del predio según los datos que se miden", "Aplicar lo mismo a todo el predio sin medir", "Cultivar solo en invernaderos", "La agricultura de precisión usa datos para ajustar el manejo por zona."),
        ("abc", "En Agropecuaria: ¿qué es un sensor?", "Un instrumento que mide una variable, como la humedad del suelo", "Una fotografía tomada desde un satélite", "Una aeronave sin piloto", "El sensor mide una variable; la fotografía es imagen satelital y la aeronave es el dron."),
        ("abc", "En Agropecuaria: ¿qué es una imagen satelital?", "Una fotografía del predio tomada desde un satélite", "Una medición de lluvia", "Un mapa dibujado a mano", "La imagen satelital se obtiene desde el espacio."),
        ("=", "{F} Un dron de ejemplo cubre 6 hectáreas por vuelo. ¿Cuántos vuelos se necesitan para cubrir el predio de la ficha?", "60//6", "Se divide la superficie del predio entre las hectáreas de cada vuelo.", " vuelos"),
        ("abc", "{F} Un pararrayos con conexión a tierra en el mástil de la estación es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla", "De EPP, porque protege a quien se acerca", "El pararrayos es una estructura física que protege sin depender de las personas."),
        ("abc", "{F} Una regla que dice «no se revisa la estación durante tormentas eléctricas» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia la estación", "De sustitución, porque cambia el mástil", "Una regla escrita es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a las baterías de litio que se calientan?", "Que se incendien y causen quemaduras o un incendio", "Las baterías de litio mismas", "Que el dron vuele más lento", "El riesgo es la posibilidad de daño; las baterías calientes son el peligro."),
        ("abc", "{F} Una estudiante dice: «sé volar drones de juguete, así que puedo volar el dron del predio». ¿Qué respuesta es correcta?", "Es falso: volar un dron exige capacitación y autorización según la norma vigente", "Es cierto, si lo vuela despacio", "Es cierto, si no hay personas cerca", "La norma exige capacitación y autorización, sin importar la velocidad."),
        ("abc", "{F} Durante una tormenta eléctrica, una persona se acerca a revisar el mástil metálico. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias si hay alguien en peligro", "Acercarte a ayudar con guantes", "Tocar el mástil para ver si está caliente", "El mástil atrae rayos; el guante no protege."),
        ("abc", "En Agropecuaria: ¿por qué se protegen con claves los datos del predio en una nube?", "Para que solo vean los datos quienes corresponden", "Para que los datos ocupen menos espacio", "Para que la estación mida mejor", "Las claves protegen la privacidad del predio y de las personas."),
        ("abc", "{F} Se propone solo pedir cuidado a quien camina mirando la pantalla cerca de los pozos. ¿Qué medida es más efectiva?", "Taparlos y señalizarlos, y mirar la pantalla en un lugar seguro", "Pedir que miren menos la pantalla", "Dar más pantallas", "Cambiar el lugar actúa sobre el peligro."),
        ("=", "{F} Cada batería de ejemplo dura 20 minutos de vuelo y se usan 3 baterías por jornada. ¿Cuántos minutos de vuelo se tienen por jornada?", "20*3", "Se multiplican los minutos de cada batería por el número de baterías.", " minutos"),
        ("abc", "En Agropecuaria: ¿qué hace una estación meteorológica?", "Mide temperatura, humedad del aire, viento y lluvia", "Ubica puntos del predio en un mapa", "Vuela sobre el predio", "La estación mide variables del clima."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por volar su dron sobre un camino con gente «porque ya viste cómo se hace en clases». ¿Qué respondes?", "Que no, porque exige capacitación y autorización, y que lo consultarás con un adulto responsable", "Que sí, si vuelas bajo", "Que sí, si hay poco viento", "Haber visto el concepto no habilita; la altura o el viento no cambian la norma."),
    sc=[
        ("En Agropecuaria: ¿qué mide un sensor de humedad?", "La humedad del suelo", "Un sensor mide una variable concreta."),
        ("En el trabajo agrícola: ¿qué se hace con un mástil metálico en una tormenta eléctrica?", "No acercarse", "El mástil atrae rayos y es peligroso."),
        ("En Agropecuaria: ¿qué es transmitir un dato?", "Enviarlo a otro lugar", "Transmitir lleva el dato a quien lo usa."),
    ],
    op=("El «Predio Demo 2» anota una tarea de ejemplo: cargar las baterías de litio de un dron en el galpón, junto a papeles y cartones, y dejarlas toda la noche. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves humo saliendo del galpón.",
        "(a) Peligro: baterías de litio junto a cartones; riesgo: que se calienten, prendan fuego y se incendie el galpón. (b) Una regla de no cargar baterías sin vigilancia. (c) Un lugar de carga aislado y con piso no inflamable. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer apagar el fuego sin formación"],
        "Pregunta: «¿qué control cambia el lugar de carga y no depende de que alguien se acuerde?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Une cada equipo inventado con lo que mide: estación, sensor de suelo, imagen satelital, GPS.",
    extend="Explica con un ejemplo por qué conviene proteger la ubicación exacta de un predio.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 2 (datos de ejemplo, inventados). Estación meteorológica del «Predio Demo»: temperatura en grados Celsius, humedad del aire en %, lluvia en mm, viento en km/h. Sensor de suelo: humedad en %. Instrumento de laboratorio: medidor de pH (de ejemplo). "
     "Calibración (ajuste de un instrumento comparando con un valor conocido, llamado patrón): al medir una solución patrón de pH 4, el medidor de ejemplo marca 5; la tolerancia de ejemplo es de 0 de diferencia. "
     "Documentos: la bitácora de mediciones (fecha, hora, instrumento, valor y responsable), el informe de laboratorio y el mapa de zonas.")
build(
    O8, 2, F,
    use="Aprenderé las unidades y la calibración de instrumentos, los documentos de la información de precisión (bitácora, informe y mapa) y los roles de quienes la obtienen y transmiten.",
    prior=["Sé qué es un sensor y una estación meteorológica.", "Sé leer una tabla de datos.", "Sé restar enteros."],
    explain=[
        "Cada variable se mide en una unidad: la temperatura en grados Celsius, la humedad en porcentaje, la lluvia en milímetros y el viento en kilómetros por hora. Sin la unidad, el valor no tiene sentido. La calibración es ajustar un instrumento comparándolo con un patrón, que es un valor conocido; si el instrumento marca distinto del patrón, está descalibrado y sus mediciones no son confiables hasta corregirlo.",
        "Los datos se anotan en una bitácora de mediciones con fecha, hora, instrumento, valor, unidad y responsable. Un informe de laboratorio entrega resultados de análisis hechos por un analista de laboratorio. Un mapa de zonas divide el predio según un dato, como la humedad o el vigor de las plantas. El técnico en agricultura de precisión interpreta los datos; el operador autorizado maneja los equipos, como el dron; el agrónomo asesor decide los manejos.",
        f"Transmitir datos es enviarlos con su unidad y su fecha; un dato sin unidad ni fecha no sirve. {EMER} {AVISO}",
    ],
    vocab=[("calibración", "ajuste de un instrumento comparándolo con un valor conocido"), ("patrón", "valor conocido con el que se compara un instrumento"), ("descalibrado", "instrumento que marca distinto del patrón"), ("bitácora de mediciones", "documento donde se anota fecha, hora, instrumento, valor y responsable"), ("mapa de zonas", "mapa que divide el predio según un dato medido"), ("analista de laboratorio", "persona que hace y entrega los análisis de muestras")],
    worked=[
        ("Detectar descalibración", "Un instrumento de ejemplo marca 10 al medir un patrón de 8. ¿Está calibrado?", ["Debería marcar 8.", "Marca 10, entonces está descalibrado."], "No, está descalibrado"),
        ("Elegir el documento", "Un técnico de ejemplo quiere saber qué lecturas hizo una persona el martes. ¿Qué documento consulta?", ["Las lecturas se anotan en una bitácora.", "La bitácora tiene fecha y responsable."], "La bitácora de mediciones"),
    ],
    mistakes=[("Usar un instrumento descalibrado «porque cerca marca parecido».", "Un error pequeño puede llevar a una decisión equivocada.", "Se informa y se recalibra antes de usarlo."),
              ("Anotar un valor sin unidad.", "El valor no se puede interpretar.", "La unidad es parte del dato.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la calibración de un instrumento?", "Ajustarlo comparándolo con un valor conocido", "Cambiarle el color", "Guardarlo en una caja", "La calibración compara el instrumento con un patrón."),
        ("abc", "En Agropecuaria: ¿qué es un patrón de calibración?", "Un valor conocido con el que se compara un instrumento", "Un dibujo con el diseño del predio", "Un registro de lluvia", "El patrón es el valor de referencia."),
        ("abc", "En Agropecuaria: ¿qué es un mapa de zonas?", "Un mapa que divide el predio según un dato medido", "Un mapa de las rutas de entrega", "Un listado de personas", "El mapa de zonas agrupa partes del predio según el dato."),
        ("abc", "{F} ¿En qué unidad se mide la lluvia en la estación?", "Milímetros", "Grados Celsius", "Kilómetros por hora", "La ficha asigna milímetros a la lluvia."),
        ("abc", "{F} ¿En qué unidad se mide el viento en la estación?", "Kilómetros por hora", "Milímetros", "Porcentaje", "La ficha asigna kilómetros por hora al viento."),
        ("abc", "{F} ¿Qué documento tiene fecha, hora, instrumento, valor y responsable de cada medición?", "La bitácora de mediciones", "El informe de laboratorio", "El mapa de zonas", "La bitácora anota los datos de cada medición."),
        ("=", "{F} ¿Cuántos puntos de diferencia hay entre lo que marca el medidor de pH y el patrón?", "5-4", "Se resta el valor del patrón al valor que marca el medidor.", " punto"),
        ("abc", "{F} Con esa diferencia y la tolerancia de ejemplo, ¿el medidor está calibrado?", "No, porque la diferencia supera la tolerancia", "Sí, porque la diferencia es pequeña", "Sí, porque marca un número entero", "La tolerancia de ejemplo es 0 y la diferencia es 1."),
        ("abc", "{F} Una compañera dice: «el medidor marca casi lo mismo, así que lo uso igual». ¿Qué respuesta es correcta?", "Es incorrecto: se informa y se recalibra antes de usarlo", "Es correcto, si el valor es parecido", "Es correcto, si lo usa una sola vez", "Un instrumento fuera de tolerancia entrega datos no confiables."),
        ("abc", "{F} El técnico encuentra una fila de la bitácora con «23» y sin unidad. ¿Qué corresponde?", "Preguntar al responsable por la unidad real, sin inventarla", "Suponer que son grados", "Borrar la fila", "Una unidad supuesta puede ser equivocada."),
        ("=", "{F} El sensor de suelo midió 24, 26 y 25 % en tres puntos. ¿Cuál es el promedio?", "(24+26+25)//3", "Se suman las tres lecturas y se divide entre 3.", " %"),
        ("abc", "{F} ¿Quién decide qué manejo aplicar según los datos?", "El agrónomo asesor", "El operador del dron", "El analista de laboratorio", "El asesor decide el manejo; el operador maneja equipos y el analista entrega resultados."),
        ("abc", "En Agropecuaria: ¿por qué un dato sin fecha ni unidad no sirve para decidir?", "Porque no se sabe cuándo se midió ni cómo interpretarlo", "Porque ocupa mucho espacio", "Porque solo los instrumentos antiguos lo anotan", "La fecha y la unidad dan sentido al dato."),
    ],
    ctx=("abc", "Una conocida te pide que le calibres su instrumento en el campo con lo que tengas a mano. ¿Qué respondes?", "Que la calibración la hace personal capacitado con un patrón adecuado, y que lo consultarás con un adulto responsable", "Que sí, con cualquier líquido", "Que lo use sin calibrar", "Un patrón inadecuado deja el instrumento más desajustado."),
    sc=[
        ("En Agropecuaria: ¿qué es un instrumento descalibrado?", "Uno que marca distinto del patrón", "El patrón es el valor de referencia."),
        ("En el trabajo agrícola: ¿qué documento anota cada medición?", "La bitácora de mediciones", "La bitácora guarda el detalle de cada medición."),
        ("En Agropecuaria: ¿qué pasa con un dato sin unidad?", "No se puede interpretar", "La unidad da sentido al valor."),
    ],
    op=("Datos de ejemplo del «Predio Demo 3»: medidor de pH que marca 8 al medir un patrón de 7; sensor de humedad con lecturas 18, 20, 22 y 20 % en cuatro puntos. Escribe (a) la diferencia del medidor con el patrón y si está calibrado con tolerancia 0, (b) el promedio de humedad, (c) qué documento usarías para anotar cada lectura, (d) qué haces si falta la unidad en una lectura.",
        "(a) 8 − 7 = 1; no está calibrado. (b) (18 + 20 + 22 + 20) ÷ 4 = 20 %. (c) La bitácora de mediciones. (d) Pregunto al responsable por la unidad real, sin inventarla.",
        ["calcula la diferencia", "calcula el promedio", "nombra el documento", "no inventa la unidad"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "usar un instrumento descalibrado", "inventar la unidad"],
        "Pregunta: «¿qué valor debería marcar el medidor?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Anota con unidad cuatro medidas inventadas de una estación: temperatura, humedad, lluvia y viento.",
    extend="Explica con un ejemplo por qué la calibración debe repetirse cada cierto tiempo.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 3 (mapa de ejemplo, inventado). Mapa de vigor de las plantas del «Predio Demo» a partir de una imagen de ejemplo. Valores de 0 a 100 (más alto, más vigor); cada celda representa 4 hectáreas. "
     "Fila A: 82, 79, 41, 80, 77. Fila B: 75, 38, 78, 81, 35. Umbral de ejemplo: bajo 50 se considera zona de bajo vigor. Un sensor de humedad en la celda con 38 mide 12 %, y en otras celdas mide alrededor de 25 %.")
build(
    O8, 3, F,
    use="Aprenderé a analizar un mapa de información remota en papel, a localizar zonas de bajo vigor y a decidir qué se revisa en terreno antes de concluir.",
    prior=["Sé qué es una imagen satelital y un sensor.", "Sé calcular porcentajes enteros.", "Sé leer una tabla de datos."],
    explain=[
        "Un mapa de vigor muestra, con números o colores, qué tan sanas y verdes están las plantas en cada zona. Los valores bajos señalan zonas de menor vigor. Pero el mapa no dice por qué: puede ser falta de agua, una plaga, un suelo distinto o una compactación. Por eso se combina con otros datos, como un sensor de humedad, y se confirma en terreno con una revisión dirigida, es decir, solo en las zonas señaladas.",
        "Para analizar un mapa se localizan las celdas bajo el umbral, se cuenta cuántas son, se calcula el porcentaje de la superficie y se cruza con otro dato. Si una celda de bajo vigor también tiene baja humedad, la falta de agua es una causa posible. La conclusión final es una hipótesis que confirma el asesor en el terreno. El manejo diferenciado aplica a cada zona lo que necesita, en vez de tratar todo igual.",
        f"Las visitas a terreno las hace personal capacitado: hay pozos, zanjas y pendientes. {EMER} {AVISO}",
    ],
    vocab=[("vigor", "qué tan sanas y verdes están las plantas"), ("celda", "cuadro de un mapa que representa una parte del predio"), ("zona de bajo vigor", "zona con valores bajo el umbral"), ("hipótesis", "explicación posible que aún hay que confirmar"), ("revisión dirigida", "revisión en terreno solo de las zonas señaladas"), ("manejo diferenciado", "manejo distinto para cada zona según lo que necesita")],
    worked=[
        ("Zonas bajo el umbral", "Un mapa de ejemplo tiene los valores 60, 45, 80 y 30, con umbral 50. ¿Cuántas celdas están bajo el umbral?", ["Se comparan los valores con 50.", "45 y 30 son menores que 50."], "2 celdas"),
        ("Cruzar dos datos", "Una celda de ejemplo tiene bajo vigor y baja humedad. ¿Qué causa es posible?", ["Dos datos apuntan a falta de agua.", "Es una hipótesis que se confirma en terreno."], "Falta de agua, como hipótesis"),
    ],
    mistakes=[("Concluir la causa solo mirando el mapa.", "El mapa muestra dónde hay un problema, no por qué.", "Se cruza con otros datos y se confirma en terreno."),
              ("Visitar sin cuidado la zona señalada mirando solo la pantalla.", "Hay pozos, zanjas y pendientes.", "La visita la hace personal capacitado.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué indica un valor bajo en un mapa de vigor?", "Una zona con plantas menos sanas o verdes", "Una zona con más lluvia", "Una zona con más hectáreas", "El valor bajo señala menor vigor; la causa se estudia aparte."),
        ("abc", "En Agropecuaria: ¿qué es una hipótesis en este contexto?", "Una explicación posible que aún hay que confirmar", "Una causa ya comprobada", "Un dato del satélite", "La hipótesis necesita confirmación en terreno."),
        ("abc", "En Agropecuaria: ¿qué es una revisión dirigida?", "Una revisión en terreno solo de las zonas señaladas", "Una revisión de todo el predio con el dron", "Una revisión del mapa en la oficina", "La revisión dirigida se concentra en las zonas con problema."),
        ("abc", "{F} ¿Cuántas celdas del mapa están bajo el umbral de 50?", "3 celdas, las de 41, 38 y 35", "2 celdas, las de 38 y 35", "4 celdas, las de 41, 38, 35 y 75", "Solo los valores 41, 38 y 35 son menores que 50."),
        ("=", "{F} ¿Qué porcentaje de las 10 celdas está bajo el umbral?", "3*100//10", "Se divide las celdas bajo el umbral entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas hectáreas suman las zonas de bajo vigor, si cada celda tiene 4 hectáreas?", "3*4", "Se multiplica el número de celdas bajas por las hectáreas de cada una.", " hectáreas"),
        ("abc", "{F} ¿Qué celda de la Fila B tiene bajo vigor y baja humedad medida?", "La celda con 38", "La celda con 75", "La celda con 81", "El sensor de la celda de 38 mide 12 %, menor que las demás."),
        ("abc", "{F} ¿Qué hipótesis es razonable para la celda de 38?", "Falta de agua, que se debe confirmar en terreno", "Exceso de cosecha, ya comprobado", "Un error del satélite, ya comprobado", "Bajo vigor con baja humedad apunta a poca agua, pero es hipótesis."),
        ("abc", "{F} Un compañero dice: «el mapa muestra bajo vigor en las celdas de 41 y 35, así que seguro son plagas». ¿Qué respuesta es correcta?", "Es incorrecto: la causa no se conoce con el mapa y hay que confirmarla en terreno", "Es correcto, porque el mapa lo indica", "Es correcto, si hay más de una celda", "El mapa muestra dónde, no por qué."),
        ("abc", "{F} Un encargado quiere visitar de noche las celdas de bajo vigor, mirando solo la pantalla del celular entre pozos y zanjas. ¿Qué corresponde?", "Rechazarlo: la visita la hace personal capacitado, con luz y en un lugar seguro", "Aceptarlo, porque ahorra tiempo", "Aceptarlo, si va acompañado", "Hay pozos y zanjas; mirar la pantalla en la noche aumenta el riesgo."),
        ("=", "{F} Un riego diferenciado de ejemplo da 12 mm a las zonas de bajo vigor y 8 mm al resto. Con 1 mm sobre 1 hectárea igual a 10 m³, ¿cuántos m³ recibe la zona de bajo vigor?", "3*4*12*10", "Se multiplican las hectáreas de bajo vigor por los mm y por 10.", " m³"),
        ("abc", "{F} ¿Qué ventaja tiene el manejo diferenciado frente a tratar todo igual?", "Aplica a cada zona lo que necesita y evita gastar donde no hace falta", "Evita medir los datos", "Hace que todas las zonas rindan lo mismo sin otro cambio", "Se ajusta el manejo a las necesidades de cada zona."),
        ("abc", "En Agropecuaria: ¿por qué conviene cruzar el mapa con un sensor de humedad?", "Porque dos datos que apuntan a lo mismo refuerzan la hipótesis", "Porque el mapa siempre está equivocado", "Porque el sensor reemplaza al asesor", "Cruzar datos reduce el riesgo de una conclusión equivocada."),
    ],
    ctx=("abc", "Un conocido te muestra un mapa de su predio con zonas bajas y te pide que le digas qué producto aplicar. ¿Qué respondes?", "Que el mapa no dice la causa y que un asesor debe confirmarla en terreno", "Que aplique un producto en todo el predio", "Que aplique más agua en todo el predio", "Sin conocer la causa, aplicar algo puede ser inútil o dañino."),
    sc=[
        ("En Agropecuaria: ¿qué muestra un mapa de vigor?", "Dónde hay zonas con plantas más o menos sanas", "El mapa muestra el dónde, no el porqué."),
        ("En el trabajo agrícola: ¿quién confirma en terreno la causa?", "El asesor, con personal capacitado", "La causa se confirma con revisión en terreno."),
        ("En Agropecuaria: ¿qué es el manejo diferenciado?", "Manejar cada zona según lo que necesita", "Cada zona recibe lo que necesita."),
    ],
    op=("Mapa de ejemplo del «Predio Demo 4», valores de vigor: Fila A: 70, 30, 85, 75; Fila B: 80, 78, 40, 82. Umbral de ejemplo 50; cada celda representa 5 hectáreas. Un sensor en la celda de 30 mide 10 % de humedad, y las demás miden alrededor de 22 %. Escribe (a) cuántas celdas están bajo el umbral, (b) cuántas hectáreas suman, (c) una hipótesis para la celda de 30 y qué la apoya, (d) quién la confirma y cómo.",
        "(a) 2 celdas: 30 y 40. (b) 2 × 5 = 10 hectáreas. (c) Falta de agua, porque el sensor mide 10 %, menos que las demás celdas; es una hipótesis. (d) El asesor, con una revisión dirigida en terreno hecha por personal capacitado.",
        ["cuenta las celdas bajo el umbral", "calcula las hectáreas", "propone una hipótesis con evidencia", "indica quién confirma"],
        ["hoja con las cuatro respuestas"],
        ["decir la causa como cierta", "no calcular las hectáreas"],
        "Pregunta: «¿qué valores son menores que 50?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Cuenta en un mapa inventado de 8 celdas cuántas están bajo un umbral de 60 con los valores 70, 55, 80, 40, 65, 59, 90 y 62.",
    extend="Explica con un ejemplo por qué una hipótesis no es lo mismo que una causa comprobada.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). El «Predio Demo» de 40 hectáreas compara dos formas de regar con datos de ejemplo. Riego uniforme: 10 mm en todo el predio. "
     "Riego diferenciado según el mapa de humedad: 30 hectáreas con 8 mm y 10 hectáreas con 14 mm. Regla del curso: 1 mm sobre 1 hectárea equivale a 10 m³. "
     "Transmisión de datos: cada imagen de ejemplo pesa 25 MB y el dispositivo tiene 1.000 MB libres.")
build(
    O8, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: comparar un manejo uniforme con uno diferenciado, y calcular promedios, volúmenes y capacidad de almacenamiento de datos.",
    prior=["Sé calcular volúmenes de riego con la regla de 1 mm.", "Sé multiplicar y dividir enteros.", "Sé calcular promedios."],
    explain=[
        "En agricultura de precisión se compara un manejo uniforme, igual para todo el predio, con uno diferenciado, ajustado por zonas. El volumen de agua se calcula multiplicando los milímetros por las hectáreas y por 10 m³. Se suman los volúmenes de cada zona y se compara con el volumen uniforme. Un manejo diferenciado puede ahorrar recursos o repartirlos mejor, pero lo importante es que cada zona reciba lo que necesita.",
        "Los datos también tienen un tamaño. Un megabyte (MB) es una unidad de tamaño de datos. El número de imágenes que caben en un dispositivo es el espacio libre dividido entre el tamaño de cada imagen. Transmitir y guardar datos cuesta espacio y tiempo, y por eso se eligen las mediciones necesarias, se respaldan y se borran solo las que ya no sirven y fueron respaldadas.",
        f"Las cifras de esta clase son de ejemplo; las reales las define el asesor. {EMER} {AVISO}",
    ],
    vocab=[("manejo uniforme", "manejo igual para todo el predio"), ("manejo diferenciado", "manejo distinto por zonas según lo que necesitan"), ("megabyte (MB)", "unidad de tamaño de datos"), ("volumen de riego", "milímetros por hectáreas por 10 m³"), ("respaldo", "copia de los datos en otro lugar")],
    worked=[
        ("Volumen uniforme", "Un predio de ejemplo de 20 hectáreas recibe 5 mm en todo el predio. ¿Cuántos m³ se usan?", ["1 mm sobre 1 hectárea son 10 m³.", "5 por 20 por 10."], "1.000 m³"),
        ("Capacidad de datos", "Cada archivo de ejemplo pesa 50 MB y hay 400 MB libres. ¿Cuántos archivos caben?", ["Se divide el espacio libre entre el tamaño de cada archivo.", "400 entre 50 es 8."], "8 archivos"),
    ],
    mistakes=[("Creer que un manejo diferenciado siempre gasta menos.", "Puede gastar lo mismo o más si hay zonas con más necesidad.", "Se calcula y se compara; el objetivo es que cada zona reciba lo que necesita."),
              ("Borrar los datos del dispositivo sin respaldar para liberar espacio.", "Se pierden datos que podrían servir.", "Se respalda antes de borrar.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es un manejo diferenciado?", "Un manejo distinto por zonas según lo que necesitan", "Un manejo igual para todo el predio", "Un manejo sin registro", "El diferenciado ajusta cada zona; el uniforme trata todo igual."),
        ("abc", "En Agropecuaria: ¿qué es un megabyte (MB)?", "Una unidad de tamaño de datos", "Una unidad de lluvia", "Una unidad de superficie", "El megabyte mide el tamaño de archivos de datos."),
        ("abc", "En Agropecuaria: ¿qué conviene hacer antes de borrar datos de un dispositivo?", "Respaldarlos en otro lugar", "Cambiarles el nombre", "Imprimirlos sin guardarlos", "El respaldo evita perder datos útiles."),
        ("=", "{F} ¿Cuántos m³ se usan con el riego uniforme?", "10*40*10", "Se multiplican los mm por las hectáreas y por 10 m³.", " m³"),
        ("=", "{F} ¿Cuántos m³ se usan en las 30 hectáreas del riego diferenciado?", "8*30*10", "Se multiplican los mm por las hectáreas y por 10 m³.", " m³"),
        ("=", "{F} ¿Cuántos m³ se usan en las 10 hectáreas con 14 mm?", "14*10*10", "Se multiplican los mm por las hectáreas y por 10 m³.", " m³"),
        ("=", "{F} ¿Cuántos m³ se usan en total con el riego diferenciado?", "8*30*10+14*10*10", "Se suman los volúmenes de las dos zonas.", " m³"),
        ("=", "{F} ¿Cuántos m³ se ahorran con el riego diferenciado respecto del uniforme?", "10*40*10-(8*30*10+14*10*10)", "Se resta el volumen diferenciado al volumen uniforme.", " m³"),
        ("=", "{F} ¿Cuántas imágenes caben en el dispositivo?", "1000//25", "Se divide el espacio libre entre el tamaño de cada imagen.", " imágenes"),
        ("=", "{F} Si se toman 12 imágenes por vuelo, ¿cuántos vuelos completos caben en el dispositivo?", "(1000//25)//12", "Se calcula cuántas imágenes caben y se divide entre las de cada vuelo.", " vuelos"),
        ("abc", "{F} Un compañero dice: «con el diferenciado se gasta siempre menos». ¿Qué respuesta es correcta?", "Es falso: el diferenciado reparte según la necesidad y su volumen se calcula", "Es cierto, porque es más moderno", "Es cierto, si hay sensores", "Puede gastar más o menos; lo importante es que cada zona reciba lo que necesita."),
        ("abc", "{F} El técnico quiere borrar las imágenes para liberar espacio sin respaldarlas. ¿Qué corresponde?", "Respaldarlas primero y borrar solo las que ya no sirven", "Borrarlas, porque ocupan lugar", "Borrarlas de noche", "Sin respaldo se pierden datos que podrían servir."),
        ("abc", "En Agropecuaria: ¿por qué el volumen de riego diferenciado se calcula zona por zona?", "Porque cada zona recibe una cantidad distinta de agua", "Porque cada zona tiene un cultivo distinto por regla", "Porque el cálculo total no existe", "Cada zona tiene su milímetro y sus hectáreas."),
    ],
    ctx=("abc", "Un conocido te pregunta si le conviene un riego diferenciado y te da solo la superficie de su predio. ¿Qué respondes?", "Que faltan los datos de las zonas, y que lo decide un asesor", "Que sí, siempre", "Que no, nunca", "Sin datos por zona no se puede calcular ni comparar."),
    sc=[
        ("En Agropecuaria: ¿cuántos m³ son 1 mm sobre 1 hectárea según la regla?", "10 m³", "La regla del curso vale 10 m³ por mm y hectárea."),
        ("En el trabajo agrícola: ¿cuántas imágenes caben en el espacio libre?", "Espacio libre entre el tamaño de cada imagen", "La capacidad se calcula con una división."),
        ("En Agropecuaria: ¿qué se hace antes de borrar datos?", "Se respaldan", "El respaldo evita perder datos útiles."),
    ],
    op=("Datos de ejemplo del «Predio Demo 5»: 20 hectáreas. Uniforme: 6 mm en todo el predio. Diferenciado: 15 hectáreas con 4 mm y 5 hectáreas con 12 mm. Regla: 1 mm sobre 1 hectárea son 10 m³. El dispositivo tiene 600 MB libres y cada imagen pesa 30 MB. Escribe (a) el volumen uniforme, (b) el volumen diferenciado, (c) la diferencia y si ahorra o gasta más, (d) cuántas imágenes caben.",
        "(a) 6 × 20 × 10 = 1.200 m³. (b) 4 × 15 × 10 + 12 × 5 × 10 = 600 + 600 = 1.200 m³. (c) La diferencia es 0: gasta lo mismo, pero lo reparte según la necesidad. (d) 600 ÷ 30 = 20 imágenes.",
        ["calcula el volumen uniforme", "calcula el volumen diferenciado", "compara", "calcula la capacidad"],
        ["hoja con las cuatro respuestas"],
        ["olvidar multiplicar por 10", "suponer que el diferenciado siempre ahorra"],
        "Pregunta: «¿por cuánto multiplicas milímetros por hectáreas para obtener m³?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el volumen de 5 mm en 12 hectáreas, con 1 mm sobre 1 hectárea igual a 10 m³.",
    extend="Explica con un ejemplo por qué repartir según la necesidad puede ser mejor aunque el volumen total sea igual.",
)
