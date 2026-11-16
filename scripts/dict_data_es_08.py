"""Diccionario de español de 8.º básico: palabras y verbos nuevos del nivel.

Formato de PALABRAS (una por línea, separado por «|»):
    palabra|sílabas|clase|significado|sinónimos|antónimos|ejemplo|tema
Formato de VERBOS:
    infinitivo|sílabas|significado|yo (hoy)|él o ella (hoy)|él o ella (ayer)|él o ella (mañana)|sinónimos|antónimos|ejemplo
Un guion «-» significa que no hay sinónimo o antónimo sencillo para ese nivel.
Textos propios del proyecto: no copian ningún diccionario publicado.
"""

NIVEL = "8-basico"
IDIOMA = "es"

PALABRAS = """
protagonista|pro-ta-go-nis-ta|sustantivo común|Personaje principal de una historia.|héroe|antagonista|La protagonista cruza el desierto sola.|literatura
antagonista|an-ta-go-nis-ta|sustantivo común|Personaje que se opone a los deseos del protagonista.|rival|protagonista|El antagonista tiende una trampa al héroe.|literatura
hablante lírico|ha-blan-te lí-ri-co|locución nominal|Voz que expresa sus sentimientos en un poema; no siempre es el autor.|-|-|El hablante lírico siente nostalgia por su patria.|literatura
oda|o-da|sustantivo femenino|Poema que celebra o alaba a una persona, una cosa o una idea.|-|-|Neruda escribió una oda a la cebolla.|literatura
elegía|e-le-gí-a|sustantivo femenino|Poema que expresa tristeza por la muerte de alguien o por una pérdida.|lamento|-|Escribió una elegía para su abuelo.|literatura
anáfora|a-ná-fo-ra|sustantivo femenino|Repetición de una palabra al comienzo de varios versos o frases.|-|-|La anáfora de «quiero» marca el ritmo del poema.|literatura
elenco|e-len-co|sustantivo masculino|Grupo de actores de una obra o película.|reparto|-|Todo el elenco salió a saludar.|literatura
fidedigno|fi-de-dig-no|adjetivo|Digno de confianza.|confiable|dudoso|Usamos un sitio fidedigno para investigar.|investigación
veraz|ve-raz|adjetivo|Que dice o muestra la verdad.|sincero|falso|Un periodista debe ser veraz.|investigación
paráfrasis|pa-rá-fra-sis|sustantivo femenino|Explicación de un texto con otras palabras, sin cambiar su sentido.|-|cita textual|En la paráfrasis conté el cuento con mis palabras.|lenguaje
cita textual|ci-ta tex-tual|locución nominal|Fragmento copiado igual que en el original y puesto entre comillas.|-|paráfrasis|La cita textual lleva comillas y el nombre del autor.|lenguaje
referencia|re-fe-ren-cia|sustantivo femenino|Dato que indica de dónde viene una información.|alusión|-|Cada referencia incluye autor y año.|investigación
campo semántico|cam-po se-mán-ti-co|locución nominal|Grupo de palabras que se relacionan por su significado.|-|-|«Pelota», «arco» y «gol» forman un campo semántico.|lenguaje
derivación|de-ri-va-ción|sustantivo femenino|Formación de palabras nuevas a partir de otra usando prefijos o sufijos.|-|-|«Zapatería» nace por derivación de «zapato».|lenguaje
oración compuesta|o-ra-ción com-pues-ta|locución nominal|Oración que tiene más de un verbo conjugado.|-|oración simple|«Llegué y comí» es una oración compuesta.|gramática
oración simple|o-ra-ción sim-ple|locución nominal|Oración que tiene un solo verbo conjugado.|-|oración compuesta|«El gato duerme» es una oración simple.|gramática
voz pasiva|voz pa-si-va|locución nominal|Construcción en que el sujeto recibe la acción del verbo.|-|voz activa|«El libro fue leído por Ana» está en voz pasiva.|gramática
diéresis|dié-re-sis|sustantivo femenino|Signo formado por dos puntos que se pone sobre la «u» en «güe» o «güi».|-|-|«Pingüino» se escribe con diéresis.|ortografía
comillas|co-mi-llas|sustantivo femenino plural|Signos que se ponen al inicio y al final de una cita o de un título.|-|-|Escribí el título entre comillas.|ortografía
puntos suspensivos|pun-tos sus-pen-si-vos|locución nominal|Tres puntos que dejan una frase sin terminar o indican duda.|-|-|Usé puntos suspensivos para dejar el final abierto.|ortografía
homófono|ho-mó-fo-no|sustantivo masculino|Palabra que suena igual que otra, pero se escribe distinto.|-|-|«Hola» y «ola» son homófonos.|ortografía
sintaxis|sin-ta-xis|sustantivo femenino|Parte de la gramática que estudia cómo se combinan las palabras en la oración.|-|-|En clase estudiamos sintaxis.|gramática
Renacimiento|Re-na-ci-mien-to|sustantivo masculino|Movimiento cultural europeo de los siglos XV y XVI que renovó el arte y las ciencias.|-|-|El Renacimiento nació en Italia.|historia
humanismo|hu-ma-nis-mo|sustantivo masculino|Corriente de pensamiento que pone al ser humano y su razón en el centro.|-|-|El humanismo impulsó el estudio de los clásicos.|historia
mecenas|me-ce-nas|sustantivo común|Persona rica que financia a artistas o científicos.|patrocinador|-|Los Médici fueron mecenas de muchos artistas.|historia
imprenta|im-pren-ta|sustantivo femenino|Máquina que reproduce textos en gran cantidad, inventada en Europa en el siglo XV.|-|-|La imprenta permitió difundir los libros.|historia
protestante|pro-tes-tan-te|adjetivo|Que pertenece a las Iglesias cristianas surgidas de la Reforma.|-|-|La región adoptó la fe protestante.|historia
católico|ca-tó-li-co|adjetivo|Que pertenece a la Iglesia cristiana dirigida por el papa.|-|-|La familia es católica.|historia
absolutismo|ab-so-lu-tis-mo|sustantivo masculino|Sistema en que el rey concentra todo el poder.|-|democracia|Luis XIV encarnó el absolutismo.|historia
monarca|mo-nar-ca|sustantivo común|Rey o reina que gobierna un reino.|soberano|-|El monarca firmó el decreto.|historia
reino|rei-no|sustantivo masculino|Territorio gobernado por un rey o una reina.|-|-|El reino se extendía hasta el mar.|historia
navegante|na-ve-gan-te|sustantivo común|Persona que viaja por el mar.|marino|-|El navegante cruzó el estrecho.|historia
mestizo|mes-ti-zo|sustantivo masculino|Persona hija de padre de origen europeo y madre indígena, o al revés.|-|-|Los mestizos fueron muchos en la Colonia.|historia
peninsular|pe-nin-su-lar|sustantivo común|Persona española que llegó a vivir a América.|-|criollo|Los peninsulares ocupaban los cargos más altos.|historia
evangelización|e-van-ge-li-za-ción|sustantivo femenino|Difusión de la fe cristiana entre los pueblos indígenas.|-|-|Los misioneros realizaron la evangelización.|historia
virrey|vi-rrey|sustantivo masculino|Autoridad que gobernaba un virreinato en nombre del rey.|-|-|El virrey vivía en Lima.|historia
real audiencia|real au-dien-cia|locución nominal|Tribunal colonial que también aconsejaba al gobernador.|-|-|La Real Audiencia resolvía pleitos.|historia
mercantilismo|mer-can-ti-lis-mo|sustantivo masculino|Idea económica que busca acumular oro y plata y vender más de lo que se compra.|-|-|El mercantilismo guió el comercio colonial.|historia
monopolio|mo-no-po-lio|sustantivo masculino|Control de un comercio por una sola persona o grupo.|-|competencia|España tenía el monopolio comercial con sus colonias.|historia
mita|mi-ta|sustantivo femenino|Trabajo obligatorio por turnos que se imponía a los indígenas.|-|-|La mita en las minas fue muy dura.|historia
estamento|es-ta-men-to|sustantivo masculino|Grupo social con derechos y funciones propios.|-|-|El clero era un estamento privilegiado.|historia
privilegio|pri-vi-le-gio|sustantivo masculino|Ventaja que tienen algunos y otros no.|ventaja|desventaja|Los nobles tenían privilegios.|historia
nobleza|no-ble-za|sustantivo femenino|Grupo social de familias con títulos heredados.|aristocracia|plebe|La nobleza poseía grandes tierras.|historia
clero|cle-ro|sustantivo masculino|Conjunto de sacerdotes y religiosos de una Iglesia.|-|-|El clero tenía mucha influencia.|historia
burguesía|bur-gue-sí-a|sustantivo femenino|Grupo social de comerciantes y dueños de negocios.|-|-|La burguesía financió muchas obras de arte.|historia
feudalismo|feu-da-lis-mo|sustantivo masculino|Sistema medieval en que los campesinos trabajaban tierras de un señor a cambio de protección.|-|-|El feudalismo dominó la Edad Media.|historia
medieval|me-die-val|adjetivo|De la Edad Media.|-|-|Visité un castillo medieval.|historia
línea de tiempo|lí-ne-a de tiem-po|locución nominal|Dibujo que ubica hechos en orden según la fecha en que ocurrieron.|-|-|Hicimos una línea de tiempo del Renacimiento.|historia
fuente primaria|fuen-te pri-ma-ria|locución nominal|Documento o testimonio de la época que se estudia.|-|fuente secundaria|Una carta de Valdivia es una fuente primaria.|historia
fuente secundaria|fuen-te se-cun-da-ria|locución nominal|Texto escrito después de los hechos, que los analiza.|-|fuente primaria|Un libro de texto es una fuente secundaria.|historia
cambio|cam-bio|sustantivo masculino|Paso de un estado a otro distinto.|transformación|continuidad|El invento trajo un gran cambio.|historia
raíz cuadrada|ra-íz cua-dra-da|locución nominal|Número que, multiplicado por sí mismo, da el número dado.|-|-|La raíz cuadrada de 49 es 7.|matemática
cuadrado perfecto|cua-dra-do per-fec-to|locución nominal|Número que es el cuadrado de un número entero.|-|-|El 36 es un cuadrado perfecto.|matemática
número entero|nú-me-ro en-te-ro|locución nominal|Número sin parte decimal, que puede ser positivo, negativo o cero.|-|-|El −4 es un número entero.|matemática
número racional|nú-me-ro ra-cio-nal|locución nominal|Número que se puede escribir como fracción de dos enteros.|-|número irracional|El 0,5 es un número racional.|matemática
irracional|i-rra-cio-nal|adjetivo|Se dice del número decimal infinito que no se puede escribir como fracción.|-|racional|El número pi es irracional.|matemática
valor absoluto|va-lor ab-so-lu-to|locución nominal|Distancia de un número al cero, sin importar su signo.|-|-|El valor absoluto de −7 es 7.|matemática
constante|cons-tan-te|sustantivo femenino|Valor que no cambia.|-|variable|La constante de proporcionalidad es 4.|matemática
expresión algebraica|ex-pre-sión al-ge-brai-ca|locución nominal|Combinación de números, letras y operaciones.|-|-|«3x + 2» es una expresión algebraica.|matemática
producto notable|pro-duc-to no-ta-ble|locución nominal|Multiplicación especial cuyo resultado se puede escribir sin desarrollarla.|-|-|El cuadrado de un binomio es un producto notable.|matemática
binomio|bi-no-mio|sustantivo masculino|Expresión algebraica de dos términos.|-|-|«x + 3» es un binomio.|matemática
función lineal|fun-ción li-ne-al|locución nominal|Función cuya gráfica es una recta que pasa por el origen.|-|-|La función lineal y = 3x pasa por el origen.|matemática
pendiente|pen-dien-te|sustantivo femenino|Número que indica cuán inclinada está una recta.|inclinación|-|La pendiente de la recta es 2.|matemática
dominio|do-mi-nio|sustantivo masculino|Conjunto de valores que puede tomar la variable de una función.|-|-|El dominio de la función son los números positivos.|matemática
recorrido|re-co-rri-do|sustantivo masculino|Conjunto de valores que toma una función.|-|-|El recorrido de la función va de 0 a 10.|matemática
plano cartesiano|pla-no car-te-sia-no|locución nominal|Plano formado por dos ejes perpendiculares para ubicar puntos.|-|-|Ubiqué el punto en el plano cartesiano.|matemática
demostración|de-mos-tra-ción|sustantivo femenino|Razonamiento que prueba que algo es verdadero.|prueba|-|La demostración usó áreas de cuadrados.|matemática
ángulo recto|án-gu-lo rec-to|locución nominal|Ángulo que mide noventa grados.|-|-|Una esquina de la hoja forma un ángulo recto.|matemática
cuerpo geométrico|cuer-po ge-o-mé-tri-co|locución nominal|Figura que ocupa un espacio en tres dimensiones.|-|-|El cubo es un cuerpo geométrico.|matemática
espacio muestral|es-pa-cio mues-tral|locución nominal|Conjunto de todos los resultados posibles de un experimento.|-|-|El espacio muestral del dado es 1, 2, 3, 4, 5 y 6.|matemática
dispersión|dis-per-sión|sustantivo femenino|Grado en que los datos se alejan unos de otros.|-|-|Hay poca dispersión en las estaturas del curso.|matemática
cuartil|cuar-til|sustantivo masculino|Cada uno de los tres valores que dividen los datos ordenados en cuatro partes iguales.|-|-|El primer cuartil deja al 25 % de los datos abajo.|matemática
notación científica|no-ta-ción cien-tí-fi-ca|locución nominal|Forma de escribir números muy grandes o muy pequeños con potencias de diez.|-|-|La distancia al Sol se escribe en notación científica.|matemática
orden de magnitud|or-den de mag-ni-tud|locución nominal|Potencia de diez más cercana a una cantidad.|-|-|El orden de magnitud de mil es tres.|matemática
núcleo celular|nú-cle-o ce-lu-lar|locución nominal|Parte de la célula que guarda el material genético.|-|-|El núcleo celular dirige las funciones de la célula.|ciencias
respiración celular|res-pi-ra-ción ce-lu-lar|locución nominal|Proceso en que las células obtienen energía de los nutrientes usando oxígeno.|-|-|La respiración celular ocurre en las mitocondrias.|ciencias
plaquetas|pla-que-tas|sustantivo femenino plural|Células de la sangre que ayudan a cerrar las heridas.|-|-|Las plaquetas forman el coágulo.|ciencias
impulso nervioso|im-pul-so ner-vio-so|locución nominal|Señal eléctrica que viaja por las neuronas.|-|-|El impulso nervioso viaja muy rápido.|ciencias
herencia genética|he-ren-cia ge-né-ti-ca|locución nominal|Transmisión de características de padres a hijos.|-|-|El color de ojos es herencia genética.|ciencias
tabaquismo|ta-ba-quis-mo|sustantivo masculino|Hábito de fumar tabaco que daña la salud.|-|-|El tabaquismo causa enfermedades del pulmón.|salud
trabajo mecánico|tra-ba-jo me-cá-ni-co|locución nominal|Energía que se transfiere cuando una fuerza mueve un cuerpo.|-|-|Subir una caja requiere trabajo mecánico.|física
energía cinética|e-ner-gí-a ci-né-ti-ca|locución nominal|Energía que tiene un cuerpo por estar en movimiento.|-|energía potencial|Una bicicleta rápida tiene mucha energía cinética.|física
energía potencial|e-ner-gí-a po-ten-cial|locución nominal|Energía almacenada por la posición o el estado de un cuerpo.|-|energía cinética|La roca en lo alto tiene energía potencial.|física
carga eléctrica|car-ga e-léc-tri-ca|locución nominal|Propiedad de la materia que produce atracción o repulsión entre cuerpos.|-|-|Frotar el globo le da carga eléctrica.|física
campo magnético|cam-po mag-né-ti-co|locución nominal|Zona alrededor de un imán donde se siente su fuerza.|-|-|La brújula reacciona al campo magnético terrestre.|física
frecuencia sonora|fre-cuen-cia so-no-ra|locución nominal|Número de vibraciones por segundo de un sonido.|-|-|Un sonido agudo tiene alta frecuencia.|física
reflexión de la luz|re-fle-xión de la luz|locución nominal|Rebote de la luz al chocar contra una superficie.|-|-|El espejo funciona por la reflexión de la luz.|física
lente|len-te|sustantivo común|Pieza de vidrio que desvía la luz para agrandar o achicar imágenes.|-|-|La lupa tiene una lente convexa.|física
protón|pro-tón|sustantivo masculino|Partícula del átomo con carga positiva.|-|electrón|El protón se encuentra en el núcleo.|química
neutrón|neu-trón|sustantivo masculino|Partícula del núcleo del átomo sin carga eléctrica.|-|-|El neutrón no tiene carga.|química
electrón|e-lec-trón|sustantivo masculino|Partícula del átomo con carga negativa que gira alrededor del núcleo.|-|protón|Los electrones giran en capas.|química
compuesto|com-pues-to|sustantivo masculino|Sustancia formada por átomos de distintos elementos.|-|-|El agua es un compuesto.|química
tabla periódica|ta-bla pe-rió-di-ca|locución nominal|Cuadro que ordena los elementos químicos según sus propiedades.|-|-|Busqué el hierro en la tabla periódica.|química
símbolo químico|sím-bo-lo quí-mi-co|locución nominal|Letra o letras con que se representa un elemento.|-|-|El símbolo químico del oro es Au.|química
solución química|so-lu-ción quí-mi-ca|locución nominal|Mezcla uniforme en que una sustancia se disuelve en otra.|disolución|-|El agua con sal es una solución química.|química
ácido|á-ci-do|sustantivo masculino|Sustancia de sabor agrio que reacciona con muchos metales.|-|base|El limón contiene ácido cítrico.|química
reacción química|re-ac-ción quí-mi-ca|locución nominal|Proceso en que unas sustancias se transforman en otras.|-|-|La combustión es una reacción química.|química
ley de conservación de la masa|ley de con-ser-va-ción de la ma-sa|locución nominal|Principio según el cual la masa total no cambia en una reacción química.|-|-|La ley de conservación de la masa se comprueba con una balanza.|química
estado de la materia|es-ta-do de la ma-te-ria|locución nominal|Forma en que se presenta la materia: sólido, líquido o gaseoso.|-|-|El hielo es el estado sólido del agua.|química
punto de fusión|pun-to de fu-sión|locución nominal|Temperatura a la que un sólido se convierte en líquido.|-|punto de ebullición|El punto de fusión del hielo es cero grados.|química
punto de ebullición|pun-to de e-bu-lli-ción|locución nominal|Temperatura a la que un líquido hierve.|-|punto de fusión|El punto de ebullición del agua es cien grados.|química
núcleo terrestre|nú-cle-o te-rres-tre|locución nominal|Centro de la Tierra, formado sobre todo por hierro.|-|-|El núcleo terrestre está a más de 5000 grados.|ciencias
placa tectónica|pla-ca tec-tó-ni-ca|locución nominal|Gran trozo de la litosfera que se mueve lentamente.|-|-|La placa de Nazca se hunde bajo Sudamérica.|ciencias
tectónica|tec-tó-ni-ca|sustantivo femenino|Estudio de los movimientos de las placas y de la forma de la corteza.|-|-|La tectónica explica por qué hay volcanes en Chile.|ciencias
roca ígnea|ro-ca íg-ne-a|locución nominal|Roca que se forma al enfriarse el magma.|-|-|El granito es una roca ígnea.|ciencias
roca sedimentaria|ro-ca se-di-men-ta-ria|locución nominal|Roca formada por capas de sedimentos acumulados.|-|-|La caliza es una roca sedimentaria.|ciencias
roca metamórfica|ro-ca me-ta-mór-fi-ca|locución nominal|Roca transformada por el calor o la presión.|-|-|El mármol es una roca metamórfica.|ciencias
atmósfera terrestre|at-mós-fe-ra te-rres-tre|locución nominal|Capa de gases que rodea la Tierra.|-|-|La atmósfera terrestre protege de la radiación.|ciencias
troposfera|tro-pos-fe-ra|sustantivo femenino|Capa más baja de la atmósfera, donde ocurre el clima.|-|-|Las nubes se forman en la troposfera.|ciencias
efecto invernadero|e-fec-to in-ver-na-de-ro|locución nominal|Retención del calor en la atmósfera por ciertos gases.|-|-|El efecto invernadero natural mantiene templada la Tierra.|ciencias
calentamiento global|ca-len-ta-mien-to glo-bal|locución nominal|Aumento sostenido de la temperatura media del planeta.|-|enfriamiento|El calentamiento global derrite los glaciares.|ciencias
cambio climático|cam-bio cli-má-ti-co|locución nominal|Variación a largo plazo del clima de la Tierra.|-|-|El cambio climático afecta las cosechas.|ciencias
presión atmosférica|pre-sión at-mos-fé-ri-ca|locución nominal|Fuerza que ejerce el aire sobre la superficie terrestre.|-|-|La presión atmosférica baja con la altura.|ciencias
anticiclón|an-ti-ci-clón|sustantivo masculino|Zona de alta presión que suele traer buen tiempo.|-|ciclón|El anticiclón del Pacífico mantiene el cielo despejado.|ciencias
frente frío|fren-te frí-o|locución nominal|Límite donde una masa de aire frío avanza sobre una de aire más cálido.|-|-|El frente frío trajo lluvia y viento.|ciencias
ciclo del agua|ci-clo del a-gua|locución nominal|Recorrido continuo del agua entre la Tierra y la atmósfera.|-|-|En el ciclo del agua participan el Sol y las nubes.|ciencias
corriente marina|co-rrien-te ma-ri-na|locución nominal|Movimiento constante de grandes masas de agua en el océano.|-|-|La corriente de Humboldt enfría la costa chilena.|ciencias
cadena alimentaria|ca-de-na a-li-men-ta-ria|locución nominal|Serie de seres vivos donde cada uno sirve de alimento al siguiente.|-|-|En la cadena alimentaria, el pasto alimenta al conejo.|ciencias
trama trófica|tra-ma tró-fi-ca|locución nominal|Red de cadenas alimentarias unidas en un ecosistema.|red alimentaria|-|La trama trófica del lago incluye peces y aves.|ciencias
población biológica|po-bla-ción bio-ló-gi-ca|locución nominal|Conjunto de seres de una misma especie que viven en un lugar.|-|-|La población de cóndores se mantiene estable.|ciencias
comunidad biológica|co-mu-ni-dad bio-ló-gi-ca|locución nominal|Conjunto de poblaciones distintas que conviven en un lugar.|-|-|El bosque alberga una comunidad biológica variada.|ciencias
nicho ecológico|ni-cho e-co-ló-gi-co|locución nominal|Papel que cumple una especie en su ecosistema.|-|-|El nicho ecológico del búho es cazar roedores de noche.|ciencias
selección natural|se-lec-ción na-tu-ral|locución nominal|Proceso por el cual sobreviven más los seres mejor adaptados.|-|-|Darwin explicó la selección natural.|ciencias
conservación ambiental|con-ser-va-ción am-bien-tal|locución nominal|Protección de la naturaleza y de sus recursos.|-|-|El parque trabaja en la conservación ambiental.|ciencias
sustentabilidad|sus-ten-ta-bi-li-dad|sustantivo femenino|Uso de los recursos sin agotarlos para las futuras generaciones.|-|-|La sustentabilidad exige consumir con responsabilidad.|ciencias
recurso renovable|re-cur-so re-no-va-ble|locución nominal|Recurso natural que se regenera con el tiempo.|-|recurso no renovable|El viento es un recurso renovable.|ciencias
combustible fósil|com-bus-ti-ble fó-sil|locución nominal|Combustible formado hace millones de años, como el petróleo.|-|-|El carbón es un combustible fósil.|ciencias
biocombustible|bio-com-bus-ti-ble|sustantivo masculino|Combustible que se obtiene de materia vegetal o de desechos.|-|-|El etanol es un biocombustible.|ciencias
energía solar|e-ner-gí-a so-lar|locución nominal|Energía que se obtiene de la luz del Sol.|-|-|El norte de Chile tiene mucha energía solar.|ciencias
energía eólica|e-ner-gí-a e-ó-li-ca|locución nominal|Energía que se obtiene del viento.|-|-|Los molinos producen energía eólica.|ciencias
energía hidráulica|e-ner-gí-a hi-dráu-li-ca|locución nominal|Energía que se obtiene de la fuerza del agua en movimiento.|-|-|La central usa energía hidráulica.|ciencias
geotérmica|ge-o-tér-mi-ca|adjetivo|Que se relaciona con el calor del interior de la Tierra.|-|-|El Tatio tiene energía geotérmica.|ciencias
huso horario|hu-so ho-ra-rio|locución nominal|Franja de la Tierra donde se usa la misma hora.|-|-|Cada huso horario difiere en una hora.|geografía
curva de nivel|cur-va de ni-vel|locución nominal|Línea que une puntos de igual altura en un mapa.|-|-|Las curvas de nivel muestran el relieve.|geografía
altitud|al-ti-tud|sustantivo femenino|Altura de un lugar sobre el nivel del mar.|elevación|-|La altitud del volcán supera los 5000 metros.|geografía
bioma|bio-ma|sustantivo masculino|Gran región con un clima y una vegetación característicos.|-|-|La tundra es un bioma frío.|geografía
urbanización|ur-ba-ni-za-ción|sustantivo femenino|Crecimiento de las ciudades y del número de personas que viven en ellas.|-|-|La urbanización ha cambiado el paisaje.|geografía
densidad de población|den-si-dad de po-bla-ción|locución nominal|Número de habitantes por kilómetro cuadrado.|-|-|La densidad de población es alta en la capital.|geografía
paleta cromática|pa-le-ta cro-má-ti-ca|locución nominal|Conjunto de colores que se usa en una obra.|-|-|La paleta cromática del mural es cálida.|artes
color complementario|co-lor com-ple-men-ta-rio|locución nominal|Color que está frente a otro en el círculo cromático y lo resalta.|-|-|El azul y el naranja son colores complementarios.|artes
intervención|in-ter-ven-ción|sustantivo femenino|Acción artística que modifica un lugar o un objeto.|-|-|La intervención cubrió la plaza de telas de colores.|artes
arte contemporáneo|ar-te con-tem-po-rá-ne-o|locución nominal|Arte que se hace en la actualidad.|-|-|El arte contemporáneo usa muchos materiales nuevos.|artes
ensayo musical|en-sa-yo mu-si-cal|locución nominal|Sesión de práctica antes de presentar una obra.|-|-|El ensayo musical empieza a las cuatro.|música
interpretación|in-ter-pre-ta-ción|sustantivo femenino|Modo de tocar, cantar o actuar una obra.|ejecución|-|Su interpretación del himno fue emotiva.|música
resistencia aeróbica|re-sis-ten-cia ae-ró-bi-ca|locución nominal|Capacidad de mantener un esfuerzo moderado durante mucho tiempo.|-|-|Trotar mejora la resistencia aeróbica.|educación física
fuerza muscular|fuer-za mus-cu-lar|locución nominal|Capacidad de los músculos para vencer una resistencia.|-|-|Las flexiones desarrollan la fuerza muscular.|educación física
frecuencia cardíaca|fre-cuen-cia car-día-ca|locución nominal|Número de latidos del corazón en un minuto.|pulso|-|Mi frecuencia cardíaca sube al correr.|educación física
sobrecarga|so-bre-car-ga|sustantivo femenino|Exceso de peso o de esfuerzo sobre el cuerpo.|-|-|La sobrecarga puede lesionar los músculos.|educación física
materiales|ma-te-ria-les|sustantivo masculino plural|Cosas de las que se hace un objeto.|-|-|Elegimos materiales resistentes.|tecnología
código fuente|có-di-go fuen-te|locución nominal|Texto con las instrucciones escritas por quien programa.|-|-|Revisé el código fuente para hallar el error.|tecnología
base de datos|ba-se de da-tos|locución nominal|Conjunto organizado de información guardada en un computador.|-|-|La biblioteca guarda sus libros en una base de datos.|tecnología
hoja de cálculo|ho-ja de cál-cu-lo|locución nominal|Programa que organiza datos en filas y columnas y hace cálculos.|-|-|Ordené las notas en una hoja de cálculo.|tecnología
copia de seguridad|co-pia de se-gu-ri-dad|locución nominal|Duplicado de archivos que se guarda por si se pierde el original.|respaldo|-|Hice una copia de seguridad de mis fotos.|tecnología
huella digital|hue-lla di-gi-tal|locución nominal|Rastro de información que dejamos al usar internet.|-|-|Pensar antes de publicar cuida tu huella digital.|tecnología
propiedad intelectual|pro-pie-dad in-te-lec-tual|locución nominal|Derecho de los autores sobre sus obras.|-|-|Citar las fuentes respeta la propiedad intelectual.|tecnología
derechos de autor|de-re-chos de au-tor|locución nominal|Conjunto de derechos legales que protegen las creaciones de una persona.|-|-|Esa canción tiene derechos de autor.|tecnología
proyecto de vida|pro-yec-to de vi-da|locución nominal|Plan personal de metas para el futuro.|-|-|Mi proyecto de vida incluye estudiar medicina.|orientación
toma de decisiones|to-ma de de-ci-sio-nes|locución nominal|Proceso de elegir entre varias opciones.|-|-|La toma de decisiones requiere pensar en las consecuencias.|orientación
presión de grupo|pre-sión de gru-po|locución nominal|Influencia de un grupo para que alguien actúe como los demás.|-|-|Resistió la presión de grupo y dijo que no.|orientación
ambiguo|am-bi-guo|adjetivo|Que puede entenderse de más de una manera.|confuso|claro|La frase era ambigua y causó dudas.|general
coherente|co-he-ren-te|adjetivo|Que mantiene una relación lógica con lo que dice o hace.|lógico|incoherente|Un texto coherente ordena bien sus ideas.|general
exhaustivo|ex-haus-ti-vo|adjetivo|Que abarca todos los aspectos de algo sin dejar nada.|completo|superficial|Hicimos un estudio exhaustivo del tema.|general
superficial|su-per-fi-cial|adjetivo|Que se queda en lo exterior y no profundiza.|ligero|profundo|El análisis fue superficial.|general
crítico|crí-ti-co|adjetivo|Que analiza con juicio y no acepta algo sin pensar.|analítico|-|Un lector crítico cuestiona lo que lee.|general
analítico|a-na-lí-ti-co|adjetivo|Que descompone algo en partes para estudiarlo.|-|-|Tiene una mente analítica.|general
trascendental|tras-cen-den-tal|adjetivo|De gran importancia y con consecuencias que van más allá.|vital|insignificante|Fue una decisión trascendental.|general
inminente|in-mi-nen-te|adjetivo|Que está a punto de ocurrir.|próximo|lejano|La tormenta es inminente.|general
imprescindible|im-pres-cin-di-ble|adjetivo|Que es absolutamente necesario.|indispensable|prescindible|El agua es imprescindible para la vida.|general
insólito|in-só-li-to|adjetivo|Raro y fuera de lo común.|extraño|habitual|Fue un hecho insólito en el pueblo.|general
unánime|u-ná-ni-me|adjetivo|Que cuenta con el acuerdo de todos.|-|dividido|La decisión fue unánime.|general
fenómeno|fe-nó-me-no|sustantivo masculino|Hecho observable de la naturaleza o de la sociedad.|suceso|-|El arcoíris es un fenómeno óptico.|general
variable de estudio|va-ria-ble de es-tu-dio|locución nominal|Característica que cambia y que se observa o mide en una investigación.|-|-|La variable de estudio era la altura de las plantas.|general
método científico|mé-to-do cien-tí-fi-co|locución nominal|Conjunto de pasos para investigar y comprobar ideas.|-|-|El método científico parte de una pregunta.|ciencias
experimento controlado|ex-pe-ri-men-to con-tro-la-do|locución nominal|Prueba en la que solo cambia una condición a la vez.|-|-|En un experimento controlado se cambia una sola variable.|ciencias
medición|me-di-ción|sustantivo femenino|Acción de determinar una magnitud con un instrumento.|-|-|La medición dio 12 centímetros.|ciencias
margen de error|mar-gen de e-rror|locución nominal|Diferencia posible entre un valor medido y el real.|-|-|La encuesta tiene un margen de error del 3 %.|ciencias
teoría|te-o-rí-a|sustantivo femenino|Conjunto de ideas comprobadas que explican un fenómeno.|-|práctica|La teoría de la evolución se apoya en evidencias.|ciencias
ley científica|ley cien-tí-fi-ca|locución nominal|Regla general que describe cómo se comporta la naturaleza.|-|-|La ley de gravedad explica por qué caen los objetos.|ciencias
al respecto|al res-pec-to|locución adverbial|Sobre el asunto del que se está hablando.|-|-|¿Qué piensas al respecto?|conectores
en cambio|en cam-bio|locución adverbial|Se usa para presentar una idea que contrasta con la anterior.|-|-|Ana es tímida; su hermano, en cambio, es muy sociable.|conectores
sin embargo|sin em-bar-go|locución conjuntiva|Se usa para oponer una idea a lo dicho antes.|no obstante|-|Hacía frío; sin embargo, salimos a caminar.|conectores
por consiguiente|por con-si-guien-te|locución conjuntiva|Se usa para indicar la consecuencia de lo dicho antes.|por lo tanto|-|No hubo quórum; por consiguiente, se suspendió la reunión.|conectores
por lo tanto|por lo tan-to|locución conjuntiva|Se usa para señalar una conclusión.|por consiguiente|-|Llovió toda la noche; por lo tanto, el río subió.|conectores
en primer lugar|en pri-mer lu-gar|locución adverbial|Se usa para empezar una lista de argumentos.|-|en último lugar|En primer lugar, quiero agradecerles.|conectores
por el contrario|por el con-tra-rio|locución adverbial|Se usa para presentar la idea opuesta a la anterior.|-|-|No me molestó; por el contrario, me alegró.|conectores
a pesar de|a pe-sar de|locución preposicional|Se usa para indicar algo que ocurre aunque exista un obstáculo.|pese a|-|A pesar de la lluvia, jugamos.|conectores
dado que|da-do que|locución conjuntiva|Se usa para dar la razón de lo que se dice.|puesto que|-|Dado que no hay clases, salimos temprano.|conectores
mientras tanto|mien-tras tan-to|locución adverbial|Durante el tiempo en que algo ocurre.|-|-|Hierve el agua; mientras tanto, corto las verduras.|conectores
es decir|es de-cir|locución conjuntiva|Se usa para explicar algo con otras palabras.|o sea|-|Soy bilingüe, es decir, hablo dos idiomas.|conectores
por ejemplo|por e-jem-plo|locución adverbial|Se usa para presentar un caso que aclara lo dicho.|-|-|Hay mamíferos acuáticos, por ejemplo, la ballena.|conectores
a diferencia de|a di-fe-ren-cia de|locución preposicional|Se usa para comparar mostrando lo que distingue a dos cosas.|-|-|A diferencia de mi hermano, yo prefiero el invierno.|conectores
gracias a|gra-cias a|locución preposicional|Se usa para indicar la causa de algo favorable.|-|-|Gracias a su ayuda, terminé a tiempo.|conectores
debido a|de-bi-do a|locución preposicional|Se usa para indicar la causa de algo.|-|-|El vuelo se retrasó debido a la niebla.|conectores
en torno a|en tor-no a|locución preposicional|Se usa para indicar el tema sobre el que gira algo.|-|-|El debate giró en torno a la seguridad vial.|conectores
si no|si no|locución conjuntiva|Se usa para plantear una condición negativa.|-|-|Si no estudias, no aprobarás.|ortografía
por qué|por qué|locución adverbial|Se usa para preguntar la causa de algo.|-|-|¿Por qué llegaste tarde?|ortografía
porqué|por-qué|sustantivo masculino|Causa o razón de algo.|motivo|-|No entiendo el porqué de tu enojo.|ortografía
con qué|con qué|locución pronominal|Se usa para preguntar el medio o instrumento.|-|-|¿Con qué cortaste el papel?|ortografía
conque|con-que|conjunción|Se usa para introducir una consecuencia o una pregunta de sorpresa.|-|-|Conque te quedas, ¿no?|ortografía
a ver|a ver|locución verbal|Expresión para pedir que se muestre o se compruebe algo.|-|-|A ver, muéstrame tu dibujo.|ortografía
nunca jamás|nun-ca ja-más|locución adverbial|De ninguna manera y en ningún momento.|-|siempre|Nunca jamás volveré a olvidarlo.|general
a menudo|a me-nu-do|locución adverbial|Con frecuencia.|frecuentemente|raramente|A menudo leo antes de dormir.|general
de antemano|de an-te-ma-no|locución adverbial|Con anticipación.|-|-|Te agradezco de antemano tu ayuda.|general
en vano|en va-no|locución adverbial|Sin lograr resultado.|-|-|Intenté en vano abrir la puerta.|general
por lo general|por lo ge-ne-ral|locución adverbial|En la mayoría de los casos.|generalmente|-|Por lo general, me levanto a las siete.|general
tarde o temprano|tar-de o tem-pra-no|locución adverbial|En algún momento, sin importar cuándo.|-|-|Tarde o temprano, la verdad se sabe.|general
cuesta arriba|cues-ta a-rri-ba|locución adverbial|Con dificultad, como subir una pendiente.|-|-|El comienzo del año se me hizo cuesta arriba.|general
meter la pata|me-ter la pa-ta|locución verbal|Cometer un error sin querer.|equivocarse|acertar|Metí la pata al decir ese secreto.|general
tirar la toalla|ti-rar la to-a-lla|locución verbal|Rendirse ante una dificultad.|rendirse|perseverar|No tires la toalla ahora.|general
estar en las nubes|es-tar en las nu-bes|locución verbal|Estar distraído, sin atender a lo que ocurre.|distraerse|-|En clase estaba en las nubes.|general
dar en el clavo|dar en el cla-vo|locución verbal|Acertar en lo que se dice o se hace.|acertar|-|Diste en el clavo con tu respuesta.|general
echar una mano|e-char u-na ma-no|locución verbal|Ayudar a alguien.|ayudar|-|¿Me echas una mano con la mochila?|general
tener buena onda|te-ner bue-na on-da|locución verbal|Ser agradable y de trato simpático (uso en Chile).|-|-|Mi profesor tiene buena onda.|general
Edad Moderna|E-dad Mo-der-na|locución nominal|Período de la historia entre fines del siglo XV y fines del siglo XVIII.|-|-|En la Edad Moderna Europa llegó a América.|historia
erudito|e-ru-di-to|sustantivo masculino|Persona que sabe mucho porque ha estudiado a fondo.|sabio|ignorante|El erudito conocía varios idiomas.|historia
inquisición|in-qui-si-ción|sustantivo femenino|Tribunal de la Iglesia que perseguía a quienes se creía que se apartaban de la fe.|-|-|La Inquisición juzgó a muchos pensadores.|historia
indulgencia|in-dul-gen-cia|sustantivo femenino|Perdón de los pecados que la Iglesia concedía, a veces a cambio de dinero en la época de Lutero.|-|-|Lutero criticó la venta de indulgencias.|historia
concilio|con-ci-lio|sustantivo masculino|Reunión de líderes de la Iglesia para tomar decisiones.|asamblea|-|El Concilio de Trento respondió a la Reforma.|historia
contrarreforma|con-tra-rre-for-ma|sustantivo femenino|Reacción de la Iglesia católica ante la Reforma protestante.|-|-|La Contrarreforma impulsó nuevas órdenes religiosas.|historia
jesuita|je-sui-ta|sustantivo masculino|Miembro de la Compañía de Jesús, orden religiosa dedicada a la enseñanza y las misiones.|-|-|Los jesuitas fundaron colegios en América.|historia
barroco|ba-rro-co|adjetivo|Se dice del estilo artístico del siglo XVII, muy adornado y dramático.|recargado|sobrio|La iglesia barroca tiene un altar dorado.|historia
mercader|mer-ca-der|sustantivo masculino|Persona que compra y vende mercaderías.|comerciante|-|El mercader llegó con telas de Oriente.|historia
gremio|gre-mio|sustantivo masculino|Asociación de artesanos de un mismo oficio.|-|-|El gremio de zapateros fijaba los precios.|historia
manuscrito|ma-nus-cri-to|sustantivo masculino|Texto escrito a mano.|-|impreso|El monje copió el manuscrito durante meses.|historia
pergamino|per-ga-mi-no|sustantivo masculino|Piel de animal preparada para escribir sobre ella.|-|-|El pergamino conservó el texto por siglos.|historia
globo terráqueo|glo-bo te-rrá-que-o|locución nominal|Esfera que representa la forma de la Tierra.|-|-|Giré el globo terráqueo para ubicar Chile.|historia
capitulación|ca-pi-tu-la-ción|sustantivo femenino|Contrato entre el rey y un conquistador que fijaba sus derechos y deberes.|-|-|Valdivia recibió una capitulación del rey.|historia
adelantado|a-de-lan-ta-do|sustantivo masculino|Jefe de una expedición que gobernaba lo que conquistaba.|-|-|El adelantado fundó una ciudad en la selva.|historia
hueste|hues-te|sustantivo femenino|Grupo de soldados que acompañaba a un jefe.|ejército|-|La hueste cruzó la cordillera.|historia
arcabuz|ar-ca-buz|sustantivo masculino|Arma de fuego antigua que se cargaba por la boca.|-|-|Los españoles disparaban con arcabuces.|historia
pólvora|pól-vo-ra|sustantivo femenino|Mezcla que explota y que se usa en armas y fuegos artificiales.|-|-|La pólvora cambió la manera de hacer la guerra.|historia
armadura|ar-ma-du-ra|sustantivo femenino|Vestimenta de metal que protegía a los guerreros.|coraza|-|La armadura pesaba más de veinte kilos.|historia
choque cultural|cho-que cul-tu-ral|locución nominal|Conflicto o desconcierto cuando se encuentran culturas muy distintas.|-|-|El choque cultural fue enorme tras la llegada de los españoles.|historia
sincretismo|sin-cre-tis-mo|sustantivo masculino|Mezcla de creencias o costumbres de culturas diferentes.|fusión|-|El sincretismo se ve en las fiestas religiosas populares.|historia
toqui|to-qui|sustantivo masculino|Jefe militar mapuche elegido en tiempos de guerra.|-|-|Lautaro fue un toqui.|historia
reducción|re-duc-ción|sustantivo femenino|Pueblo donde se reunía a los indígenas para evangelizarlos.|-|-|Los jesuitas fundaron reducciones en Paraguay.|historia
corregidor|co-rre-gi-dor|sustantivo masculino|Funcionario colonial que gobernaba una ciudad o un distrito.|-|-|El corregidor cobraba los impuestos de la zona.|historia
real hacienda|real ha-cien-da|locución nominal|Dinero y bienes que pertenecían al rey.|-|-|La Real Hacienda recibía el quinto de la plata.|historia
quinto real|quin-to real|locución nominal|Impuesto que consistía en la quinta parte de lo extraído de las minas.|-|-|El quinto real se pagaba al rey.|historia
inquilino|in-qui-li-no|sustantivo masculino|En Chile colonial, campesino que trabajaba en una hacienda a cambio de un pedazo de tierra.|-|-|Los inquilinos vivían en la hacienda.|historia
peón|pe-ón|sustantivo masculino|Trabajador del campo o de la construcción que realiza labores simples.|obrero|-|El peón cuidaba los animales de la estancia.|historia
mulato|mu-la-to|sustantivo masculino|Persona hija de padre africano y madre europea, o al revés.|-|-|Los mulatos formaban parte de la sociedad colonial.|historia
contrabando|con-tra-ban-do|sustantivo masculino|Comercio ilegal de mercaderías.|-|-|El contrabando evitaba los impuestos.|historia
corsario|cor-sa-rio|sustantivo masculino|Navegante autorizado por un gobierno para atacar barcos enemigos.|-|-|El corsario Drake atacó puertos del Pacífico.|historia
pirata|pi-ra-ta|sustantivo común|Ladrón que asalta barcos en el mar.|bucanero|-|Los piratas saquearon el puerto.|historia
galeón|ga-le-ón|sustantivo masculino|Gran barco de vela usado para el comercio y la guerra entre los siglos XVI y XVIII.|-|-|El galeón venía cargado de plata.|historia
cofradía|co-fra-dí-a|sustantivo femenino|Asociación de personas que se reúnen por devoción religiosa.|hermandad|-|La cofradía organizó la procesión.|historia
retablo|re-ta-blo|sustantivo masculino|Estructura decorada con imágenes que está detrás de un altar.|-|-|El retablo dorado ocupa todo el muro.|historia
poder ejecutivo|po-der e-je-cu-ti-vo|locución nominal|Poder del Estado que gobierna y administra el país.|-|-|El presidente encabeza el poder ejecutivo.|educación cívica
poder legislativo|po-der le-gis-la-ti-vo|locución nominal|Poder del Estado que crea las leyes.|-|-|El Congreso forma el poder legislativo.|educación cívica
poder judicial|po-der ju-di-cial|locución nominal|Poder del Estado que aplica las leyes y resuelve los conflictos.|-|-|Los tribunales forman el poder judicial.|educación cívica
participación|par-ti-ci-pa-ción|sustantivo femenino|Acción de formar parte de algo y contribuir.|-|-|La participación del curso fue alta.|educación cívica
derechos humanos|de-re-chos hu-ma-nos|locución nominal|Derechos que tiene toda persona por el hecho de serlo.|-|-|Los derechos humanos protegen la dignidad.|educación cívica
libertad de expresión|li-ber-tad de ex-pre-sión|locución nominal|Derecho a manifestar las propias ideas sin censura.|-|-|La libertad de expresión protege a los periodistas.|educación cívica
bien común|bien co-mún|locución nominal|Beneficio que busca el conjunto de la sociedad.|-|-|Las leyes buscan el bien común.|educación cívica
demanda|de-man-da|sustantivo femenino|Cantidad de bienes que la gente quiere comprar.|-|oferta|La demanda de paraguas sube en invierno.|economía
salario|sa-la-rio|sustantivo masculino|Dinero que recibe una persona por su trabajo.|sueldo|-|El salario mínimo subió este año.|economía
inversión|in-ver-sión|sustantivo femenino|Uso del dinero para obtener ganancias en el futuro.|-|-|La inversión en educación mejora el país.|economía
empresa|em-pre-sa|sustantivo femenino|Organización que produce bienes o servicios para ganar dinero.|compañía|-|La empresa contrató a diez personas.|economía
emprendedor|em-pren-de-dor|sustantivo masculino|Persona que crea un negocio o proyecto nuevo.|-|-|La emprendedora abrió una panadería.|economía
exportación|ex-por-ta-ción|sustantivo femenino|Venta de productos a otro país.|-|importación|El cobre es la principal exportación de Chile.|economía
importación|im-por-ta-ción|sustantivo femenino|Compra de productos a otro país.|-|exportación|La importación de autos creció.|economía
arancel|a-ran-cel|sustantivo masculino|Impuesto que se cobra por los productos que entran a un país.|-|-|El arancel encareció los zapatos importados.|economía
globalización|glo-ba-li-za-ción|sustantivo femenino|Proceso por el que los países se conectan cada vez más en economía y cultura.|-|-|La globalización acerca mercados lejanos.|economía
pobreza|po-bre-za|sustantivo femenino|Situación de quien no tiene lo necesario para vivir con dignidad.|escasez|riqueza|Un programa busca reducir la pobreza.|economía
turismo|tu-ris-mo|sustantivo masculino|Actividad de viajar por placer y servicios relacionados.|-|-|El turismo crece en Torres del Paine.|economía
agroindustria|a-gro-in-dus-tria|sustantivo femenino|Industria que procesa productos del campo.|-|-|La agroindustria exporta fruta.|economía
sereno|se-re-no|adjetivo|Tranquilo, sin nervios ni agitación.|calmado|nervioso|Se mantuvo sereno durante la emergencia.|carácter
vehemente|ve-he-men-te|adjetivo|Que expresa sus ideas con mucha fuerza y pasión.|apasionado|apático|Defendió su idea de forma vehemente.|carácter
lúcido|lú-ci-do|adjetivo|Que piensa con claridad y entiende bien las cosas.|claro|confuso|Aunque estaba cansado, tuvo una idea lúcida.|carácter
meticuloso|me-ti-cu-lo-so|adjetivo|Que cuida hasta el último detalle.|minucioso|descuidado|Es meticuloso al armar maquetas.|carácter
perspicaz|pers-pi-caz|adjetivo|Que se da cuenta rápido de detalles que otros no ven.|agudo|torpe|Una lectora perspicaz notó la pista.|carácter
escéptico|es-cép-ti-co|adjetivo|Que duda de lo que no está probado.|incrédulo|crédulo|Fue escéptico ante la promesa.|carácter
indignado|in-dig-na-do|adjetivo|Muy enojado por algo que parece injusto.|ofendido|conforme|Se sintió indignado por el trato.|emociones
desolado|de-so-la-do|adjetivo|Muy triste y sin consuelo.|afligido|alegre|Quedó desolado al perder su mascota.|emociones
eufórico|eu-fó-ri-co|adjetivo|Muy alegre y lleno de entusiasmo.|exultante|abatido|Los hinchas estaban eufóricos tras el gol.|emociones
nostálgico|nos-tál-gi-co|adjetivo|Que siente tristeza dulce al recordar el pasado.|añorante|-|Se puso nostálgico al ver las fotos antiguas.|emociones
melancólico|me-lan-có-li-co|adjetivo|Que siente una tristeza suave y duradera.|taciturno|jovial|La música lo dejó melancólico.|emociones
abatido|a-ba-ti-do|adjetivo|Sin ánimo, decaído.|desanimado|animado|Estaba abatido tras la derrota.|emociones
rencoroso|ren-co-ro-so|adjetivo|Que guarda resentimiento por mucho tiempo.|resentido|perdonador|Una persona rencorosa tarda en perdonar.|emociones
altruista|al-truis-ta|adjetivo|Que ayuda a los demás sin esperar nada a cambio.|generoso|egoísta|Es altruista y participa de colectas.|carácter
mezquino|mez-qui-no|adjetivo|Que da poco o actúa con mala voluntad.|tacaño|generoso|Fue mezquino con sus elogios.|carácter
hipócrita|hi-pó-cri-ta|adjetivo|Que finge sentimientos o virtudes que no tiene.|falso|sincero|Es hipócrita elogiar a alguien y luego criticarlo.|carácter
discreto|dis-cre-to|adjetivo|Que sabe guardar secretos y actuar sin llamar la atención.|reservado|indiscreto|Mi amigo es discreto y no cuenta nada.|carácter
austero|aus-te-ro|adjetivo|Que vive con sencillez y sin lujos.|sobrio|derrochador|Llevaba una vida austera.|carácter
derrochador|de-rro-cha-dor|adjetivo|Que gasta de forma excesiva.|despilfarrador|ahorrativo|Es derrochador con el agua.|carácter
avaro|a-va-ro|adjetivo|Que acumula dinero y no quiere gastar.|tacaño|generoso|El avaro contaba sus monedas cada noche.|carácter
diligente|di-li-gen-te|adjetivo|Rápido y cuidadoso al hacer su trabajo.|aplicado|perezoso|Una estudiante diligente entrega a tiempo.|carácter
taciturno|ta-ci-tur-no|adjetivo|Callado y de ánimo apagado.|callado|conversador|Su hermano es taciturno y habla poco.|carácter
locuaz|lo-cuaz|adjetivo|Que habla mucho.|hablador|callado|Un guía locuaz entretuvo al grupo.|carácter
conciso|con-ci-so|adjetivo|Que expresa mucho con pocas palabras.|breve|extenso|Su respuesta fue concisa.|lenguaje
prolijo|pro-li-jo|adjetivo|En Chile, ordenado y cuidadoso; también, muy largo y detallado.|ordenado|desordenado|Su cuaderno es muy prolijo (uso en Chile).|carácter
minucioso|mi-nu-cio-so|adjetivo|Que cuida hasta los detalles más pequeños.|meticuloso|descuidado|Hizo un trabajo minucioso.|carácter
arduo|ar-duo|adjetivo|Muy difícil y que exige gran esfuerzo.|difícil|fácil|Fue una tarea ardua.|general
fugaz|fu-gaz|adjetivo|Que dura muy poco tiempo.|breve|duradero|Vimos una estrella fugaz.|general
perenne|pe-ren-ne|adjetivo|Que dura todo el año o para siempre.|eterno|efímero|El peumo es un árbol de hoja perenne.|general
latente|la-ten-te|adjetivo|Que existe, pero todavía no se manifiesta.|oculto|manifiesto|El conflicto seguía latente.|general
palpable|pal-pa-ble|adjetivo|Que se nota con mucha claridad.|evidente|imperceptible|La tensión era palpable.|general
tangible|tan-gi-ble|adjetivo|Que se puede tocar o percibir con claridad.|material|intangible|Obtuvo un resultado tangible.|general
ineludible|i-ne-lu-di-ble|adjetivo|Que no se puede evitar.|inevitable|evitable|Era un deber ineludible.|general
utópico|u-tó-pi-co|adjetivo|Que parece ideal pero imposible de lograr.|idealista|realista|Un mundo sin conflictos suena utópico.|general
sublime|su-bli-me|adjetivo|De una belleza o grandeza extraordinaria.|excelso|vulgar|La vista desde la cumbre era sublime.|general
grotesco|gro-tes-co|adjetivo|Raro y exagerado, de forma que parece ridículo o feo.|esperpéntico|armonioso|El disfraz tenía un aspecto grotesco.|general
absurdo|ab-sur-do|adjetivo|Que va contra la razón o no tiene sentido.|disparatado|lógico|Fue una idea absurda.|general
ridículo|ri-dí-cu-lo|adjetivo|Que da risa o vergüenza por ser extraño o exagerado.|risible|serio|Se puso un sombrero ridículo.|general
verídico|ve-rí-di-co|adjetivo|Que dice la verdad.|veraz|falso|El relato es verídico.|general
ficticio|fic-ti-cio|adjetivo|Inventado, que no existe en la realidad.|imaginario|real|Pedro Urdemales es un personaje ficticio.|general
anónimo|a-nó-ni-mo|adjetivo|De autor desconocido o que no da su nombre.|-|firmado|El poema era anónimo.|general
notorio|no-to-rio|adjetivo|Que se nota mucho o es muy conocido.|evidente|discreto|Hubo una mejora notoria.|general
ínfimo|ín-fi-mo|adjetivo|Muy pequeño o de muy poca importancia.|minúsculo|enorme|El precio era ínfimo.|general
colosal|co-lo-sal|adjetivo|De tamaño o importancia enormes.|gigantesco|diminuto|Un colosal glaciar cerraba el fiordo.|general
gélido|gé-li-do|adjetivo|Muy frío, como el hielo.|helado|ardiente|Soplaba un viento gélido.|general
tórrido|tó-rri-do|adjetivo|Muy caliente y seco.|abrasador|gélido|El verano fue tórrido.|general
lúgubre|lú-gu-bre|adjetivo|Triste, oscuro y que da miedo.|sombrío|alegre|La casa abandonada era lúgubre.|general
sombrío|som-brí-o|adjetivo|Oscuro o triste.|tenebroso|luminoso|El día sombrío invitaba a quedarse adentro.|general
radiante|ra-dian-te|adjetivo|Que brilla o se ve muy feliz.|resplandeciente|apagado|Llegó radiante con su diploma.|general
nítido|ní-ti-do|adjetivo|Claro, sin confusión ni borrones.|claro|borroso|La foto quedó nítida.|general
borroso|bo-rro-so|adjetivo|Que no se ve con claridad.|difuso|nítido|La imagen estaba borrosa.|general
viscoso|vis-co-so|adjetivo|Espeso y pegajoso, como el aceite.|pegajoso|fluido|La miel es un líquido viscoso.|general
maleable|ma-le-a-ble|adjetivo|Que se puede moldear fácilmente.|dúctil|rígido|El oro es un metal maleable.|general
perecedero|pe-re-ce-de-ro|adjetivo|Que dura poco tiempo antes de echarse a perder.|-|duradero|La fruta es un alimento perecedero.|general
volátil|vo-lá-til|adjetivo|Que se evapora con rapidez.|-|estable|El alcohol es un líquido volátil.|ciencias
estable|es-ta-ble|adjetivo|Que no cambia con facilidad.|firme|inestable|El clima de la zona es estable.|general
precario|pre-ca-rio|adjetivo|Que tiene pocos recursos o poca seguridad.|inseguro|seguro|Vivían en condiciones precarias.|general
próspero|prós-pe-ro|adjetivo|Que tiene éxito y buena situación económica.|floreciente|decadente|La ciudad se volvió próspera.|general
decadente|de-ca-den-te|adjetivo|Que va perdiendo fuerza o calidad.|declinante|próspero|El teatro se veía decadente.|general
pericia|pe-ri-cia|sustantivo femenino|Gran experiencia y habilidad para una actividad.|maestría|-|La pilota condujo con pericia.|general
proeza|pro-e-za|sustantivo femenino|Acción difícil y valiente.|hazaña|-|Cruzar la cordillera fue una proeza.|general
anhelo|an-he-lo|sustantivo masculino|Deseo muy fuerte de lograr algo.|ansia|-|Su anhelo es viajar al espacio.|emociones
añoranza|a-ño-ran-za|sustantivo femenino|Tristeza por recordar algo o a alguien que está lejos.|nostalgia|-|Sintió añoranza de su pueblo.|emociones
euforia|eu-fo-ria|sustantivo femenino|Alegría intensa y muy visible.|júbilo|abatimiento|La euforia invadió el estadio.|emociones
indignación|in-dig-na-ción|sustantivo femenino|Enojo fuerte ante una injusticia.|enojo|-|Su indignación fue evidente.|emociones
desdén|des-dén|sustantivo masculino|Desprecio por algo o alguien que se considera inferior.|desprecio|aprecio|Contestó con desdén.|emociones
rencor|ren-cor|sustantivo masculino|Resentimiento que se guarda por una ofensa.|resentimiento|perdón|No guardes rencor.|emociones
empeño|em-pe-ño|sustantivo masculino|Esfuerzo constante por conseguir algo.|afán|desgano|Puso empeño en su proyecto.|emociones
tesón|te-són|sustantivo masculino|Firmeza para no rendirse ante las dificultades.|constancia|abandono|Con tesón terminó la maratón.|emociones
vigor|vi-gor|sustantivo masculino|Fuerza y energía.|vitalidad|debilidad|Corrió con vigor hasta la meta.|emociones
fragilidad|fra-gi-li-dad|sustantivo femenino|Cualidad de lo que se rompe o se daña con facilidad.|debilidad|resistencia|La fragilidad del cristal exige cuidado.|general
atributo|a-tri-bu-to|sustantivo masculino|Cualidad propia de alguien o de algo.|cualidad|-|La paciencia es un atributo valioso.|general
indicio|in-di-cio|sustantivo masculino|Señal que permite sospechar algo.|señal|-|Hallaron un indicio del robo.|general
rastro|ras-tro|sustantivo masculino|Señal que deja algo o alguien al pasar.|huella|-|Seguimos el rastro del zorro.|general
pretexto|pre-tex-to|sustantivo masculino|Excusa falsa que se da para no hacer algo.|excusa|-|Usó la lluvia como pretexto.|general
malentendido|ma-len-ten-di-do|sustantivo masculino|Error al interpretar lo que alguien quiso decir.|equívoco|-|Fue un malentendido y ya se aclaró.|general
altercado|al-ter-ca-do|sustantivo masculino|Discusión fuerte y acalorada.|riña|-|Hubo un altercado en la fila.|general
disputa|dis-pu-ta|sustantivo femenino|Discusión intensa entre personas con opiniones opuestas.|pelea|acuerdo|La disputa terminó en reconciliación.|general
alegato|a-le-ga-to|sustantivo masculino|Discurso en que se defiende un derecho o una postura.|defensa|-|El abogado presentó un alegato.|general
súplica|sú-pli-ca|sustantivo femenino|Petición humilde y con mucha emoción.|ruego|-|Su súplica conmovió a todos.|general
tregua|tre-gua|sustantivo femenino|Pausa en una pelea o guerra.|pausa|-|Los equipos pactaron una tregua.|general
hostilidad|hos-ti-li-dad|sustantivo femenino|Actitud agresiva o de enemistad hacia alguien.|enemistad|amistad|Sintió hostilidad en el ambiente.|general
contratiempo|con-tra-tiem-po|sustantivo masculino|Hecho inesperado que impide o retrasa algo.|imprevisto|-|Tuvimos un contratiempo con el bus.|general
obstáculo|obs-tá-cu-lo|sustantivo masculino|Cosa que impide o dificulta el paso o el logro.|impedimento|facilidad|La falta de tiempo fue un obstáculo.|general
umbral|um-bral|sustantivo masculino|Parte de abajo de una puerta o primer paso de algo.|entrada|-|Se detuvo en el umbral de la puerta.|general
cúspide|cús-pi-de|sustantivo femenino|Punto más alto de algo.|cima|base|Llegaron a la cúspide del cerro.|general
abismo|a-bis-mo|sustantivo masculino|Precipicio muy profundo o gran diferencia entre dos cosas.|precipicio|-|Un abismo separaba ambas opiniones.|general
vértigo|vér-ti-go|sustantivo masculino|Sensación de mareo al mirar desde una altura.|mareo|-|Sentí vértigo en el mirador.|general
rumbo|rum-bo|sustantivo masculino|Dirección que se sigue.|dirección|-|El barco cambió de rumbo.|general
travesía|tra-ve-sí-a|sustantivo femenino|Viaje largo por mar o por tierra.|viaje|-|La travesía duró tres semanas.|general
periplo|pe-ri-plo|sustantivo masculino|Viaje largo con muchas escalas.|travesía|-|Su periplo incluyó cuatro países.|general
sobre todo|so-bre to-do|locución adverbial|Especialmente, ante todo.|principalmente|-|Me gusta el deporte, sobre todo el fútbol.|general
en absoluto|en ab-so-lu-to|locución adverbial|De ningún modo.|-|completamente|No me molesta en absoluto.|general
por supuesto|por su-pues-to|locución adverbial|Claro que sí.|desde luego|-|—¿Vienes? —Por supuesto.|general
aparentemente|a-pa-ren-te-men-te|adverbio|Según parece, aunque puede no ser así.|-|-|Aparentemente no hubo heridos.|general
supuestamente|su-pues-ta-men-te|adverbio|Según se dice, pero sin estar comprobado.|presuntamente|-|Supuestamente el partido se suspendió.|general
lamentablemente|la-men-ta-ble-men-te|adverbio|De manera que causa pena.|desgraciadamente|afortunadamente|Lamentablemente se canceló el paseo.|general
afortunadamente|a-for-tu-na-da-men-te|adverbio|Por buena suerte.|por suerte|lamentablemente|Afortunadamente no llovió.|general
últimamente|úl-ti-ma-men-te|adverbio|En los días más recientes.|recientemente|-|Últimamente leo más.|general
al instante|al ins-tan-te|locución adverbial|Sin esperar nada.|inmediatamente|-|Respondió al instante.|general
de golpe|de gol-pe|locución adverbial|Bruscamente, de una vez.|-|-|Se abrió la puerta de golpe.|general
otra vez|o-tra vez|locución adverbial|Una vez más.|de nuevo|-|Lee otra vez el enunciado.|general
a toda costa|a to-da cos-ta|locución adverbial|Sin importar el esfuerzo necesario.|-|-|Quiso ganar a toda costa.|general
al pie de la letra|al pie de la le-tra|locución adverbial|Exactamente, sin cambiar nada.|-|-|Siguió las instrucciones al pie de la letra.|general
a ojos vistas|a o-jos vis-tas|locución adverbial|De manera evidente, a la vista de todos.|-|-|El río crece a ojos vistas.|general
de buena fe|de bue-na fe|locución adverbial|Con buena intención y honestidad.|-|-|Actuó de buena fe.|general
dar por sentado|dar por sen-ta-do|locución verbal|Suponer que algo es cierto sin comprobarlo.|-|-|No des por sentado que sabrán la respuesta.|general
hacer oídos sordos|ha-cer o-í-dos sor-dos|locución verbal|No escuchar o no hacer caso de algo.|-|-|Hizo oídos sordos a los consejos.|general
tomar el pelo|to-mar el pe-lo|locución verbal|Burlarse de alguien con engaños.|-|-|Me tomaron el pelo con esa noticia falsa.|general
pan comido|pan co-mi-do|locución nominal|Algo muy fácil de hacer.|-|-|El examen fue pan comido.|general
llover a cántaros|llo-ver a cán-ta-ros|locución verbal|Llover con mucha fuerza.|-|-|Anoche llovió a cántaros.|general
poner el grito en el cielo|po-ner el gri-to en el cie-lo|locución verbal|Protestar con mucha fuerza.|-|-|Puso el grito en el cielo al ver su nota.|general
ponerse las pilas|po-ner-se las pi-las|locución verbal|Esforzarse y actuar con energía (uso en Chile y otros países).|-|-|Tengo que ponerme las pilas con Matemática.|general
estar a la altura|es-tar a la al-tu-ra|locución verbal|Tener la calidad necesaria para algo.|-|-|El equipo estuvo a la altura del desafío.|general
taco|ta-co|sustantivo masculino|En Chile, atochamiento de autos.|atasco|-|Hay un taco enorme en la autopista (uso en Chile).|vida cotidiana
carrete|ca-rre-te|sustantivo masculino|En Chile, fiesta o salida para pasarlo bien.|fiesta|-|Fuimos a un carrete en casa de un amigo (uso en Chile).|vida cotidiana
luca|lu-ca|sustantivo femenino|En Chile, mil pesos.|-|-|El helado costó dos lucas (uso en Chile).|vida cotidiana
pololo|po-lo-lo|sustantivo masculino|En Chile, persona con quien se mantiene una relación de pareja.|novio|-|Su pololo la espera afuera (uso en Chile).|vida cotidiana
quiltro|quil-tro|sustantivo masculino|En Chile, perro mestizo.|-|-|El quiltro nos siguió hasta la casa (uso en Chile).|vida cotidiana
pituto|pi-tu-to|sustantivo masculino|En Chile, recomendación o contacto para obtener algo.|recomendación|-|Consiguió el trabajo por pituto (uso en Chile).|vida cotidiana
boldo|bol-do|sustantivo masculino|Árbol chileno cuyas hojas se usan en infusiones.|-|-|Tomé té de boldo después de almuerzo.|naturaleza
tundra|tun-dra|sustantivo femenino|Terreno frío donde el suelo permanece helado y solo crecen musgos y líquenes.|-|-|En la tundra casi no hay árboles.|naturaleza
sabana|sa-ba-na|sustantivo femenino|Llanura tropical con pastos y árboles aislados.|-|-|En la sabana africana viven leones y jirafas.|naturaleza
arrecife|a-rre-ci-fe|sustantivo masculino|Roca o formación de coral cercana a la superficie del mar.|-|-|El arrecife protege la costa del oleaje.|naturaleza
estuario|es-tua-rio|sustantivo masculino|Desembocadura de un río ancha y con mareas.|-|-|El estuario recibe agua dulce y salada.|geografía
manantial|ma-nan-tial|sustantivo masculino|Lugar donde brota agua de la tierra.|vertiente|-|El manantial surtía al pueblo.|geografía
catarata|ca-ta-ra-ta|sustantivo femenino|Caída grande de agua desde mucha altura.|cascada|-|Las cataratas del Iguazú son impresionantes.|geografía
meandro|me-an-dro|sustantivo masculino|Curva pronunciada de un río.|-|-|El río forma un meandro en la llanura.|geografía
cauce|cau-ce|sustantivo masculino|Lecho por donde corre un río.|-|-|El cauce se secó durante el verano.|geografía
caudal|cau-dal|sustantivo masculino|Cantidad de agua que lleva un río.|-|-|El caudal aumenta con el deshielo.|geografía
avalancha|a-va-lan-cha|sustantivo femenino|Gran masa de nieve o de rocas que cae por una ladera.|alud|-|La avalancha cerró el paso fronterizo.|geografía
marejada|ma-re-ja-da|sustantivo femenino|Oleaje fuerte del mar.|oleaje|-|La marejada obligó a cerrar el puerto.|geografía
húmero|hú-me-ro|sustantivo masculino|Hueso largo del brazo.|-|-|El húmero va del hombro al codo.|cuerpo
clavícula|cla-ví-cu-la|sustantivo femenino|Hueso que une el esternón con el hombro.|-|-|Se quebró la clavícula jugando fútbol.|cuerpo
ligamento|li-ga-men-to|sustantivo masculino|Tejido que une huesos entre sí en una articulación.|-|-|Se rompió un ligamento de la rodilla.|cuerpo
retina|re-ti-na|sustantivo femenino|Capa del ojo que recibe la luz y forma las imágenes.|-|-|La imagen se forma en la retina.|cuerpo
pupila|pu-pi-la|sustantivo femenino|Círculo negro en el centro del ojo que deja entrar la luz.|-|-|La pupila se achica con la luz fuerte.|cuerpo
tímpano|tím-pa-no|sustantivo masculino|Membrana del oído que vibra con los sonidos.|-|-|El tímpano transmite el sonido al oído interno.|cuerpo
epidermis|e-pi-der-mis|sustantivo femenino|Capa más externa de la piel.|-|-|La epidermis protege de los microbios.|cuerpo
exquisito|ex-qui-si-to|adjetivo|De sabor o calidad excelentes.|delicioso|repugnante|El pastel de manjar estaba exquisito.|ortografía
exuberante|e-xu-be-ran-te|adjetivo|Muy abundante y lleno de vida.|frondoso|escaso|La selva es exuberante.|ortografía
exhausto|ex-haus-to|adjetivo|Sin fuerzas, muy cansado.|agotado|vigoroso|Llegó exhausto a la meta.|ortografía
inmóvil|in-mó-vil|adjetivo|Que no se mueve.|quieto|móvil|El gato permaneció inmóvil.|ortografía
ilusión|i-lu-sión|sustantivo femenino|Esperanza alegre de que algo ocurra, o imagen engañosa de los sentidos.|esperanza|desilusión|Tiene ilusión por el viaje.|ortografía
obsequio|ob-se-quio|sustantivo masculino|Regalo que se da a alguien.|regalo|-|Le entregaron un obsequio.|ortografía
subvención|sub-ven-ción|sustantivo femenino|Ayuda en dinero que da el Estado a una actividad.|subsidio|-|La escuela recibe una subvención.|ortografía
vehículo|ve-hí-cu-lo|sustantivo masculino|Medio de transporte que se mueve con motor o a tracción.|-|-|Un vehículo bloqueaba el paso.|ortografía
ambigüedad|am-bi-güe-dad|sustantivo femenino|Característica de lo que puede entenderse de varias maneras.|-|claridad|La ambigüedad de la frase confundió a todos.|ortografía
cigüeña|ci-güe-ña|sustantivo femenino|Ave grande de patas y pico largos que anida en lugares altos.|-|-|La cigüeña anidó en la torre.|ortografía
lingüística|lin-güís-ti-ca|sustantivo femenino|Ciencia que estudia el lenguaje.|-|-|La lingüística analiza cómo funcionan las lenguas.|ortografía
desagüe|de-sa-güe|sustantivo masculino|Tubo o canal por donde sale el agua.|-|-|El desagüe se tapó con hojas.|ortografía
convalecencia|con-va-le-cen-cia|sustantivo femenino|Tiempo de recuperación tras una enfermedad.|recuperación|-|Su convalecencia duró dos semanas.|ortografía
ecuánime|e-cuá-ni-me|adjetivo|Que juzga y actúa con serenidad y equilibrio.|imparcial|-|Un juez debe ser ecuánime.|ortografía
beneficencia|be-ne-fi-cen-cia|sustantivo femenino|Ayuda que se da a personas necesitadas.|caridad|-|El concierto fue de beneficencia.|ortografía
malestar|ma-les-tar|sustantivo masculino|Sensación de incomodidad o de no sentirse bien.|incomodidad|bienestar|Sintió malestar después de comer.|ortografía
iniciativa|i-ni-cia-ti-va|sustantivo femenino|Disposición para comenzar algo sin que otro lo pida.|-|-|Tomó la iniciativa de ordenar la sala.|general
pauta|pau-ta|sustantivo femenino|Modelo o conjunto de criterios para hacer o evaluar algo.|-|-|La pauta de evaluación tiene cinco criterios.|general
excepción|ex-cep-ción|sustantivo femenino|Caso que no sigue la regla general.|-|regla|La palabra «mano» es una excepción a la regla.|general
trayectoria|tra-yec-to-ria|sustantivo femenino|Recorrido de algo o de alguien a lo largo del tiempo.|-|-|La trayectoria del cohete fue recta.|general
ocasión|o-ca-sión|sustantivo femenino|Momento oportuno o vez en que ocurre algo.|oportunidad|-|Aprovechó la ocasión para saludar.|general
auricular|au-ri-cu-lar|sustantivo masculino|Pieza pequeña que se pone en la oreja para escuchar sonidos.|audífono|-|Me conecté con el auricular.|tecnología
publicación|pu-bli-ca-ción|sustantivo femenino|Mensaje o contenido que se difunde en internet o en un medio.|-|-|Su publicación recibió muchos comentarios.|tecnología
notificación|no-ti-fi-ca-ción|sustantivo femenino|Aviso que envía un dispositivo o un programa.|aviso|-|Apagué las notificaciones para concentrarme.|tecnología
videojuego|vi-de-o-jue-go|sustantivo masculino|Juego que se maneja en una pantalla.|-|-|Mi videojuego favorito es de aventuras.|tecnología
resaltador|re-sal-ta-dor|sustantivo masculino|Lápiz de color fuerte para marcar partes de un texto.|-|-|Marqué las ideas con un resaltador.|escuela
ion|ion|sustantivo masculino|Átomo o grupo de átomos con carga eléctrica.|-|-|El sodio forma un ion positivo.|química
enlace químico|en-la-ce quí-mi-co|locución nominal|Unión entre átomos que forma moléculas o compuestos.|-|-|El enlace químico del agua une hidrógeno y oxígeno.|química
pH|pe-ha-che|sustantivo masculino|Medida que indica qué tan ácida o básica es una sustancia.|-|-|El agua pura tiene un pH neutro.|química
neutralización|neu-tra-li-za-ción|sustantivo femenino|Reacción entre un ácido y una base que anula sus propiedades.|-|-|La neutralización produce sal y agua.|química
no metal|no me-tal|locución nominal|Elemento que no conduce bien el calor ni la electricidad.|-|metal|El azufre es un no metal.|química
aleación|a-le-a-ción|sustantivo femenino|Mezcla de un metal con otros elementos.|-|-|El bronce es una aleación de cobre y estaño.|química
polímero|po-lí-me-ro|sustantivo masculino|Sustancia formada por moléculas muy largas, como el plástico.|-|-|El nailon es un polímero.|química
catión|ca-tión|sustantivo masculino|Ion con carga positiva.|-|anión|El catión sodio tiene carga positiva.|química
anión|a-nión|sustantivo masculino|Ion con carga negativa.|-|catión|El cloruro es un anión.|química
plano inclinado|pla-no in-cli-na-do|locución nominal|Superficie en pendiente que ayuda a subir cargas.|rampa|-|La rampa es un plano inclinado.|física
máquina simple|má-qui-na sim-ple|locución nominal|Dispositivo sencillo que cambia la fuerza necesaria para hacer un trabajo.|-|-|La palanca es una máquina simple.|física
potencia eléctrica|po-ten-cia e-léc-tri-ca|locución nominal|Cantidad de energía que consume un aparato en cada segundo.|-|-|La potencia eléctrica se mide en vatios.|física
vatio|va-tio|sustantivo masculino|Unidad con que se mide la potencia.|watt|-|Una ampolleta de cien vatios consume más.|física
fusible|fu-si-ble|sustantivo masculino|Pieza que corta la corriente si es demasiado fuerte.|-|-|El fusible se quemó por la sobrecarga.|física
cometa|co-me-ta|sustantivo masculino|Cuerpo celeste de hielo y polvo que deja una cola brillante.|-|-|El cometa Halley regresa cada setenta y seis años.|astronomía
observatorio|ob-ser-va-to-rio|sustantivo masculino|Lugar equipado para observar el cielo.|-|-|El observatorio del norte tiene cielos muy limpios.|astronomía
clon|clon|sustantivo masculino|Ser vivo que es una copia genética exacta de otro.|-|-|La oveja Dolly fue un clon.|ciencias
parásito|pa-rá-si-to|adjetivo|Que vive a expensas de otro ser vivo.|-|-|La pulga es un insecto parásito.|ciencias
carnívoro|car-ní-vo-ro|sustantivo masculino|Animal que se alimenta de carne.|-|herbívoro|El puma es un carnívoro.|ciencias
herbívoro|her-bí-vo-ro|sustantivo masculino|Animal que se alimenta de plantas.|-|carnívoro|La vicuña es un herbívoro.|ciencias
omnívoro|om-ní-vo-ro|sustantivo masculino|Animal que come tanto plantas como animales.|-|-|El oso es un omnívoro.|ciencias
polinomio|po-li-no-mio|sustantivo masculino|Expresión algebraica formada por la suma de varios términos.|-|-|«x² + 3x + 2» es un polinomio.|matemática
monomio|mo-no-mio|sustantivo masculino|Expresión algebraica de un solo término.|-|-|«5x²» es un monomio.|matemática
apotema|a-po-te-ma|sustantivo femenino|Distancia del centro de un polígono regular al punto medio de un lado.|-|-|Medí la apotema del hexágono.|matemática
ángulo agudo|án-gu-lo a-gu-do|locución nominal|Ángulo que mide menos de noventa grados.|-|ángulo obtuso|Un ángulo de 40 grados es agudo.|matemática
ángulo obtuso|án-gu-lo ob-tu-so|locución nominal|Ángulo que mide más de noventa y menos de ciento ochenta grados.|-|ángulo agudo|Un ángulo de 120 grados es obtuso.|matemática
semejanza|se-me-jan-za|sustantivo femenino|Relación entre figuras con igual forma y distinto tamaño.|parecido|diferencia|La semejanza de triángulos mantiene los ángulos.|matemática
homotecia|ho-mo-te-cia|sustantivo femenino|Transformación que amplía o reduce una figura manteniendo su forma.|-|-|La homotecia duplicó el tamaño del dibujo.|matemática
simulación|si-mu-la-ción|sustantivo femenino|Representación de un fenómeno para estudiarlo sin vivirlo realmente.|-|-|La simulación lanzó mil veces el dado.|matemática
combinación|com-bi-na-ción|sustantivo femenino|Agrupación de elementos sin importar el orden.|-|-|Hay tres combinaciones posibles de sabores.|matemática
cuartil inferior|cuar-til in-fe-rior|locución nominal|Valor que deja el 25 % de los datos por debajo.|-|cuartil superior|El cuartil inferior fue 4.|matemática
infografía|in-fo-gra-fí-a|sustantivo femenino|Imagen que explica información mediante dibujos, gráficos y textos breves.|-|-|Hicimos una infografía sobre el reciclaje.|lenguaje
currículum|cu-rrí-cu-lum|sustantivo masculino|Documento que resume la formación y la experiencia de una persona.|-|-|Envió su currículum a la empresa.|lenguaje
informe|in-for-me|sustantivo masculino|Texto que presenta datos o resultados de manera ordenada.|reporte|-|El informe de laboratorio tenía conclusiones.|lenguaje
texto instructivo|tex-to ins-truc-ti-vo|locución nominal|Texto que explica paso a paso cómo hacer algo.|-|-|La receta es un texto instructivo.|lenguaje
texto expositivo|tex-to ex-po-si-ti-vo|locución nominal|Texto que presenta información sobre un tema para que se comprenda.|-|-|El libro de Ciencias tiene textos expositivos.|lenguaje
texto argumentativo|tex-to ar-gu-men-ta-ti-vo|locución nominal|Texto que busca convencer al lector de una idea.|-|-|La columna de opinión es un texto argumentativo.|lenguaje
metonimia|me-to-ni-mia|sustantivo femenino|Figura que nombra una cosa con el nombre de otra relacionada.|-|-|«Leí a Cervantes» es una metonimia por «leí sus libros».|literatura
oxímoron|o-xí-mo-ron|sustantivo masculino|Figura que une dos palabras de significado opuesto.|-|-|«Silencio ensordecedor» es un oxímoron.|literatura
eufemismo|eu-fe-mis-mo|sustantivo masculino|Palabra suave que se usa en lugar de otra más dura.|-|-|«Pasó a mejor vida» es un eufemismo.|lenguaje
calco|cal-co|sustantivo masculino|Expresión copiada de otro idioma que suena rara en el propio.|-|-|«Hacer sentido» es un calco del inglés.|lenguaje
dequeísmo|de-que-ís-mo|sustantivo masculino|Uso incorrecto de «de que» cuando no corresponde.|-|-|«Pienso de que vendrá» es un caso de dequeísmo.|lenguaje
voseo|vo-se-o|sustantivo masculino|Uso de «vos» en lugar de «tú» como forma de trato.|-|tuteo|En Chile se usa el voseo en el trato informal.|lenguaje
tuteo|tu-te-o|sustantivo masculino|Uso de «tú» como forma de trato.|-|voseo|El tuteo es común entre compañeros.|lenguaje
lenguaje corporal|len-gua-je cor-po-ral|locución nominal|Mensajes que transmitimos con gestos y posturas.|-|-|Su lenguaje corporal mostraba nerviosismo.|lenguaje
mímica|mí-mi-ca|sustantivo femenino|Arte de expresar con gestos y sin palabras.|-|-|Jugamos a adivinar películas con mímica.|lenguaje
dicción|dic-ción|sustantivo femenino|Forma de pronunciar las palabras.|pronunciación|-|La actriz tiene una dicción impecable.|lenguaje
gesto|ges-to|sustantivo masculino|Movimiento del rostro o de las manos que expresa algo.|ademán|-|Con un gesto me pidió silencio.|lenguaje
silogismo|si-lo-gis-mo|sustantivo masculino|Razonamiento de tres partes en que dos premisas llevan a una conclusión.|-|-|«Todos los gatos son mamíferos» es una premisa de un silogismo.|argumentación
generalización|ge-ne-ra-li-za-ción|sustantivo femenino|Afirmación que extiende algo a todos los casos.|-|-|Decir «todos mienten» es una generalización.|argumentación
refutación|re-fu-ta-ción|sustantivo femenino|Argumento que muestra que una idea es falsa.|-|-|Su refutación fue clara y con datos.|argumentación
contraposición|con-tra-po-si-ción|sustantivo femenino|Enfrentamiento de dos ideas para mostrar sus diferencias.|contraste|-|La contraposición de opiniones enriqueció el debate.|argumentación
persuasión|per-sua-sión|sustantivo femenino|Capacidad de convencer con razones o emociones.|-|-|La publicidad usa la persuasión.|argumentación
sondeo|son-de-o|sustantivo masculino|Consulta a un grupo para conocer su opinión.|encuesta|-|Un sondeo mostró que el curso prefiere el jueves.|medios
audiencia|au-dien-cia|sustantivo femenino|Conjunto de personas que ven o escuchan un medio.|público|-|La audiencia del programa creció.|medios
medios de comunicación|me-dios de co-mu-ni-ca-ción|locución nominal|Canales como diarios, radio, televisión e internet que transmiten información.|-|-|Los medios de comunicación informan sobre lo que ocurre.|medios
agencia de noticias|a-gen-cia de no-ti-cias|locución nominal|Empresa que reúne y vende noticias a los medios.|-|-|La agencia de noticias envió la información.|medios
corresponsal|co-rres-pon-sal|sustantivo común|Periodista que informa desde otra ciudad o país.|-|-|La corresponsal envió su crónica desde Roma.|medios
fotoperiodismo|fo-to-pe-rio-dis-mo|sustantivo masculino|Periodismo que cuenta los hechos con fotografías.|-|-|El fotoperiodismo muestra la realidad en una imagen.|medios
paradigma|pa-ra-dig-ma|sustantivo masculino|Modelo o ejemplo que sirve como guía para pensar o actuar.|modelo|-|El paradigma científico cambió con la nueva teoría.|general
ideología|i-de-o-lo-gí-a|sustantivo femenino|Conjunto de ideas que caracteriza a una persona o a un grupo.|doctrina|-|Cada partido defiende su ideología.|general
doctrina|doc-tri-na|sustantivo femenino|Conjunto de enseñanzas o ideas que sigue un grupo.|-|-|La doctrina de esa escuela filosófica es antigua.|general
dogma|dog-ma|sustantivo masculino|Idea que se acepta como cierta sin discutirla.|-|-|Para el científico, ningún dogma es indiscutible.|general
utopía|u-to-pí-a|sustantivo femenino|Plan o lugar ideal que parece imposible de alcanzar.|-|-|La ciudad perfecta era una utopía.|general
moral|mo-ral|sustantivo femenino|Conjunto de normas sobre lo que se considera bueno o malo.|-|-|La moral guía nuestras decisiones.|general
vicio|vi-cio|sustantivo masculino|Mala costumbre que cuesta dejar.|-|virtud|Morderse las uñas es un vicio.|general
albedrío|al-be-drí-o|sustantivo masculino|Capacidad de decidir por voluntad propia.|-|-|Tiene libre albedrío para elegir su carrera.|general
conciencia|con-cien-cia|sustantivo femenino|Capacidad de reconocer lo que está bien y mal o de darse cuenta de algo.|-|-|Mi conciencia me dijo que debía devolver el dinero.|general
intuición|in-tui-ción|sustantivo femenino|Percepción inmediata de algo sin razonarlo.|-|-|Mi intuición me dijo que algo andaba mal.|general
percepción|per-cep-ción|sustantivo femenino|Modo de captar algo con los sentidos o la mente.|-|-|La percepción del color varía entre personas.|general
olvido|ol-vi-do|sustantivo masculino|Pérdida del recuerdo de algo.|-|recuerdo|El olvido de las llaves fue un problema.|general
apariencia|a-pa-rien-cia|sustantivo femenino|Aspecto exterior de algo o de alguien.|aspecto|esencia|La apariencia puede engañar.|general
esencia|e-sen-cia|sustantivo femenino|Característica más importante de algo.|-|apariencia|La esencia del cuento es la amistad.|general
tabú|ta-bú|sustantivo masculino|Tema o conducta que una sociedad prohíbe nombrar o hacer.|-|-|En muchas culturas, hablar de la muerte es un tabú.|cultura
espiritualidad|es-pi-ri-tua-li-dad|sustantivo femenino|Búsqueda de sentido que va más allá de lo material.|-|-|La espiritualidad mapuche conecta con la tierra.|cultura
laico|lai-co|adjetivo|Que no depende de ninguna religión.|secular|-|El Estado chileno es laico.|cultura
sagrado|sa-gra-do|adjetivo|Que se considera digno de respeto religioso.|santo|profano|El pehuén es un árbol sagrado.|cultura
profano|pro-fa-no|adjetivo|Que no es sagrado ni religioso.|laico|sagrado|La música profana se toca en las fiestas.|cultura
santuario|san-tua-rio|sustantivo masculino|Lugar sagrado al que se acude con devoción.|-|-|Miles de fieles visitan el santuario.|cultura
peregrino|pe-re-gri-no|sustantivo masculino|Persona que viaja a un lugar sagrado.|-|-|Los peregrinos caminaron hasta la ermita.|cultura
catedral|ca-te-dral|sustantivo femenino|Iglesia principal de una ciudad o región.|-|-|La catedral tiene vitrales de colores.|cultura
vitral|vi-tral|sustantivo masculino|Ventana de vidrios de colores unidos con plomo.|-|-|El vitral dibuja una escena bíblica.|artes
gótico|gó-ti-co|adjetivo|Se dice del estilo europeo medieval de arcos puntiagudos y grandes ventanales.|-|-|La catedral gótica tiene torres muy altas.|artes
vasallo|va-sa-llo|sustantivo masculino|En el feudalismo, persona que debía obediencia y servicio a un señor.|-|señor|El vasallo juró fidelidad al señor.|historia
siervo|sier-vo|sustantivo masculino|Campesino medieval que trabajaba la tierra del señor y no era libre.|-|-|Los siervos entregaban parte de la cosecha.|historia
feudo|feu-do|sustantivo masculino|Territorio que un señor entregaba a un vasallo a cambio de servicios.|-|-|El feudo incluía aldeas y campos.|historia
caballero|ca-ba-lle-ro|sustantivo masculino|Guerrero medieval que combatía a caballo.|-|-|El caballero defendió el castillo.|historia
trovador|tro-va-dor|sustantivo masculino|Poeta medieval que cantaba sus versos.|juglar|-|El trovador cantó a la dama.|historia
cruzada|cru-za-da|sustantivo femenino|Expedición militar medieval que buscaba recuperar Tierra Santa.|-|-|Las cruzadas unieron a Europa con Oriente.|historia
peste|pes-te|sustantivo femenino|Enfermedad contagiosa que provoca muchas muertes.|plaga|-|La peste negra diezmó a Europa.|historia
hallazgo|ha-llaz-go|sustantivo masculino|Descubrimiento de algo valioso.|descubrimiento|-|El hallazgo de fósiles sorprendió al equipo.|general
retroceso|re-tro-ce-so|sustantivo masculino|Vuelta hacia atrás o pérdida de lo logrado.|-|avance|El retroceso en las notas preocupó al curso.|general
auge|au-ge|sustantivo masculino|Momento de mayor crecimiento o éxito.|apogeo|declive|El auge de la minería cambió la región.|general
declive|de-cli-ve|sustantivo masculino|Etapa en que algo pierde fuerza o importancia.|ocaso|auge|El declive de la fábrica dejó sin trabajo a muchos.|general
crisis|cri-sis|sustantivo femenino|Momento difícil en que algo cambia de forma importante.|-|-|La crisis económica afectó a muchas familias.|general
colapso|co-lap-so|sustantivo masculino|Caída o fallo total de algo.|derrumbe|-|El colapso del puente cortó la ruta.|general
quiebra|quie-bra|sustantivo femenino|Situación en que una empresa no puede pagar sus deudas.|bancarrota|-|La quiebra de la fábrica dejó sin empleo a muchos.|economía
abundancia|a-bun-dan-cia|sustantivo femenino|Gran cantidad de algo.|profusión|escasez|Hubo abundancia de fruta este verano.|economía
déficit|dé-fi-cit|sustantivo masculino|Falta de dinero o de recursos para cubrir lo necesario.|-|superávit|El club tiene déficit en sus cuentas.|economía
superávit|su-pe-rá-vit|sustantivo masculino|Excedente de ingresos sobre los gastos.|-|déficit|El país tuvo superávit este año.|economía
transferencia|trans-fe-ren-cia|sustantivo femenino|Envío de dinero de una cuenta a otra.|-|-|Hizo una transferencia bancaria.|economía
diagnóstico|diag-nós-ti-co|sustantivo masculino|Identificación de una enfermedad por parte de un médico.|-|-|El diagnóstico fue una gripe.|salud
tratamiento|tra-ta-mien-to|sustantivo masculino|Conjunto de medios para curar o aliviar una enfermedad.|terapia|-|El tratamiento dura una semana.|salud
dosis|do-sis|sustantivo femenino|Cantidad exacta de un medicamento que se debe tomar.|-|-|Tomó la dosis indicada.|salud
inflamación|in-fla-ma-ción|sustantivo femenino|Hinchazón y enrojecimiento de una zona del cuerpo.|-|-|La inflamación bajó con hielo.|salud
jabalina|ja-ba-li-na|sustantivo femenino|Lanza ligera que se arroja en atletismo.|-|-|Lanzó la jabalina muy lejos.|deporte
pértiga|pér-ti-ga|sustantivo femenino|Vara larga y flexible que se usa para saltar en atletismo.|garrocha|-|Saltó con pértiga sobre el listón.|deporte
esgrima|es-gri-ma|sustantivo femenino|Deporte de combate con espadas.|-|-|La esgrima exige rapidez y concentración.|deporte
piragüismo|pi-ra-güis-mo|sustantivo masculino|Deporte que se practica remando en una piragua.|-|-|El piragüismo se practica en ríos y lagos.|deporte
escalada|es-ca-la-da|sustantivo femenino|Deporte que consiste en subir paredes de roca.|-|-|La escalada requiere fuerza y técnica.|deporte
ajedrez|a-je-drez|sustantivo masculino|Juego de mesa de estrategia entre dos jugadores con piezas sobre un tablero.|-|-|El ajedrez desarrolla la concentración.|deporte
pasamanos|pa-sa-ma-nos|sustantivo masculino|Barandilla que sirve para apoyar la mano al subir o bajar.|barandal|-|Me sujeté del pasamanos.|casa
peldaño|pel-da-ño|sustantivo masculino|Cada escalón de una escalera.|escalón|-|Resbalé en el último peldaño.|casa
desván|des-ván|sustantivo masculino|Espacio bajo el techo de una casa donde se guardan cosas.|buhardilla|sótano|En el desván encontré fotos antiguas.|casa
sótano|só-ta-no|sustantivo masculino|Piso de una casa que está bajo tierra.|-|desván|Guardamos las herramientas en el sótano.|casa
azotea|a-zo-te-a|sustantivo femenino|Techo plano de un edificio.|terraza|-|Subimos a la azotea a mirar las estrellas.|casa
reja|re-ja|sustantivo femenino|Conjunto de barras de metal que cierra una abertura.|-|-|La reja del jardín estaba abierta.|casa
portón|por-tón|sustantivo masculino|Puerta grande de entrada.|-|-|El auto salió por el portón.|casa
buzón|bu-zón|sustantivo masculino|Caja donde se echan o reciben las cartas.|-|-|Dejó la carta en el buzón.|casa
persiana|per-sia-na|sustantivo femenino|Cortina de láminas que regula la luz de una ventana.|-|-|Bajé la persiana para dormir la siesta.|casa
colchón|col-chón|sustantivo masculino|Pieza blanda y acolchada que se pone sobre la cama.|-|-|El colchón es firme y cómodo.|casa
frazada|fra-za-da|sustantivo femenino|Manta gruesa para abrigarse en la cama.|manta|-|En invierno uso una frazada de lana.|casa
almohada|al-mo-ha-da|sustantivo femenino|Cojín que se pone bajo la cabeza para dormir.|-|-|Dormí con la almohada alta.|casa
velador|ve-la-dor|sustantivo masculino|En Chile, mesita junto a la cama.|-|-|Dejé el reloj en el velador (uso en Chile).|casa
repisa|re-pi-sa|sustantivo femenino|Tabla fija a la pared para poner objetos.|estante|-|Los libros están en la repisa.|casa
condimento|con-di-men-to|sustantivo masculino|Sustancia que se agrega a la comida para darle sabor.|aliño|-|La sal es un condimento básico.|cocina
orégano|o-ré-ga-no|sustantivo masculino|Hierba aromática que se usa en salsas y pizzas.|-|-|Espolvoreé orégano sobre la pizza.|cocina
cilantro|ci-lan-tro|sustantivo masculino|Hierba de olor fuerte que se usa en ensaladas y salsas.|-|-|El pebre lleva cilantro.|cocina
perejil|pe-re-jil|sustantivo masculino|Hierba verde que se usa para dar sabor a las comidas.|-|-|Agregué perejil picado al caldo.|cocina
albahaca|al-ba-ha-ca|sustantivo femenino|Hierba aromática que se usa en salsas y ensaladas.|-|-|La albahaca perfumó la pasta.|cocina
canela|ca-ne-la|sustantivo femenino|Corteza aromática de un árbol que se usa en postres.|-|-|El arroz con leche lleva canela.|cocina
vainilla|vai-ni-lla|sustantivo femenino|Esencia aromática que da sabor a postres y helados.|-|-|El helado de vainilla es mi favorito.|cocina
fornido|for-ni-do|adjetivo|Fuerte y con músculos desarrollados.|corpulento|raquítico|El leñador era alto y fornido.|descripción
esbelto|es-bel-to|adjetivo|Alto, delgado y elegante.|estilizado|rechoncho|La bailarina era esbelta.|descripción
robusto|ro-bus-to|adjetivo|Fuerte y resistente.|vigoroso|débil|Es un roble robusto.|descripción
enjuto|en-ju-to|adjetivo|Delgado y seco, sin grasa.|flaco|rollizo|Era un anciano enjuto.|descripción
lozano|lo-za-no|adjetivo|Que muestra salud y frescura.|saludable|marchito|Las manzanas lucían lozanas.|descripción
pecoso|pe-co-so|adjetivo|Que tiene pequeñas manchas oscuras en la piel.|-|-|La niña pecosa se reía mucho.|descripción
calvo|cal-vo|adjetivo|Que no tiene pelo en la cabeza.|pelado|melenudo|El abuelo es calvo.|descripción
arrugado|a-rru-ga-do|adjetivo|Que tiene pliegues o arrugas.|-|liso|La camisa quedó arrugada.|descripción
diestro|dies-tro|adjetivo|Hábil y seguro en lo que hace.|hábil|torpe|Es diestro con el balón.|descripción
voraz|vo-raz|adjetivo|Que come mucho y con ansia.|glotón|inapetente|El león es un animal voraz.|descripción
sediento|se-dien-to|adjetivo|Que tiene mucha sed.|-|saciado|Llegó sediento después de la caminata.|descripción
famélico|fa-mé-li-co|adjetivo|Muy hambriento y flaco.|hambriento|saciado|Un perro famélico buscaba comida.|descripción
sobrio|so-brio|adjetivo|Moderado y sin adornos, o que no ha bebido alcohol.|austero|excesivo|El traje era sobrio y elegante.|descripción
opulento|o-pu-len-to|adjetivo|Muy rico y con mucho lujo.|lujoso|modesto|La mansión era opulenta.|descripción
modesto|mo-des-to|adjetivo|Sin lujos ni presunción.|humilde|ostentoso|Vivían en una casa modesta.|descripción
ostentoso|os-ten-to-so|adjetivo|Que se muestra con exceso para llamar la atención.|vistoso|sencillo|Llevaba un reloj ostentoso.|descripción
soberbio|so-ber-bio|adjetivo|Orgulloso y que se cree superior a los demás.|arrogante|humilde|Su actitud soberbia molestó al curso.|carácter
arrogante|a-rro-gan-te|adjetivo|Que se cree mejor que los otros y lo demuestra.|altivo|humilde|Fue arrogante con sus compañeros.|carácter
bondadoso|bon-da-do-so|adjetivo|Que tiene buen corazón.|amable|cruel|Una vecina bondadosa nos ayudó.|carácter
cruel|cruel|adjetivo|Que hace sufrir a otros sin compasión.|despiadado|compasivo|Es cruel burlarse de los demás.|carácter
compasivo|com-pa-si-vo|adjetivo|Que siente pena por el dolor ajeno y trata de ayudar.|piadoso|cruel|Fue compasivo con el herido.|carácter
terco|ter-co|adjetivo|Que insiste en sus ideas aunque no tenga razón.|obstinado|flexible|Es terco y no escucha consejos.|carácter
obstinado|obs-ti-na-do|adjetivo|Que mantiene su opinión con mucha firmeza.|terco|dócil|Se mostró obstinado en su decisión.|carácter
dócil|dó-cil|adjetivo|Que obedece con facilidad.|manso|rebelde|El caballo es dócil.|carácter
ocurrente|o-cu-rren-te|adjetivo|Que tiene ideas graciosas o ingeniosas.|ingenioso|-|Su comentario ocurrente hizo reír a todos.|carácter
sobresaliente|so-bre-sa-lien-te|adjetivo|Que destaca por ser muy bueno.|destacado|mediocre|Obtuvo una nota sobresaliente.|general
mediocre|me-dio-cre|adjetivo|De calidad media o baja.|corriente|excelente|La película me pareció mediocre.|general
excelente|ex-ce-len-te|adjetivo|Muy bueno, de gran calidad.|magnífico|pésimo|Fue una excelente exposición.|general
pésimo|pé-si-mo|adjetivo|Muy malo.|horrible|excelente|El servicio fue pésimo.|general
espléndido|es-plén-di-do|adjetivo|Muy hermoso o muy generoso.|magnífico|mediocre|Hizo un espléndido regalo.|general
deplorable|de-plo-ra-ble|adjetivo|Lamentable, que da pena.|lamentable|admirable|El estado de la plaza era deplorable.|general
admirable|ad-mi-ra-ble|adjetivo|Digno de ser admirado.|loable|deplorable|Su valentía fue admirable.|general
inusual|i-nu-sual|adjetivo|Que no es habitual.|raro|habitual|Hacía un calor inusual para la época.|general
genuino|ge-nui-no|adjetivo|Auténtico, sin imitación.|auténtico|falso|Compró artesanía genuina.|general
auténtico|au-tén-ti-co|adjetivo|Verdadero, que es lo que dice ser.|genuino|falso|El documento es auténtico.|general
repleto|re-ple-to|adjetivo|Completamente lleno.|abarrotado|vacío|El bus iba repleto.|general
espacioso|es-pa-cio-so|adjetivo|Amplio, con mucho lugar.|amplio|reducido|La sala es espaciosa.|general
luminoso|lu-mi-no-so|adjetivo|Que da luz o tiene mucha luz.|brillante|oscuro|La sala es luminosa.|general
agitado|a-gi-ta-do|adjetivo|Con mucha actividad o muy alterado.|inquieto|tranquilo|Tuvo un día agitado.|general
concurrido|con-cu-rri-do|adjetivo|Con mucha gente.|transitado|desierto|La feria estaba muy concurrida.|general
desierto|de-sier-to|adjetivo|Sin gente.|despoblado|concurrido|La calle estaba desierta a esa hora.|general
reciente|re-cien-te|adjetivo|Que ocurrió hace poco.|nuevo|antiguo|La noticia es reciente.|general
vigente|vi-gen-te|adjetivo|Que está en uso o en vigor.|activo|obsoleto|La ley sigue vigente.|general
obsoleto|ob-so-le-to|adjetivo|Que ya no se usa por estar pasado de moda.|anticuado|moderno|Ese teléfono ya es obsoleto.|general
anticuado|an-ti-cua-do|adjetivo|Pasado de moda.|obsoleto|moderno|Su vestido era anticuado.|general
pasajero|pa-sa-je-ro|adjetivo|Que dura poco.|breve|permanente|Fue un enojo pasajero.|general
permanente|per-ma-nen-te|adjetivo|Que dura o se mantiene siempre.|fijo|temporal|Tiene un trabajo permanente.|general
reservado|re-ser-va-do|adjetivo|Que habla poco de sí mismo o que ha sido apartado.|callado|extrovertido|Es una persona reservada.|general
extrovertido|ex-tro-ver-ti-do|adjetivo|Que se muestra abierto y sociable.|sociable|introvertido|Mi prima extrovertida hace amigos fácilmente.|carácter
introvertido|in-tro-ver-ti-do|adjetivo|Que se muestra reservado y piensa más hacia adentro.|reservado|extrovertido|Es introvertido y prefiere leer.|carácter
huraño|hu-ra-ño|adjetivo|Que evita el trato con las personas.|arisco|sociable|El vecino huraño casi no sale.|carácter
quisquilloso|quis-qui-llo-so|adjetivo|Que se molesta por cosas pequeñas.|melindroso|-|Es quisquilloso con la comida.|carácter
caprichoso|ca-pri-cho-so|adjetivo|Que cambia de opinión por antojo.|antojadizo|-|Es caprichoso y nunca queda conforme.|carácter
pehuenche|pe-huen-che|sustantivo común|Persona del pueblo mapuche que vivía cerca de los bosques de araucarias.|-|-|Los pehuenches recolectaban piñones.|historia
mapuche|ma-pu-che|sustantivo común|Persona del pueblo originario del centro y sur de Chile.|-|-|Los mapuche resistieron a los conquistadores.|historia
ruca|ru-ca|sustantivo femenino|Casa tradicional mapuche hecha de madera y paja.|-|-|La ruca tiene el fogón en el centro.|historia
quipu|qui-pu|sustantivo masculino|Sistema de cuerdas con nudos que los incas usaban para llevar cuentas.|-|-|Los incas registraban datos con quipus.|historia
terraza de cultivo|te-rra-za de cul-ti-vo|locución nominal|Escalón construido en una ladera para sembrar.|andén|-|Las terrazas de cultivo evitan la erosión.|historia
sincrético|sin-cré-ti-co|adjetivo|Que mezcla elementos de distintas culturas o religiones.|mixto|-|La fiesta de La Tirana es un ritual sincrético.|historia
fortificación|for-ti-fi-ca-ción|sustantivo femenino|Obra defensiva que protege un lugar.|-|-|La fortificación defendía el puerto.|historia
emboscada|em-bos-ca-da|sustantivo femenino|Ataque sorpresa desde un lugar escondido.|-|-|Los guerreros prepararon una emboscada.|historia
modernidad|mo-der-ni-dad|sustantivo femenino|Época o cualidad de lo moderno.|-|antigüedad|La modernidad trajo nuevas ideas.|historia
originario|o-ri-gi-na-rio|adjetivo|Que proviene de un lugar desde su comienzo.|nativo|extranjero|Los pueblos originarios habitaban estas tierras.|cultura
foráneo|fo-rá-ne-o|adjetivo|De fuera, que viene de otro lugar.|extranjero|local|Introdujeron plantas foráneas.|cultura
autóctono|au-tóc-to-no|adjetivo|Que es propio del lugar donde vive o se produce.|nativo|foráneo|El huemul es una especie autóctona.|cultura
transculturación|trans-cul-tu-ra-ción|sustantivo femenino|Mezcla de elementos de dos culturas que da origen a algo nuevo.|-|-|La transculturación se ve en la música popular.|cultura
etnia|et-nia|sustantivo femenino|Grupo de personas que comparten idioma, costumbres y origen.|-|-|El pueblo rapanui es una etnia de Polinesia.|cultura
festividad|fes-ti-vi-dad|sustantivo femenino|Celebración de carácter especial.|fiesta|-|La festividad convoca a todo el pueblo.|cultura
carnaval|car-na-val|sustantivo masculino|Fiesta popular con desfiles, música y disfraces.|-|-|El carnaval llenó las calles de colores.|cultura
alfarero|al-fa-re-ro|sustantivo masculino|Artesano que hace objetos de barro.|ceramista|-|El alfarero moldeó una jarra.|cultura
tejedor|te-je-dor|sustantivo masculino|Persona que fabrica telas o tejidos en un telar.|-|-|La tejedora hiló lana de oveja.|cultura
orfebre|or-fe-bre|sustantivo común|Artesano que trabaja el oro y la plata.|-|-|El orfebre hizo una joya de plata.|cultura
memoria histórica|me-mo-ria his-tó-ri-ca|locución nominal|Recuerdo colectivo de hechos importantes del pasado.|-|-|La memoria histórica ayuda a no repetir errores.|historia
"""

