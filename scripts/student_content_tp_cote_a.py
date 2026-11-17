"""Construcción, mención Terminaciones (4.º medio TP): OAM-01 (impermeabilizar y aislar: fichas técnicas, hojas de datos de seguridad y cubicación), OAM-02 (muebles, tabiques y hojas de puertas y ventanas: planos de detalle y despiece) y OAM-03 (revestimientos de pisos, muros y cielos: cuadros de acabados, cubicación y control). Solo conceptos y planillas con datos de ejemplo."""
from __future__ import annotations

from tp_cote_common import AVISO, EMER, build

O1 = "TP-COTE-4-OAM-01"
O2 = "TP-COTE-4-OAM-02"
O3 = "TP-COTE-4-OAM-03"
TAIL = f"{EMER} {AVISO}"

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (obra de ejemplo, inventada). Obra «Casa Sol» (ficticia): se impermeabiliza y aísla el techo de una vivienda. Cuadrilla de 6 personas. Se reciben 10 envases de productos: 7 con etiqueta legible y pictogramas, y 3 sin etiqueta. "
     "Riesgos anotados: caída desde la techumbre, inhalación de vapores, contacto del producto con piel y ojos, incendio de productos inflamables cerca de fuentes de calor e irritación por fibras del aislante. "
     "Medidas anotadas: hoja de datos de seguridad disponible, ventilación, guantes, lentes, mascarilla indicada por la hoja de datos, protección colectiva en el borde del techo y personal autorizado para trabajo en altura.")
build(
    O1, 1, F,
    use="Aprenderé qué es impermeabilizar y aislar, qué riesgos tienen los productos y los trabajos en techumbres y cómo se leen las etiquetas y las hojas de datos de seguridad.",
    prior=["Sé qué es la jerarquía de controles.", "Sé sumar y restar números pequeños.", "Sé leer una ficha de obra."],
    explain=[
        "Impermeabilizar es proteger una superficie para que el agua no pase hacia el interior. Aislar es reducir el paso de calor o de ruido a través de una superficie; la aislación térmica cuida la temperatura y la acústica reduce el ruido. Los muros, tabiques, pisos, cielos y techumbres se tratan con productos de distintos fabricantes, y cada fabricante entrega indicaciones por escrito que se deben respetar. Cómo se aplican esos productos lo enseña un instructor autorizado y está en las instrucciones del fabricante; este cuaderno no contiene esos pasos.",
        "Los productos químicos traen una etiqueta con pictogramas, que son símbolos gráficos que advierten un peligro, y una hoja de datos de seguridad (HDS), documento del fabricante que informa peligros, protección necesaria y qué hacer ante un derrame o contacto. Un envase sin etiqueta no se usa: se informa al responsable hasta identificar su contenido. Las techumbres suman el riesgo de caída: solo trabaja en altura el personal autorizado, con protecciones colectivas. Según la jerarquía de controles, el EPP es el último nivel y nunca reemplaza la ventilación ni la autorización.",
        TAIL,
    ],
    vocab=[("impermeabilizar", "proteger una superficie para que el agua no pase hacia el interior"), ("aislación térmica", "reducción del paso de calor a través de una superficie"), ("pictograma", "símbolo gráfico de la etiqueta que advierte un peligro"), ("hoja de datos de seguridad", "documento del fabricante con peligros, protección y qué hacer ante un derrame o contacto"), ("protección colectiva", "medida que cuida a todas las personas a la vez, como una baranda"), ("responsable", "persona que decide y firma los registros de la obra")],
    worked=[
        ("Reconocer el documento", "Un trabajador de ejemplo quiere saber qué hacer si un producto cae sobre la piel. ¿Qué documento del fabricante consulta?", ["El documento que informa peligros y qué hacer ante un contacto es la hoja de datos de seguridad.", "Esa hoja la entrega el fabricante."], "La hoja de datos de seguridad"),
        ("Contar envases", "Llegan 12 envases y 9 tienen etiqueta legible. ¿Cuántos no la tienen?", ["Se restan los envases con etiqueta del total.", "12 menos 9 son 3."], "3 envases"),
    ],
    mistakes=[("Usar un envase sin etiqueta porque «huele igual» a otro.", "El olor no identifica un producto y puede ser peligroso.", "No se usa: se informa al responsable hasta identificar su contenido."),
              ("Creer que la mascarilla reemplaza la ventilación.", "El EPP es el último nivel y no elimina el peligro.", "Se combinan ventilación, organización del trabajo y EPP según la hoja de datos.")],
    T=[
        ("abc", "En Construcción (terminaciones): ¿qué significa impermeabilizar una superficie?", "Protegerla para que el agua no pase hacia el interior", "Reducir el paso de calor a través de ella", "Pintarla de un color más claro", "Impermeabilizar frena el agua; reducir el calor es aislar."),
        ("abc", "¿Qué es una hoja de datos de seguridad?", "Un documento del fabricante con peligros, protección y qué hacer ante un derrame o contacto", "La boleta de compra del producto", "El plano que muestra dónde va el producto", "La hoja es informativa y de seguridad; la boleta y el plano son otros documentos."),
        ("abc", "¿Qué es un pictograma en la etiqueta de un producto?", "Un símbolo gráfico que advierte un peligro", "El nombre de la empresa que vende", "El precio por litro", "El pictograma comunica un peligro con un dibujo; el nombre y el precio son otros datos."),
        ("=", "{F} ¿Cuántos envases no tienen etiqueta?", "10-7", "Se restan los envases con etiqueta del total recibido.", " envases"),
        ("abc", "{F} ¿Qué medida de la ficha es una protección colectiva?", "La protección en el borde del techo", "La mascarilla", "Los guantes", "La protección del borde cuida a todos a la vez; mascarilla y guantes son EPP."),
        ("abc", "{F} ¿Dónde se consulta qué mascarilla corresponde?", "En la hoja de datos de seguridad", "En el precio del envase", "En el plano de planta", "La hoja de datos indica la protección necesaria; el precio y el plano no."),
        ("=", "{F} Cada integrante de la cuadrilla recibe guantes, lentes y mascarilla. ¿Cuántas piezas de EPP se entregan?", "6*3", "Se multiplican las 6 personas por las 3 piezas de cada una.", " piezas"),
        ("abc", "{F} ¿Qué corresponde hacer con los envases sin etiqueta?", "No usarlos e informar al responsable hasta identificar su contenido", "Usarlos si el color parece igual al de otros", "Mezclarlos con los etiquetados para aprovecharlos", "Sin etiqueta no se conoce el peligro; por eso no se usan ni se mezclan."),
        ("abc", "{F} Se ve un envase inflamable junto a un equipo que produce chispas. ¿Qué corresponde?", "Avisar al responsable para separar el producto de la fuente de calor", "Dejarlo si no hay llamas visibles", "Taparlo con una tela y seguir", "Un producto inflamable cerca de chispas es un riesgo de incendio; se informa a quien puede resolverlo."),
        ("ab", "{F} Una persona dice: «con la mascarilla no hace falta ventilar». ¿Qué respuesta es correcta?", "No: el EPP es el último nivel y no reemplaza la ventilación", "Sí: la mascarilla elimina todo el peligro", "La ficha incluye ventilación y mascarilla como medidas distintas."),
        ("abc", "{F} Una estudiante dice: «ya sé qué es impermeabilizar, puedo trabajar en el techo». ¿Qué respuesta es correcta?", "No: el trabajo en altura exige personal autorizado, instructor y norma vigente", "Sí: entender el término la habilita", "Sí, si usa guantes y lentes", "Saber un término no habilita ni los EPP reemplazan la autorización."),
        ("=", "{F} Si cada uno de los 7 envases etiquetados alcanza para 20 m² (dato de ejemplo), ¿cuántos m² cubren en total?", "7*20", "Se multiplican los envases por los m² que alcanza cada uno.", " m²"),
        ("abc", "{F} El prevencionista pide registrar los envases sin etiqueta. ¿Qué datos mínimos lleva el registro?", "Cuántos son, dónde están, quién los detectó y la fecha", "Solo el nombre del proveedor", "Solo el precio de cada uno", "Un registro útil dice cuántos, dónde, quién y cuándo."),
    ],
    ctx=("abc", "En una obra de ejemplo, una persona respira vapores de un producto y se desploma dentro de un cuarto cerrado. ¿Qué se hace según las reglas generales?", "No entrar a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar de inmediato a sacarla sin protección", "Esperar a ver si se recupera sola", "Entrar sin protección puede intoxicar también a quien ayuda; se avisa a quien corresponde y a emergencias."),
    sc=[
        ("En Construcción (terminaciones): ¿qué es aislar una superficie?", "Reducir el paso de calor o de ruido a través de ella", "Aislar reduce calor o ruido; impermeabilizar frena el agua."),
        ("¿Qué se hace con un envase sin etiqueta?", "No se usa y se informa al responsable", "Sin etiqueta no se conoce el peligro del producto."),
        ("¿Quién puede trabajar en una techumbre?", "Solo personal autorizado, con instructor y protecciones", "El trabajo en altura exige autorización y norma vigente."),
    ],
    op=("Obra de ejemplo «Bodega Ribera» (ficticia): se aísla un cielo con cuadrilla de 4 personas. Llegan 9 envases de producto: 6 con etiqueta y 3 sin ella. Riesgos anotados: vapores, fibras del aislante e incendio. Medidas disponibles: ventilación, hoja de datos de seguridad, guantes, lentes y mascarilla. Escribe (a) cuántos envases no tienen etiqueta y qué haces con ellos, (b) cuántas piezas de EPP necesitas si cada persona recibe guantes, lentes y mascarilla, (c) qué documento dice qué mascarilla corresponde y (d) qué haces si alguien se desmaya por vapores.",
        "(a) 9 menos 6 son 3 envases; no se usan y se informa al responsable. (b) 4×3 son 12 piezas. (c) La hoja de datos de seguridad. (d) No entro a la zona de riesgo, aviso a un adulto responsable y a emergencias.",
        ["calcula los envases sin etiqueta", "indica no usarlos e informar", "calcula las piezas de EPP", "nombra el documento correcto", "avisa sin acercarse al riesgo"],
        ["hoja con las cuatro respuestas"],
        ["usar envases sin etiqueta", "confundir ficha técnica con hoja de datos", "proponer entrar a rescatar sin protección"],
        "Pregunta: «¿por qué no se usa un envase sin etiqueta?». Si no responde, pídele que relea qué es un pictograma."),
    reinforce="Escribe la diferencia entre impermeabilizar y aislar con un ejemplo de cada uno en una vivienda.",
    extend="Explica por qué la ventilación y la mascarilla son medidas distintas dentro de la jerarquía de controles.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (ficha técnica de ejemplo, inventada). Producto ficticio «Membrana MX-ejemplo» (impermeabilizante): rendimiento de ejemplo de 2 m² por litro y por capa; envase de 5 litros; capas indicadas por el fabricante: 2. "
     "Condiciones de almacenamiento: lugar ventilado y alejado del calor; vigencia del producto sellado: 12 meses desde su fabricación. Pictograma de la etiqueta: «inflamable». "
     "Producto ficticio «Panel AT-ejemplo» (aislante térmico): panel de 100 cm por 50 cm, que cubre medio m²; fibras que pueden irritar la piel.")
