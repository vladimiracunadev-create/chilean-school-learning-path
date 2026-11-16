"""Educación Ciudadana 4.º medio FG: OA 03 (modelos de desarrollo, políticas económicas y cambio climático) y OA 04 (derechos laborales). Casos y cifras de ejemplo inventados."""
from __future__ import annotations

from fg_eciu_common import build

O3 = "FG-ECIU-4M-OAC-03"
O4 = "FG-ECIU-4M-OAC-04"

# ============================================================ OA 03, clase 1
F = ("Ficha 47 (país ficticio de ejemplo, Costa Nueva, con datos inventados): la economía creció 4 % en un año, pero un barrio minero tiene agua contaminada y el 20 % de su población vive con ingresos muy bajos. "
     "El gobierno aplica una política fiscal (cobra impuestos y gasta en servicios), una política monetaria (el banco central regula la inflación, es decir, el alza general de precios) y una política comercial (aranceles, impuestos a productos importados). "
     "Las emisiones de gases de efecto invernadero del país son bajas por persona, pero sufre sequías cada vez más largas.")
build(
    O3, 1, F,
    use="Aprenderé qué son los modelos de desarrollo y las políticas económicas, cómo influyen en la vida cotidiana y en el cambio climático, y qué significa una vida digna y justa para todas las personas.",
    prior=["Sé qué son el mercado y el Estado.", "Sé qué es la sustentabilidad.", "Sé qué es la justicia ambiental."],
    explain=[
        "Un modelo de desarrollo es una forma de entender el progreso de un país y de organizar su economía. Algunos ponen el acento en el crecimiento económico, es decir, el aumento de lo que el país produce. Otros miden el desarrollo humano: salud, educación y calidad de vida. El desarrollo sustentable agrega el cuidado del ambiente y de las generaciones futuras. Un país puede crecer y aun así tener desigualdad o daño ambiental.",
        "Las políticas económicas son decisiones del Estado para influir en la economía. La política fiscal usa impuestos y gasto público. La política monetaria controla el dinero y la inflación. La política comercial regula el comercio con otros países, por ejemplo mediante aranceles. Estas decisiones afectan lo cotidiano: precios, empleo, servicios públicos y cuentas del hogar.",
        "El cambio climático es el cambio de largo plazo del clima, provocado en gran parte por las emisiones de gases de efecto invernadero que producen actividades humanas, sobre todo la quema de combustibles fósiles. La justicia climática señala que quienes menos contribuyen suelen ser los más afectados. Una vida digna y justa exige desarrollo para todas las personas, sin dañar el clima ni dejar a nadie atrás.",
    ],
    vocab=[("modelo de desarrollo", "forma de entender el progreso de un país y de organizar su economía"), ("crecimiento económico", "aumento de lo que un país produce"), ("política fiscal", "uso de impuestos y gasto público para influir en la economía"), ("inflación", "alza general y sostenida de los precios"), ("justicia climática", "idea de que los costos del cambio climático deben repartirse con justicia")],
    worked=[
        ("Crecimiento y desarrollo", "Un país de ejemplo crece 5 % pero aumenta el número de personas sin acceso a salud. ¿Mejoró el desarrollo humano?", ["El crecimiento no basta.", "Empeoró un aspecto del desarrollo humano."], "No necesariamente"),
        ("Clasificar una política", "El banco central de un país de ejemplo sube las tasas para bajar la inflación. ¿Qué política es?", ["Controla el dinero y los precios.", "Es política monetaria."], "Monetaria"),
    ],
    mistakes=[("Creer que si la economía crece, todos mejoran.", "El crecimiento puede ir acompañado de desigualdad.", "Revisa cómo se reparten los beneficios."),
              ("Pensar que el cambio climático afecta igual a todos.", "Quienes tienen menos recursos suelen sufrir más.", "Pregunta quién contribuye y quién sufre.")],
    T=[
        ('abc', '¿Qué instrumento usa cada política económica?', 'Fiscal: impuestos y gasto público; monetaria: dinero e inflación; comercial: comercio con otros países', 'Fiscal: dinero e inflación; monetaria: impuestos y gasto; comercial: aranceles', 'Fiscal: aranceles; monetaria: impuestos; comercial: dinero e inflación', 'Cada política actúa sobre un ámbito distinto: las cuentas del Estado, el dinero y los precios, o el comercio exterior.'),
        ('abc', '{F} Cobrar impuestos y gastar en servicios, ¿qué tipo de política es?', 'Fiscal', 'Monetaria', 'Comercial', 'Usa los impuestos y el gasto público.'),
        ('abc', '{F} Que el banco central regule la inflación, ¿qué tipo de política es?', 'Monetaria', 'Fiscal', 'Comercial', 'Controla el dinero y los precios.'),
        ('abc', '{F} Costa Nueva creció 4 % en un año, pero un barrio minero tiene agua contaminada. ¿Qué indica?', 'Que el crecimiento económico no garantiza bienestar para todas las personas', 'Que el crecimiento elimina la pobreza con el tiempo', 'Que el agua contaminada es inevitable en países que crecen', 'El crecimiento mide cuánto produce el país, no cómo se reparten sus beneficios y costos.'),
        ('abc', '{F} ¿Qué modelo agrega el cuidado del ambiente y de las generaciones futuras?', 'Desarrollo sustentable', 'Crecimiento económico', 'Desarrollo humano', 'El desarrollo humano mide salud y educación; el sustentable agrega el ambiente y el futuro.'),
        ('abc', '{F} ¿Qué aspecto de la justicia climática se ve en Costa Nueva?', 'Emite poco por persona, pero sufre sequías cada vez más largas', 'Emite mucho por persona y sufre pocas sequías', 'Su economía crece, por lo que no le afecta el clima', 'La justicia climática señala que quienes menos contribuyen suelen ser los más afectados.'),
        ('abc', '{F} ¿Qué es la inflación?', 'El alza general de los precios', 'La baja de los salarios', 'El aumento de los impuestos', 'Se refiere al alza general de los precios, que regula la política monetaria.'),
        ('abc', '{F} Un estudiante dice: «Si la economía crece 4 %, el agua del barrio mejora sola». ¿Qué corresponde?', 'Pedir evidencia, pues el crecimiento no garantiza ese resultado', 'Aceptarlo, porque el crecimiento mejora todos los servicios', 'Rechazarlo, porque el crecimiento siempre empeora el ambiente', 'El crecimiento no es automático ni uniforme.'),
        ('abc', '{F} ¿Qué pregunta evalúa si el desarrollo es justo?', '¿Quiénes se benefician y quiénes asumen los costos?', '¿Cuánto creció el país el último año y en qué sectores?', '¿Qué país crece más rápido en la región y en el mundo?', 'La justicia del desarrollo se mira en el reparto de beneficios y costos.'),
        ('abc', '{F} ¿Qué política podría mejorar el agua del barrio minero?', 'Una política fiscal que financie el tratamiento del agua y fiscalice la minería', 'Una política monetaria que baje los precios en todo el país', 'Una política comercial que suba los aranceles', 'Dirige recursos y control al problema local.'),
        ('=', '{F} Si el barrio minero tiene 5.000 habitantes, ¿cuántos viven con ingresos muy bajos?', '5000*20//100', 'Se calcula el 20 % de la población del barrio.', ' personas'),
        ('abc', '¿Qué es el cambio climático?', 'Un cambio de largo plazo del clima, provocado sobre todo por emisiones de gases de efecto invernadero', 'La variación del tiempo atmosférico de un día a otro en una ciudad', 'Una estación seca más larga de lo normal en un año', 'Se distingue del tiempo diario por ser de largo plazo y vinculado a las emisiones humanas.'),
        ('abc', 'Para frenar el alza general de los precios, ¿qué política usa el banco central?', 'Monetaria', 'Fiscal', 'Comercial', 'La política monetaria regula el dinero y la inflación.'),
    ],
    ctx=('abc', 'Un país de ejemplo reduce los aranceles a los productos importados. ¿Qué política económica es?', 'Comercial', 'Monetaria', 'Fiscal', 'Los aranceles regulan el comercio con otros países.'),
    sc=[
        ('¿Qué es el crecimiento económico?', 'El aumento de lo que un país produce', 'No mide cómo se reparte lo producido.'),
        ('abc', '¿Qué es un modelo de desarrollo?', 'Una forma de entender el progreso de un país y de organizar su economía', 'Una ley que fija los precios de los productos en un país', 'Un plan de un solo año para el gobierno de turno', 'Distintos modelos ponen el acento en objetivos distintos.'),
        ('En Educación Ciudadana: ¿qué es la justicia climática?', 'La idea de que los costos del cambio climático deben repartirse con justicia', 'Quienes menos contribuyen suelen ser los más afectados.'),
    ],
    op=("Con la {F} escribe una tabla con tres filas (fiscal, monetaria, comercial): una decisión posible, un efecto en la vida cotidiana y quiénes serían más afectados. Agrega una frase sobre cómo hacer que el desarrollo sea digno y justo.",
        "Fiscal: más gasto en agua potable; mejora la salud; beneficia al barrio minero. Monetaria: controlar la inflación; los precios suben menos; ayuda a hogares de bajos ingresos. Comercial: aranceles a productos que compiten con la producción local; protege empleos pero puede subir precios. Desarrollo digno: crecer cuidando el ambiente y repartiendo beneficios.",
        ["relaciona política y efecto", "identifica quiénes son afectados", "incluye sustentabilidad"], ["tabla de tres filas", "frase final"], ["decir que el crecimiento resuelve todo", "olvidar el reparto"],
        "Pregunta qué política le parece más cercana a su vida diaria."),
    reinforce="Explica la diferencia entre crecimiento económico y desarrollo humano.",
    extend="Anota un precio que haya subido en tu hogar y qué política podría influir en él.",
)

# ============================================================ OA 03, clase 2
F = ("Ficha 48 (caso de ejemplo): en la ciudad ficticia de Puerto Sol, un estudio de ejemplo estimó las emisiones anuales por hogar, en unidades de «kilos de CO2 equivalente» (de ejemplo): "
     "electricidad 1.200; transporte 2.000; calefacción con leña 800; alimentación 1.000. Un hogar cercano a la ciudad, de bajos ingresos, emite 1.500 en total. "
     "Fuentes: el estudio, una carta de vecinos y una nota de prensa.")
