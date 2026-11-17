"""Diccionario de español de 5.º básico: palabras (sustantivos, adjetivos, adverbios y palabras de enlace) y verbos.

Formato de PALABRAS (una por línea, separado por «|»):
    palabra|sílabas|clase|significado|sinónimos|antónimos|ejemplo|tema
Formato de VERBOS:
    infinitivo|sílabas|significado|yo (hoy)|él o ella (hoy)|él o ella (ayer)|él o ella (mañana)|sinónimos|antónimos|ejemplo
Un guion «-» significa que no hay sinónimo o antónimo sencillo para ese nivel.
Textos propios del proyecto: no copian ningún diccionario publicado.
"""

NIVEL = "5-basico"
IDIOMA = "es"

PALABRAS = """
relato|re-la-to|sustantivo masculino|Narración de hechos, ya sean reales o inventados.|narración|-|Su relato del viaje nos hizo reír.|lenguaje
anécdota|a-néc-do-ta|sustantivo femenino|Historia corta de algo curioso que le pasó a alguien.|-|-|Mi abuelo contó una anécdota de su primer día de clases.|lenguaje
testimonio|tes-ti-mo-nio|sustantivo masculino|Relato de alguien que vivió o presenció un hecho.|declaración|-|El testimonio de una vecina ayudó a entender lo ocurrido.|lenguaje
crónica|cró-ni-ca|sustantivo femenino|Texto que cuenta hechos reales siguiendo el orden en que ocurrieron.|-|-|La crónica describe el terremoto hora por hora.|lenguaje
bitácora|bi-tá-co-ra|sustantivo femenino|Cuaderno donde se anota día a día lo que se va haciendo o descubriendo.|diario de viaje|-|Anoté el avance del experimento en mi bitácora.|lenguaje
glosario|glo-sa-rio|sustantivo masculino|Lista de palabras difíciles de un texto con su explicación.|-|-|El libro trae un glosario al final.|lenguaje
prensa|pren-sa|sustantivo femenino|Conjunto de diarios y revistas que informan de lo que sucede.|-|-|La prensa publicó la noticia al día siguiente.|lenguaje
propaganda|pro-pa-gan-da|sustantivo femenino|Información que se difunde para convencer a la gente de una idea.|-|-|La propaganda electoral llenó las paredes de la calle.|lenguaje
confiable|con-fia-ble|adjetivo|Que merece que se crea en él porque es serio y se puede comprobar.|fidedigno|dudoso|Una enciclopedia es una fuente confiable.|lenguaje
credibilidad|cre-di-bi-li-dad|sustantivo femenino|Cualidad de lo que se puede creer porque parece verdadero y serio.|-|-|El diario perdió credibilidad al publicar un error.|lenguaje
sesgo|ses-go|sustantivo masculino|Inclinación que hace ver un tema solo desde un lado.|parcialidad|-|El texto tenía un sesgo a favor de un equipo.|lenguaje
prejuicio|pre-jui-cio|sustantivo masculino|Opinión que se tiene de algo o alguien sin conocerlo bien.|-|-|Dejé de lado mi prejuicio y probé la comida nueva.|lenguaje
tesis|te-sis|sustantivo femenino|Idea principal que alguien defiende en un texto o en un discurso.|-|-|La tesis del ensayo es que leer mejora la memoria.|lenguaje
fundamento|fun-da-men-to|sustantivo masculino|Razón o dato que sostiene una opinión.|base, razón|-|Tu opinión necesita un fundamento claro.|lenguaje
inferencia|in-fe-ren-cia|sustantivo femenino|Idea que se saca pensando a partir de pistas del texto.|deducción|-|Por una inferencia supe que el personaje estaba triste.|lenguaje
clímax|clí-max|sustantivo masculino|Momento de mayor tensión en una historia.|punto culminante|-|El clímax del cuento llega cuando se apaga la luz.|lenguaje
dramaturgo|dra-ma-tur-go|sustantivo masculino|Persona que escribe obras de teatro.|-|-|El dramaturgo estrenó una obra sobre un pueblo minero.|lenguaje
hipérbole|hi-pér-bo-le|sustantivo femenino|Exageración que se usa para dar más fuerza a lo que se dice.|exageración|-|«Te lo dije un millón de veces» es una hipérbole.|lenguaje
aliteración|a-li-te-ra-ción|sustantivo femenino|Repetición de un mismo sonido en una frase para crear un efecto.|-|-|«El ruido con que rueda la ronca tormenta» tiene aliteración.|lenguaje
símil|sí-mil|sustantivo masculino|Comparación entre dos cosas usando «como» o «parecido a».|comparación|-|«Blanco como la nieve» es un símil.|lenguaje
narrativo|na-rra-ti-vo|adjetivo|Que cuenta una historia con personajes y hechos.|-|-|El cuento es un texto narrativo.|lenguaje
dramático|dra-má-ti-co|adjetivo|Propio del teatro; también, muy intenso y triste.|teatral|-|La escena final fue muy dramática.|lenguaje
lírico|lí-ri-co|adjetivo|Que expresa sentimientos, como los poemas.|-|-|El hablante lírico expresa su nostalgia por el mar.|lenguaje
adverbio|ad-ver-bio|sustantivo masculino|Palabra que explica cómo, cuándo o dónde ocurre una acción.|-|-|«Rápidamente» es un adverbio de modo.|lenguaje
modo|mo-do|sustantivo masculino|Forma en que se expresa el verbo, como indicativo o imperativo.|-|-|El imperativo es el modo de las órdenes.|lenguaje
conjugación|con-ju-ga-ción|sustantivo femenino|Conjunto de formas que toma un verbo según la persona y el tiempo.|-|-|Practicamos la conjugación del verbo «correr».|lenguaje
homónimo|ho-mó-ni-mo|sustantivo masculino|Palabra que suena o se escribe igual que otra pero significa algo distinto.|-|-|«Vaca» y «baca» son homónimos.|lenguaje
aguda|a-gu-da|adjetivo|Dicho de una palabra que se acentúa en la última sílaba.|-|-|«Canción» es una palabra aguda.|lenguaje
llana|lla-na|adjetivo|Dicho de una palabra que se acentúa en la penúltima sílaba.|grave|-|«Árbol» es una palabra llana.|lenguaje
acentuación|a-cen-tua-ción|sustantivo femenino|Uso de la tilde según las reglas del idioma.|-|-|Repasamos las reglas de acentuación.|lenguaje
puntuación|pun-tua-ción|sustantivo femenino|Conjunto de signos como la coma y el punto que ordenan un texto.|-|-|Una buena puntuación facilita la lectura.|lenguaje
coherencia|co-he-ren-cia|sustantivo femenino|Relación lógica entre las ideas de un texto.|-|incoherencia|Tu texto tiene coherencia porque las ideas siguen un orden.|lenguaje
cohesión|co-he-sión|sustantivo femenino|Unión entre las partes de un texto mediante conectores y repeticiones.|-|-|Los conectores dan cohesión a la redacción.|lenguaje
fluidez|flui-dez|sustantivo femenino|Facilidad para leer o hablar sin detenerse.|soltura|-|Con práctica ganó fluidez al leer en voz alta.|lenguaje
cuadro|cua-dro|sustantivo masculino|Pintura hecha sobre tela o madera; también, esquema con filas.|pintura|-|El cuadro muestra un paisaje de la cordillera.|artes
obra|o-bra|sustantivo femenino|Cosa hecha por un artista, como un libro, una pintura o una pieza musical.|creación|-|Esa obra se exhibe en el museo.|artes
estilo|es-ti-lo|sustantivo masculino|Manera propia de hacer algo, como pintar o escribir.|-|-|Cada pintor tiene un estilo distinto.|artes
matiz|ma-tiz|sustantivo masculino|Cada una de las variaciones suaves de un color.|tonalidad|-|El cielo tenía un matiz rosado.|artes
complementario|com-ple-men-ta-rio|adjetivo|Dicho de un color que está frente a otro en el círculo cromático y lo hace resaltar.|-|-|El naranja es complementario del azul.|artes
primario|pri-ma-rio|adjetivo|Que es el primero o el principal; los colores primarios no se logran mezclando otros.|-|-|El rojo es un color primario.|artes
claroscuro|cla-ros-cu-ro|sustantivo masculino|Contraste entre zonas de luz y de sombra en una imagen.|-|-|El claroscuro daba profundidad al retrato.|artes
composición|com-po-si-ción|sustantivo femenino|Manera de ordenar los elementos de una imagen o de una pieza.|-|-|La composición del dibujo deja el sol en el centro.|artes
encuadre|en-cua-dre|sustantivo masculino|Parte de la escena que se elige mostrar en una foto o dibujo.|-|-|Elegí un encuadre que mostrara el puente completo.|artes
técnica|téc-ni-ca|sustantivo femenino|Procedimiento y herramientas usados para hacer una obra.|método|-|Probamos la técnica del collage.|artes
óleo|ó-le-o|sustantivo masculino|Pintura espesa mezclada con aceite, que tarda en secarse.|-|-|El retrato fue pintado al óleo.|artes
pastel|pas-tel|sustantivo masculino|Barra de color suave para dibujar; también, un postre.|tiza|-|Dibujé el atardecer con pastel.|artes
estampado|es-tam-pa-do|sustantivo masculino|Dibujo repetido que se imprime sobre una tela o papel.|-|-|La falda tiene un estampado de flores.|artes
fotografía|fo-to-gra-fí-a|sustantivo femenino|Imagen obtenida con una cámara.|foto|-|La fotografía captó el vuelo de un cóndor.|artes
digital|di-gi-tal|adjetivo|Que se hace o se guarda mediante un aparato electrónico.|-|-|Hicimos un dibujo digital con una tableta.|artes
negra|ne-gra|sustantivo femenino|Figura musical que dura un tiempo.|-|-|Una negra equivale a dos corcheas.|música
blanca|blan-ca|sustantivo femenino|Figura musical que dura dos tiempos.|-|-|Mantén la blanca durante dos pulsos.|música
corchea|cor-che-a|sustantivo femenino|Figura musical que dura medio tiempo.|-|-|Dos corcheas suman una negra.|música
dinámica|di-ná-mi-ca|sustantivo femenino|Variación del volumen de la música, de suave a fuerte.|-|-|La dinámica sube hacia el final de la pieza.|música
acorde|a-cor-de|sustantivo masculino|Varias notas que suenan juntas.|-|-|Toqué un acorde en la guitarra.|música
conjunto|con-jun-to|sustantivo masculino|Grupo de personas o cosas que van juntas; también, grupo de músicos.|grupo|-|El conjunto folclórico se presentó en la plaza.|música
ensamble|en-sam-ble|sustantivo masculino|Grupo de instrumentos o voces que tocan juntos.|-|-|El ensamble de flautas abrió el acto.|música
bombo|bom-bo|sustantivo masculino|Tambor grande de sonido grave.|-|-|El bombo marca el ritmo de la marcha.|música
cajón|ca-jón|sustantivo masculino|Caja de madera sobre la que se sienta quien la toca con las manos.|-|-|Acompañaron la canción con un cajón.|música
maraca|ma-ra-ca|sustantivo femenino|Instrumento que suena al agitarlo, con semillas o piedritas dentro.|-|-|Agité la maraca al ritmo del baile.|música
pandero|pan-de-ro|sustantivo masculino|Instrumento con aro y sonajas que se golpea con la mano.|-|-|El pandero suena con cada golpe.|música
tonada|to-na-da|sustantivo femenino|Melodía sencilla de una canción popular.|-|-|Mi abuela canta una tonada del campo.|música
cumbia|cum-bia|sustantivo femenino|Música y baile popular de origen colombiano.|-|-|En la fiesta bailamos cumbia.|música
rock|rock|sustantivo masculino|Género musical con guitarras eléctricas y ritmo fuerte.|-|-|Mi tío escucha rock de los años ochenta.|música
improvisación|im-pro-vi-sa-ción|sustantivo femenino|Creación de música o de textos en el momento, sin preparación.|-|-|El pianista hizo una improvisación muy aplaudida.|música
ensayo|en-sa-yo|sustantivo masculino|Práctica previa de una presentación; también, texto que expone ideas.|práctica|-|Mañana hay ensayo del coro.|música
membrana|mem-bra-na|sustantivo femenino|Capa fina que rodea una célula o cubre un órgano.|-|-|La membrana controla lo que entra a la célula.|ciencias
citoplasma|ci-to-plas-ma|sustantivo masculino|Contenido gelatinoso que hay dentro de una célula.|-|-|En el citoplasma flotan pequeñas estructuras.|ciencias
unicelular|u-ni-ce-lu-lar|adjetivo|Dicho de un ser vivo formado por una sola célula.|-|pluricelular|La bacteria es un organismo unicelular.|ciencias
pluricelular|plu-ri-ce-lu-lar|adjetivo|Dicho de un ser vivo formado por muchas células.|-|unicelular|Una persona es un ser pluricelular.|ciencias
esófago|e-só-fa-go|sustantivo masculino|Tubo que lleva la comida desde la boca hasta el estómago.|-|-|El esófago empuja el bolo alimenticio hacia abajo.|ciencias
intestino|in-tes-ti-no|sustantivo masculino|Tubo largo donde se absorben los nutrientes de los alimentos.|-|-|En el intestino delgado pasan los nutrientes a la sangre.|ciencias
hígado|hí-ga-do|sustantivo masculino|Órgano grande que ayuda a la digestión y limpia la sangre.|-|-|El hígado produce la bilis.|ciencias
páncreas|pán-cre-as|sustantivo masculino|Órgano que produce jugos para digerir los alimentos.|-|-|El páncreas está detrás del estómago.|ciencias
saliva|sa-li-va|sustantivo femenino|Líquido de la boca que humedece y ablanda la comida.|-|-|La saliva comienza a descomponer el pan.|ciencias
absorción|ab-sor-ción|sustantivo femenino|Paso de los nutrientes desde el intestino hacia la sangre.|-|-|La absorción ocurre en las paredes del intestino.|ciencias
nutrición|nu-tri-ción|sustantivo femenino|Proceso por el que el cuerpo obtiene y usa lo que necesita de los alimentos.|alimentación|-|Una buena nutrición ayuda a crecer sano.|ciencias
proteína|pro-te-í-na|sustantivo femenino|Sustancia de los alimentos que ayuda a construir y reparar el cuerpo.|-|-|Los huevos y las lentejas tienen proteínas.|ciencias
carbohidrato|car-bo-hi-dra-to|sustantivo masculino|Sustancia de los alimentos que da energía, como el azúcar y el almidón.|-|-|El pan y el arroz aportan carbohidratos.|ciencias
grasa|gra-sa|sustantivo femenino|Sustancia que aporta energía y se guarda en el cuerpo.|-|-|Las nueces tienen grasas buenas para el corazón.|ciencias
fibra|fi-bra|sustantivo femenino|Parte de los vegetales que ayuda al tránsito del intestino.|-|-|Las verduras y los cereales integrales tienen fibra.|ciencias
caloría|ca-lo-rí-a|sustantivo femenino|Medida de la energía que dan los alimentos.|-|-|Correr gasta más calorías que caminar.|ciencias
obesidad|o-be-si-dad|sustantivo femenino|Exceso de grasa en el cuerpo que puede dañar la salud.|-|-|La obesidad se previene con ejercicio y buena alimentación.|ciencias
tráquea|trá-que-a|sustantivo femenino|Tubo por donde pasa el aire hacia los pulmones.|-|-|El aire baja por la tráquea.|ciencias
bronquio|bron-quio|sustantivo masculino|Cada uno de los dos tubos que llevan el aire a los pulmones.|-|-|Los bronquios se ramifican dentro de los pulmones.|ciencias
alvéolo|al-vé-o-lo|sustantivo masculino|Saquito diminuto del pulmón donde pasa el oxígeno a la sangre.|-|-|En cada alvéolo se intercambian los gases.|ciencias
diafragma|dia-frag-ma|sustantivo masculino|Músculo bajo los pulmones que ayuda a respirar.|-|-|El diafragma baja cuando inspiramos.|ciencias
oxígeno|o-xí-ge-no|sustantivo masculino|Gas del aire que necesitan los seres vivos para respirar.|-|-|La sangre lleva oxígeno a todo el cuerpo.|ciencias
carbono|car-bo-no|sustantivo masculino|Elemento presente en todos los seres vivos y en gases como el dióxido de carbono.|-|-|Exhalamos dióxido de carbono.|ciencias
arteria|ar-te-ria|sustantivo femenino|Vaso que lleva la sangre desde el corazón al resto del cuerpo.|-|vena|La arteria lleva sangre con oxígeno.|ciencias
vena|ve-na|sustantivo femenino|Vaso que devuelve la sangre al corazón.|-|arteria|Las venas del brazo se ven azuladas.|ciencias
capilar|ca-pi-lar|sustantivo masculino|Vaso sanguíneo muy delgado que conecta arterias y venas.|-|-|Por los capilares la sangre entrega el oxígeno.|ciencias
glóbulo|gló-bu-lo|sustantivo masculino|Cada una de las células que viajan en la sangre.|-|-|Los glóbulos rojos transportan oxígeno.|ciencias
plasma|plas-ma|sustantivo masculino|Parte líquida de la sangre.|-|-|El plasma lleva los nutrientes disueltos.|ciencias
plaqueta|pla-que-ta|sustantivo femenino|Célula de la sangre que ayuda a cerrar las heridas.|-|-|Las plaquetas detienen el sangrado.|ciencias
latido|la-ti-do|sustantivo masculino|Cada golpe que da el corazón al contraerse.|-|-|Conté sesenta latidos en un minuto.|ciencias
tabaco|ta-ba-co|sustantivo masculino|Planta cuyas hojas se fuman y que daña la salud.|-|-|El tabaco causa enfermedades del pulmón.|ciencias
nicotina|ni-co-ti-na|sustantivo femenino|Sustancia del tabaco que crea dependencia.|-|-|La nicotina hace difícil dejar de fumar.|ciencias
alquitrán|al-qui-trán|sustantivo masculino|Sustancia oscura y pegajosa que se forma al quemar tabaco.|-|-|El alquitrán se deposita en los pulmones.|ciencias
adicción|a-dic-ción|sustantivo femenino|Necesidad fuerte de consumir algo que hace daño.|dependencia|-|La adicción afecta la salud y la familia.|ciencias
droga|dro-ga|sustantivo femenino|Sustancia que altera el funcionamiento del cuerpo y puede crear dependencia.|-|-|Las drogas dañan el cerebro.|ciencias
dependencia|de-pen-den-cia|sustantivo femenino|Necesidad de algo o de alguien para poder estar bien.|-|independencia|La dependencia del tabaco es difícil de superar.|ciencias
virus|vi-rus|sustantivo masculino|Microbio muy pequeño que provoca enfermedades como la gripe.|-|-|El virus se contagia por el aire.|ciencias
microorganismo|mi-cro-or-ga-nis-mo|sustantivo masculino|Ser vivo tan pequeño que solo se ve con microscopio.|microbio|-|El yogur se hace con microorganismos útiles.|ciencias
microbio|mi-cro-bio|sustantivo masculino|Ser vivo microscópico, sobre todo el que produce enfermedades.|microorganismo|-|Los microbios se eliminan con agua y jabón.|ciencias
infección|in-fec-ción|sustantivo femenino|Enfermedad producida por microbios que entran al cuerpo.|-|-|Una herida sucia puede causar una infección.|ciencias
contagio|con-ta-gio|sustantivo masculino|Paso de una enfermedad de una persona a otra.|-|-|Taparse al toser evita el contagio.|ciencias
antibiótico|an-ti-bió-ti-co|sustantivo masculino|Medicina que combate las infecciones causadas por bacterias.|-|-|El médico recetó un antibiótico por siete días.|ciencias
fermentación|fer-men-ta-ción|sustantivo femenino|Cambio de un alimento provocado por microorganismos, como en el pan o el yogur.|-|-|La fermentación hace que la masa suba.|ciencias
levadura|le-va-du-ra|sustantivo femenino|Hongo diminuto que hace crecer la masa del pan.|-|-|Agregué levadura a la harina tibia.|ciencias
eléctrico|e-léc-tri-co|adjetivo|Que funciona con electricidad o se relaciona con ella.|-|-|El auto eléctrico no usa bencina.|ciencias
corriente|co-rrien-te|sustantivo femenino|Movimiento continuo de algo, como la electricidad o el agua.|flujo|-|La corriente eléctrica pasa por el cable.|ciencias
batería|ba-te-rí-a|sustantivo femenino|Aparato que almacena energía eléctrica y se puede recargar.|-|-|La batería del celular dura todo el día.|ciencias
interruptor|in-te-rrup-tor|sustantivo masculino|Pieza que abre o cierra el paso de la electricidad.|-|-|Apreté el interruptor y se encendió la luz.|ciencias
cable|ca-ble|sustantivo masculino|Hilo de metal cubierto de plástico por donde pasa la electricidad.|-|-|El cable del cargador está pelado.|ciencias
enchufe|en-chu-fe|sustantivo masculino|Pieza con que un aparato se conecta a la red eléctrica.|-|-|No toques el enchufe con las manos mojadas.|ciencias
aislante|ais-lan-te|sustantivo masculino|Material que no deja pasar la electricidad o el calor.|-|conductor|El plástico es un aislante eléctrico.|ciencias
voltaje|vol-ta-je|sustantivo masculino|Fuerza con que la electricidad empuja por un cable, medida en voltios.|tensión|-|Una pila pequeña tiene poco voltaje.|ciencias
cortocircuito|cor-to-cir-cui-to|sustantivo masculino|Falla eléctrica en que la corriente pasa por un camino indebido y puede producir chispas.|-|-|Un cortocircuito dejó el barrio sin luz.|ciencias
generador|ge-ne-ra-dor|sustantivo masculino|Máquina que produce energía eléctrica.|-|-|El generador mantuvo encendido el hospital.|ciencias
central|cen-tral|sustantivo femenino|Lugar donde se produce energía, como la central hidroeléctrica.|-|-|La central usa la fuerza del agua para dar electricidad.|ciencias
hidroeléctrica|hi-dro-e-léc-tri-ca|adjetivo|Dicho de la energía eléctrica que se obtiene del movimiento del agua.|-|-|Una represa hidroeléctrica abastece a la ciudad.|ciencias
renovable|re-no-va-ble|adjetivo|Que se puede reponer o que no se agota, como el viento o el sol.|-|agotable|La energía solar es renovable.|ciencias
combustible|com-bus-ti-ble|sustantivo masculino|Material que se quema para obtener energía, como la leña o la bencina.|-|-|El carbón es un combustible.|ciencias
bencina|ben-ci-na|sustantivo femenino|Combustible líquido para los autos (uso en Chile).|gasolina|-|Paramos a echar bencina antes del viaje.|ciencias
consumo|con-su-mo|sustantivo masculino|Uso de algo hasta gastarlo, como energía o alimentos.|gasto|ahorro|Bajamos el consumo de luz apagando lo que no se usa.|ciencias
eficiente|e-fi-cien-te|adjetivo|Que logra buenos resultados gastando poco.|eficaz|ineficiente|Una ampolleta led es más eficiente.|ciencias
transformación|trans-for-ma-ción|sustantivo femenino|Cambio de una forma a otra.|cambio|-|En el motor hay una transformación de energía.|ciencias
cuenca|cuen-ca|sustantivo femenino|Territorio cuyas aguas van a un mismo río o lago.|-|-|La cuenca recoge el agua de las lluvias.|geografía
afluente|a-fluen-te|sustantivo masculino|Río pequeño que desemboca en otro mayor.|-|-|El afluente aumentó su caudal con el deshielo.|geografía
desembocadura|de-sem-bo-ca-du-ra|sustantivo femenino|Lugar donde un río termina y entrega sus aguas.|-|nacimiento|En la desembocadura viven muchas aves.|geografía
embalse|em-bal-se|sustantivo masculino|Lago artificial que guarda agua para riego o electricidad.|represa|-|El embalse abastece a los campos vecinos.|geografía
acuífero|a-cuí-fe-ro|sustantivo masculino|Capa de roca o arena que guarda agua bajo la tierra.|-|-|El pozo saca agua del acuífero.|geografía
deshielo|des-hie-lo|sustantivo masculino|Derretimiento de la nieve y del hielo.|-|congelación|En primavera el deshielo alimenta los ríos.|geografía
salinidad|sa-li-ni-dad|sustantivo femenino|Cantidad de sal que tiene el agua.|-|-|El mar tiene mayor salinidad que un lago.|geografía
profundidad|pro-fun-di-dad|sustantivo femenino|Distancia desde la superficie hasta el fondo.|hondura|altura|Midieron la profundidad de la laguna.|geografía
oleaje|o-le-a-je|sustantivo masculino|Movimiento continuo de las olas.|-|-|El oleaje era fuerte y nadie se bañó.|geografía
marino|ma-ri-no|adjetivo|Que pertenece al mar o vive en él.|-|-|La ballena es un mamífero marino.|geografía
potable|po-ta-ble|adjetivo|Dicho del agua que se puede beber sin riesgo.|-|-|Hirvieron el agua para hacerla potable.|geografía
contaminante|con-ta-mi-nan-te|sustantivo masculino|Sustancia que ensucia o daña el aire, el agua o el suelo.|-|-|Los desechos de la fábrica eran un contaminante del río.|geografía
fertilizante|fer-ti-li-zan-te|sustantivo masculino|Sustancia que se echa a la tierra para que las plantas crezcan mejor.|abono|-|El agricultor aplicó fertilizante al maizal.|geografía
estepa|es-te-pa|sustantivo femenino|Terreno llano y seco con pastos y pocos árboles.|-|-|La estepa patagónica es muy ventosa.|geografía
camanchaca|ca-man-cha-ca|sustantivo femenino|Niebla espesa de la costa del norte de Chile.|-|-|La camanchaca humedece los cerros del desierto.|geografía
géiser|géi-ser|sustantivo masculino|Chorro de agua caliente que sale de la tierra.|-|-|El géiser lanzó vapor a gran altura.|geografía
quillay|qui-llay|sustantivo masculino|Árbol de Chile de corteza rica en espuma, usado para limpiar.|-|-|El quillay crece en la zona central.|geografía
araucaria|a-rau-ca-ria|sustantivo femenino|Árbol de Chile de copa alta y hojas puntiagudas, llamado también pehuén.|pehuén|-|Las araucarias viven en la cordillera del sur.|geografía
alpaca|al-pa-ca|sustantivo femenino|Animal andino parecido a la llama, criado por su suave lana.|-|-|El abrigo de alpaca es muy abrigador.|geografía
zona|zo-na|sustantivo femenino|Parte de un territorio con características propias.|área, región|-|La zona norte de Chile es muy seca.|geografía
minería|mi-ne-rí-a|sustantivo femenino|Actividad que extrae minerales de la tierra.|-|-|La minería del cobre es muy importante en Chile.|geografía
cobre|co-bre|sustantivo masculino|Metal rojizo que conduce bien la electricidad.|-|-|Chile es uno de los mayores productores de cobre.|geografía
salitre|sa-li-tre|sustantivo masculino|Mineral usado antes para abonos y explosivos, abundante en el norte de Chile.|-|-|Hubo oficinas salitreras en medio del desierto.|geografía
pesca|pes-ca|sustantivo femenino|Actividad de capturar peces y mariscos.|-|-|La pesca artesanal sostiene a muchas familias de la costa.|geografía
forestal|fo-res-tal|adjetivo|Relacionado con los bosques y su cuidado.|-|-|La industria forestal planta pinos y eucaliptos.|geografía
sostenible|sos-te-ni-ble|adjetivo|Que se puede mantener sin agotar los recursos para el futuro.|sustentable|-|Buscamos una pesca sostenible.|geografía
explotación|ex-plo-ta-ción|sustantivo femenino|Uso de un recurso o de un terreno para sacarle provecho.|-|-|La explotación excesiva agotó el bosque.|geografía
amenaza|a-me-na-za|sustantivo femenino|Posibilidad de que ocurra algo dañino.|riesgo|-|La sequía es una amenaza para la agricultura.|geografía
vulnerable|vul-ne-ra-ble|adjetivo|Que puede ser dañado con facilidad.|frágil|resistente|Las casas de adobe son vulnerables a los terremotos.|geografía
aluvión|a-lu-vión|sustantivo masculino|Crecida repentina de agua con barro y piedras.|-|-|Un aluvión bajó por la quebrada.|geografía
deslizamiento|des-li-za-mien-to|sustantivo masculino|Caída de tierra y rocas por una ladera.|derrumbe|-|El deslizamiento cortó el camino.|geografía
alerta|a-ler-ta|sustantivo femenino|Aviso que hace estar atento ante un peligro.|aviso|-|La alerta de tsunami se difundió por radio.|geografía
protocolo|pro-to-co-lo|sustantivo masculino|Conjunto de pasos que se deben seguir en una situación.|-|-|Seguimos el protocolo de evacuación.|geografía
exploración|ex-plo-ra-ción|sustantivo femenino|Viaje para conocer un lugar desconocido.|-|-|La exploración del continente duró años.|historia
navegación|na-ve-ga-ción|sustantivo femenino|Viaje por mar, ríos o lagos en una embarcación.|-|-|La navegación de aquel tiempo era muy peligrosa.|historia
astrolabio|as-tro-la-bio|sustantivo masculino|Instrumento antiguo para medir la altura de los astros y orientarse.|-|-|Los marinos usaban el astrolabio para ubicarse.|historia
ruta|ru-ta|sustantivo femenino|Camino que se sigue para ir de un lugar a otro.|trayecto|-|Trazaron una ruta hacia las Indias.|historia
europeo|eu-ro-pe-o|adjetivo|Que es de Europa.|-|-|Los viajeros europeos llegaron en barco.|historia
colonial|co-lo-nial|adjetivo|De la época en que un territorio dependía de otro país.|-|-|Visité una casa colonial muy bien conservada.|historia
corona|co-ro-na|sustantivo femenino|Adorno de la cabeza de un rey; también, el rey y su gobierno.|-|-|La Corona española gobernaba sus territorios en América.|historia
rey|rey|sustantivo masculino|Hombre que gobierna una monarquía.|monarca|súbdito|El rey nombraba a los gobernadores.|historia
monarquía|mo-nar-quí-a|sustantivo femenino|Gobierno en que el poder lo tiene un rey o reina.|-|república|España era una monarquía.|historia
virreinato|vi-rrei-na-to|sustantivo masculino|Gran territorio gobernado por un virrey en nombre del rey.|-|-|Chile dependía del virreinato del Perú.|historia
gobernador|go-ber-na-dor|sustantivo masculino|Autoridad que dirige un territorio.|-|-|El gobernador dictó una orden para los vecinos.|historia
cabildo|ca-bil-do|sustantivo masculino|Consejo que gobernaba una ciudad en la Colonia.|-|-|El cabildo se reunía en la plaza.|historia
encomienda|en-co-mien-da|sustantivo femenino|Sistema colonial en que indígenas debían trabajar para un español.|-|-|La encomienda obligaba a trabajar sin buena paga.|historia
hacienda|ha-cien-da|sustantivo femenino|Gran propiedad rural con campos y animales.|fundo|-|En la hacienda se criaba ganado y se cultivaba trigo.|historia
misión|mi-sión|sustantivo femenino|Tarea encargada; también, lugar de trabajo de los misioneros.|encargo|-|Los frailes fundaron una misión en el sur.|historia
misionero|mi-sio-ne-ro|sustantivo masculino|Religioso que viaja a otras tierras para enseñar su fe.|-|-|El misionero aprendió la lengua de la zona.|historia
convento|con-ven-to|sustantivo masculino|Casa donde viven religiosos o religiosas.|monasterio|-|El convento tenía un patio con fuente.|historia
esclavo|es-cla-vo|sustantivo masculino|Persona que era propiedad de otra y no tenía libertad.|-|libre|Muchos esclavos fueron traídos desde África.|historia
mestizaje|mes-ti-za-je|sustantivo masculino|Mezcla de pueblos y culturas distintos.|-|-|El mestizaje dio origen a nuevas costumbres.|historia
criollo|crio-llo|sustantivo masculino|Hijo de españoles nacido en América.|-|-|Los criollos ocupaban cargos en los cabildos.|historia
epidemia|e-pi-de-mia|sustantivo femenino|Enfermedad que se extiende rápido y afecta a muchas personas.|-|-|Una epidemia de viruela diezmó a la población.|historia
indígena|in-dí-ge-na|adjetivo|Que pertenece a los pueblos que vivían en América antes de la llegada de los europeos.|originario|-|Las comunidades indígenas conservan su lengua.|historia
parlamento|par-la-men-to|sustantivo masculino|Reunión formal para conversar y llegar a acuerdos; también, discurso en una obra.|asamblea|-|Hispanos y mapuches realizaron parlamentos para pactar la paz.|historia
tratado|tra-ta-do|sustantivo masculino|Acuerdo formal entre dos o más pueblos o países.|pacto|-|Firmaron un tratado de paz.|historia
alianza|a-lian-za|sustantivo femenino|Unión de personas o grupos para lograr algo juntos.|unión|-|Los pueblos formaron una alianza para defenderse.|historia
adobe|a-do-be|sustantivo masculino|Ladrillo hecho de barro y paja secado al sol.|-|-|Las casas de adobe mantienen el calor.|historia
teja|te-ja|sustantivo femenino|Pieza curva de arcilla que cubre los techos.|-|-|La casa colonial tenía techo de teja.|historia
arquitectura|ar-qui-tec-tu-ra|sustantivo femenino|Arte de diseñar y construir edificios.|-|-|La arquitectura colonial usa muros gruesos.|historia
dignidad|dig-ni-dad|sustantivo femenino|Valor que tiene toda persona y que merece respeto.|-|-|Todos tenemos derecho a vivir con dignidad.|historia
ciudadanía|ciu-da-da-ní-a|sustantivo femenino|Condición de las personas que pertenecen a un país y participan en él.|-|-|La ciudadanía incluye derechos y deberes.|historia
mérito|mé-ri-to|sustantivo masculino|Valor que se gana por el esfuerzo y las buenas acciones.|-|-|Ganó el premio por mérito propio.|historia
reconocimiento|re-co-no-ci-mien-to|sustantivo masculino|Muestra de aprecio por el trabajo o el valor de alguien.|homenaje|-|Recibió un reconocimiento por su ayuda.|historia
cívico|cí-vi-co|adjetivo|Relacionado con los ciudadanos y la vida en comunidad.|-|-|Respetar la fila es una conducta cívica.|historia
directiva|di-rec-ti-va|sustantivo femenino|Grupo de personas elegidas para dirigir un curso o una organización.|-|-|Elegimos la directiva del curso por votación.|historia
candidato|can-di-da-to|sustantivo masculino|Persona que se presenta para ser elegida.|postulante|-|Cada candidato expuso su propuesta.|historia
votación|vo-ta-ción|sustantivo femenino|Acto de elegir a alguien o decidir algo entregando un voto.|-|-|La votación fue secreta.|historia
mayoría|ma-yo-rí-a|sustantivo femenino|Mayor parte de un grupo.|-|minoría|La mayoría del curso eligió el paseo al parque.|historia
minoría|mi-no-rí-a|sustantivo femenino|Parte más pequeña de un grupo.|-|mayoría|Una minoría prefirió quedarse en la sala.|historia
propuesta|pro-pues-ta|sustantivo femenino|Idea que se ofrece para que otros la consideren.|sugerencia|-|Mi propuesta es hacer una colecta de libros.|historia
presupuesto|pre-su-pues-to|sustantivo masculino|Cálculo de lo que se gastará en un proyecto.|-|-|El presupuesto del paseo incluye el transporte.|historia
organización|or-ga-ni-za-ción|sustantivo femenino|Grupo de personas que se unen para un fin común.|asociación|-|La organización vecinal limpió la plaza.|historia
debate|de-ba-te|sustantivo masculino|Conversación en que se defienden ideas distintas con respeto.|discusión|-|Hubo un debate sobre el uso del celular en clase.|historia
asunto|a-sun-to|sustantivo masculino|Tema o materia de la que se trata.|tema, cuestión|-|Es un asunto de interés público.|historia
ofensiva|o-fen-si-va|sustantivo femenino|Acción de atacar para ganar terreno.|ataque|defensiva|El equipo lanzó una ofensiva en el segundo tiempo.|educación física
defensiva|de-fen-si-va|sustantivo femenino|Actitud de quien se protege de un ataque.|-|ofensiva|Jugamos a la defensiva los primeros minutos.|educación física
defensa|de-fen-sa|sustantivo femenino|Acción de proteger algo; también, jugadores que impiden los goles.|protección|ataque|La defensa del equipo bloqueó el tiro.|educación física
ataque|a-ta-que|sustantivo masculino|Acción de avanzar para marcar puntos o goles.|ofensiva|defensa|El ataque rápido sorprendió a los rivales.|educación física
pase|pa-se|sustantivo masculino|Envío del balón a un compañero.|-|-|Hizo un pase largo hacia la banda.|educación física
marca|mar-ca|sustantivo femenino|Vigilancia de un rival; también, el mejor resultado en una prueba.|-|-|Batió su marca personal en los cien metros.|educación física
falta|fal-ta|sustantivo femenino|Infracción de una regla en un juego; también, ausencia de algo.|infracción|-|El árbitro sancionó la falta con un tiro libre.|educación física
habilidad|ha-bi-li-dad|sustantivo femenino|Capacidad para hacer bien algo.|destreza|torpeza|Dribleaba con mucha habilidad.|educación física
motriz|mo-triz|adjetivo|Relativo al movimiento del cuerpo.|-|-|Saltar y lanzar son habilidades motrices.|educación física
danza|dan-za|sustantivo femenino|Arte de moverse al ritmo de la música.|baile|-|La danza de la cueca se baila en pareja.|educación física
baile|bai-le|sustantivo masculino|Movimiento del cuerpo al ritmo de una música.|danza|-|El baile de cierre fue el favorito.|educación física
pareja|pa-re-ja|sustantivo femenino|Conjunto de dos personas que actúan juntas.|-|-|Cada pareja ensayó un paso de cueca.|educación física
condición|con-di-ción|sustantivo femenino|Estado en que se encuentra algo; también, requisito.|estado|-|Mi condición física mejoró con el entrenamiento.|educación física
aeróbico|ae-ró-bi-co|adjetivo|Dicho del ejercicio que se hace a ritmo moderado y por tiempo prolongado.|-|-|Trotar es un ejercicio aeróbico.|educación física
musculatura|mus-cu-la-tu-ra|sustantivo femenino|Conjunto de músculos del cuerpo.|-|-|Los ejercicios fortalecen la musculatura.|educación física
fatiga|fa-ti-ga|sustantivo femenino|Cansancio fuerte después de un esfuerzo.|agotamiento|energía|Sentí fatiga al subir el cerro.|educación física
trote|tro-te|sustantivo masculino|Carrera suave y a paso corto.|-|-|Empezamos con un trote ligero.|educación física
liderazgo|li-de-raz-go|sustantivo masculino|Capacidad de guiar a un grupo e inspirarlo.|-|-|Mostró liderazgo al organizar el equipo.|educación física
espacio|es-pa-cio|sustantivo masculino|Lugar o extensión donde ocurre algo.|-|-|Dejemos espacio para que pase el balón.|educación física
autoestima|au-to-es-ti-ma|sustantivo femenino|Valor y cariño que una persona siente por sí misma.|-|-|Sentirte capaz fortalece tu autoestima.|orientación
fortaleza|for-ta-le-za|sustantivo femenino|Cualidad que ayuda a enfrentar las dificultades; también, edificio de defensa.|-|debilidad|Mi fortaleza es la constancia.|orientación
debilidad|de-bi-li-dad|sustantivo femenino|Aspecto en que alguien necesita mejorar.|-|fortaleza|Reconozco que mi debilidad es el desorden.|orientación
pubertad|pu-ber-tad|sustantivo femenino|Etapa en que el cuerpo empieza a cambiar hacia la adultez.|-|-|En la pubertad cambian la voz y la estatura.|orientación
adolescencia|a-do-les-cen-cia|sustantivo femenino|Período de la vida entre la niñez y la edad adulta.|-|-|La adolescencia trae cambios y nuevas responsabilidades.|orientación
intimidad|in-ti-mi-dad|sustantivo femenino|Parte privada de la vida de una persona.|-|-|Nadie debe invadir tu intimidad.|orientación
privacidad|pri-va-ci-dad|sustantivo femenino|Derecho a mantener privados tus datos y tu vida.|-|-|Cuida tu privacidad en internet.|orientación
autocuidado|au-to-cui-da-do|sustantivo masculino|Cuidado que una persona se da a sí misma para estar sana.|-|-|El autocuidado incluye dormir bien.|orientación
estrés|es-trés|sustantivo masculino|Tensión del cuerpo y la mente ante demasiadas exigencias.|tensión|calma|Antes del examen sentí mucho estrés.|orientación
ansiedad|an-sie-dad|sustantivo femenino|Inquietud intensa ante algo que puede pasar.|nerviosismo|tranquilidad|Respirar hondo calma la ansiedad.|orientación
impulso|im-pul-so|sustantivo masculino|Ganas repentinas de hacer algo sin pensar.|-|-|Controlé el impulso de gritar.|orientación
violencia|vio-len-cia|sustantivo femenino|Uso de la fuerza o de las palabras para hacer daño.|agresión|paz|La violencia nunca resuelve un conflicto.|orientación
acoso|a-co-so|sustantivo masculino|Molestia repetida y dañina hacia una persona.|hostigamiento|-|Informar un caso de acoso protege a la víctima.|orientación
mediación|me-dia-ción|sustantivo femenino|Ayuda de una tercera persona para resolver un conflicto.|-|-|La mediación ayudó a que ambos se escucharan.|orientación
honradez|hon-ra-dez|sustantivo femenino|Cualidad de quien obra con rectitud y no engaña.|honestidad|-|Devolver lo ajeno muestra honradez.|orientación
desafío|de-sa-fí-o|sustantivo masculino|Tarea difícil que pone a prueba a alguien.|reto|-|Aprender a nadar fue un desafío.|orientación
logro|lo-gro|sustantivo masculino|Cosa que se consigue con esfuerzo.|éxito|fracaso|Terminar el proyecto fue un gran logro.|orientación
planilla|pla-ni-lla|sustantivo femenino|Hoja con filas y columnas para ordenar datos (uso en Chile para la hoja de cálculo).|-|-|Anoté los resultados en una planilla.|tecnología
celda|cel-da|sustantivo femenino|Casilla de una planilla donde se escribe un dato.|casilla|-|Escribe la fecha en la celda A1.|tecnología
fórmula|fór-mu-la|sustantivo femenino|Regla que indica qué cálculo hacer con unos datos.|-|-|La fórmula suma todas las celdas de la columna.|tecnología
presentación|pre-sen-ta-ción|sustantivo femenino|Exposición de un tema ante un grupo, a veces con diapositivas.|exposición|-|Mi presentación sobre el cobre duró cinco minutos.|tecnología
diapositiva|dia-po-si-ti-va|sustantivo femenino|Cada pantalla de una presentación.|-|-|Pon una imagen en la primera diapositiva.|tecnología
formato|for-ma-to|sustantivo masculino|Forma en que se presenta un texto o un archivo.|-|-|Cambié el formato de la letra a negrita.|tecnología
navegador|na-ve-ga-dor|sustantivo masculino|Programa para recorrer páginas de internet.|-|-|Abrí el navegador para buscar información.|tecnología
buscador|bus-ca-dor|sustantivo masculino|Sitio de internet que halla páginas según las palabras que se escriben.|-|-|Escribí mi pregunta en el buscador.|tecnología
sitio|si-tio|sustantivo masculino|Lugar; también, página o conjunto de páginas de internet.|lugar|-|Visitamos el sitio oficial del museo.|tecnología
enlace|en-la-ce|sustantivo masculino|Palabra o imagen que lleva a otra página al hacer clic.|vínculo|-|Haz clic en el enlace para ver el video.|tecnología
usuario|u-sua-rio|sustantivo masculino|Persona que usa un aparato o un servicio.|-|-|Cada usuario tiene su propia contraseña.|tecnología
red|red|sustantivo femenino|Conjunto de computadores o personas conectados entre sí; también, malla para pescar.|malla|-|La red del colegio se cayó un momento.|tecnología
seguridad|se-gu-ri-dad|sustantivo femenino|Estado en que no hay peligro; también, medidas para evitarlo.|protección|peligro|Usa gafas por seguridad.|tecnología
criterio|cri-te-rio|sustantivo masculino|Regla o idea que sirve para juzgar o elegir.|-|-|Elegimos la maqueta con un criterio claro.|tecnología
calidad|ca-li-dad|sustantivo femenino|Conjunto de cualidades que hacen bueno a un objeto.|-|-|La calidad del papel es excelente.|tecnología
impacto|im-pac-to|sustantivo masculino|Efecto fuerte que deja algo; también, choque.|efecto|-|El impacto ambiental del embalse fue estudiado.|tecnología
durable|du-ra-ble|adjetivo|Que dura mucho tiempo sin dañarse.|resistente|frágil|Escogimos un material durable.|tecnología
funcional|fun-cio-nal|adjetivo|Que cumple bien la función para la que se hizo.|práctico|-|El diseño debe ser bonito y funcional.|tecnología
prueba|prue-ba|sustantivo femenino|Ensayo para comprobar que algo funciona; también, examen.|ensayo|-|La prueba del puente de palitos fue un éxito.|tecnología
falla|fa-lla|sustantivo femenino|Defecto que impide que algo funcione bien.|defecto|-|Una falla en el cable apagó el motor.|tecnología
cronograma|cro-no-gra-ma|sustantivo masculino|Calendario que ordena las tareas de un proyecto en el tiempo.|-|-|Seguimos el cronograma para entregar a tiempo.|tecnología
requisito|re-qui-si-to|sustantivo masculino|Condición necesaria para lograr algo.|condición|-|Tener el casco es un requisito para andar en bicicleta.|tecnología
plan|plan|sustantivo masculino|Conjunto de pasos pensados para lograr un objetivo.|proyecto|-|Hicimos un plan para armar la maqueta.|tecnología
divisible|di-vi-si-ble|adjetivo|Dicho de un número que se puede dividir por otro sin que sobre nada.|-|-|El doce es divisible por tres.|matemática
potencia|po-ten-cia|sustantivo femenino|Resultado de multiplicar un número por sí mismo varias veces; también, fuerza.|-|-|Ocho es una potencia de dos.|matemática
redondeo|re-don-de-o|sustantivo masculino|Cambio de un número por otro cercano más fácil de usar.|aproximación|-|Con el redondeo, 48 queda en 50.|matemática
estimación|es-ti-ma-ción|sustantivo femenino|Cálculo aproximado de una cantidad.|-|-|Mi estimación fue de cien personas.|matemática
conmutativa|con-mu-ta-ti-va|adjetivo|Dicho de la propiedad que dice que el orden no cambia el resultado al sumar o multiplicar.|-|-|La propiedad conmutativa dice que 3 × 4 es igual a 4 × 3.|matemática
asociativa|a-so-cia-ti-va|adjetivo|Dicho de la propiedad que permite agrupar números de distintas formas sin cambiar el resultado.|-|-|Por la propiedad asociativa, (2 + 3) + 4 es igual a 2 + (3 + 4).|matemática
distributiva|dis-tri-bu-ti-va|adjetivo|Dicho de la propiedad que reparte una multiplicación entre los sumandos.|-|-|Con la propiedad distributiva, 6 × 12 se calcula como 6 × 10 más 6 × 2.|matemática
jerarquía|je-rar-quí-a|sustantivo femenino|Orden de importancia; en matemática, el orden en que se hacen las operaciones.|-|-|La jerarquía indica que se multiplica antes de sumar.|matemática
propia|pro-pia|adjetivo|Dicho de una fracción cuyo numerador es menor que el denominador.|-|impropia|Un medio es una fracción propia.|matemática
impropia|im-pro-pia|adjetivo|Dicho de una fracción cuyo numerador es mayor o igual que el denominador.|-|propia|Cinco tercios es una fracción impropia.|matemática
mixto|mix-to|adjetivo|Formado por una parte entera y una fracción.|-|-|Dos y un medio es un número mixto.|matemática
equivalente|e-qui-va-len-te|adjetivo|Que vale lo mismo que otra cosa.|-|-|Un medio y dos cuartos son fracciones equivalentes.|matemática
porcentaje|por-cen-ta-je|sustantivo masculino|Cantidad que representa una parte de cien.|-|-|El porcentaje de aprobados fue muy alto.|matemática
razón|ra-zón|sustantivo femenino|Comparación de dos cantidades; también, motivo.|-|-|La razón entre niñas y niños del curso es de uno a uno.|matemática
proporción|pro-por-ción|sustantivo femenino|Relación de tamaño o cantidad entre las partes de un todo.|-|-|Mantén la proporción de harina y agua.|matemática
congruente|con-gruen-te|adjetivo|Dicho de figuras que tienen la misma forma y el mismo tamaño.|-|-|Los dos triángulos son congruentes.|matemática
origen|o-ri-gen|sustantivo masculino|Principio de algo; en el plano, el punto donde se cruzan los ejes.|comienzo|fin|El origen tiene coordenadas cero y cero.|matemática
barra|ba-rra|sustantivo femenino|Rectángulo largo que representa un dato en un gráfico.|-|-|La barra más alta muestra el mayor valor.|matemática
moda|mo-da|sustantivo femenino|Valor que más se repite en un conjunto de datos; también, estilo del momento.|-|-|La moda de las notas fue un seis.|matemática
mediana|me-dia-na|sustantivo femenino|Valor que queda en el centro cuando los datos están ordenados.|-|-|La mediana de las estaturas es 140 centímetros.|matemática
rango|ran-go|sustantivo masculino|Diferencia entre el mayor y el menor de los datos.|-|-|El rango de las temperaturas fue de diez grados.|matemática
muestra|mues-tra|sustantivo femenino|Parte pequeña que representa a un grupo mayor.|-|-|Encuestamos a una muestra de veinte estudiantes.|matemática
tendencia|ten-den-cia|sustantivo femenino|Dirección hacia la que parecen ir los datos o las costumbres.|-|-|El gráfico muestra una tendencia al alza.|matemática
intervalo|in-ter-va-lo|sustantivo masculino|Espacio entre dos valores o dos momentos.|-|-|Hubo un intervalo de diez minutos entre las clases.|matemática
diagrama|dia-gra-ma|sustantivo masculino|Dibujo que muestra de forma simple cómo se relacionan las partes de algo.|esquema|-|Dibujé un diagrama del sistema digestivo.|matemática
variable|va-ria-ble|sustantivo femenino|Elemento que puede cambiar de valor.|-|constante|La temperatura es una variable del experimento.|matemática
término|tér-mi-no|sustantivo masculino|Cada elemento de una secuencia o de una operación; también, palabra.|-|-|El quinto término de la secuencia es 23.|matemática
tablero|ta-ble-ro|sustantivo masculino|Superficie plana dividida en casillas para juegos o cálculos.|-|-|El tablero de ajedrez tiene sesenta y cuatro casillas.|matemática
resto|res-to|sustantivo masculino|Lo que sobra al dividir; también, la parte que queda.|sobrante|-|Al dividir 17 por 5 el resto es 2.|matemática
inverso|in-ver-so|adjetivo|Que está en sentido contrario.|-|directo|La resta es la operación inversa de la suma.|matemática
unitario|u-ni-ta-rio|adjetivo|De una sola unidad; el precio unitario es el de cada pieza.|-|-|El precio unitario del cuaderno es de mil pesos.|matemática
oferta|o-fer-ta|sustantivo femenino|Producto que se vende a precio rebajado; también, propuesta.|promoción|-|Compramos zapatillas en oferta.|matemática
ejemplo|e-jem-plo|sustantivo masculino|Caso que se muestra para explicar algo.|-|-|Dame un ejemplo de fracción equivalente.|vida cotidiana
experiencia|ex-pe-rien-cia|sustantivo femenino|Conocimiento que se adquiere al vivir o hacer algo.|-|-|Mi experiencia en el campamento fue inolvidable.|vida cotidiana
información|in-for-ma-ción|sustantivo femenino|Datos que permiten conocer algo.|-|-|Busqué información sobre el cobre en la biblioteca.|vida cotidiana
función|fun-ción|sustantivo femenino|Tarea que cumple algo o alguien.|-|-|La función del corazón es bombear sangre.|vida cotidiana
característica|ca-rac-te-rís-ti-ca|sustantivo femenino|Rasgo que distingue algo de lo demás.|rasgo|-|Una característica del desierto es la poca lluvia.|vida cotidiana
elemento|e-le-men-to|sustantivo masculino|Parte que forma un conjunto.|componente|-|El agua es un elemento esencial para la vida.|vida cotidiana
aspecto|as-pec-to|sustantivo masculino|Cada una de las formas en que se puede ver algo; también, apariencia.|faceta|-|Analizamos tres aspectos del problema.|vida cotidiana
situación|si-tua-ción|sustantivo femenino|Conjunto de circunstancias en que se encuentra alguien.|circunstancia|-|La situación del camino mejoró.|vida cotidiana
opción|op-ción|sustantivo femenino|Cada una de las posibilidades entre las que se puede elegir.|alternativa|-|Tienes dos opciones: caminar o ir en micro.|vida cotidiana
alternativa|al-ter-na-ti-va|sustantivo femenino|Otra posibilidad distinta a la primera.|opción|-|Como no hay pan, la alternativa es comprar galletas.|vida cotidiana
beneficio|be-ne-fi-cio|sustantivo masculino|Provecho o ayuda que se obtiene de algo.|provecho|perjuicio|Hacer deporte tiene muchos beneficios.|vida cotidiana
perjuicio|per-jui-cio|sustantivo masculino|Daño que se causa a alguien o a algo.|daño|beneficio|El ruido causa perjuicio a los vecinos.|vida cotidiana
daño|da-ño|sustantivo masculino|Mal o dolor causado a algo o alguien.|perjuicio|beneficio|La tormenta provocó daño en los techos.|vida cotidiana
cuidado|cui-da-do|sustantivo masculino|Atención que se pone para no dañar algo.|atención|descuido|Lleva el vaso con cuidado.|vida cotidiana
protección|pro-tec-ción|sustantivo femenino|Acción de guardar algo o a alguien de un daño.|resguardo|-|El casco da protección a la cabeza.|vida cotidiana
peligro|pe-li-gro|sustantivo masculino|Situación en que puede ocurrir un daño.|riesgo|seguridad|Cruzar sin mirar es un peligro.|vida cotidiana
límite|lí-mi-te|sustantivo masculino|Punto hasta donde llega algo.|frontera|-|El río es el límite entre los dos campos.|vida cotidiana
avance|a-van-ce|sustantivo masculino|Paso hacia adelante en un trabajo o proyecto.|progreso|retroceso|Mostramos el avance de la maqueta.|vida cotidiana
progreso|pro-gre-so|sustantivo masculino|Mejora gradual de algo.|avance|retroceso|Se nota tu progreso en la lectura.|vida cotidiana
etapa|e-ta-pa|sustantivo femenino|Cada período o parte de un proceso.|fase|-|La primera etapa del proyecto es investigar.|vida cotidiana
fase|fa-se|sustantivo femenino|Cada uno de los estados sucesivos de un proceso o fenómeno.|etapa|-|La luna pasa por distintas fases.|vida cotidiana
nivel|ni-vel|sustantivo masculino|Altura o grado de algo.|grado|-|El nivel del río subió con la lluvia.|vida cotidiana
grupo|gru-po|sustantivo masculino|Conjunto de personas, animales o cosas reunidos.|equipo|-|Trabajamos en un grupo de cuatro.|vida cotidiana
entorno|en-tor-no|sustantivo masculino|Lo que rodea a una persona o a una cosa.|ambiente|-|Cuidemos el entorno de la escuela.|vida cotidiana
rincón|rin-cón|sustantivo masculino|Ángulo que forman dos paredes; también, lugar apartado.|-|-|El gato duerme en un rincón de la sala.|vida cotidiana
bienestar|bien-es-tar|sustantivo masculino|Estado de comodidad y salud del cuerpo y de la mente.|-|malestar|El juego al aire libre da bienestar.|vida cotidiana
oportunidad|o-por-tu-ni-dad|sustantivo femenino|Momento favorable para hacer algo.|ocasión|-|Aproveché la oportunidad de visitar el museo.|vida cotidiana
valor|va-lor|sustantivo masculino|Cualidad que hace que algo sea importante, como la honestidad; también, precio.|-|-|La amistad es un valor que cuidamos.|vida cotidiana
excursión|ex-cur-sión|sustantivo femenino|Paseo corto para conocer un lugar.|paseo|-|En la excursión vimos aves en el humedal.|vida cotidiana
exhibición|ex-hi-bi-ción|sustantivo femenino|Muestra pública de algo.|muestra|-|La exhibición de dibujos duró una semana.|vida cotidiana
huésped|hués-ped|sustantivo masculino|Persona que se aloja en casa ajena o en un hotel.|invitado|anfitrión|Recibimos a un huésped extranjero.|vida cotidiana
poroto|po-ro-to|sustantivo masculino|Legumbre de semilla pequeña (uso en Chile).|frijol|-|Los porotos con riendas son un plato típico.|vida cotidiana
yegua|ye-gua|sustantivo femenino|Hembra del caballo.|-|-|La yegua se acercó a beber agua.|vida cotidiana
jinete|ji-ne-te|sustantivo masculino|Persona que monta a caballo.|-|-|El jinete saludó al público.|vida cotidiana
capaz|ca-paz|adjetivo|Que puede hacer algo bien.|hábil|incapaz|Soy capaz de resolver este problema.|vida cotidiana
adecuado|a-de-cua-do|adjetivo|Que sirve para lo que se necesita.|apropiado|inadecuado|Elige un tono adecuado para hablar con el director.|vida cotidiana
apropiado|a-pro-pia-do|adjetivo|Que es justo para cierta situación.|adecuado|inapropiado|Un abrigo es apropiado para el invierno.|vida cotidiana
eficaz|e-fi-caz|adjetivo|Que logra el resultado que se busca.|eficiente|ineficaz|El jabón es eficaz contra los microbios.|vida cotidiana
digno|dig-no|adjetivo|Que merece algo o que se comporta con honor.|merecedor|indigno|Tiene un trabajo digno.|vida cotidiana
leal|le-al|adjetivo|Fiel a sus amigos o a sus compromisos.|fiel|desleal|Un amigo leal no traiciona tu confianza.|vida cotidiana
humilde|hu-mil-de|adjetivo|Que no presume de lo que tiene o logra.|modesto|soberbio|Ganó el campeonato y siguió siendo humilde.|vida cotidiana
egoísta|e-go-ís-ta|adjetivo|Que solo piensa en sí mismo.|-|generoso|Es egoísta no compartir el balón.|vida cotidiana
prudente|pru-den-te|adjetivo|Que piensa antes de actuar para evitar riesgos.|cauto|imprudente|Es prudente mirar antes de cruzar.|vida cotidiana
sensato|sen-sa-to|adjetivo|Que actúa con buen juicio.|juicioso|insensato|Fue sensato pedir ayuda a un adulto.|vida cotidiana
audaz|au-daz|adjetivo|Que se atreve a hacer cosas difíciles.|atrevido|cobarde|El audaz navegante cruzó el océano.|vida cotidiana
tenaz|te-naz|adjetivo|Que no se rinde fácilmente.|persistente|inconstante|Una investigadora tenaz repitió el experimento.|vida cotidiana
ingenuo|in-ge-nuo|adjetivo|Que cree todo con inocencia y no sospecha de nadie.|inocente|astuto|Fue ingenuo creer que nadie se enteraría.|vida cotidiana
astuto|as-tu-to|adjetivo|Que es hábil para lograr lo que quiere.|listo|ingenuo|El zorro del cuento es muy astuto.|vida cotidiana
rebelde|re-bel-de|adjetivo|Que no obedece o se opone a una autoridad.|desobediente|obediente|El caballo rebelde no quería avanzar.|vida cotidiana
culto|cul-to|adjetivo|Que tiene mucha educación y conocimientos.|instruido|ignorante|Es una persona culta que lee mucho.|vida cotidiana
cierto|cier-to|adjetivo|Que es verdadero; también, alguno que no se precisa.|verdadero|falso|Cierto día de invierno comenzó la lluvia.|vida cotidiana
grave|gra-ve|adjetivo|Que es serio o peligroso.|serio|leve|El accidente fue grave, pero nadie salió herido.|vida cotidiana
leve|le-ve|adjetivo|Que es de poca importancia o muy ligero.|ligero|grave|Tuvo una molestia leve en el tobillo.|vida cotidiana
ligero|li-ge-ro|adjetivo|Que pesa poco o es rápido.|liviano|pesado|Llevo una mochila ligera.|vida cotidiana
no obstante|no obs-tan-te|locución adverbial|Expresa que algo ocurre a pesar de lo dicho antes.|sin embargo|-|Llovía; no obstante, salimos de excursión.|conectores
en consecuencia|en con-se-cuen-cia|locución adverbial|Expresa el resultado de lo anterior.|por lo tanto|-|Hubo temporal; en consecuencia, se suspendieron las clases.|conectores
por consiguiente|por con-si-guien-te|locución adverbial|Introduce una conclusión que se deduce de lo anterior.|por lo tanto|-|El agua es escasa; por consiguiente, debemos cuidarla.|conectores
en resumen|en re-su-men|locución adverbial|Anuncia que se dirá lo principal de lo anterior.|en síntesis|-|En resumen, el reciclaje ayuda al ambiente.|conectores
en síntesis|en sín-te-sis|locución adverbial|Indica que se dará una versión corta de lo dicho.|en resumen|-|En síntesis, el proyecto cumplió sus metas.|conectores
de hecho|de he-cho|locución adverbial|Refuerza lo dicho con algo que realmente ocurre.|en realidad|-|Me gusta leer; de hecho, leo todas las noches.|conectores
en efecto|en e-fec-to|locución adverbial|Confirma que lo dicho es cierto.|efectivamente|-|En efecto, la lluvia llegó antes de lo previsto.|conectores
con respecto a|con res-pec-to a|locución preposicional|Introduce el tema del que se va a hablar.|en cuanto a|-|Con respecto a la tarea, deben entregarla el lunes.|conectores
acerca de|a-cer-ca de|locución preposicional|Indica el tema sobre el que trata algo.|sobre|-|Leímos un artículo acerca de las abejas.|conectores
puesto que|pues-to que|locución conjuntiva|Introduce la razón de lo que se afirma.|ya que|-|Iremos a la plaza, puesto que no llueve.|conectores
ahora bien|a-ho-ra bien|locución adverbial|Introduce una idea que matiza o contrasta con lo anterior.|sin embargo|-|El plan es bueno; ahora bien, falta dinero.|conectores
tal vez|tal vez|locución adverbial|Indica que algo es posible pero no seguro.|quizás|-|Tal vez mañana salga el sol.|conectores
acaso|a-ca-so|adverbio|Expresa duda o posibilidad.|quizás|-|¿Acaso no lo viste en el mapa?|conectores
especialmente|es-pe-cial-men-te|adverbio|De manera particular, más que otras cosas.|particularmente|-|Me gustan las frutas, especialmente las frutillas.|conectores
generalmente|ge-ne-ral-men-te|adverbio|En la mayoría de los casos.|normalmente|raramente|Generalmente llego al colegio a las ocho.|conectores
principalmente|prin-ci-pal-men-te|adverbio|En primer lugar o con más importancia.|sobre todo|-|La zona sur es lluviosa, principalmente en invierno.|conectores
seguramente|se-gu-ra-men-te|adverbio|Con mucha probabilidad.|probablemente|-|Seguramente llegarán antes del almuerzo.|conectores
efectivamente|e-fec-ti-va-men-te|adverbio|Confirma que algo es verdad o realmente ocurrió.|en efecto|-|Efectivamente, el tren llegó a la hora.|conectores
lentamente|len-ta-men-te|adverbio|Con poca velocidad.|despacio|rápidamente|El barco avanzaba lentamente por el fiordo.|conectores
rápidamente|rá-pi-da-men-te|adverbio|Con mucha velocidad.|deprisa|lentamente|Los bomberos llegaron rápidamente.|conectores
cuidadosamente|cui-da-do-sa-men-te|adverbio|Con mucha atención para no dañar nada.|con cuidado|descuidadamente|Armó la maqueta cuidadosamente.|conectores
antiguamente|an-ti-gua-men-te|adverbio|En tiempos pasados.|en otro tiempo|actualmente|Antiguamente se viajaba en carreta.|conectores
actualmente|ac-tual-men-te|adverbio|En el tiempo presente.|hoy en día|antiguamente|Actualmente los niños usan tabletas en clase.|conectores
recién|re-cién|adverbio|Hace muy poco tiempo.|hace poco|-|Mi hermano recién llegó del colegio.|conectores
anteayer|an-te-a-yer|adverbio|En el día anterior a ayer.|-|pasado mañana|Anteayer empezó el campeonato.|conectores
anoche|a-no-che|adverbio|Durante la noche de ayer.|-|-|Anoche se vieron muchas estrellas.|conectores
aparte|a-par-te|adverbio|En otro lugar o por separado.|separadamente|junto|Guarda la tarea aparte de los apuntes.|conectores
tras|tras|preposición|Después de algo o detrás de algo.|después de|-|Tras la lluvia salió el arcoíris.|conectores
ante|an-te|preposición|En presencia de algo o alguien.|frente a|-|Expuso su trabajo ante el curso.|conectores
ni|ni|conjunción|Une dos negaciones.|-|-|No quiero té ni café.|conectores
a fin de que|a fin de que|locución conjuntiva|Indica el propósito con que se hace algo.|para que|-|Habla despacio a fin de que todos entiendan.|conectores
en cuanto a|en cuan-to a|locución preposicional|Señala de qué aspecto se hablará.|con respecto a|-|En cuanto a la comida, la traerá cada uno.|conectores
prólogo|pró-lo-go|sustantivo masculino|Texto que va al comienzo de un libro y lo presenta.|introducción|epílogo|El prólogo explica por qué el autor escribió la novela.|lenguaje
epílogo|e-pí-lo-go|sustantivo masculino|Parte final de una obra que cuenta lo que pasó después.|conclusión|prólogo|En el epílogo se cuenta cómo siguió la vida de los personajes.|lenguaje
estructura|es-truc-tu-ra|sustantivo femenino|Forma en que están ordenadas las partes de algo.|organización|-|La estructura de la noticia va de lo más importante a lo menos importante.|lenguaje
sección|sec-ción|sustantivo femenino|Cada una de las partes en que se divide un todo.|parte|-|La sección de deportes está al final del diario.|lenguaje
apunte|a-pun-te|sustantivo masculino|Nota breve que se escribe para recordar algo.|nota|-|Repasé mis apuntes antes de la prueba.|lenguaje
esquema|es-que-ma|sustantivo masculino|Dibujo o resumen simple que muestra lo principal de un tema.|diagrama|-|Hice un esquema con las ideas del capítulo.|lenguaje
cuestionario|cues-tio-na-rio|sustantivo masculino|Lista de preguntas que se deben responder.|-|-|Respondimos un cuestionario sobre el texto.|lenguaje
consigna|con-sig-na|sustantivo femenino|Instrucción que se da para hacer una tarea.|indicación|-|La consigna pedía escribir tres líneas.|lenguaje
rúbrica|rú-bri-ca|sustantivo femenino|Tabla que muestra qué se evaluará en un trabajo.|-|-|Revisé la rúbrica antes de entregar mi trabajo.|lenguaje
informativo|in-for-ma-ti-vo|adjetivo|Que sirve para dar a conocer datos.|-|-|Leímos un texto informativo sobre los volcanes.|lenguaje
argumentativo|ar-gu-men-ta-ti-vo|adjetivo|Que defiende una idea con razones.|-|-|Un texto argumentativo da motivos para convencer.|lenguaje
descriptivo|des-crip-ti-vo|adjetivo|Que cuenta cómo es algo.|-|-|El párrafo descriptivo detalla cómo es el paisaje.|lenguaje
formal|for-mal|adjetivo|Dicho del lenguaje o del trato que sigue reglas de cortesía.|serio|informal|Usa un lenguaje formal en la carta al director.|lenguaje
informal|in-for-mal|adjetivo|Dicho del lenguaje o del trato sencillo y de confianza.|coloquial|formal|Con mis amigos hablo de manera informal.|lenguaje
registro|re-gis-tro|sustantivo masculino|Manera de hablar según la situación; también, anotación escrita.|-|-|Cambié mi registro al hablar con la rectora.|lenguaje
léxico|lé-xi-co|sustantivo masculino|Conjunto de palabras de una lengua o de una persona.|vocabulario|-|Leer amplía el léxico.|lenguaje
préstamo|prés-ta-mo|sustantivo masculino|Palabra que una lengua toma de otra.|-|-|«Fútbol» es un préstamo del inglés.|lenguaje
extranjerismo|ex-tran-je-ris-mo|sustantivo masculino|Palabra de otro idioma que se usa en el propio.|-|-|«Software» es un extranjerismo.|lenguaje
mapudungun|ma-pu-dun-gun|sustantivo masculino|Lengua del pueblo mapuche.|-|-|Aprendimos un saludo en mapudungun.|lenguaje
quechua|que-chua|sustantivo masculino|Lengua de los pueblos andinos, hablada desde Perú hasta el norte de Chile.|-|-|La palabra «puma» viene del quechua.|lenguaje
bilingüe|bi-lin-güe|adjetivo|Que habla dos lenguas o que se hace en dos lenguas.|-|-|Mi prima es bilingüe en español e inglés.|lenguaje
dialecto|dia-lec-to|sustantivo masculino|Variedad de una lengua que se habla en una región.|-|-|En el campo se oye un dialecto con palabras antiguas.|lenguaje
pronunciación|pro-nun-cia-ción|sustantivo femenino|Modo de decir los sonidos de las palabras.|-|-|Practicamos la pronunciación del poema.|lenguaje
compuesto|com-pues-to|adjetivo|Dicho de un número con más de dos divisores.|-|primo|El nueve es un número compuesto.|matemática
aproximación|a-pro-xi-ma-ción|sustantivo femenino|Resultado cercano al valor exacto.|-|-|Una buena aproximación de 98 es 100.|matemática
reparto|re-par-to|sustantivo masculino|División de algo entre varias personas.|distribución|-|El reparto de las galletas fue equitativo.|matemática
equitativo|e-qui-ta-ti-vo|adjetivo|Que da a cada uno la parte que le corresponde.|justo|desigual|Hicimos un reparto equitativo.|matemática
cuadrilátero|cua-dri-lá-te-ro|sustantivo masculino|Figura plana de cuatro lados.|-|-|El rombo es un cuadrilátero.|matemática
paralelogramo|pa-ra-le-lo-gra-mo|sustantivo masculino|Cuadrilátero con sus lados opuestos paralelos.|-|-|El rectángulo es un paralelogramo.|matemática
arco|ar-co|sustantivo masculino|Parte de una circunferencia; también, arma para lanzar flechas.|-|-|Pinté un arco de la circunferencia de color rojo.|matemática
teselado|te-se-la-do|sustantivo masculino|Cubrimiento de una superficie con figuras que encajan sin dejar huecos.|-|-|El piso tiene un teselado de hexágonos.|matemática
balanceado|ba-lan-cea-do|adjetivo|Que tiene las cantidades adecuadas de cada cosa.|equilibrado|desbalanceado|Una dieta balanceada incluye frutas y verduras.|ciencias
etiqueta|e-ti-que-ta|sustantivo femenino|Papel pegado a un producto con información.|-|-|La etiqueta dice cuántas calorías tiene el yogur.|ciencias
colesterol|co-les-te-rol|sustantivo masculino|Grasa presente en la sangre; en exceso daña el corazón.|-|-|Comer menos frituras ayuda a bajar el colesterol.|ciencias
sedentarismo|se-den-ta-ris-mo|sustantivo masculino|Falta de actividad física habitual.|-|-|El sedentarismo debilita los músculos.|ciencias
pulmonar|pul-mo-nar|adjetivo|Relacionado con los pulmones.|-|-|El humo puede causar enfermedades pulmonares.|ciencias
cardíaco|car-día-co|adjetivo|Relacionado con el corazón.|-|-|El pulso cardíaco sube al correr.|ciencias
orina|o-ri-na|sustantivo femenino|Líquido que el cuerpo elimina tras filtrar la sangre.|-|-|Los riñones producen la orina.|ciencias
riñón|ri-ñón|sustantivo masculino|Órgano que filtra la sangre y produce orina.|-|-|Tenemos dos riñones.|ciencias
vejiga|ve-ji-ga|sustantivo femenino|Bolsa donde se guarda la orina.|-|-|La vejiga se llena poco a poco.|ciencias
sudor|su-dor|sustantivo masculino|Líquido que sale por la piel cuando hace calor o se hace esfuerzo.|transpiración|-|El sudor ayuda a enfriar el cuerpo.|ciencias
poro|po-ro|sustantivo masculino|Agujero muy pequeño de la piel por donde sale el sudor.|-|-|Los poros de la piel dejan salir el sudor.|ciencias
glándula|glán-du-la|sustantivo femenino|Órgano que produce una sustancia útil para el cuerpo.|-|-|La glándula salival produce saliva.|ciencias
hormona|hor-mo-na|sustantivo femenino|Sustancia que regula funciones del cuerpo, como el crecimiento.|-|-|Las hormonas cambian durante la pubertad.|ciencias
inmunidad|in-mu-ni-dad|sustantivo femenino|Capacidad del cuerpo para defenderse de enfermedades.|-|-|La vacuna da inmunidad contra el sarampión.|ciencias
anticuerpo|an-ti-cuer-po|sustantivo masculino|Sustancia que produce el cuerpo para combatir microbios.|-|-|Tras la vacuna el cuerpo fabrica anticuerpos.|ciencias
cuarentena|cua-ren-te-na|sustantivo femenino|Período de aislamiento para evitar que una enfermedad se contagie.|-|-|El enfermo hizo cuarentena en su casa.|ciencias
pandemia|pan-de-mia|sustantivo femenino|Epidemia que se extiende por muchos países.|-|-|La pandemia obligó a cerrar los colegios.|ciencias
higiénico|hi-gié-ni-co|adjetivo|Que está limpio y cuida la salud.|-|antihigiénico|Es higiénico lavarse las manos antes de comer.|ciencias
desinfectante|des-in-fec-tan-te|sustantivo masculino|Producto que mata los microbios.|-|-|Limpiamos la mesa con desinfectante.|ciencias
carga|car-ga|sustantivo femenino|Propiedad de la materia que produce fenómenos eléctricos; también, peso que se lleva.|-|-|Los imanes y las cargas eléctricas se atraen o se repelen.|ciencias
positivo|po-si-ti-vo|adjetivo|Que tiene signo más o carga eléctrica de ese tipo.|-|negativo|La pila tiene un polo positivo.|ciencias
negativo|ne-ga-ti-vo|adjetivo|Que tiene signo menos o carga eléctrica de ese tipo.|-|positivo|Menos tres es un número negativo.|ciencias
linterna|lin-ter-na|sustantivo femenino|Aparato portátil que da luz con una pila.|-|-|Usamos una linterna en la cueva.|ciencias
poste|pos-te|sustantivo masculino|Pieza larga y vertical que sostiene algo, como los cables de luz.|-|-|El poste sostiene los cables eléctricos.|ciencias
medidor|me-di-dor|sustantivo masculino|Aparato que mide el consumo de electricidad o agua.|-|-|El medidor de luz está afuera de la casa.|ciencias
pozo|po-zo|sustantivo masculino|Hoyo profundo que se cava para sacar agua.|-|-|Sacaban el agua del pozo con un balde.|geografía
canal|ca-nal|sustantivo masculino|Cauce hecho por personas para llevar agua; también, paso angosto de mar.|acequia|-|El canal lleva agua a los cultivos.|geografía
acequia|a-ce-quia|sustantivo femenino|Zanja que lleva agua para regar.|canal|-|La acequia riega el huerto.|geografía
riego|rie-go|sustantivo masculino|Aplicación de agua a los cultivos.|-|-|El riego por goteo ahorra agua.|geografía
represa|re-pre-sa|sustantivo femenino|Muro que detiene el agua de un río.|-|-|La represa genera electricidad.|geografía
escasez|es-ca-sez|sustantivo femenino|Falta de algo que se necesita.|falta|abundancia|La escasez de agua preocupa al campo.|geografía
derroche|de-rro-che|sustantivo masculino|Gasto excesivo de algo.|despilfarro|ahorro|Dejar la llave abierta es un derroche de agua.|geografía
descubridor|des-cu-bri-dor|sustantivo masculino|Persona que halla algo que antes no se conocía.|explorador|-|El descubridor llegó a nuevas costas.|historia
cartógrafo|car-tó-gra-fo|sustantivo masculino|Persona que dibuja mapas.|-|-|El cartógrafo trazó la costa de Chile.|historia
especia|es-pe-cia|sustantivo femenino|Sustancia vegetal aromática que se agrega a las comidas, como la pimienta.|-|-|Europa buscaba especias en Oriente.|historia
oro|o-ro|sustantivo masculino|Metal amarillo, brillante y muy valioso.|-|-|Los conquistadores buscaban oro.|historia
plata|pla-ta|sustantivo femenino|Metal blanco y brillante que se usa en joyas y monedas.|-|-|Hicieron monedas de plata.|historia
riqueza|ri-que-za|sustantivo femenino|Abundancia de bienes o de dinero.|fortuna|pobreza|La minería trajo riqueza a la región.|historia
fortín|for-tín|sustantivo masculino|Fuerte pequeño para defender un lugar.|-|-|El fortín vigilaba la frontera.|historia
soldado|sol-da-do|sustantivo masculino|Persona que forma parte de un ejército.|-|-|Los soldados marcharon hacia el sur.|historia
capitán|ca-pi-tán|sustantivo masculino|Jefe de un grupo de soldados o de un barco.|-|-|El capitán dirigió la expedición.|historia
esclavitud|es-cla-vi-tud|sustantivo femenino|Sistema en que unas personas eran propiedad de otras.|-|libertad|La esclavitud fue una práctica injusta.|historia
abuso|a-bu-so|sustantivo masculino|Uso injusto de la fuerza o del poder.|-|-|El abuso de los más fuertes provocó reclamos.|historia
religión|re-li-gión|sustantivo femenino|Conjunto de creencias sobre lo divino y sus ritos.|-|-|La religión ocupaba un lugar central en la Colonia.|historia
cristiano|cris-tia-no|adjetivo|Que sigue la religión basada en las enseñanzas de Jesucristo.|-|-|Los españoles trajeron la fe cristiana.|historia
procesión|pro-ce-sión|sustantivo femenino|Desfile religioso por las calles.|-|-|La procesión recorrió la plaza.|historia
trigo|tri-go|sustantivo masculino|Cereal con cuyo grano se hace harina para el pan.|-|-|En la hacienda cultivaban trigo.|historia
viñedo|vi-ñe-do|sustantivo masculino|Terreno plantado de vides.|-|-|El viñedo da uvas para hacer vino.|historia
mula|mu-la|sustantivo femenino|Animal de carga, hijo de yegua y burro.|-|-|La mula cargaba los sacos por el cerro.|historia
carreta|ca-rre-ta|sustantivo femenino|Vehículo de madera de dos ruedas tirado por bueyes.|-|-|La carreta llevaba el trigo al puerto.|historia
carruaje|ca-rrua-je|sustantivo masculino|Vehículo tirado por caballos para llevar personas.|-|-|El carruaje cruzó la plaza.|historia
capilla|ca-pi-lla|sustantivo femenino|Iglesia pequeña.|-|-|La capilla del fundo tenía una campana.|historia
campanario|cam-pa-na-rio|sustantivo masculino|Torre de una iglesia donde están las campanas.|-|-|Subimos al campanario para ver la ciudad.|historia
claustro|claus-tro|sustantivo masculino|Patio con galerías de un convento.|-|-|Los monjes paseaban por el claustro.|historia
muralla|mu-ra-lla|sustantivo femenino|Muro grande que rodea y defiende un lugar.|-|-|La muralla protegía la ciudad.|historia
zaguán|za-guán|sustantivo masculino|Entrada de una casa antigua entre la calle y el patio.|-|-|El zaguán estaba lleno de macetas.|historia
ladrillo|la-dri-llo|sustantivo masculino|Pieza de arcilla cocida que se usa para construir.|-|-|Levantaron el muro con ladrillos.|historia
restauración|res-tau-ra-ción|sustantivo femenino|Trabajo de reparar algo antiguo para devolverle su aspecto original.|reparación|-|La restauración de la iglesia tomó dos años.|historia
inmueble|in-mue-ble|sustantivo masculino|Edificio o terreno que no se puede mover.|propiedad|mueble|El museo ocupa un inmueble histórico.|historia
ritual|ri-tual|sustantivo masculino|Conjunto de acciones que se repiten con un significado especial.|ceremonia|-|El ritual se realizaba al amanecer.|historia
lonko|lon-ko|sustantivo masculino|Jefe de una comunidad mapuche.|cacique|-|El lonko dirigió la reunión de la comunidad.|historia
ruka|ru-ka|sustantivo femenino|Casa tradicional del pueblo mapuche.|-|-|La ruka tiene techo de paja.|historia
poder|po-der|sustantivo masculino|Capacidad o autoridad para mandar o decidir.|autoridad|-|En una democracia el poder se reparte.|historia
ejecutivo|e-je-cu-ti-vo|adjetivo|Dicho del poder del Estado que gobierna y hace cumplir las leyes.|-|-|El presidente encabeza el poder ejecutivo.|historia
legislativo|le-gis-la-ti-vo|adjetivo|Dicho del poder del Estado que hace las leyes.|-|-|El Congreso ejerce el poder legislativo.|historia
judicial|ju-di-cial|adjetivo|Dicho del poder del Estado que aplica las leyes en los tribunales.|-|-|El poder judicial resuelve conflictos con ayuda de la ley.|historia
tribunal|tri-bu-nal|sustantivo masculino|Lugar donde los jueces resuelven casos según la ley.|-|-|El caso llegó al tribunal.|historia
juez|juez|sustantivo masculino|Persona que decide según la ley quién tiene la razón.|-|-|El juez escuchó a ambas partes.|historia
impuesto|im-pues-to|sustantivo masculino|Dinero que las personas pagan al Estado para financiar servicios.|-|-|Con los impuestos se construyen escuelas.|historia
municipio|mu-ni-ci-pio|sustantivo masculino|Territorio y organización que gobierna una comuna.|-|-|El municipio arregló la plaza.|historia
concejal|con-ce-jal|sustantivo masculino|Persona elegida para formar parte del consejo de una comuna.|-|-|El concejal visitó el barrio.|historia
vecinal|ve-ci-nal|adjetivo|Relacionado con los vecinos de un barrio.|-|-|La junta vecinal se reúne el sábado.|historia
reunión|reu-nión|sustantivo femenino|Encuentro de varias personas para tratar un tema.|encuentro|-|Hubo una reunión de apoderados.|historia
asamblea|a-sam-ble-a|sustantivo femenino|Reunión de muchas personas para decidir algo.|-|-|La asamblea aprobó el nuevo reglamento.|historia
acta|ac-ta|sustantivo femenino|Documento que registra lo tratado en una reunión.|-|-|La secretaria escribió el acta de la reunión.|historia
secretario|se-cre-ta-rio|sustantivo masculino|Persona que registra y ordena los documentos de un grupo.|-|-|El secretario del curso anota los acuerdos.|historia
tesorero|te-so-re-ro|sustantivo masculino|Persona que cuida y anota el dinero de un grupo.|-|-|El tesorero cuenta lo reunido en la rifa.|historia
delegado|de-le-ga-do|sustantivo masculino|Persona elegida para representar a un grupo.|representante|-|La delegada del curso habló con la directora.|historia
urna|ur-na|sustantivo femenino|Caja donde se depositan los votos.|-|-|Cada estudiante puso su voto en la urna.|historia
campaña|cam-pa-ña|sustantivo femenino|Conjunto de acciones para lograr un fin, como ganar una elección.|-|-|La campaña de reciclaje fue un éxito.|historia
flexión|fle-xión|sustantivo femenino|Ejercicio en que se dobla y estira el cuerpo.|-|-|Hicimos diez flexiones de brazos.|educación física
abdominal|ab-do-mi-nal|sustantivo masculino|Ejercicio que trabaja los músculos del estómago.|-|-|Cada día hago veinte abdominales.|educación física
sentadilla|sen-ta-di-lla|sustantivo femenino|Ejercicio en que se doblan las rodillas como para sentarse.|-|-|Hicimos sentadillas para fortalecer las piernas.|educación física
elástico|e-lás-ti-co|adjetivo|Que se estira y vuelve a su forma.|flexible|rígido|Usé una banda elástica en la clase.|educación física
colchoneta|col-cho-ne-ta|sustantivo femenino|Colchón delgado para hacer ejercicios en el suelo.|-|-|Nos tendimos sobre la colchoneta.|educación física
balón|ba-lón|sustantivo masculino|Pelota grande que se usa en deportes.|pelota|-|El balón de básquetbol es naranja.|educación física
cesto|ces-to|sustantivo masculino|Aro con una red donde se encesta en el básquetbol.|-|-|Lanzó el balón al cesto.|educación física
malla|ma-lla|sustantivo femenino|Red de hilos o alambres que se cruzan.|red|-|La pelota quedó enredada en la malla.|educación física
relevo|re-le-vo|sustantivo masculino|Carrera en que un atleta pasa la posta a otro.|-|-|Ganamos la carrera de relevos.|educación física
destreza|des-tre-za|sustantivo femenino|Habilidad para hacer algo con facilidad.|habilidad|torpeza|Mostró destreza al driblar.|educación física
pulsaciones|pul-sa-cio-nes|sustantivo femenino|Latidos del corazón en un minuto.|latidos|-|Tras correr, las pulsaciones subieron.|educación física
bloqueador|blo-quea-dor|sustantivo masculino|Crema que protege la piel del sol.|protector solar|-|Usa bloqueador en la playa.|educación física
insolación|in-so-la-ción|sustantivo femenino|Malestar causado por exponerse demasiado al sol.|-|-|La insolación le provocó dolor de cabeza.|educación física
deshidratación|des-hi-dra-ta-ción|sustantivo femenino|Pérdida excesiva de agua del cuerpo.|-|hidratación|Beber agua previene la deshidratación.|educación física
frustración|frus-tra-ción|sustantivo femenino|Sentimiento de enojo cuando algo no sale como se quiere.|-|-|Sentí frustración al perder el juego.|orientación
celos|ce-los|sustantivo masculino|Sentimiento de molestia por temer perder el cariño de alguien.|-|-|Sentir celos es normal, pero hay que hablarlo.|orientación
valentía|va-len-tí-a|sustantivo femenino|Capacidad de actuar a pesar del miedo.|coraje|cobardía|Mostró valentía al hablar ante todo el colegio.|orientación
autonomía|au-to-no-mí-a|sustantivo femenino|Capacidad de decidir y actuar por uno mismo.|independencia|dependencia|La autonomía se aprende de a poco.|orientación
consentimiento|con-sen-ti-mien-to|sustantivo masculino|Permiso que alguien da libremente.|permiso|-|Nadie puede tocarte sin tu consentimiento.|orientación
ciberacoso|ci-be-ra-co-so|sustantivo masculino|Molestia repetida a una persona a través de internet o del celular.|-|-|El ciberacoso se debe informar a un adulto.|orientación
perfil|per-fil|sustantivo masculino|Conjunto de datos de una persona en una cuenta; también, vista de lado.|-|-|Mantén privado tu perfil.|orientación
denuncia|de-nun-cia|sustantivo femenino|Aviso a una autoridad de algo que está mal.|-|-|La denuncia ayudó a detener el abuso.|orientación
adulto|a-dul-to|sustantivo masculino|Persona que ya terminó de crecer.|-|niño|Pide ayuda a un adulto de confianza.|orientación
apoyo|a-po-yo|sustantivo masculino|Ayuda o sostén que se da a alguien.|ayuda|-|Mi curso me dio mucho apoyo.|orientación
método|mé-to-do|sustantivo masculino|Modo ordenado de hacer algo.|procedimiento|-|Cada estudiante tiene un método para estudiar.|orientación
concentración|con-cen-tra-ción|sustantivo femenino|Atención fija en una sola cosa.|atención|distracción|Necesito concentración para resolver problemas.|orientación
constancia|cons-tan-cia|sustantivo femenino|Firmeza para seguir haciendo algo con el tiempo.|perseverancia|inconstancia|Con constancia mejoró su caligrafía.|orientación
plagio|pla-gio|sustantivo masculino|Copiar el trabajo de otro y presentarlo como propio.|copia|-|El plagio es una falta de honestidad.|orientación
trampa|tram-pa|sustantivo femenino|Engaño que se hace para obtener ventaja.|engaño|-|Copiar en la prueba es una trampa.|orientación
lienzo|lien-zo|sustantivo masculino|Tela sobre la que se pinta.|tela|-|El pintor extendió un lienzo en el caballete.|artes
caballete|ca-ba-lle-te|sustantivo masculino|Soporte donde se apoya un cuadro mientras se pinta.|-|-|El caballete sostenía el lienzo.|artes
cálido|cá-li-do|adjetivo|Dicho de los colores cercanos al rojo y al amarillo.|-|frío|El naranja es un color cálido.|artes
tonalidad|to-na-li-dad|sustantivo femenino|Variación de un color más claro o más oscuro.|matiz|-|La tonalidad del cielo cambió al atardecer.|artes
degradado|de-gra-da-do|sustantivo masculino|Cambio suave de un color a otro.|-|-|El degradado va del azul al verde.|artes
silueta|si-lue-ta|sustantivo femenino|Contorno de una figura que se ve oscuro frente a la luz.|-|-|Se veía la silueta del cerro al atardecer.|artes
contorno|con-tor-no|sustantivo masculino|Línea que rodea una figura.|borde|-|Dibujé el contorno de la hoja.|artes
trazo|tra-zo|sustantivo masculino|Línea hecha con un lápiz o un pincel.|línea|-|El artista hizo un trazo firme.|artes
pincelada|pin-ce-la-da|sustantivo femenino|Cada pasada del pincel sobre una superficie.|-|-|Con tres pinceladas pintó el cielo.|artes
plantilla|plan-ti-lla|sustantivo femenino|Pieza que se usa como molde para repetir una forma.|molde|-|Usé una plantilla para dibujar estrellas.|artes
solista|so-lis-ta|sustantivo masculino|Músico o cantante que actúa solo.|-|-|La solista cantó frente al coro.|música
dúo|dú-o|sustantivo masculino|Grupo de dos personas que cantan o tocan juntas.|-|-|El dúo tocó una cueca.|música
director|di-rec-tor|sustantivo masculino|Persona que dirige un grupo, como una orquesta o un colegio.|-|-|El director marcó el ritmo con las manos.|música
percusión|per-cu-sión|sustantivo femenino|Familia de instrumentos que suenan al ser golpeados.|-|-|El bombo y la maraca son instrumentos de percusión.|música
bailarín|bai-la-rín|sustantivo masculino|Persona que baila.|-|-|El bailarín giró con gran elegancia.|música
coreografía|co-re-o-gra-fí-a|sustantivo femenino|Conjunto de pasos que se ensayan para un baile.|-|-|Aprendimos la coreografía de la cueca.|música
"""

