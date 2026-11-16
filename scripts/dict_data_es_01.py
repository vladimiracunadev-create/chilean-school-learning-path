"""Diccionario de español de 1.º básico: palabras (sustantivos, adjetivos, adverbios y palabras de enlace) y verbos.

Formato de PALABRAS (una por línea, separado por «|»):
    palabra|sílabas|clase|significado|sinónimos|antónimos|ejemplo|tema
Formato de VERBOS:
    infinitivo|sílabas|significado|yo (hoy)|él o ella (hoy)|él o ella (ayer)|él o ella (mañana)|sinónimos|antónimos|ejemplo
Un guion «-» significa que no hay sinónimo o antónimo sencillo para ese nivel.
Textos propios del proyecto: no copian ningún diccionario publicado.
"""

NIVEL = "1-basico"
IDIOMA = "es"

PALABRAS = """
mamá|ma-má|sustantivo femenino|Mujer que tiene un hijo o una hija.|madre|-|Mi mamá me lee un cuento.|familia
papá|pa-pá|sustantivo masculino|Hombre que tiene un hijo o una hija.|padre|-|Mi papá cocina los domingos.|familia
hermano|her-ma-no|sustantivo masculino|Niño que tiene los mismos padres que tú.|-|-|Mi hermano juega a la pelota.|familia
hermana|her-ma-na|sustantivo femenino|Niña que tiene los mismos padres que tú.|-|-|Mi hermana dibuja flores.|familia
abuelo|a-bue-lo|sustantivo masculino|Papá de tu mamá o de tu papá.|-|nieto|Mi abuelo cuenta historias.|familia
abuela|a-bue-la|sustantivo femenino|Mamá de tu mamá o de tu papá.|-|nieta|Mi abuela teje una bufanda.|familia
tío|tí-o|sustantivo masculino|Hermano de tu mamá o de tu papá.|-|-|Mi tío viene de visita.|familia
tía|tí-a|sustantivo femenino|Hermana de tu mamá o de tu papá.|-|-|Mi tía trae pan.|familia
primo|pri-mo|sustantivo masculino|Hijo de tu tío o de tu tía.|-|-|Mi primo vive en otra ciudad.|familia
bebé|be-bé|sustantivo masculino|Niño muy pequeño que todavía no habla ni camina.|guagua|-|El bebé duerme en la cuna.|familia
familia|fa-mi-lia|sustantivo femenino|Grupo de personas que viven juntas o están unidas por el cariño y el parentesco.|-|-|Mi familia es grande.|familia
amigo|a-mi-go|sustantivo masculino|Persona a la que quieres y con la que te gusta estar.|compañero|enemigo|Mi amigo me prestó un lápiz.|familia
niño|ni-ño|sustantivo masculino|Persona que todavía es pequeña.|chico|adulto|El niño salta la cuerda.|familia
niña|ni-ña|sustantivo femenino|Mujer que todavía es pequeña.|chica|adulta|La niña canta una canción.|familia
profesora|pro-fe-so-ra|sustantivo femenino|Mujer que enseña en el colegio.|maestra|alumna|La profesora escribe en la pizarra.|escuela
profesor|pro-fe-sor|sustantivo masculino|Hombre que enseña en el colegio.|maestro|alumno|El profesor nos enseña a leer.|escuela
cabeza|ca-be-za|sustantivo femenino|Parte de arriba del cuerpo, donde están la cara y el cerebro.|-|pies|Me puse el gorro en la cabeza.|cuerpo
cara|ca-ra|sustantivo femenino|Parte delantera de la cabeza, con los ojos, la nariz y la boca.|rostro|-|Me lavé la cara.|cuerpo
ojo|o-jo|sustantivo masculino|Parte de la cara con la que vemos.|-|-|Cierro los ojos para dormir.|cuerpo
nariz|na-riz|sustantivo femenino|Parte de la cara con la que olemos.|-|-|Huelo la flor con la nariz.|cuerpo
boca|bo-ca|sustantivo femenino|Parte de la cara con la que hablamos y comemos.|-|-|Abro la boca para comer.|cuerpo
diente|dien-te|sustantivo masculino|Pieza dura de la boca que sirve para morder.|-|-|Me cepillo los dientes.|cuerpo
oreja|o-re-ja|sustantivo femenino|Parte de la cabeza con la que oímos.|-|-|Me tapo la oreja con la mano.|cuerpo
pelo|pe-lo|sustantivo masculino|Hilos finos que crecen en la cabeza.|cabello|-|Mi pelo es largo.|cuerpo
mano|ma-no|sustantivo femenino|Parte del cuerpo con cinco dedos que usamos para agarrar.|-|-|Levanto la mano para pedir la palabra.|cuerpo
dedo|de-do|sustantivo masculino|Cada una de las partes alargadas de la mano o del pie.|-|-|Tengo cinco dedos en cada mano.|cuerpo
brazo|bra-zo|sustantivo masculino|Parte del cuerpo que va desde el hombro hasta la mano.|-|-|Abrazo a mi mamá con los brazos.|cuerpo
pierna|pier-na|sustantivo femenino|Parte del cuerpo que va desde la cadera hasta el pie.|-|-|Me duele la pierna.|cuerpo
pie|pie|sustantivo masculino|Parte del cuerpo donde terminan las piernas y con la que caminamos.|-|cabeza|Me duelen los pies.|cuerpo
barriga|ba-rri-ga|sustantivo femenino|Parte del cuerpo donde está el estómago.|guata|espalda|Me duele la barriga.|cuerpo
espalda|es-pal-da|sustantivo femenino|Parte de atrás del cuerpo.|-|pecho|Llevo la mochila en la espalda.|cuerpo
corazón|co-ra-zón|sustantivo masculino|Órgano que late y mueve la sangre por el cuerpo.|-|-|Mi corazón late rápido.|cuerpo
casa|ca-sa|sustantivo femenino|Lugar donde vive una familia.|hogar|-|Mi casa tiene un jardín.|casa
puerta|puer-ta|sustantivo femenino|Pieza que se abre y se cierra para entrar o salir.|-|-|Cierro la puerta con cuidado.|casa
ventana|ven-ta-na|sustantivo femenino|Abertura en la pared por donde entra la luz.|-|-|Miro la lluvia por la ventana.|casa
cama|ca-ma|sustantivo femenino|Mueble donde dormimos.|-|-|Me acuesto en mi cama.|casa
mesa|me-sa|sustantivo femenino|Mueble con patas y una tabla plana para comer o trabajar.|-|-|Pongo el plato en la mesa.|casa
silla|si-lla|sustantivo femenino|Mueble con respaldo donde nos sentamos.|asiento|-|Me siento en la silla.|casa
cocina|co-ci-na|sustantivo femenino|Lugar de la casa donde se prepara la comida.|-|-|Mamá cocina en la cocina.|casa
baño|ba-ño|sustantivo masculino|Lugar de la casa donde nos lavamos.|-|-|Me lavo las manos en el baño.|casa
techo|te-cho|sustantivo masculino|Parte de arriba de una pieza o de una casa.|-|suelo|Una lámpara cuelga del techo.|casa
pared|pa-red|sustantivo femenino|Muro que forma los lados de una pieza.|muro|-|Colgué un dibujo en la pared.|casa
suelo|sue-lo|sustantivo masculino|Superficie sobre la que caminamos.|piso|techo|Se me cayó el lápiz al suelo.|casa
llave|lla-ve|sustantivo femenino|Objeto que sirve para abrir una puerta con cerradura.|-|-|Mi mamá guarda la llave.|casa
cuchara|cu-cha-ra|sustantivo femenino|Cubierto que usamos para tomar la sopa.|-|-|Tomo la sopa con la cuchara.|casa
plato|pla-to|sustantivo masculino|Recipiente plano donde se pone la comida.|-|-|El plato está lleno de arroz.|casa
vaso|va-so|sustantivo masculino|Recipiente para tomar líquidos.|-|-|Bebo agua en un vaso.|casa
cepillo|ce-pi-llo|sustantivo masculino|Objeto con cerdas para limpiar los dientes o peinar.|-|-|Uso el cepillo para lavarme los dientes.|casa
jabón|ja-bón|sustantivo masculino|Producto con el que nos lavamos para quedar limpios.|-|-|Me lavo las manos con jabón.|casa
toalla|to-a-lla|sustantivo femenino|Tela suave para secarse.|-|-|Me seco con la toalla.|casa
escuela|es-cue-la|sustantivo femenino|Lugar donde los niños aprenden.|colegio|-|Voy a la escuela todos los días.|escuela
colegio|co-le-gio|sustantivo masculino|Lugar donde estudian los niños y los jóvenes.|escuela|-|Mi colegio tiene un patio grande.|escuela
sala|sa-la|sustantivo femenino|Pieza donde se hace la clase.|aula|-|Entramos a la sala.|escuela
pizarra|pi-za-rra|sustantivo femenino|Superficie donde el profesor escribe para toda la clase.|-|-|La profesora escribe en la pizarra.|escuela
lápiz|lá-piz|sustantivo masculino|Objeto de madera con mina para escribir y dibujar.|-|-|Saco punta al lápiz.|escuela
goma|go-ma|sustantivo femenino|Objeto que borra lo que escribimos con lápiz.|-|-|Borro el error con la goma.|escuela
cuaderno|cua-der-no|sustantivo masculino|Conjunto de hojas unidas donde escribimos y dibujamos.|-|-|Escribo mi nombre en el cuaderno.|escuela
libro|li-bro|sustantivo masculino|Conjunto de hojas impresas con historias o información.|-|-|Leo un libro de animales.|escuela
mochila|mo-chi-la|sustantivo femenino|Bolsa que se lleva en la espalda para cargar útiles.|-|-|Guardo el estuche en la mochila.|escuela
estuche|es-tu-che|sustantivo masculino|Cajita donde guardamos lápices y otros útiles.|-|-|Mi estuche tiene colores.|escuela
tijera|ti-je-ra|sustantivo femenino|Herramienta con dos hojas que sirve para cortar papel.|-|-|Corto el papel con la tijera.|escuela
pegamento|pe-ga-men-to|sustantivo masculino|Sustancia que sirve para unir cosas.|cola|-|Pego la hoja con pegamento.|escuela
regla|re-gla|sustantivo femenino|Objeto largo y plano que sirve para trazar líneas rectas.|-|-|Dibujo una línea con la regla.|escuela
hoja|ho-ja|sustantivo femenino|Trozo delgado de papel; también cada parte verde y plana de una planta.|-|-|Escribo en una hoja blanca.|escuela
dibujo|di-bu-jo|sustantivo masculino|Figura que hacemos con lápices o pinturas.|-|-|Hice un dibujo de mi casa.|escuela
patio|pa-tio|sustantivo masculino|Espacio abierto del colegio o de la casa donde se juega.|-|-|Jugamos en el patio.|escuela
recreo|re-cre-o|sustantivo masculino|Tiempo para descansar y jugar entre clases.|descanso|clase|En el recreo corremos.|escuela
clase|cla-se|sustantivo femenino|Tiempo en que el profesor enseña a los alumnos.|lección|recreo|La clase empieza a las ocho.|escuela
compañero|com-pa-ñe-ro|sustantivo masculino|Persona que estudia contigo en el mismo curso.|amigo|-|Mi compañero me ayudó.|escuela
nombre|nom-bre|sustantivo masculino|Palabra con la que llamamos a una persona, animal o cosa.|-|-|Escribo mi nombre arriba de la hoja.|escuela
letra|le-tra|sustantivo femenino|Cada signo que usamos para escribir.|-|-|La «a» es la primera letra.|escuela
sílaba|sí-la-ba|sustantivo femenino|Cada golpe de voz con que se divide una palabra.|-|-|«Ca-sa» tiene dos sílabas.|escuela
palabra|pa-la-bra|sustantivo femenino|Conjunto de letras que tiene un significado.|-|-|«Sol» es una palabra corta.|escuela
oración|o-ra-ción|sustantivo femenino|Conjunto de palabras que dice algo completo.|frase|-|«El gato duerme» es una oración.|escuela
cuento|cuen-to|sustantivo masculino|Historia corta inventada.|relato|-|Mi abuela me cuenta un cuento.|escuela
canción|can-ción|sustantivo femenino|Texto que se canta con música.|-|-|Aprendimos una canción nueva.|escuela
número|nú-me-ro|sustantivo masculino|Signo que nos dice cuántos hay.|cifra|-|El número 5 viene después del 4.|escuela
perro|pe-rro|sustantivo masculino|Animal doméstico que ladra.|-|-|Mi perro mueve la cola.|animales
gato|ga-to|sustantivo masculino|Animal doméstico que maúlla.|-|-|El gato duerme en el sillón.|animales
pájaro|pá-ja-ro|sustantivo masculino|Animal con plumas y alas que suele volar.|ave|-|El pájaro canta en el árbol.|animales
pez|pez|sustantivo masculino|Animal que vive en el agua y respira por branquias.|-|-|El pez nada en la pecera.|animales
caballo|ca-ba-llo|sustantivo masculino|Animal grande que se puede montar y corre rápido.|-|-|El caballo galopa por el campo.|animales
vaca|va-ca|sustantivo femenino|Animal de granja que da leche.|-|-|La vaca come pasto.|animales
oveja|o-ve-ja|sustantivo femenino|Animal de granja cuya lana sirve para hacer ropa.|-|-|La oveja tiene lana blanca.|animales
gallina|ga-lli-na|sustantivo femenino|Ave de granja que pone huevos.|-|gallo|La gallina puso un huevo.|animales
pato|pa-to|sustantivo masculino|Ave que nada en lagunas y camina balanceándose.|-|-|El pato nada en la laguna.|animales
cerdo|cer-do|sustantivo masculino|Animal de granja de cuerpo gordo y hocico chato.|chancho|-|El cerdo come en el corral.|animales
conejo|co-ne-jo|sustantivo masculino|Animal pequeño de orejas largas que salta.|-|-|El conejo come zanahorias.|animales
ratón|ra-tón|sustantivo masculino|Animal pequeño de cola larga.|-|-|El ratón se escondió en su cueva.|animales
león|le-ón|sustantivo masculino|Animal salvaje de gran melena que vive en la sabana.|-|-|El león ruge fuerte.|animales
elefante|e-le-fan-te|sustantivo masculino|Animal enorme con trompa y orejas grandes.|-|-|El elefante toma agua con la trompa.|animales
mono|mo-no|sustantivo masculino|Animal que trepa y tiene cola y manos hábiles.|-|-|El mono come un plátano.|animales
tortuga|tor-tu-ga|sustantivo femenino|Animal lento que lleva un caparazón en la espalda.|-|-|La tortuga camina despacio.|animales
mariposa|ma-ri-po-sa|sustantivo femenino|Insecto de alas coloridas.|-|-|La mariposa se posó en una flor.|animales
abeja|a-be-ja|sustantivo femenino|Insecto que hace miel.|-|-|La abeja visita las flores.|animales
hormiga|hor-mi-ga|sustantivo femenino|Insecto muy pequeño que vive en grupo bajo la tierra.|-|-|Las hormigas cargan comida.|animales
araña|a-ra-ña|sustantivo femenino|Animal de ocho patas que teje redes.|-|-|La araña teje su tela.|animales
rana|ra-na|sustantivo femenino|Animal pequeño que salta y vive cerca del agua.|-|-|La rana croa en la noche.|animales
pan|pan|sustantivo masculino|Alimento que se hace con harina y se hornea.|-|-|Como pan con mantequilla.|comida
leche|le-che|sustantivo femenino|Líquido blanco que dan las vacas y otros animales.|-|-|Tomo leche en el desayuno.|comida
agua|a-gua|sustantivo femenino|Líquido transparente sin sabor que bebemos.|-|-|Bebo agua después de correr.|comida
huevo|hue-vo|sustantivo masculino|Alimento redondeado que ponen las gallinas.|-|-|Comí un huevo cocido.|comida
queso|que-so|sustantivo masculino|Alimento que se hace con leche cuajada.|-|-|Pongo queso en el pan.|comida
arroz|a-rroz|sustantivo masculino|Cereal en granos blancos que se cocina.|-|-|Almorcé arroz con pollo.|comida
sopa|so-pa|sustantivo femenino|Comida líquida caliente con verduras o fideos.|caldo|-|La sopa está caliente.|comida
fruta|fru-ta|sustantivo femenino|Alimento dulce que crece en árboles y plantas.|-|-|La fruta es sana.|comida
manzana|man-za-na|sustantivo femenino|Fruta redonda de piel roja o verde.|-|-|Me comí una manzana.|comida
plátano|plá-ta-no|sustantivo masculino|Fruta alargada de cáscara amarilla.|banana|-|El mono come un plátano.|comida
naranja|na-ran-ja|sustantivo femenino|Fruta redonda de color naranja y jugosa.|-|-|Tomé jugo de naranja.|comida
uva|u-va|sustantivo femenino|Fruta pequeña y redonda que crece en racimos.|-|-|Las uvas son dulces.|comida
sandía|san-dí-a|sustantivo femenino|Fruta grande, verde por fuera y roja por dentro.|-|-|La sandía refresca en verano.|comida
frutilla|fru-ti-lla|sustantivo femenino|Fruta pequeña, roja y dulce.|fresa|-|Me gustan las frutillas con crema.|comida
verdura|ver-du-ra|sustantivo femenino|Planta que se come, como la lechuga o la zanahoria.|hortaliza|-|Como verduras todos los días.|comida
zanahoria|za-na-ho-ria|sustantivo femenino|Verdura anaranjada que crece bajo la tierra.|-|-|El conejo come una zanahoria.|comida
papa|pa-pa|sustantivo femenino|Tubérculo que crece bajo la tierra y se cocina.|patata|-|Comí papas fritas.|comida
tomate|to-ma-te|sustantivo masculino|Fruto rojo y redondo que se usa en ensaladas.|-|-|Pongo tomate en la ensalada.|comida
carne|car-ne|sustantivo femenino|Parte del cuerpo de los animales que se come.|-|-|Mi papá asó carne.|comida
pollo|po-llo|sustantivo masculino|Ave de granja que se come; cría de la gallina.|-|-|El pollo está rico.|comida
pescado|pes-ca-do|sustantivo masculino|Pez que se cocina para comer.|-|-|Comimos pescado con arroz.|comida
helado|he-la-do|sustantivo masculino|Postre dulce muy frío.|-|-|Me comí un helado de frutilla.|comida
galleta|ga-lle-ta|sustantivo femenino|Dulce pequeño, seco y crujiente.|-|-|Mojo la galleta en la leche.|comida
jugo|ju-go|sustantivo masculino|Líquido que sale de las frutas.|zumo|-|Tomo jugo de naranja.|comida
desayuno|de-sa-yu-no|sustantivo masculino|Primera comida del día.|-|cena|En el desayuno tomo leche.|comida
almuerzo|al-muer-zo|sustantivo masculino|Comida del mediodía.|-|-|El almuerzo es a la una.|comida
cena|ce-na|sustantivo femenino|Última comida del día.|once|desayuno|La cena es en la noche.|comida
rojo|ro-jo|adjetivo|Color de la sangre y de la frutilla.|colorado|-|El tomate es rojo.|colores
azul|a-zul|adjetivo|Color del cielo despejado.|-|-|El mar es azul.|colores
amarillo|a-ma-ri-llo|adjetivo|Color del sol y del plátano.|-|-|El pollito es amarillo.|colores
verde|ver-de|adjetivo|Color de las hojas.|-|-|El pasto es verde.|colores
negro|ne-gro|adjetivo|Color de la noche muy oscura.|-|blanco|El carbón es negro.|colores
blanco|blan-co|adjetivo|Color de la nieve y de la leche.|-|negro|La nieve es blanca.|colores
café|ca-fé|adjetivo|Color de la tierra y del chocolate.|marrón|-|El oso es café.|colores
naranja|na-ran-ja|adjetivo|Color entre el rojo y el amarillo.|anaranjado|-|La zanahoria es naranja.|colores
rosado|ro-sa-do|adjetivo|Color suave entre el rojo y el blanco.|rosa|-|La flor es rosada.|colores
morado|mo-ra-do|adjetivo|Color de la uva oscura.|violeta|-|El jugo de uva es morado.|colores
gris|gris|adjetivo|Color de las nubes de lluvia.|-|-|El elefante es gris.|colores
uno|u-no|numeral|El número 1.|-|-|Tengo un lápiz, uno solo.|números
dos|dos|numeral|El número 2.|par|-|Tengo dos manos.|números
tres|tres|numeral|El número 3.|-|-|Tengo tres amigos en el curso.|números
cuatro|cua-tro|numeral|El número 4.|-|-|Un gato tiene cuatro patas.|números
cinco|cin-co|numeral|El número 5.|-|-|Una mano tiene cinco dedos.|números
seis|seis|numeral|El número 6.|-|-|Compré seis huevos.|números
siete|sie-te|numeral|El número 7.|-|-|La semana tiene siete días.|números
ocho|o-cho|numeral|El número 8.|-|-|Una araña tiene ocho patas.|números
nueve|nue-ve|numeral|El número 9.|-|-|Tengo nueve lápices.|números
diez|diez|numeral|El número 10.|-|-|Tengo diez dedos.|números
primero|pri-me-ro|numeral|El que va antes que todos los demás.|-|último|Llegué primero a la fila.|números
último|úl-ti-mo|adjetivo|El que va después de todos los demás.|final|primero|Soy el último de la fila.|números
mitad|mi-tad|sustantivo femenino|Cada una de las dos partes iguales de algo.|-|-|Comí la mitad de la manzana.|números
sol|sol|sustantivo masculino|Estrella que nos da luz y calor.|-|luna|El sol sale en la mañana.|naturaleza
luna|lu-na|sustantivo femenino|Astro que vemos brillar de noche.|-|sol|La luna sale en la noche.|naturaleza
estrella|es-tre-lla|sustantivo femenino|Punto brillante que se ve en el cielo de noche.|-|-|Conté estrellas en el cielo.|naturaleza
cielo|cie-lo|sustantivo masculino|Espacio que vemos sobre nosotros.|-|tierra|El cielo está azul.|naturaleza
nube|nu-be|sustantivo femenino|Masa blanca o gris de gotitas de agua en el cielo.|-|-|Una nube tapó el sol.|naturaleza
lluvia|llu-via|sustantivo femenino|Agua que cae de las nubes.|-|sequía|La lluvia moja el patio.|naturaleza
viento|vien-to|sustantivo masculino|Aire que se mueve.|-|-|El viento movió las hojas.|naturaleza
nieve|nie-ve|sustantivo femenino|Agua helada que cae en copos blancos.|-|-|Hay nieve en la montaña.|naturaleza
árbol|ár-bol|sustantivo masculino|Planta grande con tronco, ramas y hojas.|-|-|El pájaro está en el árbol.|naturaleza
flor|flor|sustantivo femenino|Parte colorida de una planta.|-|-|Regalé una flor a mi mamá.|naturaleza
planta|plan-ta|sustantivo femenino|Ser vivo que crece en la tierra y tiene raíces.|-|-|Riego mi planta.|naturaleza
pasto|pas-to|sustantivo masculino|Hierba baja y verde que cubre el suelo.|césped|-|Me siento en el pasto.|naturaleza
tierra|tie-rra|sustantivo femenino|Suelo donde crecen las plantas; también nuestro planeta.|suelo|cielo|Las semillas están en la tierra.|naturaleza
piedra|pie-dra|sustantivo femenino|Trozo duro de roca.|roca|-|Encontré una piedra lisa.|naturaleza
río|rí-o|sustantivo masculino|Agua que corre desde la montaña hacia el mar.|-|-|El río lleva agua clara.|naturaleza
mar|mar|sustantivo masculino|Gran extensión de agua salada.|océano|-|Me baño en el mar.|naturaleza
playa|pla-ya|sustantivo femenino|Orilla del mar cubierta de arena.|-|-|Hacemos castillos en la playa.|naturaleza
montaña|mon-ta-ña|sustantivo femenino|Elevación muy alta del terreno.|monte|llano|Subimos la montaña.|naturaleza
arena|a-re-na|sustantivo femenino|Granitos muy pequeños de roca que hay en la playa.|-|-|Juego con la arena.|naturaleza
semilla|se-mi-lla|sustantivo femenino|Parte de la planta de donde nace otra planta.|-|-|De una semilla crece un árbol.|naturaleza
día|dí-a|sustantivo masculino|Tiempo en que hay luz del sol; también las veinticuatro horas.|-|noche|Hoy es un día lindo.|tiempo
noche|no-che|sustantivo femenino|Tiempo en que no hay luz del sol.|-|día|En la noche me duermo.|tiempo
mañana|ma-ña-na|sustantivo femenino|Primeras horas del día.|-|tarde|En la mañana desayuno.|tiempo
tarde|tar-de|sustantivo femenino|Horas del día después del mediodía.|-|mañana|En la tarde hago mis tareas.|tiempo
semana|se-ma-na|sustantivo femenino|Siete días seguidos.|-|-|La semana empieza el lunes.|tiempo
mes|mes|sustantivo masculino|Periodo de unas cuatro semanas.|-|-|Mi cumpleaños es este mes.|tiempo
año|a-ño|sustantivo masculino|Periodo de doce meses.|-|-|Un año tiene doce meses.|tiempo
hoy|hoy|adverbio|En este día.|-|ayer|Hoy voy al colegio.|tiempo
ayer|a-yer|adverbio|En el día anterior a hoy.|-|mañana|Ayer jugué en el parque.|tiempo
lunes|lu-nes|sustantivo masculino|Primer día de la semana escolar.|-|-|El lunes vuelvo a clases.|tiempo
martes|mar-tes|sustantivo masculino|Día que viene después del lunes.|-|-|El martes tengo Música.|tiempo
miércoles|miér-co-les|sustantivo masculino|Día que viene después del martes.|-|-|El miércoles hay Educación Física.|tiempo
jueves|jue-ves|sustantivo masculino|Día que viene después del miércoles.|-|-|El jueves leemos en la biblioteca.|tiempo
viernes|vier-nes|sustantivo masculino|Último día de clases de la semana.|-|-|El viernes termina la semana.|tiempo
sábado|sá-ba-do|sustantivo masculino|Día de descanso que sigue al viernes.|-|-|El sábado juego con mis primos.|tiempo
domingo|do-min-go|sustantivo masculino|Último día de la semana.|-|-|El domingo almorzamos en familia.|tiempo
calle|ca-lle|sustantivo femenino|Camino de una ciudad por donde pasan personas y autos.|-|-|Miro a ambos lados antes de cruzar la calle.|lugares
ciudad|ciu-dad|sustantivo femenino|Lugar grande con muchas casas, calles y edificios.|-|campo|Vivo en una ciudad.|lugares
campo|cam-po|sustantivo masculino|Lugar abierto fuera de la ciudad, con plantas y animales.|-|ciudad|En el campo hay vacas.|lugares
parque|par-que|sustantivo masculino|Lugar con árboles y juegos para pasear.|plaza|-|Jugamos en el parque.|lugares
plaza|pla-za|sustantivo femenino|Espacio abierto en la ciudad donde la gente pasea.|parque|-|Hay una fuente en la plaza.|lugares
tienda|tien-da|sustantivo femenino|Lugar donde se venden cosas.|negocio|-|Compré pan en la tienda.|lugares
hospital|hos-pi-tal|sustantivo masculino|Lugar donde se cuida a los enfermos.|-|-|El doctor trabaja en el hospital.|lugares
biblioteca|bi-blio-te-ca|sustantivo femenino|Lugar donde se guardan libros para leer o pedir prestados.|-|-|Pedí un libro en la biblioteca.|lugares
iglesia|i-gle-sia|sustantivo femenino|Edificio donde se reúnen quienes tienen una religión cristiana.|-|-|La iglesia tiene una campana.|lugares
auto|au-to|sustantivo masculino|Vehículo con cuatro ruedas para viajar por la calle.|coche|-|Papá maneja el auto.|lugares
bus|bus|sustantivo masculino|Vehículo grande que lleva muchas personas.|micro|-|Voy al colegio en bus.|lugares
bicicleta|bi-ci-cle-ta|sustantivo femenino|Vehículo de dos ruedas que se mueve con pedales.|-|-|Paseo en bicicleta.|lugares
tren|tren|sustantivo masculino|Vehículo que va sobre rieles y tiene muchos carros.|-|-|El tren pasa por el puente.|lugares
barco|bar-co|sustantivo masculino|Vehículo que viaja por el agua.|bote|-|El barco navega por el mar.|lugares
avión|a-vión|sustantivo masculino|Vehículo que vuela por el aire.|-|-|El avión vuela alto.|lugares
polera|po-le-ra|sustantivo femenino|Prenda de vestir para la parte de arriba del cuerpo.|camiseta|-|Me puse una polera azul.|ropa
pantalón|pan-ta-lón|sustantivo masculino|Prenda que cubre las piernas.|-|-|Mi pantalón es largo.|ropa
falda|fal-da|sustantivo femenino|Prenda que cubre desde la cintura hacia abajo.|-|-|Mi hermana usa una falda.|ropa
zapato|za-pa-to|sustantivo masculino|Calzado que cubre el pie.|-|-|Me amarro los zapatos.|ropa
calcetín|cal-ce-tín|sustantivo masculino|Prenda que cubre el pie por dentro del zapato.|media|-|Perdí un calcetín.|ropa
gorro|go-rro|sustantivo masculino|Prenda que cubre la cabeza.|-|-|Me pongo el gorro cuando hace frío.|ropa
abrigo|a-bri-go|sustantivo masculino|Prenda gruesa que da calor.|-|-|Uso abrigo en invierno.|ropa
chaleco|cha-le-co|sustantivo masculino|Prenda sin mangas que se usa sobre la camisa o la polera.|-|-|Mi chaleco del colegio es azul.|ropa
pelota|pe-lo-ta|sustantivo femenino|Objeto redondo que se usa para jugar.|balón|-|Pateo la pelota.|juegos
juego|jue-go|sustantivo masculino|Actividad que hacemos para divertirnos.|-|-|Mi juego favorito es el luche.|juegos
juguete|ju-gue-te|sustantivo masculino|Objeto con el que juegan los niños.|-|-|Guardo mis juguetes.|juegos
muñeca|mu-ñe-ca|sustantivo femenino|Juguete con forma de persona.|-|-|Mi muñeca tiene pelo largo.|juegos
globo|glo-bo|sustantivo masculino|Bolsa de goma que se infla con aire.|-|-|El globo subió al cielo.|juegos
cometa|co-me-ta|sustantivo femenino|Juguete de papel que vuela con el viento.|volantín|-|La cometa vuela alto.|juegos
alegre|a-le-gre|adjetivo|Que siente o muestra felicidad.|contento|triste|Estoy alegre porque es mi cumpleaños.|sentimientos
triste|tris-te|adjetivo|Que siente pena.|apenado|alegre|Estoy triste porque perdí mi juguete.|sentimientos
enojado|e-no-ja-do|adjetivo|Que siente rabia.|molesto|contento|Mi hermano está enojado.|sentimientos
asustado|a-sus-ta-do|adjetivo|Que siente miedo.|temeroso|valiente|El gato quedó asustado por el trueno.|sentimientos
cansado|can-sa-do|adjetivo|Que necesita descansar.|agotado|descansado|Estoy cansado después de correr.|sentimientos
feliz|fe-liz|adjetivo|Que se siente muy bien y con alegría.|contento|infeliz|Soy feliz con mi familia.|sentimientos
miedo|mie-do|sustantivo masculino|Sensación que sentimos ante algo que nos asusta.|temor|valentía|Tengo miedo de la oscuridad.|sentimientos
cariño|ca-ri-ño|sustantivo masculino|Sentimiento bueno que tenemos por alguien.|afecto|odio|Doy cariño a mi perro.|sentimientos
grande|gran-de|adjetivo|De tamaño mayor que lo normal.|enorme|pequeño|El elefante es grande.|cualidades
pequeño|pe-que-ño|adjetivo|De tamaño menor que lo normal.|chico|grande|La hormiga es pequeña.|cualidades
largo|lar-go|adjetivo|Que tiene mucha distancia de un extremo a otro.|extenso|corto|La cuerda es larga.|cualidades
corto|cor-to|adjetivo|Que tiene poca distancia de un extremo a otro.|breve|largo|Mi lápiz quedó corto.|cualidades
alto|al-to|adjetivo|Que llega muy arriba.|elevado|bajo|El árbol es alto.|cualidades
bajo|ba-jo|adjetivo|Que llega poco arriba.|chico|alto|La mesa es baja.|cualidades
gordo|gor-do|adjetivo|Que tiene mucho grosor.|grueso|delgado|El libro es gordo.|cualidades
delgado|del-ga-do|adjetivo|Que tiene poco grosor.|fino|gordo|El lápiz es delgado.|cualidades
pesado|pe-sa-do|adjetivo|Que pesa mucho.|-|liviano|La mochila está pesada.|cualidades
liviano|li-via-no|adjetivo|Que pesa poco.|ligero|pesado|La pluma es liviana.|cualidades
rápido|rá-pi-do|adjetivo|Que se mueve o hace algo en poco tiempo.|veloz|lento|El conejo es rápido.|cualidades
lento|len-to|adjetivo|Que se mueve o hace algo en mucho tiempo.|pausado|rápido|La tortuga es lenta.|cualidades
caliente|ca-lien-te|adjetivo|Que tiene temperatura alta.|cálido|frío|La sopa está caliente.|cualidades
frío|frí-o|adjetivo|Que tiene temperatura baja.|helado|caliente|El helado está frío.|cualidades
nuevo|nue-vo|adjetivo|Que se hizo hace poco o no se ha usado.|-|viejo|Estrené zapatos nuevos.|cualidades
viejo|vie-jo|adjetivo|Que tiene muchos años o está muy usado.|antiguo|nuevo|El libro es viejo.|cualidades
limpio|lim-pio|adjetivo|Que no tiene suciedad.|aseado|sucio|Mis manos están limpias.|cualidades
sucio|su-cio|adjetivo|Que tiene suciedad.|manchado|limpio|Mi zapato está sucio.|cualidades
bonito|bo-ni-to|adjetivo|Que gusta al mirarlo.|lindo|feo|Qué bonito dibujo.|cualidades
lindo|lin-do|adjetivo|Que es agradable de ver o de oír.|bonito|feo|La flor es linda.|cualidades
feo|fe-o|adjetivo|Que no resulta agradable de ver.|-|bonito|El monstruo del cuento es feo.|cualidades
bueno|bue-no|adjetivo|Que es como debe ser; que hace bien.|-|malo|Mi amigo es bueno conmigo.|cualidades
malo|ma-lo|adjetivo|Que no es como debe ser; que hace daño.|-|bueno|Mentir es malo.|cualidades
fuerte|fuer-te|adjetivo|Que tiene mucha fuerza.|robusto|débil|El caballo es fuerte.|cualidades
débil|dé-bil|adjetivo|Que tiene poca fuerza.|-|fuerte|Estoy débil porque estuve enfermo.|cualidades
lleno|lle-no|adjetivo|Que no tiene espacio libre porque está ocupado.|-|vacío|El vaso está lleno de agua.|cualidades
vacío|va-cí-o|adjetivo|Que no tiene nada dentro.|-|lleno|La caja está vacía.|cualidades
abierto|a-bier-to|adjetivo|Que deja pasar; no cerrado.|-|cerrado|La puerta está abierta.|cualidades
cerrado|ce-rra-do|adjetivo|Que no deja pasar; no abierto.|-|abierto|La ventana está cerrada.|cualidades
cerca|cer-ca|adverbio|A poca distancia.|-|lejos|Mi casa está cerca del colegio.|lugares
lejos|le-jos|adverbio|A mucha distancia.|-|cerca|La playa queda lejos.|lugares
arriba|a-rri-ba|adverbio|En un lugar más alto.|-|abajo|El pájaro está arriba del árbol.|lugares
abajo|a-ba-jo|adverbio|En un lugar más bajo.|-|arriba|Mi gato duerme abajo de la cama.|lugares
dentro|den-tro|adverbio|En el interior de algo.|-|fuera|Los lápices están dentro del estuche.|lugares
fuera|fue-ra|adverbio|En el exterior de algo.|-|dentro|Los niños juegan fuera de la sala.|lugares
delante|de-lan-te|adverbio|En la parte de adelante.|-|detrás|Me paro delante de la fila.|lugares
detrás|de-trás|adverbio|En la parte de atrás.|-|delante|El gato se escondió detrás del sillón.|lugares
izquierda|iz-quier-da|sustantivo femenino|Lado del cuerpo donde está el corazón.|-|derecha|Escribo con la mano izquierda.|lugares
derecha|de-re-cha|sustantivo femenino|Lado opuesto a la izquierda.|-|izquierda|Doblo a la derecha.|lugares
sí|sí|adverbio|Palabra con la que decimos que estamos de acuerdo.|-|no|Sí, quiero jugar.|palabras de enlace
no|no|adverbio|Palabra con la que decimos que algo no es así o que no queremos.|-|sí|No quiero más sopa.|palabras de enlace
muy|muy|adverbio|Palabra que aumenta una cualidad.|-|poco|El día está muy bonito.|palabras de enlace
mucho|mu-cho|adverbio|En gran cantidad.|-|poco|Como mucho pan.|palabras de enlace
poco|po-co|adverbio|En pequeña cantidad.|-|mucho|Hay poca agua en el vaso.|palabras de enlace
todo|to-do|pronombre|La cantidad completa.|-|nada|Me comí todo el almuerzo.|palabras de enlace
nada|na-da|pronombre|Ninguna cosa.|-|todo|No hay nada en la caja.|palabras de enlace
y|y|conjunción|Palabra que une dos cosas.|-|-|Tengo un perro y un gato.|palabras de enlace
o|o|conjunción|Palabra que da a elegir entre dos cosas.|-|-|¿Quieres leche o jugo?|palabras de enlace
pero|pe-ro|conjunción|Palabra que muestra que algo se opone a lo anterior.|-|-|Quiero salir, pero llueve.|palabras de enlace
porque|por-que|conjunción|Palabra con la que damos una razón.|-|-|Me abrigo porque hace frío.|palabras de enlace
con|con|preposición|Palabra que indica compañía o instrumento.|-|sin|Voy al parque con mi hermano.|palabras de enlace
sin|sin|preposición|Palabra que indica que algo falta.|-|con|Salí sin paraguas.|palabras de enlace
en|en|preposición|Palabra que indica el lugar donde algo está.|-|-|El libro está en la mesa.|palabras de enlace
de|de|preposición|Palabra que indica pertenencia u origen.|-|-|Es el cuaderno de Ana.|palabras de enlace
para|pa-ra|preposición|Palabra que indica el fin de algo.|-|-|El regalo es para ti.|palabras de enlace
el|el|artículo|Palabra que acompaña a un nombre masculino y único.|-|-|El perro ladra.|palabras de enlace
la|la|artículo|Palabra que acompaña a un nombre femenino y único.|-|-|La niña lee.|palabras de enlace
los|los|artículo|Palabra que acompaña a un nombre masculino y plural.|-|-|Los gatos duermen.|palabras de enlace
las|las|artículo|Palabra que acompaña a un nombre femenino y plural.|-|-|Las flores huelen bien.|palabras de enlace
yo|yo|pronombre|Palabra con la que hablo de mí.|-|-|Yo me llamo Pedro.|palabras de enlace
tú|tú|pronombre|Palabra con la que hablo a otra persona.|-|-|Tú juegas conmigo.|palabras de enlace
quién|quién|pronombre|Palabra que usamos para preguntar por una persona.|-|-|¿Quién llegó primero?|palabras de enlace
qué|qué|pronombre|Palabra que usamos para preguntar por una cosa.|-|-|¿Qué estás dibujando?|palabras de enlace
dónde|dón-de|adverbio|Palabra que usamos para preguntar por un lugar.|-|-|¿Dónde está mi mochila?|palabras de enlace
cuándo|cuán-do|adverbio|Palabra que usamos para preguntar por un momento.|-|-|¿Cuándo es el recreo?|palabras de enlace
cómo|có-mo|adverbio|Palabra que usamos para preguntar la manera de hacer algo.|-|-|¿Cómo te llamas?|palabras de enlace
por favor|por fa-vor|expresión|Frase de cortesía para pedir algo con amabilidad.|-|-|¿Me pasas el lápiz, por favor?|cortesía
gracias|gra-cias|expresión|Palabra con la que agradecemos.|-|-|Gracias por ayudarme.|cortesía
perdón|per-dón|expresión|Palabra con la que pedimos disculpas.|disculpa|-|Perdón por empujarte.|cortesía
hola|ho-la|expresión|Palabra con la que saludamos.|-|chao|Hola, buenos días.|cortesía
chao|cha-o|expresión|Palabra con la que nos despedimos.|adiós|hola|Chao, hasta mañana.|cortesía
"""