build(
    O3, 2, F,
    use="Aprenderé a investigar cómo la vida cotidiana se relaciona con el cambio climático, usando cifras de ejemplo, y a distinguir responsabilidades según las posibilidades de cada hogar.",
    prior=["Sé qué es el cambio climático.", "Sé sumar y calcular porcentajes.", "Sé interpretar un dato de ejemplo."],
    explain=[
        "La huella de carbono es la cantidad de gases de efecto invernadero que emite una persona, un hogar o una actividad. Se mide en unidades de dióxido de carbono equivalente. Sirve para ver en qué parte de la vida cotidiana se emite más y para decidir dónde conviene actuar primero. Las cifras de esta ficha son de ejemplo.",
        "Para investigar se suman las emisiones, se calcula qué porcentaje aporta cada actividad y se comparan hogares. Un hogar con mayores ingresos suele emitir más porque consume más; uno de bajos ingresos emite menos, pero a veces tiene menos opciones de cambiar (por ejemplo, de calefacción). Por eso las responsabilidades se reparten según capacidades y se evitan culpas simples.",
        "Reducir emisiones se llama mitigación; prepararse para los efectos se llama adaptación. Ambas necesitan políticas públicas y hábitos personales. Se prefiere comunicar con honestidad: las cifras de un estudio muestran una estimación, y los cambios individuales son importantes, pero no reemplazan las decisiones colectivas.",
    ],
    vocab=[("huella de carbono", "cantidad de gases de efecto invernadero que emite una persona, hogar o actividad"), ("mitigación", "acciones para reducir las emisiones"), ("adaptación", "acciones para prepararse a los efectos del cambio climático"), ("emisión", "gas que se libera a la atmósfera"), ("estimación", "valor aproximado calculado con datos")],
    worked=[
        ("Calcular una huella", "Un hogar de ejemplo emite 600 por transporte y 400 por electricidad. ¿Cuánto emite en total?", ["Se suman las dos fuentes.", "600 más 400."], "1.000"),
        ("Distinguir mitigación y adaptación", "Instalar árboles que den sombra en un barrio caluroso, ¿qué es?", ["Ayuda a enfrentar el calor.", "Es adaptación."], "Adaptación"),
    ],
    mistakes=[("Responsabilizar de la misma manera a todos los hogares.", "Las posibilidades de cambio son distintas.", "Considera ingresos y opciones disponibles."),
              ("Creer que los cambios personales bastan.", "Se necesitan también políticas colectivas.", "Combina acciones personales y públicas.")],
    T=[
        ('abc', '¿Qué es la huella de carbono?', 'La cantidad de gases de efecto invernadero que emite una persona, un hogar o una actividad', 'La superficie de terreno que ocupa una persona, un hogar o una actividad', 'El consumo de agua que realiza un hogar durante un mes', 'Se mide en unidades de dióxido de carbono equivalente.'),
        ('=', '{F} ¿Cuántas unidades emite el hogar tipo en total?', '1200+2000+800+1000', 'Se suman las cuatro fuentes de emisión.', ' unidades'),
        ('=', '{F} ¿Qué porcentaje del total del hogar tipo corresponde al transporte?', '2000*100//5000', 'Se compara el transporte con el total de 5.000 unidades.', ' %'),
        ('=', '{F} ¿Cuánto más emite el hogar tipo que el hogar de bajos ingresos?', '5000-1500', 'Se resta lo emitido por el hogar de bajos ingresos al total del hogar tipo.', ' unidades'),
        ('abc', '{F} ¿Qué actividad emite más en el hogar tipo?', 'Transporte, con 2.000 unidades', 'Electricidad, con 1.200 unidades', 'Calefacción con leña, con 800 unidades', '2.000 es la mayor de las cuatro cifras.'),
        ('=', '{F} Si el hogar tipo reduce a la mitad la calefacción con leña, ¿cuántas unidades ahorra?', '800//2', 'Se toma la mitad de 800.', ' unidades'),
        ('abc', '{F} ¿Qué es la mitigación?', 'Acciones para reducir las emisiones', 'Acciones para prepararse a los efectos del cambio climático', 'Acciones para medir el clima', 'Mitigar es actuar sobre el origen del problema.'),
        ('abc', '{F} Cambiar de calefacción cuesta dinero. ¿Qué consecuencia tiene para un hogar de bajos ingresos?', 'Tiene menos opciones para cambiar de sistema por el costo', 'Emite más por decisión propia, porque no le importa el ambiente', 'No necesita calefacción porque gasta poca energía', 'El costo limita sus posibilidades, por lo que las responsabilidades se reparten según capacidades.'),
        ('abc', '{F} Alguien dice: «Los hogares de bajos ingresos son los que más contaminan». ¿Qué corresponde?', 'Revisar la ficha: ese hogar emite 1.500, menos que el hogar tipo con 5.000', 'Aceptarlo, porque necesitan usar leña', 'Rechazarlo, porque los hogares de bajos ingresos no emiten', 'Los datos de la ficha muestran lo contrario.'),
        ('abc', '{F} ¿Qué medida pública ayudaría a todos los hogares?', 'Un transporte público más limpio y accesible', 'Prohibir los vehículos sin ofrecer alternativas', 'Pedir solo a cada hogar que reduzca su consumo', 'Reduce emisiones del transporte, la mayor fuente, y mantiene la movilidad.'),
        ('abc', '{F} ¿Qué conclusión es prudente?', 'Las cifras sugieren que el transporte es la mayor fuente y que se necesitan medidas colectivas', 'El estudio prueba que el transporte es el único problema de emisiones', 'Los cambios individuales bastan para resolver por completo el problema', 'Las cifras son estimaciones y los cambios personales no reemplazan las decisiones colectivas.'),
        ('abc', 'Un liceo de ejemplo quiere reducir su huella. ¿Qué medida es de mitigación?', 'Apagar luces y reducir el consumo de electricidad', 'Instalar toldos para dar sombra', 'Instalar ventilación para los días de calor extremo', 'Mitigar es reducir emisiones; los toldos y la ventilación ayudan a adaptarse.'),
        ('abc', 'Un liceo de ejemplo se prepara para olas de calor. ¿Qué medida es de adaptación?', 'Instalar toldos y ventilación para soportar el calor', 'Apagar luces sin uso durante el día y la noche', 'Usar más transporte público en los traslados', 'Adaptarse es prepararse a los efectos del cambio climático.'),
    ],
    ctx=('abc', 'Una familia calcula su huella con una herramienta en línea y obtiene 4.800. ¿Cómo interpretar la cifra?', 'Como una estimación aproximada, útil para comparar y decidir dónde reducir', 'Como la cifra exacta de lo que emite, sin margen de error', 'Como prueba de que contamina más que todos los demás hogares', 'Las cifras de un estudio son estimaciones, no medidas exactas.'),
    sc=[
        ('¿Qué es una emisión?', 'La liberación de gases a la atmósfera por una actividad', 'Las emisiones de gases de efecto invernadero se miden en la huella de carbono.'),
        ('abc', '¿Qué es la adaptación al cambio climático?', 'Prepararse para sus efectos', 'Reducir las emisiones', 'Medir las temperaturas', 'La adaptación actúa sobre los efectos, no sobre el origen.'),
        ('¿Qué es una estimación?', 'Un valor aproximado calculado con datos', 'No es exacto, por eso se comunica con honestidad.'),
    ],
    op=("Con la {F} haz un informe de cinco puntos: total del hogar tipo, porcentaje de cada fuente, diferencia con el hogar de bajos ingresos, una medida personal y una medida pública. No culpes a ningún grupo.",
        "Total: 5.000. Porcentajes: electricidad 24 %, transporte 40 %, leña 16 %, alimentación 20 %. Diferencia: 3.500. Medida personal: compartir viajes. Medida pública: transporte público limpio y accesible.",
        ["calcula bien", "compara hogares", "propone medidas personales y públicas"], ["informe de cinco puntos"], ["culpar a un grupo", "olvidar medidas colectivas"],
        "Pregunta cómo medir la mejora tras un año."),
    reinforce="Explica con un ejemplo la diferencia entre mitigación y adaptación.",
    extend="Anota una actividad cotidiana de tu casa que emita gases y una alternativa.",
)

# ============================================================ OA 03, clase 3
F = ("Ficha 49 (modelos de ejemplo en un país ficticio, Montes Verdes). "
     "Modelo A (crecimiento): atraer inversión con pocos requisitos ambientales para crear empleos rápido. "
     "Modelo B (desarrollo humano): invertir en educación y salud para ampliar capacidades. "
     "Modelo C (economía circular): reutilizar materiales y reparar productos para reducir residuos. "
     "Dato de ejemplo: con el modelo A hubo 1.000 empleos nuevos y 500 hogares con agua contaminada; con el C, 400 empleos nuevos y 0 hogares con agua contaminada.")
build(
    O3, 3, F,
    use="Aprenderé a contrastar modelos de desarrollo con evidencia y valores, reconociendo ventajas, costos y quiénes los asumen.",
    prior=["Sé qué son los modelos de desarrollo.", "Sé comparar perspectivas.", "Sé calcular diferencias simples."],
    explain=[
        "Los modelos de desarrollo ponen el acento en objetivos distintos. El modelo de crecimiento busca aumentar la producción y el empleo con rapidez. El de desarrollo humano busca ampliar las capacidades de las personas, como educación y salud. La economía circular busca reducir residuos reutilizando materiales. Ninguno es perfecto, y en la práctica los países combinan elementos.",
        "Para contrastarlos se examinan sus beneficios (empleos, ingresos, bienestar), sus costos (contaminación, desigualdad) y quién los asume. Un dato aislado, como «1.000 empleos», no basta: hay que preguntar por la calidad de los empleos, por sus efectos ambientales y por el plazo. Algunos costos aparecen años después.",
        "Las posturas dependen de valores: quien prioriza el empleo inmediato verá el modelo A con simpatía; quien prioriza el ambiente verá el C. Una discusión seria presenta ambas razones sin caricaturas, distingue datos de valoraciones y busca combinaciones que reduzcan el daño y mantengan el empleo.",
    ],
    vocab=[("economía circular", "modelo que reutiliza materiales y repara productos para reducir residuos"), ("desarrollo humano", "ampliación de las capacidades de las personas, como salud y educación"), ("costo ambiental", "daño al ambiente que provoca una actividad"), ("calidad del empleo", "condiciones de estabilidad, seguridad y derechos de un trabajo"), ("combinación de modelos", "uso de elementos de varios modelos")],
    worked=[
        ("Comparar empleos", "El modelo X de ejemplo crea 800 empleos y el Y 500. ¿Cuántos más crea X?", ["Se resta 500 a 800.", "Son 300."], "300 empleos más"),
        ("Un costo que aparece después", "Una fábrica de ejemplo crea empleos hoy pero contamina un río que se usará en 10 años. ¿Qué se debe considerar?", ["El costo ambiental futuro.", "Y la calidad de los empleos."], "El costo ambiental a largo plazo"),
    ],
    mistakes=[("Elegir un modelo solo por la cantidad de empleos.", "Falta calidad del empleo y costos ambientales.", "Revisa varios indicadores."),
              ("Presentar a quien prefiere otro modelo como alguien que no se preocupa.", "Es una caricatura.", "Explica el valor que defiende.")],
    T=[
        ('abc', '¿Qué es la economía circular?', 'Reutilizar materiales y reparar productos para reducir residuos', 'Producir cada vez más para vender más productos nuevos', 'Reciclar los productos una sola vez y luego desecharlos', 'Busca que los materiales sigan en uso en vez de convertirse en residuos.'),
        ('abc', '{F} ¿Qué busca el modelo B?', 'Ampliar las capacidades de las personas, como educación y salud', 'Aumentar la producción de bienes y la inversión en la economía', 'Reducir los impuestos que pagan las empresas del país', 'El modelo B invierte en educación y salud.'),
        ('=', '{F} ¿Cuántos empleos más creó el modelo A que el C?', '1000-400', 'Se resta los empleos del C a los del A.', ' empleos'),
        ('=', '{F} Si el territorio tiene 2.500 hogares, ¿qué porcentaje queda con agua contaminada con el modelo A?', '500*100//2500', 'Se compara los hogares afectados con el total.', ' %'),
        ('abc', '{F} ¿Qué valor defiende el modelo A?', 'El empleo y la inversión rápidos', 'La reducción de residuos', 'La ampliación de capacidades en educación y salud', 'El modelo A atrae inversión rápida para crear empleos cuanto antes.'),
        ('abc', '{F} ¿Qué valor defiende el modelo C?', 'La reducción de residuos y el cuidado ambiental', 'Atraer inversión sin requisitos', 'El crecimiento rápido de la producción', 'Reutiliza y repara para generar menos residuos.'),
        ('abc', '{F} ¿Qué costo del modelo A muestra el dato?', '500 hogares con agua contaminada por la actividad', 'Pocos empleos nuevos creados en el territorio', 'Falta de inversión de las empresas en el país', 'El dato muestra un costo ambiental que asumen esos hogares.'),
        ('abc', '{F} Alguien dice: «El modelo A es mejor porque crea más empleos». ¿Qué respuesta es más completa?', 'Hay que mirar también la calidad de los empleos y los costos ambientales', 'Es correcto, porque el empleo es lo único que importa', 'Es falso, porque los empleos siempre dañan el ambiente', 'Un solo indicador no basta para comparar modelos.'),
        ('abc', '{F} ¿Qué combinación podría reducir el daño y mantener empleo?', 'Inversión con requisitos ambientales, educación y reutilización de materiales', 'Prohibir toda inversión nueva en el territorio para evitar daños', 'Atraer inversión sin requisitos y limpiar después si hay problemas', 'Une elementos de los tres modelos para cuidar empleo y ambiente.'),
        ('abc', '{F} ¿Qué dato falta para comparar mejor?', 'La calidad de los empleos y el plazo de los efectos', 'El nombre de las empresas que invierten', 'La opinión de un solo dirigente', 'Algunos costos aparecen años después y no todo empleo es igual.'),
        ('abc', '{F} ¿Qué cuestionaría la justicia ambiental en el modelo A?', 'Que 500 hogares asumen un costo ambiental que otros no asumen', 'Que se creen empleos nuevos con rapidez para el territorio', 'Que el modelo C emplee menos personas que el modelo A', 'Es un reparto desigual de los costos.'),
        ('=', '{F} ¿Qué porcentaje de los empleos del modelo A equivalen a los del modelo C?', '400*100//1000', 'Se compara los empleos del C con los del A.', ' %'),
        ('abc', '{F} ¿Qué significa calidad del empleo?', 'Las condiciones de estabilidad, seguridad y derechos de un trabajo', 'El número de empleos creados en el territorio durante el año', 'La cantidad de horas extra que trabaja cada persona', 'No basta contar empleos; importa cómo son.'),
    ],
    ctx=('abc', 'Una comuna debe elegir entre un centro comercial que crea empleo y un taller que repara productos. ¿Qué modelo se parece al taller?', 'Economía circular', 'Crecimiento económico', 'Desarrollo humano', 'Repara y reutiliza, que es la idea de la economía circular.'),
    sc=[
        ('¿Qué es un costo ambiental?', 'El daño al ambiente o a la salud que produce una actividad', 'Alguien lo asume, a veces años después.'),
        ('abc', '¿Qué significa combinar modelos?', 'Tomar elementos de distintos modelos para equilibrar sus beneficios y costos', 'Elegir un modelo y descartar los demás sin considerar sus aportes', 'Aplicar todos los modelos a la vez sin ordenarlos', 'En la práctica los países combinan elementos de varios modelos.'),
        ('¿Qué es el desarrollo humano?', 'La ampliación de las capacidades de las personas', 'Incluye salud, educación y calidad de vida.'),
    ],
    op=("Con la {F} arma una tabla con los tres modelos: beneficio, costo, quién lo asume y valor que defiende. Escribe luego una combinación de cuatro líneas con un indicador y una medida de compensación para quienes pierden.",
        "A: empleo rápido; agua contaminada para 500 hogares; esos hogares; valor, empleo inmediato. B: capacidades; resultados lentos; el Estado; valor, igualdad. C: menos residuos; pocos empleos nuevos; algunas empresas; valor, cuidado ambiental. Combinación: inversión con requisitos ambientales y capacitación. Indicador: empleos de calidad y hogares con agua segura. Compensación: agua potable para los 500 hogares.",
        ["describe beneficios y costos", "identifica quién asume", "propone compensación"], ["tabla de tres modelos", "combinación"], ["caricaturizar", "comparar con un solo dato"],
        "Pregunta qué evidencia buscaría en el largo plazo."),
    reinforce="Explica por qué los costos de un modelo no siempre los asumen quienes se benefician.",
    extend="Anota un ejemplo de reutilización o reparación que veas en tu barrio.",
)

