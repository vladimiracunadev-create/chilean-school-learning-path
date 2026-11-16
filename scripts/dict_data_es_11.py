"""Diccionario de español de 3.º medio: palabras (sustantivos, adjetivos, adverbios, locuciones y palabras de enlace) y verbos.

Formato de PALABRAS (una por línea, separado por «|»):
    palabra|sílabas|clase|significado|sinónimos|antónimos|ejemplo|tema
Formato de VERBOS:
    infinitivo|sílabas|significado|yo (hoy)|él o ella (hoy)|él o ella (ayer)|él o ella (mañana)|sinónimos|antónimos|ejemplo
Un guion «-» significa que no hay sinónimo o antónimo sencillo para ese nivel.
Textos propios del proyecto: no copian ningún diccionario publicado.
"""

NIVEL = "3-medio"
IDIOMA = "es"

PALABRAS = """
epistemología|e-pis-te-mo-lo-gí-a|sustantivo femenino|Rama de la filosofía que estudia cómo conocemos y qué hace válido un conocimiento.|teoría del conocimiento|-|La epistemología se pregunta si los sentidos bastan para conocer el mundo.|filosofía
ontología|on-to-lo-gí-a|sustantivo femenino|Parte de la filosofía que estudia qué significa existir y qué tipos de cosas existen.|-|-|En la clase de ontología discutimos si los números existen fuera de la mente.|filosofía
metafísica|me-ta-fí-si-ca|sustantivo femenino|Parte de la filosofía que se ocupa de las preguntas últimas sobre la realidad, el ser y el tiempo.|-|-|La metafísica se pregunta qué es el tiempo en realidad.|filosofía
racionalismo|ra-cio-na-lis-mo|sustantivo masculino|Corriente que sostiene que la razón es la fuente principal del conocimiento.|-|empirismo|Descartes es un representante del racionalismo.|filosofía
empirismo|em-pi-ris-mo|sustantivo masculino|Corriente que sostiene que el conocimiento nace de la experiencia y los sentidos.|-|racionalismo|El empirismo defiende que aprendemos observando el mundo.|filosofía
escepticismo|es-cep-ti-cis-mo|sustantivo masculino|Actitud de dudar de que se pueda llegar a una verdad segura.|incredulidad|credulidad|El escepticismo nos ayuda a no creer cualquier noticia.|filosofía
dogmatismo|dog-ma-tis-mo|sustantivo masculino|Forma de pensar que presenta las propias ideas como verdades que no se pueden discutir.|intransigencia|flexibilidad|El dogmatismo impide que dos personas conversen de verdad.|filosofía
relativismo|re-la-ti-vis-mo|sustantivo masculino|Idea de que las verdades y los valores dependen de la época, la cultura o la persona.|-|absolutismo|El relativismo cultural sostiene que cada sociedad tiene sus propias costumbres válidas.|filosofía
utilitarismo|u-ti-li-ta-ris-mo|sustantivo masculino|Teoría ética que considera correcto lo que produce mayor bienestar para la mayoría.|-|-|Según el utilitarismo, conviene elegir la acción que beneficie a más personas.|ética
deontología|de-on-to-lo-gí-a|sustantivo femenino|Conjunto de deberes que rigen el comportamiento correcto en una profesión.|-|-|La deontología médica exige guardar el secreto de los pacientes.|ética
hedonismo|he-do-nis-mo|sustantivo masculino|Doctrina que sostiene que el placer es el objetivo de la vida.|-|ascetismo|El hedonismo busca el placer como meta principal.|filosofía
estoicismo|es-toi-cis-mo|sustantivo masculino|Corriente que enseña a mantener la serenidad frente a lo que no podemos cambiar.|-|-|El estoicismo aconseja aceptar con calma lo inevitable.|filosofía
existencialismo|e-xis-ten-cia-lis-mo|sustantivo masculino|Corriente que pone en el centro la libertad y la responsabilidad de cada persona por su propia vida.|-|-|El existencialismo afirma que cada uno da sentido a su existencia.|filosofía
sofisma|so-fis-ma|sustantivo masculino|Argumento engañoso que se usa para convencer aunque sea incorrecto.|falacia|-|Usó un sofisma para ganar la discusión.|lógica
dialéctica|dia-léc-ti-ca|sustantivo femenino|Arte de razonar y avanzar en el conocimiento confrontando ideas opuestas.|-|-|La dialéctica de Sócrates se basaba en preguntas y respuestas.|filosofía
subjetividad|sub-je-ti-vi-dad|sustantivo femenino|Modo personal de ver las cosas, influido por lo que cada uno siente y piensa.|-|objetividad|La subjetividad se nota cuando alguien opina sobre una película.|argumentación
determinismo|de-ter-mi-nis-mo|sustantivo masculino|Idea de que todo lo que ocurre está causado por hechos anteriores.|-|-|El determinismo plantea dudas sobre si somos realmente libres.|filosofía
altruismo|al-truis-mo|sustantivo masculino|Actitud de ayudar a otros sin esperar nada a cambio.|generosidad|egoísmo|Su altruismo la llevó a trabajar como voluntaria.|ética
egoísmo|e-go-ís-mo|sustantivo masculino|Exceso de amor por uno mismo que hace pensar solo en el propio provecho.|-|altruismo|Por egoísmo no quiso compartir sus apuntes.|ética
intolerancia|in-to-le-ran-cia|sustantivo femenino|Rechazo hacia quienes piensan o viven de manera distinta.|intransigencia|tolerancia|La intolerancia alimenta la discriminación.|ética
heteronomía|he-te-ro-no-mí-a|sustantivo femenino|Situación de quien actúa guiado por normas o voluntades ajenas.|-|autonomía|Obedecer solo por miedo al castigo es una forma de heteronomía.|ética
moralidad|mo-ra-li-dad|sustantivo femenino|Conjunto de principios que distinguen lo correcto de lo incorrecto en una persona o grupo.|ética|inmoralidad|Se discutió la moralidad de esa decisión.|ética
intrínseco|in-trín-se-co|adjetivo|Que pertenece a una cosa por su propia naturaleza.|esencial|extrínseco|El valor intrínseco de la vida no depende de la opinión de nadie.|filosofía
extrínseco|ex-trín-se-co|adjetivo|Que viene de fuera y no forma parte de la naturaleza de algo.|externo|intrínseco|Un premio es una motivación extrínseca.|filosofía
inexorable|i-ne-xo-ra-ble|adjetivo|Que no se puede detener ni evitar.|inevitable|evitable|El paso del tiempo es inexorable.|lenguaje
paradójico|pa-ra-dó-ji-co|adjetivo|Que encierra una contradicción aparente.|contradictorio|-|Es paradójico que tenga tanto dinero y se sienta pobre.|lenguaje
fenomenología|fe-no-me-no-lo-gí-a|sustantivo femenino|Corriente filosófica que describe cómo las cosas se presentan a la conciencia tal como se viven.|-|-|La fenomenología parte de la experiencia vivida y no de teorías previas.|filosofía
idealismo|i-de-a-lis-mo|sustantivo masculino|Postura que afirma que las ideas o la mente son lo más importante para explicar la realidad.|-|materialismo|Para el idealismo, conocemos las cosas a través de las ideas que tenemos de ellas.|filosofía
materialismo|ma-te-ria-lis-mo|sustantivo masculino|Postura que sostiene que todo lo que existe es materia o depende de ella.|-|idealismo|El materialismo explica la mente a partir del funcionamiento del cerebro.|filosofía
positivismo|po-si-ti-vis-mo|sustantivo masculino|Corriente que solo acepta como válido el conocimiento basado en hechos comprobables.|-|-|El positivismo confió en que la ciencia resolvería los problemas de la sociedad.|filosofía
pragmatismo|prag-ma-tis-mo|sustantivo masculino|Postura que valora una idea según los resultados prácticos que produce.|-|-|Por pragmatismo eligió la solución que funcionaba, aunque no fuera la más elegante.|filosofía
nihilismo|ni-hi-lis-mo|sustantivo masculino|Actitud que niega que existan valores o sentido en la vida.|-|-|El nihilismo sostiene que nada tiene un valor definitivo.|filosofía
legitimidad|le-gi-ti-mi-dad|sustantivo femenino|Cualidad de un poder o una decisión que la gente reconoce como justa y válida.|validez|ilegitimidad|El gobierno ganó legitimidad al ser elegido en votaciones limpias.|ciudadanía
jurisprudencia|ju-ris-pru-den-cia|sustantivo femenino|Conjunto de decisiones de los tribunales que sirve de guía para casos parecidos.|-|-|El abogado citó la jurisprudencia de la Corte Suprema.|derecho
fiscalía|fis-ca-lí-a|sustantivo femenino|Institución que investiga los delitos y acusa a los responsables ante un tribunal.|-|-|La fiscalía abrió una investigación por el fraude.|derecho
defensoría|de-fen-so-rí-a|sustantivo femenino|Oficina que protege los derechos de las personas, por ejemplo cuando no pueden pagar un abogado.|-|-|La defensoría asignó un abogado gratuito a la familia.|derecho
parlamentario|par-la-men-ta-rio|sustantivo masculino|Persona elegida para formar parte del Congreso, como diputado o senador.|legislador|-|Un parlamentario presentó el proyecto sobre el uso del agua.|ciudadanía
bancada|ban-ca-da|sustantivo femenino|Grupo de parlamentarios de un mismo partido o alianza.|-|-|La bancada de la oposición votó en contra de la propuesta.|ciudadanía
militante|mi-li-tan-te|sustantivo masculino|Persona inscrita en un partido que participa activamente en él.|afiliado|-|Es militante de su partido desde los dieciocho años.|ciudadanía
elector|e-lec-tor|sustantivo masculino|Persona con derecho a votar.|votante|-|Cada elector debe presentar su carné en la mesa.|ciudadanía
apoderado|a-po-de-ra-do|sustantivo masculino|Adulto responsable de un estudiante ante el colegio, o persona autorizada para actuar en nombre de otra.|representante|-|El apoderado firmó la autorización para la salida.|escuela
cohecho|co-he-cho|sustantivo masculino|Delito que consiste en dar o recibir dinero para que alguien haga algo contrario a su deber.|soborno|-|El funcionario fue acusado de cohecho.|derecho
malversación|mal-ver-sa-ción|sustantivo femenino|Uso indebido del dinero público o ajeno que se tiene a cargo.|desfalco|-|La malversación de fondos dejó sin recursos al proyecto.|derecho
nepotismo|ne-po-tis-mo|sustantivo masculino|Costumbre de dar empleos o favores a familiares sin considerar sus méritos.|favoritismo|-|El nepotismo fue criticado cuando contrató a sus tres primos.|ciudadanía
clientelismo|clien-te-lis-mo|sustantivo masculino|Práctica de ofrecer favores a cambio de apoyo político.|-|-|El clientelismo debilita la confianza en las instituciones.|ciudadanía
autoritarismo|au-to-ri-ta-ris-mo|sustantivo masculino|Forma de gobernar en que el poder se impone sin respetar la opinión de la gente.|despotismo|-|El autoritarismo limita la libertad de expresión.|ciudadanía
totalitarismo|to-ta-li-ta-ris-mo|sustantivo masculino|Sistema en que el Estado controla todos los aspectos de la vida de las personas.|-|-|El totalitarismo prohíbe cualquier forma de oposición.|historia
plutocracia|plu-to-cra-cia|sustantivo femenino|Sistema en que gobiernan las personas más ricas.|-|-|Los críticos hablaban de plutocracia porque solo los ricos influían en las leyes.|historia
descentralización|des-cen-tra-li-za-ción|sustantivo femenino|Traspaso de poder y recursos desde el gobierno central a las regiones o comunas.|-|centralización|La descentralización permite que cada región decida sobre sus asuntos.|ciudadanía
regionalización|re-gio-na-li-za-ción|sustantivo femenino|Organización de un país en regiones con ciertas funciones propias.|-|-|La regionalización de los años setenta dividió Chile en trece regiones.|historia
gobernanza|go-ber-nan-za|sustantivo femenino|Forma en que se toman y aplican las decisiones entre el Estado y la sociedad.|-|-|Una buena gobernanza incluye a las comunidades en las decisiones.|ciudadanía
institucionalidad|ins-ti-tu-cio-na-li-dad|sustantivo femenino|Conjunto de organismos y reglas que sostienen el funcionamiento de un país.|-|-|La institucionalidad democrática garantiza que se respeten las leyes.|ciudadanía
amparo|am-pa-ro|sustantivo masculino|Protección que se da a alguien que lo necesita.|protección|desamparo|El recurso de amparo defiende a quien fue detenido sin motivo.|derecho
apelación|a-pe-la-ción|sustantivo femenino|Solicitud para que un tribunal superior revise una sentencia.|-|-|La defensa presentó una apelación contra el fallo.|derecho
querella|que-re-lla|sustantivo femenino|Acusación formal que se presenta ante un juez por un delito.|denuncia|-|La familia presentó una querella contra la empresa.|derecho
absolución|ab-so-lu-ción|sustantivo femenino|Decisión del tribunal que declara que el acusado no es culpable.|-|condena|La absolución llegó después de un juicio largo.|derecho
condena|con-de-na|sustantivo femenino|Castigo que impone un tribunal a quien es declarado culpable.|pena|absolución|La condena fue de tres años de libertad vigilada.|derecho
prescripción|pres-crip-ción|sustantivo femenino|Pérdida de un derecho o de una acción legal por el paso del tiempo.|caducidad|-|El delito no se castigó por prescripción.|derecho
impunidad|im-pu-ni-dad|sustantivo femenino|Falta de castigo para quien cometió un delito.|-|castigo|La impunidad deja a las víctimas sin justicia.|derecho
imputado|im-pu-ta-do|sustantivo masculino|Persona a quien se atribuye un delito durante una investigación.|-|-|El imputado declaró ante el fiscal con su abogado.|derecho
acusado|a-cu-sa-do|sustantivo masculino|Persona a quien se le atribuye un delito en un juicio.|-|-|El acusado escuchó la lectura de los cargos.|derecho
peritaje|pe-ri-ta-je|sustantivo masculino|Informe técnico que hace un experto para aclarar un hecho en un juicio.|-|-|El peritaje determinó que el incendio fue accidental.|derecho
litigio|li-ti-gio|sustantivo masculino|Disputa que se resuelve ante un tribunal.|pleito|-|El litigio por el terreno duró cinco años.|derecho
arbitraje|ar-bi-tra-je|sustantivo masculino|Solución de un conflicto por parte de un tercero elegido por ambas partes.|-|-|Las partes acordaron un arbitraje para evitar el juicio.|derecho
moción|mo-ción|sustantivo femenino|Propuesta que se presenta para que una asamblea la discuta y la vote.|propuesta|-|El delegado presentó una moción para ampliar el plazo.|ciudadanía
enmienda|en-mien-da|sustantivo femenino|Cambio que se propone a un texto, como una ley, para corregirlo o mejorarlo.|corrección|-|La enmienda agregó un artículo sobre la protección de datos.|derecho
promulgación|pro-mul-ga-ción|sustantivo femenino|Acto en que una ley aprobada se publica y comienza a regir.|-|derogación|La promulgación de la ley se hizo en una ceremonia oficial.|derecho
derogación|de-ro-ga-ción|sustantivo femenino|Anulación de una ley que deja de estar vigente.|anulación|promulgación|La derogación de la norma puso fin a esa restricción.|derecho
tramitación|tra-mi-ta-ción|sustantivo femenino|Conjunto de pasos que sigue un proyecto o un documento para ser aprobado.|-|-|La tramitación del proyecto tardó dos años en el Congreso.|ciudadanía
ratificación|ra-ti-fi-ca-ción|sustantivo femenino|Confirmación formal de un acuerdo o una decisión.|confirmación|-|La ratificación del tratado requiere el voto del Senado.|derecho
convenio|con-ve-nio|sustantivo masculino|Acuerdo entre personas, instituciones o países sobre un asunto.|acuerdo|-|El colegio firmó un convenio con la universidad.|derecho
pacto|pac-to|sustantivo masculino|Compromiso que asumen dos o más partes para cumplir algo.|acuerdo|-|Hicieron un pacto para no discutir en clase.|ciudadanía
federación|fe-de-ra-ción|sustantivo femenino|Unión de organizaciones o de territorios que mantienen su propia autonomía.|-|-|La federación de estudiantes reúne a los centros de varias universidades.|ciudadanía
activismo|ac-ti-vis-mo|sustantivo masculino|Participación intensa en acciones para defender una causa social o política.|-|pasividad|Su activismo por el reciclaje atrajo a muchos jóvenes.|ciudadanía
movilización|mo-vi-li-za-ción|sustantivo femenino|Acción conjunta de un grupo que se organiza para exigir algo.|-|-|La movilización estudiantil pidió cambios en la educación.|ciudadanía
manifestación|ma-ni-fes-ta-ción|sustantivo femenino|Reunión pública de personas que expresan una opinión o exigen algo.|marcha|-|La manifestación recorrió la Alameda de forma pacífica.|ciudadanía
petición|pe-ti-ción|sustantivo femenino|Solicitud formal que se hace a una autoridad.|solicitud|-|Los vecinos entregaron una petición para arreglar la plaza.|ciudadanía
reivindicación|rei-vin-di-ca-ción|sustantivo femenino|Exigencia de un derecho que se considera propio o que se ha perdido.|demanda|-|La reivindicación de las tierras fue una lucha de décadas.|ciudadanía
estallido|es-ta-lli-do|sustantivo masculino|Aparición brusca de un conflicto o de una explosión.|-|-|El estallido social cambió la agenda política.|historia
boicot|boi-cot|sustantivo masculino|Rechazo organizado a comprar o participar en algo para presionar a alguien.|-|-|Convocaron a un boicot contra la marca que contaminaba el río.|ciudadanía
desobediencia|de-so-be-dien-cia|sustantivo femenino|Negativa a cumplir una orden o una norma.|insubordinación|obediencia|La desobediencia civil fue una forma de protesta sin violencia.|ciudadanía
disidencia|di-si-den-cia|sustantivo femenino|Postura de quienes no están de acuerdo con una doctrina o con el poder.|oposición|conformidad|La disidencia fue perseguida durante la dictadura.|historia
bulo|bu-lo|sustantivo masculino|Noticia falsa que se difunde para engañar.|infundio|-|El bulo sobre el cierre del colegio circuló por mensajes.|medios
verificación|ve-ri-fi-ca-ción|sustantivo femenino|Comprobación de que algo es verdadero o está correcto.|comprobación|-|La verificación de los datos evitó publicar un error.|medios
manipulación|ma-ni-pu-la-ción|sustantivo femenino|Uso engañoso de la información o de las personas para conseguir un fin.|-|-|La manipulación de las imágenes confundió al público.|medios
viralización|vi-ra-li-za-ción|sustantivo femenino|Difusión muy rápida de un contenido en las redes.|-|-|La viralización del video lo hizo conocido en horas.|medios
anonimato|a-no-ni-ma-to|sustantivo masculino|Condición de quien no da a conocer su nombre.|-|-|El anonimato en internet facilita los insultos.|tecnología
vigilancia|vi-gi-lan-cia|sustantivo femenino|Observación atenta de personas o lugares para controlarlos o protegerlos.|control|descuido|Las cámaras de vigilancia plantean dudas sobre la privacidad.|tecnología
hackeo|hac-ke-o|sustantivo masculino|Ingreso no autorizado a un sistema informático.|-|-|El hackeo de la cuenta le hizo perder sus fotos.|tecnología
patente|pa-ten-te|sustantivo femenino|Derecho exclusivo que se otorga a quien inventa algo para fabricarlo y venderlo.|-|-|La investigadora registró la patente de su invento.|tecnología
dron|dron|sustantivo masculino|Aparato volador que se maneja a distancia.|-|-|Un dron fotografió la zona afectada por el incendio.|tecnología
nanotecnología|na-no-tec-no-lo-gí-a|sustantivo femenino|Ciencia que trabaja con materiales de tamaño extremadamente pequeño.|-|-|La nanotecnología permite crear materiales muy resistentes y livianos.|tecnología
eutanasia|eu-ta-na-sia|sustantivo femenino|Acción de provocar la muerte de un enfermo incurable a petición suya para evitar su sufrimiento.|-|-|La eutanasia es un tema de debate ético y legal.|ética
acervo|a-cer-vo|sustantivo masculino|Conjunto de bienes o conocimientos que se han ido reuniendo y que pertenecen a una comunidad.|patrimonio|-|La biblioteca guarda un valioso acervo de documentos antiguos.|cultura
acepción|a-cep-ción|sustantivo femenino|Cada uno de los significados que puede tener una palabra.|significado|-|La palabra «banco» tiene varias acepciones.|lenguaje
anacronismo|a-na-cro-nis-mo|sustantivo masculino|Error de poner en una época algo que pertenece a otra.|-|-|Un celular en una película medieval sería un anacronismo.|literatura
antología|an-to-lo-gí-a|sustantivo femenino|Colección de textos o poemas escogidos de uno o de varios autores.|selección|-|Leímos una antología de cuentos latinoamericanos.|literatura
apólogo|a-pó-lo-go|sustantivo masculino|Relato breve con personajes simbólicos que deja una enseñanza.|fábula|-|El apólogo del zorro y las uvas enseña a no despreciar lo que no se logra.|literatura
aserción|a-ser-ción|sustantivo femenino|Afirmación que se da por cierta.|afirmación|negación|Su aserción no tenía pruebas que la respaldaran.|lenguaje
atenuante|a-te-nuan-te|sustantivo masculino|Circunstancia que disminuye la gravedad de una falta o de un delito.|-|agravante|La confesión voluntaria fue considerada un atenuante.|derecho
catarsis|ca-tar-sis|sustantivo femenino|Liberación de emociones fuertes, por ejemplo al ver una obra de teatro.|desahogo|-|El final de la tragedia produjo una catarsis en el público.|literatura
colofón|co-lo-fón|sustantivo masculino|Final de algo, o nota al término de un libro con datos de su impresión.|remate|-|El concierto tuvo como colofón una canción de todos los participantes.|literatura
corpus|cor-pus|sustantivo masculino|Conjunto de textos o datos reunidos para estudiarlos.|-|-|Analizamos un corpus de cien entrevistas.|lenguaje
elocuencia|e-lo-cuen-cia|sustantivo femenino|Facilidad para hablar de manera clara y persuasiva.|oratoria|-|Con elocuencia, defendió la propuesta del curso.|lenguaje
epígrafe|e-pí-gra-fe|sustantivo masculino|Cita breve que se pone al comienzo de un libro o de un capítulo.|-|-|La novela abre con un epígrafe de Neruda.|literatura
exégesis|e-xé-ge-sis|sustantivo femenino|Explicación detallada de un texto para entender su sentido.|interpretación|-|La exégesis del poema reveló significados ocultos.|literatura
exordio|e-xor-dio|sustantivo masculino|Parte inicial de un discurso con la que se busca captar la atención del público.|introducción|epílogo|El exordio de su discurso comenzó con una pregunta.|lenguaje
hipérbaton|hi-pér-ba-ton|sustantivo masculino|Alteración del orden habitual de las palabras en una oración.|-|-|«Del salón en el ángulo oscuro» es un hipérbaton.|literatura
lirismo|li-ris-mo|sustantivo masculino|Carácter de lo que expresa sentimientos con belleza y emoción.|-|-|El lirismo de sus versos conmovió a los lectores.|literatura
mímesis|mí-me-sis|sustantivo femenino|Imitación de la realidad o de un modelo en una obra de arte.|imitación|-|Para Aristóteles, el arte se basa en la mímesis de la naturaleza.|literatura
paratexto|pa-ra-tex-to|sustantivo masculino|Elemento que rodea un texto, como el título, la portada o el prólogo.|-|-|La portada es un paratexto que anticipa el contenido.|literatura
peripecia|pe-ri-pe-cia|sustantivo femenino|Cambio inesperado en la acción de un relato; también, incidente en la vida de alguien.|incidente|-|Tras mil peripecias, el protagonista llegó a su destino.|literatura
polifonía|po-li-fo-ní-a|sustantivo femenino|Presencia de muchas voces o puntos de vista en una obra.|-|-|La novela tiene una polifonía de narradores.|literatura
prosopopeya|pro-so-po-pe-ya|sustantivo femenino|Figura que atribuye cualidades humanas a seres inanimados o a animales.|personificación|-|«El viento susurraba secretos» es una prosopopeya.|literatura
referente|re-fe-ren-te|sustantivo masculino|Persona, cosa o hecho al que se refiere una palabra o un texto; también, modelo que se toma como guía.|-|-|El escritor es un referente para las nuevas generaciones.|lenguaje
semblanza|sem-blan-za|sustantivo femenino|Texto breve que resume la vida y el carácter de una persona.|retrato|-|Redacté una semblanza de la poeta Gabriela Mistral.|literatura
sinécdoque|si-néc-do-que|sustantivo femenino|Figura que nombra la parte por el todo o el todo por la parte.|-|-|Decir «necesito un techo» por «necesito una casa» es una sinécdoque.|literatura
subtexto|sub-tex-to|sustantivo masculino|Significado que no está dicho de modo directo, pero se desprende de un texto.|-|-|El subtexto del diálogo revela el miedo del personaje.|literatura
versificación|ver-si-fi-ca-ción|sustantivo femenino|Arte de escribir en verso, con su métrica y su rima.|-|-|Estudiamos la versificación de un soneto.|literatura
neoclasicismo|ne-o-cla-si-cis-mo|sustantivo masculino|Movimiento del siglo dieciocho que retomó la sobriedad y el orden del arte clásico.|-|-|El neoclasicismo prefería la razón a la emoción desbordada.|literatura
criollismo|crio-llis-mo|sustantivo masculino|Corriente literaria que retrata la vida del campo y de los tipos populares de América.|-|-|El criollismo chileno describió la vida rural del campesino.|literatura
posmodernismo|pos-mo-der-nis-mo|sustantivo masculino|Tendencia cultural que cuestiona las grandes verdades y mezcla estilos y épocas.|-|-|El posmodernismo desconfía de los relatos únicos sobre el mundo.|literatura
libreto|li-bre-to|sustantivo masculino|Texto de una obra musical, como una ópera, con las palabras que se cantan.|-|-|El libreto de la ópera cuenta una historia de amor.|arte
pódcast|pód-cast|sustantivo masculino|Programa de audio que se descarga o escucha por internet cuando uno quiere.|-|-|Escucho un pódcast de historia mientras camino a clases.|tecnología
emoji|e-mo-ji|sustantivo masculino|Dibujo pequeño que se usa en mensajes para expresar una emoción o una idea.|-|-|Respondió con un emoji de pulgar arriba.|tecnología
hashtag|hash-tag|sustantivo masculino|Palabra o frase precedida del símbolo numeral que agrupa publicaciones sobre un tema.|etiqueta|-|Usaron un hashtag para organizar la campaña de reciclaje.|tecnología
avatar|a-va-tar|sustantivo masculino|Imagen o personaje que representa a un usuario en el mundo digital.|-|-|Elegí un avatar con mi gato para el foro.|tecnología
seguidor|se-gui-dor|sustantivo masculino|Persona que sigue las publicaciones de otra en una red social o apoya a alguien.|admirador|-|La deportista tiene miles de seguidores.|tecnología
influenciador|in-fluen-cia-dor|sustantivo masculino|Persona que con sus publicaciones logra influir en las opiniones o en las compras de otros.|-|-|Un influenciador recomendó el libro y se agotó.|tecnología
clic|clic|sustantivo masculino|Pulsación breve del botón del ratón; también, su sonido.|-|-|Con un clic abrió el archivo.|tecnología
posverdad|pos-ver-dad|sustantivo femenino|Situación en que las emociones y las creencias pesan más que los hechos al formar la opinión pública.|-|-|En la era de la posverdad conviene contrastar las fuentes.|medios
hipertexto|hi-per-tex-to|sustantivo masculino|Texto digital con enlaces que llevan a otros contenidos.|-|-|En un hipertexto se salta de una página a otra con un clic.|tecnología
metadato|me-ta-da-to|sustantivo masculino|Dato que describe otro dato, como la fecha o el autor de un archivo.|-|-|Los metadatos de la foto indican dónde fue tomada.|tecnología
interlineado|in-ter-li-ne-a-do|sustantivo masculino|Espacio que se deja entre las líneas de un texto.|-|-|El informe debe tener interlineado de un espacio y medio.|escritura
sangría|san-grí-a|sustantivo femenino|Espacio en blanco que se deja al comienzo de un párrafo.|-|-|Dejé una sangría al empezar cada párrafo.|escritura
encabezado|en-ca-be-za-do|sustantivo masculino|Texto que va en la parte superior de una página o un documento.|-|-|El encabezado del trabajo lleva mi nombre y el curso.|escritura
apéndice|a-pén-di-ce|sustantivo masculino|Parte que se agrega al final de un libro o de un trabajo con información adicional.|anexo|-|Los mapas están en el apéndice del libro.|escritura
monografía|mo-no-gra-fí-a|sustantivo femenino|Trabajo de estudio extenso sobre un solo tema.|-|-|Escribí una monografía sobre los glaciares de Chile.|escritura
ponencia|po-nen-cia|sustantivo femenino|Exposición que alguien presenta ante un grupo en un congreso o encuentro.|-|-|Su ponencia trató sobre el cuidado de las napas.|escritura
simposio|sim-po-sio|sustantivo masculino|Reunión de especialistas que exponen y discuten un tema.|congreso|-|Participó en un simposio de ciencias del mar.|escritura
coloquio|co-lo-quio|sustantivo masculino|Conversación organizada en la que se debate un tema.|debate|-|Tras la película hubo un coloquio con el director.|escritura
seminario|se-mi-na-rio|sustantivo masculino|Reunión de estudio en que un grupo trabaja a fondo un tema.|taller|-|El seminario de filosofía se reúne cada viernes.|escritura
plenario|ple-na-rio|sustantivo masculino|Reunión a la que asisten todos los miembros de un grupo.|asamblea|-|En el plenario se votó la propuesta del curso.|ciudadanía
contrarréplica|con-tra-rré-pli-ca|sustantivo femenino|Respuesta que se da a una réplica durante un debate.|-|-|Tras la réplica, cada equipo tuvo una contrarréplica de dos minutos.|argumentación
reiteración|rei-te-ra-ción|sustantivo femenino|Repetición de algo ya dicho o hecho.|repetición|-|La reiteración de la idea ayudó a recordarla.|lenguaje
tecnicismo|tec-ni-cis-mo|sustantivo masculino|Palabra propia de una ciencia o de un oficio.|-|-|«Fotosíntesis» es un tecnicismo de la biología.|lenguaje
regionalismo|re-gio-na-lis-mo|sustantivo masculino|Palabra o expresión propia de una región.|-|-|«Pololear» es un regionalismo chileno.|lenguaje
sociolecto|so-cio-lec-to|sustantivo masculino|Modo de hablar propio de un grupo social.|-|-|El sociolecto de los jóvenes incorpora palabras nuevas.|lenguaje
yuxtapuesta|yux-ta-pues-ta|adjetivo|Dicho de una oración unida a otra solo con una coma o con otro signo, sin conector.|-|-|«Llegué, vi, vencí» contiene oraciones yuxtapuestas.|gramática
coordinada|co-or-di-na-da|adjetivo|Dicho de una oración unida a otra por una conjunción, sin que dependa de ella.|-|subordinada|«Estudio y escucho música» tiene oraciones coordinadas.|gramática
sintagma|sin-tag-ma|sustantivo masculino|Grupo de palabras que funciona como una unidad dentro de una oración.|-|-|«El perro del vecino» es un sintagma nominal.|gramática
elisión|e-li-sión|sustantivo femenino|Supresión de una vocal o de una palabra que se sobreentiende.|omisión|-|En «Fui a casa de mi tía» y «Voy a la tuya» hay elisión de un sustantivo.|gramática
transitivo|tran-si-ti-vo|adjetivo|Dicho del verbo que necesita un complemento directo para completar su sentido.|-|intransitivo|«Comprar» es un verbo transitivo.|gramática
intransitivo|in-tran-si-ti-vo|adjetivo|Dicho del verbo que no necesita complemento directo.|-|transitivo|«Dormir» es un verbo intransitivo.|gramática
pronominal|pro-no-mi-nal|adjetivo|Dicho del verbo que se conjuga con un pronombre que concuerda con el sujeto.|-|-|«Arrepentirse» es un verbo pronominal.|gramática
impersonal|im-per-so-nal|adjetivo|Dicho de la oración que no tiene un sujeto determinado.|-|personal|«Llueve mucho» es una oración impersonal.|gramática
recíproco|re-cí-pro-co|adjetivo|Que se da por igual entre dos o más personas, de unas a otras.|mutuo|unilateral|El respeto debe ser recíproco.|gramática
difusión|di-fu-sión|sustantivo femenino|Movimiento de partículas desde donde hay más hacia donde hay menos de ellas; también, propagación de algo.|propagación|-|El olor del perfume se expande por difusión en el aire.|ciencia
ósmosis|ós-mo-sis|sustantivo femenino|Paso de agua a través de una membrana hacia el lado donde hay más sustancias disueltas.|-|-|Por ósmosis, la raíz absorbe agua del suelo.|biología
axón|a-xón|sustantivo masculino|Prolongación larga de la neurona que transmite el impulso nervioso hacia otras células.|-|-|El impulso viaja por el axón hasta la sinapsis.|biología
dendrita|den-dri-ta|sustantivo femenino|Prolongación ramificada de la neurona que recibe señales de otras células.|-|-|Las dendritas captan los mensajes de las neuronas vecinas.|biología
glucagón|glu-ca-gón|sustantivo masculino|Hormona que hace subir la glucosa en la sangre.|-|insulina|El glucagón actúa cuando el nivel de azúcar baja demasiado.|biología
tiroides|ti-roi-des|sustantivo femenino|Glándula del cuello que regula el metabolismo mediante hormonas.|-|-|La tiroides produce hormonas que controlan la energía del cuerpo.|biología
hipófisis|hi-pó-fi-sis|sustantivo femenino|Glándula pequeña en la base del cerebro que dirige a otras glándulas.|-|-|La hipófisis libera la hormona del crecimiento.|biología
cortisol|cor-ti-sol|sustantivo masculino|Hormona que el cuerpo libera ante el estrés.|-|-|El nivel de cortisol sube cuando estamos muy tensos.|biología
adrenalina|a-dre-na-li-na|sustantivo femenino|Hormona que prepara al cuerpo para reaccionar rápido ante un peligro.|-|-|La adrenalina aceleró su corazón antes de la carrera.|biología
melatonina|me-la-to-ni-na|sustantivo femenino|Hormona que regula el sueño y se produce más en la oscuridad.|-|-|La luz de las pantallas reduce la melatonina y retrasa el sueño.|biología
fertilidad|fer-ti-li-dad|sustantivo femenino|Capacidad de un ser vivo o de un suelo para reproducirse o producir.|fecundidad|esterilidad|La fertilidad del valle permite varias cosechas al año.|biología
endemia|en-de-mia|sustantivo femenino|Enfermedad que afecta de manera constante a una zona o población.|-|-|El paludismo es una endemia en algunas regiones tropicales.|salud
inmunización|in-mu-ni-za-ción|sustantivo femenino|Proceso para que el cuerpo se proteja contra una enfermedad, por ejemplo mediante vacunas.|-|-|La inmunización de los niños redujo los casos de sarampión.|salud
aislamiento|ais-la-mien-to|sustantivo masculino|Separación de una persona o cosa del resto para evitar contagios, ruidos o contacto.|-|contacto|El aislamiento de los enfermos frenó el brote.|salud
profilaxis|pro-fi-la-xis|sustantivo femenino|Conjunto de medidas para prevenir una enfermedad.|prevención|-|El lavado de manos es una profilaxis sencilla y eficaz.|salud
síndrome|sín-dro-me|sustantivo masculino|Conjunto de síntomas que aparecen juntos y caracterizan una enfermedad.|-|-|El médico explicó en qué consiste ese síndrome.|salud
patología|pa-to-lo-gí-a|sustantivo femenino|Enfermedad, o estudio de las enfermedades y sus causas.|enfermedad|-|La patología fue detectada en un examen de rutina.|salud
benigno|be-nig-no|adjetivo|Dicho de una enfermedad o un tumor que no es grave ni se extiende.|leve|maligno|El examen mostró que el quiste era benigno.|salud
maligno|ma-lig-no|adjetivo|Dicho de una enfermedad o un tumor que es grave y puede extenderse.|grave|benigno|El tumor maligno requirió un tratamiento largo.|salud
metástasis|me-tás-ta-sis|sustantivo femenino|Propagación de un tumor a otras partes del cuerpo.|-|-|Los controles buscan detectar a tiempo una metástasis.|salud
quimioterapia|qui-mio-te-ra-pia|sustantivo femenino|Tratamiento con medicamentos que destruyen células cancerosas.|-|-|La quimioterapia le hizo caer el cabello por un tiempo.|salud
radioterapia|ra-dio-te-ra-pia|sustantivo femenino|Tratamiento que usa radiación para eliminar células enfermas.|-|-|La radioterapia se aplica en sesiones breves y controladas.|salud
cirugía|ci-ru-gí-a|sustantivo femenino|Parte de la medicina que cura enfermedades mediante operaciones.|operación|-|La cirugía duró dos horas y salió bien.|salud
anestesia|a-nes-te-sia|sustantivo femenino|Pérdida temporal de la sensibilidad, provocada con medicamentos para operar sin dolor.|-|-|Con anestesia local no sintió dolor al sacarse la muela.|salud
posología|po-so-lo-gí-a|sustantivo femenino|Indicación de la cantidad de un medicamento y cada cuánto tiempo hay que tomarlo.|-|-|La receta indica la posología: una pastilla cada ocho horas.|salud
contraindicación|con-train-di-ca-ción|sustantivo femenino|Situación en que un medicamento o un tratamiento no debe usarse porque podría hacer daño.|-|indicación|La caja menciona una contraindicación para los alérgicos.|salud
automedicación|au-to-me-di-ca-ción|sustantivo femenino|Hábito de tomar medicamentos sin que los recete un profesional.|-|-|La automedicación puede esconder una enfermedad más seria.|salud
abstinencia|abs-ti-nen-cia|sustantivo femenino|Privación voluntaria de algo, como una sustancia o un alimento.|privación|-|Su abstinencia del tabaco duró ya dos años.|salud
sobredosis|so-bre-do-sis|sustantivo femenino|Cantidad de una droga o un medicamento mayor a la que el cuerpo tolera.|-|-|Una sobredosis de analgésicos puede dañar el hígado.|salud
alcoholismo|al-co-ho-lis-mo|sustantivo masculino|Enfermedad que consiste en la dependencia del alcohol.|-|-|El alcoholismo afecta la salud y las relaciones familiares.|salud
drogadicción|dro-ga-dic-ción|sustantivo femenino|Dependencia de sustancias que alteran el funcionamiento del cuerpo y de la mente.|adicción|-|La drogadicción requiere tratamiento y apoyo familiar.|salud
ludopatía|lu-do-pa-tí-a|sustantivo femenino|Adicción a los juegos de azar.|-|-|La ludopatía puede arruinar la economía de una familia.|salud
anorexia|a-no-re-xia|sustantivo femenino|Trastorno que lleva a rechazar la comida por una imagen deformada del propio cuerpo.|-|-|La anorexia necesita ayuda médica y psicológica.|salud
bulimia|bu-li-mia|sustantivo femenino|Trastorno en que la persona come en exceso y luego intenta eliminar lo ingerido.|-|-|La bulimia daña la salud física y emocional.|salud
ayuno|a-yu-no|sustantivo masculino|Abstención de comer por un tiempo.|-|-|Para el examen de sangre debes llegar en ayuno.|salud
luxación|lu-xa-ción|sustantivo femenino|Salida de un hueso de su articulación.|dislocación|-|La luxación del hombro le dolió mucho.|salud
contusión|con-tu-sión|sustantivo femenino|Lesión causada por un golpe que no abre la piel.|golpe|-|Se hizo una contusión en la rodilla jugando fútbol.|salud
hemorragia|he-mo-rra-gia|sustantivo femenino|Salida abundante de sangre por una herida o dentro del cuerpo.|-|-|Para detener la hemorragia hay que presionar la herida.|salud
torniquete|tor-ni-que-te|sustantivo masculino|Vendaje apretado que se coloca para detener una hemorragia grave en un brazo o una pierna.|-|-|El rescatista colocó un torniquete sobre la herida.|salud
quemadura|que-ma-du-ra|sustantivo femenino|Lesión de la piel causada por fuego, calor, sustancias químicas o el sol.|-|-|Enfrió la quemadura con agua fresca.|salud
hipotermia|hi-po-ter-mia|sustantivo femenino|Descenso peligroso de la temperatura del cuerpo.|-|hipertermia|El excursionista sufrió hipotermia por el frío intenso.|salud
convulsión|con-vul-sión|sustantivo femenino|Contracción brusca e involuntaria de los músculos.|espasmo|-|Durante la convulsión hay que alejar los objetos peligrosos.|salud
desmayo|des-ma-yo|sustantivo masculino|Pérdida breve del conocimiento.|-|-|El calor y el cansancio le provocaron un desmayo.|salud
atragantamiento|a-tra-gan-ta-mien-to|sustantivo masculino|Obstrucción de la garganta por un trozo de comida u otro objeto.|-|-|Ante un atragantamiento se aplica la maniobra de Heimlich.|salud
maniobra|ma-nio-bra|sustantivo femenino|Operación manual o conjunto de movimientos que se hacen para lograr algo.|-|-|La maniobra de reanimación salvó al paciente.|salud
señalética|se-ña-lé-ti-ca|sustantivo femenino|Conjunto de señales que orientan o advierten en un lugar.|-|-|La señalética del edificio indica las vías de evacuación.|seguridad
extintor|ex-tin-tor|sustantivo masculino|Aparato portátil que lanza una sustancia para apagar el fuego.|-|-|El extintor está junto a la puerta de la cocina.|seguridad
protección civil|pro-tec-ción ci-vil|locución nominal|Sistema de organismos y acciones que protege a la población ante emergencias y desastres.|-|-|Protección civil avisó que se debía evacuar la costa.|seguridad
preservación|pre-ser-va-ción|sustantivo femenino|Acción de proteger algo para que no se dañe ni se pierda.|protección|destrucción|La preservación de los humedales protege a las aves.|ambiente
efluente|e-fluen-te|sustantivo masculino|Líquido residual que sale de una industria, una planta o una ciudad.|-|-|El efluente se trata antes de volver al río.|ambiente
sumidero|su-mi-de-ro|sustantivo masculino|Lugar o sistema que absorbe algo, como los bosques que captan dióxido de carbono; también, conducto por donde se va el agua.|-|-|Los bosques son un sumidero natural de carbono.|ambiente
geotermia|ge-o-ter-mia|sustantivo femenino|Energía que se obtiene del calor del interior de la Tierra.|-|-|La geotermia aprovecha el calor de los volcanes para generar electricidad.|energía
acidificación|a-ci-di-fi-ca-ción|sustantivo femenino|Aumento de la acidez de un medio, como el océano al absorber más dióxido de carbono.|-|-|La acidificación del mar daña a los corales.|ambiente
napa|na-pa|sustantivo femenino|Capa de agua que se encuentra bajo tierra.|acuífero|-|La sequía bajó el nivel de las napas.|ambiente
agroecología|a-gro-e-co-lo-gí-a|sustantivo femenino|Forma de producir alimentos cuidando el suelo, el agua y la biodiversidad.|-|-|La agroecología combina saberes campesinos y ciencia.|ambiente
codominio|co-do-mi-nio|sustantivo masculino|Conjunto de valores que se permiten como resultado en una función, aunque no todos se alcancen.|-|-|En esa función, el codominio son todos los números reales.|matemática
hipérbola|hi-pér-bo-la|sustantivo femenino|Curva con dos ramas separadas, como la gráfica de una proporción inversa.|-|-|La gráfica de la proporcionalidad inversa es una hipérbola.|matemática
exponencial|ex-po-nen-cial|adjetivo|Dicho de un crecimiento o una función en que la cantidad se multiplica una y otra vez por el mismo factor.|-|-|El crecimiento exponencial de las bacterias sorprendió a los científicos.|matemática
progresión|pro-gre-sión|sustantivo femenino|Serie de números en que cada término se obtiene del anterior siguiendo una regla.|serie|-|En una progresión aritmética se suma siempre el mismo número.|matemática
sucesión|su-ce-sión|sustantivo femenino|Conjunto ordenado de elementos que van uno tras otro; también, hecho de ocupar el lugar de otro.|serie|-|La sucesión de los números pares empieza con dos, cuatro y seis.|matemática
derivada|de-ri-va-da|sustantivo femenino|Medida de la rapidez con que cambia el valor de una función en un punto.|-|-|La derivada indica qué tan empinada es la curva en cada punto.|matemática
integral|in-te-gral|sustantivo femenino|Herramienta del cálculo que permite sumar cantidades infinitamente pequeñas, por ejemplo para hallar un área.|-|-|Con una integral calculamos el área bajo la curva.|matemática
factorización|fac-to-ri-za-ción|sustantivo femenino|Descomposición de una expresión en factores que, multiplicados, la reproducen.|-|-|La factorización simplifica la ecuación cuadrática.|matemática
trinomio|tri-no-mio|sustantivo masculino|Expresión algebraica formada por tres términos.|-|-|Factorizó el trinomio para hallar las raíces.|matemática
amortización|a-mor-ti-za-ción|sustantivo femenino|Pago gradual de una deuda en cuotas.|-|-|La amortización mensual redujo el saldo del crédito.|economía
repactación|re-pac-ta-ción|sustantivo femenino|Nuevo acuerdo para cambiar las condiciones de una deuda.|renegociación|-|Pidió una repactación porque no alcanzaba a pagar las cuotas.|economía
comisión|co-mi-sión|sustantivo femenino|Pago que se cobra por un servicio; también, grupo encargado de una tarea.|-|-|El banco cobra una comisión por mantener la cuenta.|economía
tasa de interés|ta-sa de in-te-rés|locución nominal|Porcentaje que se cobra o se paga por el uso del dinero durante un tiempo.|-|-|Una tasa de interés alta encarece los créditos.|economía
deflación|de-fla-ción|sustantivo femenino|Baja general y sostenida de los precios.|-|inflación|La deflación puede frenar el consumo porque la gente espera precios aún menores.|economía
recesión|re-ce-sión|sustantivo femenino|Período en que la economía de un país se contrae y baja la producción.|crisis|auge|La recesión aumentó el desempleo.|economía
previsión|pre-vi-sión|sustantivo femenino|Sistema de ahorro y seguros para cubrir la vejez, la enfermedad o la cesantía; también, anticipación de algo.|-|-|Cotiza en una administradora de previsión para su jubilación.|economía
jubilación|ju-bi-la-ción|sustantivo femenino|Retiro del trabajo al llegar a cierta edad, con derecho a una pensión.|retiro|-|Su jubilación llegó tras treinta años de trabajo.|trabajo
póliza|pó-li-za|sustantivo femenino|Documento que fija las condiciones de un contrato de seguro.|-|-|La póliza cubre los daños por incendio.|economía
honorarios|ho-no-ra-rios|sustantivo masculino plural|Pago que recibe un profesional que trabaja por cuenta propia.|-|-|El arquitecto cobró honorarios por el diseño.|trabajo
renta|ren-ta|sustantivo femenino|Ganancia que produce un trabajo, un capital o un bien; también, ingreso anual sobre el que se pagan impuestos.|ingreso|-|La renta de ese local es muy alta.|economía
elusión|e-lu-sión|sustantivo femenino|Uso de vacíos de la ley para pagar menos impuestos, sin violar la norma.|-|-|La elusión tributaria es legal, pero discutida.|economía
subsidio|sub-si-dio|sustantivo masculino|Ayuda en dinero que entrega el Estado a ciertas personas o actividades.|ayuda|-|Recibió un subsidio para pagar parte del arriendo.|economía
aduana|a-dua-na|sustantivo femenino|Oficina que controla y cobra impuestos a lo que entra y sale de un país.|-|-|En la aduana revisaron las maletas de los viajeros.|economía
rentabilidad|ren-ta-bi-li-dad|sustantivo femenino|Ganancia que produce una inversión en relación con lo invertido.|ganancia|pérdida|La rentabilidad del negocio fue baja el primer año.|economía
bono|bo-no|sustantivo masculino|Documento que da derecho a cobrar una suma; también, ayuda económica que entrega el Estado.|vale|-|Las familias recibieron un bono para pagar la calefacción.|economía
devaluación|de-va-lua-ción|sustantivo femenino|Pérdida de valor de la moneda de un país frente a otras.|-|revaluación|La devaluación encareció los productos importados.|economía
elasticidad|e-las-ti-ci-dad|sustantivo femenino|Capacidad de un material de estirarse y volver a su forma; en economía, cuánto cambia la demanda al variar el precio.|flexibilidad|rigidez|La elasticidad de la goma permite estirarla sin romperla.|economía
oligopolio|o-li-go-po-lio|sustantivo masculino|Mercado dominado por muy pocas empresas.|-|-|En un oligopolio, unas pocas empresas fijan los precios.|economía
colusión|co-lu-sión|sustantivo femenino|Acuerdo secreto entre empresas para fijar precios y evitar la competencia.|confabulación|-|La colusión de las farmacias perjudicó a los consumidores.|economía
regulación|re-gu-la-ción|sustantivo femenino|Conjunto de normas con que se controla una actividad.|control|-|La regulación del mercado protege a los consumidores.|economía
estatización|es-ta-ti-za-ción|sustantivo femenino|Paso de una empresa o un servicio a manos del Estado.|-|privatización|La estatización del servicio de agua fue un tema de debate.|economía
licitación|li-ci-ta-ción|sustantivo femenino|Proceso en que se invita a varias empresas a ofrecer un precio para realizar una obra.|-|-|La licitación del puente la ganó la empresa más económica.|economía
emprendimiento|em-pren-di-mien-to|sustantivo masculino|Negocio o proyecto que alguien inicia con esfuerzo e iniciativa propia.|-|-|Su emprendimiento vende pan artesanal por encargo.|economía
cooperativa|co-o-pe-ra-ti-va|sustantivo femenino|Organización de personas que trabajan juntas y reparten los beneficios entre sus socios.|-|-|La cooperativa de pescadores vende su producción en conjunto.|economía
microempresa|mi-cro-em-pre-sa|sustantivo femenino|Empresa muy pequeña, con pocos trabajadores.|-|-|La microempresa familiar fabrica velas.|economía
capital humano|ca-pi-tal hu-ma-no|locución nominal|Conjunto de conocimientos y habilidades de las personas que aportan al trabajo y a la economía.|-|-|Invertir en educación aumenta el capital humano de un país.|economía
productividad|pro-duc-ti-vi-dad|sustantivo femenino|Relación entre lo que se produce y los recursos empleados para lograrlo.|-|-|Mejores herramientas aumentan la productividad del taller.|economía
externalidad|ex-ter-na-li-dad|sustantivo femenino|Efecto, bueno o malo, que una actividad produce en personas que no participan en ella.|-|-|La contaminación de la fábrica es una externalidad negativa.|economía
extractivismo|ex-trac-ti-vis-mo|sustantivo masculino|Modelo económico basado en sacar recursos naturales para venderlos con poco procesamiento.|-|-|El extractivismo minero dejó ganancias, pero también daño ambiental.|economía
desindustrialización|de-sin-dus-tria-li-za-ción|sustantivo femenino|Disminución de la industria de un país frente a otras actividades.|-|industrialización|La desindustrialización hizo cerrar muchas fábricas.|economía
comunismo|co-mu-nis-mo|sustantivo masculino|Doctrina que propone que los medios de producción pertenezcan a toda la comunidad.|-|capitalismo|El comunismo plantea una sociedad sin clases sociales.|historia
anarquismo|a-nar-quis-mo|sustantivo masculino|Doctrina que propone una sociedad sin Estado ni autoridad impuesta.|-|-|El anarquismo defiende la libre organización de las personas.|historia
fascismo|fas-cis-mo|sustantivo masculino|Régimen autoritario y nacionalista que anula las libertades y exalta a un líder.|-|-|El fascismo en Italia reprimió a sus opositores.|historia
imperialismo|im-pe-ria-lis-mo|sustantivo masculino|Política de un Estado que domina a otros pueblos para controlar sus territorios y riquezas.|-|-|El imperialismo europeo del siglo diecinueve repartió África.|historia
colonialismo|co-lo-nia-lis-mo|sustantivo masculino|Sistema en que un país controla y explota territorios de otros pueblos.|-|-|El colonialismo impuso lenguas y costumbres ajenas.|historia
descolonización|des-co-lo-ni-za-ción|sustantivo femenino|Proceso en que las colonias se independizan de la potencia que las dominaba.|-|-|La descolonización de África ocurrió sobre todo después de 1950.|historia
guerra fría|gue-rra frí-a|locución nominal|Tensión política y militar que enfrentó a Estados Unidos y la Unión Soviética tras la Segunda Guerra Mundial.|-|-|Durante la guerra fría hubo una gran carrera espacial.|historia
represión|re-pre-sión|sustantivo femenino|Uso de la fuerza para impedir que la gente exprese sus ideas o proteste.|-|libertad|La represión contra los manifestantes fue condenada.|historia
justicia transicional|jus-ti-cia tran-si-cio-nal|locución nominal|Medidas que se toman para enfrentar violaciones de derechos humanos tras una dictadura o un conflicto.|-|-|La justicia transicional busca verdad, reparación y garantías de no repetición.|derechos
genocidio|ge-no-ci-dio|sustantivo masculino|Exterminio planificado de un grupo humano por su origen, religión o cultura.|-|-|El genocidio es uno de los crímenes más graves contra la humanidad.|historia
holocausto|ho-lo-caus-to|sustantivo masculino|Exterminio de millones de judíos y de otros grupos por el régimen nazi.|-|-|El museo recuerda a las víctimas del holocausto.|historia
segregación|se-gre-ga-ción|sustantivo femenino|Separación de un grupo de personas por su origen, su religión u otra condición.|separación|integración|La segregación racial se aplicó en escuelas y transportes.|sociedad
sufragismo|su-fra-gis-mo|sustantivo masculino|Movimiento que luchó para que las mujeres pudieran votar.|-|-|El sufragismo logró el voto femenino en muchos países.|historia
patriarcado|pa-triar-ca-do|sustantivo masculino|Sistema social en que los hombres tienen más poder y autoridad que las mujeres.|-|matriarcado|Las feministas critican el patriarcado por sostener desigualdades.|sociedad
machismo|ma-chis-mo|sustantivo masculino|Actitud que considera a los hombres superiores a las mujeres.|-|feminismo|El machismo se nota en los chistes que ridiculizan a las mujeres.|sociedad
misoginia|mi-so-gi-nia|sustantivo femenino|Odio o desprecio hacia las mujeres.|-|-|Los mensajes de misoginia en redes fueron denunciados.|sociedad
sexismo|se-xis-mo|sustantivo masculino|Discriminación de una persona por su sexo.|-|-|El sexismo limita las oportunidades de trabajo de las mujeres.|sociedad
brecha salarial|bre-cha sa-la-rial|locución nominal|Diferencia entre lo que ganan hombres y mujeres por un trabajo similar.|-|-|La brecha salarial persiste en muchas profesiones.|sociedad
femicidio|fe-mi-ci-dio|sustantivo masculino|Asesinato de una mujer por el hecho de ser mujer.|-|-|La ley sanciona el femicidio con las penas más altas.|derechos
homofobia|ho-mo-fo-bia|sustantivo femenino|Rechazo o miedo irracional hacia las personas homosexuales.|-|-|La campaña busca combatir la homofobia en los colegios.|sociedad
xenofobia|xe-no-fo-bia|sustantivo femenino|Rechazo o miedo hacia las personas extranjeras.|-|-|La xenofobia afecta a muchos migrantes en el trabajo.|sociedad
racismo|ra-cis-mo|sustantivo masculino|Discriminación hacia personas por su origen étnico o el color de su piel.|-|-|El racismo se combate con educación y respeto.|sociedad
asimilación|a-si-mi-la-ción|sustantivo femenino|Proceso en que un grupo adopta la cultura de otro y pierde la suya; también, absorción de nuevos conocimientos.|-|-|La asimilación forzada hizo desaparecer lenguas indígenas.|sociedad
multiculturalidad|mul-ti-cul-tu-ra-li-dad|sustantivo femenino|Presencia de varias culturas en un mismo lugar.|-|-|La multiculturalidad enriquece la vida de la ciudad.|sociedad
interculturalidad|in-ter-cul-tu-ra-li-dad|sustantivo femenino|Relación respetuosa y de intercambio entre personas de distintas culturas.|-|-|La interculturalidad promueve el diálogo entre pueblos.|sociedad
refugiado|re-fu-gia-do|sustantivo masculino|Persona que debe abandonar su país por guerras o persecuciones y busca protección en otro.|-|-|Los refugiados recibieron ayuda humanitaria en la frontera.|sociedad
asilo|a-si-lo|sustantivo masculino|Protección que un país da a una persona perseguida en el suyo.|refugio|-|El periodista pidió asilo político.|derechos
apátrida|a-pá-tri-da|adjetivo|Dicho de una persona que no tiene ninguna nacionalidad reconocida.|-|-|Un niño apátrida enfrenta dificultades para estudiar o recibir salud.|derechos
visa|vi-sa|sustantivo femenino|Autorización que se pone en el pasaporte para entrar a un país durante cierto tiempo.|-|-|Necesitó una visa para viajar a ese país.|sociedad
remesa|re-me-sa|sustantivo femenino|Dinero que un migrante envía a su familia en su país de origen.|-|-|Las remesas ayudan a sostener la economía de muchas familias.|economía
diáspora|diás-po-ra|sustantivo femenino|Dispersión de un pueblo que vive fuera de su lugar de origen.|-|-|La diáspora chilena se formó con quienes se exiliaron.|historia
interdependencia|in-ter-de-pen-den-cia|sustantivo femenino|Relación en que cada parte necesita de las otras.|-|independencia|La interdependencia entre países hace que una crisis se contagie.|sociedad
hegemonía|he-ge-mo-ní-a|sustantivo femenino|Dominio de un país, grupo o idea sobre otros.|supremacía|-|Tras la guerra, Estados Unidos ejerció hegemonía económica.|historia
geopolítica|ge-o-po-lí-ti-ca|sustantivo femenino|Estudio de cómo la geografía influye en la política y en las relaciones entre países.|-|-|La geopolítica explica por qué ciertos pasos marítimos son estratégicos.|historia
indigencia|in-di-gen-cia|sustantivo femenino|Pobreza extrema, en que falta lo necesario para vivir.|miseria|-|Los albergues atienden a personas en situación de indigencia.|sociedad
movilidad social|mo-vi-li-dad so-cial|locución nominal|Posibilidad de pasar de un nivel socioeconómico a otro, hacia arriba o hacia abajo.|-|-|La educación favorece la movilidad social.|sociedad
élite|é-li-te|sustantivo femenino|Grupo pequeño que tiene mucho poder o prestigio en una sociedad.|-|-|La élite económica influyó en esa decisión.|sociedad
brecha digital|bre-cha di-gi-tal|locución nominal|Diferencia entre quienes tienen acceso a internet y tecnología y quienes no lo tienen.|-|-|La brecha digital se notó cuando las clases pasaron a internet.|tecnología
cohesión social|co-he-sión so-cial|locución nominal|Grado de unión y confianza entre los miembros de una sociedad.|-|-|La desigualdad debilita la cohesión social.|sociedad
gentrificación|gen-tri-fi-ca-ción|sustantivo femenino|Transformación de un barrio popular cuando llegan personas con más recursos y suben los precios.|-|-|La gentrificación obligó a muchas familias antiguas a mudarse.|ciudad
hacinamiento|ha-ci-na-mien-to|sustantivo masculino|Situación en que demasiadas personas viven en un espacio reducido.|-|-|El hacinamiento en las viviendas facilita los contagios.|ciudad
megaciudad|me-ga-ciu-dad|sustantivo femenino|Ciudad con millones de habitantes.|-|-|Santiago aspira a ser una megaciudad con transporte más eficiente.|ciudad
periferia|pe-ri-fe-ria|sustantivo femenino|Zona alejada del centro de una ciudad.|afueras|centro|Vive en la periferia y tarda una hora en llegar al trabajo.|ciudad
metrópolis|me-tró-po-lis|sustantivo femenino|Ciudad grande e importante, con mucha población y actividad.|-|-|La metrópolis funciona día y noche.|ciudad
éxodo rural|é-xo-do ru-ral|locución nominal|Migración masiva de personas del campo a la ciudad.|-|-|El éxodo rural dejó pueblos casi vacíos.|ciudad
ruralidad|ru-ra-li-dad|sustantivo femenino|Condición de lo que pertenece al campo y a su forma de vida.|-|-|La ruralidad enfrenta problemas de acceso a servicios.|ciudad
zonificación|zo-ni-fi-ca-ción|sustantivo femenino|División de un territorio en zonas con usos determinados, como vivienda o industria.|-|-|La zonificación evita instalar una fábrica junto a un colegio.|ciudad
aberrante|a-be-rran-te|adjetivo|Que se aparta mucho de lo normal o de lo correcto.|anormal|normal|Esa conducta aberrante fue rechazada por todos.|lenguaje
abnegado|ab-ne-ga-do|adjetivo|Que se sacrifica por los demás sin pensar en sí mismo.|sacrificado|egoísta|La enfermera abnegada trabajó día y noche en la emergencia.|valores
abrumador|a-bru-ma-dor|adjetivo|Que agobia o supera por ser excesivo.|agobiante|-|Recibió una cantidad abrumadora de mensajes.|lenguaje
acérrimo|a-cé-rri-mo|adjetivo|Muy firme y obstinado en defender una idea o una causa.|fervoroso|tibio|Es un defensor acérrimo del medioambiente.|lenguaje
acuciante|a-cu-cian-te|adjetivo|Que apremia y exige atención inmediata.|apremiante|-|La falta de agua es un problema acuciante.|lenguaje
adverso|ad-ver-so|adjetivo|Contrario o desfavorable.|contrario|favorable|Jugaron bajo condiciones climáticas adversas.|lenguaje
afable|a-fa-ble|adjetivo|Amable y agradable en el trato.|cordial|hosco|La vecina afable siempre saluda con una sonrisa.|carácter
alentador|a-len-ta-dor|adjetivo|Que da ánimo y esperanza.|esperanzador|desalentador|Los resultados del examen fueron alentadores.|lenguaje
altanero|al-ta-ne-ro|adjetivo|Que se cree superior y trata a los demás con soberbia.|soberbio|humilde|Su actitud altanera molestó a todo el curso.|carácter
anodino|a-no-di-no|adjetivo|Sin interés ni personalidad.|insulso|llamativo|Dio un discurso anodino que nadie recordó.|lenguaje
arraigado|a-rrai-ga-do|adjetivo|Firmemente establecido o muy fijo en una persona o en una comunidad.|enraizado|superficial|Es una costumbre arraigada en el pueblo.|cultura
ascendente|as-cen-den-te|adjetivo|Que sube o crece.|creciente|descendente|La curva ascendente muestra el aumento de las ventas.|lenguaje
beligerante|be-li-ge-ran-te|adjetivo|Que está en guerra o tiene una actitud agresiva y conflictiva.|belicoso|pacífico|Mantuvo una postura beligerante durante el debate.|historia
bienintencionado|bien-in-ten-cio-na-do|adjetivo|Que actúa con buena intención, aunque no siempre acierte.|-|malintencionado|Fue un consejo bienintencionado, pero poco útil.|carácter
cabal|ca-bal|adjetivo|Completo, exacto o íntegro.|íntegro|incompleto|Tiene un conocimiento cabal del tema.|lenguaje
categórico|ca-te-gó-ri-co|adjetivo|Que afirma o niega con total seguridad y sin dudas.|rotundo|dubitativo|Fue categórico: no cambiará de opinión.|lenguaje
caótico|ca-ó-ti-co|adjetivo|Desordenado y confuso.|desordenado|ordenado|El tránsito fue caótico por la lluvia.|lenguaje
cínico|cí-ni-co|adjetivo|Que miente o actúa sin vergüenza y sin importarle lo que piensen los demás.|descarado|sincero|Fue cínico al negar lo que todos habían visto.|carácter
complaciente|com-pla-cien-te|adjetivo|Que trata de agradar a otros y accede a sus deseos.|condescendiente|exigente|Su actitud complaciente evitó una discusión.|carácter
concluyente|con-cluyen-te|adjetivo|Que cierra una discusión por ser decisivo.|decisivo|dudoso|Las pruebas fueron concluyentes.|argumentación
condescendiente|con-des-cen-dien-te|adjetivo|Que se muestra amable con otros, pero creyéndose superior.|paternalista|humilde|Su tono condescendiente irritó al equipo.|carácter
conformista|con-for-mis-ta|adjetivo|Que se conforma con lo que hay y no intenta cambiar las cosas.|resignado|inconformista|Una actitud conformista no mejora la situación.|carácter
contundente|con-tun-den-te|adjetivo|Que convence por ser claro y fuerte.|rotundo|débil|Dio una respuesta contundente al reclamo.|argumentación
convincente|con-vin-cen-te|adjetivo|Que logra persuadir.|persuasivo|dudoso|Su argumento fue convincente.|argumentación
copioso|co-pio-so|adjetivo|Abundante.|abundante|escaso|Cayó una lluvia copiosa durante la noche.|lenguaje
crónico|cró-ni-co|adjetivo|Dicho de una enfermedad o un problema que dura mucho tiempo.|persistente|agudo|El asma es una enfermedad crónica.|salud
cuestionable|cues-tio-na-ble|adjetivo|Que puede ser puesto en duda o discutido.|discutible|incuestionable|La fuente de esa noticia es cuestionable.|argumentación
dadivoso|da-di-vo-so|adjetivo|Que da con generosidad.|generoso|tacaño|Es una persona dadivosa con quienes lo necesitan.|carácter
deficiente|de-fi-cien-te|adjetivo|Que no alcanza el nivel esperado.|insuficiente|excelente|El servicio de transporte es deficiente.|lenguaje
delicado|de-li-ca-do|adjetivo|Frágil, fino o que requiere cuidado; también, difícil de tratar.|frágil|resistente|Es un asunto delicado que debe tratarse con respeto.|lenguaje
desmesurado|des-me-su-ra-do|adjetivo|Excesivo, sin medida.|excesivo|moderado|Tuvo una ambición desmesurada.|lenguaje
despiadado|des-pia-da-do|adjetivo|Sin compasión.|cruel|compasivo|La crítica fue despiadada con el autor.|carácter
desproporcionado|des-pro-por-cio-na-do|adjetivo|Que no guarda la medida adecuada respecto de otra cosa.|excesivo|proporcionado|La respuesta fue desproporcionada para un error tan pequeño.|lenguaje
destacable|des-ta-ca-ble|adjetivo|Que merece ser destacado por su calidad o importancia.|notable|insignificante|Su esfuerzo es destacable.|lenguaje
detallista|de-ta-llis-ta|adjetivo|Que cuida los detalles.|minucioso|descuidado|Es muy detallista al armar sus maquetas.|carácter
diáfano|diá-fa-no|adjetivo|Que deja pasar la luz o es muy claro.|claro|opaco|El agua del lago es diáfana.|lenguaje
disperso|dis-per-so|adjetivo|Esparcido o separado en distintas direcciones.|esparcido|concentrado|Los datos están dispersos en varios archivos.|lenguaje
disruptivo|dis-rup-ti-vo|adjetivo|Que produce un cambio brusco y profundo en lo establecido.|rupturista|-|La nueva tecnología fue disruptiva para el comercio.|tecnología
drástico|drás-ti-co|adjetivo|Muy fuerte y rápido, que no admite medias tintas.|radical|moderado|Se tomaron medidas drásticas para ahorrar agua.|lenguaje
enrevesado|en-re-ve-sa-do|adjetivo|Muy complicado y difícil de entender.|intrincado|sencillo|Explicó el asunto de manera enrevesada.|lenguaje
ensimismado|en-si-mis-ma-do|adjetivo|Absorto en sus propios pensamientos.|abstraído|atento|Caminaba ensimismado, sin ver a nadie.|carácter
escueto|es-cue-to|adjetivo|Breve y sin adornos.|conciso|extenso|Dio una respuesta escueta.|lenguaje
espontáneo|es-pon-tá-ne-o|adjetivo|Que nace sin planificación y de manera natural.|natural|premeditado|Fue un aplauso espontáneo del público.|carácter
esporádico|es-po-rá-di-co|adjetivo|Que ocurre de vez en cuando, sin regularidad.|ocasional|frecuente|Tuvo contactos esporádicos con sus antiguos compañeros.|lenguaje
estéril|es-té-ril|adjetivo|Que no produce frutos o resultados; también, libre de gérmenes.|infértil|fértil|Fue una discusión estéril que no llevó a nada.|lenguaje
ético|é-ti-co|adjetivo|Que respeta los principios morales.|moral|inmoral|Es ético informar con honestidad.|ética
exacerbado|e-xa-cer-ba-do|adjetivo|Que se ha vuelto más intenso o más violento.|agravado|calmado|Un nacionalismo exacerbado generó conflictos.|lenguaje
excelso|ex-cel-so|adjetivo|De gran elevación o excelencia.|sublime|ínfimo|El poeta alcanzó una obra excelsa.|lenguaje
exiguo|e-xi-guo|adjetivo|Muy escaso o insuficiente.|escaso|abundante|El sueldo exiguo no cubría los gastos.|lenguaje
exorbitante|e-xor-bi-tan-te|adjetivo|Excesivo y fuera de lo razonable, sobre todo en precio.|desmedido|módico|Cobraron un precio exorbitante por una entrada.|economía
feroz|fe-roz|adjetivo|Muy violento o intenso.|fiero|manso|Hubo una feroz competencia entre los equipos.|lenguaje
fortuito|for-tui-to|adjetivo|Que sucede por azar.|casual|previsto|Fue un encuentro fortuito en la calle.|lenguaje
frugal|fru-gal|adjetivo|Moderado en el comer y el beber; sencillo.|sobrio|abundante|Tomó un almuerzo frugal de sopa y pan.|lenguaje
fútil|fú-til|adjetivo|Poco importante o sin valor.|trivial|importante|Perdieron tiempo en una discusión fútil.|lenguaje
grandilocuente|gran-di-lo-cuen-te|adjetivo|Que habla de manera pomposa y exagerada.|pomposo|sencillo|El discurso grandilocuente no convenció a nadie.|lenguaje
gregario|gre-ga-rio|adjetivo|Que vive en grupo o sigue siempre a la mayoría.|sociable|solitario|Las ovejas son animales gregarios.|lenguaje
hermético|her-mé-ti-co|adjetivo|Que está cerrado de manera que nada entra ni sale; también, difícil de comprender.|cerrado|abierto|Guardó la comida en un recipiente hermético.|lenguaje
ilustre|i-lus-tre|adjetivo|De fama y prestigio por sus méritos.|célebre|desconocido|Recibimos a un ilustre científico.|lenguaje
impasible|im-pa-si-ble|adjetivo|Que no muestra emoción ni se altera.|imperturbable|inquieto|Escuchó impasible la noticia.|carácter
imperante|im-pe-ran-te|adjetivo|Que domina en un momento o lugar.|predominante|-|La ideología imperante en esa época defendía el progreso.|lenguaje
impetuoso|im-pe-tuo-so|adjetivo|Que actúa con fuerza y rapidez, sin pensar mucho.|vehemente|sereno|Su carácter impetuoso lo metió en problemas.|carácter
improvisado|im-pro-vi-sa-do|adjetivo|Hecho sin preparación previa.|espontáneo|planificado|Dio un discurso improvisado.|lenguaje
incierto|in-cier-to|adjetivo|Que no es seguro ni conocido.|dudoso|seguro|El futuro del proyecto es incierto.|lenguaje
incisivo|in-ci-si-vo|adjetivo|Que ataca con agudeza.|penetrante|romo|Hizo una pregunta incisiva al candidato.|lenguaje
inconexo|in-co-ne-xo|adjetivo|Sin relación o sin hilo lógico entre sus partes.|incoherente|coherente|Su relato fue inconexo y difícil de seguir.|lenguaje
incuestionable|in-cues-tio-na-ble|adjetivo|Que no admite duda ni discusión.|indiscutible|cuestionable|Es un hecho incuestionable que el clima está cambiando.|argumentación
indeleble|in-de-le-ble|adjetivo|Que no se puede borrar.|imborrable|borrable|La experiencia dejó una huella indeleble en ella.|lenguaje
indiferente|in-di-fe-ren-te|adjetivo|Que no muestra interés ni preferencia.|apático|interesado|No puedo permanecer indiferente ante la injusticia.|carácter
indisoluble|in-di-so-lu-ble|adjetivo|Que no se puede deshacer ni separar.|inseparable|separable|Los une una amistad indisoluble.|lenguaje
inequívoco|i-ne-quí-vo-co|adjetivo|Que no admite duda ni confusión.|claro|ambiguo|Dio una señal inequívoca de que aceptaba.|lenguaje
inescrutable|i-nes-cru-ta-ble|adjetivo|Que no se puede conocer ni averiguar.|enigmático|evidente|Mantuvo un gesto inescrutable.|lenguaje
inestimable|i-nes-ti-ma-ble|adjetivo|Tan valioso que no puede medirse.|invaluable|despreciable|Su ayuda fue inestimable.|lenguaje
inocuo|i-no-cuo|adjetivo|Que no hace daño.|inofensivo|dañino|Esa sustancia es inocua para el cuerpo.|lenguaje
insondable|in-son-da-ble|adjetivo|Imposible de averiguar o de medir su profundidad.|profundo|superficial|El misterio de su desaparición es insondable.|lenguaje
insoslayable|in-sos-la-ya-ble|adjetivo|Que no se puede evitar ni dejar de lado.|ineludible|evitable|Cumplir las leyes es una obligación insoslayable.|lenguaje
intachable|in-ta-cha-ble|adjetivo|Que no tiene falta ni mancha.|irreprochable|reprochable|Tuvo una trayectoria intachable.|carácter
irrefutable|i-rre-fu-ta-ble|adjetivo|Que no se puede rebatir.|innegable|refutable|Presentó pruebas irrefutables.|argumentación
irrisorio|i-rri-so-rio|adjetivo|De valor tan bajo que resulta ridículo.|insignificante|considerable|Ofrecieron un precio irrisorio por el terreno.|economía
itinerante|i-ti-ne-ran-te|adjetivo|Que va de un lugar a otro.|ambulante|fijo|Una feria itinerante recorre los pueblos.|lenguaje
jerárquico|je-rár-qui-co|adjetivo|Organizado por grados o niveles de autoridad.|-|-|La empresa tiene una estructura jerárquica.|sociedad
jovial|jo-vial|adjetivo|Alegre y de buen humor.|alegre|melancólico|Es un maestro jovial que siempre bromea.|carácter
lacónico|la-có-ni-co|adjetivo|Que habla poco y de manera breve.|breve|locuaz|Su respuesta lacónica fue un simple sí.|lenguaje
lapidario|la-pi-da-rio|adjetivo|Dicho de una frase o una sentencia, tan definitiva que parece grabada en piedra.|categórico|-|Soltó una frase lapidaria que dejó a todos en silencio.|lenguaje
letárgico|le-tár-gi-co|adjetivo|Que está en un estado de sueño profundo o de gran lentitud.|aletargado|activo|Tras el almuerzo se sintió letárgico.|lenguaje
lúdico|lú-di-co|adjetivo|Relacionado con el juego.|-|-|El profesor propuso una actividad lúdica para aprender.|lenguaje
magnánimo|mag-ná-ni-mo|adjetivo|Generoso y comprensivo, sobre todo al perdonar.|generoso|mezquino|El rey magnánimo perdonó a los rebeldes.|carácter
mundano|mun-da-no|adjetivo|Relativo al mundo y a sus placeres, no a lo espiritual.|terrenal|espiritual|Prefiere una vida sencilla, lejos de lo mundano.|lenguaje
nocivo|no-ci-vo|adjetivo|Que hace daño.|dañino|beneficioso|El humo es nocivo para los pulmones.|salud
nutrido|nu-tri-do|adjetivo|Abundante o numeroso.|numeroso|escaso|Un nutrido grupo asistió al acto.|lenguaje
ominoso|o-mi-no-so|adjetivo|De mal presagio o muy desagradable.|ingrato|-|Un silencio ominoso precedió a la tormenta.|lenguaje
onírico|o-ní-ri-co|adjetivo|Relacionado con los sueños.|-|-|La película tiene imágenes oníricas y extrañas.|arte
pernicioso|per-ni-cio-so|adjetivo|Muy dañino, a veces de manera lenta o invisible.|nocivo|beneficioso|El rumor tuvo un efecto pernicioso en el grupo.|lenguaje
perplejo|per-ple-jo|adjetivo|Confuso y sorprendido, sin saber qué pensar.|desconcertado|seguro|Se quedó perplejo ante el resultado.|carácter
plausible|plau-si-ble|adjetivo|Que parece razonable y digno de aceptarse.|razonable|inverosímil|Es una explicación plausible del fenómeno.|argumentación
ponderado|pon-de-ra-do|adjetivo|Equilibrado y prudente al juzgar.|prudente|impulsivo|Dio una opinión ponderada sobre el conflicto.|carácter
prematuro|pre-ma-tu-ro|adjetivo|Que ocurre antes del tiempo debido.|temprano|tardío|Sería prematuro sacar conclusiones.|lenguaje
propicio|pro-pi-cio|adjetivo|Favorable para que algo ocurra.|favorable|adverso|El clima es propicio para sembrar.|lenguaje
pusilánime|pu-si-lá-ni-me|adjetivo|Que carece de valor para enfrentar las dificultades.|cobarde|valiente|Fue pusilánime y no se atrevió a hablar.|carácter
quimérico|qui-mé-ri-co|adjetivo|Producto de la imaginación, imposible de lograr.|ilusorio|real|Parecía un sueño quimérico, pero lo consiguieron.|lenguaje
rancio|ran-cio|adjetivo|Dicho de algo muy antiguo y pasado de moda, o de un alimento que huele y sabe mal por viejo.|anticuado|moderno|Esas costumbres rancias ya no tienen sentido.|lenguaje
renuente|re-nuen-te|adjetivo|Que se resiste a hacer algo.|reacio|dispuesto|Se mostró renuente a cambiar de opinión.|carácter
resuelto|re-suel-to|adjetivo|Decidido y que actúa con determinación.|decidido|indeciso|Caminó resuelto hacia la dirección.|carácter
reticente|re-ti-cen-te|adjetivo|Reservado y poco dispuesto a decir lo que piensa.|reservado|franco|Fue reticente al hablar de su pasado.|carácter
sigiloso|si-gi-lo-so|adjetivo|Que se hace con cuidado para no ser descubierto.|silencioso|ruidoso|El gato avanzó con pasos sigilosos.|lenguaje
simbólico|sim-bó-li-co|adjetivo|Que representa otra cosa mediante un símbolo.|-|literal|La paloma es un símbolo de paz.|lenguaje
solícito|so-lí-ci-to|adjetivo|Atento y dispuesto a servir.|diligente|indiferente|El camarero solícito nos trajo agua.|carácter
tosco|tos-co|adjetivo|Poco fino o mal acabado.|burdo|delicado|Fabricó una mesa tosca con restos de madera.|lenguaje
transitorio|tran-si-to-rio|adjetivo|Que dura poco tiempo y no es definitivo.|pasajero|permanente|Es una medida transitoria mientras se repara el edificio.|lenguaje
ufano|u-fa-no|adjetivo|Orgulloso y satisfecho.|orgulloso|humilde|Se mostró ufano por su premio.|carácter
venerable|ve-ne-ra-ble|adjetivo|Digno de gran respeto por su edad o sus méritos.|respetable|despreciable|El venerable anciano contó su historia.|lenguaje
vetusto|ve-tus-to|adjetivo|Muy antiguo y viejo.|antiguo|nuevo|Visitamos una vetusta casona del siglo diecinueve.|lenguaje
virulento|vi-ru-len-to|adjetivo|Muy violento o muy dañino; también, causado por un virus.|violento|suave|Hubo una discusión virulenta entre los candidatos.|lenguaje
voluble|vo-lu-ble|adjetivo|Que cambia con facilidad de opinión o de ánimo.|inconstante|constante|Un carácter voluble hace difícil confiar en él.|carácter
yermo|yer-mo|adjetivo|Dicho de un terreno sin cultivar o sin habitantes.|desierto|fértil|El valle yermo se cubrió de flores tras la lluvia.|lenguaje
zafio|za-fio|adjetivo|Grosero y poco educado.|grosero|refinado|Su comportamiento zafio incomodó a los invitados.|carácter
sustancial|sus-tan-cial|adjetivo|Importante y esencial.|esencial|secundario|Hubo una mejora sustancial en las notas.|lenguaje
tangencial|tan-gen-cial|adjetivo|Que toca algo solo de pasada, sin ser lo central.|superficial|central|Hizo un comentario tangencial sobre el tema.|argumentación
tentativo|ten-ta-ti-vo|adjetivo|Que se propone de modo provisional, para probar.|provisional|definitivo|Este es un plan tentativo que podemos modificar.|lenguaje
idóneo|i-dó-ne-o|adjetivo|Adecuado para lo que se necesita.|apropiado|inadecuado|Es la persona idónea para ese cargo.|lenguaje
óptimo|óp-ti-mo|adjetivo|Lo mejor posible.|excelente|pésimo|El agua está a una temperatura óptima para nadar.|lenguaje
supremo|su-pre-mo|adjetivo|Que está por encima de todo, en grado o autoridad.|máximo|ínfimo|La Corte Suprema es el tribunal más alto del país.|lenguaje
cabalmente|ca-bal-men-te|adverbio|De manera completa y exacta.|íntegramente|parcialmente|Cumplió cabalmente su tarea.|lenguaje
fehacientemente|fe-ha-cien-te-men-te|adverbio|De una forma que prueba algo sin dejar duda.|claramente|dudosamente|Demostró fehacientemente que tenía razón.|lenguaje
ineludiblemente|i-ne-lu-di-ble-men-te|adverbio|De modo que no se puede evitar.|forzosamente|evitablemente|Ineludiblemente, habrá que decidir pronto.|lenguaje
alcalino|al-ca-li-no|adjetivo|Dicho de una sustancia que tiene carácter básico, con un pH mayor que siete.|básico|ácido|El jabón es una sustancia alcalina.|química
entalpía|en-tal-pí-a|sustantivo femenino|Magnitud que mide el calor que se absorbe o se libera en una reacción a presión constante.|-|-|La entalpía de la reacción indica si libera o absorbe calor.|química
entropía|en-tro-pí-a|sustantivo femenino|Medida del desorden de un sistema.|desorden|-|La entropía aumenta cuando el hielo se derrite.|física
monómero|mo-nó-me-ro|sustantivo masculino|Molécula pequeña que se une con otras iguales para formar un polímero.|-|polímero|El etileno es el monómero del polietileno.|química
isómero|i-só-me-ro|sustantivo masculino|Compuesto que tiene los mismos átomos que otro, pero ordenados de forma distinta.|-|-|Dos isómeros pueden tener propiedades muy diferentes.|química
semiconductor|se-mi-con-duc-tor|sustantivo masculino|Material que conduce la electricidad mejor que un aislante, pero peor que un metal.|-|-|El silicio es un semiconductor usado en los chips.|física
superconductor|su-per-con-duc-tor|sustantivo masculino|Material que, a muy baja temperatura, conduce la electricidad sin ninguna resistencia.|-|-|Un superconductor permite transportar corriente sin pérdidas.|física
condensador|con-den-sa-dor|sustantivo masculino|Componente eléctrico que almacena carga por un breve tiempo.|-|-|El condensador del circuito guarda carga para el flash.|física
interferencia|in-ter-fe-ren-cia|sustantivo femenino|Efecto que ocurre cuando dos ondas se encuentran y se suman o se anulan; también, obstáculo que perturba algo.|-|-|La interferencia entre ondas produce zonas de más y de menos intensidad.|física
difracción|di-frac-ción|sustantivo femenino|Desvío de una onda cuando pasa por una abertura pequeña o rodea un obstáculo.|-|-|La difracción permite oír a alguien que está detrás de una esquina.|física
láser|lá-ser|sustantivo masculino|Aparato que produce un haz de luz muy intenso y concentrado.|-|-|El láser sirve para cortar metal y para operaciones del ojo.|física
fisión|fi-sión|sustantivo femenino|División del núcleo de un átomo pesado en núcleos más pequeños, con liberación de energía.|-|fusión|La fisión nuclear se usa en las centrales atómicas.|física
desintegración|de-sin-te-gra-ción|sustantivo femenino|Pérdida de partículas por parte de un núcleo inestable; también, ruptura de un todo en partes.|-|-|La desintegración radiactiva del uranio es muy lenta.|física
reactor|re-ac-tor|sustantivo masculino|Instalación donde se produce una reacción de manera controlada, como la nuclear.|-|-|El reactor de la central está protegido por muros gruesos.|física
relatividad|re-la-ti-vi-dad|sustantivo femenino|Teoría de Einstein que explica cómo el espacio y el tiempo dependen del movimiento y de la gravedad.|-|-|La relatividad cambió la manera de entender el tiempo.|física
supernova|su-per-no-va|sustantivo femenino|Explosión violenta con que termina la vida de ciertas estrellas.|-|-|Una supernova puede brillar más que toda su galaxia.|astronomía
exoplaneta|e-xo-pla-ne-ta|sustantivo masculino|Planeta que gira alrededor de una estrella distinta del Sol.|-|-|Los astrónomos han descubierto miles de exoplanetas.|astronomía
paralaje|pa-ra-la-je|sustantivo femenino|Cambio aparente en la posición de un objeto cuando se lo mira desde dos lugares distintos.|-|-|Los astrónomos usan la paralaje para medir la distancia a estrellas cercanas.|astronomía
cosmología|cos-mo-lo-gí-a|sustantivo femenino|Ciencia que estudia el origen, la estructura y la evolución del universo.|-|-|La cosmología estudia cómo el universo comenzó y cómo cambia.|astronomía
astrofísica|as-tro-fí-si-ca|sustantivo femenino|Ciencia que aplica la física al estudio de los astros.|-|-|La astrofísica explica por qué brillan las estrellas.|astronomía
radiotelescopio|ra-dio-te-les-co-pio|sustantivo masculino|Instrumento que capta ondas de radio procedentes del espacio.|-|-|Un radiotelescopio del desierto de Atacama capta señales de galaxias lejanas.|astronomía
perihelio|pe-ri-he-lio|sustantivo masculino|Punto de la órbita de un planeta en que está más cerca del Sol.|-|afelio|La Tierra pasa por el perihelio a comienzos de enero.|astronomía
afelio|a-fe-lio|sustantivo masculino|Punto de la órbita de un planeta en que está más lejos del Sol.|-|perihelio|En el afelio la Tierra está a su máxima distancia del Sol.|astronomía
ionosfera|io-nos-fe-ra|sustantivo femenino|Capa alta de la atmósfera con partículas cargadas que reflejan las ondas de radio.|-|-|La ionosfera permite que las señales de radio viajen lejos.|ciencias de la Tierra
estratosfera|es-tra-tos-fe-ra|sustantivo femenino|Capa de la atmósfera sobre la troposfera, donde está la capa de ozono.|-|-|La capa de ozono se encuentra en la estratosfera.|ciencias de la Tierra
termosfera|ter-mos-fe-ra|sustantivo femenino|Capa de la atmósfera en que la temperatura aumenta mucho con la altura.|-|-|Los satélites orbitan cerca de la termosfera.|ciencias de la Tierra
albedo|al-be-do|sustantivo masculino|Proporción de luz que una superficie refleja respecto de la que recibe.|-|-|La nieve tiene un albedo alto porque refleja casi toda la luz.|ciencias de la Tierra
ciclón|ci-clón|sustantivo masculino|Zona de bajas presiones con vientos que giran con fuerza.|tormenta|anticiclón|El ciclón dejó lluvias intensas en la costa.|ciencias de la Tierra
monzón|mon-zón|sustantivo masculino|Viento que cambia de dirección con las estaciones y trae lluvias abundantes.|-|-|El monzón trae las lluvias a Asia en verano.|ciencias de la Tierra
surgencia|sur-gen-cia|sustantivo femenino|Ascenso de aguas profundas, frías y ricas en nutrientes hacia la superficie del mar.|-|-|La surgencia frente a la costa explica la abundancia de peces.|ciencias de la Tierra
plataforma continental|pla-ta-for-ma con-ti-nen-tal|locución nominal|Zona poco profunda del fondo marino que rodea a los continentes.|-|-|La plataforma continental es rica en pesca.|ciencias de la Tierra
talud|ta-lud|sustantivo masculino|Pendiente inclinada de un terreno o del fondo marino.|-|-|El talud continental baja hacia el fondo del océano.|ciencias de la Tierra
tectónica de placas|tec-tó-ni-ca de pla-cas|locución nominal|Teoría que explica el movimiento lento de grandes bloques que forman la corteza terrestre.|-|-|La tectónica de placas explica los terremotos y las cordilleras.|ciencias de la Tierra
piroclasto|pi-ro-clas-to|sustantivo masculino|Fragmento de roca que lanza un volcán al hacer erupción.|-|-|Los piroclastos cayeron cerca del cráter.|ciencias de la Tierra
bofedal|bo-fe-dal|sustantivo masculino|Humedal del altiplano andino donde crece vegetación y pastan llamas y alpacas.|-|-|Los bofedales almacenan agua en la cordillera.|ambiente
ecorregión|e-co-rre-gión|sustantivo femenino|Zona extensa con clima, suelo y seres vivos similares.|-|-|Chile tiene varias ecorregiones, desde el desierto hasta los bosques del sur.|ambiente
páramo|pá-ra-mo|sustantivo masculino|Terreno alto, frío y desabrigado, con poca vegetación.|-|-|El viento helado recorre el páramo.|ambiente
comensalismo|co-men-sa-lis-mo|sustantivo masculino|Relación entre dos especies en la que una se beneficia y la otra no se ve afectada.|-|-|Las aves que descansan en un árbol viven en comensalismo con él.|biología
depredación|de-pre-da-ción|sustantivo femenino|Caza de un animal por parte de otro para alimentarse.|-|-|La depredación mantiene el equilibrio entre las poblaciones.|biología
sucesión ecológica|su-ce-sión e-co-ló-gi-ca|locución nominal|Cambio gradual de las especies que ocupan un lugar hasta formar una comunidad estable.|-|-|Después del incendio comenzó una sucesión ecológica en el bosque.|biología
bioindicador|bio-in-di-ca-dor|sustantivo masculino|Ser vivo cuya presencia o ausencia indica el estado del ambiente.|-|-|Los líquenes son bioindicadores de la calidad del aire.|biología
bioacumulación|bio-a-cu-mu-la-ción|sustantivo femenino|Aumento de una sustancia tóxica en el cuerpo de un ser vivo con el paso del tiempo.|-|-|La bioacumulación de mercurio en los peces afecta a quien los come.|biología
glucólisis|glu-có-li-sis|sustantivo femenino|Proceso en que la célula descompone la glucosa para obtener energía.|-|-|La glucólisis ocurre en el citoplasma de la célula.|biología
micorriza|mi-co-rri-za|sustantivo femenino|Asociación entre un hongo y las raíces de una planta que beneficia a ambos.|-|-|La micorriza ayuda al árbol a absorber agua y minerales.|biología
bosque esclerófilo|bos-que es-cle-ró-fi-lo|locución nominal|Bosque de la zona central de Chile con árboles de hojas duras y brillantes que resisten la sequía.|-|-|El bosque esclerófilo incluye especies como el quillay y el peumo.|ambiente
bosque valdiviano|bos-que val-di-via-no|locución nominal|Bosque lluvioso del sur de Chile, muy denso y con gran variedad de especies.|-|-|El bosque valdiviano conserva alerces y helechos gigantes.|ambiente
abolengo|a-bo-len-go|sustantivo masculino|Origen noble o antiguo de una familia.|linaje|-|Presumía de su abolengo, aunque su familia ya no tenía fortuna.|sociedad
acaparamiento|a-ca-pa-ra-mien-to|sustantivo masculino|Compra o retención de grandes cantidades de un producto para controlar su venta.|-|-|El acaparamiento de alimentos hizo subir los precios.|economía
acechanza|a-ce-chan-za|sustantivo femenino|Vigilancia oculta para atacar o sorprender a alguien.|emboscada|-|Vivían bajo la constante acechanza de los ladrones.|lenguaje
afán|a-fán|sustantivo masculino|Deseo intenso de lograr algo; también, trabajo duro.|empeño|desgano|Estudia con afán de superarse.|carácter
agudeza|a-gu-de-za|sustantivo femenino|Capacidad de percibir o de pensar con rapidez y precisión.|ingenio|torpeza|Respondió con agudeza a la pregunta difícil.|carácter
aliciente|a-li-cien-te|sustantivo masculino|Cosa que mueve o incita a hacer algo.|incentivo|desaliento|El premio fue un aliciente para esforzarse más.|carácter
amago|a-ma-go|sustantivo masculino|Gesto o señal de que se va a hacer algo, aunque no se llegue a hacer.|conato|-|Hizo un amago de salir, pero se quedó.|lenguaje
anuencia|a-nuen-cia|sustantivo femenino|Consentimiento o permiso que se da para algo.|consentimiento|negativa|Entró al local con la anuencia del dueño.|lenguaje
apatía|a-pa-tí-a|sustantivo femenino|Falta de interés, de ánimo o de ganas de hacer cosas.|desgana|entusiasmo|La apatía del grupo hizo fracasar la campaña.|carácter
aprensión|a-pren-sión|sustantivo femenino|Temor o desconfianza ante algo que podría hacernos daño.|recelo|confianza|Sintió aprensión al subir al avión.|carácter
arbitrio|ar-bi-trio|sustantivo masculino|Facultad de decidir según la propia voluntad.|voluntad|-|Dejó el asunto al arbitrio del comité.|lenguaje
ascendiente|as-cen-dien-te|sustantivo masculino|Influencia que una persona tiene sobre otras.|influencia|-|El profesor tiene gran ascendiente sobre sus alumnos.|lenguaje
aspereza|as-pe-re-za|sustantivo femenino|Característica de lo que no es suave; también, dureza en el trato.|rugosidad|suavidad|Le habló con aspereza y se arrepintió después.|lenguaje
atisbo|a-tis-bo|sustantivo masculino|Indicio leve o primera señal de algo.|indicio|-|No había ni un atisbo de duda en su voz.|lenguaje
audacia|au-da-cia|sustantivo femenino|Valor para hacer cosas arriesgadas o nuevas.|atrevimiento|timidez|Con audacia, propuso un cambio al plan.|carácter
augurio|au-gu-rio|sustantivo masculino|Señal que anuncia cómo será el futuro.|presagio|-|Las nubes oscuras eran un mal augurio para el picnic.|lenguaje
avidez|a-vi-dez|sustantivo femenino|Deseo muy fuerte y apresurado de algo.|ansia|desgana|Leyó la novela con avidez en una sola tarde.|carácter
baluarte|ba-luar-te|sustantivo masculino|Lugar o persona que defiende algo con firmeza.|bastión|-|La biblioteca es un baluarte de la cultura del barrio.|lenguaje
bastión|bas-tión|sustantivo masculino|Lugar firme que sirve de defensa; también, grupo que defiende con fuerza una causa.|fortaleza|-|Ese colegio es un bastión de la educación pública.|lenguaje
bochorno|bo-chor-no|sustantivo masculino|Calor sofocante; también, vergüenza intensa.|sofoco|frescura|El bochorno de la tarde anunciaba tormenta.|lenguaje
bonanza|bo-nan-za|sustantivo femenino|Tiempo de calma en el mar; también, período de prosperidad.|prosperidad|crisis|La bonanza económica trajo nuevos empleos.|economía
bullicio|bu-lli-cio|sustantivo masculino|Ruido y movimiento de mucha gente reunida.|alboroto|silencio|El bullicio del mercado despertó a todo el barrio.|lenguaje
cabida|ca-bi-da|sustantivo femenino|Espacio o capacidad para contener algo; también, posibilidad de aceptar algo.|capacidad|-|En esta sala hay cabida para cien personas.|lenguaje
calibre|ca-li-bre|sustantivo masculino|Diámetro interior de un tubo o de un arma; también, importancia o tamaño de algo.|diámetro|-|Fue un error de gran calibre.|lenguaje
celo|ce-lo|sustantivo masculino|Cuidado y entrega al hacer algo; también, impulso de los animales en época de reproducción.|esmero|descuido|Cumple su trabajo con celo.|carácter
cese|ce-se|sustantivo masculino|Fin o interrupción de una acción.|interrupción|inicio|Pidieron el cese de las hostilidades.|lenguaje
convicción|con-vic-ción|sustantivo femenino|Seguridad firme de que algo es cierto o correcto.|certeza|duda|Habló con convicción sobre la importancia del voto.|carácter
coyuntura|co-yun-tu-ra|sustantivo femenino|Conjunto de circunstancias que se dan en un momento determinado.|situación|-|En la coyuntura actual conviene ahorrar.|economía
credo|cre-do|sustantivo masculino|Conjunto de creencias de una persona o de un grupo.|doctrina|-|Respetaba el credo de cada compañero.|lenguaje
cúmulo|cú-mu-lo|sustantivo masculino|Gran cantidad de cosas juntas.|montón|escasez|Tuvo un cúmulo de problemas en una semana.|lenguaje
decoro|de-co-ro|sustantivo masculino|Respeto a las normas de conducta y a la propia dignidad.|decencia|indecoro|Se comportó con decoro durante la ceremonia.|carácter
delirio|de-li-rio|sustantivo masculino|Trastorno de la mente en que se dicen o se creen cosas fuera de la realidad.|desvarío|lucidez|Con la fiebre alta empezó a tener delirios.|salud
demasía|de-ma-sí-a|sustantivo femenino|Exceso en algo.|exceso|escasez|Hubo demasía de comida en la fiesta.|lenguaje
desazón|de-sa-zón|sustantivo femenino|Inquietud o disgusto interior.|inquietud|tranquilidad|Sentía una desazón que no lo dejaba dormir.|carácter
desidia|de-si-dia|sustantivo femenino|Falta de interés y de cuidado en lo que se debe hacer.|abandono|diligencia|La desidia de los vecinos dejó la plaza sucia.|carácter
despojo|des-po-jo|sustantivo masculino|Acción de quitar algo a alguien con violencia o con abuso.|expolio|restitución|Los comuneros denunciaron el despojo de sus tierras.|derecho
detrimento|de-tri-men-to|sustantivo masculino|Daño o pérdida que sufre algo.|perjuicio|beneficio|Estudió en detrimento de su descanso.|lenguaje
devenir|de-ve-nir|sustantivo masculino|Proceso de cambio y transformación a lo largo del tiempo.|transcurso|-|Los filósofos reflexionaron sobre el devenir de las cosas.|filosofía
dádiva|dá-di-va|sustantivo femenino|Cosa que se da de manera gratuita.|regalo|-|Recibió con gratitud la dádiva de sus vecinos.|lenguaje
diatriba|dia-tri-ba|sustantivo femenino|Discurso violento y ofensivo contra algo o alguien.|ataque|elogio|Lanzó una diatriba contra la corrupción.|lenguaje
divergencia|di-ver-gen-cia|sustantivo femenino|Diferencia de opiniones o de caminos que se separan.|discrepancia|coincidencia|Hubo divergencias sobre cómo organizar la actividad.|argumentación
dolencia|do-len-cia|sustantivo femenino|Enfermedad o dolor persistente.|achaque|-|Una dolencia en la espalda lo obligó a descansar.|salud
duelo|due-lo|sustantivo masculino|Dolor y tristeza por la muerte de alguien; también, combate entre dos personas.|pena|alegría|La familia vivió su duelo con el apoyo de los amigos.|lenguaje
ecuanimidad|e-cua-ni-mi-dad|sustantivo femenino|Serenidad y equilibrio para juzgar o reaccionar.|serenidad|apasionamiento|El juez actuó con ecuanimidad.|carácter
efigie|e-fi-gie|sustantivo femenino|Imagen o representación de una persona en una moneda, una estatua o un grabado.|-|-|La moneda lleva la efigie de un prócer.|arte
embate|em-ba-te|sustantivo masculino|Golpe fuerte y violento, como el de las olas.|golpe|-|El muelle resistió el embate del temporal.|lenguaje
enclave|en-cla-ve|sustantivo masculino|Territorio o grupo rodeado por otro de distinto carácter.|-|-|La pequeña aldea es un enclave en medio del valle.|geografía
encrucijada|en-cru-ci-ja-da|sustantivo femenino|Lugar donde se cruzan varios caminos; también, situación difícil en que hay que decidir.|disyuntiva|-|Estaba en una encrucijada: estudiar o trabajar.|lenguaje
envergadura|en-ver-ga-du-ra|sustantivo femenino|Importancia o tamaño de algo; distancia entre las puntas de las alas abiertas.|magnitud|-|Es un proyecto de gran envergadura.|lenguaje
escollo|es-co-llo|sustantivo masculino|Peñasco a flor de agua; también, dificultad que obstaculiza algo.|obstáculo|facilidad|El mayor escollo fue conseguir el permiso.|lenguaje
esmero|es-me-ro|sustantivo masculino|Cuidado grande que se pone al hacer algo.|cuidado|descuido|Preparó la cena con esmero.|carácter
espejismo|es-pe-jis-mo|sustantivo masculino|Ilusión óptica que hace ver cosas que no existen; también, idea engañosa.|ilusión|realidad|La laguna en el desierto resultó ser un espejismo.|lenguaje
estigma|es-tig-ma|sustantivo masculino|Marca social negativa que se asigna a una persona o a un grupo.|deshonra|-|Las enfermedades mentales todavía cargan con un estigma.|sociedad
estratagema|es-tra-ta-ge-ma|sustantivo femenino|Plan ingenioso para engañar o lograr algo.|ardid|-|Usó una estratagema para escapar sin ser visto.|lenguaje
evasiva|e-va-si-va|sustantivo femenino|Respuesta que sirve para evitar una pregunta o un compromiso.|rodeo|-|Respondió con evasivas cuando le preguntaron por la deuda.|lenguaje
exhorto|ex-hor-to|sustantivo masculino|Petición o aviso que se hace para animar a hacer algo.|llamado|-|El alcalde hizo un exhorto a cuidar el agua.|lenguaje
expectativa|ex-pec-ta-ti-va|sustantivo femenino|Esperanza de que algo ocurra.|esperanza|-|Había mucha expectativa por el resultado del partido.|lenguaje
facción|fac-ción|sustantivo femenino|Grupo dentro de un conjunto mayor que sigue sus propias ideas; también, rasgo del rostro.|bando|-|Una facción del partido se opuso a la propuesta.|ciudadanía
falencia|fa-len-cia|sustantivo femenino|Falla o error en algo (uso frecuente en América).|falla|acierto|El informe mostró varias falencias en el sistema.|lenguaje
filón|fi-lón|sustantivo masculino|Veta de mineral en la roca; también, fuente de riqueza o de oportunidades.|veta|-|El minero encontró un rico filón de cobre.|economía
flaqueza|fla-que-za|sustantivo femenino|Debilidad de fuerza o de carácter.|debilidad|fortaleza|Mostró flaqueza al ceder a la presión.|carácter
fuero|fue-ro|sustantivo masculino|Privilegio o derecho especial de una persona o institución.|prerrogativa|-|Los parlamentarios tienen fuero para expresar sus opiniones.|derecho
germen|ger-men|sustantivo masculino|Origen o principio de algo; también, microbio.|origen|-|En esa conversación estaba el germen del proyecto.|lenguaje
grieta|grie-ta|sustantivo femenino|Abertura larga y estrecha en una superficie; también, separación entre grupos.|fisura|-|Una grieta apareció en el muro tras el temblor.|lenguaje
holgura|hol-gu-ra|sustantivo femenino|Amplitud o espacio suficiente; también, bienestar económico.|amplitud|estrechez|Vive con holgura gracias a sus ahorros.|lenguaje
honra|hon-ra|sustantivo femenino|Buena fama y estima propia o ajena.|honor|deshonra|Defendió la honra de su familia.|valores
ignominia|ig-no-mi-nia|sustantivo femenino|Deshonra pública y grave.|deshonra|honor|La traición cubrió de ignominia al jefe.|lenguaje
ingenio|in-ge-nio|sustantivo masculino|Habilidad para inventar soluciones; también, chispa para el humor.|inventiva|torpeza|Con ingenio, armó una mesa con cajas viejas.|carácter
injerencia|in-je-ren-cia|sustantivo femenino|Intromisión en asuntos que no corresponden.|intromisión|-|Rechazaron la injerencia de otros países en sus asuntos.|ciudadanía
inquina|in-qui-na|sustantivo femenino|Antipatía o rencor hacia alguien.|animadversión|simpatía|Le tenía inquina desde la discusión del año pasado.|carácter
insignia|in-sig-nia|sustantivo femenino|Distintivo que identifica a una persona o a un grupo.|emblema|-|Llevaba la insignia del colegio en la solapa.|lenguaje
ínfulas|ín-fu-las|sustantivo femenino plural|Presunción excesiva.|pretensión|modestia|Se da ínfulas de experto sin haber leído el libro.|carácter
índole|ín-do-le|sustantivo femenino|Carácter propio de una persona; también, clase o naturaleza de una cosa.|naturaleza|-|Consultaron sobre asuntos de índole personal.|lenguaje
labor|la-bor|sustantivo femenino|Trabajo o tarea.|tarea|ocio|La labor de los voluntarios fue clave tras el temporal.|trabajo
lastre|las-tre|sustantivo masculino|Peso que se pone en un barco o un globo para darle estabilidad; también, carga que impide avanzar.|carga|-|Las viejas costumbres fueron un lastre para el cambio.|lenguaje
lazo|la-zo|sustantivo masculino|Cinta o cuerda anudada; también, vínculo afectivo.|nudo|-|Los lazos entre los vecinos se fortalecieron.|lenguaje
lid|lid|sustantivo femenino|Combate o competencia.|combate|-|Los candidatos entraron en lid con sus propuestas.|lenguaje
mácula|má-cu-la|sustantivo femenino|Mancha, o deshonra que cae sobre alguien.|mancha|pureza|Su historial no tiene ninguna mácula.|lenguaje
marasmo|ma-ras-mo|sustantivo masculino|Estado de inmovilidad, apatía y falta de energía.|letargo|dinamismo|La ciudad cayó en un marasmo económico.|lenguaje
mengua|men-gua|sustantivo femenino|Disminución o pérdida de algo.|disminución|aumento|La mengua del caudal preocupó a los agricultores.|lenguaje
merced|mer-ced|sustantivo femenino|Favor o gracia que se concede; poder o voluntad de alguien.|favor|-|Quedó a merced del viento en medio del lago.|lenguaje
minucia|mi-nu-cia|sustantivo femenino|Cosa de poca importancia.|nimiedad|-|No discutamos por una minucia.|lenguaje
monotonía|mo-no-to-ní-a|sustantivo femenino|Falta de variedad que cansa o aburre.|rutina|variedad|Buscaba escapar de la monotonía de su rutina.|lenguaje
nimiedad|ni-mie-dad|sustantivo femenino|Cosa sin importancia.|bagatela|-|Se enojó por una nimiedad.|lenguaje
nostalgia|nos-tal-gia|sustantivo femenino|Tristeza suave que se siente al recordar algo bueno del pasado.|añoranza|-|Sintió nostalgia al ver sus fotos de la infancia.|carácter
obstinación|obs-ti-na-ción|sustantivo femenino|Terquedad en mantener una idea o una actitud.|terquedad|flexibilidad|Su obstinación le impidió aceptar ayuda.|carácter
ocaso|o-ca-so|sustantivo masculino|Puesta del sol; también, decadencia o final de algo.|atardecer|amanecer|Contemplamos el ocaso desde la playa.|lenguaje
oprobio|o-pro-bio|sustantivo masculino|Deshonra o humillación pública.|ignominia|honra|Soportó el oprobio con dignidad.|lenguaje
orfandad|or-fan-dad|sustantivo femenino|Situación de quien ha perdido a su padre o a su madre; también, abandono o desamparo.|desamparo|amparo|Creció en la orfandad, cuidada por sus abuelos.|lenguaje
parangón|pa-ran-gón|sustantivo masculino|Comparación entre dos cosas para mostrar su semejanza o su diferencia.|comparación|-|Su talento no tiene parangón en el equipo.|lenguaje
penuria|pe-nu-ria|sustantivo femenino|Escasez de lo necesario para vivir.|escasez|abundancia|Pasaron penurias durante el invierno.|lenguaje
pesquisa|pes-qui-sa|sustantivo femenino|Investigación para descubrir algo o a alguien.|indagación|-|La policía realizó una pesquisa en el barrio.|lenguaje
pleito|plei-to|sustantivo masculino|Disputa que se lleva a un tribunal; también, riña.|litigio|acuerdo|Un pleito por la herencia dividió a la familia.|derecho
plenitud|ple-ni-tud|sustantivo femenino|Estado en que algo está completo o en su mejor momento.|apogeo|decadencia|Se sentía en plenitud de sus capacidades.|lenguaje
portento|por-ten-to|sustantivo masculino|Persona o cosa que causa admiración por ser extraordinaria.|maravilla|-|Esa pianista es un portento de la música.|lenguaje
postergación|pos-ter-ga-ción|sustantivo femenino|Retraso de algo para hacerlo más tarde.|aplazamiento|adelanto|La postergación del examen alegró al curso.|lenguaje
precepto|pre-cep-to|sustantivo masculino|Norma o mandato que se debe cumplir.|norma|-|Cumplía con el precepto de respetar a sus mayores.|lenguaje
preeminencia|pre-e-mi-nen-cia|sustantivo femenino|Superioridad o ventaja de una cosa sobre otras.|primacía|-|La preeminencia del puerto lo convirtió en centro del comercio.|lenguaje
prodigio|pro-di-gio|sustantivo masculino|Suceso extraordinario; persona con talento fuera de lo común.|portento|-|Era un niño prodigio del ajedrez.|lenguaje
pulcritud|pul-cri-tud|sustantivo femenino|Aseo y orden muy cuidados.|limpieza|desaseo|Presentó su trabajo con pulcritud.|carácter
quimera|qui-me-ra|sustantivo femenino|Ilusión que se cree posible, pero no lo es; ser mitológico.|ilusión|realidad|Para muchos, tener casa propia era una quimera.|lenguaje
rémora|ré-mo-ra|sustantivo femenino|Obstáculo que frena o retrasa algo.|obstáculo|impulso|La burocracia es una rémora para el proyecto.|lenguaje
repliegue|re-plie-gue|sustantivo masculino|Retirada ordenada; también, pliegue doble.|retirada|avance|El ejército ordenó el repliegue de sus tropas.|lenguaje
resabio|re-sa-bio|sustantivo masculino|Sabor desagradable que queda; también, mala costumbre.|vicio|-|Aún tenía el resabio de la medicina en la boca.|lenguaje
resquicio|res-qui-cio|sustantivo masculino|Abertura estrecha entre dos cosas; también, posibilidad pequeña.|rendija|-|Por un resquicio de la puerta entraba la luz.|lenguaje
revés|re-vés|sustantivo masculino|Cara posterior de algo; también, golpe de mala suerte.|dorso|derecho|Sufrió un revés económico al perder su trabajo.|lenguaje
saña|sa-ña|sustantivo femenino|Rabia con que se hace daño a alguien.|crueldad|piedad|Lo atacó con saña.|lenguaje
secuela|se-cue-la|sustantivo femenino|Consecuencia que queda después de una enfermedad o un suceso.|consecuencia|-|El accidente le dejó secuelas en la rodilla.|salud
sigilo|si-gi-lo|sustantivo masculino|Silencio o cuidado con que se hace algo para no ser notado.|discreción|escándalo|Salió de la habitación con sigilo.|lenguaje
sustento|sus-ten-to|sustantivo masculino|Alimento necesario para vivir; también, apoyo o base.|alimento|-|Con su trabajo gana el sustento de la familia.|lenguaje
tara|ta-ra|sustantivo femenino|Defecto que desvaloriza algo; peso del envase de un producto.|defecto|virtud|El informe mostró una tara en el diseño.|lenguaje
trance|tran-ce|sustantivo masculino|Momento difícil o decisivo.|situación|-|Pasó por un duro trance al perder su empleo.|lenguaje
vaticinio|va-ti-ci-nio|sustantivo masculino|Anuncio de lo que ocurrirá en el futuro.|predicción|-|El vaticinio del meteorólogo se cumplió.|lenguaje
vileza|vi-le-za|sustantivo femenino|Maldad que causa desprecio.|bajeza|nobleza|Calumniar a un amigo es una vileza.|carácter
vislumbre|vis-lum-bre|sustantivo femenino|Indicio o sospecha de algo.|indicio|-|Tuvo un vislumbre de la solución al ver el esquema.|lenguaje
yugo|yu-go|sustantivo masculino|Instrumento que une a los bueyes para arar; también, dominio opresivo.|opresión|libertad|El pueblo se liberó del yugo colonial.|lenguaje
celeridad|ce-le-ri-dad|sustantivo femenino|Rapidez al hacer algo.|rapidez|lentitud|Actuó con celeridad ante la emergencia.|lenguaje
albur|al-bur|sustantivo masculino|Azar o riesgo al que se somete algo.|azar|-|Dejó la decisión al albur de una moneda.|lenguaje
ardid|ar-did|sustantivo masculino|Medio ingenioso, a menudo engañoso, para conseguir algo.|treta|-|Usó un ardid para entrar sin entrada.|lenguaje
tribulación|tri-bu-la-ción|sustantivo femenino|Pena o sufrimiento profundo.|aflicción|alegría|Superó muchas tribulaciones con paciencia.|carácter
parsimonia|par-si-mo-nia|sustantivo femenino|Lentitud y calma al actuar.|calma|prisa|Preparó el té con parsimonia.|carácter
ráfaga|rá-fa-ga|sustantivo femenino|Golpe de viento fuerte y breve; también, serie rápida de disparos o de destellos.|racha|-|Una ráfaga de viento voló los papeles.|lenguaje
reticencia|re-ti-cen-cia|sustantivo femenino|Reserva o desconfianza al decir o aceptar algo.|reserva|franqueza|Aceptó la propuesta con reticencia.|carácter
sinsabor|sin-sa-bor|sustantivo masculino|Disgusto o pena.|disgusto|alegría|El viaje dejó más de un sinsabor.|carácter
sobrecogimiento|so-bre-co-gi-mien-to|sustantivo masculino|Sensación de miedo y asombro ante algo imponente.|asombro|-|Sintió sobrecogimiento ante la inmensidad del glaciar.|carácter
talante|ta-lan-te|sustantivo masculino|Estado de ánimo o disposición de una persona.|humor|-|Tiene un talante dialogante y abierto.|carácter
tropiezo|tro-pie-zo|sustantivo masculino|Caída o dificultad que aparece en un proceso.|contratiempo|-|Superó el tropiezo y siguió adelante.|lenguaje
urdimbre|ur-dim-bre|sustantivo femenino|Conjunto de hilos que se colocan a lo largo en un telar; también, trama o conjunto de relaciones.|trama|-|La urdimbre de intereses políticos era muy compleja.|lenguaje
a priori|a pri-o-ri|locución adverbial|Antes de examinar los hechos, solo por razonamiento o por suposición.|-|a posteriori|A priori parece buena idea, pero hay que probarla.|lenguaje
a posteriori|a pos-te-ri-o-ri|locución adverbial|Después de haber visto los hechos o la experiencia.|-|a priori|A posteriori entendimos por qué falló el plan.|lenguaje
de facto|de fac-to|locución adverbial|Que ocurre en la práctica, aunque no esté reconocido por la ley.|-|de iure|Era el líder de facto del grupo, aunque no tenía cargo.|lenguaje
de iure|de iu-re|locución adverbial|Conforme a la ley, de manera formal.|-|de facto|El presidente era jefe de Estado de iure, pero el ejército mandaba.|lenguaje
per cápita|per cá-pi-ta|locución adjetiva|Por cada persona.|-|-|El ingreso per cápita del país aumentó este año.|economía
in situ|in si-tu|locución adverbial|En el mismo lugar donde ocurre algo.|-|-|Los geólogos estudiaron la roca in situ.|lenguaje
ad hoc|ad hoc|locución adjetiva|Hecho o pensado para un fin específico.|-|-|Crearon una comisión ad hoc para resolver el problema.|lenguaje
grosso modo|gros-so mo-do|locución adverbial|De forma aproximada, sin entrar en detalles.|aproximadamente|detalladamente|Explicó grosso modo cómo funciona el sistema.|lenguaje
sine qua non|si-ne qua non|locución adjetiva|Dicho de una condición indispensable, sin la cual algo no puede darse.|imprescindible|prescindible|La honestidad es condición sine qua non de la amistad.|lenguaje
statu quo|sta-tu quo|locución nominal|Estado actual de las cosas en un momento determinado.|-|-|Algunos grupos querían mantener el statu quo y otros cambiarlo.|lenguaje
motu proprio|mo-tu pro-prio|locución adverbial|Por propia voluntad, sin que nadie lo pida.|voluntariamente|obligado|Renunció motu proprio al cargo.|lenguaje
verbigracia|ver-bi-gra-cia|adverbio|Por ejemplo.|por ejemplo|-|Hay varias fuentes de energía limpia, verbigracia, la solar.|lenguaje
ipso facto|ip-so fac-to|locución adverbial|Inmediatamente, por el hecho mismo.|enseguida|-|Quien ofenda a otros queda ipso facto fuera de la actividad.|lenguaje
vox populi|vox po-pu-li|locución nominal|Lo que es conocido y dicho por todo el mundo.|rumor público|-|Era vox populi que el colegio cambiaría de sede.|lenguaje
alter ego|al-ter e-go|locución nominal|Persona de total confianza que puede actuar en lugar de otra; segundo yo.|-|-|El personaje de ficción era el alter ego del autor.|literatura
ínterin|ín-te-rin|sustantivo masculino|Espacio de tiempo entre dos momentos.|intervalo|-|En el ínterin, los invitados fueron llegando.|lenguaje
mutatis mutandis|mu-ta-tis mu-tan-dis|locución adverbial|Cambiando lo que haya que cambiar.|-|-|Esa regla vale para todos, mutatis mutandis.|lenguaje
a mansalva|a man-sal-va|locución adverbial|En gran cantidad y sin riesgo.|abundantemente|escasamente|Recibió críticas a mansalva por esa decisión.|lenguaje
al unísono|al u-ní-so-no|locución adverbial|A la vez y de manera coordinada.|a coro|por separado|El curso respondió al unísono.|lenguaje
a ciegas|a cie-gas|locución adverbial|Sin ver; también, sin pensar ni informarse.|-|-|No firmes un contrato a ciegas.|lenguaje
a la postre|a la pos-tre|locución adverbial|Al final, después de todo.|finalmente|al principio|A la postre, su paciencia dio resultados.|lenguaje
a título de|a tí-tu-lo de|locución preposicional|En calidad de, con el carácter de.|como|-|Asistió a título de invitado.|lenguaje
a raíz de|a ra-íz de|locución preposicional|Como consecuencia de algo.|debido a|-|A raíz de la sequía, se racionó el agua.|lenguaje
a tenor de|a te-nor de|locución preposicional|Según lo que expresa o indica algo.|según|-|A tenor de los resultados, conviene cambiar la estrategia.|lenguaje
en aras de|en a-ras de|locución preposicional|Con el propósito de lograr algo.|en pos de|-|Cedió en aras de la convivencia.|lenguaje
en pos de|en pos de|locución preposicional|En busca de algo; detrás de algo.|en busca de|-|Viajó a la ciudad en pos de nuevas oportunidades.|lenguaje
en virtud de|en vir-tud de|locución preposicional|A causa de o por efecto de algo.|debido a|-|En virtud de la ley, tiene derecho a esa información.|lenguaje
en detrimento de|en de-tri-men-to de|locución preposicional|Causando perjuicio a algo.|en perjuicio de|en beneficio de|Se priorizó el comercio en detrimento del ambiente.|lenguaje
en consonancia con|en con-so-nan-cia con|locución preposicional|De acuerdo con algo, de manera armónica.|conforme a|en contra de|Sus actos están en consonancia con sus ideas.|lenguaje
merced a|mer-ced a|locución preposicional|Gracias a, por efecto de.|gracias a|-|Merced a su esfuerzo, ganó la beca.|lenguaje
so pretexto de|so pre-tex-to de|locución preposicional|Usando como excusa.|con la excusa de|-|Se fue so pretexto de un dolor de cabeza.|lenguaje
con miras a|con mi-ras a|locución preposicional|Con el fin de lograr algo en el futuro.|con el objetivo de|-|Ahorra con miras a comprar un computador.|lenguaje
de cara a|de ca-ra a|locución preposicional|Pensando en lo que viene o en lo que se aproxima.|con vistas a|-|De cara a las elecciones, se organizaron debates.|lenguaje
de buenas a primeras|de bue-nas a pri-me-ras|locución adverbial|De pronto, sin aviso ni explicación.|de repente|gradualmente|De buenas a primeras decidió mudarse.|lenguaje
de sopetón|de so-pe-tón|locución adverbial|De manera brusca e inesperada.|de improviso|-|La noticia llegó de sopetón.|lenguaje
de súbito|de sú-bi-to|locución adverbial|De pronto.|repentinamente|lentamente|La luz se apagó de súbito.|lenguaje
de raíz|de ra-íz|locución adverbial|Por completo, desde el origen.|de lleno|-|Hay que arrancar el problema de raíz.|lenguaje
de lleno|de lle-no|locución adverbial|Por completo, con total dedicación.|totalmente|parcialmente|Se dedicó de lleno a estudiar.|lenguaje
de oficio|de o-fi-cio|locución adverbial|Por obligación del cargo o sin necesidad de petición.|-|-|El tribunal actuó de oficio al conocer los hechos.|derecho
de memoria|de me-mo-ria|locución adverbial|Sin ayuda de notas, tomando de lo que se recuerda.|-|-|Recitó el poema de memoria.|lenguaje
de paso|de pa-so|locución adverbial|Aprovechando la ocasión; sin detenerse.|-|-|Voy al correo y, de paso, compro pan.|lenguaje
de ahí que|de a-hí que|locución conjuntiva|Por esa razón, y por eso.|por eso|-|Llovió mucho, de ahí que se suspendiera el acto.|lenguaje
toda vez que|to-da vez que|locución conjuntiva|Puesto que, dado que.|puesto que|-|No se aprobó, toda vez que faltaban firmas.|lenguaje
a no ser que|a no ser que|locución conjuntiva|Excepto en el caso de que.|salvo que|-|Iremos a la plaza, a no ser que llueva.|lenguaje
entre tanto|en-tre tan-to|locución adverbial|Mientras algo ocurre.|mientras tanto|-|Entre tanto, el resto del equipo preparaba la sala.|lenguaje
hasta tanto|has-ta tan-to|locución conjuntiva|Hasta el momento en que algo ocurra.|hasta que|-|Permanecerá cerrado hasta tanto se repare el techo.|lenguaje
al cabo de|al ca-bo de|locución preposicional|Después de un tiempo determinado.|tras|-|Al cabo de una hora, terminaron.|lenguaje
ante todo|an-te to-do|locución adverbial|Primero y principalmente.|primero|-|Ante todo, hay que mantener la calma.|lenguaje
de cualquier forma|de cual-quier for-ma|locución adverbial|De todos modos, sin importar las circunstancias.|de todos modos|-|De cualquier forma, avísame si cambias de opinión.|lenguaje
abarrotado|a-ba-rro-ta-do|adjetivo|Lleno hasta el límite, sin espacio libre.|repleto|vacío|El metro iba abarrotado a la hora de salida.|lenguaje
acopio|a-co-pio|sustantivo masculino|Reunión de una gran cantidad de algo para usarlo después.|reserva|-|Hicieron acopio de agua antes del corte.|lenguaje
acreedor|a-cre-e-dor|sustantivo masculino|Persona a quien se le debe algo, generalmente dinero.|-|deudor|El acreedor aceptó esperar un mes más.|economía
adhesión|ad-he-sión|sustantivo femenino|Apoyo a una idea o a una causa; unión de una cosa con otra.|apoyo|rechazo|La campaña recibió la adhesión de varias organizaciones.|lenguaje
adquisición|ad-qui-si-ción|sustantivo femenino|Acción de conseguir algo, por compra o aprendizaje.|compra|venta|La adquisición del lenguaje comienza en los primeros años.|lenguaje
afinidad|a-fi-ni-dad|sustantivo femenino|Parecido o buena relación entre personas o cosas.|semejanza|diferencia|Se hicieron amigos por su afinidad de gustos.|lenguaje
agravante|a-gra-van-te|sustantivo masculino|Circunstancia que hace más grave una falta o un delito.|-|atenuante|La reincidencia es un agravante de la pena.|derecho
agrupación|a-gru-pa-ción|sustantivo femenino|Conjunto de personas organizadas para un fin común.|asociación|-|La agrupación de vecinos limpió el río.|ciudadanía
ahínco|a-hín-co|sustantivo masculino|Esfuerzo y empeño con que se hace algo.|empeño|desgano|Trabajó con ahínco para terminar el proyecto.|carácter
alfabetización|al-fa-be-ti-za-ción|sustantivo femenino|Proceso de enseñar a leer y a escribir.|-|-|Los programas de alfabetización ayudaron a los adultos.|educación
alteridad|al-te-ri-dad|sustantivo femenino|Condición de ser otro; reconocimiento de la diferencia del otro.|-|identidad|La alteridad nos enseña a respetar a quien es distinto.|filosofía
amalgama|a-mal-ga-ma|sustantivo femenino|Mezcla de cosas distintas.|mezcla|-|La ciudad es una amalgama de culturas.|lenguaje
ambivalencia|am-bi-va-len-cia|sustantivo femenino|Presencia de dos sentimientos o sentidos opuestos a la vez.|ambigüedad|-|Sintió ambivalencia ante la mudanza: alegría y miedo.|lenguaje
amenidad|a-me-ni-dad|sustantivo femenino|Cualidad de lo que resulta agradable y entretenido.|entretención|aburrimiento|La amenidad del relato mantuvo a todos atentos.|lenguaje
anclaje|an-cla-je|sustantivo masculino|Acción de sujetar algo firmemente; punto de apoyo.|sujeción|-|El anclaje del puente está en la roca.|lenguaje
anecdotario|a-nec-do-ta-rio|sustantivo masculino|Colección de anécdotas.|-|-|Su abuelo tiene un anecdotario enorme.|lenguaje
anomalía|a-no-ma-lí-a|sustantivo femenino|Situación que se aparta de lo normal.|irregularidad|normalidad|El examen detectó una anomalía en los datos.|ciencia
antojo|an-to-jo|sustantivo masculino|Deseo caprichoso de algo.|capricho|-|A las once de la noche le dio el antojo de comer helado.|lenguaje
apostilla|a-pos-ti-lla|sustantivo femenino|Nota breve que aclara o comenta un texto.|nota|-|Agregó una apostilla al margen del informe.|escritura
aprendizaje|a-pren-di-za-je|sustantivo masculino|Proceso por el que se adquieren conocimientos o habilidades.|-|-|El aprendizaje de un idioma requiere práctica diaria.|educación
arbitrariedad|ar-bi-tra-rie-dad|sustantivo femenino|Acto injusto que depende solo de la voluntad de quien lo hace.|abuso|justicia|Denunciaron la arbitrariedad de esa decisión.|derecho
arraigo|a-rrai-go|sustantivo masculino|Vínculo firme que une a una persona con un lugar o una costumbre.|apego|desarraigo|La familia tiene mucho arraigo en el pueblo.|sociedad
arrebato|a-rre-ba-to|sustantivo masculino|Reacción repentina y violenta de una emoción.|arranque|calma|Tuvo un arrebato de ira y rompió el vaso.|carácter
artificio|ar-ti-fi-cio|sustantivo masculino|Habilidad para hacer algo; también, engaño o falta de naturalidad.|ardid|naturalidad|Su sonrisa tenía algo de artificio.|lenguaje
ascenso|as-cen-so|sustantivo masculino|Subida a un lugar más alto o a un puesto superior.|subida|descenso|Celebró su ascenso a jefa de sección.|lenguaje
aseveración|a-se-ve-ra-ción|sustantivo femenino|Afirmación hecha con seguridad.|afirmación|negación|Su aseveración se basó en datos sólidos.|lenguaje
aval|a-val|sustantivo masculino|Garantía que da una persona o institución a favor de otra.|garantía|-|La universidad dio su aval al proyecto.|economía
azote|a-zo-te|sustantivo masculino|Golpe repetido y fuerte del viento o del agua; también, desgracia que afecta a muchos.|flagelo|-|La sequía fue un azote para los campos.|lenguaje
baremo|ba-re-mo|sustantivo masculino|Tabla de puntajes para evaluar o clasificar.|escala|-|El baremo del concurso asigna puntos por experiencia.|lenguaje
barrera|ba-rre-ra|sustantivo femenino|Obstáculo que impide pasar o avanzar.|obstáculo|facilidad|La falta de internet es una barrera para estudiar.|lenguaje
beneficiario|be-ne-fi-cia-rio|sustantivo masculino|Persona que recibe un beneficio o ayuda.|-|-|Los beneficiarios del programa recibirán un aporte mensual.|ciudadanía
bifurcación|bi-fur-ca-ción|sustantivo femenino|Lugar donde algo se divide en dos ramas.|división|unión|Al llegar a la bifurcación, tomamos el camino de la derecha.|lenguaje
bosquejo|bos-que-jo|sustantivo masculino|Dibujo o plan inicial, sin detalles.|boceto|-|Hizo un bosquejo de su ensayo antes de redactarlo.|escritura
burocracia|bu-ro-cra-cia|sustantivo femenino|Conjunto de trámites y de funcionarios de la administración; también, exceso de papeleo.|-|-|La burocracia retrasó la entrega del permiso.|ciudadanía
cabecera|ca-be-ce-ra|sustantivo femenino|Parte principal o inicial de algo, como la de una cama o una mesa.|-|pie|Dejó el libro en la cabecera de la cama.|lenguaje
candidatura|can-di-da-tu-ra|sustantivo femenino|Propuesta de una persona para ocupar un cargo en una elección.|-|-|Presentó su candidatura a presidente del centro de estudiantes.|ciudadanía
capacitación|ca-pa-ci-ta-ción|sustantivo femenino|Proceso para que alguien adquiera las habilidades necesarias para un trabajo.|formación|-|La empresa ofreció una capacitación en primeros auxilios.|trabajo
carisma|ca-ris-ma|sustantivo masculino|Don de atraer y convencer a los demás.|magnetismo|-|El líder tenía un carisma que entusiasmaba a su equipo.|carácter
casuística|ca-suís-ti-ca|sustantivo femenino|Conjunto de casos particulares que se estudian para sacar conclusiones.|-|-|La casuística del hospital mostró patrones comunes.|lenguaje
causalidad|cau-sa-li-dad|sustantivo femenino|Relación entre una causa y su efecto.|-|-|Hay que probar la causalidad, no solo la coincidencia.|ciencia
certificación|cer-ti-fi-ca-ción|sustantivo femenino|Documento o acción que da fe de que algo es cierto o cumple una norma.|-|-|La certificación garantiza que el producto es seguro.|lenguaje
circunstancia|cir-cuns-tan-cia|sustantivo femenino|Condición o hecho que rodea una situación.|-|-|Dadas las circunstancias, se suspendió el acto.|lenguaje
clausura|clau-su-ra|sustantivo femenino|Acto de cerrar o terminar algo de manera formal.|cierre|inauguración|La clausura del año escolar fue en el gimnasio.|lenguaje
colaboración|co-la-bo-ra-ción|sustantivo femenino|Trabajo conjunto para lograr un fin.|cooperación|-|Con la colaboración de todos, terminamos antes.|lenguaje
colectivo|co-lec-ti-vo|sustantivo masculino|Grupo de personas que actúan juntas por un interés común.|grupo|-|Un colectivo de artistas pintó el mural.|sociedad
colindante|co-lin-dan-te|adjetivo|Que está pegado o junto a otro terreno o lugar.|vecino|apartado|Compró el terreno colindante con el río.|lenguaje
compendio|com-pen-dio|sustantivo masculino|Resumen breve de una obra o de una materia.|resumen|-|Estudió con un compendio de historia.|lenguaje
complejidad|com-ple-ji-dad|sustantivo femenino|Cualidad de lo que tiene muchas partes y es difícil de entender.|dificultad|sencillez|La complejidad del problema exigió un trabajo en equipo.|lenguaje
comportamiento|com-por-ta-mien-to|sustantivo masculino|Forma en que alguien actúa.|conducta|-|El comportamiento del grupo mejoró con las nuevas reglas.|lenguaje
comprobante|com-pro-ban-te|sustantivo masculino|Documento que demuestra que se hizo una gestión o un pago.|recibo|-|Guarda el comprobante de la transferencia.|economía
concatenación|con-ca-te-na-ción|sustantivo femenino|Unión de hechos o ideas encadenados entre sí.|encadenamiento|-|La concatenación de errores provocó el accidente.|lenguaje
condicionante|con-di-cio-nan-te|sustantivo masculino|Factor que determina o limita el desarrollo de algo.|factor|-|El clima es un condicionante del cultivo.|lenguaje
conducta|con-duc-ta|sustantivo femenino|Manera en que una persona se comporta.|comportamiento|-|La conducta de los alumnos fue ejemplar.|lenguaje
confidencialidad|con-fi-den-cia-li-dad|sustantivo femenino|Carácter de lo que se debe mantener en reserva.|reserva|-|El médico respeta la confidencialidad de sus pacientes.|derecho
contención|con-ten-ción|sustantivo femenino|Acción de frenar o de sujetar algo; apoyo emocional que se da a alguien.|freno|-|Los muros de contención evitaron el derrumbe.|lenguaje
convocatoria|con-vo-ca-to-ria|sustantivo femenino|Llamado que se hace para que la gente participe o asista.|llamado|-|La convocatoria a la marcha tuvo gran respuesta.|ciudadanía
credencial|cre-den-cial|sustantivo femenino|Documento que acredita la identidad o el cargo de alguien.|-|-|Mostró su credencial para entrar a la biblioteca.|lenguaje
cuantificación|cuan-ti-fi-ca-ción|sustantivo femenino|Expresión en números de algo que se mide.|-|-|La cuantificación de los resultados facilitó compararlos.|ciencia
currículo|cu-rrí-cu-lo|sustantivo masculino|Conjunto de estudios y contenidos de un plan educativo; resumen de la vida profesional de alguien.|-|-|El currículo escolar incluye lenguaje y matemática.|educación
decálogo|de-cá-lo-go|sustantivo masculino|Conjunto de diez normas o consejos.|-|-|El club redactó un decálogo de buenas prácticas.|lenguaje
deferencia|de-fe-ren-cia|sustantivo femenino|Muestra de respeto y consideración hacia alguien.|cortesía|desdén|Lo trató con deferencia por su edad.|carácter
delegación|de-le-ga-ción|sustantivo femenino|Entrega de una función o poder a otra persona; también, grupo que representa a otros.|-|-|Una delegación del curso fue a hablar con el director.|ciudadanía
delimitación|de-li-mi-ta-ción|sustantivo femenino|Fijación de los límites de algo.|-|-|La delimitación del tema es el primer paso de un ensayo.|lenguaje
desfase|des-fa-se|sustantivo masculino|Falta de ajuste o de coincidencia entre dos cosas.|desajuste|-|Hay un desfase entre lo que se enseña y lo que el mercado pide.|lenguaje
desgaste|des-gas-te|sustantivo masculino|Pérdida gradual de fuerza o de calidad por el uso.|deterioro|-|El desgaste de los neumáticos exige cambiarlos.|lenguaje
deslinde|des-lin-de|sustantivo masculino|Acción de señalar los límites de un terreno; separación clara entre dos cosas.|límite|-|El deslinde del predio se hizo con estacas.|lenguaje
desvío|des-ví-o|sustantivo masculino|Cambio de dirección; camino alternativo.|rodeo|-|Un desvío nos hizo llegar tarde.|lenguaje
dicotomía|di-co-to-mí-a|sustantivo femenino|División de algo en dos partes opuestas.|oposición|-|Planteó una dicotomía entre razón y emoción.|filosofía
diplomacia|di-plo-ma-cia|sustantivo femenino|Arte de tratar los asuntos entre países; habilidad para tratar a los demás con tacto.|tacto|-|Resolvió el conflicto con diplomacia.|ciudadanía
discrepancia|dis-cre-pan-cia|sustantivo femenino|Diferencia de opinión o de resultado entre dos partes.|desacuerdo|acuerdo|Hubo una discrepancia entre ambos informes.|argumentación
disponibilidad|dis-po-ni-bi-li-dad|sustantivo femenino|Condición de estar libre o listo para ser usado.|-|-|Consulta la disponibilidad de horarios en la web.|lenguaje
disposición|dis-po-si-ción|sustantivo femenino|Manera en que algo está colocado; ánimo para hacer algo; norma que se debe cumplir.|actitud|-|Tuvo la mejor disposición para ayudar.|lenguaje
distribución|dis-tri-bu-ción|sustantivo femenino|Reparto de algo entre varios lugares o personas.|reparto|-|La distribución de alimentos llegó a todas las comunas.|lenguaje
divulgación|di-vul-ga-ción|sustantivo femenino|Difusión de un conocimiento para que llegue al público.|difusión|ocultamiento|Escribe artículos de divulgación científica.|lenguaje
documentación|do-cu-men-ta-ción|sustantivo femenino|Conjunto de papeles que prueban o explican algo.|-|-|Revisó la documentación antes de enviar el trámite.|lenguaje
domicilio|do-mi-ci-lio|sustantivo masculino|Lugar donde alguien vive de manera permanente.|residencia|-|Indicó su domicilio en el formulario.|lenguaje
efectividad|e-fec-ti-vi-dad|sustantivo femenino|Capacidad de lograr el efecto buscado.|eficacia|ineficacia|Se comprobó la efectividad de la vacuna.|lenguaje
empadronamiento|em-pa-dro-na-mien-to|sustantivo masculino|Inscripción de una persona en el padrón de una localidad.|inscripción|-|El empadronamiento permite votar en las elecciones.|ciudadanía
emulación|e-mu-la-ción|sustantivo femenino|Intento de imitar y superar a alguien admirado.|imitación|-|Su emulación de los grandes deportistas la hizo mejorar.|lenguaje
equivalencia|e-qui-va-len-cia|sustantivo femenino|Igualdad de valor entre dos cosas.|igualdad|diferencia|Hay una equivalencia entre un kilo y mil gramos.|matemática
estancamiento|es-tan-ca-mien-to|sustantivo masculino|Detención del avance de algo.|parálisis|progreso|Hubo un estancamiento en las negociaciones.|lenguaje
exhortación|ex-hor-ta-ción|sustantivo femenino|Llamado con razones para que alguien actúe de cierta manera.|llamado|-|Su exhortación a ayudar movió a muchos vecinos.|lenguaje
expediente|ex-pe-dien-te|sustantivo masculino|Conjunto de documentos sobre un asunto o una persona.|dossier|-|El expediente del alumno incluye sus notas y su asistencia.|derecho
extensión|ex-ten-sión|sustantivo femenino|Tamaño o alcance de algo; ampliación de un plazo.|alcance|-|La extensión del ensayo no debe pasar de tres páginas.|lenguaje
facilitador|fa-ci-li-ta-dor|sustantivo masculino|Persona que ayuda a que un grupo trabaje o dialogue mejor.|guía|-|El facilitador organizó los turnos de palabra.|educación
fiabilidad|fia-bi-li-dad|sustantivo femenino|Seguridad de que algo funciona o dice la verdad.|confiabilidad|-|Se evaluó la fiabilidad de la fuente.|lenguaje
fiscalización|fis-ca-li-za-ción|sustantivo femenino|Control que se hace para verificar que se cumplan las normas.|control|-|La fiscalización reveló irregularidades en el local.|derecho
fluctuación|fluc-tua-ción|sustantivo femenino|Variación en subida y bajada de algo.|oscilación|estabilidad|Hubo una fluctuación en el precio del dólar.|economía
foco|fo-co|sustantivo masculino|Punto central de algo; lámpara que ilumina.|centro|-|El foco del debate fue el uso del agua.|lenguaje
fortalecimiento|for-ta-le-ci-mien-to|sustantivo masculino|Acción de hacer más fuerte algo.|refuerzo|debilitamiento|El fortalecimiento de la democracia exige participación.|lenguaje
fragmentación|frag-men-ta-ción|sustantivo femenino|División de algo en partes.|división|unión|La fragmentación del bosque amenaza a los animales.|lenguaje
gestión|ges-tión|sustantivo femenino|Conjunto de acciones para administrar o resolver algo.|administración|-|La gestión del colegio mejoró con el nuevo equipo.|lenguaje
gradación|gra-da-ción|sustantivo femenino|Serie de pasos o grados ordenados.|escala|-|Una gradación de colores va del claro al oscuro.|lenguaje
heterogeneidad|he-te-ro-ge-nei-dad|sustantivo femenino|Cualidad de lo que está formado por elementos distintos.|diversidad|homogeneidad|La heterogeneidad del curso enriqueció el debate.|lenguaje
homogeneidad|ho-mo-ge-nei-dad|sustantivo femenino|Cualidad de lo que está formado por elementos semejantes.|uniformidad|heterogeneidad|Se buscó la homogeneidad de la mezcla.|lenguaje
implementación|im-ple-men-ta-ción|sustantivo femenino|Puesta en práctica de un plan o de un sistema.|aplicación|-|La implementación del reciclaje fue gradual.|lenguaje
incidencia|in-ci-den-cia|sustantivo femenino|Efecto o influencia de algo sobre otra cosa; frecuencia de un hecho.|influencia|-|La incidencia del tabaco en el cáncer está comprobada.|lenguaje
incentivo|in-cen-ti-vo|sustantivo masculino|Estímulo que impulsa a hacer algo.|estímulo|freno|El premio fue un incentivo para estudiar.|lenguaje
infraestructura|in-fra-es-truc-tu-ra|sustantivo femenino|Conjunto de obras y servicios necesarios para el funcionamiento de algo, como caminos y redes.|-|-|La región necesita mejor infraestructura vial.|ciudad
insumo|in-su-mo|sustantivo masculino|Material necesario para producir algo.|-|-|El costo de los insumos subió este mes.|economía
integridad|in-te-gri-dad|sustantivo femenino|Cualidad de lo completo; también, honradez.|honradez|corrupción|Se le reconoce por su integridad.|valores
intercambio|in-ter-cam-bio|sustantivo masculino|Cambio recíproco de una cosa por otra.|trueque|-|Hubo un intercambio de ideas muy provechoso.|lenguaje
interlocutor|in-ter-lo-cu-tor|sustantivo masculino|Persona con quien se habla en una conversación.|-|-|Escuchó atentamente a su interlocutor.|lenguaje
invariante|in-va-rian-te|sustantivo femenino|Elemento que no cambia al transformar algo.|-|-|La longitud es una invariante en el giro de la figura.|matemática
irrupción|i-rrup-ción|sustantivo femenino|Entrada repentina y violenta en un lugar; aparición brusca de algo nuevo.|invasión|-|La irrupción de internet cambió la comunicación.|lenguaje
justificación|jus-ti-fi-ca-ción|sustantivo femenino|Razón con que se explica o se defiende algo.|explicación|-|No aceptó la justificación del atraso.|lenguaje
lineamiento|li-ne-a-mien-to|sustantivo masculino|Directriz que orienta cómo actuar.|directriz|-|Seguimos los lineamientos del manual.|lenguaje
logística|lo-gís-ti-ca|sustantivo femenino|Organización de personas, materiales y transporte para realizar una actividad.|-|-|La logística del evento incluyó el transporte y la comida.|trabajo
lógica|ló-gi-ca|sustantivo femenino|Ciencia del razonamiento correcto; modo coherente de pensar.|razonamiento|absurdo|Su respuesta no tiene lógica.|lenguaje
modalidad|mo-da-li-dad|sustantivo femenino|Forma particular de hacer o de presentar algo.|forma|-|Eligió la modalidad de estudio a distancia.|lenguaje
monitoreo|mo-ni-to-re-o|sustantivo masculino|Seguimiento continuo de un proceso para controlarlo.|seguimiento|-|El monitoreo del río detectó la contaminación.|ciencia
motivación|mo-ti-va-ción|sustantivo femenino|Razón o ánimo que impulsa a actuar.|ánimo|desgano|La motivación del equipo creció tras el triunfo.|carácter
optimización|op-ti-mi-za-ción|sustantivo femenino|Mejora de algo para obtener el mejor resultado posible.|mejora|-|La optimización de la ruta ahorró combustible.|lenguaje
pasantía|pa-san-tí-a|sustantivo femenino|Período de práctica que realiza un estudiante en una empresa o institución.|práctica|-|Hizo una pasantía en un laboratorio.|trabajo
permanencia|per-ma-nen-cia|sustantivo femenino|Estado de quien se mantiene en un lugar o situación.|estadía|partida|Su permanencia en el club duró diez años.|lenguaje
planificación|pla-ni-fi-ca-ción|sustantivo femenino|Organización de lo que se va a hacer, con pasos y plazos.|organización|improvisación|Una buena planificación evita problemas de última hora.|lenguaje
pluralidad|plu-ra-li-dad|sustantivo femenino|Existencia de muchos y diversos elementos.|diversidad|uniformidad|La pluralidad de opiniones enriquece la democracia.|ciudadanía
ponderación|pon-de-ra-ción|sustantivo femenino|Evaluación cuidadosa de la importancia de algo; peso asignado a cada elemento.|evaluación|-|La ponderación de las notas dio más peso al examen final.|lenguaje
portafolio|por-ta-fo-lio|sustantivo masculino|Carpeta que reúne trabajos de una persona para mostrarlos.|carpeta|-|Su portafolio de dibujos le abrió las puertas de la escuela de arte.|educación
precedente|pre-ce-den-te|sustantivo masculino|Hecho anterior que sirve de guía o de ejemplo.|antecedente|-|Esta sentencia sienta un precedente.|derecho
predicción|pre-dic-ción|sustantivo femenino|Anuncio de lo que se cree que sucederá.|pronóstico|-|La predicción del tiempo se cumplió.|ciencia
preferencia|pre-fe-ren-cia|sustantivo femenino|Inclinación a elegir algo antes que otra cosa.|predilección|-|Tiene preferencia por los libros de ciencia ficción.|lenguaje
prevalencia|pre-va-len-cia|sustantivo femenino|Predominio de algo sobre otras cosas; proporción de personas con una enfermedad.|predominio|-|La prevalencia de la diabetes ha aumentado.|salud
protagonismo|pro-ta-go-nis-mo|sustantivo masculino|Papel principal que alguien tiene en un asunto.|-|-|Los jóvenes tomaron protagonismo en la campaña.|sociedad
razonamiento|ra-zo-na-mien-to|sustantivo masculino|Serie de ideas con que se llega a una conclusión.|argumento|-|Siguió un razonamiento lógico para resolver el problema.|lenguaje
reciprocidad|re-ci-pro-ci-dad|sustantivo femenino|Correspondencia mutua entre dos personas o partes.|correspondencia|-|La reciprocidad es la base de una buena convivencia.|lenguaje
recopilación|re-co-pi-la-ción|sustantivo femenino|Reunión de textos o datos en un solo lugar.|compilación|-|Hicimos una recopilación de leyendas de la zona.|lenguaje
redacción|re-dac-ción|sustantivo femenino|Acción de escribir un texto; lugar donde se redactan las noticias.|escritura|-|La redacción del informe me tomó una tarde.|escritura
relevancia|re-le-van-cia|sustantivo femenino|Importancia de algo.|importancia|insignificancia|El tema tiene gran relevancia para la comunidad.|lenguaje
replicabilidad|re-pli-ca-bi-li-dad|sustantivo femenino|Posibilidad de repetir un experimento y obtener resultados parecidos.|-|-|La replicabilidad es clave para confiar en un estudio.|ciencia
representatividad|re-pre-sen-ta-ti-vi-dad|sustantivo femenino|Capacidad de una muestra o de una persona de reflejar a un grupo.|-|-|La representatividad de la muestra afecta la validez de la encuesta.|ciencia
significación|sig-ni-fi-ca-ción|sustantivo femenino|Sentido o importancia que se le da a algo.|sentido|-|Cada símbolo tiene una significación especial.|lenguaje
sinergia|si-ner-gia|sustantivo femenino|Efecto que se produce cuando varias partes, al trabajar juntas, logran más que por separado.|-|-|Hubo sinergia entre los dos equipos.|trabajo
sistematización|sis-te-ma-ti-za-ción|sustantivo femenino|Organización de datos o ideas siguiendo un sistema.|-|-|La sistematización de la experiencia ayudó a mejorar el taller.|lenguaje
trazabilidad|tra-za-bi-li-dad|sustantivo femenino|Posibilidad de seguir el recorrido de un producto o un dato desde su origen.|-|-|La trazabilidad de los alimentos permite retirar lotes dañados.|lenguaje
validez|va-li-dez|sustantivo femenino|Cualidad de lo que es válido o legítimo.|legitimidad|invalidez|La validez del documento depende de la firma.|lenguaje
viabilidad|via-bi-li-dad|sustantivo femenino|Posibilidad de que algo se lleve a cabo.|factibilidad|inviabilidad|Se estudió la viabilidad del proyecto.|lenguaje
visión|vi-sión|sustantivo femenino|Capacidad de ver; manera de entender algo; imagen de futuro.|-|-|Tiene una visión clara de lo que quiere lograr.|lenguaje
"""