VERBOS = """
absorber|ab-sor-ber|Tomar un líquido o una sustancia y hacerla entrar en el interior.|absorbo|absorbe|absorbió|absorberá|chupar|-|La esponja absorbe el agua del piso.
inhalar|in-ha-lar|Tomar aire o un gas hacia los pulmones.|inhalo|inhala|inhaló|inhalará|aspirar|exhalar|Al inhalar, el pecho se llena de aire.
exhalar|ex-ha-lar|Sacar el aire de los pulmones.|exhalo|exhala|exhaló|exhalará|espirar|inhalar|Exhala despacio por la boca.
bombear|bom-be-ar|Hacer que un líquido se mueva con presión, como lo hace el corazón con la sangre.|bombeo|bombea|bombeó|bombeará|impulsar|-|El corazón bombea sangre a todo el cuerpo.
circular|cir-cu-lar|Moverse por un camino cerrado o por un lugar.|circulo|circula|circuló|circulará|moverse|detenerse|La sangre circula por las venas.
infectar|in-fec-tar|Meter microbios en el cuerpo y causar una enfermedad.|infecto|infecta|infectó|infectará|contagiar|desinfectar|La herida se infectó por falta de limpieza.
contagiar|con-ta-giar|Pasar una enfermedad a otra persona.|contagio|contagia|contagió|contagiará|transmitir|-|La gripe se contagia al estornudar.
desinfectar|des-in-fec-tar|Eliminar los microbios de un lugar o de una herida.|desinfecto|desinfecta|desinfectó|desinfectará|esterilizar|infectar|Desinfectó la herida con agua oxigenada.
fermentar|fer-men-tar|Transformarse un alimento por acción de microorganismos.|fermento|fermenta|fermentó|fermentará|-|-|La masa fermenta cuando se pone en un lugar tibio.
conducir|con-du-cir|Llevar algo por un camino; también, manejar un vehículo o dejar pasar la electricidad.|conduzco|conduce|condujo|conducirá|guiar|-|El cobre conduce muy bien la electricidad.
aislar|ais-lar|Separar algo para que no se toque ni se contagie, o para que no pase la electricidad.|aíslo|aísla|aisló|aislará|apartar|unir|El plástico del cable aísla la corriente.
conectar|co-nec-tar|Unir una cosa con otra para que funcionen juntas.|conecto|conecta|conectó|conectará|unir|desconectar|Conectó la ampolleta al circuito.
generar|ge-ne-rar|Producir algo, como energía o ideas.|genero|genera|generó|generará|producir|-|La represa genera electricidad.
consumir|con-su-mir|Gastar o usar algo, como comida o energía.|consumo|consume|consumió|consumirá|gastar|ahorrar|La estufa consume mucha electricidad.
almacenar|al-ma-ce-nar|Guardar cosas en un lugar para usarlas después.|almaceno|almacena|almacenó|almacenará|guardar|-|La batería almacena energía.
filtrar|fil-trar|Hacer pasar un líquido por un material para limpiarlo.|filtro|filtra|filtró|filtrará|colar|-|Filtramos el agua con una tela.
purificar|pu-ri-fi-car|Quitar a algo las impurezas o lo que lo ensucia.|purifico|purifica|purificó|purificará|depurar|contaminar|La planta purifica el agua del río.
disolver|di-sol-ver|Mezclar una sustancia con un líquido hasta que parezca desaparecer.|disuelvo|disuelve|disolvió|disolverá|deshacer|-|El azúcar se disuelve en el té caliente.
abastecer|a-bas-te-cer|Proveer a un lugar de lo que necesita.|abastezco|abastece|abasteció|abastecerá|proveer|-|El embalse abastece de agua a la ciudad.
explotar|ex-plo-tar|Sacar provecho de un recurso; también, reventar con fuerza.|exploto|explota|explotó|explotará|aprovechar|-|La empresa explota una mina de cobre.
extraer|ex-tra-er|Sacar algo de dentro de un lugar.|extraigo|extrae|extrajo|extraerá|sacar|introducir|Los mineros extraen cobre de la montaña.
exportar|ex-por-tar|Vender productos a otros países.|exporto|exporta|exportó|exportará|-|importar|Chile exporta cobre y fruta.
importar|im-por-tar|Traer productos de otros países para venderlos; también, tener valor para alguien.|importo|importa|importó|importará|-|exportar|Mi tía importa telas de Italia.
navegar|na-ve-gar|Viajar por el agua en una embarcación.|navego|navega|navegó|navegará|zarpar|-|El velero navega por el canal.
colonizar|co-lo-ni-zar|Poblar un territorio y gobernarlo desde otro país.|colonizo|coloniza|colonizó|colonizará|poblar|-|España colonizó gran parte de América.
evangelizar|e-van-ge-li-zar|Enseñar la religión cristiana.|evangelizo|evangeliza|evangelizó|evangelizará|-|-|Los misioneros quisieron evangelizar a los pueblos originarios.
someter|so-me-ter|Hacer que alguien o algo quede bajo el poder de otro.|someto|somete|sometió|someterá|dominar|liberar|Los conquistadores intentaron someter a los pueblos de la zona.
negociar|ne-go-ciar|Conversar para llegar a un acuerdo.|negocio|negocia|negoció|negociará|pactar|-|Los jefes negociaron la paz en el parlamento.
firmar|fir-mar|Escribir el nombre al final de un documento para aprobarlo.|firmo|firma|firmó|firmará|rubricar|-|El presidente firmó el tratado.
pactar|pac-tar|Acordar algo de forma seria con otro.|pacto|pacta|pactó|pactará|acordar|romper|Ambos bandos pactaron una tregua.
defender|de-fen-der|Proteger a alguien o algo de un daño; también, sostener una idea.|defiendo|defiende|defendió|defenderá|proteger|atacar|El portero defendió el arco con valentía.
reclamar|re-cla-mar|Pedir con firmeza algo a lo que se tiene derecho.|reclamo|reclama|reclamó|reclamará|exigir|-|Los vecinos reclamaron por el ruido.
exigir|e-xi-gir|Pedir con fuerza algo que se considera un derecho.|exijo|exige|exigió|exigirá|demandar|-|El profesor exige respeto en la sala.
debatir|de-ba-tir|Conversar sobre un tema defendiendo ideas distintas.|debato|debate|debatió|debatirá|discutir|-|Los estudiantes debatieron sobre el reciclaje.
citar|ci-tar|Nombrar la fuente de una frase o una idea; también, dar una cita a alguien.|cito|cita|citó|citará|mencionar|-|Cita siempre el libro del que sacas los datos.
analizar|a-na-li-zar|Examinar algo con detalle separando sus partes.|analizo|analiza|analizó|analizará|estudiar|-|Analizamos los resultados del experimento.
sintetizar|sin-te-ti-zar|Resumir una idea quedándose con lo más importante.|sintetizo|sintetiza|sintetizó|sintetizará|resumir|ampliar|Sintetiza el capítulo en tres oraciones.
destacar|des-ta-car|Hacer notar algo o sobresalir entre otros.|destaco|destaca|destacó|destacará|resaltar|ocultar|El profesor destacó el esfuerzo del curso.
ilustrar|i-lus-trar|Poner dibujos o ejemplos para explicar mejor un texto.|ilustro|ilustra|ilustró|ilustrará|dibujar|-|Una pintora ilustró el libro de cuentos.
componer|com-po-ner|Crear una obra, sobre todo musical; también, formar un todo con varias partes.|compongo|compone|compuso|compondrá|crear|-|Mi tío compone canciones con la guitarra.
improvisar|im-pro-vi-sar|Hacer algo sin preparación, en el momento.|improviso|improvisa|improvisó|improvisará|-|planificar|El flautista improvisó una melodía.
afinar|a-fi-nar|Ajustar un instrumento para que suene con las notas correctas.|afino|afina|afinó|afinará|ajustar|desafinar|Antes de tocar, afina la guitarra.
ensayar|en-sa-yar|Practicar algo varias veces antes de presentarlo.|ensayo|ensaya|ensayó|ensayará|practicar|-|El coro ensayó dos horas.
simplificar|sim-pli-fi-car|Hacer más simple algo, como una fracción.|simplifico|simplifica|simplificó|simplificará|facilitar|complicar|Simplificó la fracción dividiendo por dos.
verificar|ve-ri-fi-car|Comprobar que algo es verdadero o está correcto.|verifico|verifica|verificó|verificará|comprobar|-|Verifica el resultado con una calculadora.
ampliar|am-pliar|Hacer algo más grande o más extenso.|amplío|amplía|amplió|ampliará|agrandar|reducir|Amplió la foto para ver mejor los detalles.
evaluar|e-va-luar|Calcular el valor o la calidad de algo.|evalúo|evalúa|evaluó|evaluará|valorar|-|El curso evaluó las propuestas.
ensamblar|en-sam-blar|Unir las piezas de algo para armarlo.|ensamblo|ensambla|ensambló|ensamblará|armar|desarmar|Ensamblamos la maqueta con tornillos pequeños.
reflexionar|re-fle-xio-nar|Pensar con calma y detalle sobre algo.|reflexiono|reflexiona|reflexionó|reflexionará|meditar|-|Reflexionó sobre lo que había hecho.
expresar|ex-pre-sar|Dar a conocer lo que se piensa o se siente.|expreso|expresa|expresó|expresará|manifestar|callar|Expresó su opinión con respeto.
controlar|con-tro-lar|Dirigir o vigilar algo para que esté bajo orden.|controlo|controla|controló|controlará|dominar|descontrolar|Aprendí a controlar mi enojo.
enfrentar|en-fren-tar|Hacer frente a un problema o a un peligro.|enfrento|enfrenta|enfrentó|enfrentará|afrontar|evitar|Enfrentó el miedo y habló ante todos.
superar|su-pe-rar|Vencer una dificultad; también, ser mejor que otro.|supero|supera|superó|superará|vencer|-|Superó su miedo al agua.
contener|con-te-ner|Tener algo dentro; también, frenar una emoción o una acción.|contengo|contiene|contuvo|contendrá|incluir|-|El jugo contiene mucha vitamina C.
obtener|ob-te-ner|Conseguir algo que se desea.|obtengo|obtiene|obtuvo|obtendrá|conseguir|perder|Obtuvo el primer lugar en la feria científica.
suponer|su-po-ner|Pensar que algo es cierto sin tener pruebas.|supongo|supone|supuso|supondrá|imaginar|-|Supongo que la lluvia parará pronto.
atravesar|a-tra-ve-sar|Pasar de un lado a otro de algo.|atravieso|atraviesa|atravesó|atravesará|cruzar|-|El puente atraviesa el río.
convertir|con-ver-tir|Hacer que algo cambie y se vuelva otra cosa.|convierto|convierte|convirtió|convertirá|transformar|-|El calor convierte el hielo en agua.
establecer|es-ta-ble-cer|Fundar o dejar fijada una norma o un lugar.|establezco|establece|estableció|establecerá|fijar|-|El curso estableció normas de convivencia.
traducir|tra-du-cir|Expresar en un idioma lo que está dicho en otro.|traduzco|traduce|tradujo|traducirá|-|-|Mi tío traduce textos del inglés al español.
ventilar|ven-ti-lar|Hacer que entre aire fresco a un lugar.|ventilo|ventila|ventiló|ventilará|airear|-|Ventila la sala antes de la clase.
hidratar|hi-dra-tar|Dar agua o humedad a algo.|hidrato|hidrata|hidrató|hidratará|humedecer|deshidratar|Hidrata tu cuerpo bebiendo agua.
restaurar|res-tau-rar|Reparar algo antiguo para que se vea como antes.|restauro|restaura|restauró|restaurará|reparar|deteriorar|Restauraron la iglesia colonial.
juzgar|juz-gar|Decidir si alguien tiene o no la razón.|juzgo|juzga|juzgó|juzgará|sentenciar|-|El tribunal juzgó el caso.
denunciar|de-nun-ciar|Avisar a una autoridad de algo que está mal.|denuncio|denuncia|denunció|denunciará|acusar|-|Denunció el maltrato a la profesora.
concentrar|con-cen-trar|Poner toda la atención en algo.|concentro|concentra|concentró|concentrará|centrar|distraer|Me concentro para resolver el problema.
bautizar|bau-ti-zar|Dar nombre a algo o a alguien; también, hacer una ceremonia de bautizo.|bautizo|bautiza|bautizó|bautizará|nombrar|-|Los exploradores bautizaron el río con un nombre nuevo.
agotar|a-go-tar|Gastar algo por completo.|agoto|agota|agotó|agotará|acabar|llenar|La sequía agotó el agua del pozo.
derrochar|de-rro-char|Gastar demasiado de algo sin necesidad.|derrocho|derrocha|derrochó|derrochará|despilfarrar|ahorrar|No hay que derrochar agua.
vacunar|va-cu-nar|Poner una vacuna a alguien para protegerlo de una enfermedad.|vacuno|vacuna|vacunó|vacunará|inmunizar|-|La enfermera vacunó a los niños.
desplazar|des-pla-zar|Mover algo de un lugar a otro.|desplazo|desplaza|desplazó|desplazará|mover|-|El viento desplaza las nubes.
flexionar|fle-xio-nar|Doblar una parte del cuerpo.|flexiono|flexiona|flexionó|flexionará|doblar|estirar|Flexiona las rodillas antes de saltar.
marcar|mar-car|Hacer una señal en algo; también, anotar un gol.|marco|marca|marcó|marcará|señalar|-|Marcó un gol en el último minuto.
bloquear|blo-quear|Impedir el paso o el movimiento de algo.|bloqueo|bloquea|bloqueó|bloqueará|obstruir|despejar|La defensa bloqueó el tiro.
atacar|a-ta-car|Lanzarse contra alguien para vencerlo.|ataco|ataca|atacó|atacará|embestir|defender|El equipo atacó por la banda.
amenazar|a-me-na-zar|Anunciar que se hará daño o que algo malo puede pasar.|amenazo|amenaza|amenazó|amenazará|intimidar|-|La sequía amenaza los cultivos.
tolerar|to-le-rar|Aceptar algo o a alguien aunque no guste.|tolero|tolera|toleró|tolerará|aguantar|rechazar|Debemos tolerar las ideas distintas.
sospechar|sos-pe-char|Pensar que algo pasa sin tener pruebas.|sospecho|sospecha|sospechó|sospechará|desconfiar|confiar|Sospechó que alguien había entrado.
lamentar|la-men-tar|Sentir pena por algo.|lamento|lamenta|lamentó|lamentará|sentir|celebrar|Lamentó haber llegado tarde.
negar|ne-gar|Decir que algo no es verdad.|niego|niega|negó|negará|rechazar|afirmar|Negó haber roto el vaso.
confesar|con-fe-sar|Reconocer algo que se había ocultado.|confieso|confiesa|confesó|confesará|admitir|negar|Confesó que había copiado.
"""