# ============================================================ OA 03, clase 4
F = ("Ficha 50 (tema de deliberación de ejemplo): un país ficticio evalúa dos políticas para reducir emisiones del transporte. "
     "Política 1: un impuesto a los combustibles que sube el precio de la bencina en 10 %. Política 2: subsidiar el transporte público eléctrico, con fondos del presupuesto. "
     "Argumento a favor de 1: desincentiva el uso de combustibles. Objeción a 1: afecta más a quienes viven lejos del centro y no tienen alternativa. "
     "Argumento a favor de 2: da alternativa a todos. Objeción a 2: cuesta fondos públicos. Dato de ejemplo: 100 familias gastan 40.000 pesos al mes en bencina.")
build(
    O3, 4, F,
    use="Aprenderé a deliberar sobre políticas económicas y climáticas, ponderando eficacia, equidad y costo, y proponiendo medidas que protejan a quienes más podrían perder.",
    prior=["Sé comparar políticas con criterios.", "Sé qué es justicia climática.", "Sé calcular porcentajes."],
    explain=[
        "Las políticas climáticas combinan incentivos y alternativas. Un impuesto sobre el combustible incentiva a usar menos, pero puede afectar más a quienes viven lejos y no tienen transporte público. Un subsidio al transporte limpio da una alternativa, pero requiere financiamiento. Muchas veces se combinan: el impuesto recauda y el dinero se usa para financiar alternativas y ayudas.",
        "Al deliberar se pregunta por la eficacia (cuánto reduce emisiones), la equidad (quién paga más), la viabilidad (si se puede financiar) y la aceptación social (si la gente la apoya). Un porcentaje, como 10 %, debe traducirse a pesos: ¿cuánto más gasta una familia al mes? Así se ve el efecto real.",
        "Una propuesta sólida incluye medidas para proteger a los más afectados, plazos y un modo de evaluar. Quien disiente tiene derecho a objetar y a ser respondido con razones. Se busca un acuerdo basado en evidencia, no el triunfo de una postura.",
    ],
    vocab=[("incentivo", "estímulo que motiva a actuar de cierta forma"), ("desincentivar", "hacer menos atractiva una conducta"), ("subsidio", "ayuda económica para aliviar un costo"), ("viabilidad", "posibilidad de llevar a cabo una medida"), ("aceptación social", "grado de apoyo de la gente a una medida")],
    worked=[
        ("Traducir un porcentaje", "Si una familia de ejemplo gasta 30.000 pesos al mes y el costo sube 10 %, ¿cuánto más gasta?", ["10 % de 30.000 es una décima parte.", "30.000 entre 10."], "3.000 pesos"),
        ("Proteger a los afectados", "Un impuesto de ejemplo afecta más a quienes no tienen alternativa. ¿Qué medida compensa?", ["Dar una alternativa o ayuda.", "Por ejemplo, transporte público accesible."], "Alternativa de transporte o ayuda"),
    ],
    mistakes=[("Evaluar una política solo por su efecto en las emisiones.", "Puede ser injusta con quienes tienen menos opciones.", "Revisa eficacia y equidad."),
              ("No traducir un porcentaje a pesos.", "No se ve el efecto concreto en un hogar.", "Calcula el gasto adicional.")],
    T=[
        ('abc', '¿Qué es un incentivo?', 'Un estímulo que motiva a actuar de cierta forma', 'Una obligación impuesta por ley a toda la población', 'Una sanción por incumplir una norma de tránsito', 'Un impuesto cambia el precio y con ello motiva a actuar de otro modo.'),
        ('=', '{F} ¿Cuánto más gasta al mes una familia que gastaba 40.000 pesos en bencina?', '40000*10//100', 'Se calcula el 10 % de 40.000.', ' pesos'),
        ('=', '{F} ¿Cuántos pesos más gastan en total las 100 familias al mes?', '4000*100', 'Se multiplica el gasto adicional por 100 familias.', ' pesos'),
        ('abc', '{F} ¿Qué ventaja tiene la política 1?', 'Desincentiva el uso de combustibles', 'Da una alternativa de transporte a todos', 'No cuesta nada a las familias', 'Es el argumento a favor registrado en la ficha.'),
        ('abc', '{F} ¿Qué objeción tiene la política 1?', 'Afecta más a quienes viven lejos y no tienen alternativa', 'Cuesta fondos públicos que deben financiarse con el presupuesto', 'Aumenta el uso de combustibles en las ciudades', 'Es la objeción que registra la ficha.'),
        ('abc', '{F} ¿Qué ventaja tiene la política 2?', 'Da una alternativa a todos', 'Hace subir el precio de la bencina', 'No requiere financiamiento', 'Es el argumento a favor de la política 2.'),
        ('abc', '{F} ¿Qué objeción tiene la política 2?', 'Cuesta fondos públicos', 'Afecta más a quienes no tienen alternativa', 'Aumenta el precio de la bencina', 'Es la objeción registrada en la ficha.'),
        ('abc', '{F} ¿Qué propuesta combinada es más equitativa?', 'Un impuesto cuyos fondos financien transporte limpio y ayudas a quienes no tienen alternativa', 'Un impuesto sin ninguna ayuda ni alternativa para las familias afectadas', 'Un subsidio sin analizar cómo se financiaría en el presupuesto', 'Compensa a los más afectados y da una alternativa.'),
        ('abc', '{F} Alguien dice: «El impuesto reduce emisiones, así que es justo». ¿Qué corresponde?', 'Revisar cuánto afecta a quienes no tienen alternativa', 'Aceptarlo, porque lo importante es reducir emisiones', 'Rechazarlo, porque los impuestos nunca son justos', 'La eficacia no basta: también se evalúa la equidad.'),
        ('abc', '{F} ¿Qué indicador mostraría si la combinación funciona?', 'Emisiones del transporte y gasto de las familias más afectadas', 'Cantidad de carteles instalados para difundir la medida', 'Número de reuniones realizadas por las autoridades', 'Mide los dos objetivos: reducir emisiones y proteger a los más afectados.'),
        ('abc', '{F} ¿Qué es la aceptación social?', 'El grado de apoyo de la gente a una medida', 'El precio de la bencina antes del impuesto', 'El costo fiscal de aplicar una medida', 'Influye en que una medida pueda mantenerse.'),
        ('abc', '{F} ¿Qué dato falta para decidir sobre la política 2?', 'Cuánto costaría y cuántas personas la usarían', 'El precio de la bencina en otro país', 'Cuántas familias tienen auto de lujo', 'Define si es viable y qué tan eficaz puede ser.'),
        ('abc', '{F} ¿Qué decisión respeta a quienes disienten?', 'Registrar sus objeciones y responderlas con razones', 'Ignorarlas porque la decisión ya está tomada', 'Repetir la votación hasta que cambien de opinión', 'La deliberación incluye a la minoría con razones.'),
    ],
    ctx=('abc', 'Un liceo de ejemplo quiere reducir el uso de autos de los apoderados. ¿Qué medida combina incentivo y alternativa?', 'Cobrar estacionamiento y organizar transporte compartido', 'Prohibir el acceso de los apoderados al liceo', 'Pedir que nadie use auto, sin ninguna alternativa', 'Incentiva el cambio y ofrece una alternativa práctica.'),
    sc=[
        ('¿Qué significa desincentivar?', 'Hacer menos atractiva una conducta para que se practique menos', 'Un impuesto a los combustibles desincentiva su uso.'),
        ('abc', '¿Qué es la viabilidad de una medida?', 'La posibilidad de llevarla a cabo con los recursos disponibles', 'Un castigo para quien no cumple la medida acordada', 'El grado de apoyo que tiene la medida entre la gente', 'Se refiere a si puede hacerse realidad.'),
        ('En Educación Ciudadana: ¿Qué es un subsidio?', 'Una ayuda económica para aliviar un costo', 'El subsidio al transporte reduce lo que pagan las personas.'),
    ],
    op=("Con la {F} escribe una propuesta de siete líneas: política elegida o combinación, razón, objeción, cálculo del efecto en una familia, medida de protección, indicador y plazo de evaluación.",
        "Propongo un impuesto moderado con fondos para transporte público limpio. Razón: reduce emisiones y da alternativa. Objeción: afecta a quienes no tienen alternativa. Efecto: 4.000 pesos más al mes por familia. Protección: ayuda y transporte en sectores alejados. Indicador: emisiones y gasto. Evaluación: en un año.",
        ["traduce el porcentaje a pesos", "protege a afectados", "incluye indicador y plazo"], ["propuesta de siete líneas"], ["ignorar el efecto en las familias", "no fijar plazo"],
        "Pregunta quién debería evaluar los resultados."),
    reinforce="Explica por qué un impuesto puede ser injusto sin medidas de apoyo.",
    extend="Averigua qué opciones de transporte público hay cerca de tu casa.",
)

# ============================================================ OA 03, clase 5
F = ("Ficha 51 (diagnóstico de ejemplo en el liceo ficticio Alto Mar): el liceo consume 2.400 unidades de electricidad al mes. Estimaciones de ejemplo: iluminación 40 %, computadores 25 %, calefacción 20 %, otros 15 %. "
     "Recursos: 12 voluntarios, 4 semanas, apoyo de un docente y del encargado de mantención. Se propone un plan de ahorro de energía y reducción de residuos con metas medibles, sin riesgos físicos.")