build(
    O1, 2, F,
    use="Aprenderé a leer una ficha técnica y una etiqueta: rendimiento, capas, vigencia, almacenamiento y pictogramas.",
    prior=["Sé qué es una hoja de datos de seguridad.", "Sé multiplicar y dividir.", "Sé que las indicaciones del fabricante se respetan."],
    explain=[
        "La ficha técnica es el documento del fabricante que describe un producto: para qué sirve, cuánto rinde, cómo se almacena y cuánto dura. El rendimiento dice qué superficie cubre una cantidad del producto; por ejemplo, 2 m² por litro significa que un litro alcanza para 2 m² en una capa. La vigencia es el tiempo durante el cual el producto sellado es utilizable, contado desde su fabricación; pasada la vigencia no se usa. Las condiciones de almacenamiento indican dónde guardar el producto, por ejemplo lejos del calor.",
        "La ficha técnica y la hoja de datos de seguridad son documentos distintos: la primera dice cómo es el producto y la segunda cómo protegerse de él. Las instrucciones de uso las fija el fabricante y las practica personal capacitado; aquí solo se leen y se calculan con valores de ejemplo. Si la ficha técnica contradice las especificaciones del proyecto, no se decide por cuenta propia: se informa a quien inspecciona la obra.",
        TAIL,
    ],
    vocab=[("ficha técnica", "documento del fabricante que describe un producto, su rendimiento, almacenamiento y vigencia"), ("rendimiento", "superficie que cubre una cantidad de producto"), ("vigencia", "tiempo en que el producto sellado se puede usar, contado desde su fabricación"), ("almacenamiento", "forma y lugar de guardar un producto"), ("capa", "cada pasada de producto sobre una superficie, según indica el fabricante")],
    worked=[
        ("Superficie por envase", "Un producto de ejemplo rinde 4 m² por litro en una capa y el envase es de 3 litros. ¿Cuántos m² cubre un envase en una capa?", ["Se multiplica el rendimiento por los litros del envase.", "4 por 3 son 12."], "12 m²"),
        ("Revisar la vigencia", "Un producto de ejemplo tiene vigencia de 6 meses y fue fabricado hace 8 meses. ¿Se puede usar?", ["Han pasado 8 meses y la vigencia es de 6.", "Se pasó de la vigencia."], "No, está vencido"),
    ],
    mistakes=[("Confundir la ficha técnica con la hoja de datos de seguridad.", "Una describe el producto y la otra cómo protegerse.", "Consulta la ficha para rendimiento y vigencia, y la hoja para peligros y protección."),
              ("Usar un producto vencido porque se ve igual.", "La vigencia indica hasta cuándo es utilizable.", "Respeta la vigencia de la ficha técnica y informa si está vencido.")],
    T=[
        ("abc", "En Construcción (terminaciones): ¿qué es el rendimiento de un producto?", "La superficie que cubre una cantidad de producto", "El precio por litro", "El tiempo que tarda en secar", "El rendimiento relaciona cantidad de producto y superficie cubierta; no es precio ni tiempo."),
        ("abc", "¿Qué indica la vigencia de un producto?", "Cuánto tiempo se puede usar el producto sellado desde su fabricación", "Cuánto cuesta el producto", "Qué color tiene", "La vigencia es el período de uso desde la fabricación."),
        ("abc", "¿Qué documento informa cómo protegerse de los peligros del producto?", "La hoja de datos de seguridad", "La ficha técnica de rendimiento", "El presupuesto de la obra", "La protección se explica en la hoja de datos; la ficha técnica describe el producto."),
        ("=", "{F} Si se compran 3 envases de membrana, ¿cuántos litros de producto son?", "3*5", "Se multiplican los envases por los 5 litros de cada uno.", " litros"),
        ("=", "{F} ¿Cuántos m² cubre un envase de 5 litros en una capa?", "2*5", "Se multiplica el rendimiento por los litros del envase.", " m²"),
        ("abc", "{F} ¿Qué pictograma lleva la etiqueta de la membrana?", "Inflamable", "Corrosivo", "Tóxico para el agua", "La ficha anota el pictograma «inflamable»."),
        ("=", "{F} ¿Cuántos m² cubre un envase de membrana con las 2 capas indicadas?", "2*5//2", "Los m² de una capa se reparten entre las 2 capas indicadas.", " m²"),
        ("=", "{F} ¿Cuántos paneles de aislante cubren 6 m²?", "6*2", "Cada panel cubre medio m², por lo que hay 2 paneles por m².", " paneles"),
        ("ab", "{F} La membrana se fabricó hace 14 meses. ¿Qué conclusión es correcta?", "Está vencida: la vigencia es de 12 meses", "Se puede usar: 14 meses es menos que 12", "Han pasado más de 12 meses desde su fabricación."),
        ("abc", "{F} ¿Dónde se debe guardar la membrana según la ficha?", "En un lugar ventilado y alejado del calor", "Junto a un equipo que genera chispas", "En un lugar cerrado sin ventilación", "La ficha pide ventilación y lejanía del calor por el pictograma inflamable."),
        ("abc", "{F} La ficha técnica dice 2 capas y las especificaciones del proyecto dicen 3. ¿Qué corresponde?", "Anotar la diferencia e informar a quien inspecciona la obra", "Elegir 2 porque lo dice el fabricante", "Elegir 3 sin avisar", "Una contradicción de documentos se informa; no se resuelve por cuenta propia."),
        ("=", "{F} ¿Cuántos paneles se necesitan para 15 m²?", "15*2", "Se multiplican los m² por los 2 paneles de cada m².", " paneles"),
        ("abc", "{F} Un estudiante dice: «la ficha técnica ya me indica cómo protegerme, no necesito la hoja de datos». ¿Qué respuesta es correcta?", "No: la protección está en la hoja de datos de seguridad, que es otro documento", "Sí: la ficha técnica incluye toda la seguridad", "Sí, si el producto es de baja vigencia", "La ficha técnica describe el producto; para la protección se consulta la hoja de datos."),
    ],
    ctx=("abc", "En una bodega de ejemplo hay un envase inflamable junto a una fuente de calor y alguien propone «solo apartarlo un poco con el pie». ¿Qué corresponde?", "Avisar al responsable para reubicarlo con seguridad según la ficha", "Moverlo con el pie", "Taparlo con una caja", "Los productos inflamables se reubican de forma segura y con autorización."),
    sc=[
        ("¿Qué es la vigencia de un producto?", "El tiempo en que se puede usar el producto sellado, desde su fabricación", "Pasada la vigencia el producto no debe usarse."),
        ("En Construcción (terminaciones): ¿qué indica un rendimiento de 3 m² por litro?", "Que un litro cubre 3 m² en una capa", "Relaciona el volumen del producto con la superficie que cubre."),
        ("¿Qué se hace si la ficha técnica contradice las especificaciones?", "Se informa a quien inspecciona la obra", "No se resuelve por cuenta propia."),
    ],
    op=("Ficha de ejemplo (inventada) del producto «Membrana NR-ejemplo»: rendimiento de 3 m² por litro y por capa; envase de 4 litros; 2 capas indicadas; vigencia de 10 meses desde la fabricación; pictograma «inflamable». Un envase se fabricó hace 11 meses. Escribe (a) cuántos m² cubre un envase en una capa, (b) cuántos m² cubre con las 2 capas, (c) si puedes usar el envase y por qué y (d) qué documento consultas para saber cómo protegerte.",
        "(a) 3×4 son 12 m². (b) 12 dividido en 2 capas son 6 m². (c) No: la vigencia es de 10 meses y pasaron 11. (d) La hoja de datos de seguridad.",
        ["calcula m² de una capa", "reparte entre las capas", "concluye la vigencia", "nombra la hoja de datos"],
        ["hoja con las cuatro respuestas"],
        ["no dividir entre las capas", "usar un producto vencido", "confundir ficha con hoja de datos"],
        "Pregunta: «¿por qué se divide entre las 2 capas?». Si no responde, pídele que relea qué es una capa."),
    reinforce="Escribe cinco datos que puede traer una ficha técnica y para qué sirve cada uno.",
    extend="Explica por qué un producto vencido puede ser un problema aunque se vea igual que uno nuevo.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Obra «Condominio Estero» (ficticia): planilla de superficies a impermeabilizar: baño 12 m², cocina 10 m², terraza 18 m². "
     "Las especificaciones del proyecto piden impermeabilizar 44 m² y usar el producto «P1» en la terraza; en bodega solo hay el producto «P2». "
     "Hallazgos del revisor: 2 envases de P2 sin etiqueta legible y un panel aislante húmedo, con la caja rota. Hay 8 envases de P2 en bodega, incluidos los 2 sin etiqueta.")
build(
    O1, 3, F,
    use="Aprenderé a analizar un caso en papel: comparar una planilla con las especificaciones, detectar sustituciones de productos y decidir qué se informa.",
    prior=["Sé leer una ficha técnica.", "Sé sumar superficies.", "Sé que las diferencias entre documentos se informan."],
    explain=[
        "Un revisor compara tres cosas: la planilla de superficies, las especificaciones del proyecto y lo que hay en bodega. Primero suma las superficies de la planilla y las compara con lo que piden las especificaciones; si no coinciden, hay una diferencia. Luego revisa que cada producto sea el especificado para ese lugar. Una sustitución de producto, es decir, usar uno distinto al especificado, no la decide quien trabaja: la autoriza el proyectista o la inspección técnica de obra.",
        "También revisa el estado de los materiales: un envase sin etiqueta legible no se usa y un material dañado o mojado se informa, porque puede haber perdido sus propiedades. El revisor no corrige por su cuenta: deja un registro con qué encontró, dónde, cuándo y quién lo informó. Todos los datos de este caso son inventados.",
        TAIL,
    ],
    vocab=[("planilla de superficies", "tabla con las superficies de cada recinto o elemento"), ("sustitución", "uso de un producto distinto del especificado"), ("especificaciones del proyecto", "documento que fija qué producto y calidad se usan en cada lugar"), ("inspección técnica de obra", "revisión del cumplimiento del proyecto por un profesional"), ("registro", "documento donde se anota lo encontrado")],
    worked=[
        ("Comparar superficies", "Una planilla de ejemplo suma 25 m² y las especificaciones piden 30 m². ¿Hay diferencia? ¿De cuánto?", ["Se comparan los dos totales.", "30 menos 25 son 5 m² de diferencia."], "Sí, 5 m²"),
        ("Detectar una sustitución", "Las especificaciones piden el producto A para un cielo y en bodega solo hay el producto B. ¿Se puede usar B?", ["Usar B sería una sustitución.", "Una sustitución la autoriza el proyectista, no quien trabaja."], "No, hasta que lo autorice el proyectista"),
    ],
    mistakes=[("Usar el producto que hay porque «es parecido» al especificado.", "Una sustitución no autorizada puede dejar la superficie sin la protección esperada.", "Informa la diferencia y espera la decisión del proyectista."),
              ("Ajustar la planilla para que coincida con las especificaciones.", "Alterar un dato oculta un error de cantidad.", "Deja la diferencia registrada e informa.")],
    T=[
        ("abc", "En Construcción (terminaciones): ¿qué es una sustitución de producto?", "Usar un producto distinto del especificado", "Devolver un producto al proveedor", "Usar menos producto del necesario", "Sustituir es reemplazar el producto especificado por otro; debe autorizarse."),
        ("abc", "¿Quién autoriza el uso de un producto distinto al especificado?", "El proyectista o la inspección técnica de obra", "Cualquier integrante de la cuadrilla", "El proveedor de bodega", "Los cambios de especificación los decide quien diseña o inspecciona."),
        ("abc", "Un material aparece mojado y con la caja rota. ¿Qué corresponde?", "Informarlo y no usarlo hasta que se decida", "Usarlo igual, si se ve seco por dentro", "Secarlo al sol y usarlo", "Un material dañado puede haber perdido sus propiedades; se informa."),
        ("=", "{F} ¿Cuántos m² suman las tres superficies de la planilla?", "12+10+18", "Se suman baño, cocina y terraza.", " m²"),
        ("=", "{F} ¿Cuál es la diferencia entre lo que piden las especificaciones y lo que suma la planilla?", "44-(12+10+18)", "Se resta el total de la planilla de lo que piden las especificaciones.", " m²"),
        ("abc", "{F} ¿Qué producto piden las especificaciones para la terraza?", "P1", "P2", "Cualquiera", "Las especificaciones piden P1 en la terraza."),
        ("abc", "{F} En bodega solo hay P2. ¿Qué corresponde hacer?", "Informar la diferencia y esperar la autorización del proyectista", "Usar P2 en la terraza porque está disponible", "Pedir al proveedor que cambie la etiqueta a P1", "Usar P2 sería una sustitución no autorizada; no se cambian etiquetas."),
        ("=", "{F} Si los 2 envases sin etiqueta no se pueden usar, ¿cuántos envases de P2 quedan utilizables?", "8-2", "Se restan los envases sin etiqueta de los 8 que hay.", " envases"),
        ("abc", "{F} ¿Qué se hace con el panel aislante húmedo y con la caja rota?", "Informarlo y no usarlo hasta que se decida", "Usarlo si solo la caja está dañada", "Mezclarlo con paneles secos", "Un material dañado se informa y no se usa hasta evaluarlo."),
        ("ab", "{F} Un compañero propone anotar 44 m² en la planilla para que cuadre con las especificaciones. ¿Qué respuesta es correcta?", "No: la planilla debe reflejar la realidad y la diferencia se informa", "Sí: así los documentos coinciden", "Alterar un dato oculta un posible error de cantidad."),
        ("abc", "{F} Un compañero dice que P2 «es casi lo mismo» que P1 y propone usarlo en la terraza. ¿Qué corresponde?", "Aunque se parezca, solo el proyectista puede autorizar el cambio", "Usarlo, porque la terraza quedaría protegida igual", "Usarlo solo en la mitad de la terraza", "Parecido no significa equivalente: la sustitución la autoriza quien diseña, no quien ejecuta."),
        ("=", "{F} Si la terraza tuviera 22 m² en vez de 18, ¿cuántos m² sumaría la planilla?", "12+10+22", "Se reemplaza la terraza por 22 m² y se suman los tres recintos.", " m²"),
        ("abc", "{F} El supervisor pide un registro del hallazgo de los envases sin etiqueta. ¿Qué incluye?", "Cuántos son, dónde están, quién los detectó y la fecha", "Solo el nombre del proveedor", "El precio de cada envase", "El registro deja constancia de cantidad, lugar, responsable y fecha."),
    ],
    ctx=("abc", "Revisando la bodega de ejemplo, ves a un compañero subir a una pila inestable de envases para alcanzar una caja. ¿Qué haces?", "Avisarle que se detenga y avisar al responsable para retirar los envases con seguridad", "Sujetar la pila con tu cuerpo", "Dejar que termine y avisar al final", "Una pila inestable puede caer sobre alguien; se detiene la tarea y se avisa."),
    sc=[
        ("¿Quién autoriza una sustitución de producto?", "El proyectista o la inspección técnica de obra", "La decisión no es de quien ejecuta el trabajo."),
        ("En Construcción (terminaciones): ¿qué se hace con un envase sin etiqueta?", "No se usa y se informa al responsable", "Sin etiqueta no se conocen sus peligros."),
        ("¿Se puede cambiar la planilla para que cuadre con las especificaciones?", "No, se informa la diferencia", "Cambiar datos oculta un posible error."),
    ],
    op=("Caso de ejemplo (inventado): planilla de la obra «Edificio Faro»: dormitorios 20 m², baños 8 m², azotea 24 m². Las especificaciones piden 56 m² y producto «Q1» en la azotea; en bodega hay solo «Q2» y un envase de Q2 sin etiqueta. Escribe (a) cuántos m² suma la planilla, (b) la diferencia con las especificaciones, (c) qué haces con Q2 en la azotea y (d) qué haces con el envase sin etiqueta.",
        "(a) 20+8+24 son 52 m². (b) 56 menos 52 son 4 m². (c) No uso Q2: informo la diferencia y espero la autorización del proyectista. (d) No lo uso e informo al responsable para identificar su contenido.",
        ["suma las superficies", "calcula la diferencia", "no sustituye sin autorización", "no usa el envase sin etiqueta"],
        ["hoja con las cuatro respuestas"],
        ["usar Q2 por disponibilidad", "ajustar la planilla", "usar el envase sin etiqueta"],
        "Pregunta: «¿quién puede autorizar usar Q2?». Si no responde, pídele que relea la definición de sustitución."),
    reinforce="Inventa una planilla de tres recintos, compárala con un total de especificaciones y escribe la diferencia.",
    extend="Explica qué consecuencias puede tener usar un producto distinto al especificado en una terraza.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (cubicación de ejemplo, inventada). Obra «Residencia Duna» (ficticia): superficie a impermeabilizar de 60 m². Producto ficticio «Membrana ZR-ejemplo»: rendimiento de ejemplo de 3 m² por litro y por capa, 2 capas, envase de 5 litros, precio de ejemplo $40.000 por envase. "
     "Aislante: 45 m² a cubrir con paneles que cubren medio m² cada uno (2 paneles por m²); pérdida de ejemplo del 10 %; precio de ejemplo $2.000 por panel.")
