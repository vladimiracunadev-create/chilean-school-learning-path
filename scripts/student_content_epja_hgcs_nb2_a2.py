"""Historia, Geografía y Ciencias Sociales EPJA Básica N2, módulo 1 (parte 2): OAD-02, secuencias cronológicas y líneas de tiempo que relacionan hechos conocidos o de una vida de ejemplo con periodos de Chile y de la humanidad. Fechas solo de hitos muy conocidos; el resto es «de ejemplo»."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, regla, goma y cuaderno. Las líneas de tiempo se describen con palabras y tablas dentro de cada ejercicio; si quieres dibujarlas, usa una hoja y una regla. "
             "Las fechas de hitos de Chile y del mundo son las más conocidas; los límites de los periodos son aproximados y los historiadores los discuten. Las vidas y los barrios de los ejemplos son inventados. "
             "No necesitas contar datos de tu propia vida: trabajamos con casos del cuaderno. Si algo cuesta leer, pide apoyo.")
build = make_build(MATERIALS)

O = "EPJA-HGCS-NB2-OAD-02"

# ======================================================= clase 1
F1 = ("Ficha 1 (de ejemplo). Pasos desordenados para sacar un certificado en una oficina pública de ejemplo: "
      "A) Recibe el certificado impreso. B) Toma un número en la entrada. C) Llega a la oficina. D) Pide el certificado en el mesón. E) Espera a que llamen su número. "
      "Sucesos de un barrio ficticio: 1998 se abre la escuela; 2004 llega la locomoción colectiva; 2011 se pavimenta el pasaje; 2018 se instala una plaza.")
build(
    O, 1, F1,
    use="Hoy ordeno sucesos de la vida diaria y del pasado por orden de tiempo: qué ocurrió antes y qué ocurrió después.",
    prior=["Sé qué es «antes» y «después».", "Leo fechas y años.", "Resto números sencillos."],
    explain=[
        "Ordenar en el tiempo es algo que haces a diario: primero llegas a la oficina, luego sacas un número, esperas y recién después te atienden. Si cambias el orden, la historia no se entiende. Lo mismo pasa con los hechos del pasado.",
        "Una secuencia cronológica es una lista de hechos ordenados según el momento en que ocurrieron, desde el más antiguo hasta el más reciente. Se ordena por la fecha, no por la importancia que nosotros le demos ni por lo que nos gusta más.",
        "Para ordenar bien, busca la fecha de cada hecho. Si no hay fecha, busca pistas como «antes de», «después de» o «al año siguiente». Y revisa al final: ¿cada hecho está después del anterior?",
    ],
    vocab=[("secuencia cronológica", "hechos ordenados según cuándo ocurrieron"), ("antes", "en un momento anterior"), ("después", "en un momento posterior"), ("fecha", "día, mes o año en que ocurrió algo"), ("orden", "forma en que se colocan las cosas una tras otra")],
    worked=[
        ("Ordenar un trámite", "{F} Ordena los pasos A) a E) del certificado.", ["Lo primero es llegar a la oficina (C).", "Luego se toma un número (B), se espera (E), se pide en el mesón (D) y se recibe (A)."], "C, B, E, D, A"),
        ("Ordenar años", "{F} ¿Qué hecho ocurrió entre la locomoción y la plaza?", ["Busco 2004 y 2018.", "El año que queda entre ellos es 2011."], "Se pavimentó el pasaje (2011)"),
    ],
    mistakes=[("Ordenar los hechos por la importancia que me parece.", "Una secuencia cronológica se ordena por cuándo ocurrió cada hecho.", "Ordena por la fecha, del más antiguo al más reciente."),
              ("Confundir «antes» con «más reciente».", "Antes es lo que pasó primero, es decir, más antiguo.", "Comprueba con los años: el número menor es el más antiguo.")],
    T=[
        ("abc", "{F} ¿Qué paso del certificado va primero?", "Llega a la oficina", "Recibe el certificado impreso", "Pide el certificado en el mesón", "Sin llegar a la oficina no se puede hacer nada más; es el primer paso."),
        ("ab", "En HGCS: ¿qué es una secuencia cronológica?", "Hechos ordenados según cuándo ocurrieron", "Hechos ordenados según cuánto nos gustan", "Cronológico significa seguir el orden del tiempo."),
        ("{F} ¿Cuál es el último paso del trámite?", "Recibe el certificado impreso", "Al final de la atención se recibe el certificado."),
        ("abc", "{F} ¿Qué paso va justo después de tomar un número?", "Esperar a que llamen el número", "Recibir el certificado", "Llegar a la oficina", "Con el número en la mano se espera el turno."),
        ("ab", "{F} Pedir el certificado en el mesón, ¿ocurre antes o después de esperar el turno?", "Después", "Antes", "Primero se espera el turno y luego se pasa al mesón."),
        ("{F} ¿Qué hecho del barrio ocurrió primero?", "Se abrió la escuela", "El año 1998 es el menor de la lista, por eso es el más antiguo."),
        ("=", "{F} ¿Cuántos años pasaron entre que llegó la locomoción (2004) y se instaló la plaza (2018)?", "2018-2004", "Se resta el año más antiguo del más reciente.", " años"),
        ("abc", "{F} ¿Qué hecho ocurrió entre 2004 y 2018?", "Se pavimentó el pasaje", "Se abrió la escuela", "Se instaló la plaza", "El 2011 queda entre 2004 y 2018; la escuela es anterior y la plaza es posterior."),
        ("{F} Ordena por letras del más antiguo al más reciente: A) pavimento 2011, B) escuela 1998, C) plaza 2018, D) locomoción 2004. Escribe las letras separadas por comas.", "B, D, A, C", "Los años en orden son 1998, 2004, 2011 y 2018."),
        ("abc", "Una persona ordena los hechos del barrio según cuál le parece «más importante». ¿Por qué eso no es una secuencia cronológica?", "Porque el orden depende del momento en que ocurrieron los hechos", "Porque debe usar números romanos", "Porque no se pueden ordenar hechos", "Lo cronológico se rige por las fechas, no por la valoración personal."),
        ("ab", "Una vecina cuenta: «Primero llegó el agua, luego la luz y por último el pavimento». ¿Qué llegó antes del pavimento?", "El agua y la luz", "Solo el pavimento", "El relato ordena tres hechos con «primero», «luego» y «por último»."),
        ("abc", "{F} Se agrega un hecho sin fecha: «La junta de vecinos se creó antes de la escuela y después de la fundación de la población (1990)». ¿Entre qué años pudo crearse?", "Entre 1990 y 1998", "Entre 1998 y 2004", "Después de 2018", "Debe quedar después de 1990 y antes de 1998, año de la escuela."),
        ("abc", "{F} Un relato dice: «La escuela se abrió antes de que llegara la locomoción». ¿Coincide con las fechas de la ficha?", "Sí, porque 1998 es anterior a 2004", "No, porque 2004 es anterior a 1998", "No se puede saber", "La escuela es de 1998 y la locomoción de 2004, así que el relato coincide."),
    ],
    ctx=("abc", "Una persona prepara un papel con los pasos para renovar un documento de ejemplo: «Pedir hora», «Llevar el documento», «Pagar», «Recibir el comprobante». Si los ordena mal, ¿cuál paso NO puede ir primero?", "Recibir el comprobante", "Pedir hora", "Llevar el documento", "El comprobante se entrega al final, cuando todo lo demás ya se hizo."),
    sc=[("En HGCS: ¿qué significa ordenar cronológicamente?", "Ordenar según el momento en que ocurrió cada hecho", "Se ordena de lo más antiguo a lo más reciente."),
        ("¿Qué año es más antiguo, 1998 o 2004?", "1998", "El número menor corresponde al hecho que ocurrió primero."),
        ("¿Qué palabras me dan pistas de orden cuando no hay fecha?", "Antes de, después de, al año siguiente", "Esas expresiones indican qué fue primero.")],
    op=("Ficha de ejemplo: «Sucesos de la población Las Violetas (ficticia): se abre el consultorio (2003), llega el alumbrado público (1996), se funda la junta de vecinos (1991), se inaugura la cancha (2010)». "
        "Ordénalos del más antiguo al más reciente y escribe cuántos años pasan entre el primero y el último.",
        "1991 junta de vecinos; 1996 alumbrado; 2003 consultorio; 2010 cancha. Entre 1991 y 2010 pasan 19 años.",
        ["ordena por año de menor a mayor", "no omite ningún hecho", "calcula bien los años"],
        ["lista ordenada de cuatro hechos y un cálculo"], ["ordenar por importancia", "restar al revés"],
        "Pregunta: «¿Este hecho ocurrió antes o después del anterior?»."),
    reinforce="Escribe tres cosas que hiciste hoy en orden y marca cuál fue primero.",
    extend="Explica con un ejemplo por qué una secuencia mal ordenada cambia la explicación de un hecho.",
)

# ======================================================= clase 2
F2 = ("Ficha 2 (hitos conocidos de la historia). 1492: una expedición europea llega a América. 1541: se funda la ciudad de Santiago. "
      "1810: se forma en Chile la Primera Junta Nacional de Gobierno. 1818: se proclama la independencia de Chile. "
      "1990: comienzan los gobiernos democráticos tras el retorno a la democracia.")
build(
    O, 2, F2,
    use="Hoy aprendo palabras para hablar del tiempo: año, década, siglo, periodo e hito, y las uso con fechas conocidas.",
    prior=["Sé ordenar hechos de antes a después.", "Leo años de cuatro cifras.", "Resto años."],
    explain=[
        "Para hablar del tiempo en la historia usamos unidades. Un año tiene doce meses. Una década son diez años, como los años 1810 a 1819. Un siglo son cien años. Los siglos se escriben con números romanos. En ellos I vale 1, V vale 5 y X vale 10; se suman (XVI = 10 + 5 + 1 = 16) y una letra menor antes de una mayor se resta (IX = 9, XIX = 19).",
        "El siglo I va del año 1 al 100; el siglo II, del 101 al 200, y así sigue. Por eso el año 1818 está en el siglo XIX, que va de 1801 a 1900. Un truco: toma las dos primeras cifras (18), suma uno (19) y escríbelo en romano (XIX), salvo que el año termine en 00.",
        "Un hito es un hecho importante que marca un cambio, como la proclamación de la independencia. Un periodo es una etapa larga con rasgos comunes, que se abre y se cierra con hitos.",
    ],
    vocab=[("década", "diez años seguidos"), ("siglo", "cien años seguidos"), ("hito", "hecho importante que marca un cambio"), ("periodo", "etapa larga con rasgos comunes"), ("número romano", "forma de escribir números con letras, como XIX")],
    worked=[
        ("Hallar el siglo", "{F} ¿En qué siglo está 1541?", ["Tomo 15 y le sumo uno: 16.", "En romano es XVI."], "Siglo XVI (años 1501 a 1600)"),
        ("Hallar la década", "{F} ¿A qué década pertenece 1818?", ["Los años 1810 a 1819 forman la década de 1810.", "1818 está en ese grupo."], "Década de 1810"),
    ],
    mistakes=[("Pensar que el año 1818 es del siglo XVIII porque empieza con 18.", "El siglo XIX comienza en 1801; se suma uno a las dos primeras cifras.", "Usa el truco: 18 + 1 = 19, o sea XIX."),
              ("Creer que una década son cien años.", "Una década son diez; cien años son un siglo.", "Recuerda: década = 10, siglo = 100.")],
    T=[
        ("abc", "¿Cuántos años tiene una década?", "10", "100", "1.000", "La palabra década viene de diez: son diez años."),
        ("ab", "¿Cuántos años tiene un siglo?", "100", "10", "Un siglo reúne cien años, es decir, diez décadas."),
        ("En HGCS: ¿cómo se llama un hecho importante que marca un cambio?", "hito", "Un hito es un hecho que cambia el curso de los procesos."),
        ("abc", "{F} ¿En qué siglo ocurrió 1492?", "XV", "XIV", "XVI", "Con 14 más uno resulta 15, que es XV; el siglo XV va de 1401 a 1500."),
        ("ab", "{F} ¿En qué siglo se fundó Santiago, en 1541?", "XVI", "XV", "Se suma uno a 15 y resulta 16, es decir, XVI."),
        ("{F} ¿En qué década están 1810 y 1818? Escribe «década de ...».", "década de 1810", "Los años 1810 a 1819 forman la década de 1810."),
        ("=", "{F} ¿Cuántos años pasaron entre la fundación de Santiago (1541) y la Primera Junta (1810)?", "1810-1541", "Se resta el año más antiguo del más reciente.", " años"),
        ("=", "{F} ¿Cuántos años separan la Primera Junta (1810) y la proclamación de la independencia (1818)?", "1818-1810", "La diferencia entre dos años se calcula restando.", " años"),
        ("abc", "{F} ¿Cuál de estos hitos ocurrió en el siglo XX?", "El inicio de los gobiernos democráticos en 1990", "La fundación de Santiago", "La Primera Junta", "El año 1990 está entre 1901 y 2000, es decir, siglo XX."),
        ("abc", "¿Por qué 1818 está en el siglo XIX y no en el XVIII?", "Porque el siglo XIX va de 1801 a 1900", "Porque 18 es mayor que 17", "Porque la independencia es del siglo pasado", "Los años 1801 a 1900 forman el siglo XIX."),
        ("ab", "Una persona dice: «El siglo XVI son los años 1600». ¿Qué corrección corresponde?", "El siglo XVI va de 1501 a 1600", "El siglo XVI va de 1601 a 1700", "El año 1600 es el último del siglo XVI, que parte en 1501."),
        ("abc", "Si estamos en el año 2026, ¿en qué siglo estamos?", "XXI", "XX", "XXII", "El siglo XXI comenzó en 2001 y llega hasta 2100."),
        ("abc", "{F} ¿Cuál de estas es un periodo y cuál un hito?", "1818 es un hito y la etapa entre 1541 y 1810 es un periodo", "Los dos son hitos", "1818 es un periodo", "Un hito es un hecho puntual; un periodo es una etapa larga."),
    ],
    ctx=("abc", "Un centro cultural prepara una placa que dice: «Esta biblioteca se abrió en 1925». Un voluntario debe escribir el siglo en números romanos. ¿Qué escribe?", "Siglo XX", "Siglo XIX", "Siglo XXI", "Los años 1901 a 2000 forman el siglo XX, y 1925 está ahí."),
    sc=[("En HGCS: ¿qué es una década?", "Diez años seguidos", "Décadas como la de 1810 agrupan diez años."),
        ("¿Qué es un periodo?", "Una etapa larga con rasgos comunes", "Se delimita por hitos de inicio y de término."),
        ("¿En qué siglo está el año 1541?", "XVI", "Se suma uno a 15 y se escribe en romano.")],
    op=("Ficha de ejemplo: «Hitos de la comunidad Los Pinos (ficticia): 1888 se funda la escuela rural; 1905 llega el telégrafo; 1952 se instala el agua potable; 2003 se abre el centro cultural». "
        "Escribe para cada hito el siglo en número romano y la década. Luego di cuántos años pasaron entre el primer y el último hito.",
        "1888: siglo XIX, década de 1880; 1905: siglo XX, década de 1900; 1952: siglo XX, década de 1950; 2003: siglo XXI, década de 2000. Entre 1888 y 2003 pasaron 115 años.",
        ["escribe bien los siglos romanos", "da la década de cada fecha", "calcula 115 años"],
        ["tabla con cuatro filas y una resta"], ["usar el siglo anterior", "mezclar década con siglo"],
        "Pregunta: «¿Cuál es el siglo de este año: suma uno a sus dos primeras cifras?»."),
    reinforce="Elige tres años que veas en una boleta o un cartel y di su siglo y su década.",
    extend="Explica por qué el año 2000 pertenece al siglo XX y no al XXI.",
)

# ======================================================= clase 3
F3 = ("Ficha 3 (de ejemplo). Se quiere dibujar una línea de tiempo de 10 cm de largo que va de 1400 a 1900, con una marca cada 100 años (1400, 1500, 1600, 1700, 1800, 1900); "
      "cada 100 años miden 2 cm. Hitos a ubicar: 1492, 1541, 1810 y 1818.")
build(
    O, 3, F3,
    use="Hoy sigo pasos para construir una línea de tiempo: elegir la escala, ubicar los hitos y rotularlos.",
    prior=["Sé ordenar hechos por fecha.", "Calculo siglos y décadas.", "Uso regla y multiplicaciones simples."],
    explain=[
        "Una línea de tiempo es un dibujo con una línea donde los hechos se ubican según su fecha. Sirve para ver de un vistazo qué ocurrió antes, qué después y cuánto tiempo pasó entre un hecho y otro.",
        "Se hace en cuatro pasos. Paso 1: anota los hitos con sus fechas. Paso 2: elige dónde empieza y dónde termina la línea. Paso 3: divide la línea en tramos iguales: cada marca debe valer lo mismo, por ejemplo cien años. Paso 4: ubica cada hito en su lugar, escríbele la fecha y ponle un título a la línea.",
        "La escala dice cuánto tiempo representa cada centímetro. Si cada 100 años miden 2 cm, entonces 50 años miden 1 cm. Mantener la escala igual evita que parezca que dos hechos están más cerca o más lejos de lo que realmente están.",
    ],
    vocab=[("línea de tiempo", "dibujo donde los hechos se ubican según su fecha"), ("escala", "cuánto tiempo representa cada trozo de la línea"), ("tramo", "parte de la línea entre dos marcas"), ("rotular", "escribir el nombre y la fecha de cada hito"), ("título", "frase que dice de qué trata la línea")],
    worked=[
        ("Ubicar entre marcas", "{F} ¿Entre qué marcas queda 1541?", ["Busco la marca anterior: 1500.", "Busco la siguiente: 1600."], "Entre 1500 y 1600, más cerca de 1500"),
        ("Medir con la escala", "{F} ¿Cuántos centímetros hay entre la marca 1500 y la 1800?", ["De 1500 a 1800 hay 300 años, que son tres tramos de 100 años.", "Cada tramo mide 2 cm: 3 por 2."], "6 cm"),
    ],
    mistakes=[("Hacer tramos desiguales: una marca cada 100 años y otra cada 50.", "La escala se deforma y los hechos parecen más cerca o lejos.", "Todas las marcas deben valer lo mismo."),
              ("Olvidar el título y las fechas.", "Sin ellos la línea no explica de qué trata.", "Rotula cada hito con su fecha y escribe un título.")],
    T=[
        ("abc", "{F} ¿Cuántos años representa cada marca de la línea?", "100", "50", "10", "La ficha dice que hay una marca cada 100 años."),
        ("ab", "{F} ¿Cuántos centímetros mide la línea completa?", "10", "2", "La ficha indica que la línea completa mide 10 cm."),
        ("En HGCS: ¿cómo se llama lo que dice cuánto tiempo representa cada trozo de la línea?", "escala", "La escala relaciona longitud con tiempo."),
        ("abc", "{F} ¿Entre qué marcas queda 1492?", "Entre 1400 y 1500", "Entre 1500 y 1600", "Entre 1300 y 1400", "1492 es mayor que 1400 y menor que 1500."),
        ("ab", "{F} ¿Entre qué marcas queda 1810?", "Entre 1800 y 1900", "Entre 1700 y 1800", "El año 1810 supera 1800 y no llega a 1900."),
        ("=", "{F} ¿Cuántos centímetros hay entre la marca 1400 y la marca 1700? (cada 100 años miden 2 cm)", "3*2", "Son tres tramos de 100 años y cada uno mide 2 cm.", " cm"),
        ("=", "{F} ¿Cuántos años representan 4 cm de la línea?", "4*50", "Si 2 cm son 100 años, cada cm vale 50 años.", " años"),
        ("abc", "{F} ¿Cuál es el paso 3 del método?", "Dividir la línea en tramos iguales", "Escribir el título", "Elegir el hito más importante", "El tercer paso crea la escala con marcas de igual valor."),
        ("abc", "{F} ¿Cuál de estos hitos queda más cerca de la marca 1500?", "1492", "1541", "1810", "Desde 1500, 1492 está a 8 años y 1541 a 41; 1810 está mucho más lejos."),
        ("abc", "Una línea tiene marcas en 1400, 1500, 1700 y 1800, sin 1600. ¿Qué problema tiene?", "Los tramos no son iguales y la escala se deforma", "Tiene demasiados títulos", "Está bien así", "Falta una marca y el tramo de 1500 a 1700 vale el doble."),
        ("ab", "¿Por qué se pone un título a la línea de tiempo?", "Para indicar de qué trata la secuencia", "Para llenar espacio", "El título orienta a quien la mira sobre el tema."),
        ("abc", "{F} Dos hitos distan 8 años. ¿Cuántos centímetros separan 1810 y 1818 en la línea?", "0,16 cm, es decir, casi juntos", "8 cm", "2 cm", "Como 100 años miden 2 cm, 8 años miden 0,16 cm: casi no se separan."),
        ("abc", "{F} Si agregas el hito 1990, ¿qué conviene hacer?", "Extender la línea hasta 2000 con la misma escala", "Acortar los tramos anteriores", "Ubicarlo sin marca", "Hay que seguir la misma escala para no deformar la línea."),
    ],
    ctx=("abc", "Una organización de adultos mayores arma una línea de tiempo de su sede con estos hitos de ejemplo: 1980, 1995, 2005 y 2020. La línea mide 8 cm y va de 1980 a 2020. ¿Cuántos años representa cada centímetro?", "5 años", "4 años", "10 años", "Son 40 años en 8 cm, es decir, 5 años por centímetro."),
    sc=[("En HGCS: ¿qué es una línea de tiempo?", "Un dibujo donde los hechos se ubican según su fecha", "Permite ver el orden y la distancia entre hechos."),
        ("¿Por qué las marcas deben valer lo mismo?", "Para que la escala no se deforme", "Marcas desiguales hacen que los hechos parezcan más cerca o lejos."),
        ("¿Cuántos cm hay entre 1500 y 1700 si 100 años miden 2 cm?", "4 cm", "Son dos tramos de 2 cm cada uno.")],
    op=("Hitos de ejemplo de una plaza: 1950 se planta el primer árbol, 1975 se instalan los bancos, 2000 se construye la sede y 2025 se renueva el piso. "
        "Describe cómo harías una línea de tiempo de 10 cm de 1950 a 2050 con una marca cada 25 años (cada marca mide 2,5 cm). Indica en qué marca queda cada hito y escribe el título.",
        "Marcas: 1950, 1975, 2000, 2025, 2050. Los cuatro hitos quedan exactamente sobre las cuatro primeras marcas. Título: «Historia de la plaza, 1950-2025».",
        ["divide en tramos iguales de 25 años", "ubica cada hito en su marca", "agrega título y fechas"],
        ["una descripción o dibujo de la línea con rótulos"], ["marcas desiguales", "no escribir el título"],
        "Pregunta: «¿Cada marca representa lo mismo?»."),
    reinforce="Dibuja una línea de tiempo con tres hechos de tu semana y marca en qué día ocurrieron.",
    extend="Explica qué ventaja tiene una línea de tiempo sobre una lista de fechas.",
)

# ======================================================= clase 4
F4 = ("Ficha 4 (periodos aproximados; los historiadores discuten sus límites). Historia de la humanidad: Prehistoria (antes de la escritura); Edad Antigua (desde la escritura hasta el siglo V); "
      "Edad Media (siglos V a XV); Edad Moderna (siglos XV a XVIII); Edad Contemporánea (desde fines del siglo XVIII hasta hoy). "
      "Historia de Chile: Pueblos originarios (los pueblos que habitaban el territorio antes de la llegada de los españoles y que siguen presentes hoy); Conquista (siglo XVI); Colonia (desde fines del siglo XVI hasta 1810); Independencia (desde 1810 hasta 1818 y años siguientes); República (siglo XIX hasta hoy).")
build(
    O, 4, F4,
    use="Hoy practico ubicando hechos en los periodos de la historia de la humanidad y de Chile, con una tabla de apoyo.",
    prior=["Calculo siglos y décadas.", "Sé qué es un hito y un periodo.", "Leo una tabla con periodos."],
    explain=[
        "Los historiadores dividen el pasado en periodos para estudiarlo mejor. En la historia de la humanidad se usa la Prehistoria, la Edad Antigua, la Edad Media, la Edad Moderna y la Edad Contemporánea. En Chile se habla de pueblos originarios, Conquista, Colonia, Independencia y República.",
        "Los periodos no tienen límites exactos: son aproximados y hay debates sobre dónde empiezan o terminan. Cada periodo se reconoce por rasgos comunes, como la forma de vivir, de gobernarse o de producir.",
        "Para ubicar un hecho, mira su fecha y busca el periodo que la contiene. Si el hecho es de un lugar, usa los periodos de ese lugar: un hecho ocurrido en Chile se ubica en los periodos de Chile, y puede relacionarse con los del mundo.",
    ],
    vocab=[("Edad Media", "periodo de la historia europea entre los siglos V y XV, aproximadamente"), ("Colonia", "periodo de Chile bajo el gobierno de la Corona española, hasta 1810"), ("República", "forma de gobierno en que las autoridades son elegidas y no heredan el cargo"), ("Prehistoria", "tiempo anterior a la escritura"), ("Edad Contemporánea", "periodo que llega desde fines del siglo XVIII hasta hoy")],
    worked=[
        ("Ubicar por fecha", "{F} ¿En qué periodo de Chile está el año 1541?", ["Es del siglo XVI.", "Ese siglo corresponde a la Conquista."], "Conquista"),
        ("Dos periodos a la vez", "{F} La Primera Junta de 1810, ¿con qué periodo de Chile se relaciona y con cuál de la humanidad?", ["En Chile, 1810 abre el periodo de la Independencia.", "En el mundo es parte de la Edad Contemporánea."], "Independencia (Chile) y Edad Contemporánea (humanidad)"),
    ],
    mistakes=[("Usar un periodo de Europa para un hecho de Chile sin aclararlo.", "Los periodos locales tienen nombres y límites propios.", "Usa los periodos de Chile y luego relaciónalos con los del mundo."),
              ("Creer que los límites de los periodos son exactos.", "Los historiadores los fijan de forma aproximada.", "Di «aproximadamente» y revisa de qué fuente salen.")],
    T=[
        ("abc", "{F} ¿Cuál es el periodo de Chile del siglo XVI?", "Conquista", "Colonia", "República", "La ficha asigna el siglo XVI a la Conquista."),
        ("ab", "{F} ¿Qué periodo de la humanidad llega desde fines del siglo XVIII hasta hoy?", "Edad Contemporánea", "Edad Media", "La ficha define así la Edad Contemporánea."),
        ("¿Qué periodo de la humanidad corresponde al tiempo anterior a la escritura?", "Prehistoria", "Prehistoria significa antes de la escritura."),
        ("abc", "{F} Una pintura en una cueva hecha antes de que existiera la escritura, ¿en qué periodo se ubica?", "Prehistoria", "Edad Media", "Edad Moderna", "Lo anterior a la escritura se llama Prehistoria."),
        ("ab", "{F} Una catedral construida en el siglo XII en Europa, ¿en qué periodo se ubica?", "Edad Media", "Edad Moderna", "El siglo XII está entre los siglos V y XV."),
        ("{F} El año 1700 en Chile, ¿a qué periodo pertenece?", "Colonia", "Entre fines del siglo XVI y 1810 corresponde a la Colonia."),
        ("=", "{F} ¿Cuántos años pasaron entre la fundación de Santiago (1541) y la proclamación de la independencia (1818)?", "1818-1541", "Se resta el año más antiguo del más reciente.", " años"),
        ("abc", "{F} Una ley de ejemplo dictada en 1850 en Chile, ¿en qué periodo cae según la ficha?", "República", "Conquista", "Prehistoria", "El año 1850 es posterior a la independencia, y la ficha ubica ahí la República."),
        ("abc", "{F} La proclamación de la independencia en 1818, ¿dónde se ubica en la historia de la humanidad?", "En la Edad Contemporánea", "En la Edad Media", "En la Prehistoria", "1818 está después de fines del siglo XVIII."),
        ("abc", "Alguien dice: «El periodo de la Colonia empezó exactamente el 1 de enero de 1600». ¿Qué corrección corresponde?", "Los límites de los periodos son aproximados, no exactos", "Es exacta", "Fue en 1700", "La ficha indica que son aproximados y discutidos."),
        ("ab", "{F} Una persona ubica la Conquista de Chile en la Edad Media. ¿Qué falla?", "Era del siglo XVI y ese siglo no es de la Edad Media", "Nada, es correcto", "La Edad Media termina en el siglo XV, antes de la Conquista de Chile."),
        ("abc", "{F} Un hecho ocurrido en Chile en 1990, ¿cómo se ubica?", "En la República en Chile y en la Edad Contemporánea en el mundo", "En la Colonia", "En la Edad Media", "El año 1990 pertenece a la República chilena y a la Edad Contemporánea."),
        ("abc", "{F} ¿Qué periodo de la humanidad se superpone en el tiempo con la Conquista de Chile (siglo XVI)?", "La Edad Moderna", "La Edad Antigua", "La Prehistoria", "El siglo XVI está dentro de la Edad Moderna, que va de los siglos XV a XVIII."),
    ],
    ctx=("abc", "Un museo comunal quiere ordenar una sala con tres objetos de ejemplo: una herramienta de piedra de antes de la escritura, un documento colonial de 1750 y un afiche de 1990. ¿Cuál es el orden de los periodos de esos tres objetos?", "Prehistoria, Colonia, República", "República, Colonia, Prehistoria", "Colonia, Prehistoria, República", "La herramienta es prehistórica, el documento es de la Colonia y el afiche de la República."),
    sc=[("En HGCS: ¿qué es un periodo?", "Una etapa larga con rasgos comunes", "Se usa para ordenar el pasado en bloques."),
        ("¿Son exactos los límites de los periodos?", "No, son aproximados", "Los historiadores discuten dónde empiezan y terminan los periodos."),
        ("¿Cómo ubico un hecho en un periodo?", "Miro su fecha y busco el periodo que la incluye", "La fecha indica a qué etapa pertenece.")],
    op=("Ficha de ejemplo: «a) año 1550, fundación de una ciudad en Chile; b) año 1700, un comerciante anota sus ventas en un cuaderno; c) año 1850, se abre una escuela en un pueblo; d) un objeto de piedra anterior a la escritura». "
        "Para cada hecho escribe el periodo de Chile (si corresponde) y el periodo de la humanidad.",
        "a) Conquista en Chile; Edad Moderna. b) Colonia; Edad Moderna. c) República; Edad Contemporánea. d) Prehistoria (en Chile, tiempo de los pueblos originarios).",
        ["usa la tabla de la ficha", "distingue periodos de Chile y de la humanidad", "reconoce que los límites son aproximados"],
        ["una tabla de cuatro filas con dos columnas de periodos"], ["usar solo periodos europeos", "decir que los límites son exactos"],
        "Pregunta: «¿Qué periodo contiene esta fecha, en este lugar?»."),
    reinforce="Elige un año de una boleta o un cartel y dile a otra persona en qué periodo de Chile estaba.",
    extend="Explica por qué un hecho puede pertenecer a dos periodos distintos a la vez, uno de Chile y otro del mundo.",
)

# ======================================================= clase 5
F5 = ("Ficha 5 (de ejemplo). Rosa es un personaje inventado; sus fechas son de ejemplo. 1962: nace. 1985: empieza a trabajar en una panadería. 1998: se muda a otra ciudad. 2010: cambia de oficio. "
      "Hitos conocidos: 1969: una misión espacial llega a la Luna. 1990: comienzan los gobiernos democráticos en Chile. 2010: ocurre un gran terremoto en Chile. 2020: comienza la pandemia mundial de COVID-19.")
build(
    O, 5, F5,
    use="Hoy relaciono hechos de una vida de ejemplo con hitos de Chile y del mundo, usando una línea de tiempo en una tabla.",
    prior=["Ordeno hechos por fecha.", "Ubico hechos en periodos.", "Resto años para calcular edades."],
    explain=[
        "La vida de cada persona se mueve dentro de la historia de su país y del mundo. Si relacionas la fecha de un hecho personal con un hito de Chile o del mundo, puedes entender en qué contexto ocurrió y qué edad se tenía.",
        "Para relacionarlos haz una tabla con tres columnas: año, hecho de la vida y hito de Chile o del mundo. Luego resta años para calcular la edad. Por ejemplo, si alguien nació en 1962, en 1990 tenía 28 años (1990 menos 1962).",
        "Esto no significa que un hecho personal haya sido causado por uno histórico. Relacionar es poner uno junto al otro en el tiempo; después se estudia si hubo conexión o no. En esta clase trabajamos con un personaje de ejemplo y no tienes que contar datos propios.",
    ],
    vocab=[("hito personal", "hecho importante en la vida de una persona"), ("hito histórico", "hecho importante para un país o el mundo"), ("contexto", "lo que ocurría alrededor de un hecho en su tiempo y lugar"), ("edad", "años cumplidos desde el nacimiento"), ("relacionar", "poner dos hechos juntos para ver cómo se conectan en el tiempo")],
    worked=[
        ("Calcular la edad", "{F} ¿Qué edad tenía Rosa cuando comenzaron los gobiernos democráticos en 1990?", ["Resto 1990 menos 1962.", "Compruebo: 28 años cumplidos o por cumplir según el mes; usamos el cálculo por años."], "28 años"),
        ("Hecho y hito en el mismo año", "{F} ¿Qué hito de Chile ocurrió el mismo año en que Rosa cambió de oficio?", ["Busco 2010 en los hitos.", "En 2010 hubo un gran terremoto en Chile."], "El terremoto de 2010"),
    ],
    mistakes=[("Creer que si dos hechos ocurren el mismo año, uno causó el otro.", "La coincidencia en el tiempo no prueba una causa.", "Di que ocurrieron en el mismo año y busca fuentes para saber si se conectan."),
              ("Contar mal la edad por usar el año del hecho como edad.", "La edad es la resta entre el año del hecho y el de nacimiento.", "Resta siempre el año de nacimiento.")],
    T=[
        ("abc", "{F} ¿En qué año nació Rosa, según la ficha?", "1962", "1985", "1998", "La ficha lo indica al comienzo de su lista."),
        ("ab", "{F} ¿Qué hito del mundo ocurrió en 1969?", "Una misión espacial llegó a la Luna", "Comenzó una pandemia", "La ficha lo anota como hito de 1969."),
        ("En HGCS: ¿cómo se llama un hecho importante para un país o el mundo?", "hito histórico", "Un hito histórico marca un cambio que afecta a muchas personas."),
        ("=", "{F} ¿Qué edad tenía Rosa en 1985, cuando empezó a trabajar?", "1985-1962", "La edad es la diferencia entre el año del hecho y el de nacimiento.", " años"),
        ("=", "{F} ¿Qué edad tenía Rosa en 2010?", "2010-1962", "Se resta el año de nacimiento del año de 2010.", " años"),
        ("abc", "{F} ¿Qué hito del mundo ocurrió cuando Rosa tenía 7 años?", "Una misión espacial llegó a la Luna", "Comenzó la pandemia", "Comenzaron los gobiernos democráticos en Chile", "Rosa nació en 1962; con 7 años estaba en 1969, año de la misión a la Luna."),
        ("abc", "{F} ¿Cuántos años pasaron desde que Rosa empezó a trabajar (1985) hasta el comienzo de la pandemia (2020)?", "35", "25", "45", "La resta 2020 menos 1985 da 35."),
        ("ab", "{F} ¿Cuál es más antiguo, que Rosa llegara a otra ciudad (1998) o que comenzaran los gobiernos democráticos (1990)?", "Los gobiernos democráticos de 1990", "La mudanza de 1998", "El año 1990 es anterior a 1998."),
        ("=", "{F} ¿Cuántos años tenía Rosa cuando se muda (1998)?", "1998-1962", "Se resta el año de nacimiento del año de la mudanza.", " años"),
        ("abc", "{F} Una persona dice: «Rosa cambió de oficio por el terremoto, porque pasó el mismo año». ¿Qué falla?", "Coincidir en el año no prueba que uno causara el otro", "Nada, está probado", "El terremoto fue en 2020", "Para afirmar una causa se necesita una fuente que lo diga."),
        ("abc", "{F} Si se quiere contar una vida con su contexto, ¿cuál es una tabla útil?", "Año, hecho de la vida y hito de Chile o del mundo", "Solo los hitos del mundo", "Solo los años pares", "La tabla relaciona lo personal con lo histórico."),
        ("abc", "{F} En 1990, ¿qué periodo de Chile y de la humanidad corresponde?", "República y Edad Contemporánea", "Colonia y Edad Media", "Conquista y Edad Moderna", "El año 1990 es del siglo XX, parte de la República y de la Edad Contemporánea."),
        ("ab", "{F} ¿Qué conviene hacer para saber si un hecho de la vida de Rosa se conectó con un hito histórico?", "Buscar fuentes que lo expliquen, como su relato o documentos", "Suponer que sí", "Coincidir en fecha da una pista, pero hay que comprobar con fuentes."),
    ],
    ctx=("abc", "En un taller de memoria barrial se pide a una dirigente ficticia, nacida en 1970 (dato de ejemplo), ubicar su historia en una línea de tiempo. Con el hito de 1990, ¿qué cuenta hace para saber su edad?", "1990 menos 1970", "1970 menos 1990", "1990 más 1970", "La edad es el año del hito menos el año de nacimiento."),
    sc=[("¿Qué significa relacionar un hecho personal con un hito histórico?", "Ponerlos juntos en el tiempo para ver el contexto", "No prueba causa, solo los ubica."),
        ("¿Cómo calculo una edad en un año dado?", "Resto el año de nacimiento del año del hecho", "Esa resta da los años transcurridos."),
        ("En HGCS: ¿qué es el contexto de un hecho?", "Lo que ocurría alrededor en su tiempo y lugar", "Ayuda a entender por qué algo pasó así.")],
    op=("Personaje de ejemplo: Hugo, nacido en 1975. Hechos: 1993 termina sus estudios, 2001 abre un negocio, 2012 se cambia de barrio. Hitos de ejemplo: 1990 gobiernos democráticos en Chile, 2010 terremoto, 2020 pandemia. "
        "Arma una tabla con año, hecho de Hugo, hito y edad de Hugo en cada año. Después escribe una frase: «en el año ... Hugo tenía ... años cuando ...».",
        "1993: 18 años, termina estudios (3 años tras 1990). 2001: 26, abre un negocio. 2012: 37, cambia de barrio (2 años tras el terremoto). Frase: en 2020 Hugo tenía 45 años cuando comenzó la pandemia.",
        ["calcula bien las edades", "relaciona cada hecho con un hito sin afirmar causas", "escribe la frase pedida"],
        ["una tabla y una frase"], ["afirmar que un hito causó un hecho personal", "restar mal"],
        "Pregunta: «¿Esto lo prueba una fuente o solo coincide en el año?»."),
    reinforce="Con el personaje de ejemplo, calcula qué edad tendría en el año actual.",
    extend="Explica qué fuentes podrían mostrar si un hito histórico influyó en una decisión personal.",
)

# ======================================================= clase 6
F6 = ("Ficha 6 (de ejemplo). Una línea de tiempo hecha por un vecino tiene estos rótulos, en este orden de izquierda a derecha: «1818 Proclamación de la independencia», «1810 Primera Junta», «1541 Fundación de Santiago», «1990 Retorno a la democracia». "
      "Las marcas de la línea son: 1500, 1600, 1800 y 2000. No tiene título. La escala no está indicada.")
build(
    O, 6, F6,
    use="Hoy reviso lo logrado: reviso una línea de tiempo con una pauta, corrijo errores y decido qué practicar.",
    prior=["Ordeno hechos por fecha y calculo siglos.", "Conozco la escala de una línea de tiempo.", "Ubico hechos en periodos."],
    explain=[
        "Revisar una línea de tiempo es comprobar cuatro cosas. Primero, el orden: los hechos van de la fecha más antigua a la más reciente, de izquierda a derecha. Segundo, la escala: las marcas valen lo mismo. Tercero, los rótulos: cada hito tiene fecha y nombre. Cuarto, el título: dice de qué trata.",
        "Cuando encuentras un error, no es un fracaso: es parte del trabajo. Se corrige moviendo el hito mal ubicado, ajustando las marcas o agregando lo que falta. También conviene probar con un cálculo: ¿la distancia entre dos hitos coincide con los años que los separan?",
        "Al final, relaciona la línea con los periodos de Chile y de la humanidad. Pregúntate: ¿qué periodos aparecen? ¿Qué hitos abren o cierran cada uno? Esa mirada muestra para qué sirve ordenar el tiempo.",
    ],
    vocab=[("pauta de revisión", "lista de preguntas para comprobar un trabajo"), ("corregir", "cambiar lo que está mal"), ("orden cronológico", "de lo más antiguo a lo más reciente"), ("rótulo", "texto que nombra un hito y su fecha"), ("cierre de un periodo", "hito que marca su término")],
    worked=[
        ("Detectar el error de orden", "{F} ¿Qué hitos están mal ordenados?", ["De izquierda a derecha debería ir 1541, 1810, 1818 y 1990.", "El vecino puso 1818 en primer lugar y 1541 en tercero; 1810 y 1990 ya están en su sitio."], "Hay que intercambiar 1818 y 1541; el orden correcto es 1541, 1810, 1818, 1990"),
        ("Corregir la escala", "{F} Las marcas 1500, 1600, 1800 y 2000 no valen lo mismo. ¿Qué marca falta?", ["Entre 1600 y 1800 falta 1700.", "Entre 1800 y 2000 falta 1900."], "Faltan 1700 y 1900 para que cada tramo valga 100 años"),
    ],
    mistakes=[("Corregir solo la ortografía y no el orden de los hitos.", "Lo más grave es que la secuencia no sea cronológica.", "Revisa primero el orden y la escala; después los rótulos."),
              ("No comprobar con un cálculo.", "Un error de ubicación puede pasar inadvertido sin medir.", "Comprueba que la distancia entre hitos corresponde a los años que los separan.")],
    T=[
        ("abc", "{F} ¿Cuál es el hito más antiguo de la ficha?", "1541 Fundación de Santiago", "1990 Retorno a la democracia", "1818 Proclamación de la independencia", "El año 1541 es el menor de los cuatro."),
        ("ab", "{F} ¿Qué falta en la línea del vecino?", "Un título", "Las fechas", "La ficha dice que no tiene título; las fechas sí están."),
        ("En HGCS: ¿cómo se llama la lista de preguntas para comprobar un trabajo?", "pauta de revisión", "Una pauta ayuda a revisar con criterios."),
        ("abc", "{F} ¿Cuál debería ser el orden de izquierda a derecha?", "1541, 1810, 1818, 1990", "1990, 1818, 1810, 1541", "1818, 1810, 1541, 1990", "La secuencia cronológica va del año menor al mayor."),
        ("ab", "{F} ¿Cuántos años separan 1810 y 1818?", "8", "18", "La resta 1818 menos 1810 es 8."),
        ("=", "{F} ¿Cuántos años pasaron entre la fundación de Santiago (1541) y el retorno a la democracia (1990)?", "1990-1541", "Se resta el año más antiguo del más reciente.", " años"),
        ("abc", "{F} Para que los tramos valgan 100 años, ¿qué marcas faltan entre 1600 y 2000?", "1700 y 1900", "1650 y 1950", "1610 y 1990", "Entre 1600 y 1800 falta 1700 y entre 1800 y 2000 falta 1900."),
        ("ab", "{F} Un hito de 1990, ¿en qué siglo está?", "XX", "XIX", "Los años 1901 a 2000 forman el siglo XX."),
        ("abc", "{F} ¿Qué periodo de Chile cierra con el hito de 1818 o muy cerca de él?", "El proceso de Independencia", "La Conquista", "La Prehistoria", "Los hitos 1810 y 1818 abren y cierran la etapa inicial de la Independencia."),
        ("abc", "El vecino dice: «Mi línea está bien porque me gustó cómo quedó». ¿Qué criterio olvida?", "Revisar el orden, la escala, los rótulos y el título", "El color de la regla", "El número de hitos", "Una línea se evalúa con criterios, no solo por gusto."),
        ("ab", "¿Por qué comprobar con un cálculo la distancia entre dos hitos?", "Porque así se detectan errores de ubicación", "Porque las líneas no tienen escala", "El cálculo confirma que lo dibujado representa los años reales."),
        ("abc", "{F} Una persona agrega el hito 1973 a la línea. ¿Dónde debe ir?", "Entre 1818 y 1990", "Antes de 1541", "Después de 1990", "Los años 1973 quedan entre 1818 y 1990, siguiendo el orden cronológico."),
        ("abc", "{F} Si debes decidir qué practicar, ¿cuál es una buena decisión?", "Repasar el cálculo de siglos si me equivoco con los años", "Dejar de usar fechas", "Memorizar sin entender", "Elegir lo que me cuesta orienta el estudio."),
    ],
    ctx=("abc", "En la sede vecinal alguien arma un mural cronológico con estos hitos de ejemplo: 2005, 1980, 1995, 2018. ¿Cuál es el orden correcto de izquierda a derecha?", "1980, 1995, 2005, 2018", "2018, 2005, 1995, 1980", "1995, 1980, 2005, 2018", "El orden va de lo más antiguo a lo más reciente."),
    sc=[("¿Qué cuatro cosas reviso en una línea de tiempo?", "Orden, escala, rótulos y título", "Estas cuatro comprobaciones cubren lo central."),
        ("¿Qué significa «orden cronológico»?", "De lo más antiguo a lo más reciente", "Se sigue la secuencia del tiempo."),
        ("¿Qué hago cuando encuentro un error?", "Lo corrijo y lo compruebo con un cálculo", "Corregir y comprobar mejora el trabajo.")],
    op=("Línea de ejemplo mal hecha: título ausente; hitos de izquierda a derecha: «2000 Se abre la biblioteca», «1950 Se funda el club», «1975 Se instala el agua potable»; marcas: 1950, 1975, 2025. "
        "Revisa con las cuatro preguntas de la pauta. Escribe qué errores hay y cómo quedaría corregida, con un título.",
        "Errores: no hay título; el orden es incorrecto; la escala es irregular (25 y 50 años). Corregida: 1950 Se funda el club, 1975 Se instala el agua potable, 2000 Se abre la biblioteca; marcas cada 25 años; título «Hitos de la comunidad, 1950-2000».",
        ["detecta orden, escala y título", "propone una versión corregida", "explica cada corrección"],
        ["lista de errores y la línea corregida en una tabla"], ["corregir solo un error", "no explicar los cambios"],
        "Pregunta: «¿Qué criterio de la pauta no se cumple aquí?»."),
    reinforce="Revisa una lista de fechas de tu calendario con las cuatro preguntas de la pauta.",
    extend="Explica cómo cambiaría tu línea de tiempo si agregaras un hito del mundo.",
)