build(
    O3, 5, F,
    use="Aprenderé a diseñar una acción escolar para reducir el impacto climático, con metas, medidas seguras, equidad y evaluación.",
    prior=["Sé qué es la huella de carbono.", "Sé diseñar una acción con indicador.", "Sé calcular porcentajes."],
    explain=[
        "Una acción escolar de mitigación parte de un diagnóstico: en qué se consume más. En el ejemplo, la iluminación representa el 40 % del consumo. Se fija una meta medible, como reducir 10 % el consumo total en un mes, se eligen medidas (apagar luces sin uso, aprovechar la luz natural, registrar los consumos) y se asignan roles.",
        "La acción debe ser segura y equitativa: sin manipular instalaciones eléctricas ni trabajar en alturas, con apoyo de un adulto responsable, y sin culpar a personas. Se define un indicador (consumo mensual) y un modo de comunicar los resultados. También se pide al encargado de mantención que revise los aspectos técnicos.",
        "Al final se evalúa: ¿se cumplió la meta?, ¿qué medidas funcionaron? Se reconocen los límites, como que una acción escolar es pequeña frente al problema global. Aun así, enseña hábitos, demuestra corresponsabilidad y puede inspirar decisiones colectivas.",
    ],
    vocab=[("meta medible", "objetivo que se puede verificar con un número"), ("consumo mensual", "cantidad de un recurso usada en un mes"), ("línea base", "dato inicial con el que se compara un resultado"), ("registro de consumo", "anotación periódica de cuánto se usa"), ("encargado de mantención", "persona responsable de las instalaciones del liceo")],
    worked=[
        ("Calcular una meta", "Un liceo de ejemplo consume 1.000 unidades al mes y quiere reducir 10 %. ¿Cuál es la meta de consumo?", ["10 % de 1.000 es 100.", "1.000 menos 100."], "900 unidades"),
        ("Medida segura", "¿Cuál es segura: «subir al techo a cambiar focos» o «apagar luces cuando nadie está»?", ["La primera implica riesgo de caída.", "La segunda es segura."], "Apagar luces cuando nadie está"),
    ],
    mistakes=[("Proponer tareas peligrosas, como tocar instalaciones eléctricas.", "Hay riesgo de accidentes.", "Elige medidas seguras y consulta al encargado."),
              ("No medir antes de actuar.", "No se puede saber si hubo mejora.", "Define una línea base.")],
    T=[
        ('abc', '¿Qué es una meta medible?', 'Un objetivo que se puede verificar con un número', 'Un deseo sobre el futuro que nadie puede comprobar', 'Una promesa de esforzarse más sin una cifra definida', 'Un número permite comprobar si se logró.'),
        ('=', '{F} ¿Cuántas unidades consume la iluminación?', '2400*40//100', 'Se calcula el 40 % de 2.400.', ' unidades'),
        ('=', '{F} ¿Cuántas unidades consumen los computadores?', '2400*25//100', 'Se calcula el 25 % de 2.400.', ' unidades'),
        ('=', '{F} Si el plan reduce 10 % el consumo total, ¿cuántas unidades ahorra?', '2400*10//100', 'Se calcula el 10 % de 2.400.', ' unidades'),
        ('=', '{F} ¿Cuál sería el consumo mensual si se cumple esa meta?', '2400-2400*10//100', 'Se resta el ahorro al consumo inicial.', ' unidades'),
        ('abc', '{F} ¿Cuál es una medida segura?', 'Apagar luces sin uso y aprovechar la luz natural', 'Cambiar enchufes dañados por cuenta propia', 'Subir a una escalera para sacar ampolletas', 'Las acciones escolares no deben manipular instalaciones eléctricas ni trabajar en alturas.'),
        ('abc', '{F} ¿Qué es la línea base?', 'El dato inicial con el que se compara el resultado', 'El resultado final de la acción al terminar el mes', 'La meta que se espera alcanzar al terminar el plan', 'Sin un dato inicial no se puede saber cuánto cambió el consumo.'),
        ('abc', '{F} ¿Quién revisa los aspectos técnicos?', 'El encargado de mantención', 'Cualquier voluntario con conocimientos', 'El centro de estudiantes', 'Es la persona responsable de las instalaciones.'),
        ('abc', '{F} ¿Qué indicador sirve para medir el resultado?', 'Consumo mensual de electricidad comparado con la línea base', 'Cantidad de afiches pegados en el liceo durante las semanas', 'Número de voluntarios inscritos en el equipo del plan', 'Mide el resultado de las medidas y no solo la actividad.'),
        ('abc', '{F} Un compañero dice: «Con esto salvamos el planeta». ¿Qué corresponde?', 'Reconocer que es una acción pequeña pero valiosa para aprender y dar el ejemplo', 'Aceptarlo, porque toda acción escolar resuelve el problema climático', 'Decir que no sirve, porque es demasiado pequeña para importar', 'Es honesto sobre los límites sin restar valor a la acción.'),
        ('abc', '{F} ¿Qué evita culpar a personas?', 'Comunicar los resultados del liceo en general', 'Publicar quién dejó luces encendidas', 'Comparar a los cursos con nombres propios', 'Respeta la dignidad de las personas y mantiene el foco en el objetivo común.'),
        ('abc', '{F} Si el consumo no baja, ¿qué corresponde?', 'Revisar qué medidas no funcionaron y ajustarlas', 'Abandonar la acción y no volver a intentar otra', 'Informar que se cumplió igual, aunque el consumo no bajó', 'Evaluar permite detectar qué falló y corregirlo en la próxima acción.'),
        ('abc', 'Un curso de ejemplo quiere reducir el uso de papel. ¿Qué meta es medible?', 'Bajar de 500 a 400 hojas al mes', 'Usar menos papel', 'Ser más conscientes del papel', 'Un objetivo con cantidades concretas permite comprobar si se cumplió.'),
    ],
    ctx=('=', 'Si una acción escolar ahorra 240 unidades al mes y cada unidad cuesta 300 pesos, ¿cuánto se ahorra al mes?', '240*300', 'Se multiplica el ahorro en unidades por el valor de cada una.', ' pesos'),
    sc=[
        ('¿Para qué sirve un registro de consumo?', 'Para anotar cuánto se usa y ver si cambia', 'Permite comparar con la línea base.'),
        ('abc', '¿Qué es el consumo mensual?', 'La cantidad de energía que se usa en un mes', 'El precio de una unidad de energía', 'El número de aparatos del liceo', 'Es el indicador que se compara con la línea base.'),
        ('¿Qué hace el encargado de mantención en esta acción?', 'Revisa los aspectos técnicos de las instalaciones', 'Revisar lo técnico con la persona responsable evita riesgos eléctricos para el grupo.'),
    ],
    op=("Con la {F} diseña el plan: meta medible, tres medidas seguras, roles para 12 voluntarios, plazo por semana, indicador, y una frase honesta sobre los límites de la acción.",
        "Meta: bajar de 2.400 a 2.160 unidades al mes. Medidas: apagar luces sin uso, aprovechar la luz natural, registrar consumos. Roles: 4 por medida. Semana 1 línea base, 2 y 3 medidas, 4 resultados. Indicador: consumo mensual. Límite: una acción escolar es pequeña frente al problema global, pero enseña hábitos.",
        ["meta medible", "medidas seguras", "límites honestos"], ["plan de ahorro"], ["medidas peligrosas", "no medir"],
        "Pregunta cómo involucrar a otros cursos."),
    reinforce="Calcula el 10 % de 3.000 y explica qué significa.",
    extend="Observa tu casa y anota dos hábitos de ahorro de energía posibles.",
)

# ============================================================ OA 03, clase 6
F = ("Ficha 52 (evaluación de ejemplo): el plan de ahorro de un liceo ficticio dio estos resultados en 3 meses. Consumo inicial 2.400 unidades al mes; mes 1: 2.300; mes 2: 2.200; mes 3: 2.250. "
     "Meta: 2.160. Costo del plan: 50.000 pesos (carteles y registro). Ahorro en la cuenta: 300 pesos por unidad ahorrada. Observaciones: algunos cursos redujeron más que otros; hubo un mes con más actividades.")
build(
    O3, 6, F,
    use="Aprenderé a evaluar los efectos y límites de una acción o política climática con datos, sin exagerar los logros ni ignorar sus costos.",
    prior=["Sé qué es una meta e indicador.", "Sé calcular diferencias y porcentajes.", "Sé leer una serie de datos."],
    explain=[
        "Evaluar una acción es comparar sus resultados con la meta y con la línea base, y calcular su costo-beneficio. En el ejemplo, el consumo bajó, pero no llegó a la meta. Se calcula cuánto se ahorró cada mes y el ahorro total, y se compara con el costo del plan. También se pregunta por efectos no previstos.",
        "Los datos tienen límites. Un mes con más actividades puede aumentar el consumo sin que el plan haya fallado. Una serie corta no permite concluir tendencias. Por eso se evita decir «el plan fracasó» o «el plan fue un éxito total»: se dice qué se logró, qué falta y qué datos habría que reunir.",
        "También se evalúa la justicia: ¿hubo cursos que se esforzaron más?, ¿se reconoció a todos?, ¿hubo personas que no podían participar? Y se piensa en la continuidad: ¿cómo se mantiene el hábito? La evaluación termina con recomendaciones concretas y una comunicación honesta.",
    ],
    vocab=[("costo-beneficio", "comparación entre lo que cuesta una medida y lo que se obtiene"), ("efecto no previsto", "consecuencia que no se había anticipado"), ("tendencia", "dirección en que cambia un dato en el tiempo"), ("continuidad", "capacidad de mantener una acción en el tiempo"), ("recomendación", "propuesta concreta para mejorar")],
    worked=[
        ("Calcular ahorro", "Un consumo de ejemplo baja de 1.000 a 920. ¿Cuánto es el ahorro?", ["Se resta 920 a 1.000.", "Ahorro de 80 unidades."], "80 unidades"),
        ("Costo-beneficio", "Un plan de ejemplo cuesta 10.000 pesos y ahorra 15.000. ¿Conviene?", ["El ahorro supera el costo.", "Hay beneficio neto."], "Sí; ahorra más de lo que cuesta"),
    ],
    mistakes=[("Concluir que el plan fracasó por un solo mes.", "Una serie corta no permite concluir.", "Reúne más meses y revisa causas."),
              ("Ignorar los costos del plan.", "El beneficio debe compararse con el costo.", "Calcula el costo-beneficio.")],
    T=[
        ('abc', '¿Qué significa evaluar el costo-beneficio de una acción?', 'Comparar lo que cuesta con lo que se obtiene', 'Sumar el ahorro de todos los meses sin considerar el costo', 'Contar cuántas personas participaron', 'Es una comparación entre costos y resultados.'),
        ('=', '{F} ¿Cuánto se ahorró en el mes 2 respecto del consumo inicial?', '2400-2200', 'Se resta el consumo del mes 2 al consumo inicial.', ' unidades'),
        ('=', '{F} ¿Cuánto se ahorró en total en los tres meses?', '(2400-2300)+(2400-2200)+(2400-2250)', 'Se suman los ahorros de cada mes.', ' unidades'),
        ('=', '{F} ¿Cuántas unidades faltaron en el mes 3 para llegar a la meta?', '2250-2160', 'Se resta la meta al consumo del mes 3.', ' unidades'),
        ('=', '{F} ¿Cuántos pesos ahorró el liceo con las unidades ahorradas en los tres meses?', '450*300', 'Se multiplica las unidades ahorradas por el valor de cada una.', ' pesos'),
        ('=', '{F} Si el ahorro total fue de 135.000 pesos, ¿cuál fue el beneficio neto después de pagar el costo del plan?', '135000-50000', 'Se resta el costo del plan al ahorro.', ' pesos'),
        ('abc', '{F} ¿Qué mes estuvo más cerca de la meta?', 'El mes 2, con 2.200 unidades', 'El mes 1, con 2.300 unidades', 'El mes 3, con 2.250 unidades', '2.200 es el consumo más cercano a la meta de 2.160.'),
        ('abc', '{F} ¿Qué dice el aumento del mes 3 sobre el plan?', 'Puede deberse a factores como más actividades, y hacen falta más datos', 'Que el plan fracasó, porque el consumo volvió a subir', 'Que los cursos dejaron de esforzarse después del segundo mes', 'Una variación puntual no permite concluir por sí sola.'),
        ('abc', '{F} ¿Qué conclusión es prudente?', 'El plan redujo el consumo, pero no llegó a la meta; conviene seguir midiendo', 'El plan fue un éxito total porque bajó el consumo en dos meses', 'El plan fracasó porque no alcanzó la meta de 2.160 unidades', 'Se ajusta a los datos sin exagerar ni minimizar.'),
        ('abc', '{F} ¿Qué recomendación es concreta?', 'Reconocer a los cursos que más redujeron y compartir sus prácticas', 'Mejorar todo lo que se pueda en las próximas semanas', 'Esforzarse más el próximo mes y pedir a todos que ahorren', 'Una recomendación concreta indica qué hacer y a quiénes involucra.'),
        ('abc', '{F} ¿Qué efecto no previsto podría revisarse?', 'Que algunos cursos hayan sentido presión o culpa por los resultados', 'Que el consumo bajó durante los primeros dos meses', 'Que se cumplió la meta de consumo en el mes 2', 'Un efecto no previsto es una consecuencia que no se había anticipado.'),
        ('abc', 'Una ciudad de ejemplo evalúa un programa de reciclaje con solo dos semanas de datos. ¿Qué advertencia corresponde?', 'Es una serie corta y no permite concluir tendencias', 'Ya se pueden afirmar efectos definitivos', 'Dos semanas bastan si el resultado fue bueno', 'Falta tiempo para ver si el cambio se mantiene.'),
        ('abc', '{F} Con un ahorro de 135.000 pesos y un costo de 50.000, ¿qué se puede decir?', 'En pesos, el plan ahorró más de lo que costó, aunque no alcanzó la meta', 'El plan costó más de lo que ahorró en los tres meses', 'El plan solo es valioso si alcanza la meta de consumo', 'Se compara el ahorro con el costo, además de la meta.'),
    ],
    ctx=('abc', '{F} Algunos cursos redujeron más que otros. ¿Qué conviene hacer en términos de justicia?', 'Reconocer el esfuerzo de todos los cursos', 'Publicar quién redujo menos', 'Ignorar las diferencias entre cursos', 'La evaluación también pregunta si se reconoció a todos.'),
    sc=[
        ('¿Qué es un efecto no previsto?', 'Una consecuencia que no se había anticipado', 'No se había anticipado y puede mejorar o empeorar la convivencia del grupo.'),
        ('¿Qué es la tendencia?', 'La dirección en que cambia un dato en el tiempo', 'Se observa en una serie de datos.'),
        ('abc', '¿Qué es la continuidad de una acción?', 'Cómo se mantiene el hábito después de terminar la acción', 'El número de veces que se repite una reunión', 'El costo de repetir la acción', 'Mira si el cambio dura más allá del plan.'),
    ],
    op=("Con la {F} escribe una evaluación de seis líneas: ahorro total, comparación con la meta, costo-beneficio, dos límites de los datos, un efecto no previsto posible y dos recomendaciones.",
        "Ahorro total: 450 unidades. No se alcanzó la meta (faltaron 90 en el mes 3). Costo-beneficio: ahorró 135.000 pesos y costó 50.000. Límites: serie corta; un mes con más actividades. Efecto no previsto: presión sobre algunos cursos. Recomendaciones: seguir midiendo y compartir buenas prácticas.",
        ["calcula bien", "reconoce límites", "propone recomendaciones"], ["evaluación de seis líneas"], ["concluir con un solo mes", "ignorar el costo"],
        "Pregunta qué dato nuevo reuniría."),
    reinforce="Explica por qué una serie corta limita las conclusiones.",
    extend="Anota un hábito de ahorro que podrías medir durante un mes.",
)