build(
    O1, 4, F,
    use="Aprenderé a calcular en una planilla la cantidad de producto y de paneles necesarios con rendimiento, capas y pérdida, y el costo con precios de ejemplo.",
    prior=["Sé qué es el rendimiento y la capa.", "Sé calcular un porcentaje simple.", "Sé multiplicar y dividir con números enteros."],
    explain=[
        "Para calcular la cantidad de un producto que se aplica por capas se usa esta lógica de planilla: litros por capa = superficie dividida por el rendimiento; litros totales = litros por capa multiplicados por el número de capas; envases = litros totales divididos por los litros de cada envase. Cada dato sale de la ficha técnica; los de este caso son de ejemplo. Si la división no es exacta, se pide un envase más, porque los envases se compran completos.",
        "Para los paneles se divide la superficie por lo que cubre cada panel o se multiplica por los paneles de cada m². A esa cantidad se le suma la pérdida, un porcentaje por cortes y sobrantes. El costo se calcula multiplicando cantidades por precios. Estos cálculos son de planilla y no enseñan a aplicar productos ni a instalar paneles: eso lo enseña un instructor autorizado, con las indicaciones del fabricante y la norma vigente.",
        TAIL,
    ],
    vocab=[("litros por capa", "superficie dividida por el rendimiento"), ("litros totales", "litros por capa multiplicados por el número de capas"), ("envase", "unidad en que se compra el producto"), ("pérdida", "porcentaje de ejemplo por cortes y sobrantes"), ("costo", "cantidad multiplicada por el precio")],
    worked=[
        ("Litros de producto", "Un caso de ejemplo cubre 20 m² con un producto de 2 m² por litro y por capa y 1 capa. ¿Cuántos litros hacen falta?", ["Litros por capa son 20 divididos en 2.", "Con 1 capa, los litros totales son 10."], "10 litros"),
        ("Cantidad de paneles", "Un caso de ejemplo cubre 10 m² con paneles de medio m² cada uno. ¿Cuántos paneles se necesitan sin pérdida?", ["Cada m² necesita 2 paneles.", "10 por 2 son 20."], "20 paneles"),
    ],
    mistakes=[("Olvidar multiplicar por el número de capas.", "El producto se gasta en cada capa y el pedido quedaría corto.", "Calcula los litros por capa y multiplícalos por las capas."),
              ("Pedir 7,5 envases como si se pudieran comprar fracciones.", "Los envases se compran completos.", "Redondea hacia arriba al envase completo siguiente.")],
    T=[
        ("abc", "En Construcción (terminaciones): ¿cómo se obtienen los litros por capa?", "Dividiendo la superficie por el rendimiento", "Multiplicando la superficie por el rendimiento", "Sumando superficie y rendimiento", "El rendimiento son m² por litro; la superficie dividida por él da los litros."),
        ("abc", "Si la división de envases no es exacta, ¿qué se hace en la planilla?", "Se pide un envase completo más", "Se pide la mitad de un envase", "Se descuenta un envase", "Los envases se compran completos, por eso se redondea hacia arriba."),
        ("abc", "¿Para qué se suma una pérdida a los paneles?", "Para cubrir cortes y sobrantes", "Para que cuesten más", "Para aumentar la superficie cubierta", "La pérdida cubre lo que se corta o sobra; no cambia la superficie."),
        ("=", "{F} ¿Cuántos litros por capa necesita la superficie?", "60//3", "Se divide la superficie por el rendimiento de 3 m² por litro.", " litros"),
        ("=", "{F} ¿Cuántos litros se necesitan con las 2 capas?", "60//3*2", "Los litros de una capa se multiplican por las 2 capas.", " litros"),
        ("=", "{F} ¿Cuántos envases de 5 litros se necesitan?", "60//3*2//5", "Los litros totales se dividen por los 5 litros de cada envase.", " envases"),
        ("=", "{F} ¿Cuánto cuestan los envases al precio de ejemplo?", "60//3*2//5*40000", "Se multiplican los envases por el precio de cada uno.", " pesos"),
        ("=", "{F} ¿Cuántos paneles se necesitan para los 45 m² sin pérdida?", "45*2", "Se multiplican los m² por los 2 paneles de cada m².", " paneles"),
        ("=", "{F} ¿Cuántos paneles equivalen a la pérdida del 10 %?", "45*2*10//100", "Se calcula el 10 % de los paneles sin pérdida.", " paneles"),
        ("=", "{F} ¿Cuántos paneles se piden en total, con la pérdida?", "45*2+45*2*10//100", "A los paneles sin pérdida se les suma el 10 %.", " paneles"),
        ("=", "{F} ¿Cuánto cuestan los paneles pedidos al precio de ejemplo?", "(45*2+45*2*10//100)*2000", "Se multiplican los paneles pedidos por el precio de cada uno.", " pesos"),
        ("abc", "{F} Una persona calcula 120 litros para la membrana. ¿Qué error pudo cometer?", "Multiplicó la superficie por 2 capas sin dividir por el rendimiento", "Dividió dos veces por el rendimiento", "Sumó las capas al rendimiento", "60 por 2 es 120: omitió dividir por el rendimiento de 3 m² por litro."),
        ("ab", "{F} Un estudiante dice: «con este cálculo ya sé aplicar la membrana». ¿Qué respuesta es correcta?", "No: el cálculo es de planilla; aplicar el producto exige instructor y las indicaciones del fabricante", "Sí: calcular los litros es lo mismo que aplicar", "Calcular una cantidad no enseña cómo se aplica el producto."),
    ],
    ctx=("abc", "Para medir la superficie del techo de ejemplo, un compañero propone caminar sobre el borde sin protección. ¿Qué corresponde?", "No hacerlo: la medición se hace en el plano o por personal autorizado con protecciones", "Hacerlo con cuidado", "Hacerlo si alguien lo vigila desde abajo", "El trabajo en altura exige autorización y protecciones; que alguien vigile no evita la caída."),
    sc=[
        ("¿Cómo se calculan los litros totales de un producto por capas?", "Litros por capa multiplicados por el número de capas", "Cada capa gasta la misma cantidad de producto."),
        ("En Construcción (terminaciones): ¿por qué se redondea hacia arriba la cantidad de envases?", "Porque los envases se compran completos", "Un envase incompleto no se puede comprar."),
        ("¿Quién enseña a aplicar un producto?", "Un instructor autorizado, con las indicaciones del fabricante", "Este cuaderno solo calcula con datos de ejemplo."),
    ],
    op=("Caso de ejemplo (inventado): superficie de 48 m²; membrana con rendimiento de 4 m² por litro y por capa, 2 capas, envases de 6 litros, precio de ejemplo $30.000 por envase. Aislante de 20 m² con 2 paneles por m², pérdida de ejemplo del 10 % y $1.500 por panel. Escribe (a) los litros totales, (b) los envases, (c) el costo de la membrana, (d) los paneles con pérdida y (e) el costo de los paneles.",
        "(a) 48 dividido en 4 son 12 litros por capa; con 2 capas, 24 litros. (b) 24 dividido en 6 son 4 envases. (c) 4×30.000 son 120.000 pesos. (d) 20×2 son 40 paneles; el 10 % es 4; en total 44 paneles. (e) 44×1.500 son 66.000 pesos.",
        ["calcula litros por capa y totales", "calcula envases", "calcula el costo", "suma la pérdida", "calcula el costo de paneles"],
        ["hoja con cálculos"],
        ["no multiplicar por las capas", "olvidar la pérdida", "no dividir por el rendimiento"],
        "Pregunta: «¿qué dato de la ficha usas para los litros?». Si no responde, pídele que relea el rendimiento."),
    reinforce="Calcula los litros de un producto de 2 m² por litro, 1 capa, para 30 m² (datos de ejemplo).",
    extend="Explica por qué una pérdida mal estimada puede dejar sin material al final de la obra.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 5 (obra de ejemplo, inventada). Obra «Cocina Alelí» (ficticia): se arman e instalan muebles de cocina en una vivienda. Cuadrilla de 4 personas (2 parejas). Hay 12 tableros por trasladar al lugar de trabajo. "
     "Riesgos anotados: atrapamiento de dedos en puertas y bisagras, cortes con herramientas, sobreesfuerzo al mover tableros pesados, polvo de los tableros, vuelco de muebles altos mal fijados y contacto con instalaciones eléctricas o sanitarias ocultas en la pared. "
     "Medidas anotadas: traslado de tableros entre dos personas, revisión del plano de instalaciones con el responsable antes de perforar, mascarilla, lentes, guantes y capacitación.")