VERBOS = """
reescribir|re-es-cri-bir|Volver a escribir un texto para mejorarlo.|reescribo|reescribe|reescribió|reescribirá|corregir|-|Reescribió el párrafo más claro.
plantear|plan-te-ar|Presentar una idea, un problema o una pregunta para discutirlo.|planteo|plantea|planteó|planteará|proponer|-|Planteó una solución al problema.
formular|for-mu-lar|Expresar una idea o una pregunta de manera clara.|formulo|formula|formuló|formulará|expresar|-|Formuló una hipótesis para el experimento.
enfatizar|en-fa-ti-zar|Poner especial fuerza en lo que se dice.|enfatizo|enfatiza|enfatizó|enfatizará|subrayar|-|Enfatizó la importancia de la puntualidad.
aludir|a-lu-dir|Referirse a alguien o algo sin nombrarlo del todo.|aludo|alude|aludió|aludirá|mencionar|-|El poema alude a la infancia del autor.
factorizar|fac-to-ri-zar|Escribir una expresión como producto de factores.|factorizo|factoriza|factorizó|factorizará|-|-|Factorizó el polinomio para resolver la ecuación.
heredar|he-re-dar|Recibir rasgos o bienes de los antepasados.|heredo|hereda|heredó|heredará|recibir|-|Heredó el color de ojos de su abuela.
evolucionar|e-vo-lu-cio-nar|Cambiar y desarrollarse poco a poco.|evoluciono|evoluciona|evolucionó|evolucionará|desarrollarse|-|Las especies evolucionan con el tiempo.
regenerar|re-ge-ne-rar|Volver a formar algo que se había perdido.|regenero|regenera|regeneró|regenerará|renovar|-|La piel se regenera tras una herida.
esbozar|es-bo-zar|Hacer un dibujo o un plan muy general.|esbozo|esboza|esbozó|esbozará|bosquejar|-|Esbozó el diseño en una servilleta.
plasmar|plas-mar|Dar forma concreta a una idea.|plasmo|plasma|plasmó|plasmará|reflejar|-|El pintor plasmó el paisaje en su cuadro.
retratar|re-tra-tar|Hacer una imagen o descripción de una persona o de una época.|retrato|retrata|retrató|retratará|describir|-|La novela retrata la vida rural.
exhibir|ex-hi-bir|Mostrar algo en público.|exhibo|exhibe|exhibió|exhibirá|exponer|ocultar|El museo exhibe pinturas del siglo XVIII.
discriminar|dis-cri-mi-nar|Tratar a una persona peor por su origen u otra característica.|discrimino|discrimina|discriminó|discriminará|excluir|incluir|Nadie debe discriminar a otro por su apariencia.
impulsar|im-pul-sar|Dar fuerza para que algo avance.|impulso|impulsa|impulsó|impulsará|promover|frenar|La beca impulsó sus estudios.
abarcar|a-bar-car|Incluir o contener varias cosas dentro de sí.|abarco|abarca|abarcó|abarcará|incluir|excluir|El curso abarca cuatro unidades.
acatar|a-ca-tar|Obedecer una norma o una orden.|acato|acata|acató|acatará|obedecer|desobedecer|Acató las reglas del juego.
acumular|a-cu-mu-lar|Juntar cosas en cantidad.|acumulo|acumula|acumuló|acumulará|amontonar|repartir|Acumuló puntos durante el campeonato.
aliviar|a-li-viar|Hacer menos intenso un dolor o una carga.|alivio|alivia|alivió|aliviará|calmar|agravar|La pomada alivió el dolor.
alterar|al-te-rar|Cambiar la forma o el orden de algo.|altero|altera|alteró|alterará|modificar|mantener|El calor altera el sabor de la leche.
anticipar|an-ti-ci-par|Hacer o decir algo antes de tiempo.|anticipo|anticipa|anticipó|anticipará|adelantar|retrasar|Anticipó el final de la historia.
apelar|a-pe-lar|Recurrir a algo o a alguien para pedir ayuda o una revisión.|apelo|apela|apeló|apelará|recurrir|-|Apeló a la justicia.
arriesgar|a-rries-gar|Poner algo en peligro para conseguir un fin.|arriesgo|arriesga|arriesgó|arriesgará|exponer|proteger|Arriesgó su puesto por decir la verdad.
asimilar|a-si-mi-lar|Comprender y hacer propio lo que se aprende.|asimilo|asimila|asimiló|asimilará|absorber|-|Asimiló rápido las reglas del juego.
atenuar|a-te-nuar|Hacer algo menos fuerte o intenso.|atenúo|atenúa|atenuó|atenuará|suavizar|intensificar|La cortina atenúa la luz.
autorizar|au-to-ri-zar|Dar permiso oficial para hacer algo.|autorizo|autoriza|autorizó|autorizará|permitir|prohibir|La directora autorizó la salida.
beneficiar|be-ne-fi-ciar|Hacer bien o dar ventaja a alguien.|beneficio|beneficia|benefició|beneficiará|favorecer|perjudicar|La lluvia beneficia a los agricultores.
captar|cap-tar|Percibir algo o atraer la atención.|capto|capta|captó|captará|percibir|-|Captó el mensaje de inmediato.
caracterizar|ca-rac-te-ri-zar|Distinguir algo por sus rasgos propios.|caracterizo|caracteriza|caracterizó|caracterizará|definir|-|La amabilidad caracteriza a mi tía.
ceder|ce-der|Dar algo a otro o dejar de oponerse.|cedo|cede|cedió|cederá|renunciar|resistir|Cedió su asiento a una señora.
coincidir|coin-ci-dir|Ser igual o ocurrir a la vez que otra cosa.|coincido|coincide|coincidió|coincidirá|concordar|discrepar|Mi cumpleaños coincide con el de mi prima.
compensar|com-pen-sar|Equilibrar un daño o una falta con algo a cambio.|compenso|compensa|compensó|compensará|equilibrar|-|Compensó su atraso con un gran trabajo.
complicar|com-pli-car|Hacer algo más difícil o confuso.|complico|complica|complicó|complicará|dificultar|facilitar|La lluvia complicó el viaje.
conceder|con-ce-der|Dar algo a alguien, como un permiso o un premio.|concedo|concede|concedió|concederá|otorgar|negar|Le concedieron una beca.
concebir|con-ce-bir|Formar una idea o un plan en la mente.|concibo|concibe|concibió|concebirá|idear|-|Concibió un plan para ahorrar agua.
condicionar|con-di-cio-nar|Hacer que algo dependa de una condición.|condiciono|condiciona|condicionó|condicionará|limitar|-|El clima condiciona el viaje.
consolidar|con-so-li-dar|Hacer algo más firme y seguro.|consolido|consolida|consolidó|consolidará|afianzar|debilitar|El equipo consolidó su liderazgo.
constatar|cons-ta-tar|Comprobar y dejar claro un hecho.|constato|constata|constató|constatará|verificar|-|Constató que la puerta estaba abierta.
consultar|con-sul-tar|Pedir consejo o buscar información.|consulto|consulta|consultó|consultará|preguntar|-|Consultó el diccionario.
contradecir|con-tra-de-cir|Decir lo contrario de lo que otro afirma.|contradigo|contradice|contradijo|contradirá|refutar|confirmar|Su ejemplo contradice la regla.
coordinar|co-or-di-nar|Organizar acciones para que funcionen en conjunto.|coordino|coordina|coordinó|coordinará|organizar|-|Coordinó el trabajo del grupo.
dedicar|de-di-car|Destinar tiempo o esfuerzo a algo.|dedico|dedica|dedicó|dedicará|consagrar|-|Dedicó la tarde a estudiar.
definir|de-fi-nir|Explicar con precisión qué es algo.|defino|define|definió|definirá|precisar|-|Define la palabra con tus propios términos.
delatar|de-la-tar|Contar a otros un hecho que alguien quería ocultar.|delato|delata|delató|delatará|acusar|encubrir|Su silencio lo delató.
derivar|de-ri-var|Provenir de algo o tomar otra dirección.|derivo|deriva|derivó|derivará|proceder|-|«Zapatería» deriva de «zapato».
desafiar|de-sa-fiar|Retar a alguien a hacer algo difícil.|desafío|desafía|desafió|desafiará|retar|-|Me desafió a una carrera.
descender|des-cen-der|Ir de un lugar alto a otro más bajo.|desciendo|desciende|descendió|descenderá|bajar|ascender|La temperatura desciende de noche.
desempeñar|de-sem-pe-ñar|Cumplir una función o un trabajo.|desempeño|desempeña|desempeñó|desempeñará|ejercer|-|Desempeña el cargo de tesorera.
desencadenar|de-sen-ca-de-nar|Provocar una serie de hechos.|desencadeno|desencadena|desencadenó|desencadenará|provocar|-|La sequía desencadenó una crisis.
desmentir|des-men-tir|Decir que algo es falso.|desmiento|desmiente|desmintió|desmentirá|negar|confirmar|El gobierno desmintió el rumor.
despreciar|des-pre-ciar|Considerar que algo o alguien no vale.|desprecio|desprecia|despreció|despreciará|menospreciar|apreciar|Nunca desprecies el trabajo de otros.
desvanecer|des-va-ne-cer|Hacer que algo desaparezca poco a poco.|desvanezco|desvanece|desvaneció|desvanecerá|disipar|-|La niebla se desvaneció al mediodía.
detener|de-te-ner|Parar algo o a alguien.|detengo|detiene|detuvo|detendrá|parar|continuar|La policía detuvo al ladrón.
devolver|de-vol-ver|Regresar algo a quien lo tenía.|devuelvo|devuelve|devolvió|devolverá|restituir|quedarse|Devolvió el libro a la biblioteca.
dispersar|dis-per-sar|Separar y esparcir cosas o personas.|disperso|dispersa|dispersó|dispersará|esparcir|reunir|El viento dispersó las hojas.
disponer|dis-po-ner|Colocar algo en cierto orden o tener algo para usar.|dispongo|dispone|dispuso|dispondrá|ordenar|-|Dispuso los libros por tamaño.
divulgar|di-vul-gar|Dar a conocer algo a mucha gente.|divulgo|divulga|divulgó|divulgará|difundir|ocultar|La radio divulgó la noticia.
eludir|e-lu-dir|Evitar algo con habilidad.|eludo|elude|eludió|eludirá|esquivar|enfrentar|Eludió la pregunta con una broma.
emprender|em-pren-der|Empezar una tarea o un proyecto importante.|emprendo|emprende|emprendió|emprenderá|iniciar|abandonar|Emprendió un viaje por el sur.
engañar|en-ga-ñar|Hacer creer algo falso.|engaño|engaña|engañó|engañará|embaucar|-|El mago engañó al público.
enmendar|en-men-dar|Corregir un error.|enmiendo|enmienda|enmendó|enmendará|corregir|-|Enmendó su falta con una disculpa.
erradicar|e-rra-di-car|Eliminar algo por completo.|erradico|erradica|erradicó|erradicará|eliminar|-|La vacuna erradicó la viruela.
evidenciar|e-vi-den-ciar|Mostrar algo con claridad.|evidencio|evidencia|evidenció|evidenciará|demostrar|ocultar|Los datos evidencian un cambio.
facilitar|fa-ci-li-tar|Hacer algo más fácil.|facilito|facilita|facilitó|facilitará|simplificar|dificultar|El mapa facilita la ruta.
implicar|im-pli-car|Incluir algo como consecuencia o involucrar a alguien.|implico|implica|implicó|implicará|conllevar|-|Estudiar implica esfuerzo.
inaugurar|i-nau-gu-rar|Abrir algo oficialmente por primera vez.|inauguro|inaugura|inauguró|inaugurará|estrenar|clausurar|Inauguraron el nuevo gimnasio.
incentivar|in-cen-ti-var|Animar a alguien con un premio o estímulo.|incentivo|incentiva|incentivó|incentivará|estimular|desalentar|La profesora incentiva la lectura.
indagar|in-da-gar|Investigar para llegar a saber algo.|indago|indaga|indagó|indagará|investigar|-|La policía indaga la causa del incendio.
inscribir|ins-cri-bir|Anotar a alguien en una lista oficial.|inscribo|inscribe|inscribió|inscribirá|matricular|-|Inscribió a su hermana en el taller.
insistir|in-sis-tir|Repetir algo con firmeza para lograrlo.|insisto|insiste|insistió|insistirá|persistir|desistir|Insistió hasta que la escucharon.
inspirar|ins-pi-rar|Despertar una idea o un sentimiento.|inspiro|inspira|inspiró|inspirará|motivar|-|El paisaje inspiró su poema.
instaurar|ins-tau-rar|Establecer algo nuevo.|instauro|instaura|instauró|instaurará|establecer|-|Instauraron un nuevo reglamento.
interrumpir|in-te-rrum-pir|Cortar la continuidad de algo.|interrumpo|interrumpe|interrumpió|interrumpirá|detener|continuar|Interrumpió la clase con una pregunta.
intuir|in-tuir|Sentir o saber algo sin razonarlo.|intuyo|intuye|intuyó|intuirá|presentir|-|Intuyó que algo andaba mal.
inundar|i-nun-dar|Cubrir de agua un lugar.|inundo|inunda|inundó|inundará|anegar|-|El río inundó el campo.
merecer|me-re-cer|Ser digno de recibir algo.|merezco|merece|mereció|merecerá|ameritar|-|Mereces un descanso.
mitigar|mi-ti-gar|Hacer menos fuerte un daño o un dolor.|mitigo|mitiga|mitigó|mitigará|atenuar|agravar|Los árboles mitigan el calor.
optar|op-tar|Elegir entre varias posibilidades.|opto|opta|optó|optará|escoger|-|Optó por el camino más corto.
originar|o-ri-gi-nar|Dar comienzo a algo.|origino|origina|originó|originará|causar|-|El cortocircuito originó el incendio.
padecer|pa-de-cer|Sufrir una enfermedad o un daño.|padezco|padece|padeció|padecerá|sufrir|-|Padece de alergia al polen.
preservar|pre-ser-var|Proteger algo para que no se dañe.|preservo|preserva|preservó|preservará|conservar|destruir|Preservan el bosque nativo.
procurar|pro-cu-rar|Hacer lo posible para conseguir algo.|procuro|procura|procuró|procurará|intentar|-|Procura llegar temprano.
profundizar|pro-fun-di-zar|Estudiar algo con más detalle.|profundizo|profundiza|profundizó|profundizará|ahondar|-|Profundizó en el tema del agua.
proveer|pro-ve-er|Dar lo que hace falta.|proveo|provee|proveyó|proveerá|abastecer|-|El río provee agua al valle.
provocar|pro-vo-car|Causar algo o hacer que alguien reaccione.|provoco|provoca|provocó|provocará|causar|evitar|El viento provocó una caída de árboles.
reafirmar|re-a-fir-mar|Afirmar de nuevo con más fuerza.|reafirmo|reafirma|reafirmó|reafirmará|ratificar|-|Reafirmó su compromiso con el curso.
rectificar|rec-ti-fi-car|Corregir algo equivocado.|rectifico|rectifica|rectificó|rectificará|enmendar|-|Rectificó su respuesta.
renovar|re-no-var|Cambiar algo viejo por algo nuevo.|renuevo|renueva|renovó|renovará|restaurar|-|Renovaron el carné de la biblioteca.
repercutir|re-per-cu-tir|Tener efecto en algo.|repercuto|repercute|repercutió|repercutirá|afectar|-|El alza del precio repercute en todos.
reprimir|re-pri-mir|Contener un impulso o impedir que algo se exprese.|reprimo|reprime|reprimió|reprimirá|contener|liberar|Reprimió las ganas de reír.
requerir|re-que-rir|Necesitar algo.|requiero|requiere|requirió|requerirá|necesitar|-|Este trabajo requiere paciencia.
resguardar|res-guar-dar|Proteger algo de un daño o un peligro.|resguardo|resguarda|resguardó|resguardará|proteger|exponer|Se resguardó de la lluvia bajo el techo.
restringir|res-trin-gir|Limitar algo dentro de ciertos márgenes.|restrinjo|restringe|restringió|restringirá|limitar|permitir|Restringieron el acceso a la zona.
resultar|re-sul-tar|Acabar siendo de cierta manera.|resulto|resulta|resultó|resultará|salir|-|El experimento resultó bien.
retomar|re-to-mar|Volver a empezar algo que se había dejado.|retomo|retoma|retomó|retomará|reanudar|abandonar|Retomó sus estudios en marzo.
revertir|re-ver-tir|Volver algo a su estado anterior.|revierto|revierte|revirtió|revertirá|invertir|-|Quieren revertir el daño al río.
sancionar|san-cio-nar|Aplicar un castigo por no cumplir una norma.|sanciono|sanciona|sancionó|sancionará|castigar|premiar|Sancionaron al club por el incidente.
satisfacer|sa-tis-fa-cer|Dar lo que se necesita o desea.|satisfago|satisface|satisfizo|satisfará|complacer|frustrar|El resultado satisfizo a todos.
solicitar|so-li-ci-tar|Pedir algo de manera formal.|solicito|solicita|solicitó|solicitará|pedir|-|Solicitó una beca.
soportar|so-por-tar|Aguantar un peso o una situación difícil.|soporto|soporta|soportó|soportará|aguantar|-|El puente soporta mucho peso.
sumergir|su-mer-gir|Meter algo por completo dentro de un líquido.|sumerjo|sumerge|sumergió|sumergirá|hundir|emerger|Sumergió el pan en la sopa.
sustentar|sus-ten-tar|Apoyar algo para que se mantenga.|sustento|sustenta|sustentó|sustentará|respaldar|-|Datos sólidos sustentan la teoría.
tergiversar|ter-gi-ver-sar|Cambiar el sentido de lo que se dijo.|tergiverso|tergiversa|tergiversó|tergiversará|distorsionar|-|El titular tergiversó sus palabras.
transcurrir|trans-cu-rrir|Pasar el tiempo.|transcurro|transcurre|transcurrió|transcurrirá|pasar|-|Transcurrió una hora sin noticias.
trascender|tras-cen-der|Ir más allá de un límite o tener consecuencias duraderas.|trasciendo|trasciende|trascendió|trascenderá|perdurar|-|Su obra trascendió su época.
vincular|vin-cu-lar|Unir o relacionar una cosa con otra.|vinculo|vincula|vinculó|vinculará|relacionar|desvincular|Vincula las ideas del texto.
introducir|in-tro-du-cir|Meter algo dentro de otra cosa o presentar algo nuevo.|introduzco|introduce|introdujo|introducirá|insertar|extraer|Introdujo la tarjeta en la ranura.
retener|re-te-ner|Conservar algo sin dejarlo ir.|retengo|retiene|retuvo|retendrá|guardar|soltar|La esponja retiene agua.
convenir|con-ve-nir|Ser adecuado o acordar algo.|convengo|conviene|convino|convendrá|acordar|-|Conviene salir temprano.
perseguir|per-se-guir|Ir tras algo o alguien para alcanzarlo.|persigo|persigue|persiguió|perseguirá|acosar|huir|El perro persiguió la pelota.
"""