# ============================================================ OA 04, clase 1
F = ("Ficha 53 (casos de ejemplo): (1) Una empleada de comercio trabaja sin contrato escrito y le pagan sin liquidación. (2) Un grupo de trabajadores forma un sindicato para negociar mejores condiciones. "
     "(3) Un trabajador de una bodega tiene turnos de 12 horas todos los días, sin descanso semanal. (4) Un joven de 17 años quiere trabajar en vacaciones y su familia consulta a la Dirección del Trabajo qué protecciones existen.")
build(
    O4, 1, F,
    use="Aprenderé qué son los derechos laborales, cuáles son los principales (contrato, jornada, descansos, remuneración, seguridad, organización) y qué instituciones y organizaciones los resguardan.",
    prior=["Sé qué es un derecho y una norma.", "Sé que existen empleadores y trabajadores.", "Sé qué es una institución pública."],
    explain=[
        "Los derechos laborales son los derechos de las personas que trabajan. Incluyen un contrato por escrito, una remuneración justa y pagada a tiempo, una jornada máxima y descansos, vacaciones, seguridad e higiene en el trabajo, protección social (como salud y pensión), no discriminación y la libertad de organizarse en sindicatos y negociar colectivamente. Las cifras exactas las fija la ley y pueden cambiar.",
        "Hay instituciones que los resguardan: la inspección del trabajo, que fiscaliza que se cumplan las normas; los tribunales laborales, que resuelven conflictos; y organismos de seguridad social. Las organizaciones de trabajadores, como los sindicatos, representan a quienes trabajan y han contribuido históricamente a conquistar derechos mediante la organización y la negociación.",
        "Las personas menores de 18 años tienen protecciones especiales, por ejemplo, limitaciones en tipos de trabajo y horarios, y la consulta a una persona adulta responsable o a la institución competente antes de trabajar. Si un trabajo parece inseguro o abusivo, se avisa a una persona adulta de confianza y se consulta a la autoridad laboral.",
    ],
    vocab=[("derechos laborales", "derechos de las personas que trabajan, como contrato, descanso y seguridad"), ("contrato de trabajo", "acuerdo escrito entre trabajador y empleador sobre condiciones del trabajo"), ("sindicato", "organización de trabajadores que los representa y negocia por ellos"), ("negociación colectiva", "diálogo organizado entre trabajadores y empleador para acordar condiciones"), ("fiscalizar", "controlar que se cumplan las normas")],
    worked=[
        ("Identificar un derecho", "Una trabajadora de ejemplo recibe su sueldo con atraso de dos meses. ¿Qué derecho se afecta?", ["No se paga a tiempo.", "Es la remuneración."], "Derecho a la remuneración"),
        ("Instancia adecuada", "Un trabajador de ejemplo quiere denunciar que no se cumplen normas de seguridad. ¿A quién acude?", ["Alguien que fiscaliza.", "La inspección del trabajo."], "Inspección del trabajo"),
    ],
    mistakes=[("Pensar que sin contrato escrito no hay derechos.", "Los derechos laborales existen igual.", "Consulta a la autoridad laboral."),
              ("Aceptar un trabajo inseguro para no perderlo.", "Se arriesga la salud.", "Avisa a un adulto de confianza y consulta a la autoridad.")],
    T=[
        ('abc', '¿Qué incluyen los derechos laborales?', 'Contrato escrito, remuneración a tiempo, jornada máxima, descansos, seguridad y libertad sindical', 'Solo el pago de un sueldo mínimo, sin otros derechos', 'Solo el derecho a formar sindicatos y negociar colectivamente', 'Son varios derechos que protegen a quienes trabajan, no uno solo.'),
        ('abc', '{F} ¿Qué derecho se afecta en el caso 1?', 'El contrato por escrito y la remuneración con respaldo', 'La libertad sindical de organizarse con otros trabajadores', 'El descanso semanal después de una jornada de trabajo', 'No tiene contrato escrito y le pagan sin liquidación.'),
        ('abc', '{F} ¿Qué derecho ejerce el grupo del caso 2?', 'La libertad de organizarse en sindicatos y negociar colectivamente en el trabajo', 'El derecho a vacaciones pagadas durante el año', 'El derecho a un seguro de salud para la familia', 'Se organizan para negociar mejores condiciones.'),
        ('abc', '{F} ¿Qué derechos se afectan en el caso 3?', 'La jornada máxima y el descanso semanal de la persona', 'El contrato por escrito entre trabajador y empleador', 'La negociación colectiva con el empleador', 'Trabaja turnos de 12 horas todos los días, sin descanso semanal.'),
        ('=', '{F} Si el trabajador del caso 3 trabaja 12 horas los 7 días de la semana, ¿cuántas horas trabaja a la semana?', '12*7', 'Se multiplica las horas diarias por los días.', ' horas'),
        ('abc', '¿Qué institución fiscaliza que se cumplan las normas laborales?', 'La inspección del trabajo', 'Los tribunales laborales', 'El sindicato', 'Fiscalizar es controlar el cumplimiento de las normas.'),
        ('abc', '¿Quién resuelve un conflicto laboral que no se pudo acordar?', 'Los tribunales laborales', 'El sindicato, mediante una votación', 'El empleador, al interpretar el contrato', 'Los tribunales laborales resuelven los conflictos con base en la ley.'),
        ('abc', '{F} ¿Qué es la negociación colectiva?', 'El diálogo organizado entre trabajadores y empleador para acordar condiciones', 'Un acuerdo entre dos empleadores sobre los precios de sus productos', 'Una votación de los trabajadores sin la participación del empleador', 'Incluye a ambas partes de la relación laboral.'),
        ('abc', '{F} Un amigo dice: «Sin contrato no tengo ningún derecho». ¿Qué corresponde?', 'Consultar a la autoridad laboral, pues los derechos existen aunque falte el papel', 'Aceptarlo y esperar a que lo contraten por escrito en el futuro', 'Exigir de inmediato el pago de cualquier cantidad que pida', 'Los derechos laborales no dependen solo del contrato escrito.'),
        ('abc', '{F} ¿Qué debe hacer la familia del joven del caso 4?', 'Consultar a la institución competente por las protecciones para menores antes de trabajar', 'Ignorar las reglas porque se trata de un trabajo de vacaciones', 'Pedir que el empleador decida qué protecciones se aplicarán', 'Las personas menores de 18 años tienen protecciones especiales.'),
        ('abc', '{F} ¿Qué hace un trabajador si una orden le parece insegura?', 'Avisar a una persona adulta de confianza y consultar a la autoridad laboral', 'Cumplir en silencio la orden para no perder el trabajo', 'Discutir con el empleador hasta convencerlo de cambiarla', 'Se protege su salud y se usa la instancia competente.'),
        ('abc', '{F} ¿Por qué se dice que los sindicatos han contribuido a conquistar derechos?', 'Porque, al organizarse, los trabajadores pudieron negociar y exigir mejores condiciones', 'Porque obligaron a todos los trabajadores a afiliarse a un sindicato', 'Porque reemplazaron a las instituciones del Estado en la fiscalización', 'La organización y la negociación fortalecen a quienes trabajan.'),
        ('abc', 'Una trabajadora de ejemplo recibe una oferta de trabajo sin contrato. ¿Cuál es el mejor paso?', 'Pedir el contrato por escrito y consultar a la autoridad laboral si se niega', 'Aceptar sin preguntar para asegurar el empleo cuanto antes', 'Pedir que el acuerdo sea solo de palabra para evitar trámites', 'Contar con contrato escrito es un derecho.'),
    ],
    ctx=('abc', 'Un empleador dice que las vacaciones son un favor. ¿Qué responde la clase?', 'Que las vacaciones son un derecho de quien trabaja', 'Que dependen de la buena voluntad del empleador', 'Que solo corresponden a quienes tienen sindicato', 'Las vacaciones están entre los derechos laborales.'),
    sc=[
        ('¿Qué es un contrato de trabajo?', 'Un acuerdo que fija las condiciones de un trabajo y que debe constar por escrito', 'Es el documento base de los derechos laborales.'),
        ('abc', '¿Qué es un sindicato?', 'Una organización de trabajadores', 'Una empresa que contrata personas', 'Un tribunal que resuelve conflictos', 'Representa a los trabajadores y negocia en su nombre.'),
        ('¿Qué hace la inspección del trabajo?', 'Fiscaliza que se cumplan las normas laborales', 'Controla el cumplimiento, por ejemplo, de la jornada y el descanso.'),
    ],
    op=("Con la {F} haz una tabla con los cuatro casos: derecho en juego, instancia a la que acudir y una acción pacífica. Incluye una frase sobre a quién avisarías (una persona adulta de confianza).",
        "Caso 1: contrato y liquidación; inspección del trabajo; solicitar el contrato por escrito. Caso 2: libertad sindical; negociación colectiva; presentar sus demandas. Caso 3: descanso; inspección del trabajo; denunciar los turnos. Caso 4: protecciones de menores; institución competente; consultar antes de trabajar. Aviso: a una persona adulta de confianza en la familia.",
        ["relaciona derecho e instancia", "acciones pacíficas", "incluye el aviso a un adulto"], ["tabla de cuatro casos"], ["acudir a la violencia", "aceptar el abuso"],
        "Pregunta qué derecho es más importante para una persona joven."),
    reinforce="Explica con tus palabras tres derechos laborales y para qué sirven.",
    extend="Averigua con una persona adulta cómo se recibe un contrato de trabajo.",
)

