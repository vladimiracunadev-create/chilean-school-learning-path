"""Diccionario de español de 7.º básico: palabras (sustantivos, adjetivos, adverbios y palabras de enlace) y verbos.

Formato de PALABRAS (una por línea, separado por «|»):
    palabra|sílabas|clase|significado|sinónimos|antónimos|ejemplo|tema
Formato de VERBOS:
    infinitivo|sílabas|significado|yo (hoy)|él o ella (hoy)|él o ella (ayer)|él o ella (mañana)|sinónimos|antónimos|ejemplo
Un guion «-» significa que no hay sinónimo o antónimo sencillo para ese nivel.
Textos propios del proyecto: no copian ningún diccionario publicado.
"""

NIVEL = "7-basico"
IDIOMA = "es"

PALABRAS = """
hablante|ha-blan-te|sustantivo masculino y femenino|Persona que habla; en un poema, la voz que expresa lo que siente.|-|-|El hablante del poema extraña a su abuela.|lenguaje
alegoría|a-le-go-rí-a|sustantivo femenino|Relato en que los personajes y los hechos representan ideas, como la justicia o el bien.|-|-|La fábula es una alegoría sobre la avaricia.|lenguaje
tragedia|tra-ge-dia|sustantivo femenino|Obra de teatro de final triste, en que un personaje lucha contra su destino.|-|comedia|La tragedia griega termina con la caída del héroe.|lenguaje
comedia|co-me-dia|sustantivo femenino|Obra de teatro divertida que suele tener un final feliz.|-|tragedia|Nos reímos mucho con la comedia del colegio.|lenguaje
drama|dra-ma|sustantivo masculino|Obra de teatro que muestra problemas serios entre las personas.|-|-|El drama trata de una familia que pierde su casa.|lenguaje
acto|ac-to|sustantivo masculino|Cada una de las grandes partes en que se divide una obra de teatro.|-|-|En el segundo acto aparece el villano.|lenguaje
emisor|e-mi-sor|sustantivo masculino|Persona que envía un mensaje.|-|receptor|El emisor del correo es mi profesor.|lenguaje
receptor|re-cep-tor|sustantivo masculino|Persona que recibe un mensaje.|destinatario|emisor|Soy la receptora del aviso del colegio.|lenguaje
contexto|con-tex-to|sustantivo masculino|Situación y datos que rodean a un texto y ayudan a entenderlo.|circunstancia|-|Sin el contexto, la frase no se entiende.|lenguaje
modismo|mo-dis-mo|sustantivo masculino|Expresión fija cuyo sentido no resulta de sumar el de sus palabras.|-|-|«Estar en las nubes» es un modismo.|lenguaje
neologismo|ne-o-lo-gis-mo|sustantivo masculino|Palabra nueva, o con un sentido nuevo, que aparece en una lengua.|-|arcaísmo|«Tuitear» nació como neologismo.|lenguaje
arcaísmo|ar-ca-ís-mo|sustantivo masculino|Palabra o expresión antigua que casi ya no se usa.|-|neologismo|«Vos sois» en un texto antiguo es un arcaísmo.|lenguaje
perífrasis|pe-rí-fra-sis|sustantivo femenino|Grupo de palabras que dice con rodeos lo que podría decirse con una sola.|rodeo|-|«El astro rey» es una perífrasis de «el sol».|lenguaje
subordinada|su-bor-di-na-da|sustantivo femenino|Oración que depende de otra para tener sentido completo.|-|-|En «dijo que vendría», «que vendría» es subordinada.|lenguaje
vocativo|vo-ca-ti-vo|sustantivo masculino|Palabra con que se llama a alguien al hablarle.|-|-|En «Ana, ven acá», «Ana» es un vocativo.|lenguaje
aposición|a-po-si-ción|sustantivo femenino|Palabra o grupo que explica a un sustantivo y va junto a él entre comas.|-|-|En «Santiago, la capital», hay una aposición.|lenguaje
puntos suspensivos|pun-tos sus-pen-si-vos|sustantivo masculino plural|Signo de tres puntos que deja una frase sin terminar o marca una pausa.|-|-|Puse puntos suspensivos para dejar la duda.|lenguaje
contraargumento|con-tra-ar-gu-men-to|sustantivo masculino|Razón que se da para oponerse al argumento de otra persona.|réplica|-|Preparé un contraargumento para el debate.|lenguaje
discurso|dis-cur-so|sustantivo masculino|Texto que se dice en voz alta ante un público.|alocución|-|El presidente del curso dio un discurso breve.|lenguaje
antihéroe|an-ti-hé-ro-e|sustantivo masculino|Protagonista que no tiene las virtudes del héroe tradicional.|-|héroe|El antihéroe de la novela es torpe y miedoso.|lenguaje
prosa|pro-sa|sustantivo femenino|Forma de escribir sin versos ni rima.|-|verso|La novela está escrita en prosa.|lenguaje
décima|dé-ci-ma|sustantivo femenino|Estrofa de diez versos que se canta en la poesía popular.|-|-|El cantor improvisó una décima.|lenguaje
payador|pa-ya-dor|sustantivo masculino|Cantor que improvisa versos con su guitarra.|-|-|El payador respondió con rimas al público.|lenguaje
tertulia|ter-tu-lia|sustantivo femenino|Reunión de personas que conversan sobre temas que les interesan.|-|-|Mis tíos organizan una tertulia sobre libros.|lenguaje
moderador|mo-de-ra-dor|sustantivo masculino|Persona que da la palabra y ordena un debate.|-|-|El moderador pidió respetar los turnos.|lenguaje
disertación|di-ser-ta-ción|sustantivo femenino|Exposición oral y ordenada sobre un tema.|charla|-|Mi disertación fue sobre los volcanes.|lenguaje
hiperónimo|hi-pe-ró-ni-mo|sustantivo masculino|Palabra que nombra un grupo grande que contiene a otras, como «ave» respecto de «gorrión».|-|hipónimo|«Fruta» es hiperónimo de «manzana».|lenguaje
hipónimo|hi-pó-ni-mo|sustantivo masculino|Palabra cuyo significado queda dentro de otro más amplio.|-|hiperónimo|«Rosa» es hipónimo de «flor».|lenguaje
latín|la-tín|sustantivo masculino|Lengua de la antigua Roma, de la que viene el español.|-|-|Muchas palabras en español vienen del latín.|lenguaje
lírica|lí-ri-ca|sustantivo femenino|Género literario en que se expresan sentimientos, casi siempre en verso.|-|-|La lírica nos permite decir lo que sentimos.|lenguaje
narrativa|na-rra-ti-va|sustantivo femenino|Género literario que cuenta historias, como el cuento y la novela.|-|-|Elegí un libro de narrativa para el verano.|lenguaje
dramaturgia|dra-ma-tur-gia|sustantivo femenino|Arte de escribir obras de teatro.|-|-|Mi hermana estudia dramaturgia en un taller.|lenguaje
anticipación|an-ti-ci-pa-ción|sustantivo femenino|Hecho de adelantar algo que ocurrirá después en un relato.|-|-|La nube negra es una anticipación de la tormenta.|lenguaje
enseñanza|en-se-ñan-za|sustantivo femenino|Idea útil que se aprende de una historia o de una experiencia.|lección|-|La enseñanza del cuento es ser honesto.|lenguaje
tópico|tó-pi-co|sustantivo masculino|Tema o idea muy repetida en la literatura.|-|-|El paso del tiempo es un tópico de la poesía.|lenguaje
subgénero|sub-gé-ne-ro|sustantivo masculino|Cada grupo menor dentro de un género literario.|-|-|La novela policial es un subgénero narrativo.|lenguaje
trasfondo|tras-fon-do|sustantivo masculino|Lo que hay detrás de una historia, no dicho directamente.|-|-|El cuento tiene un trasfondo de amistad.|lenguaje
motivo|mo-ti-vo|sustantivo masculino|Razón por la que alguien hace algo.|causa|-|El motivo de su viaje era visitar a su abuela.|lenguaje
por una parte|por u-na par-te|locución adverbial|Presenta el primer punto de una lista que continúa con «por otra parte».|-|-|Por una parte, el cine es caro.|conectores
por tanto|por tan-to|locución conjuntiva|Introduce una consecuencia de lo que se dijo.|por lo tanto|-|Llueve; por tanto, suspendimos el paseo.|conectores
por ende|por en-de|locución adverbial|Introduce una consecuencia, en un estilo más formal.|por tanto|-|Faltó agua; por ende, se cerró la piscina.|conectores
si bien|si bien|locución conjuntiva|Introduce una idea que se acepta, pero que no impide otra.|aunque|-|Si bien es difícil, lo lograremos.|conectores
en contraste|en con-tras-te|locución adverbial|Presenta una idea opuesta a la anterior.|en cambio|-|El norte es seco; en contraste, el sur es lluvioso.|conectores
al contrario|al con-tra-rio|locución adverbial|Indica que lo cierto es lo opuesto de lo que se dijo.|por el contrario|-|No estoy cansada; al contrario, tengo energía.|conectores
a su vez|a su vez|locución adverbial|Añade un hecho que también se produce desde otro lado.|-|-|El río alimenta un lago que, a su vez, riega el valle.|conectores
en todo caso|en to-do ca-so|locución adverbial|Señala lo que se hará si hay dudas.|-|-|En todo caso, llámame si hay un problema.|conectores
así como|a-sí co-mo|locución conjuntiva|Une dos elementos y da importancia a ambos.|y también|-|Compré lápices, así como cuadernos.|conectores
antes de que|an-tes de que|locución conjuntiva|Indica que algo ocurre primero que otro hecho.|-|después de que|Llega antes de que empiece la clase.|conectores
después de que|des-pués de que|locución conjuntiva|Indica que algo ocurre más tarde que otro hecho.|-|antes de que|Almorzamos después de que terminó el partido.|conectores
en primer término|en pri-mer tér-mi-no|locución adverbial|Presenta lo primero de una serie.|en primer lugar|-|En primer término, lean las instrucciones.|conectores
por lo demás|por lo de-más|locución adverbial|Indica que, aparte de lo dicho, el resto es normal.|-|-|Estuvo cansado, pero por lo demás bien.|conectores
valor absoluto|va-lor ab-so-lu-to|sustantivo masculino|Distancia de un número al cero en la recta numérica, sin importar su signo.|-|-|El valor absoluto de −7 es 7.|matemática
opuesto|o-pues-to|sustantivo masculino|Número que está a la misma distancia del cero, pero del otro lado.|inverso aditivo|-|El opuesto de 4 es −4.|matemática
recta numérica|rec-ta nu-mé-ri-ca|sustantivo femenino|Línea en que se ubican los números en orden, con el cero al centro.|-|-|Ubiqué −3 en la recta numérica.|matemática
proporcional|pro-por-cio-nal|adjetivo|Dicho de dos cantidades que cambian de modo que su razón se mantiene.|-|-|El precio es proporcional a los kilos de fruta.|matemática
constante de proporcionalidad|cons-tan-te de pro-por-cio-na-li-dad|sustantivo femenino|Número por el que se multiplica una cantidad para obtener la otra.|-|-|Si 2 manzanas cuestan 600, la constante es 300.|matemática
aumento|au-men-to|sustantivo masculino|Cantidad que se suma a otra para que sea mayor.|incremento|disminución|Hubo un aumento del diez por ciento.|matemática
disminución|dis-mi-nu-ción|sustantivo femenino|Reducción de una cantidad.|descenso|aumento|La disminución de las ventas preocupó al local.|matemática
raíz cuadrada|ra-íz cua-dra-da|sustantivo femenino|Número que, multiplicado por sí mismo, da el número dado.|-|-|La raíz cuadrada de 49 es 7.|matemática
cuadrado perfecto|cua-dra-do per-fec-to|sustantivo masculino|Número cuya raíz cuadrada es un número entero.|-|-|El 36 es un cuadrado perfecto.|matemática
notación científica|no-ta-ción cien-tí-fi-ca|sustantivo femenino|Forma de escribir números muy grandes o muy pequeños con una potencia de diez.|-|-|Escribí la distancia en notación científica.|matemática
máximo común divisor|má-xi-mo co-mún di-vi-sor|sustantivo masculino|El mayor número que divide exactamente a dos o más números.|-|-|El máximo común divisor de 12 y 18 es 6.|matemática
mínimo común múltiplo|mí-ni-mo co-mún múl-ti-plo|sustantivo masculino|El menor número que es múltiplo de dos o más números.|-|-|El mínimo común múltiplo de 4 y 6 es 12.|matemática
expresión algebraica|ex-pre-sión al-ge-brai-ca|sustantivo femenino|Combinación de números, letras y operaciones.|-|-|«3x + 2» es una expresión algebraica.|matemática
inecuación|i-ne-cua-ción|sustantivo femenino|Desigualdad con una incógnita que tiene muchas soluciones posibles.|-|-|La inecuación x > 3 incluye al 4 y al 5.|matemática
plano cartesiano|pla-no car-te-sia-no|sustantivo masculino|Cuadrícula con dos ejes que cruzan en el origen y que sirve para ubicar puntos.|-|-|Dibujé un triángulo en el plano cartesiano.|matemática
par ordenado|par or-de-na-do|sustantivo masculino|Dos números escritos en un orden fijo que ubican un punto en el plano.|-|-|El par ordenado (2, 5) está en el primer cuadrante.|matemática
pi|pi|sustantivo masculino|Número que resulta de dividir el largo de una circunferencia por su diámetro.|-|-|El valor aproximado de pi es 3,14.|matemática
sector circular|sec-tor cir-cu-lar|sustantivo masculino|Parte de un círculo limitada por dos radios y un arco.|-|-|Pinté un sector circular de mi gráfico.|matemática
mediatriz|me-dia-triz|sustantivo femenino|Recta que corta un segmento por su punto medio y en ángulo recto.|-|-|La mediatriz pasa por el punto medio.|matemática
hipotenusa|hi-po-te-nu-sa|sustantivo femenino|Lado más largo de un triángulo rectángulo, opuesto al ángulo recto.|-|-|Calculé la hipotenusa del triángulo.|matemática
cateto|ca-te-to|sustantivo masculino|Cada uno de los dos lados que forman el ángulo recto de un triángulo rectángulo.|-|-|Los dos catetos miden tres y cuatro.|matemática
teorema|te-o-re-ma|sustantivo masculino|Afirmación matemática que se puede demostrar.|-|-|El teorema de Pitágoras relaciona los lados de un triángulo.|matemática
vector|vec-tor|sustantivo masculino|Flecha que indica cuánto y hacia dónde se mueve una figura al trasladarla.|-|-|Trasladé el triángulo siguiendo un vector.|matemática
media aritmética|me-dia a-rit-mé-ti-ca|sustantivo femenino|Resultado de sumar todos los datos y dividir por la cantidad de datos.|promedio|-|La media aritmética de 4, 6 y 8 es 6.|matemática
histograma|his-to-gra-ma|sustantivo masculino|Gráfico de barras pegadas que muestra cuántos datos caen en cada intervalo.|-|-|Hicimos un histograma con las estaturas del curso.|matemática
gráfico circular|grá-fi-co cir-cu-lar|sustantivo masculino|Gráfico en forma de círculo dividido en sectores que muestran partes de un total.|-|-|El gráfico circular muestra los deportes favoritos.|matemática
tallo y hojas|ta-llo y ho-jas|sustantivo masculino|Diagrama que ordena los datos separando la decena de la unidad.|-|-|Organicé las edades en un diagrama de tallo y hojas.|matemática
espacio muestral|es-pa-cio mues-tral|sustantivo masculino|Conjunto de todos los resultados posibles de un experimento.|-|-|El espacio muestral de un dado tiene seis números.|matemática
equiprobable|e-qui-pro-ba-ble|adjetivo|Dicho de los resultados que tienen la misma probabilidad de salir.|-|-|En un dado justo, los números son equiprobables.|matemática
frecuencia relativa|fre-cuen-cia re-la-ti-va|sustantivo femenino|Cuántas veces ocurre algo dividido por el total de intentos.|-|-|Obtuve cara en 6 de 10 tiros, y su frecuencia relativa es 0,6.|matemática
directo|di-rec-to|adjetivo|Dicho de lo que va sin desvíos o en el mismo sentido.|derecho|inverso|En la proporción directa, si una cantidad sube, la otra también.|matemática
elemento neutro|e-le-men-to neu-tro|sustantivo masculino|Número que no cambia el resultado de una operación, como el cero en la suma.|-|-|El elemento neutro de la multiplicación es 1.|matemática
orden de las operaciones|or-den de las o-pe-ra-cio-nes|sustantivo masculino|Reglas que dicen qué cálculo se hace primero en una expresión.|-|-|Por el orden de las operaciones, primero se multiplica.|matemática
común denominador|co-mún de-no-mi-na-dor|sustantivo masculino|Denominador igual para varias fracciones, que permite sumarlas.|-|-|Busqué un común denominador para sumar las fracciones.|matemática
ecuación de primer grado|e-cua-ción de pri-mer gra-do|sustantivo femenino|Ecuación donde la incógnita no tiene exponente mayor que uno.|-|-|Resolví una ecuación de primer grado.|matemática
sustitución|sus-ti-tu-ción|sustantivo femenino|Acción de reemplazar una letra por un valor.|reemplazo|-|Con la sustitución comprobé mi resultado.|matemática
partícula|par-tí-cu-la|sustantivo femenino|Pedazo muy pequeño de materia.|-|-|El humo está hecho de partículas diminutas.|ciencias
átomo|á-to-mo|sustantivo masculino|Parte muy pequeña de la que está hecha toda la materia.|-|-|Cada átomo es demasiado pequeño para verse a simple vista.|ciencias
molécula|mo-lé-cu-la|sustantivo femenino|Grupo de átomos unidos entre sí.|-|-|Una molécula de agua tiene tres átomos.|ciencias
estado de la materia|es-ta-do de la ma-te-ria|sustantivo masculino|Forma en que se presenta la materia: sólida, líquida o gaseosa.|-|-|El hielo es el estado sólido del agua.|ciencias
modelo cinético|mo-de-lo ci-né-ti-co|sustantivo masculino|Explicación que dice que la materia está hecha de partículas en movimiento.|-|-|El modelo cinético explica por qué el gas se expande.|ciencias
dilatación|di-la-ta-ción|sustantivo femenino|Aumento del tamaño de un cuerpo cuando se calienta.|expansión|contracción|La dilatación hace que el riel se alargue con el sol.|ciencias
contracción|con-trac-ción|sustantivo femenino|Disminución del tamaño de un cuerpo cuando se enfría.|encogimiento|dilatación|El frío provoca la contracción del metal.|ciencias
solidificación|so-li-di-fi-ca-ción|sustantivo femenino|Paso de líquido a sólido por enfriamiento.|-|fusión|La solidificación del agua forma el hielo.|ciencias
sublimación|su-bli-ma-ción|sustantivo femenino|Paso directo de sólido a gas, sin pasar por líquido.|-|-|La naftalina desaparece por sublimación.|ciencias
vaporización|va-po-ri-za-ción|sustantivo femenino|Paso de líquido a gas.|-|condensación|La vaporización del agua ocurre al hervirla.|ciencias
punto de ebullición|pun-to de e-bu-lli-ción|sustantivo masculino|Temperatura a la que un líquido hierve.|-|-|El punto de ebullición del agua es cien grados.|ciencias
punto de fusión|pun-to de fu-sión|sustantivo masculino|Temperatura a la que un sólido se derrite.|-|-|El hielo tiene un punto de fusión de cero grados.|ciencias
energía térmica|e-ner-gí-a tér-mi-ca|sustantivo femenino|Energía que tienen los cuerpos por el movimiento de sus partículas.|-|-|La energía térmica pasa de lo caliente a lo frío.|ciencias
equilibrio térmico|e-qui-li-brio tér-mi-co|sustantivo masculino|Situación en que dos cuerpos en contacto llegan a la misma temperatura.|-|-|El té llegó al equilibrio térmico con el ambiente.|ciencias
conducción|con-duc-ción|sustantivo femenino|Paso del calor a través de un material por contacto.|-|-|La cuchara se calienta por conducción.|ciencias
convección|con-vec-ción|sustantivo femenino|Paso del calor mediante el movimiento de un líquido o de un gas.|-|-|El aire caliente sube por convección.|ciencias
newton|new-ton|sustantivo masculino|Unidad con que se mide la fuerza.|-|-|La fuerza se mide en newton.|ciencias
rozamiento|ro-za-mien-to|sustantivo masculino|Fuerza que se opone al movimiento cuando dos superficies se tocan.|fricción|-|El rozamiento frena la bicicleta.|ciencias
fricción|fric-ción|sustantivo femenino|Roce entre dos superficies que se tocan al moverse.|rozamiento|-|La fricción calienta las manos.|ciencias
aceleración|a-ce-le-ra-ción|sustantivo femenino|Cambio de la velocidad de un cuerpo en cada unidad de tiempo.|-|-|La aceleración del auto fue rápida al partir.|ciencias
inercia|i-ner-cia|sustantivo femenino|Tendencia de un cuerpo a seguir quieto o a seguir moviéndose igual.|-|-|Por inercia, el cuerpo se va hacia delante cuando el bus frena.|ciencias
onda|on-da|sustantivo femenino|Perturbación que se propaga llevando energía de un lugar a otro.|-|-|El sonido viaja como una onda.|ciencias
longitud de onda|lon-gi-tud de on-da|sustantivo femenino|Distancia entre dos puntos iguales y seguidos de una onda.|-|-|La longitud de onda de un sonido grave es grande.|ciencias
amplitud|am-pli-tud|sustantivo femenino|Altura máxima que alcanza una onda desde su punto de reposo.|-|-|Una gran amplitud significa un sonido fuerte.|ciencias
propagación|pro-pa-ga-ción|sustantivo femenino|Avance de una onda, de una enfermedad o de una noticia por un lugar.|difusión|-|La propagación del sonido necesita un medio.|ciencias
medio|me-dio|sustantivo masculino|Sustancia por la que viaja una onda, como el aire o el agua.|-|-|El sonido no viaja sin un medio.|ciencias
ultrasonido|ul-tra-so-ni-do|sustantivo masculino|Sonido muy agudo que las personas no pueden oír.|-|-|Los murciélagos usan ultrasonido para orientarse.|ciencias
reverberación|re-ver-be-ra-ción|sustantivo femenino|Prolongación de un sonido en un lugar cerrado.|resonancia|-|En la iglesia vacía hay mucha reverberación.|ciencias
refracción|re-frac-ción|sustantivo femenino|Cambio de dirección de la luz al pasar de un medio a otro.|-|-|La refracción hace que el lápiz parezca quebrado en el vaso.|ciencias
espectro|es-pec-tro|sustantivo masculino|Conjunto de colores en que se separa la luz.|-|-|El arcoíris muestra el espectro de la luz.|ciencias
cóncavo|cón-ca-vo|adjetivo|Que tiene la parte central hundida, como el interior de una cuchara.|hundido|convexo|Un espejo cóncavo agranda las imágenes cercanas.|ciencias
convexo|con-ve-xo|adjetivo|Que tiene la parte central abultada hacia fuera.|abultado|cóncavo|El espejo convexo muestra un campo amplio.|ciencias
translúcido|trans-lú-ci-do|adjetivo|Que deja pasar la luz, pero no deja ver con claridad.|-|opaco|El vidrio esmerilado es translúcido.|ciencias
penumbra|pe-num-bra|sustantivo femenino|Zona entre la luz y la sombra completa.|media luz|claridad|En la penumbra casi no se leía.|ciencias
fotosíntesis|fo-to-sín-te-sis|sustantivo femenino|Proceso por el que las plantas producen su alimento con luz, agua y dióxido de carbono.|-|-|La fotosíntesis ocurre en las hojas.|ciencias
clorofila|clo-ro-fi-la|sustantivo femenino|Sustancia verde de las plantas que capta la luz del sol.|-|-|La clorofila da el color verde a las hojas.|ciencias
cloroplasto|clo-ro-plas-to|sustantivo masculino|Parte de la célula vegetal donde ocurre la fotosíntesis.|-|-|Los cloroplastos contienen clorofila.|ciencias
mitocondria|mi-to-con-dria|sustantivo femenino|Parte de la célula que libera energía de los alimentos.|-|-|La mitocondria es la central de energía de la célula.|ciencias
organelo|or-ga-ne-lo|sustantivo masculino|Cada una de las pequeñas estructuras que cumplen una función dentro de la célula.|-|-|El núcleo es un organelo de la célula.|ciencias
pared celular|pa-red ce-lu-lar|sustantivo femenino|Capa rígida que rodea la célula de las plantas.|-|-|La pared celular da forma a las células vegetales.|ciencias
eucarionte|eu-ca-rion-te|adjetivo|Dicho de la célula que tiene un núcleo bien definido.|-|procarionte|Las células de los animales son eucariontes.|ciencias
procarionte|pro-ca-rion-te|adjetivo|Dicho de la célula que no tiene núcleo definido.|-|eucarionte|Las bacterias son procariontes.|ciencias
ADN|a-de-e-ne|sustantivo masculino|Molécula que guarda la información genética de los seres vivos.|-|-|El ADN está en el núcleo de la célula.|ciencias
cromosoma|cro-mo-so-ma|sustantivo masculino|Estructura del núcleo que lleva los genes.|-|-|Los humanos tienen cuarenta y seis cromosomas.|ciencias
gen|gen|sustantivo masculino|Parte del ADN que contiene una instrucción para una característica.|-|-|Un gen influye en el color de los ojos.|ciencias
cadena trófica|ca-de-na tró-fi-ca|sustantivo femenino|Serie de seres vivos en que cada uno sirve de alimento al siguiente.|-|-|En la cadena trófica, el zorro come al conejo.|ciencias
red trófica|red tró-fi-ca|sustantivo femenino|Conjunto de cadenas que se cruzan en un mismo ecosistema.|-|-|La red trófica muestra quién come a quién.|ciencias
mutualismo|mu-tua-lis-mo|sustantivo masculino|Relación entre especies en que ambas salen beneficiadas.|-|parasitismo|El mutualismo une al colibrí con las flores.|ciencias
parasitismo|pa-ra-si-tis-mo|sustantivo masculino|Relación en que un ser vivo se beneficia y el otro sale perjudicado.|-|mutualismo|El parasitismo de las garrapatas enferma a los animales.|ciencias
nicho ecológico|ni-cho e-co-ló-gi-co|sustantivo masculino|Papel que cumple una especie en su ecosistema y lo que necesita para vivir.|-|-|El nicho del búho es cazar de noche.|ciencias
laboratorio|la-bo-ra-to-rio|sustantivo masculino|Lugar con instrumentos para hacer experimentos y análisis.|-|-|En el laboratorio usamos delantal y lentes.|ciencias
matraz|ma-traz|sustantivo masculino|Frasco de vidrio con base ancha y cuello angosto.|-|-|Calenté agua en un matraz.|ciencias
pipeta|pi-pe-ta|sustantivo femenino|Tubo fino de vidrio que sirve para medir y pasar pequeñas cantidades de líquido.|-|-|Con la pipeta saqué diez mililitros.|ciencias
reactivo|re-ac-ti-vo|sustantivo masculino|Sustancia que se usa para provocar o detectar una reacción.|-|-|Añadí un reactivo para ver si cambiaba de color.|ciencias
trastorno|tras-tor-no|sustantivo masculino|Alteración de la salud, del ánimo o del orden normal de algo.|-|-|El trastorno del sueño le impide descansar.|ciencias
ovulación|o-vu-la-ción|sustantivo femenino|Salida de un óvulo maduro del ovario.|-|-|La ovulación ocurre cada mes.|ciencias
gameto|ga-me-to|sustantivo masculino|Célula sexual, que es el óvulo o el espermatozoide.|-|-|El gameto masculino se llama espermatozoide.|ciencias
embarazo|em-ba-ra-zo|sustantivo masculino|Período en que una mujer lleva un bebé en el vientre.|gestación|-|El embarazo dura unas cuarenta semanas.|ciencias
sexualidad|se-xua-li-dad|sustantivo femenino|Conjunto de sentimientos, conductas y rasgos ligados a ser mujer u hombre y a relacionarse con otros.|-|-|La sexualidad se vive con respeto y responsabilidad.|ciencias
madurez|ma-du-rez|sustantivo femenino|Etapa en que algo o alguien ha terminado su desarrollo.|-|inmadurez|Con la madurez llegan nuevas responsabilidades.|ciencias
placa tectónica|pla-ca tec-tó-ni-ca|sustantivo femenino|Gran trozo de la corteza terrestre que se mueve muy lentamente.|-|-|Chile se ubica donde chocan dos placas tectónicas.|ciencias
deriva continental|de-ri-va con-ti-nen-tal|sustantivo femenino|Idea de que los continentes se han ido separando con el tiempo.|-|-|La deriva continental explica la forma de las costas.|ciencias
capa de ozono|ca-pa de o-zo-no|sustantivo femenino|Zona de la atmósfera que filtra gran parte de los rayos ultravioleta.|-|-|La capa de ozono nos protege del sol.|ciencias
efecto invernadero|e-fec-to in-ver-na-de-ro|sustantivo masculino|Calentamiento de la Tierra porque algunos gases retienen el calor.|-|-|El efecto invernadero aumenta con la contaminación.|ciencias
cambio climático|cam-bio cli-má-ti-co|sustantivo masculino|Variación del clima de la Tierra que se nota por décadas.|-|-|El cambio climático derrite los glaciares.|ciencias
presión atmosférica|pre-sión at-mos-fé-ri-ca|sustantivo femenino|Peso del aire sobre la superficie terrestre.|-|-|La presión atmosférica baja en lo alto de una montaña.|ciencias
huracán|hu-ra-cán|sustantivo masculino|Tormenta muy fuerte con vientos giratorios, propia de mares cálidos.|ciclón|-|El huracán dañó casas en la costa.|ciencias
tornado|tor-na-do|sustantivo masculino|Remolino de viento muy fuerte que baja de una nube hasta el suelo.|-|-|El tornado levantó los techos.|ciencias
sedimento|se-di-men-to|sustantivo masculino|Material sólido que el agua o el viento van dejando en el fondo.|-|-|El río deposita sedimento en su desembocadura.|ciencias
meteorología|me-te-o-ro-lo-gí-a|sustantivo femenino|Ciencia que estudia el tiempo atmosférico.|-|-|La meteorología anunció lluvias para el fin de semana.|ciencias
pronóstico|pro-nós-ti-co|sustantivo masculino|Anuncio de lo que se espera que ocurra.|predicción|-|El pronóstico dice que habrá sol.|ciencias
intoxicación|in-to-xi-ca-ción|sustantivo femenino|Daño al cuerpo causado por una sustancia dañina.|envenenamiento|-|La intoxicación por comida mala causa dolor de guata.|ciencias
fumador|fu-ma-dor|sustantivo masculino|Persona que fuma.|-|-|El fumador tose por las mañanas.|ciencias
hominización|ho-mi-ni-za-ción|sustantivo femenino|Proceso de cambios por el que los antepasados del ser humano llegaron a ser como somos.|-|-|La hominización incluyó caminar en dos pies.|historia
homínido|ho-mí-ni-do|sustantivo masculino|Ser vivo de la familia de los antepasados del ser humano.|-|-|Lucy fue una homínida muy antigua.|historia
bipedismo|bi-pe-dis-mo|sustantivo masculino|Capacidad de caminar sobre dos pies.|-|-|El bipedismo dejó las manos libres para fabricar herramientas.|historia
evolución|e-vo-lu-ción|sustantivo femenino|Cambio gradual de los seres vivos a lo largo de muchas generaciones.|-|-|La evolución explica cómo cambian las especies.|historia
Paleolítico|pa-le-o-lí-ti-co|sustantivo masculino|Etapa de la prehistoria en que se usaban piedras talladas y se vivía de la caza.|-|Neolítico|En el Paleolítico los grupos eran nómadas.|historia
Neolítico|ne-o-lí-ti-co|sustantivo masculino|Etapa de la prehistoria en que aparecieron la agricultura y los pueblos.|-|Paleolítico|En el Neolítico se domesticaron animales.|historia
domesticación|do-mes-ti-ca-ción|sustantivo femenino|Proceso de acostumbrar a animales o plantas a vivir con las personas.|-|-|La domesticación del perro ayudó a cazar.|historia
excedente|ex-ce-den-te|sustantivo masculino|Cantidad que sobra después de cubrir lo necesario.|sobrante|escasez|Los agricultores guardaron el excedente de trigo.|historia
aldea|al-de-a|sustantivo femenino|Población pequeña, con pocas casas.|poblado|ciudad|La aldea tenía un pozo en el centro.|historia
fuente histórica|fuen-te his-tó-ri-ca|sustantivo femenino|Objeto, texto o relato que sirve para conocer el pasado.|-|-|Una carta antigua es una fuente histórica.|historia
fuente primaria|fuen-te pri-ma-ria|sustantivo femenino|Documento hecho en la época que se estudia.|-|fuente secundaria|Un diario de viaje es una fuente primaria.|historia
fuente secundaria|fuen-te se-cun-da-ria|sustantivo femenino|Texto que estudia el pasado a partir de otras fuentes.|-|fuente primaria|El libro de texto es una fuente secundaria.|historia
línea de tiempo|lí-ne-a de tiem-po|sustantivo femenino|Esquema que ubica los hechos en orden a lo largo del tiempo.|-|-|Dibujé una línea de tiempo de Roma.|historia
yacimiento|ya-ci-mien-to|sustantivo masculino|Lugar donde se encuentran restos del pasado o minerales.|-|-|En el yacimiento hallaron huesos de mamut.|historia
arte rupestre|ar-te ru-pes-tre|sustantivo masculino|Pinturas y grabados que se hacían en las rocas y en las cuevas.|-|-|El arte rupestre muestra animales cazados.|historia
fluvial|flu-vial|adjetivo|Que se relaciona con los ríos.|-|-|Las civilizaciones fluviales nacieron junto a ríos.|historia
delta|del-ta|sustantivo masculino|Terreno en forma de abanico donde un río se divide al llegar al mar.|-|-|El Nilo forma un delta fértil.|historia
crecida|cre-ci-da|sustantivo femenino|Subida del nivel de un río.|-|bajante|La crecida del río fertilizaba la tierra.|historia
limo|li-mo|sustantivo masculino|Barro fino que deja el agua y que abona la tierra.|-|-|El limo hizo fértiles las orillas.|historia
regadío|re-ga-dí-o|sustantivo masculino|Sistema de canales para llevar agua a los cultivos.|riego|secano|El regadío permitió cultivar en el desierto.|historia
Mesopotamia|me-so-po-ta-mia|nombre propio|Región de Asia entre los ríos Tigris y Éufrates, cuna de una de las primeras civilizaciones.|-|-|En Mesopotamia se inventó la escritura cuneiforme.|historia
cuneiforme|cu-nei-for-me|adjetivo|Dicho de la escritura antigua de signos con forma de cuña.|-|-|Los escribas grababan signos cuneiformes en tablillas.|historia
tablilla|ta-bli-lla|sustantivo femenino|Pieza pequeña y plana de arcilla o de madera donde se escribía.|-|-|La tablilla de arcilla guardaba una cuenta.|historia
zigurat|zi-gu-rat|sustantivo masculino|Torre escalonada de los templos de Mesopotamia.|-|-|El zigurat se alzaba en el centro de la ciudad.|historia
escriba|es-cri-ba|sustantivo masculino|Persona que escribía y llevaba las cuentas en las civilizaciones antiguas.|-|-|El escriba anotó las cosechas.|historia
faraón|fa-ra-ón|sustantivo masculino|Rey del antiguo Egipto, considerado hijo de los dioses.|-|-|El faraón gobernaba todo Egipto.|historia
momia|mo-mia|sustantivo femenino|Cuerpo conservado con técnicas especiales para que no se destruya.|-|-|Los egipcios preparaban la momia con vendas.|historia
papiro|pa-pi-ro|sustantivo masculino|Material para escribir hecho con una planta del Nilo.|-|-|Escribían los jeroglíficos en papiro.|historia
politeísmo|po-li-te-ís-mo|sustantivo masculino|Creencia en varios dioses.|-|monoteísmo|El politeísmo griego tenía dioses del mar y del trueno.|historia
monoteísmo|mo-no-te-ís-mo|sustantivo masculino|Creencia en un solo dios.|-|politeísmo|El judaísmo es una religión monoteísta.|historia
ciudad-estado|ciu-dad-es-ta-do|sustantivo femenino|Ciudad que tiene su propio gobierno y sus propias leyes.|-|-|Atenas fue una ciudad-estado.|historia
polis|po-lis|sustantivo femenino|Ciudad-estado de la Antigua Grecia.|-|-|Cada polis tenía sus propias leyes.|historia
ágora|á-go-ra|sustantivo femenino|Plaza pública de las ciudades griegas donde se reunía la gente.|plaza|-|Los ciudadanos debatían en el ágora.|historia
acrópolis|a-cró-po-lis|sustantivo femenino|Parte alta y fortificada de una antigua ciudad griega.|-|-|El Partenón se alza en la acrópolis de Atenas.|historia
oligarquía|o-li-gar-quí-a|sustantivo femenino|Gobierno en que mandan unos pocos.|-|democracia|En una oligarquía, pocas familias deciden.|historia
tiranía|ti-ra-ní-a|sustantivo femenino|Gobierno de una persona que manda sin respetar las leyes.|despotismo|democracia|La tiranía impide opinar con libertad.|historia
aristocracia|a-ris-to-cra-cia|sustantivo femenino|Gobierno o grupo de las familias más ricas y de mayor rango.|nobleza|-|La aristocracia poseía grandes tierras.|historia
ostracismo|os-tra-cis-mo|sustantivo masculino|En Atenas, destierro por votación de un ciudadano peligroso; hoy, aislamiento de alguien.|destierro|-|El ostracismo apartó al político de Atenas.|historia
cónsul|cón-sul|sustantivo masculino|Alto magistrado de la república romana, elegido por un año.|-|-|Dos cónsules gobernaban Roma.|historia
patricio|pa-tri-cio|sustantivo masculino|Miembro de las familias nobles de la antigua Roma.|aristócrata|plebeyo|Los patricios ocupaban los cargos más altos.|historia
plebeyo|ple-be-yo|sustantivo masculino|Persona del pueblo común en la antigua Roma.|-|patricio|Los plebeyos pidieron más derechos.|historia
legión|le-gión|sustantivo femenino|Gran unidad del ejército romano.|-|-|La legión marchó a la frontera.|historia
legionario|le-gio-na-rio|sustantivo masculino|Soldado de una legión romana.|-|-|El legionario portaba escudo y espada.|historia
calzada|cal-za-da|sustantivo femenino|Camino empedrado, como los que construyeron los romanos.|-|-|Las calzadas romanas unían todo el imperio.|historia
foro|fo-ro|sustantivo masculino|Plaza principal de una ciudad romana, centro de la vida pública.|-|-|En el foro se hacían negocios y discursos.|historia
coliseo|co-li-se-o|sustantivo masculino|Gran edificio romano de forma ovalada para espectáculos.|-|-|En el Coliseo luchaban los gladiadores.|historia
expansión|ex-pan-sión|sustantivo femenino|Crecimiento de un territorio, de un pueblo o de una idea.|extensión|reducción|La expansión romana llegó hasta Britania.|historia
dinastía|di-nas-tí-a|sustantivo femenino|Serie de gobernantes de una misma familia.|-|-|Una larga dinastía gobernó Egipto.|historia
reinado|rei-na-do|sustantivo masculino|Período en que gobierna un rey o una reina.|-|-|Su reinado duró treinta años.|historia
filosofía|fi-lo-so-fí-a|sustantivo femenino|Disciplina que busca responder preguntas profundas sobre la vida y el conocimiento.|-|-|La filosofía nació en Grecia.|historia
elecciones|e-lec-cio-nes|sustantivo femenino plural|Votación en que los ciudadanos escogen a sus autoridades.|comicios|-|Las elecciones se hacen en un domingo.|historia
partido político|par-ti-do po-lí-ti-co|sustantivo masculino|Grupo de personas con ideas comunes que busca participar en el gobierno.|-|-|Cada partido político presenta sus candidatos.|historia
clase social|cla-se so-cial|sustantivo femenino|Grupo de personas con un nivel parecido de riqueza y de poder.|-|-|En la antigua Roma había distintas clases sociales.|historia
casta|cas-ta|sustantivo femenino|Grupo social cerrado al que se pertenece por nacimiento.|estamento|-|Las castas casi no cambiaban de oficio.|historia
mapamundi|ma-pa-mun-di|sustantivo masculino|Mapa que muestra toda la superficie de la Tierra.|-|-|Busqué Egipto en el mapamundi.|geografía
cartografía|car-to-gra-fí-a|sustantivo femenino|Técnica y arte de hacer mapas.|-|-|La cartografía antigua era dibujada a mano.|geografía
huso horario|hu-so ho-ra-rio|sustantivo masculino|Franja de la Tierra con la misma hora.|-|-|Chile y España tienen distinto huso horario.|geografía
zona climática|zo-na cli-má-ti-ca|sustantivo femenino|Franja de la Tierra con un clima parecido.|-|-|La zona climática templada tiene cuatro estaciones.|geografía
estrecho|es-tre-cho|sustantivo masculino|Paso angosto de mar entre dos tierras.|paso|-|El estrecho de Magallanes une dos océanos.|geografía
cabo|ca-bo|sustantivo masculino|Punta de tierra que entra en el mar.|punta|-|El navegante dobló el cabo con cuidado.|geografía
vertiente|ver-tien-te|sustantivo femenino|Ladera o pendiente de una montaña por donde baja el agua.|ladera|-|Esa vertiente de la cordillera tiene nieve todo el año.|geografía
oasis|o-a-sis|sustantivo masculino|Lugar con agua y plantas en medio de un desierto.|-|-|La caravana descansó en un oasis.|geografía
ámbito|ám-bi-to|sustantivo masculino|Espacio o campo de actividad en que algo ocurre.|campo|-|En el ámbito deportivo, el esfuerzo es clave.|vocabulario académico
indicador|in-di-ca-dor|sustantivo masculino|Dato que muestra cómo va algo.|señal|-|La nota promedio es un indicador de avance.|vocabulario académico
parámetro|pa-rá-me-tro|sustantivo masculino|Dato fijo que sirve como referencia para analizar algo.|-|-|El parámetro de calidad es cumplir las normas.|vocabulario académico
supuesto|su-pues-to|sustantivo masculino|Idea que se da por cierta sin haberla probado.|suposición|-|Partimos de un supuesto que debemos revisar.|vocabulario académico
premisa|pre-mi-sa|sustantivo femenino|Idea de partida de la que se saca una conclusión.|-|conclusión|Si la premisa es falsa, la conclusión falla.|vocabulario académico
deducción|de-duc-ción|sustantivo femenino|Razonamiento que va de lo general a lo particular.|-|inducción|La deducción me llevó a una respuesta lógica.|vocabulario académico
inducción|in-duc-ción|sustantivo femenino|Razonamiento que va de casos particulares a una idea general.|-|deducción|Por inducción, sacamos una regla de varios ejemplos.|vocabulario académico
noción|no-ción|sustantivo femenino|Idea básica o conocimiento inicial sobre algo.|idea|-|Tengo una noción de cómo funciona.|vocabulario académico
categoría|ca-te-go-rí-a|sustantivo femenino|Grupo en el que se clasifican cosas con rasgos comunes.|clase|-|Agrupé los libros por categoría.|vocabulario académico
vínculo|vín-cu-lo|sustantivo masculino|Unión o relación entre personas o cosas.|lazo|-|Hay un vínculo entre salud y alimentación.|vocabulario académico
antecedente|an-te-ce-den-te|sustantivo masculino|Hecho anterior que ayuda a entender algo posterior.|-|consecuencia|Los antecedentes de la guerra se remontan a años atrás.|vocabulario académico
repercusión|re-per-cu-sión|sustantivo femenino|Efecto que algo produce más allá de sí mismo.|consecuencia|-|La noticia tuvo gran repercusión.|vocabulario académico
controversia|con-tro-ver-sia|sustantivo femenino|Discusión larga entre personas con opiniones opuestas.|polémica|-|El proyecto generó controversia en el barrio.|vocabulario académico
desacuerdo|de-sa-cuer-do|sustantivo masculino|Falta de coincidencia entre opiniones.|discrepancia|acuerdo|Hubo un desacuerdo sobre el horario.|vocabulario académico
conciliación|con-ci-lia-ción|sustantivo femenino|Acuerdo logrado entre personas enfrentadas.|reconciliación|-|La conciliación terminó la pelea.|vocabulario académico
asertividad|a-ser-ti-vi-dad|sustantivo femenino|Capacidad de expresar lo que uno piensa de modo claro y respetuoso.|-|-|La asertividad ayuda a resolver conflictos.|orientación
pertenencia|per-te-nen-cia|sustantivo femenino|Sentimiento de ser parte de un grupo.|-|-|Sentimos pertenencia a nuestro curso.|orientación
aptitud|ap-ti-tud|sustantivo femenino|Capacidad natural para hacer bien algo.|talento|-|Tiene aptitud para el dibujo.|orientación
rendimiento|ren-di-mien-to|sustantivo masculino|Resultado que se obtiene en relación con el esfuerzo realizado.|desempeño|-|Mejoró su rendimiento escolar.|orientación
desempeño|de-sem-pe-ño|sustantivo masculino|Forma en que alguien cumple su tarea o su trabajo.|rendimiento|-|Su desempeño en el equipo fue destacado.|orientación
instancia|ins-tan-cia|sustantivo femenino|Momento o etapa dentro de un proceso.|etapa|-|La final es la última instancia del torneo.|vocabulario académico
restricción|res-tric-ción|sustantivo femenino|Límite que se pone a algo.|límite|libertad|Hay una restricción de edad para entrar.|vocabulario académico
normativa|nor-ma-ti-va|sustantivo femenino|Conjunto de normas que regulan una actividad.|-|-|La normativa del colegio prohíbe correr en los pasillos.|vocabulario académico
sanción|san-ción|sustantivo femenino|Castigo o medida que se aplica a quien rompe una norma.|castigo|-|La sanción fue una advertencia escrita.|vocabulario académico
irrelevante|i-rre-le-van-te|adjetivo|Que no importa o no aporta nada al asunto.|trivial|relevante|El color de la hoja es irrelevante.|vocabulario académico
pertinente|per-ti-nen-te|adjetivo|Que viene al caso y tiene relación con lo que se trata.|adecuado|impertinente|Tu comentario es pertinente.|vocabulario académico
consistente|con-sis-ten-te|adjetivo|Firme y sin contradicciones.|sólido|débil|Presentó un argumento consistente.|vocabulario académico
riguroso|ri-gu-ro-so|adjetivo|Que se hace con exactitud y mucho cuidado.|exigente|descuidado|Hizo un análisis riguroso.|vocabulario académico
arbitrario|ar-bi-tra-rio|adjetivo|Que se decide por capricho y sin una razón justa.|caprichoso|justo|Fue una decisión arbitraria.|vocabulario académico
explícito|ex-plí-ci-to|adjetivo|Que se dice de forma clara y directa.|claro|implícito|La instrucción es explícita.|vocabulario académico
implícito|im-plí-ci-to|adjetivo|Que se entiende sin que se diga directamente.|tácito|explícito|Su tristeza estaba implícita en sus palabras.|vocabulario académico
figurado|fi-gu-ra-do|adjetivo|Dicho de un sentido que no es el literal y se usa como imagen.|metafórico|literal|«Tener un corazón de oro» está en sentido figurado.|vocabulario académico
específico|es-pe-cí-fi-co|adjetivo|Que se refiere a algo determinado y no a algo en general.|preciso|general|Busco un dato específico.|vocabulario académico
particular|par-ti-cu-lar|adjetivo|Propio de una persona o de un caso, y distinto del resto.|singular|general|Cada animal tiene un rasgo particular.|vocabulario académico
general|ge-ne-ral|adjetivo|Que abarca a todos o a la mayoría.|común|particular|Dame una idea general del texto.|vocabulario académico
simple|sim-ple|adjetivo|Sin complicaciones y fácil de entender.|sencillo|complejo|Elegí un diseño simple.|vocabulario académico
fundamental|fun-da-men-tal|adjetivo|Que sirve de base y es muy importante.|esencial|secundario|Dormir bien es fundamental.|vocabulario académico
prioritario|prio-ri-ta-rio|adjetivo|Que debe atenderse antes que otras cosas.|urgente|secundario|Terminar la tarea es prioritario.|vocabulario académico
urgente|ur-gen-te|adjetivo|Que necesita hacerse de inmediato.|apremiante|postergable|Necesito una respuesta urgente.|vocabulario académico
progresivo|pro-gre-si-vo|adjetivo|Que avanza poco a poco.|gradual|brusco|Hubo un aumento progresivo de la temperatura.|vocabulario académico
paulatino|pau-la-ti-no|adjetivo|Que se produce despacio y de manera continua.|gradual|repentino|Notamos una mejora paulatina.|vocabulario académico
ocasional|o-ca-sio-nal|adjetivo|Que ocurre de vez en cuando.|esporádico|frecuente|Tuvimos una lluvia ocasional.|vocabulario académico
indispensable|in-dis-pen-sa-ble|adjetivo|Que es absolutamente necesario.|imprescindible|prescindible|El agua es indispensable para vivir.|vocabulario académico
innecesario|in-ne-ce-sa-rio|adjetivo|Que no hace falta.|superfluo|necesario|Fue un gasto innecesario.|vocabulario académico
suficiente|su-fi-cien-te|adjetivo|Que alcanza para lo que se necesita.|bastante|insuficiente|Tenemos tiempo suficiente.|vocabulario académico
insuficiente|in-su-fi-cien-te|adjetivo|Que no alcanza para lo que se necesita.|escaso|suficiente|El agua era insuficiente para todos.|vocabulario académico
excesivo|ex-ce-si-vo|adjetivo|Que se pasa de lo normal o de lo necesario.|exagerado|moderado|Hacía un calor excesivo.|vocabulario académico
moderado|mo-de-ra-do|adjetivo|Que no llega a los extremos.|templado|excesivo|Hizo ejercicio moderado.|vocabulario académico
razonable|ra-zo-na-ble|adjetivo|Que es justo, lógico o aceptable.|sensato|absurdo|El precio es razonable.|vocabulario académico
imprudente|im-pru-den-te|adjetivo|Que actúa sin pensar en los riesgos.|temerario|prudente|Cruzar sin mirar es imprudente.|vocabulario académico
impulsivo|im-pul-si-vo|adjetivo|Que actúa sin pensar, llevado por lo que siente.|irreflexivo|reflexivo|Fue impulsivo y habló sin pensar.|orientación
reflexivo|re-fle-xi-vo|adjetivo|Que piensa con calma antes de actuar.|pensativo|impulsivo|Es una persona reflexiva.|orientación
irresponsable|i-rres-pon-sa-ble|adjetivo|Que no cumple con sus deberes.|descuidado|responsable|Olvidar la tarea es irresponsable.|orientación
autónomo|au-tó-no-mo|adjetivo|Que puede hacer las cosas sin depender de otros.|independiente|dependiente|Soy autónomo para ir al colegio.|orientación
independiente|in-de-pen-dien-te|adjetivo|Que no necesita de otros para actuar o decidir.|autónomo|dependiente|Es un joven independiente.|orientación
dependiente|de-pen-dien-te|adjetivo|Que necesita de otros para actuar o mantenerse.|-|independiente|El bebé es dependiente de sus padres.|orientación
resiliente|re-si-lien-te|adjetivo|Que se recupera bien después de una situación difícil.|-|-|Un niño resiliente supera las pérdidas.|orientación
optimista|op-ti-mis-ta|adjetivo|Que ve el lado bueno de las cosas.|positivo|pesimista|Es optimista y cree que saldrá bien.|orientación
pesimista|pe-si-mis-ta|adjetivo|Que espera siempre lo peor.|negativo|optimista|Fue pesimista sobre el resultado.|orientación
inseguro|in-se-gu-ro|adjetivo|Que duda de sí mismo o que no ofrece garantías.|-|seguro|Me siento inseguro al hablar en público.|orientación
inicialmente|i-ni-cial-men-te|adverbio|Al comienzo.|al principio|finalmente|Inicialmente dudé, pero luego acepté.|vocabulario académico
posteriormente|pos-te-rior-men-te|adverbio|Más tarde, después de algo.|después|anteriormente|Posteriormente se aprobó la ley.|vocabulario académico
previamente|pre-via-men-te|adverbio|Antes de algo.|antes|posteriormente|Lee previamente las instrucciones.|vocabulario académico
simultáneamente|si-mul-tá-nea-men-te|adverbio|Al mismo tiempo.|a la vez|-|Dos equipos jugaron simultáneamente.|vocabulario académico
paulatinamente|pau-la-ti-na-men-te|adverbio|De manera lenta y continua.|gradualmente|bruscamente|Se acostumbró paulatinamente al frío.|vocabulario académico
necesariamente|ne-ce-sa-ria-men-te|adverbio|Por obligación, sin otra opción.|forzosamente|-|No siempre es necesariamente cierto.|vocabulario académico
evidentemente|e-vi-den-te-men-te|adverbio|De manera clara y sin dudas.|claramente|-|Evidentemente, él tenía razón.|vocabulario académico
claramente|cla-ra-men-te|adverbio|De manera que se entiende sin duda.|nítidamente|confusamente|Habló claramente.|vocabulario académico
directamente|di-rec-ta-men-te|adverbio|Sin rodeos y sin pasar por otro.|-|indirectamente|Fui directamente a casa.|vocabulario académico
indirectamente|in-di-rec-ta-men-te|adverbio|Por un camino distinto del directo.|-|directamente|Me enteré indirectamente.|vocabulario académico
constantemente|cons-tan-te-men-te|adverbio|Sin parar y de modo continuo.|siempre|-|Practica constantemente.|vocabulario académico
frecuentemente|fre-cuen-te-men-te|adverbio|Muchas veces.|a menudo|raramente|Frecuentemente voy a la biblioteca.|vocabulario académico
eventualmente|e-ven-tual-men-te|adverbio|De vez en cuando o si llega a ocurrir.|-|-|Eventualmente hay cortes de agua.|vocabulario académico
exclusivamente|ex-clu-si-va-men-te|adverbio|Solo y únicamente.|solamente|-|Este patio es exclusivamente para los pequeños.|vocabulario académico
prácticamente|prác-ti-ca-men-te|adverbio|Casi del todo.|casi|-|Prácticamente terminé la tarea.|vocabulario académico
parcialmente|par-cial-men-te|adverbio|Solo en parte.|en parte|totalmente|El cielo estaba parcialmente nublado.|vocabulario académico
software|soft-wa-re|sustantivo masculino|Conjunto de programas y datos que hacen funcionar un equipo.|programa|hardware|Instalé un software para editar fotos.|tecnología
hardware|hard-wa-re|sustantivo masculino|Partes físicas de un computador, como la pantalla o el teclado.|equipo|software|El hardware incluye el disco y el procesador.|tecnología
procesador|pro-ce-sa-dor|sustantivo masculino|Parte del computador que ejecuta las instrucciones.|-|-|El procesador hace funcionar los programas.|tecnología
plataforma|pla-ta-for-ma|sustantivo femenino|Sistema digital donde se usan servicios o contenidos.|-|-|Entregamos la tarea en la plataforma del colegio.|tecnología
red social|red so-cial|sustantivo femenino|Sitio de internet donde las personas se comunican y comparten contenidos.|-|-|Cuidé mis datos en la red social.|tecnología
antivirus|an-ti-vi-rus|sustantivo masculino|Programa que protege el computador de programas dañinos.|-|-|El antivirus detectó un archivo peligroso.|tecnología
cortafuegos|cor-ta-fue-gos|sustantivo masculino|Sistema que bloquea accesos no deseados a una red.|-|-|El cortafuegos frenó un acceso sospechoso.|tecnología
huella digital|hue-lla di-gi-tal|sustantivo femenino|Rastro de datos que deja una persona al usar internet.|-|-|Mi huella digital incluye mis comentarios.|tecnología
derechos de autor|de-re-chos de au-tor|sustantivo masculino plural|Derechos que tiene quien crea una obra sobre su uso y copia.|-|-|Respeto los derechos de autor al citar una imagen.|tecnología
automatización|au-to-ma-ti-za-ción|sustantivo femenino|Uso de máquinas para hacer tareas sin ayuda de personas.|-|-|La automatización acelera la producción.|tecnología
innovación|in-no-va-ción|sustantivo femenino|Cambio que trae algo nuevo y útil.|novedad|-|Esta innovación ahorra agua.|tecnología
ergonomía|er-go-no-mí-a|sustantivo femenino|Estudio de cómo adaptar objetos al cuerpo para usarlos cómodamente.|-|-|La ergonomía mejora el diseño de las sillas.|tecnología
fotomontaje|fo-to-mon-ta-je|sustantivo masculino|Imagen creada uniendo partes de varias fotografías.|-|-|Hice un fotomontaje con paisajes distintos.|artes
vanguardia|van-guar-dia|sustantivo femenino|Movimiento artístico que rompe con las normas anteriores.|-|-|La vanguardia cambió la manera de pintar.|artes
énfasis|én-fa-sis|sustantivo masculino|Fuerza especial que se da a algo para destacarlo.|realce|-|El artista puso énfasis en el color rojo.|artes
curador|cu-ra-dor|sustantivo masculino|Persona que elige y organiza las obras de una exposición.|-|-|La curadora eligió veinte pinturas.|artes
redonda|re-don-da|sustantivo femenino|Figura musical de mayor duración, que vale cuatro tiempos.|-|-|La redonda dura cuatro pulsos.|música
solfeo|sol-fe-o|sustantivo masculino|Práctica de leer música diciendo el nombre de las notas.|-|-|Aprendí solfeo en clases de música.|música
trío|trí-o|sustantivo masculino|Grupo de tres músicos o pieza para tres voces o instrumentos.|-|-|El trío tocó un vals.|música
ostinato|os-ti-na-to|sustantivo masculino|Frase musical que se repite una y otra vez.|-|-|El ostinato del bombo sostenía la canción.|música
género musical|gé-ne-ro mu-si-cal|sustantivo masculino|Grupo de canciones con rasgos parecidos de ritmo y estilo.|-|-|El rock es un género musical.|música
jazz|jazz|sustantivo masculino|Género de música con improvisación y ritmos libres.|-|-|El jazz nació en Estados Unidos.|música
pifilca|pi-fil-ca|sustantivo femenino|Flauta tradicional mapuche.|-|-|La pifilca emite un sonido agudo.|música
capacidad aeróbica|ca-pa-ci-dad a-e-ró-bi-ca|sustantivo femenino|Habilidad del cuerpo para hacer ejercicio por mucho rato.|-|-|Mejoré mi capacidad aeróbica trotando.|educación física
frecuencia cardíaca|fre-cuen-cia car-día-ca|sustantivo femenino|Número de latidos del corazón en un minuto.|pulsaciones|-|Mi frecuencia cardíaca sube al correr.|educación física
anaeróbico|a-na-e-ró-bi-co|adjetivo|Dicho del ejercicio corto e intenso que no depende del oxígeno.|-|aeróbico|La carrera de velocidad es un ejercicio anaeróbico.|educación física
calambre|ca-lam-bre|sustantivo masculino|Contracción dolorosa y repentina de un músculo.|-|-|Un calambre me detuvo en la carrera.|educación física
primeros auxilios|pri-me-ros au-xi-lios|sustantivo masculino plural|Ayuda inmediata que se da a una persona herida o enferma antes de que llegue un médico.|-|-|Aprendí primeros auxilios en el colegio.|educación física
reanimación|re-a-ni-ma-ción|sustantivo femenino|Maniobra para hacer que alguien vuelva a respirar o a tener latidos.|-|-|La reanimación debe hacerla alguien capacitado.|educación física
remate|re-ma-te|sustantivo masculino|Golpe final que se da a la pelota para anotar.|-|-|Su remate entró en el ángulo del arco.|educación física
saque|sa-que|sustantivo masculino|Golpe con que se inicia una jugada.|-|-|El saque de la volea cruzó la red.|educación física
drible|dri-ble|sustantivo masculino|Movimiento para esquivar a un rival con la pelota.|regate|-|Hizo un drible y pasó la pelota.|educación física
deportividad|de-por-ti-vi-dad|sustantivo femenino|Comportamiento justo y respetuoso al competir.|-|-|La deportividad se nota al saludar al rival.|educación física
rivalidad|ri-va-li-dad|sustantivo femenino|Competencia entre personas o equipos que quieren ganar.|-|-|Hay rivalidad sana entre los dos cursos.|educación física
campeonato|cam-pe-o-na-to|sustantivo masculino|Competencia deportiva para decidir quién es el mejor.|torneo|-|Ganamos el campeonato de la escuela.|educación física
ciclismo|ci-clis-mo|sustantivo masculino|Deporte o actividad de andar en bicicleta.|-|-|El ciclismo fortalece las piernas.|educación física
entrenamiento|en-tre-na-mien-to|sustantivo masculino|Preparación repetida para mejorar en un deporte.|práctica|-|El entrenamiento es los martes.|educación física
deportista|de-por-tis-ta|sustantivo masculino y femenino|Persona que practica un deporte.|atleta|-|La deportista ganó una medalla.|educación física
entrenador|en-tre-na-dor|sustantivo masculino|Persona que prepara a un deportista o a un equipo.|-|-|El entrenador corrigió mi postura.|educación física
repetición|re-pe-ti-ción|sustantivo femenino|Cada vez que se hace un ejercicio de una serie.|-|-|Hice diez repeticiones de sentadillas.|educación física
recuperación|re-cu-pe-ra-ción|sustantivo femenino|Vuelta a un buen estado después de un esfuerzo o enfermedad.|-|-|La recuperación exige descanso.|educación física
ingreso|in-gre-so|sustantivo masculino|Dinero que una persona o familia recibe.|-|gasto|El ingreso de la familia alcanzó para el mes.|vida cotidiana
garantía|ga-ran-tí-a|sustantivo femenino|Compromiso de arreglar o cambiar un producto que falla.|-|-|La garantía cubre un año.|vida cotidiana
factura|fac-tu-ra|sustantivo femenino|Documento que detalla una compra entre empresas.|-|-|La empresa pidió una factura.|vida cotidiana
choro|cho-ro|adjetivo|(uso en Chile) Que impresiona por ser muy bueno o audaz.|genial|-|Tu truco con el skate es choro.|vida cotidiana
caleta|ca-le-ta|locución adverbial|(uso en Chile) Mucho o gran cantidad.|mucho|poco|Había caleta de gente en el estadio.|vida cotidiana
pega|pe-ga|sustantivo femenino|(uso en Chile) Trabajo u ocupación.|trabajo|-|Mi mamá salió temprano a la pega.|vida cotidiana
sobremesa|so-bre-me-sa|sustantivo femenino|Rato de conversación después de comer, sin levantarse de la mesa.|-|-|Disfrutamos la sobremesa con mis abuelos.|vida cotidiana
vecindad|ve-cin-dad|sustantivo femenino|Conjunto de personas que viven cerca unas de otras.|-|-|La vecindad organizó una feria.|vida cotidiana
trayecto|tra-yec-to|sustantivo masculino|Camino que se recorre de un lugar a otro.|recorrido|-|El trayecto al colegio dura diez minutos.|vida cotidiana
itinerario|i-ti-ne-ra-rio|sustantivo masculino|Descripción del camino y de las paradas de un viaje.|ruta|-|Revisamos el itinerario del paseo.|vida cotidiana
desechable|de-se-cha-ble|adjetivo|Que se usa una vez y se bota.|-|reciclable|Evito los vasos desechables.|vida cotidiana
carga eléctrica|car-ga e-léc-tri-ca|sustantivo femenino|Propiedad de la materia que hace que los cuerpos se atraigan o se rechacen.|-|-|Frotar un globo le da carga eléctrica.|ciencias
amperio|am-pe-rio|sustantivo masculino|Unidad con que se mide la intensidad de la corriente eléctrica.|-|-|El enchufe soporta diez amperios.|ciencias
magnetismo|mag-ne-tis-mo|sustantivo masculino|Fuerza con que los imanes atraen algunos metales.|-|-|El magnetismo mantiene pegado el imán al refrigerador.|ciencias
campo magnético|cam-po mag-né-ti-co|sustantivo masculino|Zona alrededor de un imán donde se siente su fuerza.|-|-|La brújula se orienta con el campo magnético terrestre.|ciencias
macronutriente|ma-cro-nu-trien-te|sustantivo masculino|Nutriente que el cuerpo necesita en grandes cantidades, como los carbohidratos.|-|micronutriente|Las proteínas son un macronutriente.|ciencias
micronutriente|mi-cro-nu-trien-te|sustantivo masculino|Nutriente que el cuerpo necesita en cantidades muy pequeñas, como las vitaminas.|-|macronutriente|El hierro es un micronutriente.|ciencias
lípido|lí-pi-do|sustantivo masculino|Nutriente graso que da energía y protege el cuerpo.|grasa|-|El aceite de oliva contiene lípidos.|ciencias
metabolismo|me-ta-bo-lis-mo|sustantivo masculino|Conjunto de cambios químicos que ocurren en el cuerpo para usar los alimentos.|-|-|Hacer ejercicio acelera el metabolismo.|ciencias
apetito|a-pe-ti-to|sustantivo masculino|Ganas de comer.|hambre|inapetencia|Después de nadar tengo mucho apetito.|ciencias
saciedad|sa-cie-dad|sustantivo femenino|Sensación de estar satisfecho después de comer.|-|hambre|La fibra aumenta la saciedad.|ciencias
sistema circulatorio|sis-te-ma cir-cu-la-to-rio|sustantivo masculino|Conjunto de órganos que llevan la sangre por el cuerpo.|-|-|El corazón es parte del sistema circulatorio.|ciencias
sistema respiratorio|sis-te-ma res-pi-ra-to-rio|sustantivo masculino|Conjunto de órganos que permiten tomar oxígeno y expulsar dióxido de carbono.|-|-|Los pulmones forman parte del sistema respiratorio.|ciencias
sistema digestivo|sis-te-ma di-ges-ti-vo|sustantivo masculino|Conjunto de órganos que transforman los alimentos y absorben sus nutrientes.|-|-|El estómago pertenece al sistema digestivo.|ciencias
sistema nervioso|sis-te-ma ner-vio-so|sustantivo masculino|Conjunto de órganos que reciben información y controlan el cuerpo.|-|-|El cerebro dirige el sistema nervioso.|ciencias
sistema inmune|sis-te-ma in-mu-ne|sustantivo masculino|Conjunto de células y órganos que defienden al cuerpo de los microbios.|-|-|El sistema inmune combate los virus.|ciencias
hemoglobina|he-mo-glo-bi-na|sustantivo femenino|Sustancia de los glóbulos rojos que transporta el oxígeno.|-|-|La hemoglobina da el color rojo a la sangre.|ciencias
aorta|a-or-ta|sustantivo femenino|Arteria principal que sale del corazón.|-|-|La aorta lleva sangre a todo el cuerpo.|ciencias
aurícula|au-rí-cu-la|sustantivo femenino|Cavidad superior del corazón que recibe la sangre.|-|ventrículo|La sangre entra por la aurícula.|ciencias
ventrículo|ven-trí-cu-lo|sustantivo masculino|Cavidad inferior del corazón que impulsa la sangre.|-|aurícula|El ventrículo bombea sangre hacia las arterias.|ciencias
válvula|vál-vu-la|sustantivo femenino|Pieza que deja pasar un líquido en un solo sentido.|-|-|Las válvulas del corazón evitan que la sangre retroceda.|ciencias
linfocito|lin-fo-ci-to|sustantivo masculino|Glóbulo blanco que ayuda a defender el cuerpo.|-|-|Los linfocitos producen anticuerpos.|ciencias
antígeno|an-tí-ge-no|sustantivo masculino|Sustancia extraña que activa las defensas del cuerpo.|-|-|El anticuerpo reconoce el antígeno.|ciencias
patógeno|pa-tó-ge-no|sustantivo masculino|Microbio capaz de provocar una enfermedad.|-|-|Los virus son patógenos.|ciencias
elemento químico|e-le-men-to quí-mi-co|sustantivo masculino|Sustancia hecha de un solo tipo de átomo.|-|-|El oxígeno es un elemento químico.|ciencias
tabla periódica|ta-bla pe-rió-di-ca|sustantivo femenino|Cuadro que ordena todos los elementos químicos.|-|-|Busqué el hierro en la tabla periódica.|ciencias
soluto|so-lu-to|sustantivo masculino|Sustancia que se disuelve en otra.|-|solvente|La sal es el soluto del agua salada.|ciencias
solvente|sol-ven-te|sustantivo masculino|Sustancia en la que se disuelve otra.|disolvente|soluto|El agua es el solvente más común.|ciencias
disolución|di-so-lu-ción|sustantivo femenino|Mezcla uniforme de un soluto en un solvente.|-|-|Preparé una disolución de azúcar.|ciencias
neutro|neu-tro|adjetivo|Que no es ácido ni básico.|-|-|El agua pura es neutra.|ciencias
oxidación|o-xi-da-ción|sustantivo femenino|Reacción en que una sustancia se combina con oxígeno, como cuando se oxida el hierro.|-|-|La oxidación cubre el clavo de óxido.|ciencias
combustión|com-bus-tión|sustantivo femenino|Reacción en que algo arde al combinarse con oxígeno y libera calor.|-|-|La combustión de la leña produce calor.|ciencias
reacción química|re-ac-ción quí-mi-ca|sustantivo femenino|Proceso en que unas sustancias se transforman en otras.|-|-|El pan que se hornea es una reacción química.|ciencias
reactante|re-ac-tan-te|sustantivo masculino|Sustancia que participa en una reacción química al inicio.|-|-|El vinagre y el bicarbonato son reactantes.|ciencias
catalizador|ca-ta-li-za-dor|sustantivo masculino|Sustancia que acelera una reacción sin gastarse.|-|-|El catalizador hizo la reacción más rápida.|ciencias
inflamable|in-fla-ma-ble|adjetivo|Que se prende fácilmente y arde rápido.|-|ininflamable|El alcohol es inflamable.|ciencias
corrosivo|co-rro-si-vo|adjetivo|Que destruye poco a poco otras sustancias al tocarlas.|-|-|El ácido fuerte es corrosivo.|ciencias
decantación|de-can-ta-ción|sustantivo femenino|Método que separa un líquido de un sólido que se asienta o dos líquidos que no se mezclan.|-|-|Separamos aceite y agua por decantación.|ciencias
filtración|fil-tra-ción|sustantivo femenino|Método para separar un sólido de un líquido con un filtro.|-|-|Usé papel filtro para la filtración.|ciencias
destilación|des-ti-la-ción|sustantivo femenino|Método que separa líquidos usando la evaporación y la condensación.|-|-|La destilación permite obtener agua pura.|ciencias
tamizado|ta-mi-za-do|sustantivo masculino|Método para separar sólidos de distinto tamaño con un colador.|-|-|El tamizado separó la harina de los grumos.|ciencias
cristalización|cris-ta-li-za-ción|sustantivo femenino|Formación de cristales a partir de una disolución.|-|-|La sal se obtiene por cristalización.|ciencias
heterogéneo|he-te-ro-gé-ne-o|adjetivo|Dicho de una mezcla en que se distinguen sus partes.|-|homogéneo|La ensalada es una mezcla heterogénea.|ciencias
homogéneo|ho-mo-gé-ne-o|adjetivo|Dicho de una mezcla en que no se distinguen sus partes.|uniforme|heterogéneo|El agua con azúcar es homogénea.|ciencias
sistema solar|sis-te-ma so-lar|sustantivo masculino|Conjunto formado por el Sol y los astros que giran a su alrededor.|-|-|La Tierra pertenece al sistema solar.|ciencias
planeta enano|pla-ne-ta e-na-no|sustantivo masculino|Astro redondo que gira alrededor del Sol, pero más pequeño que un planeta.|-|-|Plutón es un planeta enano.|ciencias
estación del año|es-ta-ción del a-ño|sustantivo femenino|Cada una de las cuatro épocas del año con clima propio.|-|-|El otoño es una estación del año.|ciencias
fases lunares|fa-ses lu-na-res|sustantivo femenino plural|Distintas formas con que vemos la Luna a lo largo del mes.|-|-|Dibujé las fases lunares durante un mes.|ciencias
luna llena|lu-na lle-na|sustantivo femenino|Fase en que vemos la Luna completamente iluminada.|-|luna nueva|La luna llena alumbró el camino.|ciencias
luna nueva|lu-na nue-va|sustantivo femenino|Fase en que la Luna casi no se ve.|-|luna llena|En luna nueva el cielo está más oscuro.|ciencias
año luz|a-ño luz|sustantivo masculino|Distancia que recorre la luz en un año.|-|-|La estrella está a cuatro años luz.|ciencias
mareas|ma-re-as|sustantivo femenino plural|Subida y bajada del nivel del mar causada sobre todo por la Luna.|-|-|Con la marea alta el agua cubre la arena.|ciencias
fotón|fo-tón|sustantivo masculino|Partícula mínima de la luz.|-|-|La luz está formada por fotones.|ciencias
dióxido de carbono|dió-xi-do de car-bo-no|sustantivo masculino|Gas que expulsamos al respirar y que absorben las plantas.|-|-|Las plantas absorben dióxido de carbono.|ciencias
glucosa|glu-co-sa|sustantivo femenino|Azúcar que las plantas producen en la fotosíntesis y que da energía al cuerpo.|-|-|Las células usan la glucosa como energía.|ciencias
estoma|es-to-ma|sustantivo masculino|Pequeña abertura de las hojas por donde entra y sale el aire.|-|-|Los estomas se abren para dejar pasar gases.|ciencias
savia|sa-via|sustantivo femenino|Líquido que circula por el interior de las plantas.|-|-|La savia lleva agua y nutrientes por el tallo.|ciencias
transpiración|trans-pi-ra-ción|sustantivo femenino|Pérdida de agua en forma de vapor por la piel o las hojas.|sudoración|-|La transpiración enfría el cuerpo.|ciencias
carroñero|ca-rro-ñe-ro|sustantivo masculino|Animal que se alimenta de animales muertos.|-|-|El cóndor es un carroñero.|ciencias
extinto|ex-tin-to|adjetivo|Dicho de una especie que ya no existe.|desaparecido|vivo|El mamut es un animal extinto.|ciencias
amenazado|a-me-na-za-do|adjetivo|Dicho de una especie que está en peligro de desaparecer.|-|-|El huemul es un animal amenazado.|ciencias
selección natural|se-lec-ción na-tu-ral|sustantivo femenino|Proceso en que sobreviven los seres vivos mejor adaptados.|-|-|La selección natural explica por qué cambian las especies.|ciencias
mutación|mu-ta-ción|sustantivo femenino|Cambio en el material genético de un ser vivo.|-|-|Una mutación puede cambiar el color del pelaje.|ciencias
cigoto|ci-go-to|sustantivo masculino|Primera célula que se forma cuando se unen el óvulo y el espermatozoide.|-|-|El cigoto se divide para formar el embrión.|ciencias
menstruación|mens-trua-ción|sustantivo femenino|Pérdida mensual de sangre y tejido del útero en las mujeres.|-|-|La menstruación forma parte del ciclo mensual.|ciencias
caracteres sexuales|ca-rac-te-res se-xua-les|sustantivo masculino plural|Rasgos del cuerpo que cambian en la pubertad y distinguen a mujeres y a hombres.|-|-|El vello es un carácter sexual secundario.|ciencias
estirón|es-ti-rón|sustantivo masculino|Crecimiento rápido de la estatura durante la pubertad.|-|-|Mi hermano dio el estirón este año.|ciencias
acné|ac-né|sustantivo masculino|Granitos que aparecen en la piel durante la adolescencia.|-|-|El acné suele aparecer en la pubertad.|ciencias
afectividad|a-fec-ti-vi-dad|sustantivo femenino|Capacidad de sentir y mostrar cariño y emociones.|-|-|La afectividad crece con el trato respetuoso.|orientación
derrumbe|de-rrum-be|sustantivo masculino|Caída de tierra o de rocas desde un cerro.|desprendimiento|-|Un derrumbe cortó el camino.|ciencias
cenizas|ce-ni-zas|sustantivo femenino plural|Polvo gris que queda después de quemar algo.|-|-|El volcán lanzó cenizas al aire.|ciencias
placa de Nazca|pla-ca de Naz-ca|sustantivo femenino|Placa tectónica del océano Pacífico que choca contra Sudamérica.|-|-|La placa de Nazca se hunde bajo Chile.|ciencias
hipocentro|hi-po-cen-tro|sustantivo masculino|Punto bajo tierra donde nace un sismo.|foco|epicentro|El hipocentro estaba a treinta kilómetros de profundidad.|ciencias
escala de Richter|es-ca-la de Rich-ter|sustantivo femenino|Escala que mide la magnitud de un sismo.|-|-|El sismo alcanzó siete grados en la escala de Richter.|ciencias
plan de evacuación|plan de e-va-cua-ción|sustantivo masculino|Instrucciones que dicen cómo salir de un lugar en una emergencia.|-|-|Practicamos el plan de evacuación del colegio.|ciencias
tribuno|tri-bu-no|sustantivo masculino|En la antigua Roma, magistrado que defendía los derechos de los plebeyos.|-|-|El tribuno protegió a los plebeyos.|historia
dictador|dic-ta-dor|sustantivo masculino|En la antigua Roma, magistrado con poder total por un tiempo corto; hoy, gobernante que manda sin límites.|-|-|El dictador romano tenía poder por seis meses.|historia
latifundio|la-ti-fun-dio|sustantivo masculino|Propiedad agrícola muy extensa que pertenece a un solo dueño.|-|minifundio|Los latifundios eran trabajados por esclavos.|historia
bárbaro|bár-ba-ro|sustantivo masculino|Nombre que daban los romanos a los pueblos que vivían fuera de su imperio.|-|-|Los bárbaros cruzaron las fronteras de Roma.|historia
invasión|in-va-sión|sustantivo femenino|Entrada por la fuerza de un ejército a un territorio.|-|-|La invasión debilitó al imperio.|historia
Occidente|oc-ci-den-te|sustantivo masculino|Parte oeste del mundo; en la historia romana, la mitad occidental del imperio.|-|Oriente|Roma fue la capital de Occidente.|historia
Oriente|o-rien-te|sustantivo masculino|Parte este del mundo; en la historia romana, la mitad oriental del imperio.|-|Occidente|Constantinopla fue la capital de Oriente.|historia
fenicio|fe-ni-cio|sustantivo masculino|Persona del antiguo pueblo comerciante del Mediterráneo oriental.|-|-|Los fenicios navegaban para comerciar.|historia
alfabeto|al-fa-be-to|sustantivo masculino|Conjunto de letras de un idioma, ordenadas de forma fija.|abecedario|-|Los fenicios crearon un alfabeto sencillo.|historia
hoplita|ho-pli-ta|sustantivo masculino|Soldado griego que luchaba con lanza y escudo.|-|-|Los hoplitas formaban una falange.|historia
falange|fa-lan-ge|sustantivo femenino|Formación cerrada de soldados con escudos y lanzas.|-|-|La falange avanzó como un muro.|historia
sofista|so-fis-ta|sustantivo masculino|En la Antigua Grecia, maestro que enseñaba a argumentar y a hablar bien.|-|-|Los sofistas cobraban por enseñar retórica.|historia
retórica|re-tó-ri-ca|sustantivo femenino|Arte de hablar y de escribir para convencer.|oratoria|-|La retórica era clave en la asamblea ateniense.|historia
capitel|ca-pi-tel|sustantivo masculino|Parte superior de una columna.|-|-|El capitel dórico es muy sencillo.|historia
friso|fri-so|sustantivo masculino|Franja decorada que corre a lo largo de una pared.|-|-|El friso del templo muestra un desfile.|historia
ánfora|án-fo-ra|sustantivo femenino|Vasija alta con dos asas usada para guardar vino o aceite.|-|-|Los griegos pintaban escenas en las ánforas.|historia
mosaico|mo-sai-co|sustantivo masculino|Imagen hecha con pequeñas piezas de piedra o de vidrio.|-|-|El mosaico romano decoraba el piso.|historia
bóveda|bó-ve-da|sustantivo femenino|Techo curvo hecho con arcos.|-|-|La bóveda cubre la sala del templo.|historia
cúpula|cú-pu-la|sustantivo femenino|Techo en forma de media esfera.|-|-|La cúpula del Panteón impresiona.|historia
basílica|ba-sí-li-ca|sustantivo femenino|Edificio romano de planta alargada, usado para reuniones y justicia.|-|-|La basílica albergaba el tribunal.|historia
termas|ter-mas|sustantivo femenino plural|Baños públicos de la antigua Roma.|-|-|Los romanos conversaban en las termas.|historia
isonomía|i-so-no-mí-a|sustantivo femenino|Igualdad de todos los ciudadanos ante la ley.|-|-|La isonomía fue un ideal de Atenas.|historia
magistrado|ma-gis-tra-do|sustantivo masculino|Persona con un cargo de autoridad en la justicia o el gobierno.|-|-|El magistrado dictó una sentencia.|historia
jurado|ju-ra-do|sustantivo masculino|Grupo de ciudadanos que decide si alguien es culpable.|-|-|El jurado ateniense votaba con piedras.|historia
estela|es-te-la|sustantivo femenino|Piedra alta y grabada que recuerda un hecho o una ley.|-|-|La estela muestra las leyes de Hammurabi.|historia
obelisco|o-be-lis-co|sustantivo masculino|Monumento alto de piedra con forma de columna terminada en punta.|-|-|Un obelisco se alza frente al templo.|historia
sarcófago|sar-có-fa-go|sustantivo masculino|Caja de piedra donde se guardaba un cuerpo enterrado.|-|-|El sarcófago del faraón era de oro.|historia
necrópolis|ne-cró-po-lis|sustantivo femenino|Gran cementerio de una ciudad antigua.|cementerio|-|La necrópolis de Giza tiene pirámides.|historia
sacrificio|sa-cri-fi-cio|sustantivo masculino|Ofrenda que se entrega a una divinidad.|ofrenda|-|En ese templo hacían sacrificios de animales.|historia
peregrinación|pe-re-gri-na-ción|sustantivo femenino|Viaje a un lugar sagrado por motivos de fe.|romería|-|La peregrinación llegó a un santuario.|historia
periodización|pe-rio-di-za-ción|sustantivo femenino|División de la historia en períodos para estudiarla mejor.|-|-|La periodización separa la Edad Antigua de la Media.|historia
continuidad|con-ti-nui-dad|sustantivo femenino|Característica de lo que sigue sin cortarse en el tiempo.|permanencia|cambio|Hay continuidad en la lengua desde el latín.|historia
multicausal|mul-ti-cau-sal|adjetivo|Que tiene varias causas.|-|-|La caída de Roma fue un proceso multicausal.|historia
legado cultural|le-ga-do cul-tu-ral|sustantivo masculino|Lo que una cultura deja a las generaciones que vienen después.|herencia|-|El legado cultural romano incluye el derecho.|historia
derecho romano|de-re-cho ro-ma-no|sustantivo masculino|Conjunto de leyes y principios de la antigua Roma, base del derecho actual.|-|-|El derecho romano influyó en nuestras leyes.|historia
cristianismo|cris-tia-nis-mo|sustantivo masculino|Religión basada en las enseñanzas de Jesucristo.|-|-|El cristianismo se extendió por el Imperio romano.|historia
código de leyes|có-di-go de le-yes|sustantivo masculino|Conjunto ordenado de normas escritas.|-|-|El código de leyes se grabó en piedra.|historia
ley escrita|ley es-cri-ta|sustantivo femenino|Norma puesta por escrito para que todos la conozcan.|-|costumbre|La ley escrita limitó la arbitrariedad.|historia
mar Mediterráneo|mar Me-di-te-rrá-ne-o|sustantivo masculino|Mar interior entre Europa, África y Asia, centro de la Antigüedad.|-|-|Los barcos fenicios surcaban el mar Mediterráneo.|geografía
Egeo|E-ge-o|nombre propio|Mar entre Grecia y Turquía.|-|-|Hay muchas islas en el Egeo.|geografía
Nilo|Ni-lo|nombre propio|Gran río de África que cruza Egipto.|-|-|El Nilo inunda sus orillas cada año.|geografía
Éufrates|Éu-fra-tes|nombre propio|Río de Asia que, junto con el Tigris, rodea Mesopotamia.|-|-|El Éufrates riega las tierras de Mesopotamia.|geografía
península itálica|pe-nín-su-la i-tá-li-ca|sustantivo femenino|Península del sur de Europa donde nació Roma.|-|-|Roma surgió en la península itálica.|geografía
Egipto|E-gip-to|nombre propio|País del noreste de África, cuna de una antigua civilización junto al Nilo.|-|-|Egipto construyó pirámides gigantes.|geografía
Grecia|Gre-cia|nombre propio|País del sur de Europa, cuna de la democracia.|-|-|Grecia es famosa por sus ruinas antiguas.|geografía
Roma|Ro-ma|nombre propio|Ciudad de Italia que fue capital de un gran imperio.|-|-|Roma fue fundada junto al río Tíber.|geografía
templo griego|tem-plo grie-go|sustantivo masculino|Edificio con columnas donde se rendía culto a los dioses de Grecia.|-|-|El templo griego tiene frontón y columnas.|historia
agricultura de regadío|a-gri-cul-tu-ra de re-ga-dí-o|sustantivo femenino|Cultivo que usa canales para llevar agua a los campos.|-|agricultura de secano|La agricultura de regadío floreció junto al Nilo.|historia
secano|se-ca-no|sustantivo masculino|Tierra de cultivo que solo recibe agua de la lluvia.|-|regadío|El trigo de secano depende de las lluvias.|historia
artesanado|ar-te-sa-na-do|sustantivo masculino|Conjunto de las personas que trabajan en oficios manuales.|-|-|El artesanado producía cerámica y telas.|historia
cosecha|co-se-cha|sustantivo femenino|Conjunto de frutos que se recogen del campo.|-|siembra|La cosecha de trigo fue abundante.|historia
siembra|siem-bra|sustantivo femenino|Acción de poner semillas en la tierra para que crezcan.|-|cosecha|La siembra se hace en otoño.|historia
granero|gra-ne-ro|sustantivo masculino|Lugar donde se guarda el grano.|-|-|El granero estaba lleno de trigo.|historia
molino|mo-li-no|sustantivo masculino|Máquina o lugar donde se muele el grano para hacer harina.|-|-|El molino movía sus aspas con el viento.|historia
arado|a-ra-do|sustantivo masculino|Herramienta que abre surcos en la tierra para sembrar.|-|-|El arado facilitó el trabajo del campo.|historia
surco|sur-co|sustantivo masculino|Línea que el arado deja en la tierra.|-|-|Pusieron las semillas en cada surco.|historia
hostigamiento|hos-ti-ga-mien-to|sustantivo masculino|Conducta repetida de molestar o agredir a alguien para hacerlo sentir mal.|acoso|-|El hostigamiento en el patio debe denunciarse.|orientación
agresión|a-gre-sión|sustantivo femenino|Ataque que daña a otra persona, con golpes o con palabras.|ataque|-|La agresión verbal también duele.|orientación
agresivo|a-gre-si-vo|adjetivo|Que ataca o reacciona con violencia.|violento|pacífico|Tuvo una respuesta agresiva.|orientación
pasivo|pa-si-vo|adjetivo|Que no actúa ni expresa lo que quiere.|inactivo|activo|Es pasivo y no dice lo que piensa.|orientación
autocontrol|au-to-con-trol|sustantivo masculino|Capacidad de dominar los impulsos y las emociones.|-|-|El autocontrol evita peleas.|orientación
ira|i-ra|sustantivo femenino|Enojo muy fuerte.|furia|calma|La ira le hizo gritar.|orientación
regulación emocional|re-gu-la-ción e-mo-cio-nal|sustantivo femenino|Capacidad de manejar lo que se siente para actuar con calma.|-|-|La regulación emocional ayuda a pensar antes de reaccionar.|orientación
autoconcepto|au-to-con-cep-to|sustantivo masculino|Idea que cada persona tiene de sí misma.|-|-|Un buen autoconcepto da seguridad.|orientación
proyecto de vida|pro-yec-to de vi-da|sustantivo masculino|Plan personal sobre lo que uno quiere lograr en el futuro.|-|-|Mi proyecto de vida incluye estudiar medicina.|orientación
hábito de estudio|há-bi-to de es-tu-dio|sustantivo masculino|Costumbre de estudiar de manera regular y ordenada.|-|-|El hábito de estudio mejora las notas.|orientación
mapa conceptual|ma-pa con-cep-tual|sustantivo masculino|Esquema que muestra ideas y cómo se relacionan entre sí.|-|-|Hice un mapa conceptual de la lección.|orientación
organizador gráfico|or-ga-ni-za-dor grá-fi-co|sustantivo masculino|Esquema visual que ordena la información de un tema.|-|-|Usé un organizador gráfico para comparar dos textos.|orientación
distracción|dis-trac-ción|sustantivo femenino|Cosa que quita la atención de lo que se hace.|-|atención|El celular es una gran distracción.|orientación
atención|a-ten-ción|sustantivo femenino|Capacidad de fijar la mente en algo.|concentración|distracción|Presta atención a las instrucciones.|orientación
agenda|a-gen-da|sustantivo femenino|Cuaderno o aplicación donde se anotan tareas y fechas.|-|-|Anoté la prueba en mi agenda.|orientación
prioridad|prio-ri-dad|sustantivo femenino|Importancia que se da a algo para atenderlo primero.|preferencia|-|La tarea es la prioridad de hoy.|orientación
límites|lí-mi-tes|sustantivo masculino plural|Reglas que marcan hasta dónde se puede llegar sin dañar a otros.|-|-|Poner límites es parte de la convivencia.|orientación
noviazgo|no-viaz-go|sustantivo masculino|Relación afectiva entre dos personas que se quieren.|-|-|El noviazgo se basa en el respeto.|orientación
amor propio|a-mor pro-pio|sustantivo masculino|Valoración y respeto que una persona siente por sí misma.|autoestima|-|El amor propio ayuda a decir que no.|orientación
resolución de conflictos|re-so-lu-ción de con-flic-tos|sustantivo femenino|Manera de buscar acuerdos para terminar un desacuerdo sin violencia.|-|-|La resolución de conflictos usa el diálogo.|orientación
pensamiento crítico|pen-sa-mien-to crí-ti-co|sustantivo masculino|Habilidad de analizar la información antes de aceptarla.|-|-|El pensamiento crítico ayuda a detectar noticias falsas.|orientación
trabajo cooperativo|tra-ba-jo co-o-pe-ra-ti-vo|sustantivo masculino|Forma de trabajar en que todos aportan para lograr una meta común.|-|-|En el trabajo cooperativo cada integrante tiene un rol.|orientación
rol|rol|sustantivo masculino|Función que una persona cumple en un grupo.|papel|-|Mi rol en el equipo es registrar los datos.|orientación
vocero|vo-ce-ro|sustantivo masculino|Persona que habla en nombre de un grupo.|portavoz|-|El vocero del curso entregó la carta.|orientación
retroalimentación|re-tro-a-li-men-ta-ción|sustantivo femenino|Comentarios que ayudan a mejorar un trabajo.|-|-|La retroalimentación de la profesora me ayudó a corregir.|orientación
autoevaluación|au-to-e-va-lua-ción|sustantivo femenino|Revisión que una persona hace de su propio trabajo.|-|-|La autoevaluación me mostró en qué debo mejorar.|orientación
voluntad|vo-lun-tad|sustantivo femenino|Capacidad de decidir y de esforzarse por algo.|determinación|-|Con voluntad se aprende más rápido.|orientación
tenacidad|te-na-ci-dad|sustantivo femenino|Firmeza para seguir adelante sin rendirse.|constancia|-|Su tenacidad lo llevó a terminar la maratón.|orientación
curiosidad|cu-rio-si-dad|sustantivo femenino|Deseo de saber o de descubrir cosas nuevas.|interés|indiferencia|La curiosidad me llevó a leer más.|orientación
creatividad|cre-a-ti-vi-dad|sustantivo femenino|Capacidad de inventar ideas nuevas y originales.|ingenio|-|La creatividad ayudó a resolver el problema.|orientación
espíritu crítico|es-pí-ri-tu crí-ti-co|sustantivo masculino|Actitud de preguntar y analizar antes de aceptar algo.|-|-|El espíritu crítico se aprende leyendo con atención.|orientación
ciudadanía digital|ciu-da-da-ní-a di-gi-tal|sustantivo femenino|Uso responsable y respetuoso de la tecnología en la sociedad.|-|-|La ciudadanía digital exige cuidar a los demás en línea.|tecnología
lija|li-ja|sustantivo femenino|Papel áspero que sirve para alisar superficies.|-|-|Pasé una lija por la madera.|tecnología
sierra|sie-rra|sustantivo femenino|Herramienta con dientes que sirve para cortar madera u otros materiales.|serrucho|-|Corté el listón con una sierra.|tecnología
taladro|ta-la-dro|sustantivo masculino|Herramienta que hace agujeros en un material.|-|-|El taladro hizo un hoyo en la pared.|tecnología
tuerca|tuer-ca|sustantivo femenino|Pieza con un agujero roscado donde entra un tornillo.|-|-|Apreté la tuerca con la llave.|tecnología
alicate|a-li-ca-te|sustantivo masculino|Herramienta con dos brazos para sujetar o cortar cables y alambres.|-|-|Corté el alambre con un alicate.|tecnología
cinta métrica|cin-ta mé-tri-ca|sustantivo femenino|Cinta flexible con medidas que sirve para medir.|huincha|-|Medí el escritorio con la cinta métrica.|tecnología
ensamblaje|en-sam-bla-je|sustantivo masculino|Unión de las piezas de un objeto.|montaje|-|El ensamblaje de la maqueta tomó una hora.|tecnología
armazón|ar-ma-zón|sustantivo masculino|Estructura que sostiene un objeto o una construcción.|esqueleto|-|El armazón de la casita era de palos.|tecnología
viga|vi-ga|sustantivo femenino|Barra larga y gruesa que sostiene el techo o el piso.|-|-|La viga sostiene el techo del galpón.|tecnología
pilar|pi-lar|sustantivo masculino|Columna que sostiene una construcción.|-|-|El puente se apoya en tres pilares.|tecnología
cimiento|ci-mien-to|sustantivo masculino|Base sobre la que se levanta una construcción.|base|-|Los cimientos de la casa son de hormigón.|tecnología
estabilidad|es-ta-bi-li-dad|sustantivo femenino|Capacidad de un objeto de mantenerse firme sin caerse.|firmeza|inestabilidad|La base ancha da estabilidad a la torre.|tecnología
tensión|ten-sión|sustantivo femenino|Fuerza que estira un cuerpo; también estado de nervios.|-|-|La cuerda soporta la tensión del peso.|tecnología
impacto ambiental|im-pac-to am-bien-tal|sustantivo masculino|Efecto que una actividad humana produce en la naturaleza.|-|-|La fábrica evaluó su impacto ambiental.|tecnología
eficiencia energética|e-fi-cien-cia e-ner-gé-ti-ca|sustantivo femenino|Uso de menos energía para lograr el mismo resultado.|-|-|Las ampolletas led mejoran la eficiencia energética.|tecnología
ciclo de vida|ci-clo de vi-da|sustantivo masculino|Etapas por las que pasa un producto, desde su fabricación hasta que se desecha.|-|-|Analizamos el ciclo de vida de una botella.|tecnología
obsolescencia|ob-so-les-cen-cia|sustantivo femenino|Pérdida de utilidad de un producto por quedar anticuado o dejar de funcionar.|-|-|La obsolescencia hace cambiar el teléfono cada pocos años.|tecnología
diagrama de flujo|dia-gra-ma de flu-jo|sustantivo masculino|Dibujo con cajas y flechas que muestra los pasos de un proceso.|-|-|Dibujé un diagrama de flujo para mi programa.|tecnología
bucle|bu-cle|sustantivo masculino|Parte de un programa que se repite varias veces.|ciclo|-|El bucle repite la orden diez veces.|tecnología
condicional|con-di-cio-nal|sustantivo masculino|Instrucción de un programa que actúa solo si se cumple una condición.|-|-|El condicional revisa si la clave es correcta.|tecnología
depuración|de-pu-ra-ción|sustantivo femenino|Búsqueda y corrección de errores en un programa.|-|-|La depuración me mostró dónde fallaba.|tecnología
interfaz|in-ter-faz|sustantivo femenino|Parte de un programa o aparato con la que el usuario interactúa.|-|-|La interfaz de la aplicación es fácil de usar.|tecnología
icono|i-co-no|sustantivo masculino|Dibujo pequeño que representa una función o un programa.|-|-|Toqué el icono de la cámara.|tecnología
menú|me-nú|sustantivo masculino|Lista de opciones que se muestra en la pantalla.|-|-|Abrí el menú para elegir otra opción.|tecnología
hoja de cálculo|ho-ja de cál-cu-lo|sustantivo femenino|Programa que ordena datos en filas y columnas y hace cuentas con ellos.|-|-|Calculé el promedio en una hoja de cálculo.|tecnología
resolución|re-so-lu-ción|sustantivo femenino|Cantidad de puntos que forman una imagen, que define su nitidez.|-|-|Esta foto tiene alta resolución.|tecnología
píxel|pí-xel|sustantivo masculino|Cada punto pequeño que forma una imagen digital.|-|-|Al ampliar la foto se ven los píxeles.|tecnología
servidor|ser-vi-dor|sustantivo masculino|Computador que entrega información o servicios a otros equipos.|-|-|El servidor del colegio guarda las tareas.|tecnología
ancho de banda|an-cho de ban-da|sustantivo masculino|Cantidad de datos que una conexión puede transmitir por segundo.|-|-|Con poco ancho de banda el video se corta.|tecnología
descarga|des-car-ga|sustantivo femenino|Copia de un archivo desde internet a un equipo.|-|carga|La descarga del juego tardó diez minutos.|tecnología
adjunto|ad-jun-to|sustantivo masculino|Archivo que se envía junto con un correo.|-|-|Revisa el adjunto del correo.|tecnología
suplantación|su-plan-ta-ción|sustantivo femenino|Engaño en que alguien se hace pasar por otra persona.|-|-|La suplantación de identidad es un delito.|tecnología
ciberseguridad|ci-ber-se-gu-ri-dad|sustantivo femenino|Conjunto de medidas para proteger la información y los equipos en línea.|-|-|La ciberseguridad empieza con una buena clave.|tecnología
cifrado|ci-fra-do|sustantivo masculino|Transformación de un mensaje en un código para que solo lo lea quien tiene la clave.|-|-|El cifrado protege los mensajes.|tecnología
autenticación|au-ten-ti-ca-ción|sustantivo femenino|Comprobación de que alguien es quien dice ser.|-|-|La autenticación pide clave y un código.|tecnología
copia de seguridad|co-pia de se-gu-ri-dad|sustantivo femenino|Duplicado de archivos guardado para no perderlos.|respaldo|-|Hice una copia de seguridad de mis fotos.|tecnología
fuente de información|fuen-te de in-for-ma-ción|sustantivo femenino|Lugar, persona o documento de donde se obtienen datos.|-|-|Anota cada fuente de información que uses.|tecnología
noticia falsa|no-ti-cia fal-sa|sustantivo femenino|Información inventada que se hace pasar por verdadera.|-|-|Revisé si era una noticia falsa antes de compartirla.|tecnología
edición|e-di-ción|sustantivo femenino|Corrección y arreglo de un texto, video o imagen antes de publicarlo.|-|-|La edición del video tomó una tarde.|tecnología
audiovisual|au-dio-vi-sual|adjetivo|Que combina sonido e imagen.|-|-|Preparé un recurso audiovisual.|tecnología
storyboard|story-board|sustantivo masculino|Serie de dibujos que muestra, escena por escena, cómo será un video.|-|-|Dibujamos el storyboard antes de grabar.|tecnología
alocución|a-lo-cu-ción|sustantivo femenino|Discurso breve que una autoridad dirige a un grupo.|discurso|-|El director dio una alocución al inicio del año.|lenguaje
tesitura|te-si-tu-ra|sustantivo femenino|Conjunto de notas que una voz puede cantar con comodidad.|-|-|Su tesitura es de tono agudo.|música
oratoria|o-ra-to-ria|sustantivo femenino|Arte de hablar en público con eficacia.|retórica|-|En el taller de oratoria practicamos discursos.|lenguaje
glosa|glo-sa|sustantivo femenino|Nota que explica un texto difícil.|comentario|-|La glosa aclara el sentido del verso.|lenguaje
incisos|in-ci-sos|sustantivo masculino plural|Frases cortas que se intercalan en una oración, entre comas o rayas.|-|-|Los incisos aclaran la idea sin cortarla.|lenguaje
pleonasmo|ple-o-nas-mo|sustantivo masculino|Uso de palabras innecesarias que repiten una idea, como en «subir arriba».|redundancia|-|«Lo vi con mis propios ojos» contiene un pleonasmo.|lenguaje
redundancia|re-dun-dan-cia|sustantivo femenino|Repetición innecesaria de una idea o de una palabra.|-|-|Evita la redundancia en tu escrito.|lenguaje
muletilla|mu-le-ti-lla|sustantivo femenino|Palabra que alguien repite sin darse cuenta al hablar.|-|-|«Como que» es una muletilla muy usada.|lenguaje
cacofonía|ca-co-fo-ní-a|sustantivo femenino|Sonido desagradable por la repetición de ciertos sonidos.|-|eufonía|La repetición de «ss» produce cacofonía.|lenguaje
mapa de ideas|ma-pa de i-de-as|sustantivo masculino|Dibujo que organiza las ideas de un tema alrededor de una idea central.|-|-|Hice un mapa de ideas antes de escribir.|lenguaje
corrección|co-rrec-ción|sustantivo femenino|Cambio que se hace en un texto para quitar errores.|enmienda|-|La corrección del ensayo me tomó una tarde.|lenguaje
revisión|re-vi-sión|sustantivo femenino|Lectura cuidadosa de algo para mejorarlo.|repaso|-|La revisión del informe mostró dos errores.|lenguaje
cita textual|ci-ta tex-tual|sustantivo femenino|Frase copiada exactamente de otro texto, entre comillas.|-|-|Puse una cita textual con su fuente.|lenguaje
bibliografía|bi-blio-gra-fí-a|sustantivo femenino|Lista de libros y textos que se usaron en un trabajo.|-|-|Al final del trabajo escribí la bibliografía.|lenguaje
autoría|au-to-rí-a|sustantivo femenino|Condición de ser el autor de una obra.|-|-|La autoría del poema es de una escritora chilena.|lenguaje
seudónimo|seu-dó-ni-mo|sustantivo masculino|Nombre falso que usa un autor en lugar del propio.|alias|-|Escribía con un seudónimo.|lenguaje
crítica literaria|crí-ti-ca li-te-ra-ria|sustantivo femenino|Opinión razonada sobre una obra escrita.|-|-|La crítica literaria elogió la novela.|lenguaje
tradición oral|tra-di-ción o-ral|sustantivo femenino|Conjunto de historias y cantos que pasan de boca en boca.|-|-|La leyenda llegó por tradición oral.|lenguaje
leyenda urbana|le-yen-da ur-ba-na|sustantivo femenino|Relato falso o exagerado que se cuenta como verdadero en una ciudad.|-|-|Esa historia del fantasma es una leyenda urbana.|lenguaje
humor|hu-mor|sustantivo masculino|Característica de lo que da risa; ánimo de una persona.|gracia|seriedad|El humor del cuento alegró al curso.|lenguaje
sátira|sá-ti-ra|sustantivo femenino|Escrito que critica algo con humor y exageración.|-|-|La sátira se burla de los políticos vanidosos.|lenguaje
parodia|pa-ro-dia|sustantivo femenino|Imitación exagerada de una obra para divertir.|-|-|Hicimos una parodia de la película.|lenguaje
caricaturista|ca-ri-ca-tu-ris-ta|sustantivo masculino y femenino|Persona que dibuja caricaturas.|-|-|El caricaturista exageró la nariz del alcalde.|artes
historietista|his-to-rie-tis-ta|sustantivo masculino y femenino|Persona que crea historietas.|-|-|La historietista dibuja cada viñeta a mano.|artes
guionista|guio-nis-ta|sustantivo masculino y femenino|Persona que escribe guiones para cine, televisión o teatro.|-|-|El guionista escribió los diálogos.|artes
panorámica|pa-no-rá-mi-ca|sustantivo femenino|Vista amplia de un paisaje o de una escena.|-|-|Saqué una panorámica del valle.|artes
perspectiva lineal|pers-pec-ti-va li-ne-al|sustantivo femenino|Técnica de dibujo que usa líneas hacia un punto para mostrar profundidad.|-|-|La perspectiva lineal dio profundidad a la calle.|artes
volumétrico|vo-lu-mé-tri-co|adjetivo|Que tiene volumen y se puede rodear con la vista.|-|plano|La escultura es una obra volumétrica.|artes
modelado|mo-de-la-do|sustantivo masculino|Técnica de dar forma a una masa blanda con las manos.|-|-|El modelado en arcilla requiere paciencia.|artes
hormigón|hor-mi-gón|sustantivo masculino|Mezcla de cemento, arena, grava y agua que se endurece.|concreto|-|La losa es de hormigón.|tecnología
cemento|ce-men-to|sustantivo masculino|Polvo gris que mezclado con agua se endurece como piedra.|-|-|Mezclamos cemento con arena y agua.|tecnología
andamio|an-da-mio|sustantivo masculino|Estructura temporal que permite trabajar en lo alto de un edificio.|-|-|Los obreros subieron por el andamio.|tecnología
grúa|grú-a|sustantivo femenino|Máquina con un brazo que levanta cargas pesadas.|-|-|La grúa subió las vigas.|tecnología
excavadora|ex-ca-va-do-ra|sustantivo femenino|Máquina que cava la tierra con una pala grande.|-|-|La excavadora abrió una zanja.|tecnología
casco de seguridad|cas-co de se-gu-ri-dad|sustantivo masculino|Prenda rígida que protege la cabeza en trabajos de riesgo.|-|-|Todos usan casco de seguridad en la obra.|tecnología
guantes de trabajo|guan-tes de tra-ba-jo|sustantivo masculino plural|Protección para las manos al manipular materiales.|-|-|Uso guantes de trabajo para cortar madera.|tecnología
usabilidad|u-sa-bi-li-dad|sustantivo femenino|Facilidad con que una persona puede usar un producto.|-|-|La usabilidad de la aplicación es muy buena.|tecnología
accesibilidad|ac-ce-si-bi-li-dad|sustantivo femenino|Condición de lo que todas las personas pueden usar o alcanzar.|-|-|La rampa mejora la accesibilidad del colegio.|tecnología
inclusivo|in-clu-si-vo|adjetivo|Que incluye a todas las personas sin dejar a nadie fuera.|-|excluyente|Buscamos un juego inclusivo.|orientación
asamblea de curso|a-sam-ble-a de cur-so|sustantivo femenino|Reunión de todo un curso para conversar y decidir asuntos comunes.|-|-|En la asamblea de curso votamos el paseo.|orientación
directiva de curso|di-rec-ti-va de cur-so|sustantivo femenino|Grupo de alumnos elegidos para representar a su curso.|-|-|La directiva de curso organizó la colecta.|orientación
centro de estudiantes|cen-tro de es-tu-dian-tes|sustantivo masculino|Organización de alumnos que los representa ante el colegio.|-|-|El centro de estudiantes propuso un reciclaje.|orientación
campaña solidaria|cam-pa-ña so-li-da-ria|sustantivo femenino|Acción organizada para ayudar a personas que lo necesitan.|-|-|Hicimos una campaña solidaria de abrigo.|orientación
reglamento interno|re-gla-men-to in-ter-no|sustantivo masculino|Conjunto de normas de convivencia de un colegio.|-|-|El reglamento interno explica las sanciones.|orientación
"""

