"""Diccionario de español de 1.º medio: palabras (vocabulario de Lenguaje, Matemática, Ciencias, Historia y vida cotidiana) y verbos.

Formato de PALABRAS (una por línea, separado por «|»):
    palabra|sílabas|clase|significado|sinónimos|antónimos|ejemplo|tema
Formato de VERBOS:
    infinitivo|sílabas|significado|yo (hoy)|él o ella (hoy)|él o ella (ayer)|él o ella (mañana)|sinónimos|antónimos|ejemplo
Un guion «-» significa que no hay sinónimo o antónimo sencillo para ese nivel.
Textos propios del proyecto: no copian ningún diccionario publicado.
"""

NIVEL = "1-medio"
IDIOMA = "es"

PALABRAS = """
protagonista|pro-ta-go-nis-ta|sustantivo masculino y femenino|Personaje principal de una historia.|héroe|antagonista|La protagonista busca a su hermano perdido.|literatura
antagonista|an-ta-go-nis-ta|sustantivo masculino y femenino|Personaje que se enfrenta al protagonista.|rival|protagonista|El antagonista engañó a todo el pueblo.|literatura
subordinada|su-bor-di-na-da|adjetivo|Dicho de una oración que depende de otra principal.|dependiente|principal|Subrayé la oración subordinada.|lengua
modalizador|mo-da-li-za-dor|sustantivo masculino|Palabra que muestra la actitud del hablante ante lo que dice.|-|-|«Quizás» es un modalizador de duda.|lengua
semántica|se-mán-ti-ca|sustantivo femenino|Parte de la lengua que estudia el significado.|-|-|La semántica analiza qué significan las palabras.|lengua
simbolismo|sim-bo-lis-mo|sustantivo masculino|Uso de símbolos para representar ideas.|-|-|El simbolismo de la paloma es la paz.|literatura
radicando|ra-di-can-do|sustantivo masculino|Número que está dentro del signo de raíz.|-|-|En la raíz de 81, el radicando es 81.|matemática
racional|ra-cio-nal|adjetivo|Dicho del número que se puede escribir como fracción.|-|irracional|El 0,5 es un número racional.|matemática
intersección|in-ter-sec-ción|sustantivo femenino|Punto o conjunto donde se cruzan dos figuras o conjuntos.|cruce|-|La intersección de las rectas es el punto (1, 2).|matemática
combinatoria|com-bi-na-to-ria|sustantivo femenino|Rama de la matemática que cuenta las formas de agrupar elementos.|-|-|La combinatoria resuelve problemas de ordenar objetos.|probabilidad
variable independiente|va-ria-ble in-de-pen-dien-te|locución nominal|Factor que el investigador cambia a propósito en un experimento.|-|variable dependiente|La temperatura fue la variable independiente.|ciencias
reacción|re-ac-ción|sustantivo femenino|Proceso en que unas sustancias se transforman en otras.|-|-|La reacción liberó burbujas de gas.|química
ecuación química|e-cua-ción quí-mi-ca|locución nominal|Forma escrita de representar una reacción con símbolos.|-|-|Balanceó la ecuación química.|química
frecuencia de onda|fre-cuen-cia de on-da|locución nominal|Número de ondas que pasan por un punto cada segundo.|-|-|La frecuencia de onda se mide en hertz.|física
cadena trófica|ca-de-na tró-fi-ca|locución nominal|Orden en que unos seres vivos sirven de alimento a otros.|cadena alimentaria|-|En la cadena trófica, el pasto alimenta al conejo.|ecología
patriota|pa-trio-ta|sustantivo masculino y femenino|Persona que ama a su patria y la defiende.|-|-|Los patriotas lucharon por la independencia.|historia
realista|re-a-lis-ta|sustantivo masculino y femenino|Partidario del rey en las guerras de independencia.|monárquico|patriota|Los realistas defendían la corona.|historia
inmigrante|in-mi-gran-te|sustantivo masculino y femenino|Persona que llega a un país distinto del suyo para vivir.|-|emigrante|Muchos inmigrantes trabajan en el comercio.|geografía
emigrante|e-mi-gran-te|sustantivo masculino y femenino|Persona que deja su país para vivir en otro.|-|inmigrante|Los emigrantes envían dinero a sus familias.|geografía
economía|e-co-no-mí-a|sustantivo femenino|Organización de la producción, el consumo y el dinero en una sociedad.|-|-|La economía del país creció este año.|economía
préstamo bancario|prés-ta-mo ban-ca-rio|locución nominal|Dinero que un banco entrega y que debe devolverse con intereses.|crédito|-|Pidieron un préstamo bancario para la casa.|economía
endeudamiento|en-deu-da-mien-to|sustantivo masculino|Situación de quien debe más dinero del que puede pagar con facilidad.|-|-|El endeudamiento familiar preocupa a los expertos.|economía
pueblo originario|pue-blo o-ri-gi-na-rio|locución nominal|Comunidad cuyos antepasados vivían en el territorio antes de la llegada de los colonizadores.|-|-|El pueblo mapuche es un pueblo originario.|cultura
solista|so-lis-ta|sustantivo masculino y femenino|Músico que toca o canta solo.|-|-|La solista cantó el último tema.|música
algoritmo de búsqueda|al-go-rit-mo de bús-que-da|locución nominal|Conjunto de reglas que usa un buscador para ordenar resultados.|-|-|El algoritmo de búsqueda priorizó las páginas más visitadas.|tecnología
resiliencia|re-si-lien-cia|sustantivo femenino|Capacidad de recuperarse después de una dificultad.|fortaleza|fragilidad|Su resiliencia le ayudó a superar la pérdida.|valores
conflicto de intereses|con-flic-to de in-te-re-ses|locución nominal|Situación en que alguien debe decidir entre su beneficio y su deber.|-|-|El juez se retiró por un conflicto de intereses.|ciudadanía
no obstante|no obs-tan-te|locución conjuntiva|Introduce una idea que se opone a la anterior.|sin embargo|-|El plan era bueno; no obstante, falló.|conectores
ciertamente|cier-ta-men-te|adverbio|Sin duda alguna.|seguramente|-|Ciertamente, tienes razón.|conectores
bruscamente|brus-ca-men-te|adverbio|De manera repentina y violenta.|de golpe|gradualmente|El auto frenó bruscamente.|conectores
indudable|in-du-da-ble|adjetivo|Que no admite duda.|seguro|dudoso|Su talento es indudable.|descripción
rudimentario|ru-di-men-ta-rio|adjetivo|Que es muy simple y poco desarrollado.|primitivo|sofisticado|Construyó un refugio rudimentario con ramas.|descripción
cuantioso|cuan-tio-so|adjetivo|Que es abundante en cantidad.|abundante|escaso|El terremoto dejó cuantiosos daños.|descripción
análisis|a-ná-li-sis|sustantivo masculino|Estudio detallado de las partes de algo.|examen|síntesis|Hicimos el análisis del poema.|vocabulario académico
síntesis|sín-te-sis|sustantivo femenino|Unión de varias partes en un todo breve y claro.|resumen|análisis|Escribe una síntesis de la clase.|vocabulario académico
objetivo del estudio|ob-je-ti-vo del es-tu-dio|locución nominal|Meta que se quiere alcanzar al investigar algo.|propósito|-|El objetivo del estudio es medir la contaminación.|vocabulario académico
metodología|me-to-do-lo-gí-a|sustantivo femenino|Conjunto de métodos que se siguen en una investigación.|-|-|La metodología incluyó encuestas y entrevistas.|vocabulario académico
relación|re-la-ción|sustantivo femenino|Conexión entre dos o más cosas.|vínculo|-|Existe una relación entre sueño y rendimiento.|vocabulario académico
correlación|co-rre-la-ción|sustantivo femenino|Relación entre dos cosas que cambian juntas.|-|-|Hay correlación entre estudio y buenas notas.|vocabulario académico
magnitud física|mag-ni-tud fí-si-ca|locución nominal|Propiedad que se puede medir, como la longitud o el tiempo.|-|-|La velocidad es una magnitud física.|física
lente|len-te|sustantivo femenino|Pieza transparente que desvía la luz para formar imágenes.|-|-|La lente del microscopio amplía la imagen.|física
solubilidad|so-lu-bi-li-dad|sustantivo femenino|Capacidad de una sustancia para disolverse.|-|-|La solubilidad de la sal aumenta con el calor.|química
cristal|cris-tal|sustantivo masculino|Sólido cuyas partículas están ordenadas de forma regular.|-|-|El azúcar forma cristales.|química
precisión|pre-ci-sión|sustantivo femenino|Exactitud al medir o hacer algo.|exactitud|imprecisión|La balanza mide con precisión.|ciencias
unión|u-nión|sustantivo femenino|Reunión de los elementos de dos o más conjuntos.|-|-|La unión de ambos conjuntos tiene seis elementos.|matemática
distancia|dis-tan-cia|sustantivo femenino|Espacio entre dos puntos.|separación|cercanía|La distancia entre las ciudades es de cien kilómetros.|matemática
tangente|tan-gen-te|sustantivo femenino|Recta que toca a una curva en un solo punto.|-|-|Dibujó una tangente a la circunferencia.|matemática
paralela|pa-ra-le-la|sustantivo femenino|Recta que nunca se cruza con otra.|-|-|Dibuja una paralela a esta línea.|matemática
oblicuo|o-bli-cuo|adjetivo|Que está inclinado, ni horizontal ni vertical.|inclinado|perpendicular|Trazó una línea oblicua.|matemática
diagonal|dia-go-nal|sustantivo femenino|Segmento que une dos vértices no consecutivos.|-|-|El cuadrado tiene dos diagonales.|matemática
tabulación|ta-bu-la-ción|sustantivo femenino|Ordenamiento de datos en una tabla.|-|-|La tabulación facilitó contar las respuestas.|estadística
complemento de un suceso|com-ple-men-to de un su-ce-so|locución nominal|Suceso que ocurre cuando el primero no ocurre.|-|-|El complemento de ganar es no ganar.|probabilidad
bocadillo|bo-ca-di-llo|sustantivo masculino|Globo con el texto que dicen los personajes de un cómic.|globo|-|El bocadillo muestra lo que piensa el héroe.|medios
podcast|pod-cast|sustantivo masculino|Programa de audio que se escucha por internet.|-|-|Escuchamos un podcast de historia.|medios
reputación|re-pu-ta-ción|sustantivo femenino|Opinión que la gente tiene sobre alguien.|fama|-|Cuida tu reputación en internet.|medios
rumor|ru-mor|sustantivo masculino|Noticia que corre sin que se sepa si es verdadera.|chisme|-|Se esparció un rumor sobre el colegio.|medios
cuarto|cuar-to|adjetivo numeral|Que ocupa el lugar número cuatro.|-|-|Quedó en cuarto lugar.|vida cotidiana
recibo|re-ci-bo|sustantivo masculino|Papel que prueba que se recibió algo o se pagó.|comprobante|-|Guarda el recibo de la compra.|vida cotidiana
entrevista laboral|en-tre-vis-ta la-bo-ral|locución nominal|Conversación con una empresa para ver si alguien sirve para un cargo.|-|-|Se preparó para la entrevista laboral.|vida cotidiana
beca|be-ca|sustantivo femenino|Ayuda económica para estudiar.|-|-|Ganó una beca para la universidad.|vida cotidiana
atochamiento|a-to-cha-mien-to|sustantivo masculino|Congestión de vehículos en una calle (uso en Chile).|taco|-|Hubo un atochamiento en la autopista.|vida cotidiana
vegetariano|ve-ge-ta-ria-no|adjetivo|Que no come carne.|-|carnívoro|Mi prima es vegetariana.|salud
anticoncepción|an-ti-con-cep-ción|sustantivo femenino|Uso de métodos para evitar un embarazo.|-|-|Hablamos de anticoncepción con una matrona.|salud
sedimentario|se-di-men-ta-rio|adjetivo|Dicho de las rocas formadas por acumulación de sedimentos.|-|-|La caliza es una roca sedimentaria.|geología
estequiometría|es-te-quio-me-trí-a|sustantivo femenino|Parte de la química que calcula las cantidades de sustancias que participan en una reacción.|-|-|La estequiometría permite saber cuánto producto se obtiene.|química
mol|mol|sustantivo masculino|Unidad que mide la cantidad de partículas de una sustancia.|-|-|Un mol de agua tiene dieciocho gramos.|química
masa molar|ma-sa mo-lar|locución nominal|Masa de un mol de una sustancia, expresada en gramos.|-|-|Calculé la masa molar del dióxido de carbono.|química
exotérmico|e-xo-tér-mi-co|adjetivo|Dicho de un proceso que libera calor.|-|endotérmico|La combustión es una reacción exotérmica.|química
endotérmico|en-do-tér-mi-co|adjetivo|Dicho de un proceso que absorbe calor.|-|exotérmico|Disolver ciertas sales es un proceso endotérmico.|química
velocidad de reacción|ve-lo-ci-dad de re-ac-ción|locución nominal|Rapidez con que unas sustancias se transforman en otras.|-|-|El calor aumenta la velocidad de reacción.|química
hidróxido|hi-dró-xi-do|sustantivo masculino|Compuesto que contiene el grupo formado por oxígeno e hidrógeno y suele ser una base.|-|-|El hidróxido de sodio se usa para hacer jabón.|química
óxido|ó-xi-do|sustantivo masculino|Compuesto formado por oxígeno y otro elemento; también, la capa rojiza que cubre al hierro.|herrumbre|-|El óxido cubrió la reja del patio.|química
electrolito|e-lec-tro-li-to|sustantivo masculino|Sustancia que, disuelta en agua, conduce la electricidad.|-|-|La sal es un electrolito en el agua.|química
enlace iónico|en-la-ce ió-ni-co|locución nominal|Unión entre átomos que se produce al transferirse electrones.|-|enlace covalente|La sal común tiene enlace iónico.|química
enlace covalente|en-la-ce co-va-len-te|locución nominal|Unión entre átomos que comparten electrones.|-|enlace iónico|En el agua hay enlaces covalentes.|química
valencia|va-len-cia|sustantivo femenino|Capacidad de un átomo para unirse con otros.|-|-|La valencia del oxígeno en el agua es dos.|química
isótopo|i-só-to-po|sustantivo masculino|Átomo del mismo elemento que tiene distinto número de neutrones.|-|-|El carbono catorce es un isótopo radiactivo.|química
número atómico|nú-me-ro a-tó-mi-co|locución nominal|Cantidad de protones que tiene el núcleo de un átomo.|-|-|El número atómico del hidrógeno es uno.|química
halógeno|ha-ló-ge-no|sustantivo masculino|Elemento de un grupo muy reactivo, como el cloro o el flúor.|-|-|El cloro es un halógeno.|química
gas noble|gas no-ble|locución nominal|Elemento que casi no reacciona con otros, como el helio.|-|-|El helio es un gas noble.|química
metaloide|me-ta-loi-de|sustantivo masculino|Elemento con propiedades intermedias entre un metal y un no metal.|-|-|El silicio es un metaloide.|química
hidrocarburo|hi-dro-car-bu-ro|sustantivo masculino|Compuesto formado solo por carbono e hidrógeno.|-|-|El petróleo es una mezcla de hidrocarburos.|química
fusión nuclear|fu-sión nu-cle-ar|locución nominal|Unión de dos núcleos atómicos que libera mucha energía.|-|fisión nuclear|La fusión nuclear ocurre en el Sol.|química
fisión nuclear|fi-sión nu-cle-ar|locución nominal|División de un núcleo atómico que libera energía.|-|fusión nuclear|Las centrales usan la fisión nuclear.|química
radiactividad|ra-diac-ti-vi-dad|sustantivo femenino|Capacidad de algunos átomos de emitir radiación al desintegrarse.|-|-|El uranio presenta radiactividad.|química
vida media|vi-da me-dia|locución nominal|Tiempo que tarda en desintegrarse la mitad de una muestra radiactiva.|-|-|La vida media de ese isótopo es de cinco años.|química
onda sísmica|on-da sís-mi-ca|locución nominal|Vibración que viaja por la Tierra durante un sismo.|-|-|Las ondas sísmicas llegaron en segundos.|geología
falla geológica|fa-lla geo-ló-gi-ca|locución nominal|Fractura de la corteza terrestre donde se mueven bloques de roca.|-|-|La falla geológica cruza el valle.|geología
dorsal oceánica|dor-sal o-ce-á-ni-ca|locución nominal|Cadena de montañas submarinas donde se forma nueva corteza.|-|-|La dorsal oceánica separa dos placas.|geología
fosa oceánica|fo-sa o-ce-á-ni-ca|locución nominal|Zona muy profunda del fondo del mar.|-|-|La fosa oceánica de Atacama es muy profunda.|geología
cinturón de fuego|cin-tu-rón de fue-go|locución nominal|Zona alrededor del océano Pacífico con muchos volcanes y sismos.|-|-|Chile está en el cinturón de fuego del Pacífico.|geología
vulcanismo|vul-ca-nis-mo|sustantivo masculino|Conjunto de fenómenos relacionados con la salida de magma a la superficie.|-|-|El vulcanismo forma nuevas islas.|geología
caldera|cal-de-ra|sustantivo femenino|Gran depresión circular que queda tras la explosión de un volcán.|-|-|La caldera se llenó de agua y formó un lago.|geología
napa freática|na-pa fre-á-ti-ca|locución nominal|Agua subterránea que está cerca de la superficie.|-|-|La napa freática alimenta el pozo.|geología
escorrentía|es-co-rren-tí-a|sustantivo femenino|Agua que corre por la superficie del terreno.|-|-|La escorrentía arrastró tierra hacia el río.|geología
infiltración|in-fil-tra-ción|sustantivo femenino|Paso lento del agua a través del suelo.|-|-|La infiltración recarga el acuífero.|geología
humedad relativa|hu-me-dad re-la-ti-va|locución nominal|Cantidad de vapor de agua del aire respecto de la máxima posible.|-|-|La humedad relativa en la costa es alta.|clima
brisa|bri-sa|sustantivo femenino|Viento suave.|-|-|La brisa marina refresca la tarde.|clima
corriente de Humboldt|co-rrien-te de Hum-boldt|locución nominal|Corriente de agua fría que baja por la costa de Chile.|-|-|La corriente de Humboldt es rica en peces.|clima
resaca|re-sa-ca|sustantivo femenino|Movimiento de retroceso de las olas hacia el mar.|-|-|La resaca puede arrastrar a los bañistas.|clima
riesgo natural|ries-go na-tu-ral|locución nominal|Posibilidad de que un fenómeno de la naturaleza cause daño.|-|-|El aluvión es un riesgo natural en la zona.|geología
vulnerabilidad|vul-ne-ra-bi-li-dad|sustantivo femenino|Facilidad con que algo o alguien puede sufrir daño.|fragilidad|resistencia|La vulnerabilidad de las casas antiguas es alta.|geología
mitigación|mi-ti-ga-ción|sustantivo femenino|Disminución de los efectos negativos de algo.|atenuación|-|La mitigación del riesgo incluye normas de construcción.|geología
escala gráfica|es-ca-la grá-fi-ca|locución nominal|Línea dibujada en un mapa que muestra la relación con las distancias reales.|-|-|Mide la distancia con la escala gráfica.|geografía
coordenadas geográficas|coor-de-na-das geo-grá-fi-cas|locución nominal|Pareja de números, latitud y longitud, que ubican un punto en la Tierra.|-|-|Anotamos las coordenadas geográficas del faro.|geografía
zona templada|zo-na tem-pla-da|locución nominal|Región de clima moderado entre los trópicos y los polos.|-|-|Chile central está en la zona templada.|geografía
depresión intermedia|de-pre-sión in-ter-me-dia|locución nominal|Llanura que está entre la cordillera de los Andes y la de la Costa.|-|-|El valle central es parte de la depresión intermedia.|geografía
cordillera de la Costa|cor-di-lle-ra de la Cos-ta|locución nominal|Cadena de montañas que corre cerca del mar en Chile.|-|-|La cordillera de la Costa es más baja que los Andes.|geografía
islote|is-lo-te|sustantivo masculino|Isla muy pequeña.|-|-|Un islote rocoso está frente al puerto.|geografía
precordillera|pre-cor-di-lle-ra|sustantivo femenino|Zona de cerros al pie de una cordillera.|-|-|Hicimos una excursión por la precordillera.|geografía
parque nacional|par-que na-cio-nal|locución nominal|Territorio protegido por el Estado para conservar la naturaleza.|-|-|Visitamos el parque nacional Torres del Paine.|ecología
especie endémica|es-pe-cie en-dé-mi-ca|locución nominal|Especie que vive solo en un lugar determinado.|-|especie introducida|El monito del monte es una especie endémica.|ecología
especie introducida|es-pe-cie in-tro-du-ci-da|locución nominal|Especie llevada por el ser humano a un lugar donde no vivía.|-|especie endémica|El castor es una especie introducida en Tierra del Fuego.|ecología
plaga|pla-ga|sustantivo femenino|Gran cantidad de seres vivos que dañan cultivos o lugares.|-|-|Una plaga de langostas arrasó los campos.|ecología
mimetismo|mi-me-tis-mo|sustantivo masculino|Capacidad de un animal de parecerse a su entorno para no ser visto.|camuflaje|-|El mimetismo del camaleón lo protege.|ecología
era geológica|e-ra geo-ló-gi-ca|locución nominal|Gran división del tiempo de la historia de la Tierra.|-|-|Vivimos en la era Cenozoica.|geología
dinosaurio|di-no-sau-rio|sustantivo masculino|Reptil gigante que vivió hace millones de años.|-|-|Los dinosaurios se extinguieron hace mucho tiempo.|biología
artrópodo|ar-tró-po-do|sustantivo masculino|Animal invertebrado con patas articuladas y cuerpo con caparazón.|-|-|Las arañas son artrópodos.|biología
molusco|mo-lus-co|sustantivo masculino|Animal invertebrado de cuerpo blando, a veces con concha.|-|-|El caracol es un molusco.|biología
crustáceo|crus-tá-ce-o|sustantivo masculino|Animal de caparazón duro que vive sobre todo en el agua.|-|-|El cangrejo es un crustáceo.|biología
conífera|co-ní-fe-ra|sustantivo femenino|Árbol que da frutos en forma de cono, como el pino.|-|-|La conífera mantiene sus hojas todo el año.|biología
estambre|es-tam-bre|sustantivo masculino|Parte masculina de una flor, que produce polen.|-|-|El estambre está rodeado de pétalos.|biología
pistilo|pis-ti-lo|sustantivo masculino|Parte femenina de una flor, que contiene el óvulo.|-|-|El pistilo recibe el polen.|biología
homeostasis|ho-me-os-ta-sis|sustantivo femenino|Capacidad del cuerpo de mantener estable su medio interno.|-|-|La homeostasis regula la temperatura corporal.|biología
enzima|en-zi-ma|sustantivo femenino|Proteína que acelera las reacciones químicas del cuerpo.|-|-|La enzima de la saliva comienza a digerir el almidón.|biología
aminoácido|a-mi-no-á-ci-do|sustantivo masculino|Compuesto que forma las proteínas.|-|-|Los aminoácidos se unen para formar proteínas.|biología
ARN|a-e-rre-e-ne|sustantivo masculino|Molécula que ayuda a fabricar proteínas a partir del ADN.|-|-|El ARN lleva la copia del gen hasta el ribosoma.|biología
replicación|re-pli-ca-ción|sustantivo femenino|Proceso en que una molécula de ADN se copia a sí misma.|copia|-|La replicación ocurre antes de dividirse la célula.|biología
genoma|ge-no-ma|sustantivo masculino|Conjunto completo de los genes de un ser vivo.|-|-|Se logró leer el genoma humano.|biología
genotipo|ge-no-ti-po|sustantivo masculino|Conjunto de genes que tiene un individuo.|-|fenotipo|El genotipo determina muchos rasgos.|biología
fenotipo|fe-no-ti-po|sustantivo masculino|Rasgos visibles de un individuo, resultado de sus genes y del ambiente.|-|genotipo|El color de ojos es parte del fenotipo.|biología
alelo|a-le-lo|sustantivo masculino|Cada una de las versiones posibles de un gen.|-|-|Heredé un alelo de cada progenitor.|biología
dominante|do-mi-nan-te|adjetivo|Dicho del rasgo que se manifiesta aunque solo se herede una copia del gen.|-|recesivo|El pelo oscuro es dominante.|biología
recesivo|re-ce-si-vo|adjetivo|Dicho del rasgo que solo se manifiesta con dos copias del gen.|-|dominante|El pelo rojo es un rasgo recesivo.|biología
cruzamiento|cru-za-mien-to|sustantivo masculino|Unión de dos individuos para obtener descendencia.|-|-|El cruzamiento de plantas dio flores nuevas.|biología
árbol genealógico|ár-bol ge-nea-ló-gi-co|locución nominal|Esquema que muestra los parentescos de una familia.|-|-|Dibujé mi árbol genealógico hasta mis bisabuelos.|biología
meiosis|mei-o-sis|sustantivo femenino|División celular que produce las células sexuales.|-|mitosis|En la meiosis se forman los gametos.|biología
mitosis|mi-to-sis|sustantivo femenino|División celular que produce dos células idénticas.|-|meiosis|La mitosis permite el crecimiento.|biología
ciclo celular|ci-clo ce-lu-lar|locución nominal|Etapas de la vida de una célula hasta que se divide.|-|-|El ciclo celular incluye la replicación del ADN.|biología
feto|fe-to|sustantivo masculino|Ser humano en desarrollo en el vientre, desde el tercer mes de embarazo.|-|-|El feto crece protegido por el útero.|biología
parto|par-to|sustantivo masculino|Momento en que nace un bebé.|alumbramiento|-|El parto ocurrió en el hospital.|salud
lactancia|lac-tan-cia|sustantivo femenino|Período en que un bebé se alimenta con leche materna.|-|-|La lactancia fortalece las defensas del bebé.|salud
ciclo menstrual|ci-clo mens-trual|locución nominal|Cambios mensuales del cuerpo femenino relacionados con la ovulación.|-|-|El ciclo menstrual dura cerca de un mes.|salud
ovario|o-va-rio|sustantivo masculino|Órgano femenino que produce los óvulos.|-|-|El ovario libera un óvulo cada mes.|salud
útero|ú-te-ro|sustantivo masculino|Órgano donde se desarrolla un bebé antes de nacer.|matriz|-|El útero cambia de tamaño durante el embarazo.|salud
infertilidad|in-fer-ti-li-dad|sustantivo femenino|Dificultad para lograr un embarazo.|esterilidad|fertilidad|La infertilidad tiene tratamientos médicos.|salud
infección de transmisión sexual|in-fec-ción de trans-mi-sión se-xual|locución nominal|Enfermedad que se contagia por contacto sexual.|-|-|Prevenir una infección de transmisión sexual es posible.|salud
preservativo|pre-ser-va-ti-vo|sustantivo masculino|Funda delgada que protege del embarazo y de infecciones en el contacto sexual.|condón|-|El preservativo es un método de protección.|salud
método anticonceptivo|mé-to-do an-ti-con-cep-ti-vo|locución nominal|Recurso para evitar un embarazo.|-|-|Un médico explica cada método anticonceptivo.|salud
planificación familiar|pla-ni-fi-ca-ción fa-mi-liar|locución nominal|Decisión de una pareja sobre cuántos hijos tener y cuándo.|-|-|La planificación familiar es un derecho.|salud
paternidad|pa-ter-ni-dad|sustantivo femenino|Condición de ser padre.|-|-|La paternidad implica responsabilidades.|salud
maternidad|ma-ter-ni-dad|sustantivo femenino|Condición de ser madre.|-|-|La maternidad cambió su rutina.|salud
crianza|cri-an-za|sustantivo femenino|Cuidado y educación de un niño.|-|-|La crianza se comparte entre la familia.|salud
identidad de género|i-den-ti-dad de gé-ne-ro|locución nominal|Forma en que cada persona se siente y se define respecto del género.|-|-|La identidad de género debe respetarse.|salud
orientación sexual|o-rien-ta-ción se-xual|locución nominal|Atracción afectiva y sexual que una persona siente hacia otras.|-|-|Todos merecen respeto sin importar su orientación sexual.|salud
consentimiento informado|con-sen-ti-mien-to in-for-ma-do|locución nominal|Aceptación libre de un tratamiento después de entender sus riesgos.|-|-|El paciente firmó el consentimiento informado.|salud
violencia de género|vio-len-cia de gé-ne-ro|locución nominal|Daño que se hace a alguien por su condición de género.|-|-|La violencia de género se puede denunciar.|salud
redes de apoyo|re-des de a-po-yo|locución nominal|Personas e instituciones que ayudan a alguien en momentos difíciles.|-|-|Las redes de apoyo ayudan en una crisis.|salud
género narrativo|gé-ne-ro na-rra-ti-vo|locución nominal|Conjunto de obras que cuentan hechos, como el cuento y la novela.|-|-|El cuento pertenece al género narrativo.|literatura
género dramático|gé-ne-ro dra-má-ti-co|locución nominal|Conjunto de obras escritas para ser representadas ante un público.|-|-|La tragedia es parte del género dramático.|literatura
género lírico|gé-ne-ro lí-ri-co|locución nominal|Conjunto de obras que expresan sentimientos, como el poema y la canción.|-|-|La oda es una obra del género lírico.|literatura
microcuento|mi-cro-cuen-to|sustantivo masculino|Cuento extremadamente breve.|-|-|Escribí un microcuento de tres líneas.|literatura
novela histórica|no-ve-la his-tó-ri-ca|locución nominal|Novela cuyos hechos ocurren en una época del pasado.|-|-|La novela histórica narra la vida en la colonia.|literatura
ciencia ficción|cien-cia fic-ción|locución nominal|Género que imagina mundos y tecnologías futuras.|-|-|Me gustan las películas de ciencia ficción.|literatura
realismo mágico|re-a-lis-mo má-gi-co|locución nominal|Estilo en que lo extraordinario aparece como algo normal en la vida diaria.|-|-|El realismo mágico es muy frecuente en la narrativa latinoamericana.|literatura
costumbrismo|cos-tum-bris-mo|sustantivo masculino|Estilo que muestra las costumbres típicas de un lugar.|-|-|El costumbrismo retrata la vida del campo.|literatura
romanticismo|ro-man-ti-cis-mo|sustantivo masculino|Movimiento artístico del siglo XIX que da importancia a los sentimientos.|-|-|El romanticismo exalta la libertad y la pasión.|literatura
modernismo|mo-der-nis-mo|sustantivo masculino|Movimiento literario hispanoamericano de fines del siglo XIX, de gran belleza formal.|-|-|El modernismo cuidó la musicalidad de los versos.|literatura
naturalismo|na-tu-ra-lis-mo|sustantivo masculino|Estilo que muestra la realidad con gran detalle y crudeza.|-|-|El naturalismo describe la vida de los obreros.|literatura
caligrama|ca-li-gra-ma|sustantivo masculino|Poema cuyas letras forman un dibujo.|-|-|El caligrama tiene forma de paloma.|literatura
verso libre|ver-so li-bre|locución nominal|Verso que no sigue una medida ni una rima fijas.|-|-|El poeta escribió en verso libre.|literatura
endecasílabo|en-de-ca-sí-la-bo|sustantivo masculino|Verso de once sílabas.|-|-|El soneto se escribe en endecasílabos.|literatura
octosílabo|oc-to-sí-la-bo|sustantivo masculino|Verso de ocho sílabas.|-|-|La copla popular usa octosílabos.|literatura
heptasílabo|hep-ta-sí-la-bo|sustantivo masculino|Verso de siete sílabas.|-|-|El heptasílabo se combina con endecasílabos.|literatura
sinalefa|si-na-le-fa|sustantivo femenino|Unión en una sola sílaba de la vocal final de una palabra y la inicial de la siguiente al medir un verso.|-|-|Por la sinalefa, «la hora» cuenta como dos sílabas.|literatura
rima asonante|ri-ma a-so-nan-te|locución nominal|Coincidencia solo de las vocales a partir de la última vocal fuerte.|-|rima consonante|«Casa» y «palma» tienen rima asonante.|literatura
rima consonante|ri-ma con-so-nan-te|locución nominal|Coincidencia de todos los sonidos a partir de la última vocal fuerte.|-|rima asonante|«Canción» y «razón» tienen rima consonante.|literatura
terceto|ter-ce-to|sustantivo masculino|Estrofa de tres versos.|-|cuarteto|El soneto termina con dos tercetos.|literatura
balada|ba-la-da|sustantivo femenino|Poema o canción de tono suave que cuenta una historia sentimental.|-|-|La balada habla de un amor lejano.|literatura
égloga|é-glo-ga|sustantivo femenino|Poema que presenta la vida del campo y el amor de pastores.|-|-|La égloga idealiza la naturaleza.|literatura
epigrama|e-pi-gra-ma|sustantivo masculino|Poema breve y agudo, a menudo burlesco.|-|-|El epigrama se burló de un político.|literatura
aforismo|a-fo-ris-mo|sustantivo masculino|Frase corta que resume una enseñanza o una verdad.|máxima|-|Anotó un aforismo en su cuaderno.|literatura
adagio|a-da-gio|sustantivo masculino|Frase breve de sabiduría popular.|refrán|-|El adagio dice que no hay mal que dure cien años.|literatura
cantar de gesta|can-tar de ges-ta|locución nominal|Poema medieval que narra las hazañas de un héroe.|-|-|El Cantar de Mio Cid es un cantar de gesta.|literatura
picaresca|pi-ca-res-ca|sustantivo femenino|Tipo de novela que narra las aventuras de un pícaro.|-|-|La picaresca critica los abusos de la sociedad.|literatura
entremés|en-tre-més|sustantivo masculino|Pieza teatral corta y cómica que se presentaba entre actos.|-|-|El entremés hizo reír al público.|literatura
tragicomedia|tra-gi-co-me-dia|sustantivo femenino|Obra que mezcla elementos trágicos y cómicos.|-|-|La tragicomedia combina risas y lágrimas.|literatura
farsa|far-sa|sustantivo femenino|Obra de teatro cómica y exagerada.|-|-|La farsa parodiaba a los nobles.|literatura
sainete|sai-ne-te|sustantivo masculino|Obra de teatro breve y cómica que retrata costumbres populares.|-|-|El sainete muestra la vida del barrio.|literatura
melodrama|me-lo-dra-ma|sustantivo masculino|Obra de intensa emoción, con buenos y malos muy marcados.|-|-|El melodrama hizo llorar a la sala.|literatura
soliloquio|so-li-lo-quio|sustantivo masculino|Discurso de un personaje que habla consigo mismo.|monólogo|diálogo|El soliloquio revela las dudas del príncipe.|literatura
tramoya|tra-mo-ya|sustantivo femenino|Conjunto de máquinas con que se hacen los cambios en el escenario.|-|-|La tramoya hizo bajar el telón.|teatro
telón|te-lón|sustantivo masculino|Cortina grande que separa el escenario del público.|-|-|El telón se abrió al comenzar la función.|teatro
utilería|u-ti-le-rí-a|sustantivo femenino|Objetos que usan los actores en escena.|-|-|La utilería incluía una espada y una carta.|teatro
estreno|es-tre-no|sustantivo masculino|Primera presentación de una obra o película.|debut|-|Fuimos al estreno de la obra.|teatro
taquilla|ta-qui-lla|sustantivo femenino|Lugar donde se venden las entradas.|boletería|-|Hicimos fila en la taquilla del teatro.|teatro
butaca|bu-ta-ca|sustantivo femenino|Asiento cómodo de un teatro o cine.|-|-|Mi butaca estaba en primera fila.|teatro
platea|pla-te-a|sustantivo femenino|Parte baja de un teatro donde se sienta el público frente al escenario.|-|-|Nos sentamos en la platea.|teatro
bastidor|bas-ti-dor|sustantivo masculino|Armazón de madera cubierto con tela que sirve de decorado.|-|-|Los bastidores formaban un bosque pintado.|teatro
proscenio|pros-ce-nio|sustantivo masculino|Parte del escenario más cercana al público.|-|-|El actor avanzó hasta el proscenio.|teatro
mimo|mi-mo|sustantivo masculino|Actor que expresa todo con gestos, sin hablar.|-|-|El mimo imitó a un pájaro.|teatro
títere|tí-te-re|sustantivo masculino|Muñeco que se mueve con las manos o con hilos.|marioneta|-|El títere saludó a los niños.|teatro
marioneta|ma-rio-ne-ta|sustantivo femenino|Muñeco articulado que se maneja con hilos.|títere|-|Las marionetas bailaban en el escenario.|teatro
narrador omnisciente|na-rra-dor om-nis-cien-te|locución nominal|Narrador que lo sabe todo sobre la historia y los personajes.|-|-|El narrador omnisciente conoce lo que piensan todos.|literatura
narrador testigo|na-rra-dor tes-ti-go|locución nominal|Narrador que cuenta lo que ve, sin ser el protagonista.|-|-|El narrador testigo observa desde afuera.|literatura
narrador protagonista|na-rra-dor pro-ta-go-nis-ta|locución nominal|Narrador que cuenta su propia historia.|-|-|El narrador protagonista usa la primera persona.|literatura
focalización|fo-ca-li-za-ción|sustantivo femenino|Punto de vista desde el que se cuenta lo que ocurre.|-|-|La focalización limita lo que sabe el lector.|literatura
analepsis|a-na-lep-sis|sustantivo femenino|Salto del relato hacia un hecho anterior.|retrospección|prolepsis|La analepsis muestra la infancia del héroe.|literatura
prolepsis|pro-lep-sis|sustantivo femenino|Anticipación en el relato de algo que ocurrirá después.|anticipación|analepsis|La prolepsis avisa del trágico final.|literatura
elipsis|e-lip-sis|sustantivo femenino|Omisión de un tramo de tiempo o de una palabra sin que se pierda el sentido.|omisión|-|Una elipsis salta diez años en la historia.|literatura
flashback|flash-back|sustantivo masculino|Escena que regresa al pasado dentro de un relato.|retrospección|-|La película usa un flashback para explicar el secreto.|literatura
episodio|e-pi-so-dio|sustantivo masculino|Cada hecho o parte de una historia.|capítulo|-|El episodio del naufragio es el más largo.|literatura
digresión|di-gre-sión|sustantivo femenino|Parte de un texto que se aparta del tema principal.|desvío|-|La digresión interrumpe la historia principal.|literatura
etopeya|e-to-pe-ya|sustantivo femenino|Descripción del carácter y las costumbres de un personaje.|-|-|La etopeya muestra que el hombre era generoso.|literatura
estilo directo|es-ti-lo di-rec-to|locución nominal|Forma de reproducir las palabras exactas de un personaje.|-|estilo indirecto|En estilo directo, el diálogo lleva guiones.|lengua
estilo indirecto|es-ti-lo in-di-rec-to|locución nominal|Forma en que el narrador cuenta lo que dijo un personaje.|-|estilo directo|En estilo indirecto, dijo que vendría.|lengua
monólogo interior|mo-nó-lo-go in-te-rior|locución nominal|Pensamientos de un personaje presentados tal como surgen en su mente.|-|-|El monólogo interior mostró su angustia.|literatura
flujo de conciencia|flu-jo de con-cien-cia|locución nominal|Técnica que reproduce el desorden natural de los pensamientos.|-|-|Joyce usó el flujo de conciencia.|literatura
verosimilitud|ve-ro-si-mi-li-tud|sustantivo femenino|Cualidad de parecer creíble o posible.|credibilidad|-|La verosimilitud hace que creamos la historia.|literatura
intertextualidad|in-ter-tex-tua-li-dad|sustantivo femenino|Relación entre un texto y otros textos anteriores.|-|-|La intertextualidad aparece cuando se cita otra obra.|literatura
alusión|a-lu-sión|sustantivo femenino|Mención breve e indirecta de algo.|referencia|-|Hizo una alusión al mito de Ícaro.|literatura
obra clásica|o-bra clá-si-ca|locución nominal|Obra que se sigue valorando con el paso del tiempo.|-|-|El Quijote es una obra clásica.|literatura
bestseller|best-sell-er|sustantivo masculino|Libro que se vende en gran cantidad.|-|-|La novela se convirtió en un bestseller.|literatura
club de lectura|club de lec-tu-ra|locución nominal|Grupo de personas que leen y comentan libros juntas.|-|-|Mi club de lectura se reúne los jueves.|literatura
ficha de lectura|fi-cha de lec-tu-ra|locución nominal|Tarjeta o documento con datos y comentarios de un libro leído.|-|-|Completé la ficha de lectura de la novela.|literatura
crítica|crí-ti-ca|sustantivo femenino|Juicio sobre las cualidades y defectos de una obra.|reseña|elogio|La crítica elogió el estreno.|literatura
comentario|co-men-ta-rio|sustantivo masculino|Texto que explica u opina sobre algo.|observación|-|Escribí un comentario sobre el poema.|literatura
artículo de opinión|ar-tí-cu-lo de o-pi-nión|locución nominal|Texto en que alguien expresa su punto de vista sobre un tema.|-|-|Publicó un artículo de opinión sobre el transporte.|medios
carta al director|car-ta al di-rec-tor|locución nominal|Escrito que un lector envía a un diario para dar su opinión.|-|-|Mandó una carta al director sobre la plaza.|medios
ejemplificación|e-jem-pli-fi-ca-ción|sustantivo femenino|Recurso que usa ejemplos para aclarar una idea.|-|-|La ejemplificación ayuda a entender el tema.|lengua
clasificación|cla-si-fi-ca-ción|sustantivo femenino|Ordenamiento de cosas en grupos según sus características.|-|-|La clasificación de los animales incluye mamíferos y aves.|lengua
enumeración|e-nu-me-ra-ción|sustantivo femenino|Presentación de varios elementos uno tras otro.|lista|-|En la enumeración usé comas.|lengua
causa y efecto|cau-sa y e-fec-to|locución nominal|Estructura de un texto que explica por qué ocurre algo y qué resulta de ello.|-|-|La sequía explica una relación de causa y efecto.|lengua
estructura textual|es-truc-tu-ra tex-tual|locución nominal|Forma en que se organizan las partes de un texto.|-|-|Identifica la estructura textual del artículo.|lengua
subtema|sub-te-ma|sustantivo masculino|Tema secundario dentro de un tema mayor.|-|-|Cada párrafo desarrolla un subtema.|lengua
idea secundaria|i-de-a se-cun-da-ria|locución nominal|Idea que apoya o amplía la idea principal.|-|idea principal|Subraya la idea secundaria del párrafo.|lengua
lectura crítica|lec-tu-ra crí-ti-ca|locución nominal|Lectura que evalúa lo que dice el texto y cómo lo dice.|-|-|La lectura crítica detecta errores en los argumentos.|lengua
intención comunicativa|in-ten-ción co-mu-ni-ca-ti-va|locución nominal|Propósito con que alguien escribe o habla.|-|-|La intención comunicativa del afiche es informar.|lengua
destinatario|des-ti-na-ta-rio|sustantivo masculino|Persona a quien va dirigido un mensaje.|receptor|emisor|El destinatario de la carta es el alcalde.|lengua
ruido|rui-do|sustantivo masculino|Cualquier factor que dificulta entender un mensaje.|interferencia|-|El ruido de la calle impidió oír el mensaje.|lengua
función referencial|fun-ción re-fe-ren-cial|locución nominal|Uso del lenguaje para informar sobre hechos o cosas.|-|-|Las noticias cumplen una función referencial.|lengua
función emotiva|fun-ción e-mo-ti-va|locución nominal|Uso del lenguaje para expresar emociones del emisor.|-|-|Un poema de amor tiene función emotiva.|lengua
función apelativa|fun-ción a-pe-la-ti-va|locución nominal|Uso del lenguaje para influir en el receptor.|-|-|La publicidad usa la función apelativa.|lengua
función poética|fun-ción po-é-ti-ca|locución nominal|Uso del lenguaje que busca belleza en la forma del mensaje.|-|-|Los versos usan la función poética.|lengua
función fática|fun-ción fá-ti-ca|locución nominal|Uso del lenguaje para iniciar o mantener la comunicación.|-|-|«¿Aló?» cumple una función fática.|lengua
lenguaje verbal|len-gua-je ver-bal|locución nominal|Comunicación que usa palabras.|-|lenguaje no verbal|Una carta usa lenguaje verbal.|lengua
lenguaje no verbal|len-gua-je no ver-bal|locución nominal|Comunicación que usa gestos, imágenes o sonidos en lugar de palabras.|-|lenguaje verbal|Una sonrisa es lenguaje no verbal.|lengua
paralenguaje|pa-ra-len-gua-je|sustantivo masculino|Elementos de la voz que acompañan las palabras, como el tono o la risa.|-|-|El paralenguaje transmite si hablamos con enojo.|lengua
kinésica|ki-né-si-ca|sustantivo femenino|Estudio de los gestos y movimientos del cuerpo al comunicar.|-|-|La kinésica analiza el lenguaje corporal.|lengua
proxémica|pro-xé-mi-ca|sustantivo femenino|Estudio del uso de la distancia entre las personas al comunicarse.|-|-|La proxémica explica cuánto espacio dejamos al conversar.|lengua
tono de voz|to-no de voz|locución nominal|Modo en que alguien sube o baja la voz al hablar.|-|-|Su tono de voz mostraba enojo.|lengua
vocalización|vo-ca-li-za-ción|sustantivo femenino|Forma clara de pronunciar los sonidos al hablar.|dicción|-|Practiqué la vocalización antes del discurso.|lengua
coloquialismo|co-lo-quia-lis-mo|sustantivo masculino|Palabra o expresión propia de la conversación diaria.|-|-|«Pasarlo bomba» es un coloquialismo.|lengua
argot|ar-got|sustantivo masculino|Lenguaje propio de un grupo o profesión.|jerga|-|El argot de los marineros es difícil de entender.|lengua
coa|co-a|sustantivo femenino|Jerga de ciertos grupos en Chile (uso en Chile).|jerga|-|Aprendió palabras de la coa en un libro.|lengua
vulgarismo|vul-ga-ris-mo|sustantivo masculino|Palabra o forma que se considera incorrecta en la norma culta.|-|-|«Haiga» es un vulgarismo.|lengua
barbarismo|bar-ba-ris-mo|sustantivo masculino|Error al escribir o pronunciar una palabra.|-|-|«Dijistes» es un barbarismo.|lengua
anglicismo|an-gli-cis-mo|sustantivo masculino|Palabra o expresión tomada del inglés.|-|-|«Hobby» es un anglicismo.|lengua
galicismo|ga-li-cis-mo|sustantivo masculino|Palabra o expresión tomada del francés.|-|-|«Chofer» es un galicismo.|lengua
latinismo|la-ti-nis-mo|sustantivo masculino|Palabra o expresión tomada del latín.|-|-|«Ítem» es un latinismo.|lengua
indigenismo|in-di-ge-nis-mo|sustantivo masculino|Palabra de origen indígena incorporada al español.|-|-|«Chocolate» es un indigenismo.|lengua
lengua originaria|len-gua o-ri-gi-na-ria|locución nominal|Lengua propia de los pueblos que habitaban un territorio antes de la colonización.|-|-|El mapudungun es una lengua originaria.|lengua
lengua materna|len-gua ma-ter-na|locución nominal|Primera lengua que aprende una persona.|-|-|Mi lengua materna es el español.|lengua
bilingüismo|bi-lin-güis-mo|sustantivo masculino|Uso habitual de dos lenguas por una persona o comunidad.|-|-|El bilingüismo ayuda a conocer otras culturas.|lengua
variación lingüística|va-ria-ción lin-güís-ti-ca|locución nominal|Diferencias en la manera de hablar una misma lengua.|-|-|La variación lingüística depende de la región.|lengua
norma culta|nor-ma cul-ta|locución nominal|Modo de hablar y escribir que usan las personas con más educación formal.|-|-|En una exposición se usa la norma culta.|lengua
academia|a-ca-de-mia|sustantivo femenino|Institución que cuida y regula una lengua o una ciencia.|-|-|La academia incorporó nuevas palabras.|lengua
tesauro|te-sau-ro|sustantivo masculino|Diccionario de sinónimos y palabras relacionadas.|-|-|Busqué una palabra en el tesauro.|lengua
afijo|a-fi-jo|sustantivo masculino|Partícula que se une a una palabra, como un prefijo o un sufijo.|-|-|«Des-» es un afijo.|lengua
lexema|le-xe-ma|sustantivo masculino|Parte de una palabra que contiene su significado básico.|raíz|-|En «niñez» el lexema es «niñ».|lengua
morfema|mor-fe-ma|sustantivo masculino|Parte mínima de una palabra con significado gramatical.|-|-|El plural se marca con un morfema.|lengua
familia de palabras|fa-mi-lia de pa-la-bras|locución nominal|Grupo de palabras que comparten la misma raíz.|-|-|«Pan», «panadero» y «panadería» son una familia de palabras.|lengua
palabra compuesta|pa-la-bra com-pues-ta|locución nominal|Palabra formada por la unión de dos o más palabras.|-|-|«Paraguas» es una palabra compuesta.|lengua
palabra derivada|pa-la-bra de-ri-va-da|locución nominal|Palabra formada al añadir un prefijo o sufijo a otra.|-|-|«Zapatero» es una palabra derivada.|lengua
siglas|si-glas|sustantivo femenino plural|Palabra formada con las letras iniciales de varias palabras.|-|-|«ONU» es una de las siglas más conocidas.|lengua
apócope|a-pó-co-pe|sustantivo femenino|Pérdida de uno o más sonidos al final de una palabra.|-|-|«Primer» es una apócope de «primero».|lengua
Estado-nación|Es-ta-do-na-ción|sustantivo masculino|País organizado como Estado cuyos habitantes comparten una identidad nacional.|-|-|En el siglo XIX se formaron los Estados-nación de América.|historia
nacionalismo|na-cio-na-lis-mo|sustantivo masculino|Ideología que valora la propia nación y su identidad.|patriotismo|-|El nacionalismo impulsó las guerras de independencia.|historia
liberalismo|li-be-ra-lis-mo|sustantivo masculino|Doctrina que defiende las libertades individuales y limita el poder del Estado.|-|-|El liberalismo defendió la libertad de prensa.|historia
conservadurismo|con-ser-va-du-ris-mo|sustantivo masculino|Doctrina que prefiere mantener las tradiciones y los cambios graduales.|-|-|El conservadurismo defendía el orden tradicional.|historia
socialismo|so-cia-lis-mo|sustantivo masculino|Doctrina que busca que los medios de producción y la riqueza se repartan con equidad.|-|capitalismo|El socialismo nació con el movimiento obrero.|historia
capitalismo|ca-pi-ta-lis-mo|sustantivo masculino|Sistema económico basado en la propiedad privada y el mercado libre.|-|socialismo|En el capitalismo las empresas buscan ganancias.|historia
industrialización|in-dus-tria-li-za-ción|sustantivo femenino|Proceso en que un país pasa de una economía agrícola a una basada en fábricas.|-|-|La industrialización cambió las ciudades.|historia
Revolución Industrial|Re-vo-lu-ción In-dus-trial|locución nominal|Período de grandes cambios técnicos y económicos desde el siglo XVIII con las máquinas y las fábricas.|-|-|La Revolución Industrial comenzó en Inglaterra.|historia
proletariado|pro-le-ta-ria-do|sustantivo masculino|Clase social formada por los trabajadores que viven de su salario.|-|burguesía|El proletariado se organizó en sindicatos.|historia
cuestión social|cues-tión so-cial|locución nominal|Conjunto de problemas de pobreza y mal trato a los obreros a fines del siglo XIX en Chile.|-|-|La cuestión social llevó a exigir leyes laborales.|historia
parlamentarismo|par-la-men-ta-ris-mo|sustantivo masculino|Sistema de gobierno en que el Parlamento tiene gran poder sobre el Ejecutivo.|-|presidencialismo|Chile vivió un período de parlamentarismo a fines del siglo XIX.|historia
presidencialismo|pre-si-den-cia-lis-mo|sustantivo masculino|Sistema de gobierno en que el presidente tiene gran poder.|-|parlamentarismo|La Constitución de 1925 reforzó el presidencialismo.|historia
golpe de Estado|gol-pe de Es-ta-do|locución nominal|Toma del poder de manera violenta o ilegal.|-|-|Un golpe de Estado interrumpe la democracia.|historia
referéndum|re-fe-rén-dum|sustantivo masculino|Votación en que los ciudadanos deciden sobre una ley o asunto.|plebiscito|-|Se convocó un referéndum para aprobar el cambio.|ciudadanía
asamblea constituyente|a-sam-ble-a cons-ti-tu-yen-te|locución nominal|Grupo elegido para redactar una nueva constitución.|-|-|La asamblea constituyente debatió los artículos.|ciudadanía
reforma agraria|re-for-ma a-gra-ria|locución nominal|Cambio en la propiedad y reparto de las tierras agrícolas.|-|-|La reforma agraria repartió tierras a campesinos.|historia
nacionalización|na-cio-na-li-za-ción|sustantivo femenino|Paso de una empresa o un recurso a manos del Estado.|-|privatización|La nacionalización del cobre fue un hito.|historia
privatización|pri-va-ti-za-ción|sustantivo femenino|Traspaso de una empresa del Estado a manos privadas.|-|nacionalización|La privatización cambió la gestión de la empresa.|historia
neoliberalismo|ne-o-li-be-ra-lis-mo|sustantivo masculino|Modelo económico que reduce el papel del Estado y da prioridad al mercado.|-|-|El neoliberalismo se aplicó en Chile desde los años setenta.|historia
Estado de bienestar|Es-ta-do de bien-es-tar|locución nominal|Modelo en que el Estado asegura salud, educación y protección social.|-|-|El Estado de bienestar garantiza servicios básicos.|historia
derechos sociales|de-re-chos so-cia-les|locución nominal|Derechos que aseguran condiciones de vida dignas, como salud y educación.|-|-|Los derechos sociales protegen a todas las personas.|ciudadanía
derechos civiles|de-re-chos ci-vi-les|locución nominal|Derechos que protegen la libertad y la igualdad de las personas ante la ley.|-|-|La libertad de religión es un derecho civil.|ciudadanía
derechos políticos|de-re-chos po-lí-ti-cos|locución nominal|Derechos que permiten participar en el gobierno, como votar o ser elegido.|-|-|El voto es un derecho político.|ciudadanía
ciudadanía activa|ciu-da-da-ní-a ac-ti-va|locución nominal|Participación constante de las personas en los asuntos de su comunidad.|-|-|La ciudadanía activa mejora los barrios.|ciudadanía
sociedad civil|so-cie-dad ci-vil|locución nominal|Conjunto de organizaciones y personas que actúan fuera del gobierno.|-|-|La sociedad civil colaboró tras el terremoto.|ciudadanía
ONG|o-e-ne-ge|sustantivo femenino|Organización sin fines de lucro e independiente del gobierno.|-|-|Una ONG ayuda a proteger los humedales.|ciudadanía
feminismo|fe-mi-nis-mo|sustantivo masculino|Movimiento que busca la igualdad de derechos entre mujeres y hombres.|-|machismo|El feminismo logró el derecho a voto de las mujeres.|ciudadanía
movimiento social|mo-vi-mien-to so-cial|locución nominal|Grupo organizado que busca cambios en la sociedad.|-|-|El movimiento social exigió mejores salarios.|ciudadanía
protesta|pro-tes-ta|sustantivo femenino|Manifestación pública de desacuerdo.|reclamo|-|La protesta se realizó en forma pacífica.|ciudadanía
marcha|mar-cha|sustantivo femenino|Desfile de personas que se desplazan para expresar una causa.|desfile|-|La marcha recorrió la avenida principal.|ciudadanía
petitorio|pe-ti-to-rio|sustantivo masculino|Lista de peticiones que un grupo presenta a una autoridad.|-|-|Los trabajadores entregaron un petitorio a la empresa.|ciudadanía
reparación|re-pa-ra-ción|sustantivo femenino|Compensación por un daño que se causó.|compensación|-|Pidieron reparación por los daños sufridos.|ciudadanía
reconciliación|re-con-ci-lia-ción|sustantivo femenino|Vuelta a la armonía entre personas o grupos enemistados.|paz|enemistad|La reconciliación requiere verdad y respeto.|ciudadanía
Declaración Universal|De-cla-ra-ción U-ni-ver-sal|locución nominal|Documento de la ONU que establece los derechos básicos de todas las personas.|-|-|La Declaración Universal se aprobó en 1948.|ciudadanía
Naciones Unidas|Na-cio-nes U-ni-das|locución nominal|Organización de países creada para mantener la paz y la cooperación.|ONU|-|Naciones Unidas tiene su sede en Nueva York.|ciudadanía
organismo internacional|or-ga-nis-mo in-ter-na-cio-nal|locución nominal|Institución formada por varios países para tratar asuntos comunes.|-|-|La OMS es un organismo internacional de salud.|ciudadanía
soberanía nacional|so-be-ra-ní-a na-cio-nal|locución nominal|Poder de un país para gobernarse sin depender de otro.|-|-|La soberanía nacional se ejerce con las leyes propias.|ciudadanía
integración regional|in-te-gra-ción re-gio-nal|locución nominal|Unión de países vecinos para cooperar en economía y política.|-|-|La integración regional facilita el comercio.|economía
tratado de libre comercio|tra-ta-do de li-bre co-mer-cio|locución nominal|Acuerdo entre países para vender y comprar productos con pocas barreras.|-|-|Chile firmó un tratado de libre comercio con varios países.|economía
comercio exterior|co-mer-cio ex-te-rior|locución nominal|Compra y venta de productos entre países.|-|-|El comercio exterior depende de los puertos.|economía
balanza comercial|ba-lan-za co-mer-cial|locución nominal|Diferencia entre lo que un país vende y lo que compra al extranjero.|-|-|La balanza comercial tuvo un saldo favorable.|economía
divisa|di-vi-sa|sustantivo femenino|Moneda extranjera usada en el comercio entre países.|-|-|El dólar es la divisa más usada.|economía
tipo de cambio|ti-po de cam-bio|locución nominal|Valor de una moneda en relación con otra.|-|-|El tipo de cambio subió esta semana.|economía
bolsa de comercio|bol-sa de co-mer-cio|locución nominal|Lugar donde se compran y venden acciones y bonos.|-|-|La bolsa de comercio abrió con alzas.|economía
inversionista|in-ver-sio-nis-ta|sustantivo masculino y femenino|Persona que pone dinero en un negocio para obtener ganancias.|-|-|El inversionista compró acciones de la empresa.|economía
interés compuesto|in-te-rés com-pues-to|locución nominal|Interés que se calcula sobre el capital y sobre los intereses ya ganados.|-|interés simple|El interés compuesto hace crecer el ahorro.|economía
interés simple|in-te-rés sim-ple|locución nominal|Interés que se calcula solo sobre el capital inicial.|-|interés compuesto|Con interés simple, la ganancia es la misma cada año.|economía
hipoteca|hi-po-te-ca|sustantivo femenino|Préstamo para comprar una vivienda que queda garantizado con esa misma propiedad.|-|-|Pagaron la hipoteca en veinte años.|economía
tarjeta de crédito|tar-je-ta de cré-di-to|locución nominal|Tarjeta que permite comprar ahora y pagar después.|-|-|Pagué con tarjeta de crédito en tres cuotas.|economía
morosidad|mo-ro-si-dad|sustantivo femenino|Retraso en el pago de una deuda.|-|puntualidad|La morosidad aumenta los intereses.|economía
desempleo|de-sem-ple-o|sustantivo masculino|Situación de quienes quieren trabajar y no tienen empleo.|cesantía|empleo|El desempleo subió en el último trimestre.|economía
empleo informal|em-ple-o in-for-mal|locución nominal|Trabajo sin contrato ni protección laboral.|-|-|El empleo informal no ofrece seguridad social.|economía
contrato de trabajo|con-tra-to de tra-ba-jo|locución nominal|Acuerdo escrito entre un trabajador y su empleador sobre las condiciones del empleo.|-|-|Firmó su contrato de trabajo el lunes.|economía
finiquito|fi-ni-qui-to|sustantivo masculino|Documento que pone fin a una relación laboral y fija lo que se debe pagar.|-|-|Revisó su finiquito antes de firmar.|economía
jornada laboral|jor-na-da la-bo-ral|locución nominal|Horas que una persona trabaja en un día.|-|-|La jornada laboral es de ocho horas.|economía
remuneración|re-mu-ne-ra-ción|sustantivo femenino|Pago que se recibe por un trabajo.|sueldo|-|La remuneración se deposita a fin de mes.|economía
seguridad social|se-gu-ri-dad so-cial|locución nominal|Sistema que protege a las personas en caso de enfermedad, vejez o desempleo.|-|-|La seguridad social incluye las pensiones.|economía
pensión|pen-sión|sustantivo femenino|Dinero que se recibe periódicamente tras jubilar o por otra causa.|jubilación|-|Su abuelo recibe una pensión mensual.|economía
cotización|co-ti-za-ción|sustantivo femenino|Aporte mensual que se destina a la pensión o a la salud.|aporte|-|La cotización aparece en la liquidación de sueldo.|economía
producto interno bruto|pro-duc-to in-ter-no bru-to|locución nominal|Valor total de los bienes y servicios que produce un país en un año.|PIB|-|El producto interno bruto creció dos por ciento.|economía
crecimiento económico|cre-ci-mien-to e-co-nó-mi-co|locución nominal|Aumento de la producción de bienes y servicios de un país.|-|-|El crecimiento económico generó empleos.|economía
desarrollo humano|de-sa-rro-llo hu-ma-no|locución nominal|Mejora de las condiciones de vida, salud y educación de las personas.|-|-|El desarrollo humano considera más que el dinero.|economía
canasta básica|ca-nas-ta bá-si-ca|locución nominal|Conjunto de alimentos y productos necesarios para vivir.|-|-|El precio de la canasta básica subió.|economía
ingreso per cápita|in-gre-so per cá-pi-ta|locución nominal|Ingreso total de un país dividido por su número de habitantes.|-|-|El ingreso per cápita mide la riqueza promedio.|economía
brecha|bre-cha|sustantivo femenino|Diferencia o distancia grande entre dos grupos.|diferencia|-|La brecha entre ricos y pobres se amplió.|economía
justicia social|jus-ti-cia so-cial|locución nominal|Reparto justo de derechos, oportunidades y recursos en una sociedad.|-|-|La justicia social reduce la desigualdad.|ciudadanía
bien público|bien pú-bli-co|locución nominal|Bien o servicio que usa toda la comunidad y que mantiene el Estado.|-|-|Una plaza es un bien público.|ciudadanía
servicio público|ser-vi-cio pú-bli-co|locución nominal|Actividad del Estado que atiende necesidades de la comunidad.|-|-|El hospital es un servicio público.|ciudadanía
intendente|in-ten-den-te|sustantivo masculino y femenino|Autoridad que representa al gobierno en una región.|-|-|El intendente visitó la zona afectada.|ciudadanía
fiscal|fis-cal|sustantivo masculino y femenino|Abogado que investiga delitos y acusa en nombre de la sociedad.|-|-|La fiscal presentó pruebas en el juicio.|ciudadanía
defensor|de-fen-sor|sustantivo masculino|Abogado que protege los derechos de una persona acusada.|abogado|acusador|El defensor pidió que se respetara el debido proceso.|ciudadanía
ley orgánica|ley or-gá-ni-ca|locución nominal|Ley que desarrolla y organiza lo que dice la Constitución.|-|-|La ley orgánica fija las funciones del Congreso.|ciudadanía
ordenanza|or-de-nan-za|sustantivo femenino|Norma que dicta una municipalidad.|-|-|La ordenanza prohíbe tirar basura en la vía pública.|ciudadanía
proyecto de ley|pro-yec-to de ley|locución nominal|Propuesta de ley que se discute en el Congreso.|-|-|El proyecto de ley pasó a la Cámara de Diputados.|ciudadanía
quórum|quó-rum|sustantivo masculino|Número mínimo de miembros presentes para que una reunión sea válida.|-|-|Faltó quórum y la sesión se suspendió.|ciudadanía
veto|ve-to|sustantivo masculino|Rechazo de una ley o decisión por quien tiene ese poder.|-|-|El presidente aplicó el veto a la ley.|ciudadanía
indulto|in-dul-to|sustantivo masculino|Perdón de una pena que concede una autoridad.|-|-|El indulto redujo su condena.|ciudadanía
amnistía|am-nis-tí-a|sustantivo femenino|Perdón legal que borra ciertos delitos.|indulto|-|La amnistía benefició a los presos políticos.|ciudadanía
estado de derecho|es-ta-do de de-re-cho|locución nominal|Sistema en que todos, incluso las autoridades, deben cumplir las leyes.|-|-|El estado de derecho protege a los ciudadanos.|ciudadanía
división de poderes|di-vi-sión de po-de-res|locución nominal|Reparto del poder del Estado entre el Ejecutivo, el Legislativo y el Judicial.|-|-|La división de poderes evita abusos.|ciudadanía
contrapeso|con-tra-pe-so|sustantivo masculino|Fuerza que equilibra a otra.|-|-|Los tribunales son un contrapeso al poder político.|ciudadanía
rendición de cuentas|ren-di-ción de cuen-tas|locución nominal|Obligación de explicar cómo se usaron los recursos y las decisiones.|-|-|La alcaldesa hizo su rendición de cuentas.|ciudadanía
transparencia|trans-pa-ren-cia|sustantivo femenino|Cualidad de actuar de forma clara y abierta, sin ocultar información.|-|opacidad|La transparencia permite fiscalizar al gobierno.|ciudadanía
probidad|pro-bi-dad|sustantivo femenino|Honradez en el ejercicio de un cargo.|honradez|corrupción|La probidad es un deber de los funcionarios.|ciudadanía
corrupción|co-rrup-ción|sustantivo femenino|Uso indebido de un cargo para obtener beneficios personales.|-|probidad|La corrupción debilita la confianza en las instituciones.|ciudadanía
soborno|so-bor-no|sustantivo masculino|Dinero o regalo que se da para conseguir algo ilegal.|coima|-|Denunció un intento de soborno.|ciudadanía
fraude|frau-de|sustantivo masculino|Engaño para obtener un beneficio indebido.|estafa|-|El fraude fue descubierto por la auditoría.|ciudadanía
evasión|e-va-sión|sustantivo femenino|Acción de eludir una obligación, como pagar impuestos.|-|-|La evasión de impuestos es un delito.|economía
populismo|po-pu-lis-mo|sustantivo masculino|Estilo político que busca el apoyo del pueblo con promesas fáciles.|-|-|El populismo promete soluciones rápidas.|ciudadanía
demagogia|de-ma-go-gia|sustantivo femenino|Uso de promesas halagadoras para ganar apoyo político.|-|-|La demagogia se aprovecha del descontento.|ciudadanía
campaña electoral|cam-pa-ña e-lec-to-ral|locución nominal|Conjunto de actividades de los candidatos para pedir votos.|-|-|La campaña electoral duró dos meses.|ciudadanía
programa de gobierno|pro-gra-ma de go-bier-no|locución nominal|Documento donde un candidato explica lo que hará si gana.|-|-|Leí el programa de gobierno de cada candidato.|ciudadanía
coalición|co-a-li-ción|sustantivo femenino|Unión de partidos u organizaciones para un fin común.|alianza|-|La coalición ganó las elecciones.|ciudadanía
oposición|o-po-si-ción|sustantivo femenino|Conjunto de grupos que critican al gobierno.|-|oficialismo|La oposición presentó otra propuesta.|ciudadanía
oficialismo|o-fi-cia-lis-mo|sustantivo masculino|Conjunto de grupos que apoyan al gobierno.|-|oposición|El oficialismo defendió la ley.|ciudadanía
voto nulo|vo-to nu-lo|locución nominal|Voto que no vale por estar mal marcado.|-|-|Un voto nulo no se cuenta para ningún candidato.|ciudadanía
abstención|abs-ten-ción|sustantivo femenino|Decisión de no votar.|-|participación|La abstención fue alta en esa elección.|ciudadanía
padrón electoral|pa-drón e-lec-to-ral|locución nominal|Lista de las personas que pueden votar.|-|-|Revisé mi nombre en el padrón electoral.|ciudadanía
voto voluntario|vo-to vo-lun-ta-rio|locución nominal|Sistema en que votar no es obligatorio.|-|voto obligatorio|Con voto voluntario, cada persona decide si participa.|ciudadanía
polarización|po-la-ri-za-ción|sustantivo femenino|División de un grupo en dos posturas muy opuestas.|-|-|La polarización dificulta llegar a acuerdos.|ciudadanía
pluralismo|plu-ra-lis-mo|sustantivo masculino|Aceptación de que existan ideas y grupos distintos en una sociedad.|-|-|El pluralismo enriquece el debate.|ciudadanía
deliberación|de-li-be-ra-ción|sustantivo femenino|Análisis cuidadoso de las razones antes de decidir.|-|-|La deliberación del comité duró horas.|ciudadanía
espacio público|es-pa-cio pú-bli-co|locución nominal|Lugar de uso común, como una calle o una plaza.|-|-|El espacio público debe cuidarse entre todos.|ciudadanía
patrimonio cultural|pa-tri-mo-nio cul-tu-ral|locución nominal|Conjunto de bienes y tradiciones valiosos de un pueblo.|-|-|La música tradicional es patrimonio cultural.|cultura
patrimonio natural|pa-tri-mo-nio na-tu-ral|locución nominal|Paisajes y seres vivos de valor que se deben proteger.|-|-|Los glaciares son patrimonio natural.|cultura
monumento nacional|mo-nu-men-to na-cio-nal|locución nominal|Lugar u objeto protegido por la ley por su valor histórico.|-|-|La iglesia fue declarada monumento nacional.|cultura
conmemoración|con-me-mo-ra-ción|sustantivo femenino|Acto en que se recuerda un hecho importante.|homenaje|-|La conmemoración se hizo con un desfile.|cultura
feriado|fe-ria-do|sustantivo masculino|Día en que no se trabaja ni se va a clases por una fecha especial.|-|-|El feriado cayó un lunes.|cultura
Fiestas Patrias|Fies-tas Pa-trias|locución nominal|Celebración del aniversario de la independencia de Chile, en septiembre.|-|-|En Fiestas Patrias comemos empanadas.|cultura
símbolo patrio|sím-bo-lo pa-trio|locución nominal|Emblema que representa a un país, como la bandera o el himno.|-|-|El escudo es un símbolo patrio.|cultura
identidad nacional|i-den-ti-dad na-cio-nal|locución nominal|Conjunto de rasgos que hacen sentir a un grupo parte de una misma nación.|-|-|El folclor fortalece la identidad nacional.|cultura
huaso|hua-so|sustantivo masculino|Hombre del campo de Chile central, jinete y de vestimenta típica (uso en Chile).|-|-|El huaso montó su caballo en el rodeo.|cultura
rodeo|ro-de-o|sustantivo masculino|Fiesta tradicional de campo en que los jinetes muestran su habilidad.|-|-|Vimos un rodeo en la fiesta costumbrista.|cultura
mote con huesillo|mo-te con hue-si-llo|locución nominal|Bebida dulce chilena de durazno seco y trigo cocido.|-|-|En verano tomamos mote con huesillo.|cultura
mestizaje cultural|mes-ti-za-je cul-tu-ral|locución nominal|Mezcla de tradiciones de distintos pueblos.|-|-|La música muestra el mestizaje cultural.|cultura
resistencia indígena|re-sis-ten-cia in-dí-ge-na|locución nominal|Defensa de los pueblos originarios frente a la conquista.|-|-|La resistencia indígena duró siglos.|historia
guerra de Arauco|gue-rra de A-rau-co|locución nominal|Largo conflicto entre españoles y el pueblo mapuche durante la colonia.|-|-|La guerra de Arauco marcó la historia del sur.|historia
territorio ancestral|te-rri-to-rio an-ces-tral|locución nominal|Tierra que un pueblo ha habitado desde tiempos antiguos.|-|-|El territorio ancestral es parte de su identidad.|cultura
exponente negativo|ex-po-nen-te ne-ga-ti-vo|locución nominal|Exponente con signo menos que indica el inverso de la potencia.|-|exponente positivo|Dos con exponente negativo uno es un medio.|matemática
raíz enésima|ra-íz e-né-si-ma|locución nominal|Número que, elevado a cierto exponente, da el número dado.|-|-|La raíz enésima de ocho para n igual a tres es dos.|matemática
número real|nú-me-ro real|locución nominal|Número que puede ubicarse en la recta numérica, sea racional o irracional.|-|-|Todo número racional es un número real.|matemática
número natural|nú-me-ro na-tu-ral|locución nominal|Número que sirve para contar: uno, dos, tres, y así sucesivamente.|-|-|El cinco es un número natural.|matemática
sistema de ecuaciones|sis-te-ma de e-cua-cio-nes|locución nominal|Conjunto de ecuaciones que se resuelven al mismo tiempo.|-|-|Resolví el sistema de ecuaciones con dos incógnitas.|matemática
método de sustitución|mé-to-do de sus-ti-tu-ción|locución nominal|Forma de resolver un sistema reemplazando una incógnita despejada en la otra ecuación.|-|-|Usé el método de sustitución para hallar x.|matemática
método de reducción|mé-to-do de re-duc-ción|locución nominal|Forma de resolver un sistema sumando o restando ecuaciones para eliminar una incógnita.|-|-|El método de reducción eliminó la variable y.|matemática
función afín|fun-ción a-fín|locución nominal|Función cuyo gráfico es una recta que no siempre pasa por el origen.|-|-|La función afín se escribe como y igual a mx más n.|matemática
función cuadrática|fun-ción cua-drá-ti-ca|locución nominal|Función cuyo gráfico es una parábola.|-|-|Graficamos la función cuadrática con una tabla de valores.|matemática
parábola|pa-rá-bo-la|sustantivo femenino|Curva abierta que representa una función cuadrática.|-|-|La parábola abre hacia arriba.|matemática
vértice de la parábola|vér-ti-ce de la pa-rá-bo-la|locución nominal|Punto más alto o más bajo de una parábola.|-|-|El vértice de la parábola es el mínimo de la función.|matemática
ecuación cuadrática|e-cua-ción cua-drá-ti-ca|locución nominal|Ecuación en que la incógnita aparece elevada al cuadrado.|-|-|Resolví la ecuación cuadrática con la fórmula general.|matemática
discriminante|dis-cri-mi-nan-te|sustantivo masculino|Expresión que indica cuántas soluciones reales tiene una ecuación cuadrática.|-|-|El discriminante resultó positivo.|matemática
cero de una función|ce-ro de u-na fun-ción|locución nominal|Valor de la variable para el que la función vale cero.|raíz|-|El cero de la función está donde el gráfico corta el eje x.|matemática
tabla de valores|ta-bla de va-lo-res|locución nominal|Cuadro que muestra pares de valores de una función.|-|-|Armé una tabla de valores para graficar.|matemática
proporcionalidad directa|pro-por-cio-na-li-dad di-rec-ta|locución nominal|Relación en que al aumentar una cantidad, la otra aumenta en la misma razón.|-|proporcionalidad inversa|Comprar más pan es proporcionalidad directa con el costo.|matemática
proporcionalidad inversa|pro-por-cio-na-li-dad in-ver-sa|locución nominal|Relación en que al aumentar una cantidad, la otra disminuye en la misma razón.|-|proporcionalidad directa|Más obreros y menos días es proporcionalidad inversa.|matemática
regla de tres|re-gla de tres|locución nominal|Procedimiento para hallar un valor desconocido en una proporción.|-|-|Usé una regla de tres para el precio.|matemática
variación porcentual|va-ria-ción por-cen-tual|locución nominal|Cambio de una cantidad expresado como porcentaje.|-|-|La variación porcentual del precio fue de un cinco por ciento.|matemática
IVA|i-va|sustantivo masculino|Impuesto que se suma al precio de los productos.|-|-|El IVA en Chile es del diecinueve por ciento.|economía
razón trigonométrica|ra-zón tri-go-no-mé-tri-ca|locución nominal|Cociente entre dos lados de un triángulo rectángulo.|-|-|El seno es una razón trigonométrica.|matemática
seno|se-no|sustantivo masculino|Razón entre el cateto opuesto a un ángulo y la hipotenusa.|-|coseno|El seno de treinta grados es un medio.|matemática
coseno|co-se-no|sustantivo masculino|Razón entre el cateto adyacente a un ángulo y la hipotenusa.|-|seno|Usé el coseno para hallar el lado.|matemática
teorema de Pitágoras|te-o-re-ma de Pi-tá-go-ras|locución nominal|Afirma que en un triángulo rectángulo el cuadrado de la hipotenusa es la suma de los cuadrados de los catetos.|-|-|Con el teorema de Pitágoras calculé la diagonal.|matemática
teorema de Tales|te-o-re-ma de Ta-les|locución nominal|Afirma que las rectas paralelas cortan proporcionalmente a dos rectas que las cruzan.|-|-|El teorema de Tales permite medir alturas con sombras.|matemática
razón de semejanza|ra-zón de se-me-jan-za|locución nominal|Cociente entre los lados correspondientes de dos figuras semejantes.|-|-|La razón de semejanza fue dos.|matemática
traslación vectorial|tras-la-ción vec-to-rial|locución nominal|Movimiento de una figura según un vector.|-|-|Hicimos una traslación vectorial del triángulo.|matemática
eje de simetría|e-je de si-me-trí-a|locución nominal|Recta que divide una figura en dos mitades iguales.|-|-|El cuadrado tiene cuatro ejes de simetría.|matemática
simetría axial|si-me-trí-a a-xial|locución nominal|Reflejo de una figura respecto de una recta.|-|-|La simetría axial produce una imagen en espejo.|matemática
simetría central|si-me-trí-a cen-tral|locución nominal|Reflejo de una figura respecto de un punto.|-|-|En la simetría central, la figura gira media vuelta.|matemática
ángulo inscrito|án-gu-lo ins-cri-to|locución nominal|Ángulo con vértice en una circunferencia y lados que son cuerdas.|-|-|El ángulo inscrito mide la mitad del arco.|matemática
polígono regular|po-lí-go-no re-gu-lar|locución nominal|Polígono con todos sus lados y ángulos iguales.|-|-|El hexágono regular tiene seis lados iguales.|matemática
área lateral|á-re-a la-te-ral|locución nominal|Superficie de las caras laterales de un cuerpo geométrico.|-|-|Calculé el área lateral del prisma.|matemática
área total|á-re-a to-tal|locución nominal|Suma de todas las superficies de un cuerpo geométrico.|-|-|El área total incluye las bases.|matemática
generatriz|ge-ne-ra-triz|sustantivo femenino|Segmento que une el vértice de un cono con el borde de su base.|-|-|La generatriz del cono mide diez centímetros.|matemática
desarrollo plano|de-sa-rro-llo pla-no|locución nominal|Figura plana que, al doblarse, forma un cuerpo geométrico.|red|-|Dibuja el desarrollo plano del cubo.|matemática
proyección|pro-yec-ción|sustantivo femenino|Imagen que una figura deja sobre un plano.|-|-|La proyección del cilindro es un rectángulo.|matemática
probabilidad condicional|pro-ba-bi-li-dad con-di-cio-nal|locución nominal|Probabilidad de que ocurra un suceso sabiendo que otro ya ocurrió.|-|-|La probabilidad condicional cambia el espacio muestral.|probabilidad
regla de Laplace|re-gla de La-pla-ce|locución nominal|Fórmula que calcula la probabilidad como casos favorables sobre casos posibles.|-|-|Apliqué la regla de Laplace con un dado.|probabilidad
regla aditiva|re-gla a-di-ti-va|locución nominal|Regla que suma las probabilidades de sucesos que no pueden ocurrir a la vez.|-|-|La regla aditiva sirve para «uno o el otro».|probabilidad
regla multiplicativa|re-gla mul-ti-pli-ca-ti-va|locución nominal|Regla que multiplica las probabilidades de sucesos independientes.|-|-|Con la regla multiplicativa calculé dos lanzamientos seguidos.|probabilidad
diagrama de árbol|dia-gra-ma de ár-bol|locución nominal|Esquema con ramas que muestra todos los resultados posibles.|-|-|El diagrama de árbol mostró doce combinaciones.|probabilidad
tabla de doble entrada|ta-bla de do-ble en-tra-da|locución nominal|Cuadro con filas y columnas que cruza dos características.|-|-|Anotamos los resultados en una tabla de doble entrada.|estadística
ley de los grandes números|ley de los gran-des nú-me-ros|locución nominal|Principio según el cual, con muchas repeticiones, la frecuencia se acerca a la probabilidad.|-|-|La ley de los grandes números se ve al lanzar monedas muchas veces.|probabilidad
frecuencia absoluta|fre-cuen-cia ab-so-lu-ta|locución nominal|Cantidad de veces que aparece un dato.|-|frecuencia relativa|La frecuencia absoluta del tres es cinco.|estadística
frecuencia acumulada|fre-cuen-cia a-cu-mu-la-da|locución nominal|Suma de las frecuencias de un valor y de todos los menores.|-|-|La frecuencia acumulada llega al total de datos.|estadística
media ponderada|me-dia pon-de-ra-da|locución nominal|Promedio en que cada dato pesa distinto según su importancia.|-|-|La nota final se calcula con media ponderada.|estadística
desviación estándar|des-via-ción es-tán-dar|locución nominal|Medida de cuánto se alejan los datos del promedio.|-|-|Una desviación estándar baja indica datos parecidos.|estadística
varianza|va-rian-za|sustantivo femenino|Medida de dispersión que es el cuadrado de la desviación estándar.|-|-|Calculé la varianza del conjunto.|estadística
percentil|per-cen-til|sustantivo masculino|Valor que deja un cierto porcentaje de datos por debajo.|-|-|Quedó en el percentil noventa del examen.|estadística
diagrama de caja|dia-gra-ma de ca-ja|locución nominal|Gráfico que muestra la mediana y los cuartiles de unos datos.|-|-|El diagrama de caja resume la distribución.|estadística
gráfico de dispersión|grá-fi-co de dis-per-sión|locución nominal|Gráfico de puntos que muestra la relación entre dos variables.|-|-|El gráfico de dispersión mostró una relación creciente.|estadística
correlación lineal|co-rre-la-ción li-ne-al|locución nominal|Relación entre dos variables que se aproxima a una recta.|-|-|Había una correlación lineal entre horas de estudio y notas.|estadística
muestreo|mues-tre-o|sustantivo masculino|Proceso de escoger una muestra de una población.|-|-|El muestreo fue aleatorio.|estadística
muestra aleatoria|mues-tra a-lea-to-ria|locución nominal|Muestra escogida al azar, de modo que todos tengan igual opción de salir.|-|-|Se eligió una muestra aleatoria de cien alumnos.|estadística
tendencia central|ten-den-cia cen-tral|locución nominal|Valor alrededor del cual se agrupan los datos, como el promedio.|-|-|La media es una medida de tendencia central.|estadística
dato atípico|da-to a-tí-pi-co|locución nominal|Dato que se aleja mucho del resto.|-|-|El dato atípico elevó el promedio.|estadística
tabla de frecuencias|ta-bla de fre-cuen-cias|locución nominal|Cuadro que muestra cuántas veces se repite cada dato.|-|-|Armamos una tabla de frecuencias con las edades.|estadística
intervalo de clase|in-ter-va-lo de cla-se|locución nominal|Grupo de valores que se agrupan en un solo tramo de una tabla.|-|-|El intervalo de clase va de diez a veinte.|estadística
magnitud vectorial|mag-ni-tud vec-to-rial|locución nominal|Magnitud que se define con valor, dirección y sentido.|-|magnitud escalar|La fuerza es una magnitud vectorial.|física
magnitud escalar|mag-ni-tud es-ca-lar|locución nominal|Magnitud que se define solo con un valor.|-|magnitud vectorial|La masa es una magnitud escalar.|física
desplazamiento|des-pla-za-mien-to|sustantivo masculino|Cambio de posición de un cuerpo.|-|-|El desplazamiento fue de cinco metros al norte.|física
movimiento rectilíneo|mo-vi-mien-to rec-ti-lí-ne-o|locución nominal|Movimiento que sigue una línea recta.|-|-|Un tren en vía recta hace un movimiento rectilíneo.|física
movimiento uniforme|mo-vi-mien-to u-ni-for-me|locución nominal|Movimiento con velocidad constante.|-|movimiento acelerado|El auto avanzó con movimiento uniforme.|física
movimiento acelerado|mo-vi-mien-to a-ce-le-ra-do|locución nominal|Movimiento cuya velocidad cambia en el tiempo.|-|movimiento uniforme|El tren inicia con movimiento acelerado.|física
caída libre|ca-í-da li-bre|locución nominal|Movimiento de un cuerpo que cae solo por acción de la gravedad.|-|-|En caída libre, todos los cuerpos aceleran igual.|física
fuerza neta|fuer-za ne-ta|locución nominal|Resultado de sumar todas las fuerzas que actúan sobre un cuerpo.|-|-|Si la fuerza neta es cero, no hay cambio de movimiento.|física
fuerza peso|fuer-za pe-so|locución nominal|Fuerza con que la Tierra atrae a un cuerpo.|-|-|La fuerza peso depende de la masa.|física
fuerza normal|fuer-za nor-mal|locución nominal|Fuerza que una superficie ejerce perpendicular sobre un cuerpo apoyado.|-|-|La fuerza normal equilibra el peso del libro sobre la mesa.|física
fuerza elástica|fuer-za e-lás-ti-ca|locución nominal|Fuerza con que un resorte u objeto recupera su forma.|-|-|La fuerza elástica devolvió el resorte a su largo.|física
leyes de Newton|le-yes de New-ton|locución nominal|Tres principios básicos que explican el movimiento de los cuerpos.|-|-|Las leyes de Newton explican por qué frena un auto.|física
principio de acción y reacción|prin-ci-pio de ac-ción y re-ac-ción|locución nominal|Principio según el cual toda fuerza provoca otra igual y opuesta.|-|-|El cohete avanza por el principio de acción y reacción.|física
equilibrio de fuerzas|e-qui-li-brio de fuer-zas|locución nominal|Situación en que las fuerzas sobre un cuerpo se compensan.|-|-|El equilibrio de fuerzas mantiene el cuadro colgado.|física
potencia mecánica|po-ten-cia me-cá-ni-ca|locución nominal|Trabajo realizado por unidad de tiempo.|-|-|La potencia mecánica se mide en vatios.|física
energía mecánica|e-ner-gí-a me-cá-ni-ca|locución nominal|Suma de la energía cinética y la energía potencial de un cuerpo.|-|-|La energía mecánica se conserva sin roce.|física
conservación de la energía|con-ser-va-ción de la e-ner-gí-a|locución nominal|Principio según el cual la energía no se crea ni se destruye, solo se transforma.|-|-|La conservación de la energía explica el péndulo.|física
presión hidrostática|pre-sión hi-dros-tá-ti-ca|locución nominal|Presión que ejerce un líquido en reposo y que aumenta con la profundidad.|-|-|La presión hidrostática crece al bucear.|física
principio de Pascal|prin-ci-pio de Pas-cal|locución nominal|Principio según el cual la presión sobre un fluido se transmite por igual a todos sus puntos.|-|-|El principio de Pascal explica los frenos hidráulicos.|física
principio de Arquímedes|prin-ci-pio de Ar-quí-me-des|locución nominal|Principio según el cual un cuerpo sumergido recibe un empuje igual al peso del líquido desplazado.|-|-|El principio de Arquímedes explica por qué flota un barco.|física
flotación|flo-ta-ción|sustantivo femenino|Capacidad de un cuerpo de mantenerse sobre un líquido.|-|hundimiento|La flotación depende de la densidad.|física
empuje|em-pu-je|sustantivo masculino|Fuerza hacia arriba que ejerce un fluido sobre un cuerpo sumergido.|-|-|El empuje del agua alivia el peso del cuerpo.|física
tensión superficial|ten-sión su-per-fi-cial|locución nominal|Propiedad de la superficie de un líquido que actúa como una piel elástica.|-|-|La tensión superficial permite que un insecto camine sobre el agua.|física
viscosidad|vis-co-si-dad|sustantivo femenino|Resistencia de un líquido a fluir.|-|-|La miel tiene más viscosidad que el agua.|física
calor específico|ca-lor es-pe-cí-fi-co|locución nominal|Cantidad de calor que necesita un gramo de una sustancia para subir un grado.|-|-|El agua tiene un calor específico alto.|física
escala Celsius|es-ca-la Cel-sius|locución nominal|Escala de temperatura en que el agua se congela a cero y hierve a cien grados.|-|-|En la escala Celsius, el hielo se derrite a cero.|física
escala Kelvin|es-ca-la Kel-vin|locución nominal|Escala de temperatura cuyo cero es el cero absoluto.|-|-|En la escala Kelvin no hay temperaturas negativas.|física
dilatación térmica|di-la-ta-ción tér-mi-ca|locución nominal|Aumento de tamaño de un cuerpo al calentarse.|-|-|La dilatación térmica separa las vías del tren.|física
cambio de estado|cam-bio de es-ta-do|locución nominal|Paso de una sustancia de sólido, líquido o gas a otro de estos estados.|-|-|El hielo sufre un cambio de estado al derretirse.|física
calor latente|ca-lor la-ten-te|locución nominal|Calor que se absorbe o libera durante un cambio de estado sin cambiar la temperatura.|-|-|El calor latente derrite el hielo sin subir su temperatura.|física
ley de Ohm|ley de Ohm|locución nominal|Ley que relaciona voltaje, corriente y resistencia en un circuito.|-|-|La ley de Ohm dice que el voltaje es igual a la corriente por la resistencia.|física
intensidad de corriente|in-ten-si-dad de co-rrien-te|locución nominal|Cantidad de carga eléctrica que pasa por un punto cada segundo.|-|-|La intensidad de corriente se mide en amperios.|física
resistencia eléctrica|re-sis-ten-cia e-léc-tri-ca|locución nominal|Oposición de un material al paso de la corriente.|-|-|La resistencia eléctrica se mide en ohmios.|física
circuito en serie|cir-cui-to en se-rie|locución nominal|Circuito en que los componentes están uno tras otro en un único camino.|-|circuito en paralelo|En un circuito en serie, si uno falla, se apagan todos.|física
circuito en paralelo|cir-cui-to en pa-ra-le-lo|locución nominal|Circuito en que los componentes tienen caminos separados.|-|circuito en serie|En un circuito en paralelo, cada bombilla funciona sola.|física
electroimán|e-lec-troi-mán|sustantivo masculino|Imán que funciona al pasar corriente eléctrica por una bobina.|-|-|El electroimán levantó la chatarra.|física
inducción electromagnética|in-duc-ción e-lec-tro-mag-né-ti-ca|locución nominal|Producción de corriente eléctrica por un campo magnético que cambia.|-|-|La inducción electromagnética genera electricidad en las centrales.|física
transformador|trans-for-ma-dor|sustantivo masculino|Aparato que cambia el voltaje de una corriente alterna.|-|-|El transformador baja el voltaje para las casas.|física
motor eléctrico|mo-tor e-léc-tri-co|locución nominal|Máquina que transforma energía eléctrica en movimiento.|-|-|El motor eléctrico mueve el ventilador.|física
espectro electromagnético|es-pec-tro e-lec-tro-mag-né-ti-co|locución nominal|Conjunto de todas las ondas electromagnéticas, ordenadas por su frecuencia.|-|-|La luz visible es parte del espectro electromagnético.|física
ondas de radio|on-das de ra-dio|locución nominal|Ondas electromagnéticas de baja frecuencia que se usan en las comunicaciones.|-|-|Las ondas de radio llevan la señal de la emisora.|física
infrarrojo|in-fra-rro-jo|adjetivo|Dicho de la radiación invisible de menor frecuencia que la luz roja.|-|ultravioleta|El control remoto emite luz infrarroja.|física
rayos X|ra-yos e-quis|locución nominal|Radiación que atraviesa el cuerpo y permite ver los huesos.|-|-|Le sacaron una radiografía con rayos X.|física
luz visible|luz vi-si-ble|locución nominal|Parte del espectro electromagnético que ven nuestros ojos.|-|-|La luz visible va del rojo al violeta.|física
dispersión de la luz|dis-per-sión de la luz|locución nominal|Separación de la luz blanca en sus colores.|-|-|La dispersión de la luz forma el arcoíris.|física
espejo plano|es-pe-jo pla-no|locución nominal|Espejo de superficie lisa que da una imagen del mismo tamaño.|-|-|En el espejo plano, la imagen aparece invertida.|física
espejo cóncavo|es-pe-jo cón-ca-vo|locución nominal|Espejo curvo hacia adentro que puede agrandar las imágenes.|-|espejo convexo|El espejo cóncavo del maquillaje agranda la cara.|física
espejo convexo|es-pe-jo con-ve-xo|locución nominal|Espejo curvo hacia afuera que da una imagen más pequeña y amplia.|-|espejo cóncavo|El espejo convexo del pasillo muestra todo el cruce.|física
lente convergente|len-te con-ver-gen-te|locución nominal|Lente que junta los rayos de luz en un punto.|-|lente divergente|La lupa es una lente convergente.|física
lente divergente|len-te di-ver-gen-te|locución nominal|Lente que separa los rayos de luz.|-|lente convergente|Los lentes para la miopía usan lentes divergentes.|física
miopía|mio-pí-a|sustantivo femenino|Defecto de la vista que impide ver con claridad de lejos.|-|hipermetropía|Mi hermano usa lentes por su miopía.|salud
hipermetropía|hi-per-me-tro-pí-a|sustantivo femenino|Defecto de la vista que impide ver con claridad de cerca.|-|miopía|La hipermetropía se corrige con lentes.|salud
astigmatismo|as-tig-ma-tis-mo|sustantivo masculino|Defecto de la vista que hace ver borrosas las imágenes a cualquier distancia.|-|-|El astigmatismo se debe a la forma del ojo.|salud
resonancia|re-so-nan-cia|sustantivo femenino|Prolongación o aumento de un sonido por la vibración de otro cuerpo.|-|-|La caja de la guitarra produce resonancia.|física
intensidad sonora|in-ten-si-dad so-no-ra|locución nominal|Fuerza con que se percibe un sonido.|volumen|-|La intensidad sonora se mide en decibeles.|física
decibel|de-ci-bel|sustantivo masculino|Unidad con que se mide la intensidad de un sonido.|-|-|Un concierto puede superar cien decibeles.|física
infrasonido|in-fra-so-ni-do|sustantivo masculino|Sonido demasiado grave para que lo oiga el ser humano.|-|ultrasonido|Los elefantes se comunican con infrasonidos.|física
sonar|so-nar|sustantivo masculino|Aparato que localiza objetos bajo el agua con ondas sonoras.|-|-|El barco usó el sonar para ubicar el cardumen.|física
efecto Doppler|e-fec-to Dop-pler|locución nominal|Cambio en la frecuencia de una onda cuando la fuente o el observador se mueven.|-|-|El efecto Doppler cambia el sonido de la sirena que pasa.|física
escala musical|es-ca-la mu-si-cal|locución nominal|Serie ordenada de notas que sube o baja por grados.|-|-|Practiqué la escala musical en el piano.|música
modo mayor|mo-do ma-yor|locución nominal|Forma de organizar las notas que da un sonido alegre y brillante.|-|modo menor|La canción está en modo mayor.|música
modo menor|mo-do me-nor|locución nominal|Forma de organizar las notas que da un sonido más triste o serio.|-|modo mayor|El tango suele sonar en modo menor.|música
cadencia|ca-den-cia|sustantivo femenino|Final de una frase musical que da sensación de reposo.|-|-|La cadencia cerró la melodía con calma.|música
contrapunto|con-tra-pun-to|sustantivo masculino|Técnica de combinar varias melodías que suenan al mismo tiempo.|-|-|Bach dominaba el contrapunto.|música
sonata|so-na-ta|sustantivo femenino|Obra musical para uno o pocos instrumentos, dividida en varios movimientos.|-|-|Toqué una sonata de piano.|música
cantata|can-ta-ta|sustantivo femenino|Obra musical cantada con acompañamiento de instrumentos.|-|-|El coro cantó una cantata de Navidad.|música
oratorio|o-ra-to-rio|sustantivo masculino|Obra musical de gran tamaño con coro, solistas y orquesta, de tema religioso.|-|-|El oratorio duró dos horas.|música
trova|tro-va|sustantivo femenino|Canción o poema cantado, de tono sencillo.|-|-|La trova narra historias del pueblo.|música
nueva canción|nue-va can-ción|locución nominal|Movimiento musical latinoamericano que une folclor y mensajes sociales.|-|-|Violeta Parra fue clave en la nueva canción.|música
folclore|fol-clo-re|sustantivo masculino|Conjunto de costumbres, música y bailes tradicionales de un pueblo.|folclor|-|El folclore se transmite en las fiestas.|música
síncopa|sín-co-pa|sustantivo femenino|Nota que empieza en un tiempo débil y se prolonga en uno fuerte.|-|-|La síncopa da movimiento al jazz.|música
compás compuesto|com-pás com-pues-to|locución nominal|Compás cuyos tiempos se dividen en tres partes.|-|compás simple|El seis octavos es un compás compuesto.|música
clave de sol|cla-ve de sol|locución nominal|Signo al inicio del pentagrama que indica dónde está la nota sol.|-|-|La flauta se escribe en clave de sol.|música
ligadura|li-ga-du-ra|sustantivo femenino|Línea curva que une dos notas iguales para sumar su duración.|-|-|La ligadura alarga la nota.|música
puntillo|pun-ti-llo|sustantivo masculino|Punto que aumenta en la mitad la duración de una nota.|-|-|Una negra con puntillo dura tres corcheas.|música
cuarteto de cuerdas|cuar-te-to de cuer-das|locución nominal|Grupo de cuatro instrumentos de cuerda, dos violines, una viola y un violonchelo.|-|-|El cuarteto de cuerdas tocó en la sala.|música
concertista|con-cer-tis-ta|sustantivo masculino y femenino|Músico que ofrece conciertos como solista.|-|-|La concertista de piano recibió aplausos.|música
director de orquesta|di-rec-tor de or-ques-ta|locución nominal|Persona que guía a los músicos de una orquesta.|-|-|El director de orquesta marcó el ritmo con su batuta.|música
luthier|lu-thier|sustantivo masculino y femenino|Artesano que fabrica y repara instrumentos de cuerda.|-|-|El luthier reparó mi guitarra.|música
color primario|co-lor pri-ma-rio|locución nominal|Color básico que no se obtiene mezclando otros.|-|color secundario|El azul es un color primario.|arte
color secundario|co-lor se-cun-da-rio|locución nominal|Color que resulta de mezclar dos primarios.|-|color primario|El verde es un color secundario.|arte
color terciario|co-lor ter-cia-rio|locución nominal|Color que resulta de mezclar un primario con un secundario.|-|-|El naranja rojizo es un color terciario.|arte
círculo cromático|cír-cu-lo cro-má-ti-co|locución nominal|Esquema circular que ordena los colores según su relación.|-|-|Pinté el círculo cromático con témperas.|arte
gama cálida|ga-ma cá-li-da|locución nominal|Grupo de colores que recuerdan al fuego y al sol, como el rojo y el amarillo.|-|gama fría|El cuadro usa una gama cálida.|arte
gama fría|ga-ma frí-a|locución nominal|Grupo de colores que recuerdan al agua y al hielo, como el azul y el verde.|-|gama cálida|El paisaje invernal usa una gama fría.|arte
tinte|tin-te|sustantivo masculino|Sustancia que sirve para dar color a una tela o al pelo.|-|-|El tinte natural salió de las cebollas.|arte
empaste|em-pas-te|sustantivo masculino|Aplicación espesa de pintura que deja relieve.|-|-|El empaste da textura al cuadro.|arte
acrílico|a-crí-li-co|sustantivo masculino|Pintura de secado rápido que se diluye con agua.|-|-|Pinté el mural con acrílico.|arte
carboncillo|car-bon-ci-llo|sustantivo masculino|Barra de carbón de madera que se usa para dibujar.|-|-|Hice un retrato al carboncillo.|arte
grafito|gra-fi-to|sustantivo masculino|Mineral gris con el que se hacen las minas de los lápices.|-|-|El lápiz de grafito deja trazos suaves.|arte
performance|per-for-man-ce|sustantivo femenino|Obra de arte en vivo en que el artista usa su cuerpo y su acción.|-|-|La performance ocurrió en una plaza.|arte
videoarte|vi-de-o-ar-te|sustantivo masculino|Arte que usa el video como medio de expresión.|-|-|El videoarte mostraba imágenes del mar.|arte
arte digital|ar-te di-gi-tal|locución nominal|Creaciones artísticas hechas con programas o aparatos digitales.|-|-|Dibujé una ilustración de arte digital.|arte
plano general|pla-no ge-ne-ral|locución nominal|Toma que muestra todo el lugar y a las personas desde lejos.|-|primer plano|El plano general presentó el pueblo.|arte
plano medio|pla-no me-dio|locución nominal|Toma que muestra a una persona de la cintura hacia arriba.|-|-|El plano medio mostraba al entrevistado.|arte
picado|pi-ca-do|sustantivo masculino|Toma hecha desde arriba hacia abajo.|-|contrapicado|En el picado, el personaje parece pequeño.|arte
contrapicado|con-tra-pi-ca-do|sustantivo masculino|Toma hecha desde abajo hacia arriba.|-|picado|El contrapicado hace ver grande al personaje.|arte
iluminación|i-lu-mi-na-ción|sustantivo femenino|Luz con que se alumbra una escena o un lugar.|-|-|La iluminación creó un ambiente misterioso.|arte
naturaleza muerta|na-tu-ra-le-za muer-ta|locución nominal|Pintura de objetos inmóviles, como frutas y jarrones.|bodegón|-|Pintó una naturaleza muerta con manzanas.|arte
abstracción|abs-trac-ción|sustantivo femenino|Arte que no representa objetos reconocibles, sino formas y colores.|-|figuración|La abstracción usa solo líneas y manchas.|arte
figuración|fi-gu-ra-ción|sustantivo femenino|Arte que representa objetos o personas reconocibles.|-|abstracción|La figuración domina en los retratos.|arte
expresionismo|ex-pre-sio-nis-mo|sustantivo masculino|Movimiento artístico que muestra las emociones con colores y formas intensas.|-|-|El expresionismo deforma la realidad para transmitir angustia.|arte
arte urbano|ar-te ur-ba-no|locución nominal|Obras artísticas hechas en espacios públicos de la ciudad.|-|-|Los murales son arte urbano.|arte
arte precolombino|ar-te pre-co-lom-bi-no|locución nominal|Arte creado por los pueblos de América antes de la llegada de los europeos.|-|-|La cerámica diaguita es arte precolombino.|arte
arte popular|ar-te po-pu-lar|locución nominal|Creaciones artísticas hechas por el pueblo con técnicas tradicionales.|-|-|Los chanchitos de Pomaire son arte popular.|arte
greda|gre-da|sustantivo femenino|Arcilla que se usa para hacer vasijas.|arcilla|-|Pomaire es famoso por sus objetos de greda.|arte
patrimonio artístico|pa-tri-mo-nio ar-tís-ti-co|locución nominal|Obras de arte valiosas que un país protege.|-|-|El museo cuida el patrimonio artístico.|arte
curaduría|cu-ra-du-rí-a|sustantivo femenino|Selección y organización de obras para una exposición.|-|-|La curaduría eligió obras de pintoras chilenas.|arte
catálogo|ca-tá-lo-go|sustantivo masculino|Lista ordenada de obras o productos con su descripción.|-|-|El catálogo de la muestra tiene fotografías.|arte
crítica de arte|crí-ti-ca de ar-te|locución nominal|Análisis que explica y valora las obras de arte.|-|-|Leí una crítica de arte sobre la exposición.|arte
originalidad|o-ri-gi-na-li-dad|sustantivo femenino|Cualidad de lo que es nuevo y propio, no copiado.|-|copia|La originalidad de la obra sorprendió al jurado.|arte
falsificación|fal-si-fi-ca-ción|sustantivo femenino|Copia de una obra hecha para hacerla pasar por auténtica.|-|-|El museo descubrió una falsificación.|arte
resistencia cardiovascular|re-sis-ten-cia car-dio-vas-cu-lar|locución nominal|Capacidad del corazón y los pulmones de sostener un esfuerzo largo.|-|-|Trotar mejora la resistencia cardiovascular.|educación física
fuerza explosiva|fuer-za ex-plo-si-va|locución nominal|Capacidad de producir mucha fuerza en muy poco tiempo.|-|-|El salto largo requiere fuerza explosiva.|educación física
equilibrio corporal|e-qui-li-brio cor-po-ral|locución nominal|Capacidad de mantener el cuerpo estable al moverse o quedarse quieto.|-|-|La gimnasia entrena el equilibrio corporal.|educación física
enfriamiento|en-fria-mien-to|sustantivo masculino|Ejercicios suaves al terminar la actividad para bajar el ritmo.|-|calentamiento|El enfriamiento ayuda a recuperarse.|educación física
vuelta a la calma|vuel-ta a la cal-ma|locución nominal|Última parte de una clase de ejercicio, con movimientos suaves.|-|-|En la vuelta a la calma respiramos profundo.|educación física
lesión deportiva|le-sión de-por-ti-va|locución nominal|Daño al cuerpo que ocurre al practicar un deporte.|-|-|Un buen calentamiento previene una lesión deportiva.|educación física
tendinitis|ten-di-ni-tis|sustantivo femenino|Inflamación de un tendón.|-|-|La tendinitis le impidió jugar tenis.|salud
contractura|con-trac-tu-ra|sustantivo femenino|Endurecimiento doloroso de un músculo.|-|-|Una contractura en la espalda le dolió dos días.|salud
desgarro|des-ga-rro|sustantivo masculino|Rotura de un músculo o tejido.|-|-|Sufrió un desgarro en el muslo.|salud
desfibrilador|des-fi-bri-la-dor|sustantivo masculino|Aparato que da una descarga eléctrica para restablecer el ritmo del corazón.|-|-|El desfibrilador salvó la vida del vecino.|salud
frecuencia respiratoria|fre-cuen-cia res-pi-ra-to-ria|locución nominal|Número de veces que una persona respira en un minuto.|-|-|La frecuencia respiratoria sube con el ejercicio.|salud
zona de entrenamiento|zo-na de en-tre-na-mien-to|locución nominal|Rango de intensidad en que se trabaja durante un ejercicio.|-|-|Mantén tu pulso en la zona de entrenamiento.|educación física
test físico|test fí-si-co|locución nominal|Prueba para medir la condición física de una persona.|-|-|Hicimos un test físico de resistencia.|educación física
circuito de entrenamiento|cir-cui-to de en-tre-na-mien-to|locución nominal|Serie de estaciones de ejercicios que se recorren una tras otra.|-|-|El circuito de entrenamiento tenía seis estaciones.|educación física
deporte colectivo|de-por-te co-lec-ti-vo|locución nominal|Deporte que se practica en equipo.|-|deporte individual|El básquetbol es un deporte colectivo.|educación física
deporte individual|de-por-te in-di-vi-dual|locución nominal|Deporte que se practica sin compañeros de equipo.|-|deporte colectivo|La natación es un deporte individual.|educación física
reglamento deportivo|re-gla-men-to de-por-ti-vo|locución nominal|Conjunto de normas de un deporte.|-|-|El reglamento deportivo prohíbe tocar la pelota con la mano.|educación física
contraataque|con-tra-a-ta-que|sustantivo masculino|Ataque que realiza un equipo justo después de defenderse.|-|-|El contraataque terminó en gol.|educación física
marca personal|mar-ca per-so-nal|locución nominal|Mejor resultado que ha conseguido un deportista.|-|-|Mejoró su marca personal en cien metros.|educación física
récord|ré-cord|sustantivo masculino|Mejor resultado alcanzado en una prueba.|-|-|La nadadora batió el récord nacional.|educación física
podio|po-dio|sustantivo masculino|Plataforma donde suben los tres primeros de una competencia.|-|-|Subió al podio con la medalla de plata.|educación física
medallero|me-da-lle-ro|sustantivo masculino|Tabla que muestra las medallas obtenidas por cada país.|-|-|Chile mejoró en el medallero.|educación física
juegos olímpicos|jue-gos o-lím-pi-cos|locución nominal|Gran competencia deportiva mundial que se realiza cada cuatro años.|-|-|Los juegos olímpicos reúnen a deportistas de todo el mundo.|educación física
inclusión deportiva|in-clu-sión de-por-ti-va|locución nominal|Participación de todas las personas en el deporte, sin discriminación.|-|-|La inclusión deportiva adapta las reglas para todos.|educación física
torneo|tor-ne-o|sustantivo masculino|Competencia en que participan varios equipos o jugadores.|campeonato|-|El torneo de ajedrez duró un fin de semana.|educación física
eliminatoria|e-li-mi-na-to-ria|sustantivo femenino|Prueba o partido que decide quién sigue en una competencia.|-|-|Pasamos la eliminatoria por un gol.|educación física
ambivalente|am-bi-va-len-te|adjetivo|Que tiene dos valores o sentimientos opuestos a la vez.|ambiguo|-|Tuvo una actitud ambivalente ante el cambio.|vocabulario académico
apático|a-pá-ti-co|adjetivo|Que muestra poco interés o ganas de hacer las cosas.|indiferente|entusiasta|El grupo estaba apático durante la clase.|vocabulario académico
ávido|á-vi-do|adjetivo|Que desea algo con mucha fuerza.|ansioso|desinteresado|Es un lector ávido de novelas.|vocabulario académico
enigmático|e-nig-má-ti-co|adjetivo|Que encierra un misterio y cuesta entenderlo.|misterioso|claro|Su sonrisa enigmática intrigó a todos.|vocabulario académico
equívoco|e-quí-vo-co|adjetivo|Que puede entenderse de dos modos y lleva a error.|ambiguo|claro|Dio una respuesta equívoca.|vocabulario académico
escrupuloso|es-cru-pu-lo-so|adjetivo|Que cuida con mucho detalle hacer las cosas bien y con honradez.|riguroso|descuidado|Es una contadora escrupulosa.|vocabulario académico
fehaciente|fe-ha-cien-te|adjetivo|Que prueba algo de manera segura.|probatorio|-|Presentó una prueba fehaciente de su identidad.|vocabulario académico
férreo|fé-rre-o|adjetivo|Muy firme y duro, como el hierro.|firme|blando|Mantuvo una disciplina férrea.|vocabulario académico
flagrante|fla-gran-te|adjetivo|Tan evidente que no admite dudas.|evidente|oculto|Fue un error flagrante.|vocabulario académico
fructífero|fruc-tí-fe-ro|adjetivo|Que da buenos resultados.|productivo|estéril|Fue una reunión fructífera.|vocabulario académico
gratuito|gra-tui-to|adjetivo|Que no cuesta dinero.|libre|pagado|La entrada al museo es gratuita los domingos.|vida cotidiana
impecable|im-pe-ca-ble|adjetivo|Sin ningún defecto ni error.|perfecto|defectuoso|Su cuaderno estaba impecable.|vocabulario académico
implacable|im-pla-ca-ble|adjetivo|Que no se puede aplacar ni detener.|inflexible|clemente|El sol fue implacable en el desierto.|vocabulario académico
incipiente|in-ci-pien-te|adjetivo|Que está empezando.|naciente|maduro|Había una incipiente amistad entre ellos.|vocabulario académico
inherente|in-he-ren-te|adjetivo|Que está unido a algo de manera inseparable.|propio|ajeno|El riesgo es inherente a todo deporte.|vocabulario académico
inmutable|in-mu-ta-ble|adjetivo|Que no cambia.|constante|variable|Su expresión se mantuvo inmutable.|vocabulario académico
jocoso|jo-co-so|adjetivo|Que causa gracia.|gracioso|serio|Contó una anécdota jocosa.|vocabulario académico
laborioso|la-bo-rio-so|adjetivo|Que trabaja con dedicación.|trabajador|perezoso|Es un alumno laborioso.|valores
mordaz|mor-daz|adjetivo|Que critica con ironía y de forma hiriente.|burlón|amable|Hizo un comentario mordaz.|vocabulario académico
nefasto|ne-fas-to|adjetivo|Muy malo o que trae mala suerte.|funesto|favorable|El clima nefasto arruinó la cosecha.|vocabulario académico
ostensible|os-ten-si-ble|adjetivo|Claramente visible o evidente.|notorio|oculto|Hubo una mejora ostensible.|vocabulario académico
pertinaz|per-ti-naz|adjetivo|Que dura mucho o que insiste con obstinación.|persistente|breve|Una lluvia pertinaz cayó toda la semana.|vocabulario académico
pragmático|prag-má-ti-co|adjetivo|Que da importancia a lo práctico y útil.|práctico|teórico|Buscó una solución pragmática.|vocabulario académico
prolífico|pro-lí-fi-co|adjetivo|Que produce muchas obras o resultados.|fecundo|estéril|Fue un autor prolífico.|vocabulario académico
providencial|pro-vi-den-cial|adjetivo|Que ocurre justo a tiempo, como por buena suerte.|oportuno|inoportuno|Su llegada fue providencial.|vocabulario académico
pueril|pue-ril|adjetivo|Propio de un niño pequeño, sin seriedad.|infantil|maduro|Fue una excusa pueril.|vocabulario académico
recurrente|re-cu-rren-te|adjetivo|Que vuelve a ocurrir o aparecer.|repetido|único|Es un tema recurrente en sus poemas.|vocabulario académico
remoto|re-mo-to|adjetivo|Que está muy lejos en el espacio o en el tiempo.|lejano|cercano|Visitó una aldea remota.|vocabulario académico
sagaz|sa-gaz|adjetivo|Que se da cuenta de las cosas y actúa con astucia.|astuto|ingenuo|El detective fue muy sagaz.|vocabulario académico
sibilino|si-bi-li-no|adjetivo|Que esconde un sentido oculto o malicioso.|enigmático|claro|Hizo una advertencia sibilina.|vocabulario académico
solemne|so-lem-ne|adjetivo|Que se hace con ceremonia y seriedad.|formal|informal|Fue un acto solemne.|vocabulario académico
taimado|tai-ma-do|adjetivo|Que es astuto y disimula sus intenciones.|astuto|sincero|El zorro taimado engañó al gallo.|vocabulario académico
tácito|tá-ci-to|adjetivo|Que se entiende sin que se diga.|implícito|expreso|Había un acuerdo tácito entre ellos.|vocabulario académico
titánico|ti-tá-ni-co|adjetivo|De enorme esfuerzo o tamaño.|colosal|mínimo|Fue un esfuerzo titánico.|vocabulario académico
trivial|tri-vial|adjetivo|De poca importancia.|insignificante|importante|Discutieron por un asunto trivial.|vocabulario académico
ubicuo|u-bi-cuo|adjetivo|Que está en todas partes al mismo tiempo.|omnipresente|-|Los celulares son ubicuos hoy.|vocabulario académico
vacilante|va-ci-lan-te|adjetivo|Que duda o no está firme.|dudoso|firme|Entró con paso vacilante.|vocabulario académico
abnegación|ab-ne-ga-ción|sustantivo femenino|Entrega que alguien hace de sus propios deseos por el bien de otros.|sacrificio|egoísmo|Cuidó a su familia con abnegación.|valores
agravio|a-gra-vio|sustantivo masculino|Ofensa o daño que se hace a alguien.|ofensa|elogio|Sintió el comentario como un agravio.|valores
arrojo|a-rro-jo|sustantivo masculino|Valentía para enfrentar un peligro.|valentía|cobardía|Actuó con arrojo al salvar al niño.|valores
ascendencia|as-cen-den-cia|sustantivo femenino|Conjunto de antepasados de una persona.|linaje|descendencia|Su ascendencia es italiana.|cultura
aversión|a-ver-sión|sustantivo femenino|Rechazo muy fuerte hacia algo.|repulsión|simpatía|Siente aversión por las alturas.|vocabulario académico
bagaje|ba-ga-je|sustantivo masculino|Conjunto de conocimientos o experiencias de una persona.|experiencia|-|Tiene un gran bagaje cultural.|vocabulario académico
cavilación|ca-vi-la-ción|sustantivo femenino|Pensamiento profundo y prolongado sobre un asunto.|reflexión|-|Se perdió en sus cavilaciones.|vocabulario académico
certidumbre|cer-ti-dum-bre|sustantivo femenino|Seguridad total de que algo es cierto.|certeza|incertidumbre|Habló con certidumbre.|vocabulario académico
cometido|co-me-ti-do|sustantivo masculino|Tarea o misión que debe cumplirse.|misión|-|Cumplió su cometido a tiempo.|vocabulario académico
concordia|con-cor-dia|sustantivo femenino|Buena relación entre personas que piensan distinto.|armonía|discordia|Los vecinos vivieron en concordia.|valores
conjetura|con-je-tu-ra|sustantivo femenino|Juicio que se forma a partir de indicios sin pruebas seguras.|suposición|certeza|Era solo una conjetura sin prueba.|vocabulario académico
desatino|de-sa-ti-no|sustantivo masculino|Acción o idea sin sensatez.|disparate|acierto|Fue un desatino salir sin paraguas.|vocabulario académico
discernimiento|dis-cer-ni-mien-to|sustantivo masculino|Capacidad de distinguir lo correcto de lo incorrecto.|juicio|-|Actuó con discernimiento.|valores
disyuntiva|dis-yun-ti-va|sustantivo femenino|Situación en que hay que elegir entre dos opciones.|dilema|-|Se vio ante una disyuntiva difícil.|vocabulario académico
eficacia|e-fi-ca-cia|sustantivo femenino|Capacidad de lograr el efecto que se desea.|efectividad|ineficacia|La eficacia de la vacuna fue alta.|vocabulario académico
entereza|en-te-re-za|sustantivo femenino|Firmeza de ánimo para soportar las dificultades.|fortaleza|debilidad|Enfrentó la noticia con entereza.|valores
exceso|ex-ce-so|sustantivo masculino|Cantidad que pasa lo que es normal o necesario.|sobra|falta|El exceso de sal es perjudicial.|vocabulario académico
fervor|fer-vor|sustantivo masculino|Entusiasmo muy intenso.|pasión|apatía|Defendió su idea con fervor.|valores
fortuna|for-tu-na|sustantivo femenino|Suerte o conjunto de riquezas.|suerte|desgracia|Tuvo la fortuna de encontrar su mochila.|vocabulario académico
idiosincrasia|i-dio-sin-cra-sia|sustantivo femenino|Carácter y modo de ser propios de una persona o pueblo.|carácter|-|La idiosincrasia chilena valora la solidaridad.|cultura
impronta|im-pron-ta|sustantivo femenino|Huella o marca que algo deja en otra cosa.|huella|-|Dejó su impronta en el colegio.|vocabulario académico
incertidumbre|in-cer-ti-dum-bre|sustantivo femenino|Falta de seguridad sobre algo.|duda|certeza|Había incertidumbre sobre el resultado.|vocabulario académico
inquietud|in-quie-tud|sustantivo femenino|Sensación de nerviosismo o deseo de saber más.|desasosiego|calma|La inquietud no la dejó dormir.|vocabulario académico
juicio|jui-cio|sustantivo masculino|Capacidad de pensar con sensatez o proceso ante un tribunal.|criterio|-|Mostró buen juicio al decidir.|vocabulario académico
lealtad|le-al-tad|sustantivo femenino|Fidelidad hacia una persona o causa.|fidelidad|traición|Su lealtad fue clave en el equipo.|valores
linaje|li-na-je|sustantivo masculino|Conjunto de antepasados y descendientes de una familia.|estirpe|-|Su linaje se remonta a los colonos.|cultura
magnanimidad|mag-na-ni-mi-dad|sustantivo femenino|Grandeza de ánimo para perdonar y ser generoso.|generosidad|mezquindad|Actuó con magnanimidad al perdonar la deuda.|valores
menoscabo|me-nos-ca-bo|sustantivo masculino|Disminución o daño que sufre algo.|detrimento|mejora|Trabajó sin menoscabo de su salud.|vocabulario académico
mesura|me-su-ra|sustantivo femenino|Moderación y respeto al actuar o hablar.|moderación|exceso|Habló con mesura en el debate.|valores
moderación|mo-de-ra-ción|sustantivo femenino|Actitud de no pasarse de lo justo en lo que se hace.|mesura|exceso|Comer con moderación cuida la salud.|valores
osadía|o-sa-dí-a|sustantivo femenino|Atrevimiento para hacer algo difícil o arriesgado.|audacia|timidez|Su osadía le permitió cruzar el río.|valores
panorama|pa-no-ra-ma|sustantivo masculino|Vista amplia de un lugar o visión general de una situación.|vista|-|Desde el cerro se ve un panorama hermoso.|vocabulario académico
pesadumbre|pe-sa-dum-bre|sustantivo femenino|Tristeza profunda.|aflicción|alegría|Lo invadió la pesadumbre.|emociones
premura|pre-mu-ra|sustantivo femenino|Prisa o urgencia.|prisa|calma|Salió con premura del colegio.|vocabulario académico
prerrogativa|pre-rro-ga-ti-va|sustantivo femenino|Privilegio o derecho propio de un cargo.|privilegio|-|El voto es prerrogativa de los ciudadanos.|ciudadanía
presagio|pre-sa-gio|sustantivo masculino|Señal que anuncia algo que va a ocurrir.|augurio|-|El cielo oscuro era un presagio de tormenta.|vocabulario académico
primicia|pri-mi-cia|sustantivo femenino|Noticia que se da por primera vez.|novedad|-|El diario publicó la primicia.|medios
rigor|ri-gor|sustantivo masculino|Exactitud y severidad al hacer algo.|exactitud|descuido|Trabajó con rigor científico.|vocabulario académico
sensatez|sen-sa-tez|sustantivo femenino|Cualidad de actuar con buen juicio.|prudencia|insensatez|La sensatez evitó un accidente.|valores
sosiego|so-sie-go|sustantivo masculino|Calma y tranquilidad.|calma|agitación|Buscó sosiego en el campo.|emociones
vaivén|vai-vén|sustantivo masculino|Movimiento de ida y vuelta.|balanceo|-|El vaivén del barco me mareó.|vocabulario académico
vicisitud|vi-ci-si-tud|sustantivo femenino|Cambio de situación, favorable o no.|contratiempo|-|Superó las vicisitudes del viaje.|vocabulario académico
vigencia|vi-gen-cia|sustantivo femenino|Condición de lo que sigue siendo válido o vigente.|validez|-|La ley sigue teniendo vigencia.|ciudadanía
zozobra|zo-zo-bra|sustantivo femenino|Inquietud o angustia por una amenaza.|angustia|tranquilidad|Esperó los resultados con zozobra.|emociones
"""