# ============================================================ OA 04, clase 2
F = ("Ficha 54 (caso de ejemplo): Mateo, repartidor de una aplicación ficticia, trabaja 10 horas al día, 6 días a la semana, sin contrato, y la aplicación le paga por pedido: 1.500 pesos por entrega, con un promedio de 6 entregas por hora. "
     "No recibe seguro por accidentes. La empresa dice que él es «independiente». Fuentes: el registro de entregas de Mateo, los términos de la aplicación y una nota de la inspección del trabajo (de ejemplo) que dice que la relación debe analizarse caso a caso.")
build(
    O4, 2, F,
    use="Aprenderé a investigar un caso de trabajo en la economía digital, a calcular ingresos y a ver qué derechos y vacíos hay.",
    prior=["Sé los derechos laborales básicos.", "Sé calcular productos y totales.", "Sé comparar fuentes."],
    explain=[
        "Una tendencia global es el trabajo mediante plataformas digitales, donde una aplicación conecta a clientes con personas que prestan un servicio. Muchas veces se les llama «independientes», pero pueden depender de la aplicación para recibir pedidos y tarifas. La ley analiza cada caso para saber si hay subordinación, es decir, si la persona recibe órdenes y control de una empresa.",
        "Para investigarlo se calculan las horas, los ingresos y los gastos, y se revisan los términos de la aplicación y los registros. También se pregunta qué protecciones faltan: seguro de accidentes, cotización para salud y pensión, descanso. Cada fuente tiene un propósito: los términos son de la empresa; el registro es de la persona; la institución analiza.",
        "Se evita concluir sin pruebas. «La empresa abusa» o «el trabajador exagera» son afirmaciones que requieren datos. Una conclusión prudente dice qué muestran los datos, qué derechos están en discusión y quién puede resolver. Ante riesgos para la persona, se recomienda consultar a la institución competente y avisar a un adulto de confianza.",
    ],
    vocab=[("plataforma digital", "aplicación que conecta a clientes con quienes prestan un servicio"), ("subordinación", "relación en que una persona recibe órdenes y control de otra"), ("cotizar", "aportar dinero a la seguridad social para salud y pensión"), ("tarifa por pedido", "pago por cada entrega realizada"), ("trabajo independiente", "trabajo en que la persona no está subordinada a un empleador")],
    worked=[
        ("Calcular ingreso", "Un trabajador de ejemplo hace 5 entregas por hora a 1.000 pesos cada una durante 4 horas. ¿Cuánto gana?", ["Entregas: 5 por 4 horas son 20.", "20 por 1.000."], "20.000 pesos"),
        ("Hecho y valoración", "«Mateo trabaja 10 horas al día» y «la empresa es abusiva». ¿Cuál es hecho?", ["La primera se registra.", "La segunda es valoración."], "La primera"),
    ],
    mistakes=[("Concluir que hay abuso solo con el discurso de una parte.", "Faltan pruebas de ambos lados.", "Revisa registros y términos."),
              ("Ignorar los gastos del trabajador.", "El ingreso neto es menor.", "Descuenta los costos que asume.")],
    T=[
        ('abc', '¿Qué es la subordinación en una relación de trabajo?', 'Una relación en que una persona recibe órdenes y control de una empresa', 'Una relación en que la persona decide libremente cuándo y cómo trabaja', 'Un contrato que fija un sueldo mensual', 'La ley la analiza caso a caso para saber si hay un vínculo laboral.'),
        ('=', '{F} ¿Cuántas entregas hace Mateo en un día de 10 horas?', '6*10', 'Se multiplican las entregas por hora por las horas del día.', ' entregas'),
        ('=', '{F} ¿Cuánto gana Mateo en un día, antes de gastos?', '6*10*1500', 'Se multiplican las entregas del día por el pago de cada una.', ' pesos'),
        ('=', '{F} ¿Cuántas horas trabaja Mateo a la semana?', '10*6', 'Se multiplican las horas diarias por los días.', ' horas'),
        ('=', '{F} ¿Cuánto gana Mateo a la semana, antes de gastos?', '6*10*1500*6', 'Se calcula el ingreso diario y se multiplica por los días.', ' pesos'),
        ('abc', '{F} ¿Qué protección menciona la ficha que Mateo no recibe?', 'Seguro por accidentes', 'Pago por pedido', 'Acceso a la aplicación', 'La ficha dice que no tiene seguro por accidentes.'),
        ('abc', '{F} ¿Qué dice la empresa sobre Mateo?', 'Que es independiente', 'Que es empleado con contrato', 'Que es socio de la aplicación', 'La empresa lo califica de «independiente».'),
        ('abc', '{F} ¿Qué dice la nota de la inspección del trabajo?', 'Que la relación debe analizarse caso a caso', 'Que la empresa debe contratarlo como empleado', 'Que Mateo es independiente en todos los casos', 'La nota no decide, indica que se debe analizar cada caso.'),
        ('abc', '{F} Alguien dice: «Mateo gana mucho, no tiene de qué quejarse». ¿Qué corresponde?', 'Considerar también las horas, los gastos y la falta de protección', 'Aceptarlo, porque 90.000 diarios es un buen ingreso', 'Rechazarlo, porque los repartidores nunca ganan bien', 'El ingreso bruto no refleja los gastos ni las condiciones de trabajo.'),
        ('abc', '{F} ¿Qué dato falta para evaluar su situación?', 'Los gastos que asume Mateo, como bencina o mantención', 'El nombre de la aplicación y la fecha en que se creó', 'El número de clientes que tiene la empresa en la ciudad', 'Con los gastos se puede calcular cuánto gana realmente después de costos.'),
        ('abc', '{F} Una aplicación fija la tarifa, asigna los pedidos y quita puntos si el repartidor rechaza. ¿Qué elemento sugiere subordinación?', 'La empresa controla la tarifa y la asignación de pedidos', 'El repartidor usa bicicleta propia para hacer las entregas', 'El repartidor elige su ruta entre el local y el cliente', 'Hay órdenes y control de la empresa.'),
        ('abc', '{F} ¿Qué fuente representa el punto de vista de la empresa?', 'Los términos de la aplicación', 'El registro de entregas de Mateo', 'La nota de la inspección del trabajo', 'Los términos son un documento elaborado por la empresa.'),
        ('abc', '{F} ¿Qué conclusión es prudente?', 'Los datos muestran largas jornadas y falta de seguro; si hay subordinación, lo analiza la institución', 'Mateo es un trabajador dependiente, sin ninguna duda al respecto', 'Mateo es independiente porque así lo dice la empresa', 'Se limita a los datos y a quién puede resolver.'),
    ],
    ctx=('abc', 'Un repartidor sufre un accidente sin seguro. ¿Qué se recomienda?', 'Avisar a una persona adulta de confianza y consultar a la institución competente', 'Esperar a que la empresa se comunique con él por su cuenta', 'Ocultarlo para no perder pedidos ni afectar su puntaje', 'Se busca ayuda y se consulta a quien puede resolver.'),
    sc=[
        ('¿Qué es una plataforma digital?', 'Una aplicación que conecta a clientes con quienes prestan un servicio', 'Muchas veces fija las tarifas y asigna los pedidos.'),
        ('abc', '¿Qué es cotizar?', 'Aportar dinero a la seguridad social, para salud y pensión', 'Cobrar una deuda a un cliente de la aplicación', 'Pagar la tarifa de un servicio a una empresa', 'Las cotizaciones financian la protección social en salud y pensión.'),
        ('¿Qué es una tarifa por pedido?', 'El pago fijo que recibe quien presta el servicio por cada entrega', 'Hace que el ingreso dependa del número de pedidos.'),
    ],
    op=("Con la {F} escribe un informe de cinco puntos: horas semanales, ingreso semanal, protecciones que faltan, dos datos que pedirías y una conclusión prudente que no culpe a nadie. Agrega a quién consultaría un joven en esa situación.",
        "Horas semanales: 60. Ingreso semanal: 540.000 pesos. Faltan seguro de accidentes y cotizaciones. Datos: gastos y reglas de la aplicación. Conclusión: los datos sugieren una jornada larga y sin protección; la relación debe analizarse. Consulta: la inspección del trabajo y una persona adulta de confianza.",
        ["calcula bien", "no culpa", "indica a quién consultar"], ["informe de cinco puntos"], ["tomar partido sin datos", "olvidar los gastos"],
        "Pregunta qué protección le parece más urgente."),
    reinforce="Calcula las horas semanales de una persona que trabaja 8 horas durante 5 días.",
    extend="Averigua qué servicios de tu barrio funcionan mediante aplicaciones y quiénes los prestan.",
)

# ============================================================ OA 04, clase 3
F = ("Ficha 55 (perspectivas de ejemplo sobre flexibilidad laboral en una empresa ficticia). "
     "Perspectiva 1 (empleador): «Necesito flexibilidad de horarios para responder a la demanda y mantener los empleos». "
     "Perspectiva 2 (sindicato): «La flexibilidad no debe significar inestabilidad; pedimos horarios conocidos con anticipación y descanso asegurado». "
     "Perspectiva 3 (joven trabajadora): «Quiero compatibilizar estudio y trabajo; me sirve un horario flexible si no pierdo derechos». "
     "Dato de ejemplo: la empresa tiene 50 trabajadores; 30 prefieren horarios fijos, 20 prefieren flexibles.")
