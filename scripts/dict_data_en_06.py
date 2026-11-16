"""Diccionario de inglés de 6.º básico (inglés ↔ español) para hablantes de español.

Formato de PALABRAS (una por línea, separado por «|»):
    english|clase|IPA (inglés estadounidense)|pronunciación figurada|español|significado en español|ejemplo en inglés|ejemplo en español|tema
Formato de VERBOS:
    base|IPA|pasado|pasado en español (él/ella)|infinitivo en español|presente él/ella en español|significado|ejemplo en inglés|ejemplo en español
La pronunciación figurada marca la sílaba fuerte en MAYÚSCULAS y es solo una aproximación para quien habla español.
Textos propios del proyecto: no copian ningún diccionario publicado.
"""

NIVEL = "6-basico"
IDIOMA = "en"

PALABRAS = """
physics|sustantivo|/ˈfɪzɪks/|FI-siks|física|Ciencia que estudia la energía, el movimiento y la materia.|Physics explains why things fall.|La física explica por qué las cosas caen.|escuela
chemistry|sustantivo|/ˈkɛməstri/|KE-mis-tri|química|Ciencia que estudia de qué están hechas las sustancias y cómo cambian.|We mix liquids in chemistry class.|Mezclamos líquidos en la clase de química.|escuela
biology|sustantivo|/baɪˈɑːlədʒi/|bai-A-lo-yi|biología|Ciencia que estudia a los seres vivos.|Biology is about plants and animals.|La biología trata de plantas y animales.|escuela
geography|sustantivo|/dʒiˈɑːɡrəfi/|yi-A-gra-fi|geografía|Materia que estudia los países, los mapas y el paisaje.|In geography we study rivers.|En geografía estudiamos los ríos.|escuela
grammar|sustantivo|/ˈɡræmər/|GRA-mer|gramática|Reglas para formar bien las frases en un idioma.|English grammar has simple rules.|La gramática inglesa tiene reglas sencillas.|escuela
vocabulary|sustantivo|/voʊˈkæbjəˌlɛri/|vou-KA-biu-le-ri|vocabulario|Conjunto de palabras que conoces de un idioma.|I learn new vocabulary every week.|Aprendo vocabulario nuevo cada semana.|escuela
spelling|sustantivo|/ˈspɛlɪŋ/|SPE-ling|ortografía|Forma correcta de escribir las letras de una palabra.|My spelling is getting better.|Mi ortografía está mejorando.|escuela
pronunciation|sustantivo|/prəˌnʌnsiˈeɪʃən/|pro-nan-si-EI-shon|pronunciación|Forma de decir una palabra en voz alta.|Her pronunciation is very clear.|Su pronunciación es muy clara.|escuela
semester|sustantivo|/səˈmɛstər/|se-MES-ter|semestre|Mitad del año escolar.|The first semester ends in July.|El primer semestre termina en julio.|escuela
textbook|sustantivo|/ˈtɛkstˌbʊk/|TEKST-buk|libro de texto|Libro que se usa para estudiar una materia.|Open your textbook to page ten.|Abre tu libro de texto en la página diez.|escuela
worksheet|sustantivo|/ˈwɜːrkˌʃiːt/|UERK-shiit|hoja de trabajo|Hoja con ejercicios para resolver.|Please finish the worksheet.|Por favor, termina la hoja de trabajo.|escuela
quiz|sustantivo|/kwɪz/|kuis|prueba corta|Examen breve con pocas preguntas.|We have a quiz on Friday.|Tenemos una prueba corta el viernes.|escuela
whiteboard|sustantivo|/ˈwaɪtˌbɔːrd/|UAIT-bord|pizarra blanca|Superficie lisa y blanca donde se escribe con plumones.|The teacher wrote on the whiteboard.|La profesora escribió en la pizarra blanca.|escuela
projector|sustantivo|/prəˈdʒɛktər/|pro-YEK-ter|proyector|Aparato que muestra imágenes en una pared o pantalla.|The projector shows our slides.|El proyector muestra nuestras diapositivas.|escuela
university|sustantivo|/ˌjuːnəˈvɜːrsəti/|iu-ni-VER-si-ti|universidad|Lugar donde se estudia una carrera después del colegio.|My cousin studies at a university.|Mi primo estudia en una universidad.|escuela
club|sustantivo|/klʌb/|klab|club|Grupo de personas que comparten un interés.|I joined the chess club.|Me uní al club de ajedrez.|escuela
assembly|sustantivo|/əˈsɛmbli/|a-SEM-bli|acto escolar|Reunión de todo el colegio en un solo lugar.|There is an assembly in the gym.|Hay un acto en el gimnasio.|escuela
field trip|sustantivo|/ˈfiːld trɪp/|FIILD trip|salida pedagógica|Paseo escolar para aprender fuera de la sala.|Our field trip is to the museum.|Nuestra salida pedagógica es al museo.|escuela
absent|adjetivo|/ˈæbsənt/|AB-sent|ausente|Que no está en el lugar donde debería estar.|Ben was absent yesterday.|Ben estuvo ausente ayer.|escuela
relative|sustantivo|/ˈrɛlətɪv/|RE-la-tiv|pariente|Persona de tu familia.|I visited a relative in Chile.|Visité a un pariente en Chile.|personas
twin|sustantivo|/twɪn/|tuin|gemelo|Hermano que nació el mismo día que tú.|My twin sister is taller than me.|Mi hermana gemela es más alta que yo.|personas
adult|sustantivo|/əˈdʌlt/|a-DALT|adulto|Persona que ya creció.|Ask an adult for help.|Pide ayuda a un adulto.|personas
teenager|sustantivo|/ˈtiːnˌeɪdʒər/|TIIN-ei-yer|adolescente|Persona de entre trece y diecinueve años.|The teenager plays in a band.|El adolescente toca en una banda.|personas
child|sustantivo|/tʃaɪld/|chaild|niño, niña|Persona que todavía es pequeña.|The child is drawing a house.|El niño está dibujando una casa.|personas
children|sustantivo|/ˈtʃɪldrən/|CHIL-dren|niños|Plural de child.|The children are in the yard.|Los niños están en el patio.|personas
kid|sustantivo|/kɪd/|kid|chico|Forma informal de decir niño.|That kid runs very fast.|Ese chico corre muy rápido.|personas
man|sustantivo|/mæn/|man|hombre|Persona adulta de sexo masculino.|The man is waiting for the bus.|El hombre espera el bus.|personas
woman|sustantivo|/ˈwʊmən/|UU-man|mujer|Persona adulta de sexo femenino.|The woman is reading a magazine.|La mujer lee una revista.|personas
people|sustantivo|/ˈpiːpəl/|PII-pol|gente|Varias personas.|Many people come to the park.|Mucha gente viene al parque.|personas
person|sustantivo|/ˈpɜːrsən/|PER-son|persona|Un ser humano.|She is a very kind person.|Ella es una persona muy amable.|personas
husband|sustantivo|/ˈhʌzbənd/|JAS-bend|esposo|Hombre casado con una mujer.|Her husband is a pilot.|Su esposo es piloto.|personas
wife|sustantivo|/waɪf/|uaif|esposa|Mujer casada con un hombre.|His wife works at a bank.|Su esposa trabaja en un banco.|personas
grandparents|sustantivo|/ˈɡrænˌpɛrənts/|GRAN-pe-rents|abuelos|El abuelo y la abuela juntos.|My grandparents live near the sea.|Mis abuelos viven cerca del mar.|personas
nephew|sustantivo|/ˈnɛfjuː/|NE-fiu|sobrino|Hijo de tu hermano o de tu hermana.|My nephew is five years old.|Mi sobrino tiene cinco años.|personas
niece|sustantivo|/niːs/|niis|sobrina|Hija de tu hermano o de tu hermana.|My niece loves painting.|A mi sobrina le encanta pintar.|personas
chest|sustantivo|/tʃɛst/|chest|pecho|Parte delantera del cuerpo, entre el cuello y el estómago.|My chest hurts after running.|Me duele el pecho después de correr.|cuerpo
hip|sustantivo|/hɪp/|jip|cadera|Parte del cuerpo donde la pierna se une al tronco.|He fell on his hip.|Se cayó sobre la cadera.|cuerpo
waist|sustantivo|/weɪst/|ueist|cintura|Parte angosta del cuerpo, sobre las caderas.|She wears a belt at her waist.|Ella lleva un cinturón en la cintura.|cuerpo
pulse|sustantivo|/pʌls/|pals|pulso|Latido del corazón que se siente en la muñeca.|I can feel my pulse.|Puedo sentir mi pulso.|cuerpo
sweat|sustantivo|/swɛt/|suet|sudor|Agua que sale por la piel cuando tienes calor.|Sweat dripped down his face.|El sudor le caía por la cara.|cuerpo
breath|sustantivo|/brɛθ/|brez|aliento, respiración|Aire que entra y sale de los pulmones.|Take a deep breath.|Respira profundo.|cuerpo
patient|sustantivo|/ˈpeɪʃənt/|PEI-shent|paciente|Persona que recibe atención médica.|The patient is resting.|El paciente está descansando.|salud
surgeon|sustantivo|/ˈsɜːrdʒən/|SER-yon|cirujano|Médico que hace operaciones.|The surgeon works in the hospital.|El cirujano trabaja en el hospital.|salud
operation|sustantivo|/ˌɑːpəˈreɪʃən/|a-pe-REI-shon|operación|Trabajo del médico que abre el cuerpo para curar algo.|He had an operation on his knee.|Le hicieron una operación en la rodilla.|salud
emergency|sustantivo|/ɪˈmɜːrdʒənsi/|i-MER-yen-si|emergencia|Situación grave que necesita ayuda rápida.|Call 131 for a medical emergency.|Llama al 131 en una emergencia médica.|salud
wound|sustantivo|/wuːnd/|uund|herida|Lugar de la piel que se cortó o se dañó.|Clean the wound with water.|Limpia la herida con agua.|salud
scar|sustantivo|/skɑːr/|skar|cicatriz|Marca que queda en la piel después de una herida.|He has a small scar on his arm.|Tiene una pequeña cicatriz en el brazo.|salud
dizzy|adjetivo|/ˈdɪzi/|DI-si|mareado|Que siente que todo da vueltas.|I feel dizzy after spinning.|Me siento mareado después de girar.|salud
pale|adjetivo|/peɪl/|peil|pálido|De color muy claro, sin el tono normal de la piel.|She looked pale and tired.|Se veía pálida y cansada.|salud
exhausted|adjetivo|/ɪɡˈzɔːstɪd/|ig-SOS-tid|agotado|Muy cansado, sin fuerzas.|We were exhausted after the hike.|Estábamos agotados después de la caminata.|salud
diet|sustantivo|/ˈdaɪət/|DAI-et|dieta|Conjunto de alimentos que come una persona.|A healthy diet includes vegetables.|Una dieta sana incluye verduras.|salud
vitamin|sustantivo|/ˈvaɪtəmɪn/|VAI-ta-min|vitamina|Sustancia de los alimentos que el cuerpo necesita.|Oranges have vitamin C.|Las naranjas tienen vitamina C.|salud
calorie|sustantivo|/ˈkæləri/|KA-lo-ri|caloría|Unidad que mide la energía de un alimento.|This snack has many calories.|Esta colación tiene muchas calorías.|salud
protein|sustantivo|/ˈproʊtiːn/|PROU-tiin|proteína|Sustancia de los alimentos que ayuda a formar músculos.|Eggs are a good source of protein.|Los huevos son una buena fuente de proteína.|salud
glad|adjetivo|/ɡlæd/|glad|contento|Feliz por algo que pasó.|I am glad you came.|Me alegra que hayas venido.|emociones
grateful|adjetivo|/ˈɡreɪtfəl/|GREIT-ful|agradecido|Que siente gratitud por algo recibido.|We are grateful for your help.|Estamos agradecidos por tu ayuda.|emociones
curious|adjetivo|/ˈkjʊriəs/|KIU-ri-es|curioso|Con ganas de saber o de descubrir algo.|The curious cat opened the box.|El gato curioso abrió la caja.|emociones
anxious|adjetivo|/ˈæŋkʃəs/|ANK-shes|ansioso|Inquieto por algo que puede pasar.|He felt anxious before the exam.|Se sintió ansioso antes del examen.|emociones
furious|adjetivo|/ˈfjʊriəs/|FIU-ri-es|furioso|Muy enojado.|Dad was furious about the broken window.|Papá estaba furioso por la ventana rota.|emociones
ashamed|adjetivo|/əˈʃeɪmd/|a-SHEIMD|avergonzado|Que siente vergüenza por algo que hizo.|She felt ashamed of her lie.|Se sintió avergonzada de su mentira.|emociones
relieved|adjetivo|/rɪˈliːvd/|ri-LIIVD|aliviado|Tranquilo porque pasó un problema.|I was relieved when I found my keys.|Me sentí aliviado cuando encontré mis llaves.|emociones
amused|adjetivo|/əˈmjuːzd/|a-MIUSD|divertido|Que se entretiene o se ríe con algo.|The kids were amused by the clown.|Los niños se divirtieron con el payaso.|emociones
determined|adjetivo|/dɪˈtɜːrmənd/|di-TER-mind|decidido|Que está firme en lo que quiere lograr.|She is determined to win.|Ella está decidida a ganar.|emociones
impatient|adjetivo|/ɪmˈpeɪʃənt/|im-PEI-shent|impaciente|Que no sabe esperar.|Don't be impatient; wait your turn.|No seas impaciente; espera tu turno.|emociones
hopeful|adjetivo|/ˈhoʊpfəl/|JOUP-ful|esperanzado|Que cree que algo bueno va a pasar.|I am hopeful about the news.|Estoy esperanzado con la noticia.|emociones
afraid|adjetivo|/əˈfreɪd/|a-FREID|asustado|Con miedo.|He is afraid of the dark.|Le tiene miedo a la oscuridad.|emociones
annoyed|adjetivo|/əˈnɔɪd/|a-NOID|molesto|Un poco enojado por algo.|She was annoyed by the noise.|Estaba molesta por el ruido.|emociones
confused|adjetivo|/kənˈfjuːzd/|kon-FIUSD|confundido|Que no entiende bien algo.|I am confused by this map.|Estoy confundido con este mapa.|emociones
pleased|adjetivo|/pliːzd/|pliisd|complacido|Contento con algo.|The teacher was pleased with my work.|La profesora quedó complacida con mi trabajo.|emociones
stubborn|adjetivo|/ˈstʌbərn/|STA-born|terco|Que no cambia de idea aunque le digan que se equivoca.|My donkey is very stubborn.|Mi burro es muy terco.|personalidad
rude|adjetivo|/ruːd/|ruud|grosero|Sin buenos modales.|It is rude to shout at people.|Es grosero gritarle a la gente.|personalidad
humble|adjetivo|/ˈhʌmbəl/|JAM-bol|humilde|Que no presume de lo que tiene o hace.|The champion is humble.|El campeón es humilde.|personalidad
cruel|adjetivo|/ˈkruːəl/|KRU-el|cruel|Que disfruta haciendo sufrir a otros.|It is cruel to hurt animals.|Es cruel lastimar animales.|personalidad
loyal|adjetivo|/ˈlɔɪəl/|LOI-al|leal|Fiel a sus amigos o a sus ideas.|A loyal friend never lies to you.|Un amigo leal nunca te miente.|personalidad
greedy|adjetivo|/ˈɡriːdi/|GRII-di|codicioso|Que quiere tener más de lo que necesita.|The greedy king wanted all the gold.|El rey codicioso quería todo el oro.|personalidad
attic|sustantivo|/ˈætɪk/|A-tik|ático, entretecho|Espacio bajo el techo de una casa donde se guardan cosas.|We keep old boxes in the attic.|Guardamos cajas viejas en el entretecho.|casa
basement|sustantivo|/ˈbeɪsmənt/|BEIS-ment|sótano|Piso de una casa que está bajo la tierra.|The washing machine is in the basement.|La lavadora está en el sótano.|casa
hallway|sustantivo|/ˈhɔːlˌweɪ/|JOL-uei|pasillo|Espacio largo y angosto dentro de una casa.|The hallway leads to the bedrooms.|El pasillo lleva a los dormitorios.|casa
porch|sustantivo|/pɔːrtʃ/|porch|porche|Entrada cubierta de una casa.|We sat on the porch at night.|Nos sentamos en el porche por la noche.|casa
fireplace|sustantivo|/ˈfaɪərˌpleɪs/|FAIR-pleis|chimenea|Lugar de la casa donde se enciende leña.|The fireplace keeps the room warm.|La chimenea mantiene tibia la habitación.|casa
wardrobe|sustantivo|/ˈwɔːrˌdroʊb/|UOR-droub|clóset|Mueble grande donde se guarda la ropa.|My coat is in the wardrobe.|Mi abrigo está en el clóset.|casa
cushion|sustantivo|/ˈkʊʃən/|KU-shon|cojín|Almohadón blando para sentarse o apoyarse.|I put a cushion on the chair.|Puse un cojín en la silla.|casa
tap|sustantivo|/tæp/|tap|grifo|Llave por donde sale el agua.|Turn off the tap, please.|Cierra el grifo, por favor.|casa
bucket|sustantivo|/ˈbʌkɪt/|BA-kit|balde|Recipiente con asa para llevar agua u otras cosas.|He filled the bucket with sand.|Llenó el balde con arena.|casa
ladder|sustantivo|/ˈlædər/|LA-der|escalera de mano|Escalera portátil para subir a lugares altos.|Dad climbed the ladder to fix the roof.|Papá subió la escalera para arreglar el techo.|casa
hammer|sustantivo|/ˈhæmər/|JA-mer|martillo|Herramienta para clavar clavos.|He hit the nail with a hammer.|Golpeó el clavo con un martillo.|casa
screw|sustantivo|/skruː/|skruu|tornillo|Pieza de metal con espiral que se gira para unir cosas.|This screw is too loose.|Este tornillo está muy suelto.|casa
drill|sustantivo|/drɪl/|dril|taladro|Herramienta eléctrica para hacer agujeros.|The drill is very noisy.|El taladro es muy ruidoso.|casa
garbage|sustantivo|/ˈɡɑːrbɪdʒ/|GAR-bich|basura|Cosas que se botan porque ya no sirven.|Take out the garbage, please.|Saca la basura, por favor.|casa
bin|sustantivo|/bɪn/|bin|basurero|Recipiente donde se botan cosas.|Put the paper in the bin.|Pon el papel en el basurero.|casa
tram|sustantivo|/træm/|tram|tranvía|Vehículo eléctrico que anda sobre rieles por la ciudad.|The tram stops near the park.|El tranvía para cerca del parque.|transporte
ferry|sustantivo|/ˈfɛri/|FE-ri|transbordador|Barco que lleva personas y autos de un lado a otro.|We crossed the channel by ferry.|Cruzamos el canal en transbordador.|transporte
scooter|sustantivo|/ˈskuːtər/|SKUU-ter|scooter|Vehículo pequeño con dos ruedas y manubrio.|She rides her scooter to school.|Ella va al colegio en su scooter.|transporte
skateboard|sustantivo|/ˈskeɪtˌbɔːrd/|SKEIT-bord|patineta|Tabla con ruedas que se usa de pie.|He does tricks on his skateboard.|Él hace trucos en su patineta.|transporte
traffic|sustantivo|/ˈtræfɪk/|TRA-fik|tráfico|Conjunto de vehículos que circulan por una calle.|There is a lot of traffic today.|Hay mucho tráfico hoy.|transporte
crossing|sustantivo|/ˈkrɔːsɪŋ/|KRO-sing|cruce peatonal|Lugar marcado para cruzar la calle.|Cross at the crossing.|Cruza en el cruce peatonal.|transporte
roundabout|sustantivo|/ˈraʊndəˌbaʊt/|RAUN-da-baut|rotonda|Plaza circular donde se juntan varias calles.|Turn left at the roundabout.|Gira a la izquierda en la rotonda.|transporte
intersection|sustantivo|/ˌɪntərˈsɛkʃən/|in-ter-SEK-shon|intersección|Lugar donde se cruzan dos calles.|Stop at the intersection.|Detente en la intersección.|transporte
passenger|sustantivo|/ˈpæsɪndʒər/|PA-sin-yer|pasajero|Persona que viaja en un vehículo sin conducirlo.|The passenger fell asleep.|El pasajero se quedó dormido.|transporte
seat belt|sustantivo|/ˈsiːt bɛlt/|SIIT belt|cinturón de seguridad|Correa que te sujeta al asiento del auto.|Always wear your seat belt.|Usa siempre tu cinturón de seguridad.|transporte
parking lot|sustantivo|/ˈpɑːrkɪŋ lɑːt/|PAR-king lat|estacionamiento|Lugar para dejar los autos.|The parking lot is full.|El estacionamiento está lleno.|transporte
gas station|sustantivo|/ˈɡæs ˌsteɪʃən/|GAS STEI-shon|bencinera|Lugar donde los autos cargan combustible.|We stopped at a gas station.|Paramos en una bencinera.|transporte
currency|sustantivo|/ˈkɜːrənsi/|KER-ren-si|moneda|Dinero que se usa en un país.|The currency of Chile is the peso.|La moneda de Chile es el peso.|viajes
reservation|sustantivo|/ˌrɛzərˈveɪʃən/|re-ser-VEI-shon|reserva|Aviso para guardar un lugar o una mesa.|I made a reservation at the hotel.|Hice una reserva en el hotel.|viajes
reception|sustantivo|/rɪˈsɛpʃən/|ri-SEP-shon|recepción|Lugar del hotel donde se recibe a los clientes.|Ask at the reception for a map.|Pide un mapa en la recepción.|viajes
elevator|sustantivo|/ˈɛləˌveɪtər/|E-le-vei-ter|ascensor|Cabina que sube y baja por un edificio.|Take the elevator to the fifth floor.|Toma el ascensor hasta el quinto piso.|viajes
lobby|sustantivo|/ˈlɑːbi/|LA-bi|vestíbulo|Sala de entrada de un edificio u hotel.|We waited in the lobby.|Esperamos en el vestíbulo.|viajes
route|sustantivo|/ruːt/|ruut|ruta|Camino que se sigue para ir a un lugar.|This route is shorter.|Esta ruta es más corta.|viajes
price|sustantivo|/praɪs/|prais|precio|Dinero que cuesta algo.|The price is ten dollars.|El precio es diez dólares.|compras
discount|sustantivo|/ˈdɪskaʊnt/|DIS-kaunt|descuento|Rebaja que se hace al precio de algo.|They gave me a discount.|Me hicieron un descuento.|compras
sale|sustantivo|/seɪl/|seil|oferta, liquidación|Venta con precios más bajos.|The shoes are on sale.|Los zapatos están en oferta.|compras
receipt|sustantivo|/rɪˈsiːt/|ri-SIIT|boleta|Papel que prueba que pagaste.|Keep the receipt.|Guarda la boleta.|compras
cashier|sustantivo|/kæˈʃɪr/|ka-SHIR|cajero|Persona que cobra en una tienda.|The cashier gave me my change.|La cajera me dio mi vuelto.|compras
coin|sustantivo|/kɔɪn/|koin|moneda|Pieza de metal que se usa como dinero.|I found a coin on the street.|Encontré una moneda en la calle.|compras
cash|sustantivo|/kæʃ/|kash|efectivo|Dinero en billetes y monedas.|I paid in cash.|Pagué en efectivo.|compras
credit card|sustantivo|/ˈkrɛdɪt kɑːrd/|KRE-dit kard|tarjeta de crédito|Tarjeta para pagar y devolver el dinero después.|He paid with a credit card.|Él pagó con tarjeta de crédito.|compras
change|sustantivo|/tʃeɪndʒ/|cheinch|vuelto|Dinero que te devuelven cuando pagas de más.|Keep the change.|Quédate con el vuelto.|compras
bargain|sustantivo|/ˈbɑːrɡən/|BAR-gen|ganga|Cosa que se compra a muy buen precio.|This jacket was a bargain.|Esta chaqueta fue una ganga.|compras
refund|sustantivo|/ˈriːˌfʌnd/|RII-fand|reembolso|Dinero que te devuelven por algo que compraste.|I asked for a refund.|Pedí un reembolso.|compras
basket|sustantivo|/ˈbæskɪt/|BAS-kit|canasto|Recipiente de fibras tejidas para llevar cosas.|She carried a basket of fruit.|Ella llevaba un canasto con fruta.|compras
cart|sustantivo|/kɑːrt/|kart|carro de compras|Carro con ruedas para llevar la compra.|Push the cart to the checkout.|Empuja el carro hasta la caja.|compras
aisle|sustantivo|/aɪl/|ail|pasillo|Espacio entre estantes o asientos.|The cereal is in aisle three.|Los cereales están en el pasillo tres.|compras
brand|sustantivo|/brænd/|brand|marca|Nombre de un producto que lo distingue de otros.|What brand of shoes do you like?|¿Qué marca de zapatos te gusta?|compras
label|sustantivo|/ˈleɪbəl/|LEI-bol|etiqueta|Papel pegado a un producto con información.|Read the label first.|Lee primero la etiqueta.|compras
accountant|sustantivo|/əˈkaʊntənt/|a-KAUN-tent|contador|Persona que lleva las cuentas del dinero.|The accountant checks the numbers.|El contador revisa las cifras.|trabajos
architect|sustantivo|/ˈɑːrkɪˌtɛkt/|AR-ki-tekt|arquitecto|Persona que diseña edificios.|The architect drew a new school.|La arquitecta dibujó una escuela nueva.|trabajos
lawyer|sustantivo|/ˈlɔɪər/|LOI-er|abogado|Persona que defiende a otros en asuntos de la ley.|The lawyer talked to the judge.|El abogado habló con el juez.|trabajos
judge|sustantivo|/dʒʌdʒ/|yach|juez|Persona que decide en un juicio.|The judge listened to both sides.|El juez escuchó a ambas partes.|trabajos
journalist|sustantivo|/ˈdʒɜːrnəlɪst/|YER-na-list|periodista|Persona que escribe noticias.|The journalist wrote about the flood.|La periodista escribió sobre la inundación.|trabajos
reporter|sustantivo|/rɪˈpɔːrtər/|ri-POR-ter|reportero|Persona que busca y cuenta noticias en la tele o la radio.|The reporter is live from the beach.|El reportero está en vivo desde la playa.|trabajos
designer|sustantivo|/dɪˈzaɪnər/|di-SAI-ner|diseñador|Persona que crea el aspecto de objetos o ropa.|The designer made a red dress.|La diseñadora hizo un vestido rojo.|trabajos
programmer|sustantivo|/ˈproʊˌɡræmər/|PROU-gra-mer|programador|Persona que escribe programas de computador.|The programmer fixed the bug.|El programador arregló el error.|trabajos
electrician|sustantivo|/ɪˌlɛkˈtrɪʃən/|i-lek-TRI-shon|electricista|Persona que instala y arregla la electricidad.|The electrician changed the cables.|El electricista cambió los cables.|trabajos
plumber|sustantivo|/ˈplʌmər/|PLA-mer|gásfiter|Persona que arregla cañerías de agua.|The plumber fixed the sink.|El gásfiter arregló el lavaplatos.|trabajos
carpenter|sustantivo|/ˈkɑːrpəntər/|KAR-pen-ter|carpintero|Persona que trabaja la madera.|The carpenter built a table.|El carpintero construyó una mesa.|trabajos
secretary|sustantivo|/ˈsɛkrəˌtɛri/|SE-kre-te-ri|secretaria|Persona que organiza papeles y llamadas en una oficina.|The secretary answers the phone.|La secretaria contesta el teléfono.|trabajos
manager|sustantivo|/ˈmænɪdʒər/|MA-ni-yer|gerente|Persona que dirige una tienda o una empresa.|The manager opened the store.|El gerente abrió la tienda.|trabajos
tailor|sustantivo|/ˈteɪlər/|TEI-ler|sastre|Persona que hace o arregla ropa.|The tailor shortened my pants.|El sastre acortó mi pantalón.|trabajos
mayor|sustantivo|/ˈmeɪər/|MEI-er|alcalde|Persona que dirige una ciudad o comuna.|The mayor visited our school.|El alcalde visitó nuestro colegio.|trabajos
president|sustantivo|/ˈprɛzɪdənt/|PRE-si-dent|presidente|Jefe de un país o de una organización.|The president gave a speech.|El presidente dio un discurso.|trabajos
detective|sustantivo|/dɪˈtɛktɪv/|di-TEK-tiv|detective|Persona que investiga delitos o misterios.|The detective found a clue.|El detective encontró una pista.|trabajos
magician|sustantivo|/məˈdʒɪʃən/|ma-YI-shon|mago|Persona que hace trucos que parecen magia.|The magician pulled a rabbit from a hat.|El mago sacó un conejo de un sombrero.|trabajos
lifeguard|sustantivo|/ˈlaɪfˌɡɑːrd/|LAIF-gard|salvavidas|Persona que cuida a los bañistas.|The lifeguard watches the swimmers.|El salvavidas vigila a los nadadores.|trabajos
tour guide|sustantivo|/ˈtʊr ˌɡaɪd/|TUR gaid|guía turístico|Persona que muestra un lugar a los visitantes.|The tour guide told us about the castle.|El guía turístico nos habló del castillo.|trabajos
karate|sustantivo|/kəˈrɑːti/|ka-RA-ti|karate|Arte marcial que usa golpes con manos y pies.|He practices karate on Saturdays.|Él practica karate los sábados.|deportes
judo|sustantivo|/ˈdʒuːdoʊ/|YUU-dou|judo|Arte marcial en que se derriba al rival.|Judo teaches respect.|El judo enseña respeto.|deportes
yoga|sustantivo|/ˈjoʊɡə/|YOU-ga|yoga|Ejercicios de posturas, respiración y calma.|We do yoga to relax.|Hacemos yoga para relajarnos.|deportes
jogging|sustantivo|/ˈdʒɑːɡɪŋ/|YA-ging|trote|Carrera suave que se hace como ejercicio.|Jogging is good for your heart.|Trotar es bueno para el corazón.|deportes
hiking|sustantivo|/ˈhaɪkɪŋ/|JAI-king|senderismo|Caminata larga por la naturaleza.|We went hiking in the mountains.|Fuimos de senderismo a la montaña.|deportes
sailing|sustantivo|/ˈseɪlɪŋ/|SEI-ling|navegación a vela|Deporte de navegar en un velero.|Sailing needs a good wind.|La navegación a vela necesita buen viento.|deportes
diving|sustantivo|/ˈdaɪvɪŋ/|DAI-ving|buceo, clavados|Actividad de lanzarse al agua o de nadar bajo ella.|Diving is allowed in the deep pool.|Se permiten los clavados en la piscina honda.|deportes
skateboarding|sustantivo|/ˈskeɪtˌbɔːrdɪŋ/|SKEIT-bor-ding|andar en patineta|Deporte de deslizarse sobre una tabla con ruedas.|Skateboarding takes balance.|Andar en patineta requiere equilibrio.|deportes
bowling|sustantivo|/ˈboʊlɪŋ/|BOU-ling|bolos|Juego en que se lanza una bola para tumbar pinos.|We played bowling on Sunday.|Jugamos a los bolos el domingo.|deportes
board game|sustantivo|/ˈbɔːrd ɡeɪm/|BORD geim|juego de mesa|Juego con tablero y fichas.|Let's play a board game.|Juguemos un juego de mesa.|pasatiempos
cards|sustantivo|/kɑːrdz/|kards|naipes|Conjunto de cartas para jugar.|We played cards after dinner.|Jugamos a las cartas después de la cena.|pasatiempos
knitting|sustantivo|/ˈnɪtɪŋ/|NI-ting|tejido a palillos|Actividad de hacer prendas con lana y agujas.|Grandma loves knitting scarves.|A la abuela le encanta tejer bufandas.|pasatiempos
sewing|sustantivo|/ˈsoʊɪŋ/|SOU-ing|costura|Actividad de unir telas con aguja e hilo.|Sewing needs patience.|La costura requiere paciencia.|pasatiempos
gardening|sustantivo|/ˈɡɑːrdnɪŋ/|GARD-ning|jardinería|Actividad de cuidar plantas y flores.|Gardening is my hobby.|La jardinería es mi pasatiempo.|pasatiempos
stamp|sustantivo|/stæmp/|stamp|estampilla, sello|Papel pequeño que se pega en las cartas.|I collect old stamps.|Colecciono estampillas antiguas.|pasatiempos
photography|sustantivo|/fəˈtɑːɡrəfi/|fo-TA-gra-fi|fotografía|Arte de tomar fotos.|Photography is her favorite hobby.|La fotografía es su pasatiempo favorito.|pasatiempos
ballet|sustantivo|/bæˈleɪ/|ba-LEI|ballet|Danza con pasos muy elegantes.|She takes ballet lessons.|Ella toma clases de ballet.|pasatiempos
poetry|sustantivo|/ˈpoʊətri/|POU-e-tri|poesía|Escritos en verso que expresan sentimientos.|We read poetry in class.|Leemos poesía en clase.|pasatiempos
festival|sustantivo|/ˈfɛstəvəl/|FES-ti-vol|festival|Gran fiesta con música, comida o espectáculos.|The town has a music festival.|El pueblo tiene un festival de música.|fiestas
picnic|sustantivo|/ˈpɪknɪk/|PIK-nik|picnic|Comida al aire libre.|We had a picnic by the lake.|Hicimos un picnic junto al lago.|fiestas
fireworks|sustantivo|/ˈfaɪərˌwɜːrks/|FAIR-uerks|fuegos artificiales|Cohetes que explotan con luces en el cielo.|We watched the fireworks at midnight.|Vimos los fuegos artificiales a medianoche.|fiestas
costume|sustantivo|/ˈkɑːstuːm/|KAS-tuum|disfraz|Ropa especial que se usa para parecer otro personaje.|My costume is a pirate.|Mi disfraz es de pirata.|fiestas
parade|sustantivo|/pəˈreɪd/|pa-REID|desfile|Marcha de personas por la calle con música.|The parade passed in front of our school.|El desfile pasó frente a nuestro colegio.|fiestas
ceremony|sustantivo|/ˈsɛrəˌmoʊni/|SE-re-mou-ni|ceremonia|Acto solemne para celebrar algo.|The ceremony starts at five.|La ceremonia empieza a las cinco.|fiestas
celebration|sustantivo|/ˌsɛləˈbreɪʃən/|se-le-BREI-shon|celebración|Fiesta para recordar algo feliz.|The celebration lasted all night.|La celebración duró toda la noche.|fiestas
wedding|sustantivo|/ˈwɛdɪŋ/|UE-ding|matrimonio, boda|Ceremonia en que dos personas se casan.|We went to my uncle's wedding.|Fuimos a la boda de mi tío.|fiestas
invitation|sustantivo|/ˌɪnvəˈteɪʃən/|in-vi-TEI-shon|invitación|Aviso para pedir a alguien que venga a un evento.|I got an invitation to the party.|Recibí una invitación a la fiesta.|fiestas
environment|sustantivo|/ɪnˈvaɪrənmənt/|in-VAI-ron-ment|medioambiente|Todo lo que rodea a los seres vivos: aire, agua, tierra.|We must protect the environment.|Debemos proteger el medioambiente.|naturaleza
pollution|sustantivo|/pəˈluːʃən/|po-LUU-shon|contaminación|Suciedad que daña el aire, el agua o el suelo.|Pollution makes the air dirty.|La contaminación ensucia el aire.|naturaleza
plastic|sustantivo|/ˈplæstɪk/|PLAS-tik|plástico|Material liviano que no se pudre fácilmente.|Plastic bottles can be recycled.|Las botellas de plástico se pueden reciclar.|naturaleza
energy|sustantivo|/ˈɛnərdʒi/|E-ner-yi|energía|Fuerza que permite que algo se mueva o funcione.|Solar energy comes from the sun.|La energía solar viene del sol.|naturaleza
electricity|sustantivo|/ɪˌlɛkˈtrɪsəti/|i-lek-TRI-si-ti|electricidad|Energía que hace funcionar las luces y los aparatos.|The storm cut the electricity.|La tormenta cortó la electricidad.|naturaleza
climate|sustantivo|/ˈklaɪmɪt/|KLAI-mit|clima|Tiempo que hace en un lugar durante muchos años.|The climate in the north is dry.|El clima del norte es seco.|naturaleza
global warming|sustantivo|/ˌɡloʊbəl ˈwɔːrmɪŋ/|GLOU-bol UOR-ming|calentamiento global|Aumento de la temperatura de la Tierra.|Global warming melts the glaciers.|El calentamiento global derrite los glaciares.|naturaleza
species|sustantivo|/ˈspiːʃiːz/|SPII-shiis|especie|Tipo de animal o planta.|This bird is a rare species.|Esta ave es una especie rara.|naturaleza
nature|sustantivo|/ˈneɪtʃər/|NEI-cher|naturaleza|Plantas, animales y paisajes que no hizo el ser humano.|I love walking in nature.|Me encanta caminar en la naturaleza.|naturaleza
wildlife|sustantivo|/ˈwaɪldˌlaɪf/|UAILD-laif|fauna silvestre|Animales que viven libres en la naturaleza.|The park protects wildlife.|El parque protege la fauna silvestre.|naturaleza
coral|sustantivo|/ˈkɔːrəl/|KO-ral|coral|Animal marino que forma estructuras duras de colores.|Coral grows in warm seas.|El coral crece en mares cálidos.|naturaleza
swamp|sustantivo|/swɑːmp/|suamp|pantano|Terreno con agua poco profunda y mucho barro.|Frogs live in the swamp.|Las ranas viven en el pantano.|naturaleza
canyon|sustantivo|/ˈkænjən/|KA-nyon|cañón|Valle muy profundo y angosto con paredes de roca.|A river runs through the canyon.|Un río corre por el cañón.|naturaleza
peak|sustantivo|/piːk/|piik|cima|Punto más alto de una montaña.|We reached the peak at noon.|Llegamos a la cima al mediodía.|naturaleza
bay|sustantivo|/beɪ/|bei|bahía|Parte del mar que entra en la tierra.|The boats rest in the bay.|Los botes descansan en la bahía.|naturaleza
peninsula|sustantivo|/pəˈnɪnsələ/|pe-NIN-su-la|península|Tierra rodeada de agua casi por todos lados.|Italy is a peninsula.|Italia es una península.|naturaleza
dune|sustantivo|/duːn/|duun|duna|Colina de arena formada por el viento.|We slid down the dune.|Nos deslizamos por la duna.|naturaleza
drought|sustantivo|/draʊt/|draut|sequía|Tiempo largo sin lluvia.|The drought dried the fields.|La sequía secó los campos.|naturaleza
hurricane|sustantivo|/ˈhɜːrəˌkeɪn/|JE-ri-kein|huracán|Tormenta muy fuerte con viento y lluvia.|The hurricane damaged many houses.|El huracán dañó muchas casas.|naturaleza
tornado|sustantivo|/tɔːrˈneɪdoʊ/|tor-NEI-dou|tornado|Columna de aire que gira muy rápido.|The tornado lifted the roof.|El tornado levantó el techo.|naturaleza
wildfire|sustantivo|/ˈwaɪldˌfaɪər/|UAILD-fair|incendio forestal|Fuego grande que se propaga por el bosque.|A wildfire burned the hill.|Un incendio forestal quemó el cerro.|naturaleza
meadow|sustantivo|/ˈmɛdoʊ/|ME-dou|pradera|Campo con pasto y flores.|Cows eat in the meadow.|Las vacas comen en la pradera.|naturaleza
reef|sustantivo|/riːf/|riif|arrecife|Línea de rocas o coral cerca de la superficie del mar.|Fish live near the reef.|Los peces viven cerca del arrecife.|naturaleza
shore|sustantivo|/ʃɔːr/|shor|orilla|Borde de tierra junto al mar o a un lago.|We walked along the shore.|Caminamos por la orilla.|naturaleza
soil|sustantivo|/sɔɪl/|soil|suelo, tierra|Capa de tierra donde crecen las plantas.|The soil is rich and dark.|El suelo es rico y oscuro.|naturaleza
stream|sustantivo|/striːm/|striim|arroyo|Río pequeño y angosto.|A clear stream runs by the farm.|Un arroyo claro pasa junto a la granja.|naturaleza
software|sustantivo|/ˈsɔːftˌwɛr/|SOFT-uer|programa, software|Conjunto de programas de un computador.|This software edits photos.|Este programa edita fotos.|tecnología
app|sustantivo|/æp/|ap|aplicación|Programa que se usa en un celular.|I downloaded a new app.|Descargué una aplicación nueva.|tecnología
wifi|sustantivo|/ˈwaɪfaɪ/|UAI-fai|wifi|Conexión a internet sin cables.|The library has free wifi.|La biblioteca tiene wifi gratis.|tecnología
network|sustantivo|/ˈnɛtˌwɜːrk/|NET-uerk|red|Conjunto de aparatos o personas conectados entre sí.|The school network is slow today.|La red del colegio está lenta hoy.|tecnología
blog|sustantivo|/blɑːɡ/|blag|blog|Sitio web donde alguien publica textos o fotos.|She writes a blog about travel.|Ella escribe un blog sobre viajes.|tecnología
podcast|sustantivo|/ˈpɑːdˌkæst/|PAD-kast|pódcast|Programa de audio que se escucha por internet.|I listen to a science podcast.|Escucho un pódcast de ciencia.|tecnología
drone|sustantivo|/droʊn/|droun|dron|Aparato que vuela sin piloto a bordo.|The drone took photos of the field.|El dron tomó fotos del campo.|tecnología
satellite|sustantivo|/ˈsætəˌlaɪt/|SA-te-lait|satélite|Aparato que gira alrededor de la Tierra.|A satellite sends signals to the TV.|Un satélite envía señales a la tele.|tecnología
smartphone|sustantivo|/ˈsmɑːrtˌfoʊn/|SMART-foun|teléfono inteligente|Celular que funciona como pequeño computador.|My smartphone has a good camera.|Mi teléfono inteligente tiene una buena cámara.|tecnología
touchscreen|sustantivo|/ˈtʌtʃˌskriːn/|TACH-skriin|pantalla táctil|Pantalla que reacciona cuando la tocas.|The touchscreen is cracked.|La pantalla táctil está rota.|tecnología
cable|sustantivo|/ˈkeɪbəl/|KEI-bol|cable|Hilo de metal cubierto que lleva electricidad o datos.|Plug the cable into the laptop.|Conecta el cable al notebook.|tecnología
text message|sustantivo|/ˈtɛkst ˌmɛsɪdʒ/|TEKST ME-sich|mensaje de texto|Mensaje escrito que se envía por celular.|I sent her a text message.|Le envié un mensaje de texto.|tecnología
virtual|adjetivo|/ˈvɜːrtʃuəl/|VER-chu-al|virtual|Que existe en el computador, no en el mundo físico.|We took a virtual tour of the museum.|Hicimos un recorrido virtual por el museo.|tecnología
digital|adjetivo|/ˈdɪdʒɪtəl/|DI-yi-tol|digital|Que usa números o datos electrónicos.|I have a digital clock.|Tengo un reloj digital.|tecnología
screenshot|sustantivo|/ˈskriːnˌʃɑːt/|SKRIIN-shat|captura de pantalla|Imagen de lo que se ve en una pantalla.|I took a screenshot of the map.|Saqué una captura de pantalla del mapa.|tecnología
virus|sustantivo|/ˈvaɪrəs/|VAI-res|virus|Programa dañino o microbio que causa enfermedad.|The computer has a virus.|El computador tiene un virus.|tecnología
data|sustantivo|/ˈdeɪtə/|DEI-ta|datos|Información que se guarda o se analiza.|The data is stored on the cloud.|Los datos se guardan en la nube.|tecnología
code|sustantivo|/koʊd/|koud|código|Instrucciones escritas para un computador.|She wrote the code for a game.|Ella escribió el código de un juego.|tecnología
result|sustantivo|/rɪˈzʌlt/|ri-ZALT|resultado|Lo que se obtiene al final de algo.|The result of the test was good.|El resultado de la prueba fue bueno.|ideas
difference|sustantivo|/ˈdɪfrəns/|DI-frens|diferencia|Lo que hace que una cosa no sea igual a otra.|What is the difference between them?|¿Cuál es la diferencia entre ellos?|ideas
pair|sustantivo|/pɛr/|per|par|Dos cosas que van juntas.|I need a new pair of shoes.|Necesito un par de zapatos nuevos.|ideas
group|sustantivo|/ɡruːp/|gruup|grupo|Varias personas o cosas juntas.|We worked in a group.|Trabajamos en grupo.|ideas
type|sustantivo|/taɪp/|taip|tipo|Clase de cosa que comparte rasgos con otras.|What type of music do you like?|¿Qué tipo de música te gusta?|ideas
part|sustantivo|/pɑːrt/|part|parte|Trozo de un todo.|This is my favorite part of the movie.|Esta es mi parte favorita de la película.|ideas
piece|sustantivo|/piːs/|piis|pedazo|Parte separada de algo.|Can I have a piece of cake?|¿Puedo tener un pedazo de torta?|ideas
half|sustantivo|/hæf/|haf|mitad|Una de dos partes iguales.|Cut the apple in half.|Corta la manzana por la mitad.|ideas
amount|sustantivo|/əˈmaʊnt/|a-MAUNT|cantidad|Cuánto hay de algo.|A small amount of salt is enough.|Basta una pequeña cantidad de sal.|ideas
level|sustantivo|/ˈlɛvəl/|LE-vol|nivel|Grado o altura de algo.|My English level is better now.|Mi nivel de inglés es mejor ahora.|ideas
beginning|sustantivo|/bɪˈɡɪnɪŋ/|bi-GI-ning|comienzo|Primera parte de algo.|The beginning of the book is funny.|El comienzo del libro es gracioso.|ideas
middle|sustantivo|/ˈmɪdəl/|MI-dol|medio|Parte que está entre el principio y el final.|Stand in the middle of the room.|Párate en el medio de la sala.|ideas
edge|sustantivo|/ɛdʒ/|ech|borde|Lugar donde algo termina.|Do not stand at the edge.|No te pares en el borde.|ideas
top|sustantivo|/tɑːp/|tap|parte de arriba|Lugar más alto de algo.|The cat is on top of the shelf.|El gato está encima del estante.|ideas
bottom|sustantivo|/ˈbɑːtəm/|BA-tom|fondo, parte de abajo|Lugar más bajo de algo.|The key is at the bottom of the bag.|La llave está al fondo de la bolsa.|ideas
side|sustantivo|/saɪd/|said|lado|Parte de un objeto que no es el frente ni el fondo.|Write on both sides of the paper.|Escribe en ambos lados del papel.|ideas
center|sustantivo|/ˈsɛntər/|SEN-ter|centro|Punto del medio.|The fountain is in the center of the square.|La fuente está en el centro de la plaza.|ideas
surface|sustantivo|/ˈsɜːrfɪs/|SER-fis|superficie|Parte de afuera de algo.|The surface of the lake is calm.|La superficie del lago está tranquila.|ideas
area|sustantivo|/ˈɛriə/|E-ri-a|área, zona|Parte de un lugar.|This area is quiet at night.|Esta zona es tranquila de noche.|ideas
weight|sustantivo|/weɪt/|ueit|peso|Cuánto pesa algo.|The weight of the box is ten kilos.|El peso de la caja es diez kilos.|ideas
height|sustantivo|/haɪt/|jait|altura|Distancia desde el suelo hasta lo más alto de algo.|What is your height?|¿Cuánto mides?|ideas
length|sustantivo|/lɛŋkθ/|lenkz|largo|Medida de un extremo al otro.|Measure the length of the table.|Mide el largo de la mesa.|ideas
width|sustantivo|/wɪdθ/|uidz|ancho|Medida de un lado a otro.|The width of the door is one meter.|El ancho de la puerta es un metro.|ideas
distance|sustantivo|/ˈdɪstəns/|DIS-tens|distancia|Espacio entre dos puntos.|The distance to school is two miles.|La distancia al colegio es de dos millas.|ideas
speed|sustantivo|/spiːd/|spiid|velocidad|Qué tan rápido se mueve algo.|The car drove at high speed.|El auto iba a gran velocidad.|ideas
language|sustantivo|/ˈlæŋɡwɪdʒ/|LANG-guich|idioma|Sistema de palabras que usa un pueblo para hablar.|She speaks three languages.|Ella habla tres idiomas.|sociedad
culture|sustantivo|/ˈkʌltʃər/|KAL-cher|cultura|Costumbres, arte y creencias de un pueblo.|Chilean culture is rich and diverse.|La cultura chilena es rica y diversa.|sociedad
tradition|sustantivo|/trəˈdɪʃən/|tra-DI-shon|tradición|Costumbre que pasa de generación en generación.|It is a tradition to eat empanadas in September.|Es una tradición comer empanadas en septiembre.|sociedad
law|sustantivo|/lɔː/|lo|ley|Regla que deben cumplir todos en un país.|The law protects children.|La ley protege a los niños.|sociedad
freedom|sustantivo|/ˈfriːdəm/|FRII-dom|libertad|Posibilidad de actuar y pensar sin que otros te obliguen.|Freedom of speech is important.|La libertad de expresión es importante.|sociedad
peace|sustantivo|/piːs/|piis|paz|Situación sin guerra ni peleas.|The two countries live in peace.|Los dos países viven en paz.|sociedad
war|sustantivo|/wɔːr/|uor|guerra|Lucha armada entre países o grupos.|The war ended many years ago.|La guerra terminó hace muchos años.|sociedad
government|sustantivo|/ˈɡʌvərnmənt/|GA-vern-ment|gobierno|Grupo de personas que dirige un país.|The government built a new bridge.|El gobierno construyó un puente nuevo.|sociedad
election|sustantivo|/ɪˈlɛkʃən/|i-LEK-shon|elección|Votación para escoger a una persona.|The class election is on Monday.|La elección del curso es el lunes.|sociedad
citizen|sustantivo|/ˈsɪtəzən/|SI-ti-sen|ciudadano|Persona que vive en un país con sus derechos y deberes.|Every citizen can vote at eighteen.|Todo ciudadano puede votar a los dieciocho.|sociedad
community|sustantivo|/kəˈmjuːnəti/|ko-MIU-ni-ti|comunidad|Grupo de personas que viven en un mismo lugar.|Our community cleans the park.|Nuestra comunidad limpia el parque.|sociedad
volunteer|sustantivo|/ˌvɑːlənˈtɪr/|va-lon-TIR|voluntario|Persona que ayuda sin recibir pago.|A volunteer reads to the children.|Un voluntario lee a los niños.|sociedad
charity|sustantivo|/ˈtʃærəti/|CHA-ri-ti|obra benéfica|Organización que ayuda a quienes lo necesitan.|We collected food for charity.|Juntamos comida para una obra benéfica.|sociedad
moment|sustantivo|/ˈmoʊmənt/|MOU-ment|momento|Espacio de tiempo muy breve.|Wait a moment, please.|Espera un momento, por favor.|tiempo
appointment|sustantivo|/əˈpɔɪntmənt/|a-POINT-ment|cita|Hora fijada para ver a alguien.|I have a dentist appointment today.|Tengo cita con el dentista hoy.|tiempo
deadline|sustantivo|/ˈdɛdˌlaɪn/|DED-lain|plazo|Fecha límite para terminar algo.|The deadline is next Friday.|El plazo es el próximo viernes.|tiempo
date|sustantivo|/deɪt/|deit|fecha|Día, mes y año de algo.|What is today's date?|¿Cuál es la fecha de hoy?|tiempo
dawn|sustantivo|/dɔːn/|don|amanecer|Primeras luces del día.|Birds sing at dawn.|Los pájaros cantan al amanecer.|tiempo
sunrise|sustantivo|/ˈsʌnˌraɪz/|SAN-raiz|salida del sol|Momento en que el sol aparece.|We saw the sunrise from the hill.|Vimos la salida del sol desde el cerro.|tiempo
sunset|sustantivo|/ˈsʌnˌsɛt/|SAN-set|puesta del sol|Momento en que el sol desaparece.|The sunset was orange and pink.|La puesta del sol fue naranja y rosada.|tiempo
future|sustantivo|/ˈfjuːtʃər/|FIU-cher|futuro|Tiempo que vendrá.|What do you want to be in the future?|¿Qué quieres ser en el futuro?|tiempo
present|sustantivo|/ˈprɛzənt/|PRE-sent|presente|Tiempo en que estamos ahora.|Live in the present.|Vive en el presente.|tiempo
dozen|numeral|/ˈdʌzən/|DA-sen|docena|Conjunto de doce cosas.|A dozen eggs, please.|Una docena de huevos, por favor.|números
million|numeral|/ˈmɪljən/|MIL-yon|millón|El número 1.000.000.|The city has a million people.|La ciudad tiene un millón de personas.|números
billion|numeral|/ˈbɪljən/|BIL-yon|mil millones|El número 1.000.000.000.|A billion is a thousand millions.|Mil millones es un billón en inglés.|números
percent|sustantivo|/pərˈsɛnt/|per-SENT|por ciento|Parte de cada cien.|Fifty percent of the class passed.|El cincuenta por ciento del curso aprobó.|números
sixth|numeral|/sɪksθ/|siksz|sexto|Lugar número seis.|I am in the sixth grade.|Estoy en sexto básico.|números
seventh|numeral|/ˈsɛvənθ/|SE-venz|séptimo|Lugar número siete.|He finished seventh in the race.|Terminó séptimo en la carrera.|números
eighth|numeral|/eɪtθ/|eitz|octavo|Lugar número ocho.|Her seat is the eighth in the row.|Su asiento es el octavo de la fila.|números
ninth|numeral|/naɪnθ/|nainz|noveno|Lugar número nueve.|The ninth day was sunny.|El noveno día estuvo soleado.|números
tenth|numeral|/tɛnθ/|tenz|décimo|Lugar número diez.|This is my tenth try.|Este es mi décimo intento.|números
twentieth|numeral|/ˈtwɛntiəθ/|TUEN-ti-ez|vigésimo|Lugar número veinte.|It is the twentieth of May.|Es el veinte de mayo.|números
quarter|sustantivo|/ˈkwɔːrtər/|KUOR-ter|cuarto|Una de cuatro partes iguales.|A quarter of the pizza is left.|Queda un cuarto de la pizza.|números
couple|sustantivo|/ˈkʌpəl/|KA-pol|par, pareja|Dos personas o cosas.|A couple of friends came over.|Un par de amigos vinieron a casa.|números
careless|adjetivo|/ˈkɛrləs/|KER-les|descuidado|Que no pone atención al hacer algo.|A careless mistake cost him a point.|Un error por descuido le costó un punto.|descripciones
dull|adjetivo|/dʌl/|dal|aburrido, sin brillo|Poco interesante o sin brillo.|The knife is dull.|El cuchillo no tiene filo.|descripciones
eager|adjetivo|/ˈiːɡər/|II-ger|ansioso, deseoso|Con muchas ganas de hacer algo.|The kids are eager to start.|Los niños están ansiosos por comenzar.|descripciones
equal|adjetivo|/ˈiːkwəl/|II-kual|igual|Del mismo valor o tamaño.|The two halves are equal.|Las dos mitades son iguales.|descripciones
fierce|adjetivo|/fɪrs/|firs|feroz|Muy fuerte y agresivo.|The fierce lion roared.|El feroz león rugió.|descripciones
flat|adjetivo|/flæt/|flat|plano|Liso, sin partes altas ni bajas.|The land here is flat.|El terreno aquí es plano.|descripciones
foolish|adjetivo|/ˈfuːlɪʃ/|FUU-lish|tonto|Poco sensato.|It was foolish to leave the door open.|Fue tonto dejar la puerta abierta.|descripciones
mysterious|adjetivo|/mɪˈstɪriəs/|mis-TI-ri-es|misterioso|Que no se puede explicar fácilmente.|A mysterious light shone in the forest.|Una luz misteriosa brillaba en el bosque.|descripciones
official|adjetivo|/əˈfɪʃəl/|o-FI-shol|oficial|Que viene de una autoridad.|This is the official school flag.|Esta es la bandera oficial del colegio.|descripciones
ordinary|adjetivo|/ˈɔːrdənɛri/|OR-di-ne-ri|común|Normal, sin nada especial.|It was an ordinary day.|Fue un día común.|descripciones
plain|adjetivo|/pleɪn/|plein|sencillo, liso|Sin adornos.|She wore a plain white shirt.|Ella usaba una camisa blanca lisa.|descripciones
private|adjetivo|/ˈpraɪvət/|PRAI-vit|privado|Que es solo de una persona o de un grupo.|This is a private beach.|Esta es una playa privada.|descripciones
public|adjetivo|/ˈpʌblɪk/|PA-blik|público|Que es de todos.|The library is a public place.|La biblioteca es un lugar público.|descripciones
reliable|adjetivo|/rɪˈlaɪəbəl/|ri-LAI-a-bol|confiable|En quien o en lo que se puede confiar.|He is a reliable friend.|Él es un amigo confiable.|descripciones
scary|adjetivo|/ˈskɛri/|SKE-ri|que da miedo|Que asusta.|That movie was scary.|Esa película daba miedo.|descripciones
separate|adjetivo|/ˈsɛpərət/|SE-pe-rit|separado|Que no está unido a otra cosa.|We sleep in separate rooms.|Dormimos en piezas separadas.|descripciones
single|adjetivo|/ˈsɪŋɡəl/|SIN-gol|único, soltero|Solo uno.|I did not eat a single cookie.|No me comí ni una galleta.|descripciones
sleepy|adjetivo|/ˈsliːpi/|SLII-pi|con sueño|Que tiene ganas de dormir.|The baby is sleepy.|El bebé tiene sueño.|descripciones
slippery|adjetivo|/ˈslɪpəri/|SLI-pe-ri|resbaloso|Que hace que uno resbale.|The floor is slippery.|El piso está resbaloso.|descripciones
sticky|adjetivo|/ˈstɪki/|STI-ki|pegajoso|Que se pega a las manos u otras cosas.|My hands are sticky with honey.|Mis manos están pegajosas de miel.|descripciones
sudden|adjetivo|/ˈsʌdən/|SA-den|repentino|Que pasa de pronto.|A sudden noise woke me up.|Un ruido repentino me despertó.|descripciones
suitable|adjetivo|/ˈsuːtəbəl/|SUU-ta-bol|adecuado|Que sirve para algo en particular.|This jacket is suitable for the cold.|Esta chaqueta es adecuada para el frío.|descripciones
tight|adjetivo|/taɪt/|tait|apretado|Que queda muy ajustado.|These shoes are too tight.|Estos zapatos están muy apretados.|descripciones
tough|adjetivo|/tʌf/|taf|duro, difícil|Fuerte, o difícil de cortar o de lograr.|The meat is tough.|La carne está dura.|descripciones
unusual|adjetivo|/ʌnˈjuːʒuəl/|an-IU-shu-al|inusual|Que no es normal.|It is unusual to see snow here.|Es inusual ver nieve aquí.|descripciones
useful|adjetivo|/ˈjuːsfəl/|IUS-ful|útil|Que sirve para algo.|A map is useful on a trip.|Un mapa es útil en un viaje.|descripciones
useless|adjetivo|/ˈjuːsləs/|IUS-les|inútil|Que no sirve para nada.|The broken umbrella is useless.|El paraguas roto es inútil.|descripciones
valuable|adjetivo|/ˈvæljuəbəl/|VAL-iu-a-bol|valioso|Que vale mucho.|This ring is very valuable.|Este anillo es muy valioso.|descripciones
wooden|adjetivo|/ˈwʊdən/|UU-den|de madera|Hecho de madera.|We sat on a wooden bench.|Nos sentamos en una banca de madera.|descripciones
golden|adjetivo|/ˈɡoʊldən/|GOUL-den|dorado|De color oro o hecho de oro.|The golden sun set behind the hills.|El sol dorado se ocultó tras los cerros.|descripciones
silver|adjetivo|/ˈsɪlvər/|SIL-ver|plateado|De color plata o hecho de plata.|She wore a silver necklace.|Ella llevaba un collar de plata.|descripciones
metal|sustantivo|/ˈmɛtəl/|ME-tol|metal|Material duro y brillante, como el hierro.|The key is made of metal.|La llave está hecha de metal.|descripciones
abroad|adverbio|/əˈbrɔːd/|a-BROD|en el extranjero|En otro país.|My uncle works abroad.|Mi tío trabaja en el extranjero.|adverbios
completely|adverbio|/kəmˈpliːtli/|kom-PLIIT-li|completamente|Del todo.|I completely forgot my homework.|Olvidé por completo mi tarea.|adverbios
especially|adverbio|/ɪˈspɛʃəli/|is-PE-sha-li|especialmente|De manera particular.|I like fruit, especially grapes.|Me gusta la fruta, sobre todo las uvas.|adverbios
fortunately|adverbio|/ˈfɔːrtʃənətli/|FOR-chu-nit-li|afortunadamente|Por buena suerte.|Fortunately, nobody was hurt.|Afortunadamente, nadie salió herido.|adverbios
unfortunately|adverbio|/ʌnˈfɔːrtʃənətli/|an-FOR-chu-nit-li|desafortunadamente|Por mala suerte.|Unfortunately, the bus left early.|Desafortunadamente, el bus salió temprano.|adverbios
hardly|adverbio|/ˈhɑːrdli/|JARD-li|apenas|Casi nada.|I can hardly hear you.|Apenas te puedo oír.|adverbios
immediately|adverbio|/ɪˈmiːdiətli/|i-MII-diit-li|inmediatamente|Sin esperar.|Come here immediately.|Ven aquí de inmediato.|adverbios
nearby|adverbio|/ˌnɪrˈbaɪ/|nir-BAI|cerca|A poca distancia.|There is a bakery nearby.|Hay una panadería cerca.|adverbios
nowadays|adverbio|/ˈnaʊəˌdeɪz/|NAU-a-deis|hoy en día|En los tiempos actuales.|Nowadays, many people use phones.|Hoy en día, mucha gente usa celulares.|adverbios
recently|adverbio|/ˈriːsəntli/|RII-sent-li|recientemente|Hace poco tiempo.|I recently moved to a new house.|Me cambié hace poco a una casa nueva.|adverbios
simply|adverbio|/ˈsɪmpli/|SIM-pli|simplemente|De forma sencilla.|Simply press the green button.|Simplemente presiona el botón verde.|adverbios
straight|adverbio|/streɪt/|streit|derecho|Sin desviarse.|Go straight for two blocks.|Sigue derecho por dos cuadras.|adverbios
upstairs|adverbio|/ˌʌpˈstɛrz/|ap-STERS|arriba, al piso de arriba|En el piso superior.|The bedrooms are upstairs.|Los dormitorios están arriba.|adverbios
downstairs|adverbio|/ˌdaʊnˈstɛrz/|daun-STERS|abajo, al piso de abajo|En el piso inferior.|Dinner is ready downstairs.|La cena está lista abajo.|adverbios
ahead|adverbio|/əˈhɛd/|a-JED|adelante|Hacia el frente.|The road ahead is closed.|El camino de adelante está cerrado.|adverbios
forward|adverbio|/ˈfɔːrwərd/|FOR-uerd|hacia adelante|Hacia el frente.|Take two steps forward.|Da dos pasos hacia adelante.|adverbios
indoors|adverbio|/ˌɪnˈdɔːrz/|in-DORS|adentro|Dentro de un edificio.|We stayed indoors because of the rain.|Nos quedamos adentro por la lluvia.|adverbios
outdoors|adverbio|/ˌaʊtˈdɔːrz/|aut-DORS|al aire libre|Fuera de un edificio.|They play outdoors in summer.|Juegan al aire libre en verano.|adverbios
mostly|adverbio|/ˈmoʊstli/|MOUST-li|mayormente|En su mayor parte.|The class is mostly girls.|El curso es mayormente de niñas.|adverbios
nearly|adverbio|/ˈnɪrli/|NIR-li|casi|Muy cerca de algo.|It is nearly midnight.|Es casi medianoche.|adverbios
anyway|adverbio|/ˈɛniˌweɪ/|E-ni-uei|de todos modos|A pesar de todo.|It rained, but we went anyway.|Llovió, pero fuimos de todos modos.|adverbios
however|adverbio|/haʊˈɛvər/|jau-E-ver|sin embargo|Introduce una idea que contrasta con la anterior.|I like soccer; however, I prefer tennis.|Me gusta el fútbol; sin embargo, prefiero el tenis.|conectores
therefore|adverbio|/ˈðɛrˌfɔːr/|DER-for|por lo tanto|Introduce una consecuencia.|It was late; therefore, we went home.|Era tarde; por lo tanto, nos fuimos a casa.|conectores
unless|conjunción|/ənˈlɛs/|an-LES|a menos que|Introduce una condición que debe faltar.|We will go unless it rains.|Iremos a menos que llueva.|conectores
whether|conjunción|/ˈwɛðər/|UE-der|si|Se usa para indicar dos posibilidades.|I don't know whether he is home.|No sé si él está en casa.|conectores
despite|preposición|/dɪˈspaɪt/|dis-PAIT|a pesar de|Indica que algo ocurre aunque exista un obstáculo.|Despite the rain, we played outside.|A pesar de la lluvia, jugamos afuera.|conectores
except|preposición|/ɪkˈsɛpt/|ik-SEPT|excepto|Sin incluir a alguien o algo.|Everyone came except Paul.|Todos vinieron excepto Paul.|conectores
opposite|preposición|/ˈɑːpəzɪt/|A-po-sit|frente a|En el lado contrario.|The bank is opposite the park.|El banco está frente al parque.|conectores
within|preposición|/wɪˈðɪn/|ui-DIN|dentro de|En el interior o en un plazo.|We will finish within an hour.|Terminaremos dentro de una hora.|conectores
according to|preposición|/əˈkɔːrdɪŋ tuː/|a-KOR-ding tu|según|Basado en lo que dice alguien o algo.|According to the map, the lake is near.|Según el mapa, el lago está cerca.|conectores
instead of|preposición|/ɪnˈstɛd əv/|ins-TED ov|en lugar de|Reemplazando a otra cosa.|I drank water instead of juice.|Tomé agua en lugar de jugo.|conectores
such as|expresión|/sʌtʃ æz/|sach as|como, por ejemplo|Introduce ejemplos.|I like fruits such as apples and pears.|Me gustan frutas como manzanas y peras.|conectores
for example|expresión|/fər ɪɡˈzæmpəl/|for ig-SAM-pol|por ejemplo|Introduce un ejemplo.|Many animals live here, for example, foxes.|Aquí viven muchos animales, por ejemplo, zorros.|conectores
in fact|expresión|/ɪn fækt/|in fakt|de hecho|Introduce algo que confirma o refuerza lo dicho.|It is cold; in fact, it is freezing.|Hace frío; de hecho, está helando.|conectores
at first|expresión|/æt fɜːrst/|at ferst|al principio|En un primer momento.|At first, I was nervous.|Al principio, estaba nervioso.|conectores
at last|expresión|/æt læst/|at last|por fin|Después de mucho tiempo.|At last, the rain stopped.|Por fin, paró la lluvia.|conectores
on time|expresión|/ɑːn taɪm/|on taim|a tiempo|A la hora correcta.|The bus arrived on time.|El bus llegó a tiempo.|conectores
by the way|expresión|/baɪ ðə weɪ/|bai da uei|por cierto|Introduce un comentario que se te acaba de ocurrir.|By the way, do you have my book?|Por cierto, ¿tienes mi libro?|conectores
as well|expresión|/æz wɛl/|as uel|también|Además de lo ya dicho.|I like tea as well.|También me gusta el té.|conectores
no problem|expresión|/noʊ ˈprɑːbləm/|nou PRA-blem|no hay problema|Se dice cuando algo no es molestia.|No problem, I can help you.|No hay problema, puedo ayudarte.|expresiones
take care|expresión|/teɪk kɛr/|teik ker|cuídate|Se dice al despedirse.|Take care and see you soon.|Cuídate y nos vemos pronto.|expresiones
never mind|expresión|/ˈnɛvər maɪnd/|NE-ver maind|no importa|Se dice para decir que no es importante.|Never mind, I found it.|No importa, lo encontré.|expresiones
how about|expresión|/haʊ əˈbaʊt/|jau a-BAUT|¿qué tal si...?|Se usa para hacer una propuesta.|How about a walk in the park?|¿Qué tal un paseo por el parque?|expresiones
I'd like|expresión|/aɪd laɪk/|aid laik|me gustaría|Forma educada de pedir algo.|I'd like a glass of water.|Me gustaría un vaso de agua.|expresiones
what's wrong|expresión|/wʌts rɔːŋ/|uats rong|¿qué te pasa?|Pregunta para saber si hay un problema.|What's wrong? You look sad.|¿Qué te pasa? Te ves triste.|expresiones
I agree|expresión|/aɪ əˈɡriː/|ai a-GRII|estoy de acuerdo|Se dice cuando piensas igual que otra persona.|I agree with your idea.|Estoy de acuerdo con tu idea.|expresiones
look out|expresión|/lʊk aʊt/|luk aut|¡cuidado!|Se grita para avisar de un peligro.|Look out! A car is coming.|¡Cuidado! Viene un auto.|expresiones
well done|expresión|/wɛl dʌn/|uel dan|bien hecho|Se dice para felicitar a alguien.|Well done, you won the game!|¡Bien hecho, ganaste el juego!|expresiones
bad luck|expresión|/bæd lʌk/|bad lak|mala suerte|Se dice cuando algo sale mal.|Bad luck! You missed the goal.|¡Mala suerte! Fallaste el gol.|expresiones
don't worry|expresión|/doʊnt ˈwɜːri/|dount UE-ri|no te preocupes|Se dice para dar calma.|Don't worry, everything is fine.|No te preocupes, todo está bien.|expresiones
calm down|expresión|/kɑːm daʊn/|kam daun|cálmate|Se dice a alguien que está muy nervioso o enojado.|Calm down and breathe slowly.|Cálmate y respira despacio.|expresiones
come on|expresión|/kʌm ɑːn/|kam on|vamos, ánimo|Se dice para animar o apurar a alguien.|Come on, we can do it!|¡Vamos, podemos hacerlo!|expresiones
"""