VERBOS = """
ser|ser|Tener una característica o identidad.|soy|es|fue|será|-|-|Mi gato es negro.
estar|es-tar|Encontrarse en un lugar o en cierto estado.|estoy|está|estuvo|estará|-|-|Mi mamá está en casa.
tener|te-ner|Poseer algo o contar con ello.|tengo|tiene|tuvo|tendrá|poseer|carecer|Ana tiene un lápiz rojo.
hacer|ha-cer|Crear algo o realizar una acción.|hago|hace|hizo|hará|crear|deshacer|Hago mi tarea.
ir|ir|Moverse de un lugar hacia otro.|voy|va|fue|irá|-|venir|Voy al colegio.
venir|ve-nir|Moverse hacia el lugar donde está quien habla.|vengo|viene|vino|vendrá|llegar|ir|Mi tía viene mañana.
ver|ver|Mirar con los ojos.|veo|ve|vio|verá|mirar|-|Veo un pájaro.
oír|o-ír|Percibir sonidos con los oídos.|oigo|oye|oyó|oirá|escuchar|-|Oigo la campana.
decir|de-cir|Expresar algo con palabras.|digo|dice|dijo|dirá|hablar|callar|Digo mi nombre.
hablar|ha-blar|Usar la voz para decir palabras.|hablo|habla|habló|hablará|conversar|callar|Hablo con mi amiga.
callar|ca-llar|Dejar de hablar o no hablar.|callo|calla|calló|callará|silenciar|hablar|Me callo cuando la profesora explica.
dar|dar|Entregar algo a alguien.|doy|da|dio|dará|entregar|quitar|Doy un abrazo.
poner|po-ner|Colocar algo en un lugar.|pongo|pone|puso|pondrá|colocar|sacar|Pongo el libro en la mesa.
sacar|sa-car|Quitar algo del lugar donde estaba.|saco|saca|sacó|sacará|quitar|poner|Saco el lápiz del estuche.
tomar|to-mar|Agarrar algo o beber.|tomo|toma|tomó|tomará|agarrar|soltar|Tomo agua.
comer|co-mer|Meter alimento en la boca y tragarlo.|como|come|comió|comerá|alimentarse|ayunar|Como una manzana.
beber|be-ber|Tomar un líquido.|bebo|bebe|bebió|beberá|tomar|-|Bebo leche.
cocinar|co-ci-nar|Preparar la comida con calor.|cocino|cocina|cocinó|cocinará|preparar|-|Mi papá cocina arroz.
dormir|dor-mir|Descansar con los ojos cerrados y sin darse cuenta de lo que pasa.|duermo|duerme|durmió|dormirá|descansar|despertar|Duermo en mi cama.
despertar|des-per-tar|Dejar de dormir.|despierto|despierta|despertó|despertará|-|dormir|Despierto a las siete.
soñar|so-ñar|Ver imágenes en la mente mientras se duerme.|sueño|sueña|soñó|soñará|-|-|Sueño con un caballo.
caminar|ca-mi-nar|Avanzar dando pasos.|camino|camina|caminó|caminará|andar|detenerse|Camino hasta el colegio.
correr|co-rrer|Avanzar muy rápido moviendo las piernas.|corro|corre|corrió|correrá|-|caminar|Corro en el patio.
saltar|sal-tar|Elevarse del suelo con un impulso.|salto|salta|saltó|saltará|brincar|-|Salto la cuerda.
subir|su-bir|Ir hacia un lugar más alto.|subo|sube|subió|subirá|ascender|bajar|Subo la escalera.
bajar|ba-jar|Ir hacia un lugar más bajo.|bajo|baja|bajó|bajará|descender|subir|Bajo del bus.
entrar|en-trar|Pasar de afuera hacia adentro.|entro|entra|entró|entrará|pasar|salir|Entro a la sala.
salir|sa-lir|Pasar de adentro hacia afuera.|salgo|sale|salió|saldrá|-|entrar|Salgo al patio.
llegar|lle-gar|Alcanzar el lugar al que se iba.|llego|llega|llegó|llegará|-|partir|Llego temprano.
volver|vol-ver|Regresar al lugar de donde se salió.|vuelvo|vuelve|volvió|volverá|regresar|partir|Vuelvo a mi casa.
jugar|ju-gar|Hacer una actividad para divertirse.|juego|juega|jugó|jugará|divertirse|trabajar|Juego con mi hermano.
cantar|can-tar|Decir palabras con música.|canto|canta|cantó|cantará|-|-|Canto una canción.
bailar|bai-lar|Mover el cuerpo al ritmo de la música.|bailo|baila|bailó|bailará|-|-|Bailo en la fiesta.
dibujar|di-bu-jar|Hacer figuras con lápices o colores.|dibujo|dibuja|dibujó|dibujará|trazar|-|Dibujo un sol.
pintar|pin-tar|Cubrir algo con color.|pinto|pinta|pintó|pintará|colorear|-|Pinto de azul el cielo.
escribir|es-cri-bir|Hacer letras o palabras sobre una superficie.|escribo|escribe|escribió|escribirá|anotar|borrar|Escribo mi nombre.
leer|le-er|Mirar las letras y entender lo que dicen.|leo|lee|leyó|leerá|-|-|Leo un cuento.
borrar|bo-rrar|Quitar lo escrito o dibujado.|borro|borra|borró|borrará|eliminar|escribir|Borro el error.
cortar|cor-tar|Dividir algo con tijeras o con un cuchillo.|corto|corta|cortó|cortará|partir|pegar|Corto el papel.
pegar|pe-gar|Unir una cosa con otra usando pegamento.|pego|pega|pegó|pegará|unir|despegar|Pego la hoja.
contar|con-tar|Decir los números en orden; o narrar una historia.|cuento|cuenta|contó|contará|narrar|-|Cuento hasta diez.
mirar|mi-rar|Dirigir los ojos hacia algo.|miro|mira|miró|mirará|observar|-|Miro el cielo.
escuchar|es-cu-char|Poner atención para oír algo.|escucho|escucha|escuchó|escuchará|oír|-|Escucho a la profesora.
abrir|a-brir|Quitar lo que cierra algo.|abro|abre|abrió|abrirá|-|cerrar|Abro la puerta.
cerrar|ce-rrar|Poner algo de modo que no pase nada.|cierro|cierra|cerró|cerrará|-|abrir|Cierro la ventana.
lavar|la-var|Limpiar algo con agua.|lavo|lava|lavó|lavará|limpiar|ensuciar|Lavo mis manos.
ayudar|a-yu-dar|Hacer algo para que otro lo logre.|ayudo|ayuda|ayudó|ayudará|colaborar|-|Ayudo a mi mamá.
querer|que-rer|Desear algo o sentir cariño.|quiero|quiere|quiso|querrá|desear|odiar|Quiero un helado.
saber|sa-ber|Conocer algo o tener la habilidad de hacerlo.|sé|sabe|supo|sabrá|conocer|ignorar|Sé leer.
poder|po-der|Tener la capacidad o el permiso de hacer algo.|puedo|puede|pudo|podrá|-|-|Puedo saltar alto.
pensar|pen-sar|Usar la mente para razonar o recordar.|pienso|piensa|pensó|pensará|razonar|-|Pienso antes de responder.
aprender|a-pren-der|Obtener un conocimiento nuevo.|aprendo|aprende|aprendió|aprenderá|-|olvidar|Aprendo palabras nuevas.
enseñar|en-se-ñar|Dar a alguien un conocimiento.|enseño|enseña|enseñó|enseñará|instruir|aprender|La profesora enseña a leer.
llamar|lla-mar|Decir el nombre de alguien para que venga.|llamo|llama|llamó|llamará|-|-|Llamo a mi hermano.
llorar|llo-rar|Soltar lágrimas.|lloro|llora|lloró|llorará|-|reír|El bebé llora.
reír|re-ír|Mostrar alegría con la cara y con la voz.|río|ríe|rio|reirá|-|llorar|Me río con mis amigos.
sentir|sen-tir|Percibir algo con el cuerpo o con las emociones.|siento|siente|sintió|sentirá|-|-|Siento alegría.
esperar|es-pe-rar|Quedarse hasta que algo llegue o pase.|espero|espera|esperó|esperará|aguardar|-|Espero el bus.
buscar|bus-car|Tratar de encontrar algo.|busco|busca|buscó|buscará|-|encontrar|Busco mi lápiz.
encontrar|en-con-trar|Dar con algo que se buscaba.|encuentro|encuentra|encontró|encontrará|hallar|perder|Encuentro mi lápiz.
perder|per-der|Dejar de tener algo.|pierdo|pierde|perdió|perderá|extraviar|encontrar|Pierdo mi gorro.
cuidar|cui-dar|Poner atención para que algo no sufra daño.|cuido|cuida|cuidó|cuidará|proteger|descuidar|Cuido a mi gato.
"""