VERBOS = """
refutar|re-fu-tar|Demostrar que una idea o un argumento es falso.|refuto|refuta|refutó|refutará|rebatir|confirmar|Refutó mi opinión con datos del informe.
parafrasear|pa-ra-fra-se-ar|Decir con otras palabras lo que dijo otra persona.|parafraseo|parafrasea|parafraseó|parafraseará|reformular|-|Ella parafraseó el párrafo con sus propias palabras.
contrastar|con-tras-tar|Comparar dos cosas para ver sus diferencias.|contrasto|contrasta|contrastó|contrastará|comparar|-|Contrastó dos noticias sobre el mismo hecho.
ejemplificar|e-jem-pli-fi-car|Dar ejemplos para explicar mejor una idea.|ejemplifico|ejemplifica|ejemplificó|ejemplificará|ilustrar|-|El profesor ejemplificó la regla con una frase.
justificar|jus-ti-fi-car|Dar razones que muestren que algo es correcto.|justifico|justifica|justificó|justificará|fundamentar|-|Justificó su respuesta con una cita del texto.
fundamentar|fun-da-men-tar|Apoyar una idea con razones y pruebas.|fundamento|fundamenta|fundamentó|fundamentará|justificar|-|Fundamentó su opinión con tres datos.
cuestionar|cues-tio-nar|Poner en duda o preguntar por la validez de algo.|cuestiono|cuestiona|cuestionó|cuestionará|dudar|aceptar|Cuestionó la veracidad de la noticia.
persuadir|per-sua-dir|Lograr con razones que alguien crea o haga algo.|persuado|persuade|persuadió|persuadirá|convencer|disuadir|Persuadió a su curso de reciclar.
disuadir|di-sua-dir|Convencer a alguien de que no haga algo.|disuado|disuade|disuadió|disuadirá|desanimar|persuadir|Su madre lo disuadió de salir con lluvia.
exagerar|e-xa-ge-rar|Presentar algo como más grande o más grave de lo que es.|exagero|exagera|exageró|exagerará|aumentar|minimizar|Exageró el tamaño del pez que pescó.
simbolizar|sim-bo-li-zar|Representar una idea mediante un signo.|simbolizo|simboliza|simbolizó|simbolizará|representar|-|La paloma blanca simboliza la paz.
personificar|per-so-ni-fi-car|Dar rasgos humanos a un animal, una cosa o una idea.|personifico|personifica|personificó|personificará|humanizar|-|El autor personificó al viento en su poema.
rimar|ri-mar|Terminar dos palabras con los mismos sonidos desde la última vocal fuerte.|rimo|rima|rimó|rimará|-|-|«Canción» rima con «corazón».
recitar|re-ci-tar|Decir en voz alta un texto aprendido de memoria.|recito|recita|recitó|recitará|declamar|-|Recitó un poema ante todo el curso.
declamar|de-cla-mar|Recitar con expresión y entonación.|declamo|declama|declamó|declamará|recitar|-|Declamó los versos con voz firme.
dramatizar|dra-ma-ti-zar|Representar una historia como obra de teatro.|dramatizo|dramatiza|dramatizó|dramatizará|actuar|-|Mi grupo dramatizó una leyenda.
relatar|re-la-tar|Contar un hecho paso a paso.|relato|relata|relató|relatará|narrar|-|Relató su viaje con muchos detalles.
despejar|des-pe-jar|En una ecuación, dejar sola la incógnita; también dejar libre un espacio.|despejo|despeja|despejó|despejará|aclarar|-|Despejó la x para hallar el resultado.
aproximar|a-pro-xi-mar|Acercar un valor a otro más sencillo.|aproximo|aproxima|aproximó|aproximará|acercar|alejar|Aproximó 3,98 a 4.
graficar|gra-fi-car|Representar datos mediante un gráfico.|grafico|grafica|graficó|graficará|representar|-|Graficó las temperaturas de la semana.
equilibrar|e-qui-li-brar|Poner algo en equilibrio.|equilibro|equilibra|equilibró|equilibrará|nivelar|desequilibrar|Equilibró la balanza con otra pesa.
igualar|i-gua-lar|Hacer que dos cosas queden iguales.|igualo|iguala|igualó|igualará|nivelar|diferenciar|Igualó los dos lados de la ecuación.
elevar|e-le-var|Subir algo a un nivel más alto; en matemática, calcular una potencia.|elevo|eleva|elevó|elevará|subir|bajar|Elevó el número al cuadrado.
reemplazar|re-em-pla-zar|Poner a alguien o algo en el lugar de otro.|reemplazo|reemplaza|reemplazó|reemplazará|sustituir|-|Reemplazó la pila del reloj.
incrementar|in-cre-men-tar|Hacer más grande o más numeroso.|incremento|incrementa|incrementó|incrementará|aumentar|disminuir|La fábrica incrementó su producción.
descomponer|des-com-po-ner|Separar un todo en sus partes.|descompongo|descompone|descompuso|descompondrá|separar|componer|Descompuso el número en factores.
trazar|tra-zar|Dibujar líneas o figuras.|trazo|traza|trazó|trazará|dibujar|-|Trazó una recta con la regla.
ubicar|u-bi-car|Colocar algo en un lugar o encontrar dónde está.|ubico|ubica|ubicó|ubicará|situar|-|Ubicó el punto en el plano cartesiano.
rotar|ro-tar|Girar alrededor de un punto o de un eje.|roto|rota|rotó|rotará|girar|-|La figura rotó noventa grados.
vibrar|vi-brar|Moverse muy rápido de un lado a otro.|vibro|vibra|vibró|vibrará|temblar|-|La cuerda vibró al tocarla.
propagar|pro-pa-gar|Extender algo por un lugar.|propago|propaga|propagó|propagará|difundir|contener|El sonido se propagó por el aire.
refractar|re-frac-tar|Desviar la luz al pasar de un medio a otro.|refracto|refracta|refractó|refractará|desviar|-|El agua refractó el rayo de luz.
transmitir|trans-mi-tir|Pasar algo de un lugar o de una persona a otra.|transmito|transmite|transmitió|transmitirá|comunicar|-|El metal transmite el calor.
acelerar|a-ce-le-rar|Aumentar la velocidad.|acelero|acelera|aceleró|acelerará|apurar|frenar|El ciclista aceleró en la bajada.
frenar|fre-nar|Reducir la velocidad o detener algo.|freno|frena|frenó|frenará|detener|acelerar|La bicicleta frenó antes del cruce.
dilatar|di-la-tar|Hacer más grande, o hacerse más grande, por el calor.|dilato|dilata|dilató|dilatará|expandir|contraer|El metal se dilata con el calor.
contraer|con-tra-er|Hacerse más pequeño; también adquirir una enfermedad.|contraigo|contrae|contrajo|contraerá|encoger|dilatar|El músculo se contrae al levantar peso.
comprimir|com-pri-mir|Apretar algo para que ocupe menos espacio.|comprimo|comprime|comprimió|comprimirá|apretar|expandir|Comprimió el aire en la bomba.
expandir|ex-pan-dir|Hacer que algo ocupe más espacio.|expando|expande|expandió|expandirá|extender|comprimir|El gas se expandió dentro del globo.
solidificar|so-li-di-fi-car|Convertir un líquido en sólido.|solidifico|solidifica|solidificó|solidificará|endurecer|derretir|El agua se solidificó en el congelador.
difundir|di-fun-dir|Hacer que algo llegue a muchas personas.|difundo|difunde|difundió|difundirá|propagar|ocultar|La radio difundió la noticia.
nutrir|nu-trir|Dar al cuerpo los alimentos que necesita.|nutro|nutre|nutrió|nutrirá|alimentar|desnutrir|La fruta nutre el cuerpo.
excretar|ex-cre-tar|Expulsar del cuerpo los desechos.|excreto|excreta|excretó|excretará|expulsar|-|El riñón excreta sustancias de desecho.
erosionar|e-ro-sio-nar|Desgastar el suelo o las rocas por el viento o el agua.|erosiono|erosiona|erosionó|erosionará|desgastar|-|El río erosionó la ladera.
sedimentar|se-di-men-tar|Depositar materiales en el fondo.|sedimento|sedimenta|sedimentó|sedimentará|depositar|-|El río sedimentó arena en la orilla.
intoxicar|in-to-xi-car|Dañar el cuerpo con una sustancia nociva.|intoxico|intoxica|intoxicó|intoxicará|envenenar|desintoxicar|El humo intoxicó a los vecinos.
fumar|fu-mar|Aspirar y soltar el humo del tabaco.|fumo|fuma|fumó|fumará|-|-|Está prohibido fumar en el colegio.
inmunizar|in-mu-ni-zar|Proteger a alguien contra una enfermedad.|inmunizo|inmuniza|inmunizó|inmunizará|vacunar|-|La vacuna inmunizó a los niños contra el sarampión.
emigrar|e-mi-grar|Dejar el país donde se vive para ir a vivir a otro.|emigro|emigra|emigró|emigrará|marcharse|inmigrar|Su familia emigró a otro país.
inmigrar|in-mi-grar|Llegar a otro país para vivir en él.|inmigro|inmigra|inmigró|inmigrará|llegar|emigrar|Muchas personas inmigraron a la ciudad.
reinar|rei-nar|Gobernar como rey o reina.|reino|reina|reinó|reinará|gobernar|-|El faraón reinó veinte años.
tributar|tri-bu-tar|Pagar un impuesto o un tributo.|tributo|tributa|tributó|tributará|pagar|-|Los campesinos tributaban parte de su cosecha.
esclavizar|es-cla-vi-zar|Convertir a una persona en esclava.|esclavizo|esclaviza|esclavizó|esclavizará|someter|liberar|Los conquistadores esclavizaron a los prisioneros.
reformar|re-for-mar|Cambiar algo para mejorarlo.|reformo|reforma|reformó|reformará|modificar|-|El alcalde reformó la plaza.
edificar|e-di-fi-car|Construir un edificio.|edifico|edifica|edificó|edificará|construir|derribar|Los romanos edificaron grandes templos.
erigir|e-ri-gir|Levantar un monumento o una construcción.|erijo|erige|erigió|erigirá|levantar|derribar|Erigieron una estatua en la plaza.
excavar|ex-ca-var|Hacer un hoyo en la tierra.|excavo|excava|excavó|excavará|cavar|-|El equipo excavó el yacimiento.
descifrar|des-ci-frar|Lograr entender una escritura o un mensaje difícil.|descifro|descifra|descifró|descifrará|interpretar|-|Champollion descifró los jeroglíficos.
archivar|ar-chi-var|Guardar documentos de manera ordenada.|archivo|archiva|archivó|archivará|guardar|-|Archivó las pruebas en una carpeta.
legislar|le-gis-lar|Hacer leyes.|legislo|legisla|legisló|legislará|-|-|El Congreso legisló sobre el tema.
mediar|me-diar|Intervenir entre personas enfrentadas para ayudarlas a llegar a un acuerdo.|medio|media|medió|mediará|intervenir|-|La profesora medió en la discusión.
priorizar|prio-ri-zar|Dar prioridad a algo.|priorizo|prioriza|priorizó|priorizará|preferir|postergar|Priorizó estudiar antes de jugar.
comprometerse|com-pro-me-ter-se|Asumir una obligación o hacer una promesa.|me comprometo|se compromete|se comprometió|se comprometerá|obligarse|-|Se comprometió a entregar el informe.
percibir|per-ci-bir|Darse cuenta de algo por los sentidos.|percibo|percibe|percibió|percibirá|notar|-|Percibió un olor extraño.
prever|pre-ver|Ver o suponer con anticipación lo que ocurrirá.|preveo|prevé|previó|preverá|anticipar|-|Previó la lluvia por las nubes oscuras.
adaptarse|a-dap-tar-se|Ajustarse a nuevas condiciones.|me adapto|se adapta|se adaptó|se adaptará|acostumbrarse|-|El animal se adaptó al clima frío.
predominar|pre-do-mi-nar|Ser lo más abundante o lo más importante.|predomino|predomina|predominó|predominará|prevalecer|-|En esta zona predomina el viento del sur.
prevalecer|pre-va-le-cer|Mantenerse por encima de otras cosas.|prevalezco|prevalece|prevaleció|prevalecerá|predominar|ceder|Prevaleció el acuerdo de la mayoría.
permitir|per-mi-tir|Dejar que algo ocurra o se haga.|permito|permite|permitió|permitirá|autorizar|prohibir|La profesora permitió usar calculadora.
prohibir|pro-hi-bir|No dejar que algo se haga.|prohíbo|prohíbe|prohibió|prohibirá|vedar|permitir|El reglamento prohíbe correr en el pasillo.
aportar|a-por-tar|Dar algo para un fin común.|aporto|aporta|aportó|aportará|contribuir|-|Cada alumno aportó una idea.
fomentar|fo-men-tar|Impulsar algo para que crezca.|fomento|fomenta|fomentó|fomentará|impulsar|frenar|La biblioteca fomenta la lectura.
recopilar|re-co-pi-lar|Reunir datos, textos o cosas dispersas.|recopilo|recopila|recopiló|recopilará|reunir|-|Recopiló información de varias fuentes.
enumerar|e-nu-me-rar|Nombrar o contar una por una las partes de algo.|enumero|enumera|enumeró|enumerará|listar|-|Enumeró las causas del problema.
jerarquizar|je-rar-qui-zar|Ordenar según la importancia.|jerarquizo|jerarquiza|jerarquizó|jerarquizará|ordenar|-|Jerarquizó las tareas del día.
delimitar|de-li-mi-tar|Fijar los límites de algo.|delimito|delimita|delimitó|delimitará|acotar|-|Delimitó el tema de su investigación.
memorizar|me-mo-ri-zar|Aprender algo para recordarlo exactamente.|memorizo|memoriza|memorizó|memorizará|aprender|olvidar|Memorizó la tabla del siete.
delegar|de-le-gar|Dar a otra persona una tarea que le corresponde a uno.|delego|delega|delegó|delegará|encargar|-|La capitana delegó el registro en una compañera.
perseverar|per-se-ve-rar|Mantenerse firme en lo que se ha empezado.|persevero|persevera|perseveró|perseverará|persistir|desistir|Perseveró hasta aprender el pase.
embalsamar|em-bal-sa-mar|Preparar un cuerpo con sustancias para que no se descomponga.|embalsamo|embalsama|embalsamó|embalsamará|momificar|-|Los egipcios embalsamaban a sus faraones.
oxidar|o-xi-dar|Cubrir un metal de óxido por la acción del aire y la humedad.|oxido|oxida|oxidó|oxidará|corroer|-|La humedad oxidó la reja.
destilar|des-ti-lar|Separar un líquido mediante evaporación y condensación.|destilo|destila|destiló|destilará|purificar|-|Destiló agua en el laboratorio.
cristalizar|cris-ta-li-zar|Formar cristales a partir de una disolución.|cristalizo|cristaliza|cristalizó|cristalizará|-|-|La sal cristalizó al evaporarse el agua.
arder|ar-der|Estar en llamas o quemarse.|ardo|arde|ardió|arderá|quemarse|apagarse|La leña ardió toda la noche.
fecundar|fe-cun-dar|Unirse un óvulo con un espermatozoide para formar un nuevo ser.|fecundo|fecunda|fecundó|fecundará|-|-|El espermatozoide fecundó al óvulo.
madurar|ma-du-rar|Llegar a su desarrollo completo.|maduro|madura|maduró|madurará|desarrollarse|-|Las frutas maduraron con el sol.
arar|a-rar|Abrir surcos en la tierra con un arado.|aro|ara|aró|arará|labrar|-|El campesino aró el terreno antes de sembrar.
moler|mo-ler|Reducir un grano a polvo golpeándolo o aplastándolo.|muelo|muele|molió|molerá|triturar|-|El molino molió el trigo.
esculpir|es-cul-pir|Dar forma a una piedra o a otro material para crear una figura.|esculpo|esculpe|esculpió|esculpirá|tallar|-|El artista esculpió un busto en mármol.
grabar|gra-bar|Marcar signos o imágenes sobre una superficie; también registrar sonido o video.|grabo|graba|grabó|grabará|marcar|borrar|Grabó una frase en la piedra.
modelar|mo-de-lar|Dar forma a una masa blanda con las manos.|modelo|modela|modeló|modelará|moldear|-|Modeló un jarrón con arcilla.
entonar|en-to-nar|Cantar con el tono correcto.|entono|entona|entonó|entonará|cantar|desafinar|El coro entonó el himno.
ejecutar|e-je-cu-tar|Hacer o llevar a cabo algo; en computación, poner en marcha un programa.|ejecuto|ejecuta|ejecutó|ejecutará|realizar|-|Ejecutó el programa y salió bien.
programar|pro-gra-mar|Escribir las instrucciones que seguirá un computador; también fijar algo para más adelante.|programo|programa|programó|programará|codificar|-|Programó un juego sencillo.
depurar|de-pu-rar|Quitar errores o impurezas de algo, como un programa.|depuro|depura|depuró|depurará|corregir|-|Depuró el código hasta que funcionó.
descargar|des-car-gar|Copiar un archivo desde internet a un equipo; también sacar la carga de algo.|descargo|descarga|descargó|descargará|bajar|cargar|Descargó la presentación al computador.
instalar|ins-ta-lar|Dejar un programa o un aparato listo para usarse.|instalo|instala|instaló|instalará|montar|desinstalar|Instaló un programa nuevo.
configurar|con-fi-gu-rar|Ajustar un aparato o programa para que funcione como se desea.|configuro|configura|configuró|configurará|ajustar|-|Configuró la red del colegio.
cifrar|ci-frar|Convertir un mensaje en un código secreto.|cifro|cifra|cifró|cifrará|codificar|descifrar|Cifró el mensaje con una clave.
dialogar|dia-lo-gar|Conversar dos o más personas para entenderse.|dialogo|dialoga|dialogó|dialogará|conversar|-|Dialogaron para resolver el problema.
cuantificar|cuan-ti-fi-car|Expresar una cantidad con números.|cuantifico|cuantifica|cuantificó|cuantificará|medir|-|Cuantificó los resultados de la encuesta.
ponderar|pon-de-rar|Evaluar con cuidado la importancia de algo.|pondero|pondera|ponderó|ponderará|sopesar|-|Ponderó los pros y los contras.
sistematizar|sis-te-ma-ti-zar|Organizar datos o ideas siguiendo un sistema.|sistematizo|sistematiza|sistematizó|sistematizará|ordenar|-|Sistematizó la información en una tabla.
"""