build(
    O2, 1, F,
    use="Aprenderé qué es armar e instalar muebles, tabiques y hojas de puertas y ventanas, y cuáles son los riesgos y las reglas generales de prevención de estas tareas.",
    prior=["Sé qué es la jerarquía de controles.", "Sé dividir números pequeños.", "Sé leer una ficha de obra."],
    explain=[
        "Armar un mueble es unir sus piezas para formar un módulo; instalarlo es dejarlo fijo en su lugar de la vivienda. Los muebles de cocina, los clósets y los muebles de baño se organizan en módulos, y los tabiques dividen espacios. La hoja de una puerta o ventana es la parte que se abre y se cierra, y el marco es la parte fija que la rodea. Los herrajes son piezas, como bisagras y correderas, que permiten mover o unir partes. Cómo se arman, se perforan y se instalan estas piezas lo enseña un instructor autorizado con las instrucciones del fabricante; este cuaderno no incluye esos pasos.",
        "Los riesgos más frecuentes son el atrapamiento de dedos, los cortes, el sobreesfuerzo (esfuerzo excesivo del cuerpo al mover o levantar peso), el polvo y el vuelco de muebles altos que no están fijados. Antes de perforar una pared, el responsable revisa el plano de instalaciones, porque pueden existir cañerías o cables ocultos. Siguiendo la jerarquía de controles, primero se organiza el trabajo (traslados entre dos personas, ayudas mecánicas, planos revisados), y al final se usan EPP como guantes, lentes y mascarilla. Las herramientas las usa solo personal capacitado y autorizado.",
        TAIL,
    ],
    vocab=[("módulo", "unidad de un mueble que se arma por separado"), ("hoja", "parte de una puerta o ventana que se abre y se cierra"), ("marco", "parte fija que rodea a la hoja"), ("herrajes", "piezas como bisagras y correderas que permiten mover o unir partes"), ("sobreesfuerzo", "esfuerzo excesivo del cuerpo al mover o levantar peso"), ("vuelco", "caída de un mueble alto por estar mal fijado o apoyado")],
    worked=[
        ("Identificar un herraje", "Una pieza de ejemplo permite que una puerta de mueble gire al abrirse. ¿Es un herraje o un módulo?", ["La pieza permite mover una parte del mueble.", "Es un herraje."], "Un herraje"),
        ("Repartir traslados", "Hay 10 tableros y 2 parejas, cada una traslada tableros por turnos iguales. ¿Cuántos tableros traslada cada pareja?", ["Se dividen los tableros entre las parejas.", "10 dividido en 2 son 5."], "5 tableros"),
    ],
    mistakes=[("Cargar un tablero pesado solo «para ir más rápido».", "El sobreesfuerzo puede causar lesiones.", "Se traslada entre dos personas o con ayudas, como indica el plan."),
              ("Perforar la pared sin revisar el plano de instalaciones porque «no se ve nada».", "Pueden existir cables o cañerías ocultas.", "El responsable revisa el plano antes y autoriza a personal capacitado.")],
    T=[
        ("abc", "En Construcción (muebles): ¿qué son los herrajes?", "Piezas como bisagras y correderas que permiten mover o unir partes", "Las tablas que forman los costados del mueble", "La pintura del mueble", "Los herrajes son piezas funcionales; las tablas y la pintura no lo son."),
        ("abc", "¿Qué es el vuelco de un mueble alto?", "Su caída por estar mal fijado o apoyado", "El desgaste de su pintura", "La rotura de una bisagra", "El vuelco es la caída del mueble completo."),
        ("abc", "¿Qué es el sobreesfuerzo?", "El esfuerzo excesivo del cuerpo al mover o levantar peso", "El cansancio por falta de sueño", "El ruido de una herramienta", "El sobreesfuerzo se produce al mover pesos que el cuerpo no soporta con seguridad."),
        ("=", "{F} Si los 12 tableros se reparten por igual entre las 2 parejas, ¿cuántos traslados hace cada pareja?", "12//2", "Se dividen los tableros entre las parejas.", " traslados"),
        ("abc", "{F} ¿Qué medida de la ficha es administrativa?", "Revisar el plano de instalaciones con el responsable antes de perforar", "Usar mascarilla", "Usar lentes", "Revisar planos organiza el trabajo; mascarilla y lentes son EPP."),
        ("abc", "{F} ¿Qué riesgo se previene al revisar el plano de instalaciones antes de perforar?", "El contacto con instalaciones eléctricas o sanitarias ocultas", "El polvo de los tableros", "El atrapamiento de dedos", "El plano muestra cables y cañerías ocultas; el polvo y el atrapamiento se previenen de otro modo."),
        ("=", "{F} Cada integrante recibe mascarilla, lentes y guantes. ¿Cuántas piezas de EPP se entregan?", "4*3", "Se multiplican las 4 personas por las 3 piezas de cada una.", " piezas"),
        ("abc", "{F} Una persona propone cargar un tablero sola para avanzar más rápido. ¿Qué corresponde?", "Trasladarlo entre dos personas, como indica la ficha", "Cargarlo si es una persona fuerte", "Cargarlo si descansa después", "La ficha indica traslado entre dos personas para evitar el sobreesfuerzo."),
        ("abc", "{F} Se ve un mueble alto apoyado sin fijar. ¿Qué corresponde?", "Avisar al responsable para que se asegure con personal autorizado", "Probar su estabilidad empujándolo", "Dejarlo así, porque no se ha caído", "Un mueble mal fijado puede volcar; se avisa a quien puede asegurarlo."),
        ("ab", "{F} Un compañero dice: «con guantes puedo perforar la pared sin revisar el plano». ¿Qué respuesta es correcta?", "No: los guantes no evitan tocar un cable o una cañería oculta; se revisa el plano", "Sí: los guantes protegen de todo", "Los guantes protegen las manos pero no reemplazan la revisión previa del plano."),
        ("abc", "{F} Una estudiante afirma: «ya sé qué son los herrajes, así que puedo instalar un mueble». ¿Qué respuesta es correcta?", "No: esa tarea exige instructor autorizado y norma vigente", "Sí: con conocer los términos basta", "Sí, si usa mascarilla y lentes", "Conocer vocabulario no habilita; el EPP tampoco reemplaza la autorización."),
        ("=", "{F} Si llegaran 6 tableros más y se reparten por igual entre las 2 parejas, ¿cuántos traslados hace cada pareja?", "(12+6)//2", "Se suman los tableros y se dividen entre las parejas.", " traslados"),
        ("abc", "{F} El prevencionista pide registrar la falta de fijación de un mueble. ¿Qué datos mínimos lleva el registro?", "Qué mueble, dónde, quién lo detectó y la fecha", "Solo el nombre de la marca", "Solo la hora de salida del turno", "Un registro útil deja constancia de qué, dónde, quién y cuándo."),
    ],
    ctx=("abc", "En una obra de ejemplo, un mueble alto mal fijado empieza a inclinarse hacia un compañero. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias si hay heridos", "Intentar sostenerlo con el cuerpo", "Apoyarlo con una escalera y seguir", "Sostener un mueble que vuelca puede causar otro accidente; se mantiene la distancia y se avisa."),
    sc=[
        ("En Construcción (muebles): ¿qué es la hoja de una puerta?", "La parte que se abre y se cierra", "El marco es la parte fija que rodea la hoja."),
        ("¿Qué se hace antes de perforar una pared de una vivienda?", "El responsable revisa el plano de instalaciones", "Pueden existir cables o cañerías ocultas."),
        ("¿Quién puede instalar muebles y usar herramientas?", "Personal capacitado y autorizado, con instructor y norma vigente", "Este cuaderno no habilita para trabajar."),
    ],
    op=("Obra de ejemplo «Baño Calma» (ficticia): se instalan muebles de baño con una cuadrilla de 6 personas (3 parejas). Hay 18 tableros por trasladar. Riesgos anotados: sobreesfuerzo, cortes y cables ocultos. Medidas disponibles: traslado en pareja, revisión del plano de instalaciones, guantes y lentes. Escribe (a) cuántos tableros traslada cada pareja si se reparten por igual, (b) cuántas piezas de EPP necesitas si cada persona recibe guantes y lentes, (c) cuál medida es administrativa y cuáles son EPP y (d) qué haces si un mueble alto vuelca hacia alguien.",
        "(a) 18 dividido en 3 son 6 tableros. (b) 6×2 son 12 piezas. (c) La revisión del plano y el traslado en pareja son administrativas; guantes y lentes son EPP. (d) No me acerco a la zona de riesgo, aviso a un adulto responsable y a emergencias si hay heridos.",
        ["reparte los tableros", "calcula el EPP", "clasifica las medidas", "avisa sin acercarse al riesgo"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre 6 personas en vez de 3 parejas", "llamar EPP a la revisión del plano", "proponer sostener el mueble"],
        "Pregunta: «¿por qué se revisa el plano antes de perforar?». Si no responde, pídele que relea los riesgos de la ficha."),
    reinforce="Escribe tres riesgos de instalar muebles en una vivienda y una medida de prevención para cada uno.",
    extend="Explica con un ejemplo inventado por qué un mueble alto sin fijar puede ser un riesgo aunque parezca estable.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 6 (plano de detalle de ejemplo, inventado). Pared de cocina de 300 cm de largo, vista de frente (elevación). Muebles bajos de 85 cm de alto y 55 cm de fondo, en 4 módulos: B1 de 60 cm (1 puerta), B2 de 80 cm (2 puertas), B3 de 60 cm (1 puerta) y B4 de 90 cm (2 puertas). "
     "Entre el último módulo y la pared queda un relleno. Despiece del módulo B1: 2 laterales, 1 base y 1 repisa. Cada puerta lleva 2 bisagras. Todas las medidas están en cm.")
build(
    O2, 2, F,
    use="Aprenderé a leer un plano de detalle y un despiece de muebles: módulos, cotas, elevación, herrajes y holguras.",
    prior=["Sé qué es un módulo y un herraje.", "Sé sumar y restar medidas en cm.", "Sé que las diferencias entre documentos se informan."],
    explain=[
        "El plano de detalle muestra con más precisión cómo es un elemento: sus medidas, sus piezas y sus uniones. La elevación es la vista de frente de una pared o mueble. La cota es el número que indica una medida. El despiece es la lista de piezas con sus cantidades y medidas. El relleno es una pieza que cubre el espacio que sobra entre el último módulo y la pared. La holgura es un espacio pequeño y previsto entre dos piezas que permite que una se mueva sin rozar; su valor lo fija el proyecto, aquí solo se usan valores de ejemplo.",
        "Los planos de detalle y las especificaciones deben coincidir. Si una medida del plano no calza con el espacio real o con otro documento, no se recorta ni se modifica nada por cuenta propia: se registra la diferencia y se informa al proyectista o al responsable. Esta clase solo enseña a leer y calcular; el armado y la instalación los enseña un instructor autorizado.",
        TAIL,
    ],
    vocab=[("plano de detalle", "dibujo que muestra con precisión medidas, piezas y uniones de un elemento"), ("elevación", "vista de frente de una pared o mueble"), ("cota", "número que indica una medida"), ("despiece", "lista de piezas con sus cantidades y medidas"), ("relleno", "pieza que cubre el espacio que sobra entre el último módulo y la pared"), ("holgura", "espacio pequeño previsto entre dos piezas para que una se mueva sin rozar")],
    worked=[
        ("Sumar cotas", "Una elevación de ejemplo muestra tres módulos de 50, 70 y 40 cm. ¿Cuántos cm suman?", ["Se suman las cotas de los tres módulos.", "50 más 70 más 40 son 160."], "160 cm"),
        ("Calcular el relleno", "Una pared de ejemplo mide 200 cm y los módulos suman 185 cm. ¿Cuántos cm de relleno quedan?", ["Se resta lo que ocupan los módulos del largo de la pared.", "200 menos 185 son 15."], "15 cm"),
    ],
    mistakes=[("Confundir la holgura con una falla de armado.", "La holgura es un espacio previsto por el proyecto.", "Si el plano indica holgura, forma parte del diseño."),
              ("Recortar un módulo porque «no calza» en el espacio.", "Modificar piezas sin autorización cambia el diseño.", "Registra la diferencia e informa al proyectista o al responsable.")],
    T=[
        ("abc", "En Construcción (muebles): ¿qué es la elevación de una pared?", "La vista de frente de la pared o del mueble", "La vista desde arriba del recinto", "La lista de piezas con cantidades", "La elevación es la vista frontal; la vista desde arriba es la planta y la lista es el despiece."),
        ("abc", "¿Qué es el despiece de un mueble?", "La lista de piezas con sus cantidades y medidas", "El precio de cada pieza", "El dibujo de la pared completa", "El despiece ordena las piezas; no es un precio ni un dibujo de pared."),
        ("abc", "¿Qué es el relleno entre el último módulo y la pared?", "Una pieza que cubre el espacio que sobra", "Una bisagra adicional", "Un tipo de pintura", "El relleno cubre el espacio sobrante; no es un herraje ni una pintura."),
        ("=", "{F} ¿Cuántos cm ocupan los 4 módulos juntos?", "60+80+60+90", "Se suman las cotas de los cuatro módulos.", " cm"),
        ("=", "{F} ¿Cuántos cm de relleno quedan entre el último módulo y la pared?", "300-(60+80+60+90)", "Se resta lo que ocupan los módulos del largo de la pared.", " cm"),
        ("abc", "{F} ¿Cuántas puertas tiene el módulo B2?", "2", "1", "4", "La ficha anota que B2 lleva 2 puertas."),
        ("=", "{F} ¿Cuántas puertas hay en total en los 4 módulos?", "1+2+1+2", "Se suman las puertas de cada módulo.", " puertas"),
        ("=", "{F} Si cada puerta lleva 2 bisagras, ¿cuántas bisagras se necesitan en total?", "(1+2+1+2)*2", "Se multiplican las puertas por las bisagras de cada una.", " bisagras"),
        ("=", "{F} ¿Cuántas piezas tiene el módulo B1 según su despiece?", "2+1+1", "Se suman los laterales, la base y la repisa.", " piezas"),
        ("abc", "{F} Una persona mide la pared y encuentra 296 cm en vez de 300. ¿Qué corresponde?", "Registrar la diferencia e informar al proyectista o al responsable", "Recortar el módulo B4 sin avisar", "Ignorar la diferencia", "Una diferencia con el plano se informa; no se modifican piezas por cuenta propia."),
        ("ab", "{F} Un compañero dice: «el relleno es un error del plano, hay que quitarlo». ¿Qué es correcto?", "No: el relleno cubre un espacio previsto y no se elimina sin consultar", "Sí: todo el espacio debe ocuparlo un módulo", "En la ficha el relleno está previsto para el espacio sobrante entre módulo y pared."),
        ("=", "{F} Si se reemplaza B4 de 90 cm por un módulo de 100 cm, ¿cuántos cm de relleno quedarían?", "300-(60+80+60+100)", "Se vuelve a restar el nuevo ancho total del largo de la pared.", " cm"),
        ("abc", "{F} La lista de materiales compra 5 bisagras de más «por si acaso». ¿Cómo se registra la diferencia con el plano?", "Se anota lo comprado, lo que indica el plano y quién lo detectó", "Se ocultan las bisagras sobrantes", "No se registra, porque son pocas", "Las diferencias se registran con los dos datos y el responsable de la observación."),
    ],
    ctx=("abc", "En un taller de ejemplo, un compañero se sube a una escalera para mirar la elevación de un mueble alto y la escalera se mueve. ¿Qué haces?", "Avisarle que baje con cuidado y avisar al prevencionista", "Sujetar la escalera con el pie mientras él sigue", "Esperar a ver si se cae", "Una escalera inestable es un riesgo de caída; se detiene la tarea y se avisa."),
    sc=[
        ("En Construcción (muebles): ¿qué es una cota?", "El número que indica una medida", "La cota expresa una medida del plano."),
        ("¿Qué es la holgura?", "Un espacio pequeño previsto entre piezas para que una se mueva sin rozar", "No es una falla; el proyecto la prevé."),
        ("¿Qué se hace si el espacio real no coincide con el plano?", "Registrar la diferencia e informar al proyectista o al responsable", "No se recortan piezas por cuenta propia."),
    ],
    op=("Plano de ejemplo (inventado): pared de 240 cm con tres módulos bajos de 70, 70 y 60 cm. El módulo de 70 cm lleva 2 puertas; el de 60 cm lleva 1 puerta. Cada puerta lleva 2 bisagras. Escribe (a) cuántos cm ocupan los módulos, (b) cuántos cm de relleno quedan, (c) cuántas puertas y bisagras hay en total y (d) qué haces si al medir la pared encuentras 236 cm.",
        "(a) 70+70+60 son 200 cm. (b) 240 menos 200 son 40 cm. (c) 2+2+1 son 5 puertas; 5×2 son 10 bisagras. (d) Registro la diferencia (236 en lugar de 240) e informo al proyectista o al responsable, sin modificar piezas.",
        ["suma las cotas", "calcula el relleno", "calcula puertas y bisagras", "informa la diferencia"],
        ["hoja con las cuatro respuestas"],
        ["no sumar los tres módulos", "olvidar las bisagras", "recortar un módulo sin avisar"],
        "Pregunta: «¿cuántas puertas lleva cada módulo?». Si no responde, pídele que relea el enunciado."),
    reinforce="Dibuja una elevación sencilla de una pared con tres módulos y escribe las cotas y el relleno.",
    extend="Explica por qué una holgura mal prevista puede hacer que una puerta roce con el mueble vecino.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 7 (caso de ejemplo, inventado). Obra «Dormitorio Luna» (ficticia): clóset C1 para un nicho de 150 cm de ancho. El plano dibuja 3 módulos de 50, 50 y 60 cm. "
     "El plano dibuja 4 estantes por módulo y la lista de materiales compra 3 estantes por módulo. Cada módulo lleva 2 laterales, 1 techo y 1 base. Hojas de puerta: 3, una por módulo.")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso en papel: comparar el plano de un clóset con la medida del espacio, el despiece y la lista de materiales.",
    prior=["Sé leer un plano de detalle y un despiece.", "Sé sumar medidas en cm.", "Sé que las diferencias se informan."],
    explain=[
        "El nicho es el hueco de la pared donde irá un mueble. Antes de fabricar o comprar, quien revisa compara tres datos: lo que ocupa el mueble según el plano, la medida disponible del nicho y las cantidades de piezas de cada documento. Si el mueble es más ancho que el nicho no cabe, y no se resuelve recortando módulos por cuenta propia, porque eso cambia el diseño. Si el plano y la lista de materiales piden cantidades distintas, se calcula la diferencia y se informa.",
        "El revisor escribe un registro con lo encontrado: qué documento dice qué, cuál es la diferencia y quién la detectó. La decisión de modificar el plano o los materiales la toma el proyectista o el responsable. Todos los datos son inventados; el armado y la instalación del mueble lo enseña un instructor autorizado.",
        TAIL,
    ],
    vocab=[("nicho", "hueco de la pared donde irá un mueble"), ("lista de materiales", "documento que enumera las piezas y productos que se compran"), ("registro", "documento donde se anota lo encontrado"), ("diseño", "conjunto de decisiones del proyectista sobre medidas y piezas"), ("revisor", "persona que compara documentos y mediciones")],
    worked=[
        ("Ver si cabe", "Un nicho de ejemplo mide 120 cm y un mueble ocupa 110 cm. ¿Cabe?", ["Se compara lo que ocupa el mueble con la medida del nicho.", "110 es menor que 120, así que cabe."], "Sí, cabe"),
        ("Comparar cantidades", "El plano de ejemplo dibuja 8 repisas y la lista compra 6. ¿Cuántas faltan?", ["Se resta lo comprado de lo dibujado.", "8 menos 6 son 2."], "Faltan 2 repisas"),
    ],
    mistakes=[("Recortar un módulo para que el mueble quepa en el nicho.", "El recorte cambia el diseño y puede dañar el mueble.", "Registra la diferencia e informa al proyectista o al responsable."),
              ("Comprar solo lo que dice la lista sin comparar con el plano.", "Una lista incorrecta repite el error en la compra.", "Compara siempre el plano con la lista y informa las diferencias.")],
    T=[
        ("abc", "En Construcción (muebles): ¿qué es un nicho?", "El hueco de la pared donde irá un mueble", "La parte móvil de una puerta", "Una pieza que cubre un espacio sobrante", "El nicho es un hueco de la pared; la hoja y el relleno son otras cosas."),
        ("abc", "Un mueble es más ancho que su nicho. ¿Qué corresponde?", "Registrar la diferencia e informar al proyectista o al responsable", "Recortar un módulo para que quepa", "Forzarlo para que entre", "Cambiar el mueble cambia el diseño y lo decide el proyectista."),
        ("abc", "¿Qué contiene una lista de materiales?", "Las piezas y productos que se compran", "El dibujo de la pared", "Los riesgos de la obra", "La lista enumera lo que se compra; el dibujo y los riesgos están en otros documentos."),
        ("=", "{F} ¿Cuántos cm de ancho ocupan los 3 módulos juntos?", "50+50+60", "Se suman las cotas de los tres módulos.", " cm"),
        ("=", "{F} ¿Cuántos cm se pasa el clóset respecto del nicho?", "(50+50+60)-150", "Se resta el ancho del nicho de lo que ocupan los módulos.", " cm"),
        ("abc", "{F} ¿Cabe el clóset del plano en el nicho de 150 cm?", "No: ocupa 160 cm", "Sí: ocupa 150 cm", "Sí: ocupa 140 cm", "Los módulos suman 160 cm, más que los 150 cm del nicho."),
        ("=", "{F} ¿Cuántos estantes dibuja el plano en total?", "4*3", "Se multiplican los estantes por módulo por los 3 módulos.", " estantes"),
        ("=", "{F} ¿Cuántos estantes compra la lista de materiales en total?", "3*3", "Se multiplican los estantes por módulo por los 3 módulos.", " estantes"),
        ("=", "{F} ¿Cuántos estantes faltan en la lista respecto del plano?", "4*3-3*3", "Se restan los estantes de la lista de los dibujados en el plano.", " estantes"),
        ("abc", "{F} La lista compra menos estantes que el plano. ¿Qué corresponde?", "Anotar la diferencia e informar al proyectista o al responsable", "Comprar lo que dice la lista sin avisar", "Eliminar un estante del plano para que cuadre", "Una diferencia entre documentos se informa; no se ajusta a conveniencia."),
        ("ab", "{F} Un estudiante dice: «recortemos el módulo de 60 a 50 cm y así entra». ¿Qué es correcto?", "No: recortar un módulo cambia el diseño y lo decide el proyectista", "Sí: recortar es lo más simple", "El recorte modifica el diseño y puede comprometer el mueble."),
        ("=", "{F} Si el nicho midiera 165 cm, ¿cuántos cm de relleno quedarían tras los 3 módulos?", "165-(50+50+60)", "Se resta el ancho de los módulos de la medida del nicho.", " cm"),
        ("abc", "{F} El supervisor pide un registro de la diferencia de ancho. ¿Qué incluye?", "Plano 160 cm, nicho 150 cm, diferencia de 10 cm, quién lo detectó y la fecha", "Solo la palabra «no cabe»", "El nombre del fabricante de los muebles", "El registro deja los valores de cada documento, la diferencia y los datos de quien la detectó."),
    ],
    ctx=("abc", "Midiendo el nicho en una obra de ejemplo, una persona pisa el borde de una escalera sin firmeza y cae sobre un mueble. ¿Qué se hace según las reglas generales?", "No acercarse sin autorización a mover a la persona, avisar a un adulto responsable y a emergencias", "Levantarla rápido para que siga trabajando", "Esperar a que se recupere sola", "Mover a una persona caída puede empeorar una lesión; se avisa a quien corresponde y a emergencias."),
    sc=[
        ("¿Qué se hace si el mueble del plano no cabe en el nicho?", "Se registra la diferencia y se informa al proyectista o al responsable", "Recortar piezas cambia el diseño y no corresponde a quien instala."),
        ("En Construcción (muebles): ¿qué compara quien revisa un plano y una lista de materiales?", "Las cantidades de piezas de cada documento", "Las diferencias se calculan y se informan."),
        ("¿Quién decide modificar el plano o los materiales?", "El proyectista o el responsable", "La decisión no corresponde a quien instala."),
    ],
    op=("Caso de ejemplo (inventado): clóset para un nicho de 200 cm. El plano dibuja 3 módulos de 70 cm y 5 repisas por módulo; la lista de materiales compra 12 repisas. Escribe (a) cuántos cm ocupan los módulos, (b) si caben en el nicho y por qué, (c) cuántas repisas dibuja el plano y cuántas faltan en la lista y (d) qué registras.",
        "(a) 3×70 son 210 cm. (b) No caben: 210 es más que 200 y se pasan 10 cm. (c) El plano dibuja 3×5 son 15 repisas; la lista compra 12, faltan 3. (d) Registro ambas diferencias (10 cm de ancho y 3 repisas), quién las detectó y la fecha, y las informo al proyectista o al responsable.",
        ["suma el ancho", "concluye si cabe", "calcula las repisas faltantes", "registra e informa"],
        ["hoja con las cuatro respuestas"],
        ["recortar un módulo", "comprar solo lo de la lista", "no registrar quién lo detectó"],
        "Pregunta: «¿cuántos cm sobran del nicho?». Si no responde, pídele que reste 200 de 210."),
    reinforce="Inventa un nicho y tres módulos que no caben y escribe qué diferencia hay y a quién la informas.",
    extend="Explica por qué comprar piezas antes de comparar plano y lista puede costar más tiempo y dinero.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 8 (cubicación y control de ejemplo, inventados). Obra «Cocina Brisa» (ficticia): pared de 360 cm con módulos de 60 cm cada uno; cada módulo lleva 1 puerta y cada puerta 2 bisagras; precio de ejemplo $1.500 por bisagra. "
     "Una manilla por puerta, a $1.000 la unidad. Control de holgura de ejemplo: la holgura permitida entre la hoja de una puerta y su marco es de 1 a 3 cm. "
     "Registro: puerta P1, hoja de 80 cm en vano de 82 cm; puerta P2, hoja de 80 cm en vano de 85 cm.")