build(
    O4, 3, F,
    use="Aprenderé a contrastar perspectivas sobre tendencias laborales, entender cómo los movimientos sociales han aportado a los derechos y evaluar equilibrios entre flexibilidad y protección.",
    prior=["Sé los derechos laborales básicos.", "Sé comparar perspectivas.", "Sé leer proporciones."],
    explain=[
        "Las tendencias laborales actuales incluyen el teletrabajo, los horarios flexibles, el trabajo en plataformas, la automatización y la informalidad (trabajo sin contrato ni protección). Cada una ofrece oportunidades y riesgos. La flexibilidad puede ayudar a combinar estudio, trabajo y cuidado, pero también puede traducirse en inestabilidad.",
        "Los derechos laborales actuales son resultado de procesos históricos: movimientos de trabajadores se organizaron, negociaron, hicieron huelgas pacíficas y demandaron leyes que fijaran jornadas, descansos y seguridad. Los sindicatos y otras organizaciones siguen aportando al representar a quienes trabajan. Los mecanismos institucionales han evolucionado con la ley, la inspección y los tribunales.",
        "Contrastar perspectivas significa ver qué valor defiende cada una (productividad y empleo, estabilidad y descanso, autonomía) y cómo se concilian. Un dato como «30 contra 20» muestra preferencias, pero la decisión debe cuidar a quienes están en minoría. Muchas veces se acuerda flexibilidad con garantías: horarios avisados con anticipación, descansos, y no pérdida de derechos.",
    ],
    vocab=[("flexibilidad laboral", "posibilidad de adaptar horarios o condiciones de trabajo"), ("informalidad", "trabajo sin contrato ni protección social"), ("teletrabajo", "trabajo realizado a distancia, fuera de la oficina"), ("huelga", "suspensión colectiva y pacífica del trabajo para exigir mejoras"), ("garantía", "protección que asegura el cumplimiento de un derecho")],
    worked=[
        ("Preferencias", "En una empresa de ejemplo con 40 personas, 25 prefieren horario fijo. ¿Cuántas prefieren otro?", ["Se resta 25 a 40.", "Son 15."], "15 personas"),
        ("Conciliar", "El empleador de ejemplo quiere flexibilidad y el sindicato estabilidad. ¿Qué acuerdo combina?", ["Flexibilidad con aviso anticipado.", "Y descanso asegurado."], "Flexibilidad con aviso y descanso asegurado"),
    ],
    mistakes=[("Pensar que flexibilidad siempre es mala o siempre es buena.", "Depende de las garantías.", "Pregunta qué protección se mantiene."),
              ("Ignorar la preferencia de la minoría.", "Los derechos no dependen de votar.", "Busca soluciones que incluyan a todos.")],
    T=[
        ('abc', '¿Qué es la flexibilidad laboral?', 'La posibilidad de adaptar horarios o condiciones de trabajo', 'La pérdida de estabilidad y de derechos de las personas', 'La obligación de trabajar sin descanso cuando la empresa lo pide', 'Puede ayudar a combinar estudio y trabajo, pero puede traducirse en inestabilidad.'),
        ('=', '{F} ¿Qué porcentaje de los 50 trabajadores prefiere horarios fijos?', '30*100//50', 'Se compara la parte con el total.', ' %'),
        ('abc', '{F} ¿Qué valor defiende el empleador?', 'Productividad y empleo mediante flexibilidad de horarios', 'Descanso asegurado y estabilidad en los horarios de trabajo', 'Compatibilizar estudio y trabajo sin perder derechos', 'Pide flexibilidad para responder a la demanda.'),
        ('abc', '{F} ¿Qué valor defiende el sindicato?', 'Estabilidad y descanso asegurado', 'Flexibilidad total de horarios', 'Reducción de costos de la empresa', 'El sindicato pide estabilidad, es decir, horarios conocidos y descanso asegurado.'),
        ('abc', '{F} ¿Qué valor defiende la joven trabajadora?', 'Compatibilizar estudio y trabajo sin perder derechos', 'Trabajar el máximo de horas posible', 'Tener un horario fijo en todos los casos', 'Su postura pide flexibilidad siempre que no se pierdan derechos.'),
        ('abc', '{F} ¿Qué acuerdo combina las tres perspectivas?', 'Horarios flexibles con aviso anticipado, descanso asegurado y sin pérdida de derechos', 'Horario fijo para todos sin excepción, aunque algunos prefieran otro', 'Flexibilidad total sin garantías ni descansos asegurados', 'Combina lo que valora cada perspectiva sin sacrificar los derechos básicos.'),
        ('abc', '{F} ¿Qué es una garantía?', 'Una protección que asegura el cumplimiento de un derecho', 'Un permiso del empleador que puede retirarse en cualquier momento', 'Un acuerdo verbal sin registro entre las partes', 'Respalda el derecho para que no se pierda.'),
        ('abc', '{F} Alguien dice: «Como 30 prefieren fijo, que todos tengan fijo». ¿Qué corresponde?', 'Considerar también a los 20 que prefieren flexible y buscar un acuerdo con garantías', 'Aceptarlo, porque la mayoría decide y la minoría debe adaptarse', 'Rechazarlo, porque la opinión de la mayoría no importa', 'La decisión debe cuidar a quienes están en minoría.'),
        ('abc', '{F} ¿Qué rol han tenido los movimientos de trabajadores?', 'Se organizaron, negociaron y demandaron leyes para conquistar derechos', 'Pidieron eliminar la jornada máxima y los descansos', 'Reemplazaron a las instituciones del Estado en la fiscalización', 'Los derechos actuales son resultado de procesos históricos de organización.'),
        ('abc', '{F} ¿Qué riesgo tiene la informalidad?', 'Trabajar sin contrato ni protección social', 'Tener un horario flexible acordado con garantías', 'Pertenecer a un sindicato que negocia mejores condiciones', 'Es trabajo sin contrato ni protección.'),
        ('abc', '{F} ¿Qué dato falta para concretar el acuerdo?', 'Cuántas horas semanales y qué descansos garantizará la empresa', 'Cuántos trabajadores piensan cambiar de empresa en el año', 'El color del uniforme y el nombre del dueño', 'Sin cifras concretas las garantías del acuerdo quedan en una promesa vaga.'),
        ('abc', '{F} Un dato como «30 contra 20», ¿qué muestra?', 'Preferencias, pero la decisión debe cuidar a quienes están en minoría', 'La decisión correcta, que debe aplicarse a todos sin excepción', 'Que la minoría debe adaptarse sin condiciones a lo que decida la mayoría', 'Muestra cómo se distribuyen las preferencias, no qué es justo.'),
        ('abc', 'Una trabajadora de ejemplo hace teletrabajo y trabaja hasta tarde porque no hay horario definido. ¿Qué garantía falta?', 'Un horario definido y un derecho a desconectarse fuera de él', 'Más tareas para el fin de semana, sin pago adicional', 'Un contrato verbal que fije el horario de trabajo', 'Un horario definido y la desconexión protegen el descanso de la persona.'),
    ],
    ctx=('abc', 'Un trabajador joven acepta un horario flexible a cambio de perder el descanso semanal. ¿Qué principio se afecta?', 'La flexibilidad no puede significar pérdida de derechos', 'El descanso semanal es opcional si la persona lo acepta', 'Los acuerdos individuales siempre son válidos sin importar su contenido', 'La flexibilidad debe ir acompañada de garantías.'),
    sc=[
        ('En Educación Ciudadana: ¿Qué es el teletrabajo?', 'Trabajar a distancia, fuera del lugar físico de la empresa', 'Es una de las tendencias laborales actuales.'),
        ('En Educación Ciudadana: ¿Qué es la automatización?', 'El uso de máquinas o programas para hacer tareas que antes hacían personas', 'Es otra tendencia laboral con oportunidades y riesgos.'),
        ('En Educación Ciudadana: ¿Qué es una huelga?', 'La suspensión colectiva y pacífica del trabajo para exigir mejoras', 'Es una forma de presión pacífica.'),
    ],
    op=("Con la {F} haz una tabla con las tres perspectivas: valor, riesgo y garantía que pediría. Escribe luego un acuerdo de cuatro líneas con aviso anticipado, descansos, derechos y una revisión.",
        "Empleador: productividad; riesgo, perder demanda; garantía, aviso de turnos. Sindicato: estabilidad; riesgo, inestabilidad; garantía, descanso. Joven: compatibilizar; riesgo, perder derechos; garantía, horarios conocidos. Acuerdo: turnos avisados con una semana, dos días de descanso, mismos derechos, revisión en tres meses.",
        ["identifica valores", "propone garantías", "incluye revisión"], ["tabla", "acuerdo de cuatro líneas"], ["ignorar a la minoría", "no fijar garantías"],
        "Pregunta cómo se enterarían de que se cumple."),
    reinforce="Explica una ventaja y un riesgo de la flexibilidad laboral.",
    extend="Entrevista a una persona adulta sobre cómo cambió el trabajo en su vida, y anota una idea.",
)

# ============================================================ OA 04, clase 4
F = ("Ficha 56 (tema de deliberación de ejemplo): un país ficticio debate cómo proteger a las personas que trabajan por plataformas digitales. "
     "Propuesta A: reconocerlas como trabajadoras dependientes con todos los derechos. Propuesta B: crear una categoría especial con seguro de accidentes, cotizaciones y descansos, pero con libertad de horario. "
     "Argumento a favor de A: máxima protección. Objeción a A: algunas plataformas podrían reducir pedidos. Argumento a favor de B: combina flexibilidad y protección. Objeción a B: puede quedar menos protegida. "
     "Dato de ejemplo: de 100 repartidores consultados, 55 prefieren libertad de horario y 45 prefieren contrato fijo.")
build(
    O4, 4, F,
    use="Aprenderé a deliberar sobre cómo fortalecer los derechos laborales ante nuevas formas de trabajo, con razones, evidencia y propuestas que cuiden a las personas.",
    prior=["Sé las tendencias laborales.", "Sé estructurar un argumento.", "Sé leer encuestas."],
    explain=[
        "Regular una nueva forma de trabajo es una decisión pública que debe proteger derechos sin ignorar la realidad de quienes trabajan. Se examinan los efectos de cada propuesta en la protección, la flexibilidad, el empleo y el costo. Una propuesta puede ser muy protectora y a la vez provocar menos oportunidades si las empresas reducen pedidos.",
        "Un buen argumento usa evidencia: la encuesta muestra preferencias, pero no dice qué pasaría con el empleo ni qué beneficios exactos tendría cada opción. Se pregunta por los datos que faltan, como cuántos repartidores quedarían sin trabajo. Se escucha también a organizaciones de trabajadores, empresas y autoridades.",
        "Una propuesta sólida puede combinar medidas: protecciones mínimas para todos, cotizaciones, seguro por accidentes, derecho a descanso, transparencia de las reglas de la aplicación y un mecanismo de revisión. Se define un plazo, se evalúa con indicadores y se corrige. Quien disiente tiene derecho a objetar y a ser respondido.",
    ],
    vocab=[("regulación", "conjunto de normas que ordenan una actividad"), ("protección mínima", "conjunto básico de derechos que debe tener toda persona que trabaja"), ("transparencia algorítmica", "que se conozcan las reglas con que una aplicación asigna pedidos y pagos"), ("mecanismo de revisión", "forma de evaluar y ajustar una norma"), ("categoría especial", "forma particular de trabajo con reglas propias")],
    worked=[
        ("Leer una encuesta", "En una consulta de ejemplo, 60 de 100 prefieren A. ¿Cuántos prefieren otra opción?", ["Se resta 60 a 100.", "Son 40."], "40 personas"),
        ("Proteger sin eliminar la flexibilidad", "¿Qué medida protege sin quitar libertad de horario?", ["Seguro de accidentes y cotizaciones.", "No obligan a un horario fijo."], "Seguro y cotizaciones"),
    ],
    mistakes=[("Elegir la propuesta más protectora sin ver sus efectos en el empleo.", "Puede reducir oportunidades.", "Pide datos y diseña salvaguardas."),
              ("Decidir solo por la mayoría de la encuesta.", "No considera a la minoría ni los efectos.", "Usa la encuesta como un dato.")],
    T=[
        ('abc', '¿Qué es una regulación?', 'Un conjunto de normas que ordenan una actividad', 'Una prohibición total de una actividad', 'Un acuerdo privado entre empresas', 'Regular es fijar reglas para proteger derechos sin impedir la actividad.'),
        ('=', '{F} Si se consultara a 400 repartidores con la misma proporción, ¿cuántos preferirían libertad de horario?', '400*55//100', 'Se aplica la proporción de 55 de cada 100 al nuevo total.', ' repartidores'),
        ('abc', '{F} ¿Qué ventaja tiene la propuesta A?', 'Máxima protección para quienes trabajan', 'Mayor libertad de horario', 'Menor costo para las plataformas', 'Es el argumento a favor registrado en la ficha.'),
        ('abc', '{F} ¿Qué objeción tiene la propuesta A?', 'Algunas plataformas podrían reducir los pedidos', 'Daría menos derechos a los repartidores', 'Impediría el uso de aplicaciones', 'Es la objeción que registra la ficha.'),
        ('abc', '{F} ¿Qué ventaja tiene la propuesta B?', 'Combina flexibilidad con protecciones', 'Garantiza todos los derechos de un contrato', 'Elimina las cotizaciones', 'Es el argumento a favor de la categoría especial.'),
        ('abc', '{F} ¿Qué objeción tiene la propuesta B?', 'Puede quedar menos protegida que un contrato', 'Es demasiado costosa para los repartidores', 'Elimina la libertad de horario', 'Es la objeción registrada en la ficha.'),
        ('abc', '{F} ¿Qué medida reduce el riesgo de la propuesta B?', 'Fijar protecciones mínimas obligatorias y revisarlas con un mecanismo de revisión', 'Dejar las protecciones a voluntad de cada plataforma digital', 'Eliminar la categoría especial y volver a la situación anterior', 'Cuida a las personas y permite corregir si algo no funciona.'),
        ('abc', '{F} Un participante dice: «55 prefieren libertad, así que no hay que proteger». ¿Qué corresponde?', 'Recordar que la libertad de horario y la protección pueden combinarse', 'Aceptarlo, porque la mayoría prefiere libertad y no necesita protección', 'Rechazarlo, porque nadie prefiere libertad de horario', 'Son compatibles, como muestra la propuesta B.'),
        ('abc', '{F} ¿Qué dato falta para decidir mejor?', 'Cuántos empleos podrían perderse con cada propuesta', 'Cuántas aplicaciones hay en otro país de la región', 'El logo de la aplicación y los colores de la marca', 'Permite evaluar los efectos en el empleo.'),
        ('abc', '{F} ¿Qué es la transparencia algorítmica?', 'Que se conozcan las reglas con que la aplicación asigna pedidos y pagos', 'Que la aplicación publique el código completo de su programa', 'Que nadie sepa cómo se calculan las tarifas', 'Permite que las personas y las instituciones fiscalicen las reglas.'),
        ('abc', '{F} ¿Qué indicador mostraría si la propuesta funciona?', 'Repartidores con seguro y cotización, y empleos mantenidos', 'Cantidad de discursos de autoridades sobre el tema', 'Descargas de la aplicación durante el primer mes', 'Mide a la vez la protección lograda y el empleo que se mantiene.'),
        ('abc', '{F} ¿Qué haces si un repartidor joven sufre un accidente sin seguro?', 'Avisar a una persona adulta y consultar a la institución competente', 'Esperar a que la plataforma responda por su cuenta', 'No decir nada para no perder el trabajo en la aplicación', 'Se busca la ayuda de quien puede proteger y orientar a la persona.'),
        ('abc', 'Una aplicación de ejemplo cambia sus reglas de pago sin avisar. ¿Qué medida de protección corresponde?', 'Transparencia y aviso previo de los cambios', 'Cambios inmediatos para ajustarse al mercado', 'Cambios comunicados solo a quienes reclamen', 'Permite que las personas decidan informadas.'),
    ],
    ctx=('abc', 'Una autoridad propone exigir seguro de accidentes a las plataformas, con revisión anual. ¿Qué elementos incluye?', 'Una protección mínima y un mecanismo de revisión', 'Una categoría especial sin protecciones', 'La prohibición de las plataformas', 'El seguro es una protección mínima y la revisión permite ajustarla.'),
    sc=[
        ('¿Qué es una categoría especial?', 'Una forma distinta de trabajo con reglas propias entre dependiente e independiente', 'La propuesta B la plantea para plataformas digitales.'),
        ('abc', '¿Qué es una protección mínima?', 'Un conjunto básico de derechos para toda persona que trabaja', 'Un premio para quienes cumplen metas de entregas', 'El máximo de horas que se puede trabajar por día', 'Es el piso de derechos que no puede faltar.'),
        ('¿Qué es un mecanismo de revisión?', 'Una forma de evaluar y ajustar una norma', 'Permite corregir la regulación con evidencia.'),
    ],
    op=("Con la {F} escribe una propuesta de siete líneas: tu postura o combinación, una razón con el dato, la objeción, una protección mínima, una medida de transparencia, un indicador y un plazo de revisión.",
        "Propongo una categoría especial con protecciones mínimas. Razón: 55 de 100 valoran la libertad de horario. Objeción: puede quedar menos protegida. Protecciones: seguro, cotizaciones y descansos. Transparencia: reglas de asignación públicas. Indicador: repartidores con seguro y empleos mantenidos. Revisión: a los seis meses.",
        ["usa el dato", "incluye protecciones", "incluye indicador y plazo"], ["propuesta de siete líneas"], ["ignorar la minoría", "no fijar revisión"],
        "Pregunta cómo se enterarían los repartidores de sus derechos."),
    reinforce="Explica por qué libertad y protección pueden combinarse.",
    extend="Averigua qué seguros o protecciones tienen las personas que trabajan en tu barrio.",
)