VERBOS = """
elaborar|e-la-bo-rar|Preparar algo con trabajo y cuidado.|elaboro|elabora|elaboró|elaborará|preparar|-|Elaboro un informe sobre el reciclaje.
diferenciar|di-fe-ren-ciar|Reconocer lo que hace distintas a dos cosas.|diferencio|diferencia|diferenció|diferenciará|distinguir|confundir|Diferencio un hecho de una opinión.
tamizar|ta-mi-zar|Pasar una sustancia por un colador para separar las partes gruesas.|tamizo|tamiza|tamizó|tamizará|colar|-|Tamizo la harina antes de amasar.
cachar|ca-char|Darse cuenta o entender algo (uso en Chile).|cacho|cacha|cachó|cachará|entender|-|Cacho que hoy hay prueba.
excluir|ex-cluir|Dejar algo fuera de un grupo.|excluyo|excluye|excluyó|excluirá|apartar|incluir|Excluyo los datos incorrectos.
oponer|o-po-ner|Poner algo en contra de otra cosa.|opongo|opone|opuso|opondrá|enfrentar|apoyar|Opongo un argumento fuerte a esa idea.
preferir|pre-fe-rir|Elegir algo antes que otra cosa.|prefiero|prefiere|prefirió|preferirá|elegir|rechazar|Prefiero estudiar en la mañana.
divertir|di-ver-tir|Hacer pasar un rato agradable.|divierto|divierte|divirtió|divertirá|entretener|aburrir|Me divierte leer comics.
fingir|fin-gir|Aparentar algo que no es verdad.|finjo|finge|fingió|fingirá|simular|-|Finjo calma aunque estoy nervioso.
esparcir|es-par-cir|Dispersar algo en varias partes.|esparzo|esparce|esparció|esparcirá|dispersar|juntar|Esparzo las semillas en la tierra.
continuar|con-ti-nuar|Seguir haciendo algo.|continúo|continúa|continuó|continuará|seguir|detener|Continúo con el trabajo después del recreo.
graduar|gra-duar|Dar cierto grado a algo o terminar los estudios.|gradúo|gradúa|graduó|graduará|regular|-|Gradúo la luz de la lámpara.
guiar|guiar|Mostrar el camino a alguien.|guío|guía|guio|guiará|conducir|-|Guío al grupo por el sendero.
reírse|re-ír-se|Mostrar alegría con sonidos y gestos.|me río|se ríe|se rio|se reirá|carcajearse|llorar|Me río con las bromas de mi curso.
sonreír|son-re-ír|Mostrar alegría con la boca sin hacer ruido.|sonrío|sonríe|sonrió|sonreirá|-|fruncir|Sonrío al ver a mi amigo.
freír|fre-ír|Cocinar un alimento en aceite caliente.|frío|fríe|frio|freirá|-|-|Frío unas papas.
caber|ca-ber|Poder entrar una cosa en otra.|quepo|cabe|cupo|cabrá|-|-|Quepo en ese asiento.
balancear|ba-lan-ce-ar|Ajustar una ecuación química para que haya los mismos átomos a cada lado.|balanceo|balancea|balanceó|balanceará|equilibrar|desequilibrar|Balanceo la ecuación del agua.
abordar|a-bor-dar|Empezar a tratar un asunto o acercarse a algo.|abordo|aborda|abordó|abordará|encarar|eludir|Abordo el tema con calma.
acechar|a-ce-char|Vigilar a escondidas para atacar o sorprender.|acecho|acecha|acechó|acechará|vigilar|-|El gato acecha al ratón.
aducir|a-du-cir|Dar razones o pruebas para apoyar lo que se dice.|aduzco|aduce|adujo|aducirá|alegar|-|Aduzco un ejemplo del texto.
afianzar|a-fian-zar|Hacer algo más firme y seguro.|afianzo|afianza|afianzó|afianzará|asegurar|debilitar|Afianzo lo aprendido con ejercicios.
agilizar|a-gi-li-zar|Hacer algo más rápido y fácil.|agilizo|agiliza|agilizó|agilizará|acelerar|retrasar|Agilizo el trámite con un formulario en línea.
alentar|a-len-tar|Dar ánimo a alguien para que siga.|aliento|alienta|alentó|alentará|animar|desanimar|Aliento a mi equipo en la final.
amparar|am-pa-rar|Proteger a alguien de un daño.|amparo|ampara|amparó|amparará|proteger|abandonar|La ley ampara a los menores.
anteponer|an-te-po-ner|Poner una cosa antes que otra.|antepongo|antepone|antepuso|antepondrá|preferir|posponer|Antepongo la honestidad a la ganancia.
aplacar|a-pla-car|Calmar algo que está agitado.|aplaco|aplaca|aplacó|aplacará|calmar|agitar|El diálogo aplaca el enojo.
arraigar|a-rrai-gar|Echar raíces o fijarse con firmeza.|arraigo|arraiga|arraigó|arraigará|enraizar|desarraigar|La costumbre arraiga en la comunidad.
asentir|a-sen-tir|Aceptar lo que otro dice, a menudo con un gesto.|asiento|asiente|asintió|asentirá|aprobar|negar|Asiento con la cabeza.
atribuir|a-tri-buir|Decir que algo es obra o característica de alguien.|atribuyo|atribuye|atribuyó|atribuirá|adjudicar|-|Atribuyo el éxito al esfuerzo del equipo.
avalar|a-va-lar|Respaldar algo con la propia autoridad.|avalo|avala|avaló|avalará|respaldar|desautorizar|El estudio avala la hipótesis.
cimentar|ci-men-tar|Poner bases firmes para algo.|cimiento|cimienta|cimentó|cimentará|fundar|-|Cimiento mi proyecto en datos reales.
clausurar|clau-su-rar|Cerrar o dar por terminado algo de manera formal.|clausuro|clausura|clausuró|clausurará|cerrar|inaugurar|La directora clausura el año escolar.
colmar|col-mar|Llenar algo hasta el borde.|colmo|colma|colmó|colmará|llenar|vaciar|La noticia colmó de alegría a mi familia.
concertar|con-cer-tar|Acordar algo entre varias partes.|concierto|concierta|concertó|concertará|pactar|romper|Concierto una cita con la profesora.
condenar|con-de-nar|Declarar culpable a alguien o rechazar algo con firmeza.|condeno|condena|condenó|condenará|sentenciar|absolver|El jurado condenó la violencia.
conferir|con-fe-rir|Dar un cargo, un derecho o una cualidad.|confiero|confiere|confirió|conferirá|otorgar|quitar|El título confiere derechos.
congregar|con-gre-gar|Reunir a muchas personas en un lugar.|congrego|congrega|congregó|congregará|reunir|dispersar|El concierto congregó a miles.
consagrar|con-sa-grar|Dedicar algo por completo a un fin.|consagro|consagra|consagró|consagrará|dedicar|-|Consagro mis tardes al estudio.
contemplar|con-tem-plar|Mirar con atención y detenimiento.|contemplo|contempla|contempló|contemplará|observar|-|Contemplo el mar desde el cerro.
contrariar|con-tra-riar|Oponerse a algo o causar disgusto.|contrarío|contraría|contrarió|contrariará|disgustar|complacer|Me contraría perder tiempo.
convocar|con-vo-car|Llamar a un grupo para que se reúna.|convoco|convoca|convocó|convocará|citar|despedir|Convoco a una reunión de curso.
cotejar|co-te-jar|Comparar dos cosas para ver sus diferencias.|cotejo|coteja|cotejó|cotejará|comparar|-|Coteja las dos versiones del texto.
declinar|de-cli-nar|Rechazar una invitación o ir perdiendo fuerza.|declino|declina|declinó|declinará|rechazar|aceptar|Declino la invitación con amabilidad.
delinear|de-li-ne-ar|Trazar las líneas de algo o describir sus rasgos principales.|delineo|delinea|delineó|delineará|esbozar|-|Delineo el plan de trabajo.
desentrañar|de-sen-tra-ñar|Descubrir el sentido de algo difícil de entender.|desentraño|desentraña|desentrañó|desentrañará|descifrar|-|Desentraño el misterio del poema.
desistir|de-sis-tir|Abandonar un intento.|desisto|desiste|desistió|desistirá|renunciar|persistir|No desisto de mi meta.
designar|de-sig-nar|Señalar a una persona o cosa para un fin.|designo|designa|designó|designará|nombrar|destituir|La directora designa a un representante.
desvelar|des-ve-lar|Revelar algo oculto o quitar el sueño.|desvelo|desvela|desveló|desvelará|revelar|ocultar|El estudio desvela nuevos datos.
divagar|di-va-gar|Hablar o pensar sin rumbo fijo.|divago|divaga|divagó|divagará|desviarse|centrarse|No divago en mi exposición.
dotar|do-tar|Proveer a alguien o algo de lo necesario.|doto|dota|dotó|dotará|equipar|privar|La escuela se dota de nuevos libros.
ejercer|e-jer-cer|Practicar una profesión o usar un derecho o poder.|ejerzo|ejerce|ejerció|ejercerá|desempeñar|-|Ejerzo mi derecho a opinar.
emanar|e-ma-nar|Salir o proceder de algún lugar o fuente.|emano|emana|emanó|emanará|brotar|-|El olor emana de la cocina.
encarar|en-ca-rar|Enfrentar un problema con decisión.|encaro|encara|encaró|encarará|afrontar|evitar|Encaro la prueba con confianza.
encauzar|en-cau-zar|Guiar algo por buen camino.|encauzo|encauza|encauzó|encauzará|orientar|desviar|El profesor encauza el debate.
entablar|en-ta-blar|Iniciar una conversación o relación.|entablo|entabla|entabló|entablará|iniciar|terminar|Entablo amistad con los nuevos.
entrañar|en-tra-ñar|Llevar dentro de sí o implicar.|entraño|entraña|entrañó|entrañará|implicar|-|Ese trabajo entraña riesgos.
escudriñar|es-cu-dri-ñar|Examinar con mucha atención.|escudriño|escudriña|escudriñó|escudriñará|indagar|-|Escudriño el texto en busca de pistas.
esgrimir|es-gri-mir|Usar un argumento o un arma para defenderse o atacar.|esgrimo|esgrime|esgrimió|esgrimirá|blandir|-|Esgrimo un argumento sólido.
esclarecer|es-cla-re-cer|Aclarar algo que estaba confuso.|esclarezco|esclarece|esclareció|esclarecerá|aclarar|confundir|La investigación esclarece los hechos.
estipular|es-ti-pu-lar|Establecer una condición en un acuerdo.|estipulo|estipula|estipuló|estipulará|fijar|-|El contrato estipula el plazo.
evocar|e-vo-car|Traer a la mente un recuerdo.|evoco|evoca|evocó|evocará|recordar|olvidar|Esta canción evoca mi infancia.
exhortar|ex-hor-tar|Pedir con fuerza que alguien haga algo.|exhorto|exhorta|exhortó|exhortará|instar|-|La directora exhorta a cuidar el patio.
fraguar|fra-guar|Planear o formar algo, como una idea o un plan.|fraguo|fragua|fraguó|fraguará|forjar|-|Fraguo un proyecto de ciencias.
gestar|ges-tar|Desarrollar algo desde sus orígenes.|gesto|gesta|gestó|gestará|originar|-|Una nueva idea se gesta en el grupo.
hostigar|hos-ti-gar|Molestar de forma repetida a alguien.|hostigo|hostiga|hostigó|hostigará|acosar|respetar|Nadie debe hostigar a un compañero.
incidir|in-ci-dir|Tener efecto sobre algo.|incido|incide|incidió|incidirá|influir|-|El sueño incide en el rendimiento.
inculcar|in-cul-car|Hacer que alguien aprenda una idea o un hábito.|inculco|inculca|inculcó|inculcará|enseñar|-|Mis padres me inculcan el respeto.
indignar|in-dig-nar|Producir enojo por algo injusto.|indigno|indigna|indignó|indignará|irritar|calmar|La injusticia me indigna.
infundir|in-fun-dir|Causar en alguien un sentimiento.|infundo|infunde|infundió|infundirá|inspirar|-|La profesora infunde confianza.
ingeniar|in-ge-niar|Inventar con inteligencia una solución.|ingenio|ingenia|ingenió|ingeniará|idear|-|Ingenio un modo de ordenar los datos.
inhibir|in-hi-bir|Impedir o frenar algo.|inhibo|inhibe|inhibió|inhibirá|frenar|estimular|El miedo inhibe mi voz.
instar|ins-tar|Pedir algo con insistencia.|insto|insta|instó|instará|exhortar|-|Insto a mis compañeros a participar.
interceder|in-ter-ce-der|Hablar a favor de alguien para ayudarlo.|intercedo|intercede|intercedió|intercederá|mediar|-|Intercedo por mi amigo ante la directora.
invocar|in-vo-car|Pedir ayuda o citar algo como razón.|invoco|invoca|invocó|invocará|apelar|-|Invoco un artículo de la ley.
irrumpir|i-rrum-pir|Entrar de golpe y con fuerza en un lugar.|irrumpo|irrumpe|irrumpió|irrumpirá|invadir|-|Los niños irrumpen en el patio.
legitimar|le-gi-ti-mar|Hacer que algo sea legal o aceptado como válido.|legitimo|legitima|legitimó|legitimará|validar|invalidar|La votación legitima al gobierno.
menospreciar|me-nos-pre-ciar|Considerar que algo vale menos de lo que vale.|menosprecio|menosprecia|menospreció|menospreciará|despreciar|valorar|No menosprecio el trabajo ajeno.
ostentar|os-ten-tar|Mostrar algo con orgullo o desempeñar un cargo.|ostento|ostenta|ostentó|ostentará|exhibir|ocultar|Ostenta el récord de la clase.
paliar|pa-liar|Aliviar un mal sin curarlo del todo.|palío|palía|palió|paliará|aliviar|agravar|Palío el dolor con una compresa.
perdurar|per-du-rar|Durar mucho tiempo.|perduro|perdura|perduró|perdurará|persistir|acabar|El recuerdo perdura por años.
perpetuar|per-pe-tuar|Hacer que algo dure para siempre.|perpetúo|perpetúa|perpetuó|perpetuará|eternizar|-|Perpetúo la tradición familiar.
profesar|pro-fe-sar|Declarar abiertamente una creencia o sentimiento.|profeso|profesa|profesó|profesará|declarar|-|Profeso respeto por todas las ideas.
propiciar|pro-pi-ciar|Crear las condiciones para que algo ocurra.|propicio|propicia|propició|propiciará|favorecer|impedir|La lectura propicia el diálogo.
quebrantar|que-bran-tar|No cumplir una ley, una promesa o una norma.|quebranto|quebranta|quebrantó|quebrantará|infringir|cumplir|Quien quebranta la norma recibe una sanción.
rebatir|re-ba-tir|Refutar con razones lo que alguien dijo.|rebato|rebate|rebatió|rebatirá|refutar|aceptar|Rebato su argumento con un dato.
recabar|re-ca-bar|Reunir información o apoyo para algo.|recabo|recaba|recabó|recabará|recopilar|-|Recabo datos para mi investigación.
recelar|re-ce-lar|Desconfiar de algo o de alguien.|recelo|recela|receló|recelará|desconfiar|confiar|Recelo de las ofertas que parecen demasiado buenas.
recomendar|re-co-men-dar|Aconsejar algo por ser bueno o útil.|recomiendo|recomienda|recomendó|recomendará|aconsejar|desaconsejar|Recomiendo leer ese libro.
reivindicar|rei-vin-di-car|Reclamar algo a lo que se tiene derecho.|reivindico|reivindica|reivindicó|reivindicará|reclamar|renunciar|Reivindico mi derecho a opinar.
relegar|re-le-gar|Dejar algo en un lugar de menor importancia.|relego|relega|relegó|relegará|postergar|promover|No relego mis estudios por jugar.
remediar|re-me-diar|Poner solución a un daño o problema.|remedio|remedia|remedió|remediará|reparar|agravar|Remedio el error pidiendo disculpas.
repudiar|re-pu-diar|Rechazar algo con firmeza por considerarlo inaceptable.|repudio|repudia|repudió|repudiará|rechazar|aprobar|Repudio la violencia.
rescatar|res-ca-tar|Sacar a alguien o algo de un peligro o de un olvido.|rescato|rescata|rescató|rescatará|salvar|abandonar|Rescato una vieja tradición familiar.
rezagar|re-za-gar|Dejar atrás o quedarse atrás.|rezago|rezaga|rezagó|rezagará|retrasar|adelantar|No me rezago en la lectura.
rubricar|ru-bri-car|Firmar un documento o confirmar algo.|rubrico|rubrica|rubricó|rubricará|firmar|-|La alcaldesa rubrica el acuerdo.
salvaguardar|sal-va-guar-dar|Proteger algo de un daño.|salvaguardo|salvaguarda|salvaguardó|salvaguardará|proteger|dañar|La ley salvaguarda el medio ambiente.
sentenciar|sen-ten-ciar|Dictar una pena o declarar algo con autoridad.|sentencio|sentencia|sentenció|sentenciará|dictaminar|absolver|El juez sentencia el caso.
sobrellevar|so-bre-lle-var|Soportar con paciencia una dificultad.|sobrellevo|sobrelleva|sobrellevó|sobrellevará|aguantar|-|Sobrellevo la presión con calma.
sopesar|so-pe-sar|Comparar con cuidado ventajas y desventajas.|sopeso|sopesa|sopesó|sopesará|ponderar|-|Sopeso mis opciones antes de elegir.
sortear|sor-te-ar|Escapar con habilidad de una dificultad o decidir por sorteo.|sorteo|sortea|sorteó|sorteará|eludir|-|Sorteo los obstáculos del camino.
suscitar|sus-ci-tar|Provocar o despertar un sentimiento o una reacción.|suscito|suscita|suscitó|suscitará|provocar|-|La obra suscita muchas preguntas.
tantear|tan-te-ar|Probar con cuidado para conocer algo antes de decidir.|tanteo|tantea|tanteó|tanteará|sondear|-|Tanteo el terreno antes de cruzar.
transgredir|trans-gre-dir|Violar una ley o una norma.|transgredo|transgrede|transgredió|transgredirá|infringir|acatar|Quien transgrede la norma asume las consecuencias.
vaticinar|va-ti-ci-nar|Anunciar lo que sucederá en el futuro.|vaticino|vaticina|vaticinó|vaticinará|predecir|-|Vaticino una tarde lluviosa.
verter|ver-ter|Echar un líquido fuera de un recipiente.|vierto|vierte|vertió|verterá|derramar|-|Vierto el agua en el vaso.
vulnerar|vul-ne-rar|Dañar un derecho o la seguridad de algo.|vulnero|vulnera|vulneró|vulnerará|infringir|proteger|Nadie debe vulnerar los derechos de otro.
zanjar|zan-jar|Resolver un asunto de manera definitiva.|zanjo|zanja|zanjó|zanjará|resolver|-|Zanjo la discusión con un acuerdo.
"""