build(
    O2, 4, F,
    use="Aprenderé a calcular módulos, herrajes y costos en una planilla y a registrar un control de holgura con un rango de ejemplo.",
    prior=["Sé leer un despiece.", "Sé dividir y multiplicar.", "Sé comparar un valor medido con un rango."],
    explain=[
        "Para saber cuántos módulos iguales caben en una pared se divide el largo de la pared por el ancho de cada módulo. Con la cantidad de módulos se calculan las puertas y, con ellas, las bisagras y las manillas, multiplicando por las piezas de cada una. El costo se obtiene multiplicando cantidad por precio. Todos los datos de esta clase son de ejemplo.",
        "La holgura de una hoja es la diferencia entre el ancho del vano (el hueco del marco) y el ancho de la hoja. El proyecto fija un rango permitido; aquí se usa un rango de ejemplo de 1 a 3 cm. Quien controla anota las medidas en un registro y compara la holgura con el rango. Si queda fuera, no ajusta nada por su cuenta: informa al responsable. Este cuaderno no enseña a ajustar ni a instalar hojas.",
        TAIL,
    ],
    vocab=[("vano", "hueco del marco donde va la hoja"), ("holgura", "diferencia entre el ancho del vano y el de la hoja"), ("rango permitido", "valores mínimo y máximo aceptados"), ("registro de control", "documento donde se anotan medidas y conclusiones"), ("manilla", "pieza que sirve para abrir una puerta")],
    worked=[
        ("Módulos en una pared", "Una pared de ejemplo mide 240 cm y los módulos son de 80 cm. ¿Cuántos módulos caben?", ["Se divide el largo por el ancho de cada módulo.", "240 dividido en 80 son 3."], "3 módulos"),
        ("Calcular una holgura", "Un vano de ejemplo mide 91 cm y la hoja 89 cm. ¿Cuál es la holgura?", ["Se resta el ancho de la hoja del ancho del vano.", "91 menos 89 son 2."], "2 cm"),
    ],
    mistakes=[("Sumar el ancho de la hoja al del vano para obtener la holgura.", "La holgura es una diferencia, no una suma.", "Resta el ancho de la hoja del ancho del vano."),
              ("Ajustar la hoja a ojo para que la holgura «parezca» correcta.", "El control exige medir y registrar.", "Anota las medidas y, si queda fuera del rango, informa al responsable.")],
    T=[
        ("abc", "En Construcción (muebles): ¿qué es la holgura de una hoja de puerta?", "La diferencia entre el ancho del vano y el de la hoja", "La suma de los anchos del vano y la hoja", "El peso de la hoja", "La holgura se obtiene restando; no se suma ni se relaciona con el peso."),
        ("abc", "¿Qué es un rango permitido?", "Los valores mínimo y máximo aceptados", "El precio máximo de una puerta", "La cantidad de puertas por módulo", "El rango fija el mínimo y el máximo aceptados para una medida."),
        ("abc", "Una holgura queda fuera del rango permitido. ¿Qué corresponde?", "Registrar las medidas e informar al responsable", "Ajustar la hoja a ojo sin avisar", "Cambiar las medidas anotadas para que cumpla", "Un valor fuera de rango se registra tal cual y se informa."),
        ("=", "{F} ¿Cuántos módulos de 60 cm caben en la pared de 360 cm?", "360//60", "Se divide el largo de la pared por el ancho de cada módulo.", " módulos"),
        ("=", "{F} ¿Cuántas puertas hay en total?", "360//60", "Hay una puerta por módulo.", " puertas"),
        ("=", "{F} ¿Cuántas bisagras se necesitan en total?", "360//60*2", "Se multiplican las puertas por las 2 bisagras de cada una.", " bisagras"),
        ("=", "{F} ¿Cuánto cuestan las bisagras al precio de ejemplo?", "360//60*2*1500", "Se multiplican las bisagras por el precio de cada una.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan las manillas de todas las puertas?", "360//60*1000", "Se multiplican las manillas por el precio de cada una.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de bisagras y manillas?", "360//60*2*1500+360//60*1000", "Se suman el costo de las bisagras y el de las manillas.", " pesos"),
        ("=", "{F} ¿Cuántos cm de holgura tiene la puerta P1?", "82-80", "Se resta el ancho de la hoja del ancho del vano.", " cm"),
        ("abc", "{F} ¿Cumple la puerta P1 con el rango de ejemplo de 1 a 3 cm?", "Sí: 2 cm está dentro del rango", "No: 2 cm es menor que 1", "No: 2 cm es mayor que 3", "2 cm está entre 1 y 3 cm, por lo que cumple."),
        ("abc", "{F} ¿Qué corresponde con la puerta P2, cuya holgura es de 5 cm?", "Registrar que no cumple el rango e informar al responsable", "Registrar 3 cm para que cumpla", "Dejarla sin registrar", "Un valor fuera de rango se registra tal cual y se informa."),
        ("ab", "{F} Un compañero dice: «la hoja de P2 se ve bien, no hace falta registrar la medida». ¿Qué es correcto?", "No: el control exige medir y registrar aunque se vea bien", "Sí: si se ve bien basta", "A simple vista no se puede comparar una holgura con un rango."),
    ],
    ctx=("abc", "Para medir la holgura de una puerta alta de ejemplo, un compañero se sube a una silla giratoria. ¿Qué corresponde?", "No hacerlo: se usa un apoyo estable autorizado y se avisa al prevencionista", "Subir rápido a medir", "Subir si alguien sostiene la silla", "Una silla giratoria es un apoyo inestable y puede provocar una caída."),
    sc=[
        ("¿Cómo se calculan los módulos que caben en una pared?", "Dividiendo el largo de la pared por el ancho de cada módulo", "La división da cuántos módulos iguales caben."),
        ("En Construcción (muebles): ¿cómo se calcula la holgura de una hoja?", "Restando el ancho de la hoja del ancho del vano", "La holgura es una diferencia entre dos medidas, no una suma."),
        ("¿Quién ajusta las hojas de puertas o ventanas?", "Personal capacitado y autorizado, con instructor y norma vigente", "Este cuaderno solo enseña a calcular y registrar."),
    ],
    op=("Caso de ejemplo (inventado): pared de 420 cm con módulos de 70 cm; 1 puerta por módulo; 2 bisagras por puerta a $1.200 cada una. Rango de holgura de ejemplo: 1 a 3 cm. Puerta Q1: vano 71 cm y hoja 69 cm; puerta Q2: vano 74 cm y hoja 69 cm. Escribe (a) cuántos módulos y puertas hay, (b) cuántas bisagras y cuánto cuestan, (c) la holgura de Q1 y Q2 y si cumplen y (d) qué haces con la que no cumple.",
        "(a) 420 dividido en 70 son 6 módulos y 6 puertas. (b) 6×2 son 12 bisagras; 12×1.200 son 14.400 pesos. (c) Q1: 71 menos 69 son 2 cm, cumple. Q2: 74 menos 69 son 5 cm, no cumple. (d) Registro la medida real de Q2 e informo al responsable, sin ajustarla por mi cuenta.",
        ["calcula módulos y puertas", "calcula bisagras y costo", "calcula las holguras", "informa lo que no cumple"],
        ["hoja con cálculos"],
        ["sumar anchos para la holgura", "registrar un valor falso", "ajustar la hoja sin autorización"],
        "Pregunta: «¿qué operación usas para la holgura?». Si no responde, pídele que relea qué es la holgura."),
    reinforce="Calcula cuántos módulos de 50 cm caben en una pared de 300 cm y cuántas bisagras necesitas si cada módulo lleva 2 puertas (datos de ejemplo).",
    extend="Explica por qué una holgura demasiado pequeña o demasiado grande puede ser un problema para una puerta.",
)