VERBOS = """
allow|/əˈlaʊ/|allowed|permitió|permitir|permite|Dejar que alguien haga algo.|My parents allow me to play outside.|Mis padres me permiten jugar afuera.
attack|/əˈtæk/|attacked|atacó|atacar|ataca|Lanzarse contra alguien para hacerle daño.|The dog attacked the ball.|El perro se lanzó contra la pelota.
boil|/bɔɪl/|boiled|hirvió|hervir|hierve|Calentar un líquido hasta que burbujea.|I boil water for tea.|Hiervo agua para el té.
bury|/ˈbɛri/|buried|enterró|enterrar|entierra|Cubrir algo con tierra.|The dog buried a bone.|El perro enterró un hueso.
chat|/tʃæt/|chatted|conversó|conversar|conversa|Hablar de manera relajada.|We chatted for an hour.|Conversamos durante una hora.
check|/tʃɛk/|checked|revisó|revisar|revisa|Mirar algo para asegurarse de que está bien.|She checked her homework twice.|Ella revisó su tarea dos veces.
cheer|/tʃɪr/|cheered|vitoreó|vitorear|vitorea|Gritar para animar a alguien.|The crowd cheered for the team.|La multitud vitoreó al equipo.
complain|/kəmˈpleɪn/|complained|se quejó|quejarse|se queja|Decir que algo no te gusta.|He complained about the noise.|Él se quejó del ruido.
cover|/ˈkʌvər/|covered|cubrió|cubrir|cubre|Poner algo encima de otra cosa.|She covered the pot with a lid.|Ella cubrió la olla con una tapa.
damage|/ˈdæmɪdʒ/|damaged|dañó|dañar|daña|Estropear algo.|The storm damaged the roof.|La tormenta dañó el techo.
deliver|/dɪˈlɪvər/|delivered|entregó|entregar|entrega|Llevar algo a la persona que lo espera.|The mail carrier delivered a letter.|El cartero entregó una carta.
destroy|/dɪˈstrɔɪ/|destroyed|destruyó|destruir|destruye|Dejar algo tan dañado que ya no sirve.|The fire destroyed the old barn.|El fuego destruyó el viejo granero.
escape|/ɪˈskeɪp/|escaped|escapó|escapar|escapa|Salir de un lugar donde estabas encerrado.|The rabbit escaped from its cage.|El conejo escapó de su jaula.
fail|/feɪl/|failed|fracasó|fracasar|fracasa|No lograr lo que se intentaba.|He failed the driving test.|Él no pasó el examen de conducir.
fold|/foʊld/|folded|dobló|doblar|dobla|Doblar algo sobre sí mismo.|I folded the paper in half.|Doblé el papel por la mitad.
greet|/ɡriːt/|greeted|saludó|saludar|saluda|Decir hola a alguien.|She greeted every guest.|Ella saludó a cada invitado.
guard|/ɡɑːrd/|guarded|vigiló|vigilar|vigila|Cuidar un lugar para que nadie entre.|A dog guards the farm.|Un perro vigila la granja.
kiss|/kɪs/|kissed|besó|besar|besa|Tocar a alguien con los labios en señal de cariño.|Mom kissed me goodnight.|Mamá me dio un beso de buenas noches.
knock|/nɑːk/|knocked|golpeó|golpear|golpea|Pegar suavemente en una puerta.|Someone knocked on the door.|Alguien golpeó la puerta.
offer|/ˈɔːfər/|offered|ofreció|ofrecer|ofrece|Poner algo a disposición de otra persona.|He offered me a seat.|Él me ofreció un asiento.
order|/ˈɔːrdər/|ordered|pidió|pedir|pide|Pedir comida o un producto.|We ordered two pizzas.|Pedimos dos pizzas.
prefer|/prɪˈfɜːr/|preferred|prefirió|preferir|prefiere|Escoger algo antes que otra cosa.|I prefer tea to coffee.|Prefiero el té al café.
pretend|/prɪˈtɛnd/|pretended|fingió|fingir|finge|Hacer como si algo fuera verdad en un juego.|The children pretended to be pirates.|Los niños fingieron ser piratas.
provide|/prəˈvaɪd/|provided|proporcionó|proporcionar|proporciona|Dar lo necesario a alguien.|The school provides books.|El colegio proporciona libros.
refuse|/rɪˈfjuːz/|refused|rechazó|rechazar|rechaza|Decir que no a algo.|He refused the offer.|Él rechazó la oferta.
relax|/rɪˈlæks/|relaxed|se relajó|relajarse|se relaja|Descansar y quedar tranquilo.|I relax after school.|Me relajo después del colegio.
remove|/rɪˈmuːv/|removed|quitó|quitar|quita|Sacar algo de un lugar.|She removed her shoes.|Ella se quitó los zapatos.
rent|/rɛnt/|rented|arrendó|arrendar|arrienda|Pagar por usar algo por un tiempo.|We rented a cabin in the south.|Arrendamos una cabaña en el sur.
scream|/skriːm/|screamed|gritó|gritar|grita|Dar un grito muy fuerte.|The girl screamed with fear.|La niña gritó de miedo.
serve|/sɜːrv/|served|sirvió|servir|sirve|Poner la comida en la mesa.|The waiter served the soup.|El garzón sirvió la sopa.
sign|/saɪn/|signed|firmó|firmar|firma|Escribir tu nombre en un documento.|Dad signed the permission slip.|Papá firmó la autorización.
spill|/spɪl/|spilled|derramó|derramar|derrama|Dejar caer un líquido sin querer.|I spilled juice on the table.|Derramé jugo en la mesa.
stir|/stɜːr/|stirred|revolvió|revolver|revuelve|Mover una mezcla con una cuchara.|She stirred the soup.|Ella revolvió la sopa.
surf|/sɜːrf/|surfed|surfeó|surfear|surfea|Deslizarse sobre las olas con una tabla.|We surfed at the beach.|Surfeamos en la playa.
tidy|/ˈtaɪdi/|tidied|ordenó|ordenar|ordena|Dejar un lugar en orden.|He tidied his room.|Él ordenó su pieza.
tie|/taɪ/|tied|amarró|amarrar|amarra|Unir algo con un nudo.|She tied her shoes.|Ella se amarró los zapatos.
trust|/trʌst/|trusted|confió|confiar|confía|Creer que alguien es honesto o capaz.|I trust my best friend.|Confío en mi mejor amigo.
upload|/ˌʌpˈloʊd/|uploaded|subió|subir|sube|Enviar un archivo a internet.|He uploaded the photos.|Él subió las fotos.
waste|/weɪst/|wasted|desperdició|desperdiciar|desperdicia|Usar algo sin provecho.|Don't waste water.|No desperdicies agua.
wipe|/waɪp/|wiped|limpió|limpiar|limpia|Pasar un paño para quitar suciedad.|She wiped the table.|Ella limpió la mesa.
worry|/ˈwɜːri/|worried|se preocupó|preocuparse|se preocupa|Sentir inquietud por algo.|Mom worries when I am late.|Mamá se preocupa cuando llego tarde.
blow|/bloʊ/|blew|sopló|soplar|sopla|Echar aire por la boca.|She blew out the candles.|Ella sopló las velas.
bite|/baɪt/|bit|mordió|morder|muerde|Cortar o apretar algo con los dientes.|The dog bit the bone.|El perro mordió el hueso.
bend|/bɛnd/|bent|dobló|doblar|dobla|Inclinar o curvar algo.|He bent down to tie his shoes.|Él se agachó a amarrarse los zapatos.
cost|/kɔːst/|cost|costó|costar|cuesta|Tener un precio.|The book cost ten dollars.|El libro costó diez dólares.
freeze|/friːz/|froze|se congeló|congelar|congela|Convertirse en hielo por el frío.|The lake froze in winter.|El lago se congeló en invierno.
hang|/hæŋ/|hung|colgó|colgar|cuelga|Sostener algo desde arriba para que no toque el suelo.|She hung her coat on the hook.|Ella colgó su abrigo en el gancho.
shoot|/ʃuːt/|shot|disparó|disparar|dispara|Lanzar algo con fuerza hacia una meta.|He shot the ball into the net.|Él lanzó el balón a la red.
sink|/sɪŋk/|sank|se hundió|hundirse|se hunde|Irse hacia el fondo del agua.|The boat sank slowly.|El bote se hundió lentamente.
sweep|/swiːp/|swept|barrió|barrer|barre|Limpiar el suelo con una escoba.|He swept the kitchen floor.|Él barrió el piso de la cocina.
tear|/tɛr/|tore|rompió|romper|rompe|Rasgar papel o tela.|She tore the paper in two.|Ella rasgó el papel en dos.
spread|/sprɛd/|spread|esparció|esparcir|esparce|Extender algo sobre una superficie.|He spread butter on the bread.|Él untó mantequilla en el pan.
set|/sɛt/|set|puso|poner|pone|Poner algo en un lugar o a punto de funcionar.|She set the alarm for six.|Ella puso la alarma a las seis.
"""
