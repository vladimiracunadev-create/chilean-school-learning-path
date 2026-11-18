"""Operaciones Portuarias TP 3.º y 4.º medio: OAE-04 (organizar y almacenar cargas, incluidas refrigeradas y peligrosas, como lectura de documentos y cálculo de planilla). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_opor_common import AVISO, EMER, build

O4 = "TP-OPOR-3y4-OAE-04"

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Bodega Demo» tiene cuatro zonas: A, de carga general (600 m²); B, una cámara de frío para carga refrigerada (200 m²); C, una zona separada y señalizada para mercancías peligrosas (100 m²); "
     "y D, un patio de acopio al aire libre (800 m²). En cada zona, una cuarta parte del área se reserva para pasillos y circulación. Dotación por turno: zona A, 4 personas; zona B, 2; zona C, 2 (personal capacitado); zona D, 3. Hay 3 turnos al día. "
     "Peligros anotados: estanterías altas con bultos pesados en la zona A, exposición al frío en la zona B, envases con etiqueta de peligro en la zona C y vehículos de carga que circulan por el patio D.")
build(
    O4, 1, F,
    use="Aprenderé qué es almacenar y organizar la carga, qué tipos de carga existen (general, refrigerada y peligrosa), qué peligros tiene una bodega y por qué se exige personal capacitado y norma vigente.",
    prior=["Sé distinguir peligro y riesgo y ordenar la jerarquía de controles.", "Sé multiplicar y dividir números enteros.", "Sé qué es una zona de un recinto."],
    explain=[
        "Almacenar es mantener la carga ordenada en un espacio mientras espera su traslado o despacho. Se hace en bodegas (espacios cerrados), almacenes y patios de acopio, que son espacios abiertos donde se reúne y mantiene la carga. La carga puede ser general (de formas y tamaños variados), refrigerada, que debe mantenerse a una temperatura controlada para no echarse a perder, o peligrosa, que por su naturaleza puede causar daño a personas, bienes o al ambiente.",
        "Cada tipo de carga tiene peligros propios: las estanterías altas con bultos pesados pueden provocar caídas de carga; el frío expone a un daño si la permanencia es larga; las mercancías peligrosas pueden provocar incendio, intoxicación o derrame; y los vehículos de carga pueden atropellar. Se previene con la jerarquía de controles. La segregación de las mercancías peligrosas es mantenerlas separadas de otras cargas con las que no son compatibles, según su hoja de datos de seguridad y la norma vigente.",
        f"La manipulación de mercancías peligrosas y de cargas refrigeradas es una tarea de personal capacitado y autorizado; este cuaderno solo enseña conceptos y cálculos en papel. {EMER} {AVISO}",
    ],
    vocab=[("almacenar", "mantener la carga ordenada en un espacio mientras espera su traslado o despacho"), ("patio de acopio", "espacio abierto donde se reúne y mantiene la carga"), ("carga refrigerada", "carga que debe mantenerse a una temperatura controlada"), ("mercancía peligrosa", "carga que por su naturaleza puede causar daño a personas, bienes o al ambiente"), ("segregación", "mantener separadas cargas que no son compatibles"), ("pallet", "plataforma sobre la que se arma una carga"), ("derrame", "escape de un líquido o de un producto fuera de su envase")],
    worked=[
        ("Peligro y riesgo", "En una bodega de ejemplo, un pasillo estrecho es compartido por personas y por un vehículo de carga. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el vehículo de carga que circula por el pasillo estrecho.", "El riesgo es que atropelle o aplaste a una persona."], "Peligro: el vehículo en un pasillo estrecho; riesgo: que atropelle a una persona"),
        ("Clasificar la carga", "Una carga de ejemplo son pescados congelados que deben llegar a una temperatura controlada. ¿Qué tipo de carga es?", ["La temperatura controlada es la característica clave.", "Una carga que exige temperatura controlada es refrigerada."], "Carga refrigerada"),
    ],
    mistakes=[("Creer que cualquier carga puede almacenarse en cualquier zona porque «todo es carga».", "Cada tipo de carga exige condiciones y separaciones propias.", "Ubica cada carga en la zona que corresponde a su tipo."),
              ("Creer que leer sobre mercancías peligrosas habilita para manipularlas.", "Su manipulación exige formación, autorización y norma vigente.", "Aprende aquí el concepto y deja la manipulación a personal capacitado.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es un patio de acopio?", "Un espacio abierto donde se reúne y mantiene la carga mientras espera su traslado", "Una cámara cerrada con temperatura controlada", "Un documento que registra la salida de la carga", "El patio de acopio es un espacio abierto de reunión de carga; la cámara y el documento son otras cosas."),
        ("abc", "En Operaciones Portuarias: ¿qué es una carga refrigerada?", "Carga que debe mantenerse a una temperatura controlada para no echarse a perder", "Carga que debe mantenerse siempre seca", "Carga que viaja a granel y en capas", "Lo propio de la carga refrigerada es la temperatura controlada."),
        ("abc", "En Operaciones Portuarias: ¿qué es la segregación de mercancías peligrosas?", "Mantenerlas separadas de otras cargas con las que no son compatibles, según su hoja de datos de seguridad y la norma vigente", "Mezclarlas por tipo en una sola zona para ahorrar espacio", "Registrarlas en el manifiesto con un código", "Segregar es separar lo incompatible; mezclar o registrar no cumple esa función."),
        ("abc", "{F} ¿Qué zona de la ficha requiere señalización de peligro y personal capacitado?", "La zona C, de mercancías peligrosas", "La zona A, de carga general", "La zona D, el patio de acopio", "Las mercancías peligrosas se almacenan en una zona separada y señalizada."),
        ("abc", "{F} ¿Qué peligro se asocia a la permanencia prolongada en la zona B?", "La exposición al frío", "El calor excesivo", "El polvo en suspensión", "La cámara de frío expone a bajas temperaturas."),
        ("abc", "{F} ¿Qué riesgo representa una estantería de la zona A con bultos pesados en altura?", "Que bultos o la estantería caigan sobre una persona", "Que los bultos se enfríen demasiado", "Que los bultos reaccionen con los de la zona C", "Una carga en altura puede caer; el frío y la reacción corresponden a otras zonas."),
        ("=", "{F} ¿Cuántos metros cuadrados suman las cuatro zonas?", "600+200+100+800", "Se suman las áreas de las zonas A, B, C y D.", " m²"),
        ("=", "{F} ¿Cuántos metros cuadrados quedan para almacenar en la zona A, después de reservar los pasillos?", "600-600//4", "Se resta a la zona A su cuarta parte, destinada a pasillos.", " m²"),
        ("=", "Un pallet de ejemplo ocupa 2 m² de piso y se apilan 3 pallets en altura. ¿Cuántos pallets caben en 300 m² de piso?", "300//2*3", "Se calculan los pallets por piso y se multiplican por los de altura.", " pallets"),
        ("abc", "Durante una visita de ejemplo, un envase se rompe y un líquido desconocido se derrama cerca de la zona C. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte con papel o ropa para absorber el líquido", "Oler el líquido para saber qué es", "Un derrame desconocido puede ser peligroso; se mantiene la distancia y se avisa."),
        ("abc", "En Operaciones Portuarias: ¿por qué las mercancías peligrosas no se almacenan junto a cualquier otra carga?", "Porque algunas pueden reaccionar con otros materiales; por eso se segregan según la norma vigente", "Porque siempre ocupan más espacio que el resto", "Porque su valor es mayor que el de otras cargas", "La segregación evita reacciones peligrosas; no depende del espacio ni del valor."),
        ("=", "{F} ¿Cuántas personas en total trabajan en un día, sumando las dotaciones de las cuatro zonas en cada uno de los tres turnos?", "(4+2+2+3)*3", "Se suma la dotación de las zonas y se multiplica por los turnos del día.", " personas"),
        ("abc", "{F} Para reducir el riesgo de caída de bultos de las estanterías de la zona A, ¿cuál medida es de nivel más efectivo?", "Cambiar el diseño para no almacenar bultos pesados en altura", "Pegar un cartel que diga «cuidado con la altura»", "Entregar un casco a todo el personal", "Eliminar el peligro actúa en el origen; el cartel es administrativo y el casco es EPP."),
    ],
    ctx=("abc", "Un amigo que trabaja en una bodega te ofrece llevarte «a ver» la zona de productos químicos y dejarte mover un par de tambores. ¿Qué respondes?", "Que no, porque manipular mercancías peligrosas exige instructor autorizado, norma vigente y protección, y que lo consultarás con un adulto responsable", "Que sí, si usas guantes", "Que sí, pero solo los tambores que parezcan livianos", "Los guantes o el peso aparente no reemplazan la formación ni la autorización."),
    sc=[
        ("En Operaciones Portuarias: ¿qué es una carga refrigerada?", "Carga que debe mantenerse a una temperatura controlada", "La temperatura controlada es lo que la distingue de otras cargas."),
        ("¿Qué es segregar mercancías peligrosas?", "Mantenerlas separadas de cargas incompatibles", "La segregación evita reacciones peligrosas entre cargas distintas."),
        ("¿Qué hacer ante un derrame desconocido?", "No acercarse, avisar a un adulto responsable y a emergencias", "Solo personal capacitado puede actuar ante un derrame."),
    ],
    op=("Una tarea de ejemplo anota: almacenar carga general en un patio de acopio al aire libre, apilada en altura junto a una ruta por donde circulan vehículos de carga. Peligros anotados: caída de la pila y atropello. Escribe (a) un peligro de la tarea y su riesgo asociado, (b) un control administrativo, (c) un control de ingeniería, (d) qué hacer si se ve que una pila se inclina con una persona cerca.",
        "(a) Peligro: la pila alta junto a la ruta; riesgo: que la pila caiga sobre una persona o un vehículo. (b) Un permiso de ingreso al patio y un límite de altura de apilado informado por letreros y charlas. (c) Una barrera fija que separe la ruta de los vehículos de la zona de pilas. (d) No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias. La tarea la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "indica no intervenir y avisar"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer el EPP como único control", "sugerir sostener la pila para evitar que caiga"],
        "Pregunta: «¿qué hace una persona sin formación ante una pila que se inclina?». Si no responde, pídele que relea el final de la explicación."),
    reinforce="Escribe una zona de bodega de cada tipo de carga (general, refrigerada y peligrosa) y un peligro de cada una.",
    extend="Explica con un ejemplo por qué no basta con un letrero para controlar el peligro de una estantería alta.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (registro de ingreso de ejemplo, inventado). «Bodega Demo», registro de ingreso N.º 0417. Producto 1: 60 cajas de fruta de ejemplo, de 12 kg cada una; rango de temperatura requerido de ejemplo: 2 a 6 grados; llegaron en un contenedor refrigerado y el registro de temperatura al ingreso marca 4 grados. "
     "Producto 2: 20 tambores de un producto químico de ejemplo, de 40 kg cada uno; llevan una etiqueta de peligro con el símbolo de una llama; se adjunta la hoja de datos de seguridad. "
     "Producto 3: 90 cajas de repuestos (carga general), de 25 kg cada una, con la marca «mantener seco».")
build(
    O4, 2, F,
    use="Aprenderé a reconocer tipos de carga y medios de transporte, a leer etiquetas de peligro, hojas de datos de seguridad y registros de temperatura, y qué roles intervienen en el almacenamiento.",
    prior=["Sé qué es la carga refrigerada y la peligrosa.", "Sé leer una planilla con pesos y cantidades.", "Sé qué es una marca de manipulación."],
    explain=[
        "La carga llega en distintos medios de transporte: camión, tren o nave, y a veces en contenedores. Cada carga trae su información. La etiqueta de peligro es un rombo con un símbolo y un color que indica el tipo de peligro de una mercancía; por ejemplo, una llama indica que es inflamable y una calavera, que es tóxica. La hoja de datos de seguridad es el documento que describe los peligros de un producto y las medidas de prevención; debe acompañar a la mercancía peligrosa.",
        "La carga refrigerada exige cadena de frío: mantener la temperatura dentro de su rango permitido, desde el origen hasta el destino, y dejar un registro de temperatura que lo demuestre. Si una lectura queda fuera del rango, se registra la desviación y se informa. En la bodega trabajan el jefe de bodega, que organiza el espacio y los registros; el bodeguero, que lleva el inventario; el tarjador, que cuenta los bultos; y el prevencionista, que vela por la seguridad.",
        f"Un ingreso se da por conforme solo si los documentos y registros están completos y coinciden con la carga; si falta algo, se registra y se informa. {EMER} {AVISO}",
    ],
    vocab=[("etiqueta de peligro", "rombo con un símbolo y un color que indica el tipo de peligro de una mercancía"), ("hoja de datos de seguridad", "documento que describe los peligros de un producto y las medidas de prevención"), ("cadena de frío", "continuidad de la temperatura controlada desde el origen hasta el destino"), ("registro de temperatura", "anotación de las lecturas de temperatura de una carga"), ("desviación", "lectura que queda fuera del rango permitido"), ("bodeguero", "persona que lleva el inventario de la bodega")],
    worked=[
        ("Revisar una temperatura", "Una carga de ejemplo exige de 0 a 4 grados y el registro marca 3. ¿Está dentro del rango?", ["El rango va de 0 a 4 grados.", "3 está entre 0 y 4."], "Sí, está dentro del rango"),
        ("Leer una etiqueta", "Un envase de ejemplo lleva una etiqueta de peligro con una calavera. ¿Qué indica?", ["La etiqueta resume el tipo de peligro.", "La calavera indica que la mercancía es tóxica."], "Que la mercancía es tóxica"),
    ],
    mistakes=[("Creer que la etiqueta de peligro reemplaza a la hoja de datos de seguridad.", "La etiqueta resume el peligro; la hoja describe peligros y medidas de prevención.", "Revisa que ambas estén presentes y coincidan."),
              ("Dar por conforme un ingreso refrigerado sin registro de temperatura.", "Sin registro no se puede demostrar que se mantuvo la cadena de frío.", "Registra la falta e informa antes de dar por conforme el ingreso.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es una etiqueta de peligro?", "Un rombo con un símbolo y un color que indica el tipo de peligro de una mercancía", "Una etiqueta que indica el peso del bulto", "Un sello numerado de la puerta del contenedor", "La etiqueta de peligro comunica el tipo de peligro; el peso y el sello son otros datos."),
        ("abc", "En Operaciones Portuarias: ¿qué es la hoja de datos de seguridad?", "Un documento que describe los peligros de un producto y las medidas de prevención", "La lista de bultos de un contenedor", "El permiso de ingreso del camión al recinto", "La hoja de datos informa sobre el producto y su prevención."),
        ("abc", "En Operaciones Portuarias: ¿qué es la cadena de frío?", "La continuidad de la temperatura controlada de una carga desde el origen hasta el destino", "La cantidad de cámaras de frío de un puerto", "El hielo que se agrega a la carga para transportarla", "La cadena de frío es la continuidad de la temperatura controlada."),
        ("abc", "{F} ¿Qué producto de la ficha exige una hoja de datos de seguridad?", "Los tambores del producto químico", "Las cajas de repuestos", "Las cajas de fruta", "La hoja de datos corresponde a la mercancía peligrosa, que aquí son los tambores."),
        ("abc", "{F} ¿Cumple el registro de temperatura de ingreso de la fruta con el rango requerido?", "Sí, porque 4 grados está dentro del rango de 2 a 6", "No, porque es menor que 6 grados", "No, porque el rango exige exactamente 6 grados", "Un valor entre el mínimo y el máximo está dentro del rango."),
        ("abc", "{F} ¿Qué marca de manipulación tiene la carga general y qué pide?", "«Mantener seco», que pide protegerla del agua y de la humedad", "«Frágil», que pide trato cuidadoso", "«Este lado arriba», que fija su posición", "La ficha indica que las cajas de repuestos llevan «mantener seco»."),
        ("=", "{F} ¿Cuántos bultos suman los tres productos?", "60+20+90", "Se suman las cajas de fruta, los tambores y las cajas de repuestos.", " bultos"),
        ("=", "{F} ¿Cuántos kilogramos pesa en total el ingreso?", "60*12+20*40+90*25", "Se multiplica cada cantidad por su peso unitario y se suman los tres productos.", " kg"),
        ("abc", "Un registro de ejemplo de una cámara marca, en cinco lecturas, 3, 4, 5, 7 y 8 grados, con rango permitido de 2 a 6 grados. ¿Cuántas lecturas están fuera del rango?", "2 lecturas", "1 lectura", "3 lecturas", "Solo 7 y 8 superan el máximo de 6; las otras tres están dentro del rango."),
        ("abc", "{F} ¿Por qué los tambores de la ficha no pueden almacenarse junto a las cajas de fruta?", "Porque son mercancía peligrosa y se segregan según su hoja de datos de seguridad y la norma vigente", "Porque los tambores deben ir siempre al aire libre", "Porque la etiqueta de peligro solo aplica a la carga de otros países", "Una mercancía peligrosa se segrega; la fruta es refrigerada y no debe compartir zona con ella."),
        ("abc", "{F} Falta el registro de temperatura de ingreso del lote de fruta. ¿Qué corresponde?", "No dar por conforme el ingreso: registrar la falta e informar a quien corresponde", "Anotar una temperatura probable para completar el registro", "Recibir el lote y completar el registro cuando se pueda", "Sin registro no se demuestra la cadena de frío; no se inventan datos."),
        ("=", "{F} Un estante de ejemplo para tambores admite como máximo 200 kg. ¿Cuántos tambores de la ficha admite?", "200//40", "Se divide el peso máximo del estante entre el peso de cada tambor.", " tambores"),
        ("abc", "{F} Un jefe pide recibir los 20 tambores y dejarlos en la zona de carga general «un par de horas». ¿Qué corresponde?", "Que se ubiquen en la zona señalizada y segregada para mercancías peligrosas, con personal capacitado", "Aceptar, porque es solo por un par de horas", "Aceptar, si se cubren con una lona", "La segregación se aplica desde el ingreso, aunque sea por poco tiempo."),
    ],
    ctx=("abc", "Una persona de la oficina de ejemplo te dice: «el lote de fruta llegó con el registro de temperatura en blanco, pero seguro venía frío; anota que estuvo en el rango». ¿Qué respondes?", "Que no se anota un dato que no se tiene: se registra la falta y se informa a quien corresponde", "Que lo anotas, porque seguro venía frío", "Que lo anotas en lápiz para borrarlo si hay reclamo", "Inventar un registro oculta una posible ruptura de la cadena de frío."),
    sc=[
        ("En Operaciones Portuarias: ¿qué indica una etiqueta de peligro con una llama?", "Que la mercancía es inflamable", "La llama es el símbolo de las mercancías inflamables."),
        ("¿Para qué sirve el registro de temperatura?", "Para demostrar que se mantuvo la cadena de frío", "Es la evidencia de que la carga estuvo en su rango."),
        ("¿Quién lleva el inventario de la bodega?", "El bodeguero", "El bodeguero registra lo que entra y sale."),
    ],
    op=("Registro de ingreso de ejemplo. Producto 1: 30 cajas de carne de ejemplo, de 20 kg cada una; rango requerido de 0 a 4 grados; el registro de ingreso marca 3 grados. Producto 2: 12 bidones de un producto de ejemplo, de 25 kg cada uno, con etiqueta de peligro con calavera y sin hoja de datos de seguridad. Producto 3: 40 cajas de herramientas, de 15 kg cada una, con la marca «este lado arriba». Escribe (a) cuántos bultos suman, (b) cuántos kilogramos pesan, (c) si la temperatura de la carne cumple el rango, (d) qué hacer con los bidones.",
        "(a) 30 + 12 + 40 = 82 bultos. (b) 30 × 20 + 12 × 25 + 40 × 15 = 600 + 300 + 600 = 1.500 kg. (c) Sí, porque 3 grados está entre 0 y 4. (d) No darlos por conformes: falta la hoja de datos de seguridad; se registra la falta, se informa a quien corresponde y se mantienen segregados, con personal capacitado.",
        ["suma los bultos", "calcula el peso total", "compara la temperatura con el rango", "indica registrar la falta, informar y segregar"],
        ["hoja con las cuatro respuestas"],
        ["olvidar multiplicar por el peso unitario", "dar por conforme un ingreso sin hoja de datos", "inventar el dato faltante"],
        "Pregunta: «¿qué documento acompaña a una mercancía peligrosa?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un registro de ingreso con tres productos de tipos distintos y anota qué documento o registro exige cada uno.",
    extend="Explica con un ejemplo por qué la etiqueta de peligro y la hoja de datos de seguridad se complementan.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (inventario de ejemplo, inventado). Zona A de la «Bodega Demo»: 20 posiciones de estantería; cada posición admite 1 pallet y hasta 800 kg (valor de ejemplo). Inventario: producto P, lote P1 (ingresó el día 3), 4 pallets de 600 kg cada uno; "
     "producto P, lote P2 (ingresó el día 9), 4 pallets de 600 kg cada uno; producto Q, 6 pallets de 750 kg cada uno; producto R, 4 pallets de 850 kg cada uno.")
build(
    O4, 3, F,
    use="Aprenderé a leer un inventario, a calcular posiciones ocupadas y pesos, a aplicar la regla PEPS de rotación y a detectar asignaciones que no cumplen el límite.",
    prior=["Sé multiplicar y sumar números enteros.", "Sé qué es un límite de peso.", "Sé qué es un lote."],
    explain=[
        "El inventario es el registro de la cantidad de cada producto que hay almacenado y de su ubicación. Una posición de estantería es un espacio para un pallet, con un límite de peso que no puede superarse. Con el inventario se calculan las posiciones ocupadas, las libres y el peso total. Basta que un pallet supere el límite de su posición para que la planilla no esté en orden.",
        "La rotación es el orden en que la carga entra y sale. La regla PEPS significa primero en entrar, primero en salir: sale primero el lote que ingresó antes. Sirve para que la carga no quede almacenada demasiado tiempo y pierda calidad o venza. Una excepción solo se admite con una razón registrada. El inventario se registra con los datos reales y no se cambia para que cuadre; una diferencia se informa.",
        f"Los límites y los pesos de esta clase son de ejemplo. Los reales dependen de la estantería y de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("inventario", "registro de la cantidad de cada producto almacenado y de su ubicación"), ("posición", "espacio de la estantería para un pallet"), ("pallet", "plataforma sobre la que se arma una carga"), ("lote", "conjunto de carga que ingresó junto"), ("PEPS", "primero en entrar, primero en salir"), ("rotación", "orden en que la carga entra y sale")],
    worked=[
        ("Posiciones libres", "Una zona de ejemplo tiene 15 posiciones y hay 11 pallets. ¿Cuántas posiciones quedan libres?", ["Cada pallet ocupa una posición.", "15 menos 11 son 4."], "4 posiciones libres"),
        ("Aplicar PEPS", "El lote M1 ingresó el día 2 y el lote M2 el día 5, del mismo producto. Se despacha una parte. ¿De qué lote sale primero?", ["PEPS saca primero lo que entró primero.", "El lote M1 entró antes que M2."], "Del lote M1"),
    ],
    mistakes=[("Despachar primero el lote que está más a mano sin mirar su fecha de ingreso.", "Rompe la regla PEPS y un lote puede vencer o perder calidad.", "Revisa la fecha de ingreso de cada lote antes de despachar."),
              ("Creer que si el total de posiciones alcanza, la zona está en orden.", "Cada posición tiene su propio límite de peso.", "Revisa también el peso por posición.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es el inventario de una bodega?", "El registro de la cantidad de cada producto almacenado y de su ubicación", "El permiso de salida de un camión", "El plano de las rutas de circulación", "El inventario registra qué hay y dónde; el permiso y el plano son otros documentos."),
        ("abc", "En Operaciones Portuarias: ¿qué significa la regla PEPS?", "Primero en entrar, primero en salir", "Primero en pesar, primero en salir", "Producto en estantería, primero en servir", "PEPS es la regla de rotación por orden de ingreso."),
        ("abc", "En Operaciones Portuarias: ¿qué es la rotación de la carga?", "El orden y el momento en que la carga entra y sale de la bodega", "El giro de los pallets al apilarlos", "El cambio de turno del personal", "La rotación se refiere al movimiento de entrada y salida de la carga."),
        ("=", "{F} ¿Cuántas posiciones están ocupadas?", "4+4+6+4", "Se suman los pallets de todos los productos, que ocupan una posición cada uno.", " posiciones"),
        ("=", "{F} ¿Cuántas posiciones quedan libres?", "20-(4+4+6+4)", "Se restan las posiciones ocupadas a las 20 de la zona.", " posiciones"),
        ("abc", "{F} ¿Qué producto supera el peso máximo permitido por posición?", "El producto R", "El producto P", "El producto Q", "Los pallets de R pesan 850 kg y el máximo es 800; P y Q están bajo el límite."),
        ("=", "{F} ¿Cuántos kilogramos hay en total en la zona A?", "4*600+4*600+6*750+4*850", "Se multiplican los pallets de cada producto por su peso y se suman.", " kg"),
        ("abc", "{F} Se despachan 4 pallets del producto P. Según PEPS, ¿de qué lote salen?", "Del lote P1, porque ingresó primero", "Del lote P2, porque ingresó último", "De cualquiera de los dos, porque es el mismo producto", "PEPS saca primero lo más antiguo, que es el lote P1."),
        ("=", "{F} Llegan 5 pallets del producto Q. ¿Cuántos quedan sin posición libre?", "5-(20-(4+4+6+4))", "Se restan las posiciones libres a los pallets que llegan.", " pallets"),
        ("abc", "{F} Un compañero dice: «las posiciones alcanzan, así que la zona está en orden». ¿Qué respuesta es correcta?", "Es falso: los pallets de R superan el peso máximo por posición", "Es cierto: lo único que importa es la cantidad de posiciones", "Es cierto, si el producto R es el más nuevo", "El límite de peso por posición es una condición aparte del número de posiciones."),
        ("abc", "{F} Se despachan 4 pallets de P, pero la jefatura pide sacar los del lote P2 «porque están más a mano». ¿Qué riesgo tiene?", "Que el lote P1 quede almacenado demasiado tiempo y pierda calidad o venza", "Ninguno, porque el producto no cambia con el tiempo", "Que el lote P2 se descargue antes de llegar", "Romper PEPS puede dejar al lote más antiguo sin salida a tiempo."),
        ("=", "{F} Si se retira un pallet de R y los otros 3 se mantienen, ¿cuántos kilogramos quedan en la zona?", "4*600+4*600+6*750+3*850", "Se recalcula el total con 3 pallets de R en lugar de 4.", " kg"),
        ("abc", "{F} ¿Qué propuesta corrige la planilla respecto del producto R?", "Reubicar los pallets de R en posiciones con un límite de peso adecuado o dividir su carga", "Anotar que cada pallet de R pesa 800 kg", "Quitar el límite de 800 kg de las posiciones", "Se corrige la ubicación o la carga; no se altera el registro ni el límite."),
    ],
    ctx=("abc", "Un compañero de práctica te dice: «anota que los pallets de R pesan 800 kg, así el inventario queda sin problemas». ¿Qué respondes?", "Que no, porque el registro debe reflejar el peso real y el exceso se informa a quien corresponde", "Que sí, porque la diferencia es pequeña", "Que sí, y después se corrige", "Un registro falso oculta un exceso real sobre una posición."),
    sc=[
        ("En Operaciones Portuarias: ¿qué lote sale primero según PEPS?", "El que ingresó antes", "PEPS ordena por fecha de ingreso."),
        ("¿Cuántas posiciones libres hay si hay 20 y 18 están ocupadas?", "2 posiciones", "Se restan las ocupadas al total."),
        ("¿Qué se revisa además del número de posiciones?", "El límite de peso de cada posición", "Cada posición tiene su propio límite de peso."),
    ],
    op=("Zona B de una bodega de ejemplo: 10 posiciones, cada una con 1 pallet y hasta 500 kg (valor de ejemplo). Inventario: producto S, lote S1 (ingresó el día 2), 3 pallets de 400 kg; producto S, lote S2 (ingresó el día 6), 3 pallets de 400 kg; producto T, 2 pallets de 550 kg. Escribe (a) cuántas posiciones están ocupadas y cuántas libres, (b) qué producto supera el límite por posición, (c) de qué lote sale primero si se despachan 3 pallets de S, (d) cuántos kilogramos hay en total.",
        "(a) 3 + 3 + 2 = 8 ocupadas; 10 − 8 = 2 libres. (b) El producto T, porque 550 kg supera los 500 kg por posición. (c) Del lote S1, porque ingresó antes (PEPS). (d) 3 × 400 + 3 × 400 + 2 × 550 = 1.200 + 1.200 + 1.100 = 3.500 kg.",
        ["calcula posiciones ocupadas y libres", "identifica el producto que excede", "aplica PEPS", "calcula el peso total"],
        ["hoja con las cuatro respuestas"],
        ["no revisar el límite por posición", "sacar primero el lote más nuevo", "olvidar multiplicar por los pallets"],
        "Pregunta: «¿qué lote entró primero?». Si no responde, pídele que compare los días de ingreso."),
    reinforce="Inventa un inventario con dos lotes de un mismo producto y escribe de cuál saldría primero una parte.",
    extend="Explica con un ejemplo por qué un producto perecible no debería salir del lote más nuevo antes que del más antiguo.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (caso de ejemplo, inventado). Una cámara refrigerada de ejemplo tiene capacidad para 300 pallets y un rango de temperatura permitido de 2 a 6 grados; hoy hay 240 pallets. "
     "Se registra la temperatura cada 2 horas; las últimas cinco lecturas marcan 3, 4, 5, 7 y 4 grados. Costo de almacenaje de ejemplo: $1.500 por pallet por día en la cámara y $800 por pallet por día en la bodega general. "
     "La zona C, de mercancías peligrosas, admite como máximo 50 tambores (valor de ejemplo) y hoy tiene 35.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar criterios de capacidad, temperatura y costo al almacenar cargas refrigeradas y peligrosas, y a decidir qué se recibe y qué se deriva.",
    prior=["Sé calcular posiciones libres y costos.", "Sé qué es el rango de temperatura y la cadena de frío.", "Sé qué es la segregación."],
    explain=[
        "Al decidir si se recibe una carga se comprueba la capacidad: los pallets libres son la capacidad menos los que ya hay, y solo se recibe lo que cabe. En la zona de mercancías peligrosas, el máximo de ejemplo se respeta siempre; el exceso no se recibe y se deriva según indique la jefatura y la norma vigente. Una carga refrigerada solo se almacena en una cámara con su rango controlado, aunque la bodega general sea más barata.",
        "El rango de temperatura permitido tiene un mínimo y un máximo. Una lectura fuera del rango es una desviación: se registra con su hora y su duración y se informa a quien corresponde para evaluar la carga; no se borra ni se cambia. El costo de almacenaje es lo que cuesta mantener la carga por cierto tiempo: se multiplica el costo por pallet por día, la cantidad de pallets y los días.",
        f"Todos los datos de capacidad, temperatura y costo son de ejemplo. Los reales dependen de la instalación y de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("capacidad", "cantidad máxima de pallets o de tambores que puede recibir una zona"), ("rango de temperatura", "valores mínimo y máximo dentro de los cuales debe mantenerse la carga"), ("desviación", "lectura de temperatura fuera del rango permitido"), ("costo de almacenaje", "lo que cuesta mantener una carga almacenada por cierto tiempo"), ("derivar", "enviar la carga que no cabe a otro lugar según indique la jefatura")],
    worked=[
        ("Costo de almacenaje", "Se almacenan 20 pallets durante 3 días a $500 por pallet por día. ¿Cuánto cuesta?", ["Se multiplican pallets, días y costo diario.", "20 por 3 son 60, y 60 por 500 son 30.000."], "$30.000"),
        ("Revisar la capacidad", "Una zona de ejemplo admite 80 tambores y tiene 62. Llegan 25. ¿Caben?", ["Los espacios libres son 80 menos 62, o sea 18.", "25 supera 18."], "No caben: solo hay espacio para 18"),
    ],
    mistakes=[("Recibir toda la carga que llega y acomodar el exceso donde se pueda.", "Se supera la capacidad y se pierde la segregación y el orden.", "Recibe solo lo que cabe y deriva el resto según indique la jefatura."),
              ("Cambiar una lectura de temperatura para que quede en rango.", "Oculta una desviación real que puede haber dañado la carga.", "Registra la lectura tal cual e informa.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es el rango de temperatura permitido de una carga refrigerada?", "Los valores mínimo y máximo dentro de los cuales debe mantenerse la carga", "La temperatura promedio de todo el puerto", "El número de grados que se baja cada hora", "El rango fija el mínimo y el máximo aceptables para esa carga."),
        ("abc", "En Operaciones Portuarias: ¿qué es una desviación de temperatura?", "Una lectura fuera del rango permitido, que se registra e informa", "Una lectura que coincide con el máximo del rango", "El cambio de turno del encargado de la cámara", "Una lectura igual al máximo sigue dentro del rango; la desviación sale del rango."),
        ("abc", "En Operaciones Portuarias: ¿qué es el costo de almacenaje?", "Lo que cuesta mantener una carga almacenada por cierto tiempo", "Lo que cuesta transportarla hasta el puerto", "El valor del seguro de la carga", "El almacenaje cuesta por el espacio y el tiempo en que la carga queda guardada."),
        ("=", "{F} ¿Cuántos pallets libres tiene hoy la cámara?", "300-240", "Se resta a la capacidad los pallets que hay.", " pallets"),
        ("abc", "{F} Llegan 2 camiones con 25 pallets refrigerados cada uno. ¿Caben en la cámara?", "Sí, porque 50 pallets caben en los 60 espacios libres", "No, porque 50 pallets superan los 240 que ya hay", "No, porque cada camión debe traer 30 pallets", "Los espacios libres son 60 y llegan 50."),
        ("abc", "{F} ¿Cuántas de las cinco últimas lecturas están fuera del rango permitido?", "1 lectura", "2 lecturas", "Ninguna", "Solo la de 7 grados supera el máximo de 6; las otras están entre 2 y 6."),
        ("=", "{F} ¿Cuántos tambores más puede recibir la zona C?", "50-35", "Se resta al máximo los tambores que hay.", " tambores"),
        ("abc", "{F} Llegan 20 tambores a la zona C. ¿Qué corresponde?", "No recibir los 20: solo caben 15 y los 5 restantes se derivan según indique la jefatura y la norma vigente", "Recibir los 20 y apilar los 5 sobrantes fuera de la zona", "Recibir los 20 porque el máximo es aproximado", "Se respeta el máximo de la zona y el exceso se deriva."),
        ("=", "{F} ¿Cuántos pesos cuesta mantener 40 pallets de fruta durante 5 días en la cámara?", "40*1500*5", "Se multiplican los pallets, el costo por día y los días.", " pesos"),
        ("abc", "{F} Un compañero dice: «la fruta puede ir a la bodega general porque es más barata». ¿Qué respuesta es correcta?", "Es falso: la carga refrigerada exige cámara con rango controlado y ahorrar no justifica perder la calidad", "Es cierto: lo importante es ahorrar", "Es cierto, si la estadía es corta", "El costo no reemplaza las condiciones que exige la carga."),
        ("abc", "En Operaciones Portuarias: ¿por qué se registra la temperatura cada cierto tiempo?", "Para demostrar que la carga se mantuvo dentro del rango y detectar a tiempo una desviación", "Para que el personal tenga una tarea periódica", "Para que la cámara gaste menos energía", "El registro es evidencia y permite reaccionar a tiempo."),
        ("=", "{F} Si, además de 40 pallets de fruta 5 días en la cámara, se guardan 10 pallets de repuestos 5 días en la bodega general, ¿cuántos pesos cuesta el almacenaje total?", "40*1500*5+10*800*5", "Se calcula el costo de cada carga con su tarifa y se suman.", " pesos"),
        ("abc", "{F} Una lectura de 8 grados dura 3 horas por una falla y luego la temperatura vuelve al rango. ¿Qué corresponde?", "Registrar la desviación con su hora y duración e informar a quien corresponde para evaluar la carga", "Borrar la lectura, porque ya volvió al rango", "Anotar 6 grados para que quede dentro del rango", "La desviación ocurrió y debe quedar registrada aunque haya terminado."),
    ],
    ctx=("abc", "Un conocido te dice: «llegaron más tambores de los que caben en la zona C; déjalos un rato afuera, nadie se va a dar cuenta». ¿Qué respondes?", "Que no se pueden dejar fuera de la zona: el exceso se deriva según indique la jefatura y la norma vigente", "Que sí, mientras sea poco tiempo", "Que sí, si los tapas con una lona", "Las mercancías peligrosas no se dejan fuera de su zona segregada."),
    sc=[
        ("En Operaciones Portuarias: ¿cómo se calculan los pallets libres de una cámara?", "Restando los pallets que hay a la capacidad", "La capacidad menos lo ocupado da el espacio libre."),
        ("¿Qué se hace con una lectura fuera del rango?", "Se registra y se informa a quien corresponde", "Una desviación no se borra ni se cambia."),
        ("¿Cómo se calcula el costo de almacenaje?", "Pallets por costo por día por días", "Se multiplican las tres cantidades y se obtiene el costo."),
    ],
    op=("Cámara refrigerada de ejemplo con capacidad para 200 pallets y rango permitido de 1 a 5 grados; hoy hay 150 pallets. Llegan 2 camiones con 20 pallets cada uno. Las últimas cinco lecturas marcan 2, 3, 4, 6 y 3 grados. Costo de ejemplo: $1.200 por pallet por día; se almacenan 30 pallets durante 4 días. Escribe (a) cuántos pallets libres hay y si caben los que llegan, (b) cuántas lecturas están fuera del rango, (c) cuánto cuesta el almacenaje de los 30 pallets, (d) qué hacer con la lectura fuera del rango.",
        "(a) 200 − 150 = 50 libres; llegan 40, así que caben. (b) 1 lectura, la de 6 grados. (c) 30 × 1.200 × 4 = $144.000. (d) Registrarla con su hora y su duración e informar a quien corresponde para evaluar la carga, sin cambiarla.",
        ["calcula los pallets libres y compara", "identifica las lecturas fuera del rango", "calcula el costo", "indica registrar e informar la desviación"],
        ["hoja con las cuatro respuestas"],
        ["olvidar multiplicar por los días", "contar como desviación una lectura dentro del rango", "cambiar la lectura"],
        "Pregunta: «¿cuál es el máximo del rango?». Si no responde, pídele que relea el rango del enunciado."),
    reinforce="Inventa una zona con capacidad y ocupación y calcula cuánta carga más puede recibir.",
    extend="Explica con un ejemplo por qué una desviación de temperatura se registra aunque la carga parezca estar bien.",
)

# ============================================================ OAE-04, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). Hay que almacenar 400 pallets durante 10 días. Alternativa X (bodega propia): 25 pallets por cada 100 m²; costo de ejemplo $200 por m² por día; área disponible: 1.600 m². "
     "Alternativa Y (bodega externa): $750 por pallet por día más un traslado único de $500.000. Lista de verificación del almacenamiento (5 puntos): etiquetas legibles; segregación de mercancías peligrosas; límites de peso respetados; registro de temperatura al día; "
     "pasillos y salidas despejados. En la revisión de ejemplo, 4 de los 5 puntos están en orden.")
build(
    O4, 5, F,
    use="Aprenderé a comparar alternativas de almacenamiento por costo y espacio y a verificar la calidad con una lista de verificación bajo el principio de cero faltas.",
    prior=["Sé calcular costos por día y por espacio.", "Sé qué es una lista de verificación.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Al elegir entre dos alternativas de almacenamiento se comparan el espacio que necesitan, el costo total y el plazo. Una alternativa solo sirve si tiene el espacio suficiente; entre las que sirven, conviene la de menor costo total. El costo total suma todos los costos: el de cada día por los días, más los costos únicos, como un traslado.",
        "La calidad del almacenamiento se verifica con una lista de verificación: puntos como etiquetas legibles, segregación respetada, límites de peso, registros de temperatura y pasillos y salidas despejados. El porcentaje de cumplimiento es el porcentaje de puntos que están en orden respecto del total. Bajo el principio de cero faltas, la revisión solo se da por buena cuando todos los puntos están en orden: si falta uno, se corrige primero.",
        f"Los costos y las áreas son de ejemplo. Una bodega externa también se verifica con la lista. {EMER} {AVISO}",
    ],
    vocab=[("alternativa de almacenamiento", "una de las formas posibles de guardar la carga"), ("costo total", "suma de todos los costos, diarios y únicos"), ("lista de verificación", "lista de puntos que se revisan uno por uno"), ("porcentaje de cumplimiento", "porcentaje de puntos que están en orden respecto del total"), ("cero faltas", "meta de que todos los puntos estén en orden antes de aprobar")],
    worked=[
        ("Comparar costos", "Hay que almacenar 100 pallets 4 días. La bodega M cuesta $400 por pallet por día. La bodega N cuesta $350 por pallet por día más un traslado de $20.000. ¿Cuál conviene?", ["M cuesta 100 por 4 por 400, o sea $160.000.", "N cuesta 100 por 4 por 350, o sea $140.000, más $20.000, que son $160.000."], "Cuestan lo mismo: $160.000"),
        ("Porcentaje de cumplimiento", "Una lista de ejemplo tiene 8 puntos y 6 están en orden. ¿Qué porcentaje de cumplimiento tiene?", ["6 de 8 son 75 de cada 100.", "Faltan 2 puntos por corregir."], "75 %"),
    ],
    mistakes=[("Elegir la alternativa más barata por día sin sumar los costos únicos.", "El traslado u otros costos únicos cambian el costo total.", "Suma los costos diarios y los únicos antes de comparar."),
              ("Aprobar una revisión con un punto pendiente porque el porcentaje es alto.", "El principio de cero faltas exige que todos los puntos estén en orden.", "Corrige el punto pendiente antes de aprobar.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué se compara al elegir entre una bodega propia y una externa?", "El espacio disponible, el costo total, el plazo y los riesgos de cada alternativa", "Solo la distancia de cada bodega hasta el puerto", "Solo el costo por día de cada alternativa", "La decisión considera espacio, costo total y riesgos, no solo el costo diario."),
        ("abc", "En Operaciones Portuarias: ¿qué significa cero faltas al revisar una bodega?", "Que todos los puntos de la lista de verificación deben estar en orden antes de aprobar", "Que se puede aceptar una falta si es pequeña", "Que ninguna persona puede ausentarse del turno", "Cero faltas se refiere a los puntos de la revisión, no a la asistencia."),
        ("abc", "En Operaciones Portuarias: ¿qué es el porcentaje de cumplimiento de una lista de verificación?", "El porcentaje de puntos que están en orden respecto del total", "El porcentaje de la bodega que está ocupada", "El porcentaje de personas que firmaron la lista", "El cumplimiento compara los puntos en orden con los puntos totales."),
        ("=", "{F} ¿Cuántos metros cuadrados necesita la alternativa X para los 400 pallets?", "400//25*100", "Se calcula cuántos grupos de 25 pallets hay y se multiplican por 100 m².", " m²"),
        ("=", "{F} ¿Cuántos pesos cuesta la alternativa X durante los 10 días?", "400//25*100*200*10", "Se multiplican los metros cuadrados, el costo por metro cuadrado y los días.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta la alternativa Y durante los 10 días, con el traslado?", "400*750*10+500000", "Se calcula el costo diario por los pallets y los días y se suma el traslado.", " pesos"),
        ("abc", "{F} ¿Qué alternativa conviene?", "La X, porque tiene espacio suficiente y cuesta menos", "La Y, porque no tiene límite de espacio", "Ninguna, porque las dos tienen el mismo costo", "La alternativa X cuesta menos y su área alcanza."),
        ("=", "{F} ¿Cuántos pesos más cuesta la alternativa Y que la X?", "(400*750*10+500000)-(400//25*100*200*10)", "Se resta el costo de la alternativa X al de la alternativa Y.", " pesos"),
        ("=", "{F} ¿Qué porcentaje de cumplimiento tiene la revisión de ejemplo?", "4*100//5", "Se divide los puntos en orden entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} Con 4 de los 5 puntos en orden, ¿se puede dar por buena la revisión?", "No: bajo cero faltas se corrige el punto pendiente antes de aprobar", "Sí, porque 80 % es suficiente", "Sí, si el punto pendiente es el de los pasillos", "Cero faltas exige que todos los puntos estén en orden."),
        ("abc", "{F} Si la bodega propia tuviera solo 1.200 m² disponibles, ¿qué ocurriría con la alternativa X?", "No alcanzaría para los 400 pallets, que necesitan 1.600 m²", "Alcanzaría, porque 1.200 m² son suficientes", "Alcanzaría si se amontonan los pallets", "El espacio disponible no cubre los metros cuadrados que se necesitan."),
        ("=", "{F} Si el almacenamiento fuera de 20 días en lugar de 10, ¿cuántos pesos más cuesta la alternativa Y que la X?", "(400*750*20+500000)-(400//25*100*200*20)", "Se recalculan ambos costos con 20 días y se restan.", " pesos"),
        ("abc", "{F} Un jefe dice: «elijamos Y y nos ahorramos la lista de verificación». ¿Qué respuesta es correcta?", "Es falso: la lista se revisa con cualquier alternativa, también en una bodega externa", "Es cierto: la lista solo se usa en bodegas propias", "Es cierto, si la bodega externa tiene buena fama", "La verificación de calidad no depende de quién tenga la bodega."),
    ],
    ctx=("abc", "En una revisión de ejemplo, un punto de la lista está en blanco y el encargado dice: «márcalo como revisado, seguro está en orden». ¿Qué respondes?", "Que se revisa el punto y solo entonces se marca; si no se puede, se informa", "Que lo marcas, porque seguro está en orden", "Que lo marcas y lo revisas el mes siguiente", "Marcar sin revisar falsea la lista y puede ocultar una falta."),
    sc=[
        ("En Operaciones Portuarias: ¿qué es el costo total de una alternativa?", "Todos los costos, diarios y únicos, sumados", "El costo total incluye también los costos que se pagan una sola vez."),
        ("¿Qué exige el principio de cero faltas?", "Que todos los puntos de la lista estén en orden antes de aprobar", "Un punto pendiente impide aprobar la revisión."),
        ("¿Cómo se calcula el porcentaje de cumplimiento?", "Puntos en orden entre puntos totales, por 100", "El resultado se expresa como porcentaje."),
    ],
    op=("Hay que almacenar 200 pallets durante 5 días. Alternativa X (bodega propia): 20 pallets por cada 100 m²; costo de ejemplo $150 por m² por día; área disponible: 1.000 m². Alternativa Y (bodega externa): $600 por pallet por día más un traslado único de $300.000. La lista de verificación tiene 4 puntos y, en la revisión de ejemplo, 3 están en orden. Escribe (a) los metros cuadrados que necesita X y si alcanza, (b) el costo de X, (c) el costo de Y, (d) qué alternativa conviene y qué hacer con el punto pendiente.",
        "(a) 200 ÷ 20 × 100 = 1.000 m²; justo alcanza. (b) 1.000 × 150 × 5 = $750.000. (c) 200 × 600 × 5 + 300.000 = $900.000. (d) Conviene X, que alcanza y cuesta menos. El punto pendiente se corrige antes de aprobar la revisión, porque rige el principio de cero faltas.",
        ["calcula el espacio de X y compara", "calcula el costo de X", "calcula el costo de Y con el traslado", "elige y aplica cero faltas"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el traslado de Y", "no comprobar el espacio de X", "aprobar con un punto pendiente"],
        "Pregunta: «¿qué pasa si falta un punto de la lista?». Si no responde, pídele que relea el final del segundo párrafo."),
    reinforce="Inventa dos alternativas de almacenamiento con un costo diario y un costo único y calcula cuál es más barata para un plazo que elijas.",
    extend="Explica con un ejemplo por qué comparar solo el costo por día puede llevar a una mala decisión.",
)