# ============================================================ OAM-03, clase 1
F = ("Ficha 9 (obra de ejemplo, inventada). Obra «Baño Loma» (ficticia): se revisten el piso y los muros de un baño con cerámica. Cuadrilla de 5 personas. Se descargan 20 cajas de cerámica de 20 kg cada una (dato de ejemplo). "
     "Riesgos anotados: polvo al cortar piezas, cortes con bordes de piezas, sobreesfuerzo al mover cajas, contacto del adhesivo con piel y ojos, resbalones en pisos húmedos o recién revestidos y dolor por posturas prolongadas de rodillas. "
     "Medidas anotadas: hoja de datos de seguridad del adhesivo disponible, mascarilla, lentes, guantes, rodilleras, traslado de cajas en pareja, señalizar y cerrar el paso al piso recién revestido y pausas.")
build(
    O3, 1, F,
    use="Aprenderé qué es revestir pisos, muros y cielos, qué riesgos tiene la tarea y qué reglas generales de prevención y ergonomía se aplican.",
    prior=["Sé qué es la jerarquía de controles.", "Sé multiplicar y dividir números pequeños.", "Sé leer una ficha de obra."],
    explain=[
        "Revestir es cubrir una superficie, como un piso, un muro o un cielo, con un material de terminación: cerámica, porcelanato, madera, papel u otro. El revestimiento da protección y buena presentación al elemento. Se une a la superficie con un adhesivo, un producto que pega y cuyas indicaciones de uso entrega el fabricante. Quien revisa un trabajo de revestimiento verifica medidas, horizontalidad y verticalidad. Cómo se revisten las superficies lo enseña un instructor autorizado con las instrucciones del fabricante; este cuaderno no incluye esos pasos.",
        "Los riesgos más frecuentes son el polvo y los cortes al cortar piezas, el sobreesfuerzo al mover cajas, el contacto con adhesivos, los resbalones y el dolor por posturas forzadas. La ergonomía busca adaptar el trabajo a las personas, con pausas, rodilleras y traslados en pareja. Un piso recién revestido se señaliza y se cierra el paso hasta que lo autorice el responsable. Según la jerarquía de controles, primero se organiza el trabajo y se protege colectivamente, y al final se usan EPP como mascarilla, lentes y guantes.",
        TAIL,
    ],
    vocab=[("revestir", "cubrir una superficie con un material de terminación"), ("revestimiento", "material que cubre una superficie como terminación"), ("adhesivo", "producto que une un revestimiento a una superficie, según las indicaciones del fabricante"), ("ergonomía", "adaptación del trabajo a las personas para evitar lesiones"), ("sobreesfuerzo", "esfuerzo excesivo del cuerpo al mover o levantar peso"), ("responsable", "persona que decide y firma los registros de la obra")],
    worked=[
        ("Clasificar un material", "En un caso de ejemplo se coloca cerámica sobre el piso de una cocina. ¿La cerámica es un revestimiento o un adhesivo?", ["La cerámica cubre el piso como terminación.", "Es un revestimiento; el adhesivo es el producto que la une."], "Un revestimiento"),
        ("Peso total", "Se descargan 10 cajas de 15 kg cada una (de ejemplo). ¿Cuántos kg son en total?", ["Se multiplican las cajas por el peso de cada una.", "10 por 15 son 150."], "150 kg"),
    ],
    mistakes=[("Pasar por un piso recién revestido porque «ya se ve firme».", "El revestimiento puede moverse o dañarse y alguien puede resbalar.", "Respeta la señal y el cierre hasta que el responsable lo autorice."),
              ("Cortar piezas sin mascarilla porque «es solo un momento».", "El polvo puede dañar los pulmones aun en poco tiempo.", "El EPP se usa siempre que lo indique el plan de prevención y la hoja de datos.")],
    T=[
        ("abc", "En Construcción (revestimientos): ¿qué es un revestimiento?", "Un material que cubre una superficie como terminación", "Una estructura que sostiene el edificio", "Una cañería de agua", "El revestimiento cubre piso, muro o cielo; no sostiene el edificio ni transporta agua."),
        ("abc", "¿Qué es un adhesivo?", "Un producto que une el revestimiento a la superficie, según las indicaciones del fabricante", "Una herramienta de corte", "El plano del recinto", "El adhesivo pega; el corte se hace con otras herramientas y el plano es un documento."),
        ("abc", "¿Para qué se señaliza y se cierra el paso a un piso recién revestido?", "Para evitar que alguien lo pise y se dañe o resbale", "Para que se vea más limpio", "Para ahorrar material", "La señal protege al trabajo y a las personas."),
        ("=", "{F} Si cada una de las 20 cajas pesa 20 kg, ¿cuántos kg se descargan en total?", "20*20", "Se multiplican las cajas por el peso de cada una.", " kg"),
        ("abc", "{F} ¿Qué medida de la ficha es administrativa?", "Señalizar y cerrar el paso al piso recién revestido", "Usar mascarilla", "Usar rodilleras", "Señalizar organiza el trabajo; mascarilla y rodilleras son EPP."),
        ("abc", "{F} ¿Qué riesgo se asocia a cortar piezas, según la ficha?", "Polvo y cortes con bordes de piezas", "Contacto con cables ocultos", "Caída desde altura", "La ficha anota polvo y cortes al cortar piezas; los otros riesgos no aparecen."),
        ("=", "{F} Cada integrante recibe mascarilla, lentes, guantes y rodilleras. ¿Cuántas piezas de EPP se entregan?", "5*4", "Se multiplican las 5 personas por las 4 piezas de cada una.", " piezas"),
        ("=", "{F} Si 2 parejas trasladan por igual las 20 cajas, ¿cuántas cajas lleva cada pareja?", "20//2", "Se dividen las cajas entre las 2 parejas.", " cajas"),
        ("abc", "{F} Una persona quiere pasar por el piso recién revestido «solo para ahorrar camino». ¿Qué corresponde?", "No pasar y respetar el cierre hasta que el responsable lo autorice", "Pasar por el borde", "Pasar si se saca los zapatos", "El cierre se levanta solo por decisión del responsable."),
        ("ab", "{F} Un compañero dice: «con la mascarilla no necesito la hoja de datos del adhesivo». ¿Qué es correcto?", "No: la hoja informa peligros y protección y se consulta siempre", "Sí: la mascarilla reemplaza la hoja", "La hoja de datos y la mascarilla cumplen funciones distintas."),
        ("abc", "{F} Una estudiante dice: «ya sé qué es un adhesivo, puedo revestir un piso». ¿Qué respuesta es correcta?", "No: esa tarea exige instructor autorizado y norma vigente", "Sí: con conocer el término basta", "Sí, si usa rodilleras", "Conocer un término no habilita; el EPP tampoco reemplaza la autorización."),
        ("=", "{F} Si cada caja pesara 25 kg en vez de 20, ¿cuántos kg serían las 20 cajas?", "20*25", "Se reemplaza el peso de cada caja y se multiplica por las cajas.", " kg"),
        ("abc", "{F} El prevencionista pide registrar que el piso recién revestido no está señalizado. ¿Qué datos lleva el registro?", "Qué falta, dónde, quién lo detectó y la fecha", "Solo la marca del adhesivo", "Solo el peso de las cajas", "Un registro útil deja constancia de qué, dónde, quién y cuándo."),
    ],
    ctx=("abc", "En una obra de ejemplo, una persona resbala en un piso húmedo y queda en el suelo sin poder levantarse. ¿Qué se hace según las reglas generales?", "No moverla sin autorización, avisar a un adulto responsable y a emergencias", "Levantarla rápido para que siga trabajando", "Dejarla sola hasta que se recupere", "Mover a una persona caída puede empeorar una lesión; se avisa a quien corresponde y a emergencias."),
    sc=[
        ("En Construcción (revestimientos): ¿qué significa revestir?", "Cubrir una superficie con un material de terminación", "Revestir da protección y presentación a pisos, muros o cielos."),
        ("En terminaciones de obra: ¿qué es la ergonomía?", "Adaptar el trabajo a las personas para evitar lesiones", "Incluye pausas, rodilleras y traslados en pareja."),
        ("¿Quién habilita a una persona para revestir superficies?", "Un instructor autorizado, con la norma vigente", "Leer este cuaderno no reemplaza esa autorización."),
    ],
    op=("Obra de ejemplo «Cocina Pino» (ficticia): se reviste un piso con una cuadrilla de 6 personas. Se descargan 18 cajas de 15 kg cada una (dato de ejemplo). Riesgos anotados: polvo, sobreesfuerzo, contacto con adhesivo y resbalones. Medidas disponibles: traslado de cajas en pareja, señalizar el piso, mascarilla, guantes y pausas. Escribe (a) los kg totales, (b) cuántas cajas lleva cada pareja si hay 3 parejas, (c) cuál medida es administrativa y cuáles son EPP y (d) qué haces si alguien resbala y no puede levantarse.",
        "(a) 18×15 son 270 kg. (b) 18 dividido en 3 son 6 cajas por pareja. (c) Señalizar el piso, el traslado en pareja y las pausas son administrativas; mascarilla y guantes son EPP. (d) No la muevo sin autorización, aviso a un adulto responsable y a emergencias.",
        ["calcula los kg", "reparte las cajas", "clasifica las medidas", "avisa sin mover a la persona"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar cajas por peso", "llamar EPP a las pausas", "proponer levantar a la persona"],
        "Pregunta: «¿por qué el traslado en pareja es una medida administrativa?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe tres riesgos de revestir un baño y, para cada uno, una medida administrativa o un EPP.",
    extend="Explica por qué las pausas y las rodilleras ayudan a prevenir lesiones en trabajos de piso.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 10 (cuadro de acabados de ejemplo, inventado). Proyecto «Vivienda Aliso» (ficticio). Baño: piso de cerámica de 30 cm por 30 cm; muros de cerámica hasta 2 m de altura; cielo pintado. "
     "Cocina: piso de porcelanato de 60 cm por 60 cm; muros pintados; cielo pintado. Dormitorio: piso flotante (tablas); muros con papel mural; cielo pintado. "
     "Junta entre piezas de cerámica del baño: 3 mm (valor de ejemplo). Zócalo (franja baja del muro) de 10 cm en la cocina y el dormitorio.")
build(
    O3, 2, F,
    use="Aprenderé a leer un cuadro de acabados y un plano de detalle, y el vocabulario de revestimientos: acabado, formato, junta, zócalo, horizontalidad y verticalidad.",
    prior=["Sé qué es un revestimiento y un adhesivo.", "Sé multiplicar medidas.", "Sé que las diferencias entre documentos se informan."],
    explain=[
        "El cuadro de acabados es una tabla del proyecto que indica, para cada recinto, el acabado del piso, de los muros y del cielo. El acabado es la terminación visible de una superficie. El formato es el tamaño de una pieza, por ejemplo 30 cm por 30 cm. La junta es el espacio pequeño entre piezas y el zócalo es la franja baja del muro que lo protege. La horizontalidad indica que una superficie está a nivel, sin inclinación, y la verticalidad que está derecha respecto de la vertical. Ambas se controlan con instrumentos y se anotan en un registro.",
        "El proyecto arquitectónico fija los acabados y los planos de detalle los dibujan con más precisión. Si el cuadro de acabados y la lista de compra no coinciden, no se elige uno por cuenta propia: se registra la diferencia y se informa al responsable. Esta clase solo enseña a leer y calcular con valores de ejemplo; los valores reales los fija el proyecto y la norma vigente.",
        TAIL,
    ],
    vocab=[("cuadro de acabados", "tabla que indica, por recinto, la terminación de piso, muros y cielo"), ("acabado", "terminación visible de una superficie"), ("formato", "tamaño de una pieza de revestimiento"), ("junta", "espacio pequeño entre piezas"), ("zócalo", "franja baja del muro que lo protege"), ("horizontalidad", "condición de una superficie que está a nivel, sin inclinación"), ("verticalidad", "condición de una superficie que está derecha respecto de la vertical")],
    worked=[
        ("Leer un acabado", "Un cuadro de ejemplo dice: «Oficina: piso alfombra, muros pintados, cielo placa». ¿Cuál es el acabado del piso?", ["Se busca la columna del piso.", "Dice alfombra."], "Alfombra"),
        ("Área de una pieza", "Una pieza de ejemplo mide 20 cm por 40 cm. ¿Cuántos cm² tiene?", ["Se multiplican las dos medidas.", "20 por 40 son 800."], "800 cm²"),
    ],
    mistakes=[("Confundir horizontalidad con verticalidad.", "Una se refiere a estar a nivel y la otra a estar derecho.", "Horizontal es a nivel (piso); vertical es derecho (muro)."),
              ("Cambiar el acabado de un recinto porque «el otro es más bonito».", "El acabado lo fija el proyecto.", "Si ves una diferencia, registra e informa al responsable.")],
    T=[
        ("abc", "En Construcción (revestimientos): ¿qué indica un cuadro de acabados?", "La terminación de piso, muros y cielo de cada recinto", "El costo de las herramientas", "La lista de personas de la cuadrilla", "El cuadro de acabados se ordena por recinto y terminación."),
        ("abc", "¿Qué es la junta entre piezas?", "El espacio pequeño que queda entre una pieza y otra", "La pieza de la esquina", "El borde del muro", "La junta es el espacio entre piezas, no una pieza."),
        ("abc", "¿Qué significa horizontalidad de un piso?", "Que está a nivel, sin inclinación", "Que está derecho como un muro", "Que tiene muchas piezas", "Horizontal es a nivel; derecho como un muro es verticalidad."),
        ("abc", "{F} ¿Cuál es el acabado del piso del baño?", "Cerámica de 30 cm por 30 cm", "Porcelanato de 60 cm por 60 cm", "Piso flotante", "El cuadro dice cerámica de 30 por 30 para el baño."),
        ("=", "{F} ¿Cuántos cm² tiene una pieza de cerámica del baño?", "30*30", "Se multiplican las dos medidas de la pieza.", " cm²"),
        ("abc", "{F} ¿Qué recinto lleva papel mural en los muros?", "El dormitorio", "El baño", "La cocina", "La ficha anota papel mural en los muros del dormitorio."),
        ("=", "{F} ¿Cuántos cm² tiene una pieza de porcelanato de la cocina?", "60*60", "Se multiplican las dos medidas de la pieza.", " cm²"),
        ("=", "{F} ¿Cuántas piezas de cerámica de 30 cm de ancho forman una hilera de 3 m (300 cm), sin contar juntas?", "300//30", "El largo de la hilera se divide por el ancho de la pieza.", " piezas"),
        ("abc", "{F} ¿En cuántos recintos el cielo es pintado?", "3", "1", "2", "La ficha anota cielo pintado en baño, cocina y dormitorio, por lo que son 3."),
        ("abc", "{F} La lista de compra anota cerámica para el piso de la cocina. ¿Qué corresponde?", "Registrar la diferencia con el cuadro e informar al responsable", "Comprar cerámica porque es más barata", "Cambiar el cuadro para que coincida", "Una diferencia entre documentos se informa; el acabado lo fija el proyecto."),
        ("ab", "{F} Un estudiante dice: «para controlar si un muro está derecho se usa la horizontalidad». ¿Qué es correcto?", "No: que un muro esté derecho se controla con la verticalidad", "Sí: la horizontalidad controla que un muro esté derecho", "La horizontalidad se refiere a estar a nivel, como un piso; el muro derecho es verticalidad."),
        ("=", "{F} Si el zócalo de la cocina mide 10 cm y el del dormitorio también, ¿cuántos cm suman entre los dos?", "10+10", "Se suman las alturas de los dos zócalos.", " cm"),
        ("abc", "{F} Un compañero propone cambiar el formato del baño a 60 por 60 «porque son más grandes». ¿Qué corresponde?", "No: el formato lo fija el proyecto; cualquier cambio lo decide quien diseña", "Cambiarlo si rinde más", "Cambiarlo si lo prefiere el cliente sin avisar al proyectista", "Los formatos están definidos en el proyecto; los cambios los autoriza quien lo diseñó."),
    ],
    ctx=("abc", "Un compañero de ejemplo sube a una repisa alta para mirar el cielo de un recinto y la repisa cede. ¿Qué haces?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias si hay heridos", "Subir a ayudarlo", "Tomar la repisa para sostenerla", "Una repisa que cede puede caer otra vez; se mantiene la distancia y se avisa."),
    sc=[
        ("En Construcción (revestimientos): ¿qué es el formato de una pieza?", "El tamaño de la pieza", "Por ejemplo, 30 cm por 30 cm."),
        ("¿Qué es el zócalo?", "La franja baja del muro que lo protege", "Se ubica en la parte baja del muro."),
        ("¿Qué se hace si el cuadro de acabados y la lista de compra no coinciden?", "Registrar la diferencia e informar al responsable", "No se elige un documento por cuenta propia."),
    ],
    op=("Cuadro de ejemplo (inventado) del proyecto «Casa Tilo»: Baño: piso de cerámica de 25 cm por 25 cm, muros de cerámica hasta 2 m, cielo pintado. Cocina: piso de cerámica de 40 cm por 40 cm. Lavandería: piso de cerámica de 25 cm por 25 cm. La lista de compra anota 40 cm por 40 cm para la lavandería. Escribe (a) los cm² de una pieza del baño, (b) cuántas piezas de 25 cm caben en una hilera de 3 m, (c) qué diferencia hay entre cuadro y lista y (d) qué haces.",
        "(a) 25×25 son 625 cm². (b) 300 dividido en 25 son 12 piezas. (c) El cuadro dice 25 por 25 para la lavandería y la lista anota 40 por 40. (d) Registro la diferencia e informo al responsable, sin elegir un documento por mi cuenta.",
        ["calcula el área de la pieza", "calcula las piezas de la hilera", "identifica la diferencia", "informa sin decidir"],
        ["hoja con las cuatro respuestas"],
        ["sumar las medidas en vez de multiplicar", "elegir un documento al azar", "cambiar el cuadro"],
        "Pregunta: «¿qué formato dice el cuadro para la lavandería?». Si no responde, pídele que relea el cuadro."),
    reinforce="Inventa un cuadro de acabados de dos recintos y escribe el acabado de piso, muros y cielo de cada uno.",
    extend="Explica por qué un piso que no está a nivel puede causar problemas aunque las piezas estén bien colocadas.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 11 (caso de ejemplo, inventado). Proyecto «Departamento Cedro» (ficticio). Baño: piso de 2 m por 3 m; muros con revestimiento hasta 2 m de altura sobre un perímetro de 10 m, con una puerta de 1 m por 2 m y una ventana de 1 m por 1 m. "
     "Cocina: piso de 3 m por 4 m. El cuadro de acabados indica porcelanato en el piso de la cocina y cerámica en el baño; la planilla de compra anota cerámica para ambos pisos.")
build(
    O3, 3, F,
    use="Aprenderé a analizar un caso en papel: calcular superficies de pisos y muros con vanos y detectar diferencias entre el cuadro de acabados y la planilla de compra.",
    prior=["Sé calcular superficies de rectángulos.", "Sé qué es un cuadro de acabados.", "Sé que las diferencias se informan."],
    explain=[
        "La superficie de un piso rectangular es largo por ancho. La superficie de un muro revestido es el perímetro multiplicado por la altura del revestimiento, y a ese resultado se le restan los vanos, que son las aberturas como puertas y ventanas, porque ahí no se reviste. Con estas superficies se prepara una planilla de compra. El revisor compara la planilla con el cuadro de acabados, y si hay diferencias las registra.",
        "El revisor no cambia productos por cuenta propia: un producto distinto del especificado es una sustitución y la autoriza el proyectista o el responsable. En el registro anota qué documento dice qué, qué difiere y quién lo detectó. Todos los datos son de ejemplo; esta clase no enseña a colocar revestimientos.",
        TAIL,
    ],
    vocab=[("perímetro", "suma de los lados de una figura; aquí, el contorno del recinto"), ("vano", "abertura de un muro, como una puerta o una ventana"), ("superficie neta", "superficie del muro descontando los vanos"), ("planilla de compra", "tabla con lo que se pide a un proveedor"), ("sustitución", "uso de un producto distinto del especificado")],
    worked=[
        ("Superficie de un piso", "Un piso de ejemplo mide 5 m por 4 m. ¿Cuántos m² tiene?", ["Se multiplican el largo y el ancho.", "5 por 4 son 20."], "20 m²"),
        ("Muro con un vano", "Un muro revestido de ejemplo tiene perímetro de 12 m, altura de 2 m y un vano de 2 m². ¿Cuál es la superficie neta?", ["Superficie bruta: 12 por 2 son 24 m².", "Se resta el vano: 24 menos 2 son 22."], "22 m²"),
    ],
    mistakes=[("Revestir la superficie del vano porque «es parte del muro».", "En el vano no hay muro ni revestimiento.", "Se descuentan los vanos de la superficie bruta."),
              ("Cambiar la planilla para que coincida con el cuadro sin informar.", "Se oculta un posible error de pedido.", "Registra la diferencia e informa al responsable.")],
    T=[
        ("abc", "En Construcción (revestimientos): ¿cómo se calcula la superficie de un piso rectangular?", "Largo por ancho", "Largo más ancho", "Perímetro por altura", "El área de un rectángulo es largo por ancho."),
        ("abc", "¿Qué se hace con los vanos al calcular la superficie de un muro revestido?", "Se restan de la superficie bruta", "Se suman a la superficie bruta", "Se ignoran", "En los vanos no se reviste, por lo que se descuentan."),
        ("abc", "¿Qué es una sustitución de producto?", "Usar un producto distinto del especificado", "Devolver el producto sobrante", "Pedir más producto del necesario", "Sustituir es reemplazar el producto especificado por otro; debe autorizarse."),
        ("=", "{F} ¿Cuántos m² tiene el piso del baño?", "2*3", "Se multiplican el largo y el ancho del piso.", " m²"),
        ("=", "{F} ¿Cuántos m² tiene el piso de la cocina?", "3*4", "Se multiplican el largo y el ancho del piso.", " m²"),
        ("=", "{F} ¿Cuántos m² brutos tienen los muros del baño (perímetro por altura)?", "10*2", "Se multiplican el perímetro por la altura del revestimiento.", " m²"),
        ("=", "{F} ¿Cuántos m² suman los vanos del baño (puerta y ventana)?", "1*2+1*1", "Se suman las superficies de la puerta y de la ventana.", " m²"),
        ("=", "{F} ¿Cuántos m² netos de muro hay en el baño?", "10*2-(1*2+1*1)", "A la superficie bruta se le restan los vanos.", " m²"),
        ("=", "{F} ¿Cuántos m² de piso suman baño y cocina?", "2*3+3*4", "Se suman las superficies de los dos pisos.", " m²"),
        ("abc", "{F} La planilla anota cerámica para el piso de la cocina y el cuadro indica porcelanato. ¿Qué corresponde?", "Registrar la diferencia e informar al responsable", "Comprar cerámica porque es la planilla más reciente", "Cambiar el cuadro de acabados", "Una diferencia entre documentos se informa; no se resuelve por cuenta propia."),
        ("ab", "{F} Un estudiante dice: «no descontemos la ventana, así pedimos más y sobra». ¿Qué es correcto?", "No: los vanos se descuentan y la pérdida se calcula aparte", "Sí: pedir de más siempre es mejor", "Descontar los vanos da la cantidad real; la pérdida se suma después."),
        ("=", "{F} Si el baño tuviera una segunda ventana de 1 m por 1 m, ¿cuántos m² netos de muro habría?", "10*2-(1*2+1*1+1*1)", "Se agrega la segunda ventana a los vanos que se descuentan.", " m²"),
        ("abc", "{F} El supervisor pide un registro de la diferencia en el piso de la cocina. ¿Qué incluye?", "Cuadro: porcelanato; planilla: cerámica; quién lo detectó y la fecha", "Solo la palabra «error»", "El precio de la cerámica", "El registro deja el dato de cada documento, quién lo detectó y la fecha."),
    ],
    ctx=("abc", "Midiendo los muros del baño en una obra de ejemplo, un compañero se sube a un banco sin apoyo para medir arriba y cae sobre las cerámicas rotas. ¿Qué haces?", "No mover a la persona, avisar a un adulto responsable y a emergencias", "Levantarlo rápido y llevarlo afuera", "Seguir midiendo y avisar al final", "Mover a una persona caída puede empeorar una lesión; se avisa a quien corresponde y a emergencias."),
    sc=[
        ("¿Cómo se calcula la superficie bruta de un muro revestido?", "Perímetro por altura del revestimiento", "El perímetro es el contorno del recinto."),
        ("En Construcción (revestimientos): ¿qué se descuenta del muro para obtener la superficie neta?", "Los vanos", "En una puerta o ventana no se reviste."),
        ("En revestimientos: ¿quién autoriza una sustitución de producto?", "El proyectista o el responsable", "No la decide quien ejecuta ni quien compra."),
    ],
    op=("Caso de ejemplo (inventado): baño con piso de 2 m por 2 m; muros de perímetro 8 m revestidos hasta 2 m, con una puerta de 2 m² y una ventana de 1 m². El cuadro de acabados indica porcelanato en el piso y la planilla anota cerámica. Escribe (a) los m² del piso, (b) los m² brutos de muro, (c) los m² netos de muro y (d) qué haces con la diferencia de producto.",
        "(a) 2×2 son 4 m². (b) 8×2 son 16 m². (c) 16 menos (2+1) son 13 m². (d) Registro la diferencia (porcelanato en el cuadro y cerámica en la planilla) e informo al responsable.",
        ["calcula el piso", "calcula el muro bruto", "descuenta los vanos", "informa la diferencia"],
        ["hoja con las cuatro respuestas"],
        ["no descontar vanos", "sumar perímetro y altura", "cambiar el cuadro"],
        "Pregunta: «¿qué operación usas para el muro bruto?». Si no responde, pídele que relea cómo se calcula un muro revestido."),
    reinforce="Inventa un recinto con una puerta y calcula la superficie neta de su muro revestido.",
    extend="Explica por qué comprar de más por no descontar vanos puede ser costoso para una obra.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 12 (cubicación y control de ejemplo, inventados). Obra «Terraza Ñire» (ficticia): piso de 20 m² con piezas de 50 cm por 50 cm, que son 4 piezas por m². Pérdida de ejemplo del 10 %. Las piezas se venden en cajas de 4 piezas; precio de ejemplo $12.000 por caja. "
     "Control de horizontalidad de ejemplo: desnivel máximo permitido de 3 mm. Mediciones de ejemplo: punto A, 2 mm; punto B, 3 mm; punto C, 5 mm.")
build(
    O3, 4, F,
    use="Aprenderé a calcular piezas, pérdidas, cajas y costo de un revestimiento en una planilla y a registrar un control de horizontalidad con un máximo de ejemplo.",
    prior=["Sé calcular superficies y porcentajes simples.", "Sé qué es la horizontalidad.", "Sé comparar un valor medido con un máximo."],
    explain=[
        "Para cubicar piezas de un revestimiento se multiplica la superficie por las piezas que caben en cada m², dato que sale del formato de la pieza. A ese total se le suma la pérdida, un porcentaje por cortes y piezas dañadas. Como las piezas se venden en cajas completas, la cantidad de cajas se obtiene dividiendo las piezas por las que trae cada caja; si la división no es exacta se pide una caja más. El costo se calcula multiplicando las cajas por el precio de cada una.",
        "El control de horizontalidad compara el desnivel medido en puntos de la superficie con el desnivel máximo permitido. Un desnivel igual o menor que el máximo cumple; uno mayor no cumple y se informa al responsable. El registro anota cada medida real: no se cambia un valor para que cumpla. Todos los valores son de ejemplo; este cuaderno no enseña a colocar revestimientos ni a nivelar superficies.",
        TAIL,
    ],
    vocab=[("caja", "unidad en que se venden las piezas, con una cantidad fija"), ("pérdida", "porcentaje de ejemplo por cortes y piezas dañadas"), ("desnivel", "diferencia de altura entre dos puntos de una superficie"), ("máximo permitido", "valor más alto que se acepta"), ("registro de control", "documento donde se anotan las medidas y la conclusión")],
    worked=[
        ("Piezas por superficie", "Un piso de ejemplo de 10 m² usa 5 piezas por m². ¿Cuántas piezas se necesitan sin pérdida?", ["Se multiplican los m² por las piezas por m².", "10 por 5 son 50."], "50 piezas"),
        ("Comparar un desnivel", "Un desnivel de ejemplo medido es de 4 mm y el máximo permitido es de 2 mm. ¿Cumple?", ["4 es mayor que 2.", "No cumple."], "No cumple"),
    ],
    mistakes=[("Calcular las cajas sin sumar la pérdida.", "Se quedaría sin piezas al cortar o dañar algunas.", "Suma la pérdida antes de calcular las cajas."),
              ("Anotar un desnivel menor que el real para que el punto «cumpla».", "Un registro falso oculta un problema de calidad.", "Anota el valor medido y, si no cumple, informa al responsable.")],
    T=[
        ("abc", "En Construcción (revestimientos): ¿qué es el desnivel entre dos puntos de un piso?", "La diferencia de altura entre ellos", "La distancia entre ellos", "El número de piezas que los cubren", "Desnivel es diferencia de altura, no distancia ni cantidad de piezas."),
        ("abc", "En revestimientos: ¿por qué las cajas se redondean hacia arriba?", "Porque las piezas se venden en cajas completas", "Porque la pérdida es negativa", "Porque las cajas se devuelven", "Una caja incompleta no se puede comprar."),
        ("abc", "Un desnivel mayor que el máximo permitido. ¿Qué corresponde?", "Registrar la medida real e informar al responsable", "Anotar el máximo permitido para que cumpla", "No anotar nada", "Un valor fuera del límite se registra tal cual y se informa."),
        ("=", "{F} ¿Cuántas piezas se necesitan para los 20 m² sin pérdida?", "20*4", "Se multiplican los m² por las piezas de cada m².", " piezas"),
        ("=", "{F} ¿Cuántas piezas equivalen a la pérdida del 10 %?", "20*4*10//100", "Se calcula el 10 % de las piezas sin pérdida.", " piezas"),
        ("=", "{F} ¿Cuántas piezas se piden en total, con la pérdida?", "20*4+20*4*10//100", "A las piezas sin pérdida se les suma el 10 %.", " piezas"),
        ("=", "{F} ¿Cuántas cajas de 4 piezas se necesitan?", "(20*4+20*4*10//100)//4", "Las piezas pedidas se dividen por las 4 de cada caja.", " cajas"),
        ("=", "{F} ¿Cuánto cuestan las cajas al precio de ejemplo?", "(20*4+20*4*10//100)//4*12000", "Se multiplican las cajas por el precio de cada una.", " pesos"),
        ("abc", "{F} ¿Cumple el punto A con el máximo de 3 mm?", "Sí: 2 mm no supera los 3 mm", "No: 2 mm superan los 3 mm", "No se puede saber", "2 mm es menor que 3 mm, por lo que cumple."),
        ("abc", "{F} ¿Cumple el punto B, con 3 mm, el máximo permitido de 3 mm?", "Sí: es igual al máximo permitido", "No: debería ser menor que 3", "No: debería ser mayor que 3", "El máximo permitido es de 3 mm y 3 mm no lo supera."),
        ("abc", "{F} ¿Qué corresponde con el punto C, que mide 5 mm?", "Registrar que no cumple e informar al responsable", "Anotar 3 mm para que cumpla", "No registrar el punto", "Un valor fuera del límite se registra y se informa."),
        ("=", "{F} Si el piso tuviera 25 m² en vez de 20, ¿cuántas piezas sin pérdida se necesitarían?", "25*4", "Se reemplazan los m² y se multiplica por las 4 piezas de cada m².", " piezas"),
        ("ab", "{F} Un compañero dice: «el piso se ve plano, no hace falta medir los desniveles». ¿Qué es correcto?", "No: el control exige medir y registrar aunque el piso parezca plano", "Sí: si se ve plano basta", "A simple vista no se compara un desnivel con un máximo permitido."),
    ],
    ctx=("abc", "Para medir los desniveles de una terraza de ejemplo, un compañero propone caminar sobre el borde sin barandas. ¿Qué corresponde?", "No hacerlo: el borde sin protección es una zona de riesgo de caída; se avisa al prevencionista", "Caminar con cuidado", "Caminar si alguien lo mira", "Un borde sin protección es riesgo de caída; que alguien mire no lo evita."),
    sc=[
        ("¿Cómo se calculan las piezas de un revestimiento sin pérdida?", "Multiplicando los m² por las piezas de cada m²", "Cada m² necesita una cantidad fija de piezas."),
        ("En Construcción (revestimientos): ¿qué es un máximo permitido?", "El valor más alto que se acepta", "Un valor mayor no cumple y se informa."),
        ("¿Qué se hace si un desnivel supera el máximo?", "Se registra el valor real y se informa al responsable", "Nunca se cambia un valor para que cumpla."),
    ],
    op=("Caso de ejemplo (inventado): piso de 30 m² con piezas de 4 por m², pérdida de 10 %, cajas de 6 piezas y $15.000 por caja. Máximo de desnivel de ejemplo: 4 mm. Mediciones: punto X, 3 mm; punto Y, 6 mm. Escribe (a) las piezas sin pérdida, (b) las piezas con pérdida, (c) las cajas y el costo y (d) qué puntos cumplen y qué haces con el que no.",
        "(a) 30×4 son 120 piezas. (b) El 10 % de 120 es 12; en total 132 piezas. (c) 132 dividido en 6 son 22 cajas; 22×15.000 son 330.000 pesos. (d) X cumple (3 es menor que 4); Y no cumple (6 supera 4): registro el valor real e informo al responsable.",
        ["calcula las piezas", "suma la pérdida", "calcula cajas y costo", "concluye con el máximo e informa"],
        ["hoja con cálculos y conclusión"],
        ["olvidar la pérdida", "no dividir por las piezas de la caja", "registrar un valor falso"],
        "Pregunta: «¿por qué se suma la pérdida antes de las cajas?». Si no responde, pídele que relea qué cubre la pérdida."),
    reinforce="Calcula las piezas de un piso de 10 m² con 4 piezas por m² y pérdida de 10 % (datos de ejemplo).",
    extend="Explica por qué una pérdida mal calculada puede dejar un piso sin terminar por falta de piezas.",
)

# ============================================================ OAM-03, clase 5
F = ("Ficha 13 (comparación de ejemplo, inventada). Obra «Pasaje Maitén» (ficticia): piso de 40 m². Opción 1, porcelanato: precio de ejemplo $14.000 por m², pérdida de ejemplo del 5 %. "
     "Opción 2, cerámica: precio de ejemplo $9.000 por m², pérdida de ejemplo del 10 %. Registro de verificación de horizontalidad (de ejemplo): puntos 1, 2, 3 y 4 con desniveles de 1, 2, 4 y 2 mm; máximo permitido de ejemplo: 3 mm.")
build(
    O3, 5, F,
    use="Aprenderé a comparar dos alternativas de revestimiento por costo y a verificar la calidad con un registro de horizontalidad, sin olvidar que la decisión es del responsable.",
    prior=["Sé calcular una pérdida y el costo de un pedido.", "Sé comparar un desnivel con un máximo.", "Sé que las diferencias se informan."],
    explain=[
        "Comparar alternativas significa calcular el costo total de cada una con los mismos datos de superficie y pérdida. Primero se suma la pérdida a la superficie, y luego se multiplica por el precio por m². Un costo menor no significa que la opción sea la mejor: también importan el uso del recinto, la resistencia al desgaste y la humedad, el plazo y las indicaciones del fabricante. La decisión final la toma el responsable con el proyecto y la norma vigente.",
        "Para verificar la calidad se usa un registro que anota cada medida real. Se compara cada desnivel con el máximo permitido; los que lo superan se informan, y la superficie no se entrega ni se aprueba hasta que el responsable lo autorice. El registro no se altera. Todos los valores son de ejemplo; este cuaderno no enseña a colocar ni a corregir revestimientos.",
        TAIL,
    ],
    vocab=[("alternativa", "una de las opciones que se comparan"), ("costo total", "superficie con pérdida multiplicada por el precio"), ("desgaste", "daño de una superficie por el uso"), ("verificación", "comprobación de que algo cumple lo pedido"), ("aprobación", "decisión del responsable de aceptar un trabajo")],
    worked=[
        ("Costo de una opción", "Una opción de ejemplo cubre 10 m² a $6.000 por m², sin pérdida. ¿Cuál es el costo?", ["Se multiplican los m² por el precio.", "10 por 6.000 son 60.000."], "$60.000"),
        ("Contar puntos que cumplen", "Un registro de ejemplo tiene 5 puntos y 1 supera el máximo. ¿Cuántos cumplen?", ["Se resta el punto que no cumple.", "5 menos 1 son 4."], "4 puntos"),
    ],
    mistakes=[("Elegir la opción más barata sin considerar el uso del recinto.", "Una opción barata puede desgastarse rápido en un recinto exigente.", "Compara costo, uso, desgaste, plazo y la decisión del responsable."),
              ("Aprobar un piso porque la mayoría de los puntos cumple.", "Basta un punto fuera del máximo para que haya que informar.", "Revisa todos los puntos y entrega el registro al responsable.")],
    T=[
        ("abc", "En Construcción (revestimientos): ¿qué significa comparar dos alternativas?", "Calcular el costo y analizar el uso de cada una con los mismos datos", "Elegir la más bonita sin calcular", "Comprar las dos para probarlas", "Se comparan con los mismos datos de superficie y pérdida."),
        ("abc", "¿Por qué el costo menor no basta para elegir una alternativa?", "Porque también importan el uso del recinto, el desgaste y las indicaciones del fabricante", "Porque el costo menor siempre es peor", "Porque el costo no se puede calcular", "El costo es un criterio más; el uso y la durabilidad también cuentan."),
        ("abc", "¿Quién aprueba el trabajo de revestimiento?", "El responsable, con el proyecto y la norma vigente", "Cualquier integrante de la cuadrilla", "El proveedor de las piezas", "La aprobación la hace quien tiene la responsabilidad técnica."),
        ("=", "{F} ¿Cuántos m² se piden de porcelanato con la pérdida del 5 %?", "40+40*5//100", "A la superficie se le suma el 5 % de pérdida.", " m²"),
        ("=", "{F} ¿Cuántos m² se piden de cerámica con la pérdida del 10 %?", "40+40*10//100", "A la superficie se le suma el 10 % de pérdida.", " m²"),
        ("=", "{F} ¿Cuánto cuesta el porcelanato con la pérdida?", "(40+40*5//100)*14000", "Se multiplican los m² pedidos por el precio por m².", " pesos"),
        ("=", "{F} ¿Cuánto cuesta la cerámica con la pérdida?", "(40+40*10//100)*9000", "Se multiplican los m² pedidos por el precio por m².", " pesos"),
        ("=", "{F} ¿Cuál es la diferencia de costo entre las dos opciones?", "(40+40*5//100)*14000-(40+40*10//100)*9000", "Se resta el costo de la cerámica del costo del porcelanato.", " pesos"),
        ("abc", "{F} Por costo de ejemplo, ¿cuál opción es más económica?", "La cerámica", "El porcelanato", "Cuestan lo mismo", "La cerámica cuesta 396.000 y el porcelanato 588.000 en este ejemplo."),
        ("abc", "{F} ¿Cuántos puntos del registro superan el máximo permitido?", "Uno: el punto 3", "Dos: los puntos 2 y 4", "Ninguno", "Solo el punto 3, con 4 mm, supera los 3 mm."),
        ("abc", "{F} ¿Qué corresponde hacer con el registro?", "Entregarlo al responsable con el punto 3 informado como no cumple", "Corregir el valor del punto 3 a 3 mm", "Guardarlo sin informar", "Un valor fuera del máximo se informa; no se altera el registro."),
        ("ab", "{F} Un estudiante dice: «como la cerámica es más barata, el responsable ya no tiene que decidir». ¿Qué es correcto?", "No: la decisión es del responsable, que considera costo, uso, desgaste y la norma vigente", "Sí: el costo menor decide", "El costo es un criterio y no reemplaza la decisión del responsable."),
        ("=", "{F} Si el piso fuera de 60 m² y se mantienen los precios y pérdidas, ¿cuánto costaría el porcelanato con pérdida?", "(60+60*5//100)*14000", "Se reemplaza la superficie, se suma la pérdida y se multiplica por el precio.", " pesos"),
    ],
    ctx=("abc", "Una persona de ejemplo quiere probar la resistencia de un revestimiento subiéndose a una escalera apoyada de forma inestable. ¿Qué corresponde?", "No hacerlo: el trabajo en altura exige personal autorizado y protecciones; se avisa al prevencionista", "Subir con cuidado", "Subir si alguien sostiene la escalera", "Una escalera mal apoyada puede provocar una caída; no se improvisa."),
    sc=[
        ("¿Cómo se calcula el costo total de una alternativa?", "Superficie con pérdida multiplicada por el precio por m²", "La pérdida se suma antes de multiplicar por el precio."),
        ("En Construcción (revestimientos): ¿qué se hace con un punto del registro fuera del máximo?", "Se informa al responsable con el valor real", "No se altera un registro para que cumpla."),
        ("¿Quién decide la alternativa final?", "El responsable, con el proyecto y la norma vigente", "El costo es solo uno de los criterios."),
    ],
    op=("Caso de ejemplo (inventado): piso de 20 m². Opción A, $12.000 por m², pérdida de 5 %. Opción B, $8.000 por m², pérdida de 10 %. Registro de horizontalidad de ejemplo: puntos con 2, 5, 3 y 1 mm; máximo permitido de 4 mm. Escribe (a) los m² pedidos de A y de B, (b) el costo de A y de B, (c) cuántos puntos superan el máximo y qué haces y (d) quién decide la opción.",
        "(a) A: 20+1 son 21 m². B: 20+2 son 22 m². (b) A: 21×12.000 son 252.000 pesos. B: 22×8.000 son 176.000 pesos. (c) Un punto supera el máximo: el de 5 mm; registro el valor real e informo al responsable. (d) El responsable, con el proyecto y la norma vigente.",
        ["suma la pérdida", "calcula los costos", "detecta el punto fuera del máximo", "indica quién decide"],
        ["hoja con cálculos y conclusión"],
        ["olvidar la pérdida", "alterar un valor del registro", "decidir solo por precio"],
        "Pregunta: «¿qué punto supera el máximo?». Si no responde, pídele que compare cada valor con 4 mm."),
    reinforce="Compara el costo de dos pisos de 20 m², uno a $7.000 por m² con 10 % de pérdida y otro a $9.000 por m² con 5 % (datos de ejemplo).",
    extend="Explica por qué la opción más barata puede no ser la mejor en un recinto con mucho uso.",
)