# ============================================================ OA 04, clase 5
F = ("Ficha 57 (diagnóstico de ejemplo en el liceo ficticio Los Canelos): 60 estudiantes de 3.º y 4.º medio encuestados; 45 trabajan o trabajarán pronto en prácticas o empleos de verano; "
     "de ellos, 30 no conocen qué es un contrato ni dónde consultar. Recursos: 10 voluntarios, 3 semanas, una persona adulta responsable. "
     "Idea: una «guía de derechos laborales para jóvenes» con información revisada por una institución competente y una charla con un profesional invitado.")
build(
    O4, 5, F,
    use="Aprenderé a diseñar una acción para que jóvenes conozcan y exijan sus derechos laborales: objetivo, contenido, difusión, revisión experta y evaluación.",
    prior=["Sé los derechos laborales básicos.", "Sé diseñar una acción con indicador.", "Sé cuidar la privacidad."],
    explain=[
        "Una guía informativa ayuda a que las personas jóvenes sepan qué derechos tienen y a dónde acudir. Debe tener lenguaje claro, ejemplos ficticios, instituciones competentes y una advertencia: no reemplaza la asesoría de un profesional. Antes de publicarla, una persona experta o una institución la revisa para evitar errores.",
        "El diseño parte del diagnóstico: de 45 estudiantes que trabajan o trabajarán, 30 no conocen qué es un contrato ni dónde consultar. Se fija un objetivo medible, se eligen contenidos (contrato, jornada, remuneración, descanso, seguridad, organización, protecciones para menores de 18), se asignan roles y se define un indicador, como cuántos responden bien una breve pregunta de control.",
        "Se cuida la privacidad: no se usan casos reales ni nombres. Se incluye una orientación de seguridad: ante un trabajo que parezca inseguro o abusivo, se avisa a una persona adulta de confianza y se consulta a la institución competente. Se evalúa con honestidad, sin prometer más de lo que la guía puede lograr.",
    ],
    vocab=[("guía informativa", "material que explica derechos y orienta sobre cómo actuar"), ("institución competente", "organismo al que corresponde resolver o fiscalizar un asunto"), ("revisión experta", "control de la información por alguien que domina el tema"), ("pregunta de control", "pregunta breve para comprobar si se aprendió"), ("caso ficticio", "ejemplo inventado que protege la privacidad")],
    worked=[
        ("Medir el alcance", "En un curso de ejemplo, 20 de 50 conocen un derecho y tras la guía lo conocen 40. ¿Cuántos más lo conocen?", ["Se resta 20 a 40.", "Son 20."], "20 estudiantes más"),
        ("Cuidar la privacidad", "Una guía de ejemplo quiere ilustrar con un caso real de un compañero. ¿Qué se hace?", ["No se usa su historia.", "Se escribe un caso ficticio."], "Usar un caso ficticio"),
    ],
    mistakes=[("Publicar información sin revisión experta.", "Podría contener errores.", "Pide la revisión de una institución competente."),
              ("Dar consejos legales sobre casos individuales.", "Eso requiere un profesional.", "Orienta y deriva.")],
    T=[
        ('abc', '¿Qué es una guía informativa de derechos laborales?', 'Un texto en lenguaje claro con ejemplos, instituciones y la advertencia de que no reemplaza al profesional', 'Un reglamento obligatorio para todos los estudiantes del liceo', 'Un informe con casos reales de compañeros y sus nombres', 'La guía orienta a las personas jóvenes, pero no reemplaza a un profesional.'),
        ('=', '{F} ¿Qué porcentaje de los 60 encuestados trabaja o trabajará pronto?', '45*100//60', 'Se compara la parte con el total de encuestados.', ' %'),
        ('=', '{F} ¿Qué porcentaje de todos los encuestados no conoce qué es un contrato ni dónde consultar?', '30*100//60', 'Se compara la cantidad con el total de encuestados.', ' %'),
        ('=', '{F} Si el objetivo es que los 45 estudiantes que trabajan conozcan sus derechos, ¿cuántos más que los 15 actuales deben aprender?', '45-15', 'Se resta los que ya conocen a la meta.', ' estudiantes'),
        ('abc', '{F} ¿Qué debe hacerse antes de publicar la guía?', 'Que una institución competente la revise', 'Subirla sin revisar para ganar tiempo', 'Que la revise un compañero que ya trabajó', 'La revisión de la institución competente evita errores en información jurídica.'),
        ('abc', '{F} ¿Qué tipo de ejemplo se usa en la guía?', 'Ejemplos ficticios', 'Casos reales de compañeros con sus nombres', 'Casos reales sin nombres', 'Protege la privacidad de las personas.'),
        ('abc', '{F} ¿Qué indicador mide el aprendizaje?', 'Cuántos estudiantes responden bien una pregunta de control', 'Cuántas guías se imprimieron para repartir en el liceo', 'Cuántos voluntarios participaron en la redacción de la guía', 'Mide resultados y no solo actividades.'),
        ('abc', '{F} ¿Qué incluye la orientación de seguridad?', 'Avisar a una persona adulta de confianza y consultar a la institución competente', 'Resolver el problema a solas con el empleador, sin avisar a nadie', 'Renunciar sin consultar a ninguna institución ni persona adulta', 'Protege a la persona ante un trabajo inseguro o abusivo.'),
        ('abc', '{F} ¿Qué advertencia debe llevar la guía?', 'No reemplaza la asesoría de un profesional', 'Reemplaza a los abogados en casos laborales', 'Garantiza resultados en cualquier conflicto', 'Aclara que la guía orienta pero no reemplaza el consejo de un profesional.'),
        ('abc', '{F} Si solo 20 estudiantes responden bien el control, ¿qué corresponde?', 'Revisar cómo se difundió, qué contenidos no se comprendieron, y ajustar', 'Culpar a los estudiantes por no leerla con atención', 'Declarar cumplido el objetivo igualmente ante el liceo', 'Evaluar permite detectar qué falló y corregirlo en la próxima acción.'),
        ('abc', '{F} ¿Qué medio incluye a quienes no leen la guía?', 'Una charla con un profesional invitado de la institución', 'Ninguna medida adicional, porque la guía basta', 'Obligar a leer la guía a todos los estudiantes', 'Complementa la lectura con un formato oral.'),
        ('abc', '{F} ¿Qué contenido es adecuado para la guía?', 'Contrato, jornada, remuneración, descanso, seguridad y protecciones para menores de 18', 'Cifras exactas de multas y plazos tal como las recuerda un voluntario', 'Consejos para negociar en secreto con el empleador', 'Las cifras exactas las fija la ley y deben provenir de la institución competente.'),
        ('=', '{F} Si cada voluntario difunde la guía a 3 de los 30 estudiantes que no conocen sus derechos, ¿cuántos voluntarios se necesitan?', '30//3', 'Se reparte el total de estudiantes entre los que alcanza cada voluntario.', ' voluntarios'),
    ],
    ctx=('abc', 'Un centro de estudiantes de ejemplo quiere una charla sobre derechos laborales. ¿A quién invitaría?', 'A un profesional de la institución competente', 'A un familiar de un estudiante, sin verificar su experiencia', 'A cualquier persona que ofrezca ir', 'Un profesional de la institución competente entrega información confiable y actualizada.'),
    sc=[
        ('¿Qué es una institución competente?', 'El organismo al que corresponde resolver o fiscalizar un asunto', 'Por ejemplo, la inspección del trabajo en asuntos laborales.'),
        ('abc', '¿Qué es una revisión experta?', 'El control de la información por alguien que domina el tema', 'Un permiso para publicar que entrega la dirección del liceo', 'La opinión de un compañero sobre el contenido de la guía', 'Quien domina el tema detecta errores antes de que la guía se publique.'),
        ('¿Qué es un caso ficticio?', 'Un ejemplo inventado que protege la privacidad', 'Un caso inventado enseña sin revelar la situación de ninguna persona real.'),
    ],
    op=("Con la {F} diseña la guía: objetivo medible, cinco contenidos, roles para 10 voluntarios, revisión experta, difusión, indicador y la orientación de seguridad que incluirías.",
        "Objetivo: que 40 de 45 conozcan qué es un contrato y dónde consultar. Contenidos: contrato, jornada, remuneración, descanso, protecciones para menores. Roles: 5 redactan y 5 difunden. Revisión: institución competente. Difusión: panel y charla. Indicador: pregunta de control. Seguridad: avisar a una persona adulta y consultar a la institución.",
        ["objetivo medible", "revisión experta", "orientación de seguridad"], ["diseño de la guía"], ["dar consejos legales", "usar casos reales"],
        "Pregunta qué contenido considera más urgente para su curso."),
    reinforce="Escribe tres contenidos de una guía y por qué los incluirías.",
    extend="Averigua en qué sitio oficial se consultan las normas laborales.",
)
