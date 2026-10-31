"""Material del estudiante de 7.º básico, Historia, Geografía y Ciencias Sociales: OA 09 (formación de la Europa medieval)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI07 OA 09"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (cronología resumida, hecha para este cuaderno). "
     "395: el Imperio romano se divide en Occidente y Oriente. 410: los visigodos, un pueblo germánico, saquean Roma. 455: los vándalos saquean Roma. "
     "476: Odoacro, jefe de un ejército con guerreros germanos, depone al último emperador de Occidente, Rómulo Augústulo. "
     "El Imperio de Oriente, con capital en Constantinopla, continúa hasta 1453. "
     "Causas que se suelen combinar: crisis económica, inestabilidad política, presión de pueblos en las fronteras, ejército con muchos soldados germanos y epidemias. "
     "Después de 476 siguieron existiendo ciudades, obispos, el latín, caminos y leyes romanas.")
build(
    OA, 1, F,
    use="Aprenderé a ubicar la fragmentación del Imperio romano de Occidente en el tiempo y sus causas. Sirve para entender cómo empieza la Europa medieval.",
    prior=["Sé qué fue el Imperio romano y cómo se dividió.", "Sé comparar años d. C.", "Sé que una explicación puede tener varias causas."],
    explain=[
        "En 395 el Imperio romano se dividió en dos partes: Occidente y Oriente. En el Occidente, el poder del emperador se debilitó. En 410 los visigodos, un pueblo germánico, saquearon Roma, y en 455 lo hicieron los vándalos. En 476, el jefe militar Odoacro depuso al último emperador de Occidente, Rómulo Augústulo. Por eso se suele tomar 476 como el fin del Imperio romano de Occidente.",
        "No hubo una sola causa. Se combinaron la crisis económica, la inestabilidad política, la presión de pueblos en las fronteras, un ejército con muchos soldados germanos y epidemias. Además, el Imperio de Oriente, con capital en Constantinopla, siguió existiendo hasta 1453.",
        "Por eso conviene hablar de transformación y fragmentación, más que de una caída total. Después de 476 siguieron las ciudades, los obispos, el latín, los caminos y muchas leyes romanas. El Imperio se dividió en reinos gobernados por jefes germanos, y de esa mezcla nació la Europa medieval, que se extiende aproximadamente entre los siglos V y XV.",
    ],
    vocab=[("fragmentación", "división de un territorio grande en partes más pequeñas"), ("pueblo germánico", "pueblo de origen del centro y norte de Europa, como los visigodos"), ("saquear", "tomar por la fuerza los bienes de una ciudad"), ("deponer", "quitar el poder a un gobernante"), ("Edad Media", "etapa de la historia europea entre los siglos V y XV, aproximadamente")],
    worked=[
        ("Calcular un intervalo", "{F} ¿Cuántos años pasaron entre el saqueo de Roma por los visigodos y el fin del Imperio de Occidente?", ["Fechas: 410 y 476.", "Resto: 476 − 410 = 66."], "66 años"),
        ("Distinguir causas", "{F} ¿Las epidemias son una causa interna o una presión externa?", ["Las epidemias afectaban a la población dentro del Imperio.", "No son un pueblo que presionara en la frontera."], "Una causa interna"),
    ],
    mistakes=[("Hablar de la caída de Roma como si todo hubiera desaparecido en 476.", "Se confunde el fin de un emperador con el fin de una sociedad.", "Siguieron ciudades, obispos, latín y leyes romanas."),
              ("Explicar el fin del Imperio de Occidente solo por las invasiones.", "Se elige una sola causa.", "Combina crisis económica, inestabilidad política, presiones en la frontera y epidemias.")],
    T=[
        ("{F} ¿Qué pueblo germánico saqueó Roma en 410?", "Los visigodos", "La ficha lo indica."),
        ("{F} ¿Quién fue el último emperador de Occidente?", "Rómulo Augústulo", "La ficha lo indica."),
        ("{F} ¿Cuál era la capital del Imperio de Oriente?", "Constantinopla", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre la división del Imperio y el fin del Imperio de Occidente?", "476-395", "Se restan los años d. C.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre el saqueo de los vándalos y el fin del Imperio de Occidente?", "476-455", "Se restan los años d. C.", " años"),
        ("{F} Ordena de más antiguo a más reciente: saqueo de los vándalos, división del Imperio, fin del Imperio de Occidente, saqueo de los visigodos.", "División del Imperio, saqueo de los visigodos, saqueo de los vándalos, fin del Imperio de Occidente", "Las fechas son 395, 410, 455 y 476."),
        ("=", "{F} ¿Cuántos años continuó el Imperio de Oriente después de 476?", "1453-476", "Se restan los años d. C.", " años"),
        ("{F} Clasifica cada causa como interna (I) o externa (E): 1) crisis económica; 2) presión de pueblos en las fronteras; 3) inestabilidad política; 4) epidemias.", "1 I, 2 E, 3 I, 4 I", "Solo la presión en las fronteras viene de afuera."),
        ("{F} ¿Qué cosas siguieron existiendo después de 476?", "Ciudades, obispos, el latín, caminos y leyes romanas", "La ficha lo indica."),
        ("{F} Ana dice: «En 476 Roma desapareció por completo». Corrígela con dos datos de la ficha.", "Siguió el Imperio de Oriente hasta 1453 y en Occidente continuaron ciudades, latín, obispos y leyes", "Fue una transformación, no una desaparición total."),
        ("{F} Pedro dice: «Roma cayó solo porque la invadieron». Da dos causas de la ficha que muestren que no.", "Por ejemplo: la crisis económica y la inestabilidad política", "La ficha nombra varias causas."),
        ("{F} ¿Por qué se toma 476 como fecha simbólica y no como el fin de todo?", "Porque marca la deposición del último emperador de Occidente, aunque el cambio fue gradual", "Fue un hecho político, no un cambio inmediato en la vida."),
        ("{F} ¿Qué significa que los vándalos y los visigodos «saquearon» Roma y no que «la conquistaron para gobernarla»?", "Tomaron bienes de la ciudad por la fuerza; no la ocuparon para gobernar", "La ficha habla de saqueos, no de gobierno."),
    ],
    ctx=("Un afiche escolar dice: «476: cae Roma y comienza la oscuridad». Con la ficha, ¿qué dos ideas corriges? {F}", "Que no desapareció todo (siguió el Imperio de Oriente y muchas costumbres) y que no hubo una sola causa", "Fue una transformación con varias causas."),
    sc=[("¿Qué es la fragmentación del Imperio?", "La división de un territorio grande en partes más pequeñas", "Dio origen a varios reinos."),
        ("¿Cuándo terminó el Imperio de Occidente, según la ficha?", "En 476", "Odoacro depuso al último emperador."),
        ("=", "{F} ¿Cuántos años pasaron entre 410 y 455?", "455-410", "Se restan los años d. C.", " años")],
    op=("Dibuja una línea de tiempo con las fechas de la ficha entre 395 y 476, y marca el Imperio de Oriente con una flecha que sigue hasta 1453. Escribe debajo tres causas del debilitamiento y dos cosas que continuaron. {F}",
        "Fechas 395, 410, 455 y 476; flecha de Oriente; causas: crisis económica, inestabilidad política, presión de pueblos; continuidades: latín y ciudades.",
        ["respeta el orden de las fechas", "incluye la flecha de Oriente", "tres causas y dos continuidades"], ["línea de tiempo dibujada", "causas y continuidades escritas"], ["dar una sola causa", "decir que todo desapareció"],
        "Pide que explique por qué usamos el término «transformación» y no solo «caída»."),
    reinforce="Di en voz alta las cuatro fechas de la ficha y qué ocurrió en cada una.",
    extend="Escribe una pregunta sobre cómo vivían las personas comunes en las ciudades de Occidente tras 476.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (resumen hecho para este cuaderno; los años son aproximados). "
     "Visigodos: reino en Hispania y el sur de la Galia; después de 507 su territorio quedó sobre todo en Hispania, con capital en Toledo. "
     "Ostrogodos: reino en Italia desde 493 con el rey Teodorico, que gobernó hasta 526. "
     "Francos: reino en la Galia; el rey Clodoveo gobernó entre 481 y 511 y se hizo cristiano católico hacia 500. "
     "Vándalos: reino en el norte de África, con capital en Cartago, desde 439 hasta 534. "
     "Anglos y sajones: se establecieron en la isla de Britania. "
     "Lombardos: se instalaron en el norte de Italia desde 568. "
     "Visigodos, ostrogodos y vándalos seguían una doctrina cristiana llamada arrianismo, distinta de la católica.")
build(
    OA, 2, F,
    use="Aprenderé a distinguir los pueblos germánicos y los reinos que formaron. Sirve para no tratarlos como un solo grupo.",
    prior=["Sé qué pasó con el Imperio de Occidente.", "Sé calcular años d. C.", "Sé ubicar Hispania, la Galia e Italia en un mapa."],
    explain=[
        "Los pueblos germánicos no eran un solo grupo. Visigodos, ostrogodos, francos, vándalos, lombardos y anglosajones tenían jefes, costumbres y territorios distintos. Algunos llegaron como aliados o soldados del Imperio; otros, en grupos que buscaban tierras.",
        "En las antiguas provincias romanas formaron reinos. Los visigodos, en Hispania, con capital en Toledo; los ostrogodos, en Italia con el rey Teodorico; los francos, en la Galia, con el rey Clodoveo; los vándalos, en el norte de África. Cada reino tuvo su historia: unos duraron siglos y otros solo décadas.",
        "Las diferencias eran también religiosas: visigodos, ostrogodos y vándalos seguían el arrianismo, una doctrina cristiana distinta de la católica, mientras que Clodoveo, rey de los francos, se hizo católico hacia 500, lo que le dio el apoyo de la Iglesia católica, a la que pertenecía gran parte de la población romanizada. Estos reinos se mezclaron con las poblaciones romanizadas que ya vivían allí, y de esa mezcla nació una nueva sociedad.",
    ],
    vocab=[("reino", "territorio gobernado por un rey"), ("arrianismo", "doctrina cristiana distinta de la católica, seguida por varios pueblos germánicos"), ("romanizado", "que adoptó la lengua, las leyes y las costumbres de Roma"), ("aliado", "pueblo que se une a otro para ayudarse"), ("capital", "ciudad principal de un reino")],
    worked=[
        ("Calcular un reinado", "Un rey de ejemplo gobernó entre 590 y 625. ¿Cuántos años gobernó?", ["Gobernó entre 590 y 625.", "Resto: 625 − 590 = 35."], "35 años"),
        ("Ubicar un reino", "{F} ¿Dónde tuvieron su reino los ostrogodos?", ["Busco ostrogodos en la ficha.", "La ficha dice Italia."], "En Italia"),
    ],
    mistakes=[("Decir que los pueblos germánicos eran un solo pueblo.", "Se mira solo que eran «de fuera» del Imperio.", "Cada pueblo tuvo su territorio, rey y costumbres."),
              ("Creer que los reinos reemplazaron por completo a la población romana.", "Se ignora la mezcla.", "Los pueblos germánicos se mezclaron con la población romanizada.")],
    T=[
        ("{F} ¿Cuál era la capital de los visigodos en Hispania?", "Toledo", "La ficha lo indica."),
        ("{F} ¿Quién fue el rey de los ostrogodos en Italia?", "Teodorico", "La ficha lo indica."),
        ("{F} ¿Dónde se instalaron los lombardos?", "En el norte de Italia", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años gobernó Teodorico, de 493 a 526?", "526-493", "Se restan los años.", " años"),
        ("=", "{F} ¿Cuántos años duró el reino vándalo, de 439 a 534?", "534-439", "Se restan los años.", " años"),
        ("{F} ¿En qué ciudad estaba la capital del reino vándalo?", "En Cartago", "La ficha lo indica."),
        ("{F} Relaciona cada pueblo con su región: francos, vándalos, anglos y sajones.", "Francos: Galia; vándalos: norte de África; anglos y sajones: Britania", "La ficha ubica a cada uno."),
        ("{F} ¿Qué doctrina seguían visigodos, ostrogodos y vándalos?", "El arrianismo", "La ficha lo indica."),
        ("{F} ¿Qué religión adoptó Clodoveo hacia 500?", "El cristianismo católico", "La ficha lo indica."),
        ("{F} Ana dice: «Los pueblos germánicos eran todos iguales». Da dos diferencias de la ficha.", "Tenían territorios distintos y algunos eran arrianos mientras Clodoveo era católico", "La ficha muestra diferencias."),
        ("{F} Según la explicación de la clase, ¿qué ventaja le dio a Clodoveo hacerse católico?", "El apoyo de la Iglesia católica, a la que pertenecía gran parte de la población romanizada", "La Iglesia respaldó a un rey de su misma fe."),
        ("{F} Pedro dice: «Los reinos germánicos eliminaron a la población romana». Corrígelo.", "Se mezclaron con la población romanizada, que ya vivía allí", "La ficha habla de mezcla."),
        ("{F} ¿Quién gobernó menos años: Teodorico (493 a 526) o Clodoveo (481 a 511)? Calcula ambos.", "Clodoveo: 30 años frente a 33 de Teodorico", "Se restan los años de cada reinado."),
    ],
    ctx=("Un mapa de museo muestra el año 500 con un solo color para «bárbaros». Con la ficha, ¿qué corrección propones? {F}", "Mostrar reinos distintos (visigodos, ostrogodos, francos, vándalos y otros) con colores diferentes", "Eran pueblos distintos, con reinos distintos."),
    sc=[("¿Qué es un pueblo germánico?", "Un pueblo de origen del centro y norte de Europa, como los visigodos", "No eran un solo grupo."),
        ("¿Qué doctrina seguían los visigodos?", "El arrianismo", "La ficha lo indica."),
        ("{F} ¿Qué pueblo se instaló en el norte de Italia desde 568?", "Los lombardos", "La ficha lo indica.")],
    op=("Haz un mapa mudo de Europa y norte de África con los seis pueblos de la ficha. Pinta cada reino de un color y escribe junto a cada uno su capital o rey si la ficha lo da. {F}",
        "Visigodos en Hispania (Toledo), ostrogodos en Italia (Teodorico), francos en la Galia (Clodoveo), vándalos en el norte de África (Cartago).",
        ["ubica los reinos en su región", "usa colores distintos", "agrega capital o rey donde se conozca"], ["mapa dibujado"], ["usar un solo color para todos", "ubicar mal a los vándalos"],
        "Pide que explique por qué un mapa con un solo color sería engañoso."),
    reinforce="Nombra cuatro pueblos germánicos con su región.",
    extend="Escribe una pregunta sobre cómo convivían los pueblos germánicos con la población romanizada.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (resumen hecho para este cuaderno; algunas cifras son de ejemplo). "
     "Iglesia cristiana: en las ciudades había obispos que ayudaban a gobernar y a cuidar a los pobres. "
     "Monasterios: Benito de Nursia fundó el monasterio de Monte Cassino, en Italia, hacia 529, y su regla organizó la vida de los monjes en oración y trabajo. En los monasterios se copiaban libros a mano. "
     "Derecho: el rey visigodo Alarico II mandó recopilar leyes romanas en el Breviario de Alarico, de 506. "
     "El latín siguió siendo la lengua de la Iglesia, de los documentos y de la cultura. "
     "Dato de ejemplo: un monje copia una página al día y un libro tiene 300 páginas.")
build(
    OA, 3, F,
    use="Aprenderé a relacionar la herencia grecorromana con el cristianismo en la formación de la Europa medieval. Sirve para entender cómo se conservó y se transformó el legado de Roma.",
    prior=["Sé qué pueblos germánicos formaron reinos.", "Sé que el cristianismo fue religión oficial en 380.", "Sé dividir con números pequeños."],
    explain=[
        "La Europa medieval nació de una mezcla de tres herencias: la grecorromana (ciudades, derecho, latín), la germánica (reinos y costumbres) y la cristiana, también llamada judeocristiana porque el cristianismo nació en el mundo judío y usa su Biblia. La Iglesia fue una institución muy importante: los obispos vivían en las ciudades, ayudaban a gobernar y a cuidar a los pobres.",
        "En los monasterios, como Monte Cassino, fundado hacia 529 por Benito de Nursia, los monjes vivían en oración y trabajo, y copiaban libros a mano. Gracias a las copias se conservaron muchas obras antiguas. Los reinos germánicos también usaron el derecho romano: en 506, Alarico II mandó recopilar leyes romanas en el Breviario de Alarico.",
        "El latín siguió siendo la lengua de la Iglesia y de los documentos, aunque la gente hablaba lenguas que se transformaban. Así, el legado grecorromano continuó, pero cambió: se adaptó a los reinos y a la fe cristiana. No fue una copia intacta, y hubo pérdidas de obras y de conocimientos.",
    ],
    vocab=[("obispo", "jefe de la Iglesia en una ciudad y su región"), ("monasterio", "lugar donde viven monjes dedicados a la oración y el trabajo"), ("regla", "conjunto de normas que organiza la vida de una comunidad"), ("recopilar", "reunir leyes o textos en una colección"), ("herencia", "lo que se recibe de una época o grupo anterior")],
    worked=[
        ("Calcular una copia", "{F} ¿Cuántos días tarda un monje en copiar un libro de 300 páginas?", ["Copia una página al día.", "Son 300 páginas: 300 días."], "300 días"),
        ("Repartir el trabajo", "{F} ¿Cuántos días tardan 10 monjes si se reparten las páginas en partes iguales?", ["Cada uno copia 300 ÷ 10 = 30 páginas.", "A una página al día, tardan 30 días."], "30 días"),
    ],
    mistakes=[("Pensar que los monasterios solo servían para rezar.", "Se ignora el trabajo de copiar y cultivar.", "Los monjes copiaron libros y trabajaron la tierra."),
              ("Creer que el legado grecorromano pasó intacto a la Edad Media.", "Se confunde legado con copia.", "Se adaptó a los reinos y a la fe cristiana, y se perdieron cosas.")],
    T=[
        ("{F} ¿Quién fundó el monasterio de Monte Cassino?", "Benito de Nursia", "La ficha lo indica."),
        ("{F} ¿En qué año se hizo el Breviario de Alarico?", "En 506", "La ficha lo indica."),
        ("{F} ¿Qué lengua siguió usando la Iglesia?", "El latín", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos días tardan 5 monjes en copiar un libro de 300 páginas, si se reparten las páginas en partes iguales?", "300//5", "Se divide el total entre los monjes, a una página por día.", " días"),
        ("=", "{F} ¿Cuántos años pasaron entre el Breviario de Alarico y la fundación de Monte Cassino?", "529-506", "Se restan los años d. C.", " años"),
        ("{F} ¿Qué hacían los monjes en los monasterios, según la ficha?", "Oraban, trabajaban y copiaban libros", "La ficha lo indica."),
        ("{F} Clasifica como herencia grecorromana (G) o aporte cristiano (C): 1) leyes romanas recopiladas; 2) obispos que cuidan a los pobres; 3) uso del latín; 4) monasterios con regla.", "1 G, 2 C, 3 G, 4 C", "El derecho y el latín vienen de Roma; obispos y monasterios son de la Iglesia."),
        ("=", "{F} ¿Cuántas páginas copian 8 monjes en 20 días, a una página al día cada uno?", "8*20", "Se multiplican los monjes por los días.", " páginas"),
        ("{F} ¿Por qué se conservaron muchas obras antiguas gracias a los monasterios?", "Porque los monjes las copiaban a mano y guardaban las copias", "La ficha dice que copiaban libros."),
        ("{F} Pedro dice: «Los reinos germánicos rechazaron el derecho romano». Corrígelo.", "Usaron leyes romanas: el rey Alarico II mandó recopilarlas en 506", "El Breviario de Alarico lo muestra."),
        ("{F} Ana dice: «El legado de Roma llegó intacto a la Edad Media». Corrígela.", "Se adaptó a los reinos y a la fe cristiana, y se perdieron obras y conocimientos", "El legado cambió."),
        ("{F} ¿Cómo se relacionan el cristianismo y el latín en la formación de la Europa medieval?", "La Iglesia mantuvo el latín como lengua de los documentos y la cultura", "La ficha lo dice."),
        ("{F} Una persona dice: «Los monjes copiaban libros solo de la Biblia». ¿Qué le falta saber según la explicación de la clase?", "Que se conservaron muchas obras antiguas gracias a las copias", "La ficha habla de obras antiguas en general."),
    ],
    ctx=("Un taller de manualidades quiere copiar a mano un libro de 120 páginas con 4 personas, a una página al día cada una. ¿Cuántos días tardan, y qué institución medieval se parece? {F}", "30 días; un monasterio", "120 ÷ 4 = 30 días."),
    sc=[("¿Qué era un monasterio?", "Un lugar donde viven monjes dedicados a la oración y el trabajo", "Allí se copiaban libros."),
        ("¿Qué era el Breviario de Alarico?", "Una recopilación de leyes romanas hecha por un rey visigodo en 506", "Muestra el uso del derecho romano."),
        ("{F} ¿Qué lengua usaban los documentos de la Iglesia, según la ficha?", "El latín", "La ficha dice que siguió siendo la lengua de la Iglesia.")],
    op=("Dibuja un esquema con tres columnas (herencia grecorromana, herencia germánica y herencia cristiana) y escribe dos elementos en cada una. Después explica en dos líneas cómo se conservó el saber antiguo. {F}",
        "Grecorromana: latín y derecho; germánica: reinos y reyes; cristiana: obispos y monasterios; el saber se conservó copiando libros.",
        ["dos elementos por columna", "elementos bien clasificados", "explica la conservación del saber"], ["esquema dibujado", "explicación escrita"], ["poner todo en una sola herencia", "decir que no cambió nada"],
        "Pide que explique qué se pudo perder en la transmisión."),
    reinforce="Nombra dos instituciones de la Iglesia medieval y una tarea de cada una.",
    extend="Escribe una pregunta sobre cómo se aprendía a leer y a escribir en un monasterio.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (resumen hecho para este cuaderno). "
     "Imperio de Oriente (llamado bizantino): capital Constantinopla; se hablaba sobre todo griego; el emperador Justiniano (527 a 565) hizo recopilar el derecho romano entre 529 y 534. "
     "Reino de los francos: en la Galia; Carlomagno fue rey desde 768 y fue coronado emperador por el papa León III en el año 800. "
     "Hispania: tras el reino visigodo, en 711 llegaron pueblos musulmanes que dominaron gran parte de la península y formaron un emirato con capital en Córdoba desde 756. "
     "Britania: la influencia romana había sido más débil; se establecieron anglos y sajones. "
     "Italia: siguieron ciudades y obispos, y el obispo de Roma tenía gran prestigio.")
build(
    OA, 4, F,
    use="Aprenderé a reconocer continuidades y diferencias entre las regiones de Europa tras el fin del Imperio de Occidente. Sirve para no imaginar una Europa igual en todas partes.",
    prior=["Sé qué pueblos formaron reinos.", "Sé qué herencias recibió la Europa medieval.", "Sé calcular años d. C."],
    explain=[
        "Cada región de Europa siguió un camino distinto después de 476. En el Imperio de Oriente, con capital en Constantinopla, el griego fue la lengua principal y el emperador Justiniano hizo recopilar el derecho romano. Allí hubo continuidad política de un Estado romano hasta 1453.",
        "En la Galia, los francos formaron un reino que alcanzó gran poder con Carlomagno, coronado emperador por el papa León III en el año 800: la Iglesia daba así un respaldo religioso al poder del rey, es decir, lo legitimaba. En Hispania, tras el reino visigodo, llegaron en 711 pueblos musulmanes que formaron un emirato con capital en Córdoba. En Britania, donde la influencia romana había sido más débil, se establecieron anglos y sajones. En Italia continuaron ciudades y obispos.",
        "Estas diferencias muestran que no hubo una Europa uniforme. Algunas regiones mantuvieron mucho de lo romano; otras cambiaron más. Entender la Edad Media exige mirar cada región, sus lenguas, religiones y gobiernos, y evitar generalizar a toda Europa lo que ocurrió en un solo lugar.",
    ],
    vocab=[("continuidad regional", "rasgo que se mantiene en una región a lo largo del tiempo"), ("emirato", "territorio gobernado por un emir, jefe musulmán"), ("bizantino", "relativo al Imperio romano de Oriente"), ("emperador", "gobernante con gran poder sobre varios pueblos"), ("prestigio", "valor o respeto que alguien tiene ante los demás")],
    worked=[
        ("Calcular un intervalo", "{F} ¿Cuántos años pasaron entre la llegada de los musulmanes a Hispania y la coronación de Carlomagno?", ["Fechas: 711 y 800.", "Resto: 800 − 711 = 89."], "89 años"),
        ("Identificar una continuidad", "{F} ¿Qué lengua se hablaba sobre todo en el Imperio de Oriente?", ["Busco Imperio de Oriente en la ficha.", "Dice que se hablaba griego."], "Griego"),
    ],
    mistakes=[("Describir toda Europa como si fuera igual.", "Se generaliza desde una región.", "Cada región tuvo reinos, lenguas y religiones distintos."),
              ("Creer que en Hispania siguió siempre el reino visigodo.", "Se ignora la llegada de 711.", "Después de 711, gran parte de la península fue dominada por pueblos musulmanes.")],
    T=[
        ("{F} ¿Cuál era la capital del Imperio de Oriente?", "Constantinopla", "La ficha lo indica."),
        ("{F} ¿Quién fue emperador en 527 a 565 y mandó recopilar el derecho romano?", "Justiniano", "La ficha lo indica."),
        ("{F} ¿Quién coronó emperador a Carlomagno y qué muestra eso sobre la Iglesia?", "El papa León III; que la Iglesia respaldaba y legitimaba el poder político", "La coronación daba un respaldo religioso al rey."),
        ("=", "{F} ¿Cuántos años gobernó Justiniano, de 527 a 565?", "565-527", "Se restan los años d. C.", " años"),
        ("=", "{F} ¿Cuántos años fue rey Carlomagno antes de ser coronado emperador?", "800-768", "Se restan los años d. C.", " años"),
        ("{F} ¿Qué año llegaron pueblos musulmanes a Hispania?", "711", "La ficha lo indica."),
        ("{F} ¿Dónde estaba la capital del emirato en Hispania?", "En Córdoba", "La ficha lo indica."),
        ("{F} Relaciona cada región con un rasgo: Oriente, Galia, Hispania, Britania.", "Oriente: griego y derecho de Justiniano; Galia: Carlomagno; Hispania: llegada musulmana en 711; Britania: anglos y sajones", "La ficha da un rasgo de cada región."),
        ("=", "{F} ¿Cuántos años después de la llegada de los musulmanes a Hispania se formó el emirato con capital en Córdoba (756)?", "756-711", "Se restan los años d. C.", " años"),
        ("{F} Ana dice: «Toda Europa tenía el mismo gobierno que el Imperio romano». Corrígela con dos regiones.", "En el Oriente continuó un imperio con capital en Constantinopla, y en Hispania había un emirato con capital en Córdoba", "Las regiones tuvieron gobiernos distintos."),
        ("{F} ¿Por qué se dice que en el Imperio de Oriente hubo continuidad del Estado romano?", "Porque el imperio con capital en Constantinopla continuó hasta 1453", "La ficha lo dice."),
        ("{F} Pedro dice: «En Hispania siguió gobernando el reino visigodo hasta 1453». Corrígelo.", "Desde 711 pueblos musulmanes dominaron gran parte de la península", "La ficha lo muestra."),
        ("{F} ¿Qué diferencia hay entre la influencia romana en Italia y en Britania?", "En Italia continuaron ciudades y obispos; en Britania la influencia romana había sido más débil", "La ficha los contrasta."),
    ],
    ctx=("Un colegio quiere hacer una obra de teatro sobre «Europa en el año 800» y un estudiante propone un solo disfraz para todos los habitantes. ¿Qué dos disfraces distintos propones con la ficha? {F}", "Por ejemplo: un habitante del Imperio de Oriente y un franco de Carlomagno, o uno de Córdoba", "Hay varias regiones con rasgos distintos."),
    sc=[("¿Qué es una continuidad regional?", "Un rasgo que se mantiene en una región a lo largo del tiempo", "Es lo que la ficha muestra en Oriente."),
        ("¿Quién fue Carlomagno?", "Un rey franco coronado emperador en el año 800", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años duró la recopilación del derecho romano ordenada por Justiniano, de 529 a 534?", "534-529", "Se restan los años d. C.", " años")],
    op=("Haz un cuadro con cuatro regiones (Oriente, Galia, Hispania, Britania): una continuidad o rasgo, un cambio y una fecha de la ficha. Después escribe una frase que explique por qué no hubo una Europa uniforme. {F}",
        "Oriente: griego y derecho de Justiniano; Galia: Carlomagno en 800; Hispania: llegada en 711; Britania: anglos y sajones.",
        ["completa las cuatro regiones", "usa fechas de la ficha", "la frase explica la diversidad"], ["cuadro escrito", "frase escrita"], ["repetir lo mismo en todas las regiones", "ubicar mal una fecha"],
        "Pide que explique qué región mantuvo más rasgos romanos y por qué."),
    reinforce="Nombra cuatro regiones y un rasgo de cada una.",
    extend="Escribe una pregunta sobre cómo se comunicaban las personas entre regiones con lenguas distintas.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (resumen hecho para este cuaderno). "
     "Hacia el año 800 convivían en Europa y sus cercanías cuatro grandes ámbitos: el reino de los francos de Carlomagno; el Imperio de Oriente, con capital en Constantinopla; el emirato de Córdoba en Hispania, desde 756; y los reinos anglosajones de Britania. "
     "Factores de la formación de la Europa medieval: la herencia romana (latín, derecho, ciudades); los reinos germánicos; la Iglesia cristiana; el contacto con el mundo islámico, por comercio y por traducciones; y nuevos pueblos que llegaron después, como los vikingos, cuyo ataque al monasterio de Lindisfarne, en Britania, se registró en 793.")
build(
    OA, 5, F,
    use="Aprenderé a explicar la formación de la Europa medieval como un proceso plural. Sirve para integrar causas y regiones sin reducir todo a una sola explicación.",
    prior=["Sé qué pasó con el Imperio de Occidente.", "Sé qué pueblos formaron reinos y qué herencias recibieron.", "Sé que hubo regiones distintas."],
    explain=[
        "La Europa medieval se formó por la combinación de varios procesos. Hubo una herencia romana (latín, derecho, ciudades), reinos germánicos, una Iglesia cristiana muy influyente y contactos con otros mundos, como el islámico. Además llegaron nuevos pueblos, como los vikingos, que atacaron Lindisfarne en 793.",
        "No fue un proceso uniforme: hacia el año 800 convivían ámbitos distintos, como el reino de los francos de Carlomagno, el Imperio de Oriente, el emirato de Córdoba y los reinos anglosajones. Cada uno tenía sus lenguas, leyes y creencias. Por eso decimos que la Europa medieval fue plural.",
        "Para explicar este proceso se usan varias causas y se evita decir que una sola civilización o un solo pueblo lo hizo todo. Una explicación sólida señala qué herencias se mantuvieron, qué cambió, qué contactos influyeron y qué no sabemos. Esto ayuda a entender la Edad Media sin verla como una época oscura ni como una copia de Roma. Para ubicar un año en su siglo: del 701 al 800 es el siglo VIII, y del 1401 al 1500, el siglo XV.",
    ],
    vocab=[("plural", "formado por elementos distintos que conviven"), ("proceso", "conjunto de cambios que ocurren a lo largo del tiempo"), ("vikingos", "pueblos del norte de Europa que navegaban y atacaron costas europeas"), ("mundo islámico", "conjunto de territorios y pueblos que seguían el islam"), ("factor", "elemento que influye en un resultado")],
    worked=[
        ("Contar ámbitos", "{F} ¿Cuántos ámbitos distintos convivían hacia el año 800?", ["Cuento los ámbitos nombrados: francos, Oriente, Córdoba y anglosajones.", "Son cuatro nombres distintos."], "4 ámbitos"),
        ("Identificar un factor", "{F} ¿Qué factor se relaciona con las traducciones?", ["Las traducciones fueron un contacto con otro mundo.", "Ese factor es el contacto con el mundo islámico."], "El contacto con el mundo islámico"),
    ],
    mistakes=[("Decir que la Europa medieval fue solo herencia de Roma.", "Se elige un factor.", "Combina herencia romana, reinos germánicos, Iglesia y contactos."),
              ("Describir la Edad Media como una época oscura.", "Se mira solo la pérdida.", "Hubo conservación, transformación y nuevos aportes.")],
    T=[
        ("{F} ¿En qué año atacaron los vikingos el monasterio de Lindisfarne?", "En 793", "La ficha lo indica."),
        ("{F} ¿Cuál era la capital del emirato en Hispania?", "Córdoba", "La ficha lo indica."),
        ("{F} ¿Cuántos factores de la formación de la Europa medieval nombra la ficha?", "5", "Herencia romana, reinos germánicos, Iglesia, contacto islámico y nuevos pueblos."),
        ("=", "{F} ¿Cuántos años pasaron entre el ataque a Lindisfarne y el año 800?", "800-793", "Se restan los años.", " años"),
        ("=", "{F} ¿Cuántos años antes del año 800 se formó el emirato de Córdoba?", "800-756", "Se restan los años.", " años"),
        ("{F} Clasifica cada factor como herencia (H), contacto (C) o novedad (N): 1) el derecho romano; 2) las traducciones desde el mundo islámico; 3) la llegada de los vikingos.", "1 H, 2 C, 3 N", "Cada factor tiene un origen distinto."),
        ("{F} ¿Qué significa que la Europa medieval fue plural?", "Que estaba formada por elementos distintos que convivían", "Cada ámbito tenía lenguas, leyes y creencias propias."),
        ("{F} ¿Qué ámbito de la ficha pertenecía al mundo islámico y por qué dos vías hubo contacto con él?", "El emirato de Córdoba; el contacto fue por comercio y por traducciones", "La ficha nombra ambas vías."),
        ("{F} Ordena de más antiguo a más reciente: ataque a Lindisfarne, emirato de Córdoba, año 800.", "Emirato de Córdoba (756), ataque a Lindisfarne (793), año 800", "Las fechas son 756, 793 y 800."),
        ("{F} Pedro dice: «Europa se formó solo por Roma». Da dos factores de la ficha que muestren que no.", "Los reinos germánicos y la Iglesia cristiana", "La ficha nombra varios factores."),
        ("{F} Ana dice: «La Edad Media fue una época oscura y sin cambios». Corrígela con dos datos de la ficha.", "Hubo nuevos reinos, contactos con el mundo islámico y la llegada de otros pueblos, que causaron cambios", "La ficha muestra cambio y contacto."),
        ("{F} ¿Por qué es importante mencionar lo que no sabemos en una explicación sobre la Edad Media?", "Porque las fuentes son incompletas y conviene no afirmar más de lo que muestran", "Una explicación honesta reconoce sus límites."),
        ("{F} ¿Qué evidencia permitiría saber cómo se comunicaban Córdoba y la Galia?", "Textos o monedas de ambos lugares, o rutas de comercio", "Los objetos y escritos muestran contacto."),
    ],
    ctx=("Un museo prepara una sala llamada «Europa, año 800». ¿Qué título explicativo respeta mejor lo aprendido: «La Europa de los francos» o «Una Europa plural»? {F}", "«Una Europa plural»", "Convivían ámbitos distintos, no uno solo."),
    sc=[("¿Qué es un proceso histórico?", "Un conjunto de cambios que ocurren a lo largo del tiempo", "No ocurre en un solo día."),
        ("¿Qué quiere decir que la Europa medieval fue plural?", "Que reunía elementos distintos que convivían", "Es la idea central de la clase."),
        ("{F} ¿En qué siglo atacaron los vikingos Lindisfarne y en qué siglo terminó el Imperio de Oriente (1453)?", "En el siglo VIII; en el siglo XV", "793 está entre 701 y 800, y 1453 entre 1401 y 1500.")],
    op=("Escribe una explicación de 8 líneas: tres factores de la formación de la Europa medieval (con un dato de la ficha cada uno), dos regiones que fueron distintas y una frase que reconozca algo que aún no sabemos. {F}",
        "Factores: herencia romana, reinos germánicos e Iglesia; regiones: Oriente y Córdoba; no sabemos cómo vivían las personas comunes.",
        ["tres factores con datos", "dos regiones distintas", "reconoce un límite"], ["explicación escrita"], ["reducir todo a Roma", "no mencionar ningún límite"],
        "Pide que explique por qué «plural» es una mejor descripción que «uniforme»."),
    reinforce="Nombra tres factores de la formación de la Europa medieval y un dato de cada uno.",
    extend="Escribe una pregunta sobre qué papel tuvieron las mujeres en los monasterios medievales.",
)