VERBOS = """
abogar|a-bo-gar|Defender una causa o interceder a favor de alguien.|abogo|aboga|abogó|abogará|defender|atacar|La directora aboga por una educación más inclusiva.
abstraer|abs-tra-er|Separar con la mente una cualidad de un objeto para pensarla por sí sola.|abstraigo|abstrae|abstrajo|abstraerá|separar|concretar|Abstraigo la forma de la figura para ver cómo se calcula su área.
acotar|a-co-tar|Poner límites precisos a un tema o a un terreno.|acoto|acota|acotó|acotará|delimitar|ampliar|Acoto el tema de mi ensayo a la minería del cobre.
acreditar|a-cre-di-tar|Demostrar que algo es cierto o que alguien está autorizado.|acredito|acredita|acreditó|acreditará|certificar|desacreditar|Acredito mi identidad con el carné.
ahondar|a-hon-dar|Profundizar en un asunto o hacer más hondo un hueco.|ahondo|ahonda|ahondó|ahondará|profundizar|superficializar|Ahondo en las causas del problema antes de proponer soluciones.
cercenar|cer-ce-nar|Cortar los extremos de algo; reducir o limitar de modo drástico.|cerceno|cercena|cercenó|cercenará|recortar|ampliar|La censura cercena la libertad de expresión.
coartar|co-ar-tar|Limitar la libertad de alguien para actuar o expresarse.|coarto|coarta|coartó|coartará|restringir|liberar|El miedo coarta su capacidad de hablar en público.
coexistir|co-e-xis-tir|Existir a la vez en un mismo tiempo o lugar.|coexisto|coexiste|coexistió|coexistirá|convivir|-|Distintas culturas coexisten en esta ciudad.
colegir|co-le-gir|Llegar a una conclusión a partir de ciertos indicios.|colijo|colige|coligió|colegirá|deducir|-|Colijo por su gesto que no está de acuerdo.
concienciar|con-cien-ciar|Hacer que alguien sea consciente de un problema o de su importancia.|conciencio|conciencia|concienció|concienciará|sensibilizar|-|Concienciamos a los vecinos sobre el reciclaje.
confrontar|con-fron-tar|Poner frente a frente dos cosas o personas para compararlas o enfrentarlas.|confronto|confronta|confrontó|confrontará|contrastar|-|Confronto las dos versiones del hecho.
conjeturar|con-je-tu-rar|Formar un juicio a partir de indicios incompletos.|conjeturo|conjetura|conjeturó|conjeturará|suponer|comprobar|Conjeturo que llegará tarde por el tráfico.
consensuar|con-sen-suar|Tomar una decisión con el acuerdo de todas las partes.|consensúo|consensúa|consensuó|consensuará|acordar|discrepar|Consensuamos las reglas del curso.
contravenir|con-tra-ve-nir|Actuar en contra de una norma o de una orden.|contravengo|contraviene|contravino|contravendrá|infringir|acatar|Contravenir la ley tiene consecuencias.
corroborar|co-rro-bo-rar|Confirmar algo con nuevos datos o pruebas.|corroboro|corrobora|corroboró|corroborará|confirmar|desmentir|Corroboro la hora antes de salir.
demandar|de-man-dar|Pedir algo con firmeza; presentar una acción ante un tribunal.|demando|demanda|demandó|demandará|exigir|renunciar|Los vecinos demandan una solución al corte de agua.
derogar|de-ro-gar|Dejar sin efecto una ley o una norma.|derogo|deroga|derogó|derogará|anular|promulgar|El Congreso deroga la ley antigua.
desatender|de-sa-ten-der|No prestar atención o cuidado a algo o alguien.|desatiendo|desatiende|desatendió|desatenderá|descuidar|atender|Desatiendo mis estudios cuando duermo poco.
desbordar|des-bor-dar|Salirse de los límites o superar lo previsto.|desbordo|desborda|desbordó|desbordará|rebasar|contener|El río desborda su cauce con las lluvias.
desestimar|de-ses-ti-mar|Rechazar una petición o dar poco valor a algo.|desestimo|desestima|desestimó|desestimará|rechazar|aceptar|El tribunal desestima el recurso.
desvirtuar|des-vir-tuar|Hacer que algo pierda su valor o su sentido original.|desvirtúo|desvirtúa|desvirtuó|desvirtuará|tergiversar|-|Citar la frase sin contexto la desvirtúa.
detentar|de-ten-tar|Poseer un poder o un cargo de forma ilegítima o sin derecho.|detento|detenta|detentó|detentará|ocupar|-|Una élite detenta el poder en ese país.
dilucidar|di-lu-ci-dar|Aclarar un asunto confuso.|dilucido|dilucida|dilucidó|dilucidará|esclarecer|confundir|La investigación dilucida lo ocurrido.
dirimir|di-ri-mir|Resolver una disputa o una duda de manera definitiva.|dirimo|dirime|dirimió|dirimirá|zanjar|-|El árbitro dirime el conflicto entre los equipos.
disentir|di-sen-tir|No estar de acuerdo con una opinión.|disiento|disiente|disintió|disentirá|discrepar|coincidir|Disiento de su propuesta por varias razones.
equiparar|e-qui-pa-rar|Considerar iguales dos cosas o personas.|equiparo|equipara|equiparó|equiparará|igualar|diferenciar|Equiparo el valor de ambas ofertas.
eximir|e-xi-mir|Liberar a alguien de una obligación.|eximo|exime|eximió|eximirá|liberar|obligar|La enfermedad exime al alumno de la prueba de educación física.
garantizar|ga-ran-ti-zar|Asegurar que algo se cumplirá.|garantizo|garantiza|garantizó|garantizará|asegurar|-|Garantizo que el trabajo estará listo a tiempo.
hilvanar|hil-va-nar|Unir ideas con orden; coser con puntadas largas de manera provisional.|hilvano|hilvana|hilvanó|hilvanará|enlazar|-|Hilvano mis ideas antes de exponer.
impugnar|im-pug-nar|Rechazar un acto o un documento por considerarlo ilegal o injusto.|impugno|impugna|impugnó|impugnará|recurrir|aceptar|El candidato impugna el resultado de la mesa.
imputar|im-pu-tar|Atribuir a alguien un hecho, sobre todo un delito.|imputo|imputa|imputó|imputará|atribuir|exculpar|La fiscalía imputa un fraude a la empresa.
incumbir|in-cum-bir|Corresponder a alguien una obligación o tarea.|incumbo|incumbe|incumbió|incumbirá|corresponder|-|La seguridad de los alumnos incumbe a todo el colegio.
intercalar|in-ter-ca-lar|Poner una cosa entre otras.|intercalo|intercala|intercaló|intercalará|insertar|-|Intercalo ejemplos entre las explicaciones.
interpelar|in-ter-pe-lar|Pedir explicaciones a alguien, sobre todo a una autoridad.|interpelo|interpela|interpeló|interpelará|cuestionar|-|El senador interpela al ministro por el gasto.
mermar|mer-mar|Disminuir o hacer menor una cantidad.|mermo|merma|mermó|mermará|disminuir|aumentar|La sequía merma la producción de fruta.
obviar|ob-viar|Evitar o dejar de lado un obstáculo o un detalle.|obvio|obvia|obvió|obviará|eludir|considerar|Obvió los detalles para ir al grano.
pautar|pau-tar|Fijar reglas o un orden para hacer algo.|pauto|pauta|pautó|pautará|establecer|-|El docente pauta los pasos del trabajo.
postular|pos-tu-lar|Proponer una idea o a una persona; presentarse a un cargo o beca.|postulo|postula|postuló|postulará|proponer|-|Postulo a la beca de estudios.
preceder|pre-ce-der|Ir antes de algo en el tiempo o en el espacio.|precedo|precede|precedió|precederá|anteceder|seguir|La lectura precede a la discusión.
prescindir|pres-cin-dir|Pasar sin algo o alguien; renunciar a ello.|prescindo|prescinde|prescindió|prescindirá|renunciar|necesitar|Prescindo del celular durante el estudio.
presumir|pre-su-mir|Suponer algo sin pruebas; también, vanagloriarse.|presumo|presume|presumió|presumirá|suponer|dudar|Presumo que ya llegaron, porque no contestan.
proliferar|pro-li-fe-rar|Multiplicarse rápidamente.|prolifero|prolifera|proliferó|proliferará|multiplicarse|disminuir|Las algas proliferan en aguas con muchos nutrientes.
promulgar|pro-mul-gar|Publicar oficialmente una ley para que entre en vigor.|promulgo|promulga|promulgó|promulgará|decretar|derogar|El presidente promulga la nueva ley.
ratificar|ra-ti-fi-car|Confirmar algo con formalidad.|ratifico|ratifica|ratificó|ratificará|confirmar|-|El Senado ratifica el tratado.
recalcar|re-cal-car|Subrayar algo con énfasis para que se note.|recalco|recalca|recalcó|recalcará|enfatizar|minimizar|Recalco la importancia de cuidar el agua.
redundar|re-dun-dar|Tener como efecto un resultado, bueno o malo.|redundo|redunda|redundó|redundará|resultar|-|Su esfuerzo redunda en beneficio de todos.
rehuir|re-huir|Evitar algo o a alguien por temor o desagrado.|rehúyo|rehúye|rehuyó|rehuirá|esquivar|enfrentar|Rehúyo las discusiones inútiles.
remitir|re-mi-tir|Enviar algo a un lugar; referir a otro texto.|remito|remite|remitió|remitirá|enviar|recibir|Remito el informe a la dirección.
rescindir|res-cin-dir|Dejar sin efecto un contrato.|rescindo|rescinde|rescindió|rescindirá|anular|firmar|La empresa rescinde el contrato de arriendo.
secundar|se-cun-dar|Apoyar a alguien en una iniciativa.|secundo|secunda|secundó|secundará|apoyar|oponerse|El curso secunda la propuesta de reciclar.
sobrevenir|so-bre-ve-nir|Ocurrir algo de manera repentina, después de otra cosa.|sobrevengo|sobreviene|sobrevino|sobrevendrá|suceder|-|Tras el sismo sobrevino una calma inquietante.
subyacer|sub-ya-cer|Estar oculto debajo de algo o detrás de ello.|subyazco|subyace|subyació|subyacerá|esconderse|-|Una crítica social subyace en el cuento.
vacilar|va-ci-lar|Dudar entre varias opciones; moverse de forma insegura.|vacilo|vacila|vaciló|vacilará|dudar|decidir|No vaciló en ayudar a su compañero.
agravar|a-gra-var|Hacer más grave o más intenso algo.|agravo|agrava|agravó|agravará|empeorar|aliviar|La lluvia agrava la situación del campamento.
amortiguar|a-mor-ti-guar|Disminuir la fuerza de un golpe o de un ruido.|amortiguo|amortigua|amortiguó|amortiguará|atenuar|intensificar|La alfombra amortigua los pasos.
aplazar|a-pla-zar|Dejar para más adelante un acto o una tarea.|aplazo|aplaza|aplazó|aplazará|posponer|adelantar|Aplazamos la reunión hasta el viernes.
apuntalar|a-pun-ta-lar|Sostener con puntales una estructura; reforzar una idea o un proyecto.|apuntalo|apuntala|apuntaló|apuntalará|reforzar|debilitar|Los datos apuntalan nuestra hipótesis.
bifurcar|bi-fur-car|Dividir en dos ramas.|bifurco|bifurca|bifurcó|bifurcará|dividir|unir|El camino se bifurca en el cruce.
canalizar|ca-na-li-zar|Dirigir algo por un cauce determinado.|canalizo|canaliza|canalizó|canalizará|encauzar|-|La municipalidad canaliza las quejas de los vecinos.
catalogar|ca-ta-lo-gar|Registrar y ordenar en un catálogo; clasificar.|catalogo|cataloga|catalogó|catalogará|clasificar|-|La bibliotecaria cataloga los libros nuevos.
conmemorar|con-me-mo-rar|Recordar con un acto un hecho importante.|conmemoro|conmemora|conmemoró|conmemorará|rememorar|olvidar|El colegio conmemora su aniversario con un acto.
constituir|cons-ti-tuir|Formar o crear algo; ser parte esencial de algo.|constituyo|constituye|constituyó|constituirá|formar|disolver|Las plazas constituyen espacios de encuentro.
culminar|cul-mi-nar|Llegar al punto más alto o terminar algo.|culmino|culmina|culminó|culminará|concluir|iniciar|Con la ceremonia culmina el año escolar.
diversificar|di-ver-si-fi-car|Hacer variado algo.|diversifico|diversifica|diversificó|diversificará|variar|uniformar|La empresa diversifica su oferta de productos.
elucidar|e-lu-ci-dar|Aclarar un asunto difícil de entender.|elucido|elucida|elucidó|elucidará|esclarecer|confundir|El estudio elucida cómo se forma el arcoíris.
enmarcar|en-mar-car|Poner dentro de un marco; situar algo en un contexto.|enmarco|enmarca|enmarcó|enmarcará|contextualizar|-|El profesor enmarca el tema en la historia del siglo veinte.
escindir|es-cin-dir|Dividir o separar algo en partes.|escindo|escinde|escindió|escindirá|separar|unir|El partido se escinde en dos facciones.
exacerbar|e-xa-cer-bar|Hacer más intenso o más violento un sentimiento o un problema.|exacerbo|exacerba|exacerbó|exacerbará|agravar|calmar|Las críticas exacerban su enojo.
fluctuar|fluc-tuar|Cambiar de manera irregular, subiendo y bajando.|fluctúo|fluctúa|fluctuó|fluctuará|oscilar|estabilizarse|La temperatura fluctúa entre cinco y veinte grados.
gravitar|gra-vi-tar|Girar un cuerpo alrededor de otro por la atracción; pesar sobre algo.|gravito|gravita|gravitó|gravitará|pesar|-|La Luna gravita alrededor de la Tierra.
hallar|ha-llar|Encontrar algo o llegar a una conclusión.|hallo|halla|halló|hallará|encontrar|perder|Hallo la respuesta tras revisar los apuntes.
interferir|in-ter-fe-rir|Obstaculizar o alterar el curso de algo.|interfiero|interfiere|interfirió|interferirá|entorpecer|facilitar|El ruido interfiere con mi concentración.
matizar|ma-ti-zar|Dar a algo un matiz; precisar una afirmación.|matizo|matiza|matizó|matizará|precisar|generalizar|Matizo mi opinión para no ser tan tajante.
modular|mo-du-lar|Variar el tono de la voz; ajustar algo según una medida.|modulo|modula|moduló|modulará|ajustar|-|La cantante modula la voz según la emoción.
obstaculizar|obs-ta-cu-li-zar|Poner trabas a algo.|obstaculizo|obstaculiza|obstaculizó|obstaculizará|dificultar|facilitar|Las obras obstaculizan el tránsito.
ocasionar|o-ca-sio-nar|Ser causa de algo.|ocasiono|ocasiona|ocasionó|ocasionará|provocar|evitar|La lluvia ocasionó inundaciones.
paralizar|pa-ra-li-zar|Detener el movimiento o la actividad de algo.|paralizo|paraliza|paralizó|paralizará|detener|activar|La huelga paraliza el transporte.
perfilar|per-fi-lar|Dar forma definida a algo; destacar el contorno.|perfilo|perfila|perfiló|perfilará|definir|-|Perfilo el tema de mi trabajo con la profesora.
perfeccionar|per-fec-cio-nar|Hacer más perfecto algo.|perfecciono|perfecciona|perfeccionó|perfeccionará|mejorar|empeorar|Perfecciono mi redacción con la práctica.
polarizar|po-la-ri-zar|Concentrar opiniones en dos extremos opuestos.|polarizo|polariza|polarizó|polarizará|dividir|unir|El debate polariza a la audiencia.
potenciar|po-ten-ciar|Dar más fuerza o poder a algo.|potencio|potencia|potenció|potenciará|fortalecer|debilitar|La música potencia mi concentración.
reconfigurar|re-con-fi-gu-rar|Volver a organizar algo con una nueva forma.|reconfiguro|reconfigura|reconfiguró|reconfigurará|reorganizar|-|Reconfiguro el horario de estudio de la semana.
reiterar|rei-te-rar|Repetir algo ya dicho o hecho.|reitero|reitera|reiteró|reiterará|repetir|-|Reitero mi petición de silencio.
replantear|re-plan-te-ar|Volver a plantear un problema o un proyecto con nuevos enfoques.|replanteo|replantea|replanteó|replanteará|reformular|mantener|Replanteo mi estrategia de estudio.
revalorizar|re-va-lo-ri-zar|Dar nuevo valor a algo.|revalorizo|revaloriza|revalorizó|revalorizará|reivindicar|desvalorizar|Revalorizamos los oficios tradicionales.
solventar|sol-ven-tar|Resolver una dificultad; pagar una deuda.|solvento|solventa|solventó|solventará|resolver|-|Solvento un problema técnico con ayuda del profesor.
sustraer|sus-tra-er|Quitar algo con engaño; restar en matemática.|sustraigo|sustrae|sustrajo|sustraerá|restar|sumar|Sustraigo tres de cinco y obtengo dos.
vehicular|ve-hi-cu-lar|Transmitir algo por un medio.|vehiculo|vehicula|vehiculó|vehiculará|canalizar|-|Las redes vehiculan las noticias.
vertebrar|ver-te-brar|Dar estructura interna y firmeza a algo.|vertebro|vertebra|vertebró|vertebrará|estructurar|-|Los valores vertebran su proyecto de vida.
vetar|ve-tar|Rechazar una propuesta usando un derecho de oposición.|veto|veta|vetó|vetará|rechazar|aprobar|El presidente vetó el proyecto de ley.
visibilizar|vi-si-bi-li-zar|Hacer visible un problema para que la sociedad lo vea.|visibilizo|visibiliza|visibilizó|visibilizará|exponer|ocultar|La campaña visibiliza el trabajo de los voluntarios.
zarandear|za-ran-de-ar|Mover con fuerza de un lado a otro.|zarandeo|zarandea|zarandeó|zarandeará|sacudir|-|El viento zarandea los árboles.
acaparar|a-ca-pa-rar|Reunir en exceso algo para tener el control sobre ello.|acaparo|acapara|acaparó|acaparará|monopolizar|repartir|Acaparo la atención de todos cuando cuento mis viajes.
aglutinar|a-glu-ti-nar|Unir cosas o personas en un solo conjunto.|aglutino|aglutina|aglutinó|aglutinará|unir|dispersar|La campaña aglutina a varias organizaciones.
agudizar|a-gu-di-zar|Hacer más agudo o más intenso algo.|agudizo|agudiza|agudizó|agudizará|intensificar|aliviar|La falta de lluvia agudiza la sequía.
aminorar|a-mi-no-rar|Hacer menor la cantidad o la intensidad de algo.|aminoro|aminora|aminoró|aminorará|reducir|aumentar|El conductor aminora la velocidad en la curva.
apaciguar|a-pa-ci-guar|Calmar a alguien o poner fin a una disputa.|apaciguo|apacigua|apaciguó|apaciguará|calmar|exaltar|La profesora apacigua los ánimos del grupo.
atesorar|a-te-so-rar|Guardar con cuidado cosas de valor; reunir riquezas o cualidades.|atesoro|atesora|atesoró|atesorará|guardar|derrochar|Atesoro las cartas de mi abuela.
cohesionar|co-he-sio-nar|Unir firmemente las partes de un conjunto.|cohesiono|cohesiona|cohesionó|cohesionará|unir|desintegrar|La actividad cohesiona al curso.
compilar|com-pi-lar|Reunir en una sola obra textos o datos de diversas fuentes.|compilo|compila|compiló|compilará|recopilar|-|Compilo los cuentos de la región en un solo libro.
conjugar|con-ju-gar|Combinar cosas distintas de manera armoniosa; flexionar un verbo.|conjugo|conjuga|conjugó|conjugará|combinar|separar|El proyecto conjuga ciencia y arte.
crispar|cris-par|Poner tenso o irritado; contraer los músculos de manera brusca.|crispo|crispa|crispó|crispará|irritar|calmar|La discusión crispa a los participantes.
culpabilizar|cul-pa-bi-li-zar|Echar la culpa de algo a alguien.|culpabilizo|culpabiliza|culpabilizó|culpabilizará|inculpar|disculpar|No hay que culpabilizar a la víctima.
dosificar|do-si-fi-car|Repartir en cantidades justas o medidas.|dosifico|dosifica|dosificó|dosificará|administrar|-|Dosifico mis fuerzas para llegar a la meta.
efectuar|e-fec-tuar|Realizar o llevar a cabo una acción.|efectúo|efectúa|efectuó|efectuará|realizar|omitir|Se efectúa el pago en la caja.
empoderar|em-po-de-rar|Dar a alguien más poder y control sobre su propia vida.|empodero|empodera|empoderó|empoderará|fortalecer|subordinar|El taller empodera a las mujeres del barrio.
enaltecer|e-nal-te-cer|Elogiar o dar más valor y prestigio a algo.|enaltezco|enaltece|enalteció|enaltecerá|ensalzar|denigrar|El discurso enaltece su trabajo solidario.
ensalzar|en-sal-zar|Elogiar con entusiasmo.|ensalzo|ensalza|ensalzó|ensalzará|alabar|criticar|La crítica ensalza la novela.
entorpecer|en-tor-pe-cer|Poner trabas o dificultar el desarrollo de algo.|entorpezco|entorpece|entorpeció|entorpecerá|dificultar|facilitar|El ruido entorpece la clase.
escrutar|es-cru-tar|Examinar con mucha atención; contar los votos.|escruto|escruta|escrutó|escrutará|examinar|ignorar|Escruto el cielo en busca de estrellas fugaces.
"""
