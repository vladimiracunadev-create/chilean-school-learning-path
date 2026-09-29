"""Specific third-grade sequences for Arts, PE, English and Indigenous Language and Culture."""
from __future__ import annotations


ATTITUDES = {
    "AR": (
        ("de Actitud AR03 OAA A", "disfrute de expresiones artísticas diversas"),
        ("de Actitud AR03 OAA B", "expresión artística de ideas y sentimientos propios"),
        ("de Actitud AR03 OAA C", "cuidado del patrimonio artístico local y mundial"),
        ("de Actitud AR03 OAA D", "creatividad mediante experimentación y pensamiento divergente"),
        ("de Actitud AR03 OAA E", "colaboración y recepción respetuosa de retroalimentación"),
        ("de Actitud AR03 OAA F", "valoración del trabajo riguroso y el esfuerzo"),
        ("de Actitud AR03 OAA G", "respeto por la originalidad del trabajo artístico ajeno"),
    ),
    "EF": (
        ("de Actitud EF03 OAA A", "valoración de los efectos saludables de la actividad física regular"),
        ("de Actitud EF03 OAA B", "interés por mejorar la condición física de manera progresiva"),
        ("de Actitud EF03 OAA C", "confianza progresiva al practicar actividad física"),
        ("de Actitud EF03 OAA D", "participación activa mediante una vía accesible"),
        ("de Actitud EF03 OAA E", "participación equitativa sin estereotipos de género"),
        ("de Actitud EF03 OAA F", "respeto de la diversidad corporal sin comparaciones"),
        ("de Actitud EF03 OAA G", "colaboración y recepción de retroalimentación"),
        ("de Actitud EF03 OAA H", "esfuerzo, superación y perseverancia con autocuidado"),
    ),
    "EN": (
        ("de Actitud EN03 OAA A", "interés por conocer el contexto y entorno propio"),
        ("de Actitud EN03 OAA B", "confianza progresiva para aprender un nuevo idioma"),
        ("de Actitud EN03 OAA C", "curiosidad y respeto ante culturas y modos de vida diversos"),
        ("de Actitud EN03 OAA D", "cooperación para alcanzar propósitos comunicativos"),
    ),
    "LC": (
        ("de Actitud LC03 OAA A", "pertenencia responsable a la red de la vida desde lengua y cultura"),
        ("de Actitud LC03 OAA B", "interculturalidad basada en aprecio y comprensión mutuos"),
        ("de Actitud LC03 OAA C", "relación integral y respetuosa con los entornos y sus recursos"),
        ("de Actitud LC03 OAA D", "trabajo riguroso acorde con oralidad, territorio y enseñanza ancestral pertinente"),
    ),
}


def _p(topic: str, prior: str, vocabulary: str, anchor: str, misconception: str, focuses: str) -> dict:
    return {
        "topic": topic,
        "prior": prior,
        "vocabulary": vocabulary,
        "anchor": anchor,
        "misconception": misconception,
        "focuses": [focus.strip() for focus in focuses.split("|")],
    }


AR = {
    "AR03 OA 01": _p("Creación visual con propósito desde naturaleza, cultura y arte", "observar detalles y expresar ideas mediante imágenes", "propósito, referente, entorno, mito, ser imaginario, arte antiguo, Chile", "referentes naturales, culturales y artísticos identificados, sin convertirlos en modelos para copiar", "copiar un referente o presentar una cultura como decorado homogéneo", "Observar fenómenos naturales con detalle|Transformar una observación en intención visual|Interpretar un mito desde una fuente identificada|Imaginar sin estereotipar seres culturales|Dialogar con arte antiguo y arte chileno|Crear una obra personal que articule referentes"),
    "AR03 OA 02": _p("Color, textura y forma como lenguaje expresivo", "reconocer línea, color, forma y textura en imágenes", "color frío, color cálido, color expresivo, textura, forma real, forma recreada", "muestrarios y obras donde una variable visual cambia el efecto", "aplicar categorías como receta o creer que un color expresa siempre lo mismo", "Distinguir temperaturas del color|Usar color para una intención propia|Explorar textura en plano y volumen|Observar formas reales|Recrear formas sin calcar"),
    "AR03 OA 03": _p("Materiales, herramientas y procedimientos para crear", "explorar materiales y cuidar herramientas compartidas", "modelado, reciclaje, material natural, ensamblaje, pintura, herramienta, procedimiento", "estaciones técnicas con retazos limpios y herramientas revisadas", "elegir material sólo por apariencia o confundir experimentar con usar sin cuidado", "Probar modelado y huella|Combinar papel, cartón y adhesión|Transformar materiales reutilizables limpios|Integrar materiales naturales sin dañar el entorno|Controlar dibujo y pintura según intención|Construir y documentar una solución técnica"),
    "AR03 OA 04": _p("Observación, emoción y pensamiento frente al arte", "describir primero lo visible y luego interpretar", "obra, artesanía, detalle, lenguaje visual, emoción, interpretación, evidencia", "selección atribuida de obras locales, chilenas, latinoamericanas y de otros lugares", "adivinar la intención del autor o considerar una interpretación como respuesta única", "Describir sin interpretar todavía|Relacionar lenguaje visual y sensación|Fundamentar una idea con detalles|Comparar respuestas ante obras diversas"),
    "AR03 OA 05": _p("Retroalimentación y mejora de trabajos artísticos", "explicar una decisión propia y escuchar otra perspectiva", "fortaleza, criterio, material, técnica, propósito, retroalimentación, revisión", "obras en proceso y criterios acordados antes de comentar", "evaluar por gusto personal, talento o parecido con el modelo", "Construir criterios observables|Reconocer una fortaleza con evidencia|Proponer una mejora coherente|Revisar la obra conservando autoría"),
}


EF = {
    "EF03 OA 01": _p("Combinación de habilidades motrices básicas", "ejecutar locomoción, manipulación y estabilidad por separado", "locomoción, manipulación, estabilidad, dirección, altura, nivel, control", "circuitos con implementos blandos, distancias graduadas y rutas despejadas", "priorizar velocidad o comparar cuerpos en vez de observar control", "Combinar carrera y lanzamiento|Recibir manteniendo estabilidad|Saltar y girar con aterrizaje controlado|Cambiar dirección y nivel|Resolver un circuito combinado"),
    "EF03 OA 02": _p("Soluciones motrices a problemas de juego", "reconocer espacio libre, señal y regla simple", "problema motor, tiempo, espacio, oposición, colaboración, decisión, alternativa", "juegos reducidos que permiten pausar, observar y volver a intentar", "creer que existe una única solución o que ganar demuestra mejor aprendizaje", "Leer tiempo y espacio|Resolver uno contra uno|Cooperar en grupo reducido|Comparar y ajustar soluciones"),
    "EF03 OA 03": _p("Principios de juego en situaciones predeportivas", "desplazarse, pasar y recibir con control", "avanzar, retroceder, recuperar, acompañar, desmarque, visión periférica, regla", "juegos sin eliminación con balones blandos y reglas modificables", "seguir el balón en bloque sin percibir compañeros, o excluir al que pierde posesión", "Avanzar y retroceder en bloque|Recuperar sin contacto riesgoso|Acompañar la jugada|Usar visión periférica en juego"),
    "EF03 OA 04": _p("Actividad física responsable en distintos entornos", "reconocer límites, residuos y señales de seguridad", "entorno, plaza, playa, sendero, conservación, riesgo, mínimo impacto", "planos y casos ficticios de espacios abiertos antes de cualquier salida autorizada", "suponer que toda área natural es recreativa o dejar la seguridad a la improvisación", "Leer oportunidades y riesgos del entorno|Preparar una actividad al aire libre|Moverse sin dejar residuos ni daños|Resolver cambios de clima o superficie|Evaluar el cuidado del espacio utilizado"),
    "EF03 OA 05": _p("Danzas tradicionales y coordinación rítmica", "seguir pulso y secuencias corporales simples", "danza tradicional, pulso, paso, trayectoria, coordinación, contexto, respeto", "registro autorizado de una danza identificada y versión pedagógica pertinente", "reducir una danza a disfraz o exigir contacto físico y roles de género fijos", "Reconocer contexto, música y pulso|Practicar pasos sin estereotipos|Coordinar trayectoria y secuencia|Interpretar respetando origen y variantes"),
    "EF03 OA 06": _p("Condición física mediante actividad moderada a vigorosa", "regular intensidad y reconocer señales corporales", "resistencia, fuerza, flexibilidad, velocidad, intensidad, recuperación, progreso", "estaciones temporizadas con variantes equivalentes y pausas disponibles", "usar dolor, agotamiento o competencia corporal como evidencia de progreso", "Sostener esfuerzo cardiovascular regulado|Aplicar fuerza con técnica y autocarga|Explorar flexibilidad sin rebotes forzados|Combinar velocidad, pausa y recuperación"),
    "EF03 OA 07": _p("Práctica regular y autónoma de actividad física", "identificar actividades agradables y posibles", "regularidad, autonomía, intensidad, frecuencia, barrera, alternativa, disfrute", "agenda ficticia con opciones sin equipamiento y apoyos adultos cuando corresponda", "prescribir una rutina idéntica o responsabilizar al niño por barreras familiares", "Reconocer oportunidades cotidianas|Elegir intensidad moderada o vigorosa|Adaptar ante espacio y recursos|Diseñar una semana activa y flexible"),
    "EF03 OA 08": _p("Registro de respuestas corporales al ejercicio", "nombrar sensaciones antes y después de moverse", "frecuencia cardiaca, respiración, pulso, esfuerzo, registro, variación, recuperación", "actividad breve regulable, reloj y escala perceptiva sin datos biométricos públicos", "diagnosticar salud o comparar rendimiento a partir del pulso de una clase", "Observar antes, durante y después|Localizar y contar pulso con apoyo|Registrar respiración y esfuerzo percibido|Interpretar cambios y recuperación con cautela"),
    "EF03 OA 09": _p("Hábitos seguros de higiene, postura y vida activa", "aplicar higiene, hidratación y detención segura", "calentamiento, postura, higiene, hidratación, protección solar, ropa, colación", "casos ficticios y materiales disponibles, sin controlar cuerpos ni dietas", "moralizar alimentos, exigir recursos familiares o una postura rígida universal", "Preparar cuerpo, ropa y espacio|Moverse con posturas ajustables|Hidratarse y regular el esfuerzo|Aplicar higiene y protección solar|Resolver una jornada activa con autocuidado"),
    "EF03 OA 10": _p("Juego limpio, roles y honestidad", "cumplir reglas conocidas y rotar tareas", "juego limpio, responsabilidad, honestidad, regla, rol, acuerdo, reparación", "juegos colectivos con reglas visibles, arbitraje pedagógico y roles rotativos", "confundir juego limpio con no disputar o liderazgo con mandar", "Comprender el propósito de una regla|Cumplir y revisar roles|Resolver una ventaja injusta|Reparar y reanudar el juego"),
    "EF03 OA 11": _p("Comportamientos seguros durante la actividad física", "detenerse ante una señal y usar implementos conocidos", "calentamiento, instrucción, límite, implemento, distancia, riesgo, aviso", "circuito inspeccionado, señalética y protocolo escolar vigente", "obedecer sin comprender o continuar ante dolor, daño o peligro", "Calentar de manera progresiva|Comprobar instrucciones antes de iniciar|Mantener límites y distancias|Usar y guardar implementos|Detener, avisar y elegir una alternativa"),
}


EN = {
    "EN03 OA 01": _p("Listening to rhymes, chants, songs, stories and dialogues", "recognize familiar classroom words with visual support", "rhyme, chant, song, story, dialogue, speaker, sequence", "short teacher-read or authorized audio texts with pictures and objects", "translate every word or imitate peers without locating evidence", "Track repeated sounds in a rhyme|Follow actions in a chant|Sequence a short song or story|Identify speakers in a dialogue|Respond to a new listening text"),
    "EN03 OA 02": _p("Listening for familiar topics and functions", "follow common classroom instructions", "school, animal, house, shape, occupation, town, food, celebration", "brief messages about familiar themes with culturally varied images", "identify isolated nouns but miss the communicative purpose", "Follow instructions and introductions|Identify abilities and feelings|Locate possession, quantity and position|Recognize actions in progress|Connect topic and communicative purpose"),
    "EN03 OA 03": _p("Demonstrating detailed listening comprehension", "match key words to objects and actions", "character, object, animal, setting, main idea, detail, sequence", "a three-part oral text replayed for a different purpose each time", "guess from one picture without checking what was heard", "Identify people, animals and objects|Select the general idea|Locate one explicit detail|Order three events|Show evidence for an answer"),
    "EN03 OA 04": _p("Strategies for listening comprehension", "attend to gesture, image and familiar words", "predict, connect, image, key word, purpose, check, revise", "a short unfamiliar text with title, images and intentional pauses", "treat a prediction as final or use only one clue", "Predict from context|Connect with prior knowledge|Use images without guessing alone|Focus on key words|Check and revise a prediction"),
    "EN03 OA 05": _p("Responding personally and creatively to listening", "show comprehension through action, drawing or a short phrase", "preference, feeling, opinion, connection, drawing, mime, dramatization", "safe fictional choices that never require private disclosure", "repeat I like it without referring to the text", "Draw a supported response|Respond through mime and action|Dramatize a key moment|Express a preference with a reason|Connect to a safe fictional experience"),
    "EN03 OA 06": _p("Reading short literary and functional texts", "recognize familiar words and use images", "story, rhyme, chant, greeting card, instruction, information, action", "large-print short texts with clear layout and optional read-aloud access", "decode aloud fluently without understanding meaning", "Recognize the text type|Identify the general idea|Find characters and actions|Follow written instructions|Transfer to a new short text"),
    "EN03 OA 07": _p("Reading about familiar cross-curricular topics", "read labels, captions and patterned sentences", "school, wildlife, home, geometry, jobs, city, food, celebration", "brief illustrated texts that represent varied homes, jobs and celebrations", "assume every family or culture matches one example", "Read about school and home|Read about animals and shapes|Read about occupations and places|Read about food and celebrations|Compare information without stereotyping"),
    "EN03 OA 08": _p("Strategies for reading comprehension", "preview title and pictures before reading", "predict, prior knowledge, image, reread, read aloud, confirm, repair", "one text read in passes for prediction, detail and confirmation", "reread mechanically without naming what needs clarification", "Preview and predict|Connect prior knowledge cautiously|Coordinate words and images|Reread for a specific question|Choose and explain a repair strategy"),
    "EN03 OA 09": _p("Responding to reading through multiple modes", "identify one idea from a short text", "illustration, figure, dramatization, word, phrase, sentence, preference", "a choice of oral, visual, written or dramatic response modes", "decorate a response without showing textual understanding", "Illustrate one supported idea|Build a figure or scene|Dramatize with textual evidence|Write a word or phrase response|Express and support an opinion"),
    "EN03 OA 10": _p("English sounds through chants, rhymes and dialogues", "repeat short chunks with rhythm and intelligibility", "sound, mouth position, voice, vibration, /w/, /th/, /s/, /z/", "teacher model and brief authorized recordings, never accent rankings", "equate pronunciation with intelligence or demand imitation of one accent", "Notice and produce /w/|Explore /th/ safely|Contrast /s/ and /z/|Use sounds in a chant|Perform a brief intelligible dialogue"),
    "EN03 OA 11": _p("Brief classroom interaction and presentation", "use memorized chunks with gesture and image support", "question, answer, request, turn, clarification, presentation, follow-up", "objects, information-gap cards and fictional profiles without personal data", "recite a script without listening or penalize pauses and self-correction", "Exchange classroom requests|Introduce a fictional person|Ask for a missing word|Give a brief supported presentation|Adapt to a follow-up question"),
    "EN03 OA 12": _p("Supported oral expression for familiar meanings", "produce words and short patterned sentences", "ability, quantity, description, prohibition, request, location, present action", "picture scenes and fictional characters; no address, phone or sensitive data", "require long sentences before chunks become meaningful", "Share safe fictional information|Express ability and quantity|Describe and state a prohibition|Request and locate an item|Describe actions happening now"),
    "EN03 OA 13": _p("Model-supported English writing", "copy meaningful chunks and complete a pattern", "copy, complete, model, word order, capital, space, period", "sentence models paired with images and a focused checklist", "copy letter by letter without reading or choose by blank length", "Copy by meaningful chunks|Complete from a word bank|Transform one element of a model|Write and check a supported sentence"),
    "EN03 OA 14": _p("Image-supported writing for familiar topics", "write labels and patterned phrases", "label, sentence, animal, action, occupation, location, feeling, quantity", "image sequences, word banks and sentence frames that can be faded", "list words without communicating the requested meaning", "Identify and label precisely|Write feelings and quantities|Describe locations|Describe visible actions|Create and revise a mini information card"),
}


LC = {
    "LC03 OA LF01": _p("Comprensión de textos orales en lengua indígena", "escuchar fuentes comunitarias breves con atención", "oralidad, relato, secuencia, conocimiento, emoción, memoria, fuente", "registro autorizado o participación de una persona portadora de saberes", "traducir mecánicamente o tratar un relato como material anónimo", "Situar voz, pueblo y contexto|Escuchar una primera vez para disfrutar|Reconstruir secuencia y relaciones|Conectar sin forzar experiencia personal|Devolver una comprensión a la fuente"),
    "LC03 OA LF02": _p("Comunicación oral pertinente en lengua indígena", "reconocer expresiones validadas y su situación de uso", "saludo, diálogo, situación, interlocutor, pronunciación, variante, contexto", "modelos aportados por educador tradicional o fuente comunitaria validada", "inventar lengua o usar expresiones fuera de su contexto", "Reconocer situación e interlocutor|Ensayar palabras y expresiones validadas|Sostener un diálogo breve|Comunicar con respeto a variantes"),
    "LC03 OA LF03": _p("Comprensión de textos escritos en lengua indígena", "relacionar oralidad, imagen y escritura", "texto, tema, información, emoción, grafía, variante, fuente", "texto breve autorizado con información de procedencia y apoyo oral", "suponer una ortografía única o separar el texto de su cultura", "Anticipar desde contexto y fuente|Leer con apoyo oral y visual|Relacionar información y saberes|Responder reconociendo emoción y límites|Contrastar dos pistas del texto"),
    "LC03 OA LF04": _p("Construcción de oraciones en lengua indígena", "copiar y reconocer palabras desde modelos validados", "palabra, oración, nombrar, caracterizar, grafía, revisión, variante", "banco lingüístico validado por la comunidad o educador tradicional", "inventar grafías o corregir variantes como errores", "Observar cómo se nombra|Caracterizar con expresiones pertinentes|Construir una oración desde modelo|Revisar significado, grafía y contexto"),
    "LC03 OA LF05": _p("Creación digital en lengua indígena", "usar recursos tecnológicos básicos con autoría y permiso", "audio, video, texto, creación, autoría, permiso, archivo", "herramienta local y recursos autorizados, con alternativa no digital equivalente", "publicar voces, imágenes o saberes sin consentimiento", "Definir mensaje, audiencia y resguardo|Seleccionar recursos con permiso|Crear un registro breve|Revisar lengua, autoría y acceso"),
    "LC03 OA LR01": _p("Textos orales y expresiones en revitalización lingüística", "escuchar relatos en castellano y lengua indígena sin evaluar identidad", "relato, expresión, memoria, revitalización, secuencia, fuente, comunidad", "voz comunitaria o registro autorizado con expresiones contextualizadas", "usar palabras aisladas como adorno o medir pertenencia por fluidez", "Activar memoria lingüística sin examen|Escuchar relato y expresiones|Comprender secuencia y significado|Relacionar conocimientos con opción ficticia|Crear una devolución que aporta a revitalizar"),
    "LC03 OA LR02": _p("Comunicación oral con expresiones en revitalización", "reconocer palabras disponibles y pedir apoyo", "idea, sentimiento, diálogo, expresión, situación, pronunciación, apoyo", "guiones flexibles validados para situaciones personales, familiares o comunitarias ficticias", "obligar a revelar emociones o improvisar traducciones", "Elegir una situación comunicativa|Aprender expresiones desde la fuente|Construir una intervención breve|Interactuar escuchando al otro|Revisar pertinencia y pronunciación"),
    "LC03 OA LR03": _p("Comprensión textual con expresiones culturalmente significativas", "usar imágenes, oralidad y palabras conocidas", "texto, expresión, significado, conocimiento, emoción, contexto, fuente", "texto breve de procedencia identificada y glosario autorizado", "reemplazar el contexto por una traducción única", "Reconocer fuente y propósito|Localizar expresiones significativas|Relacionar información interna|Responder sin exigir vivencias|Explicar significado dentro del texto"),
    "LC03 OA LR04": _p("Escritura de palabras y frases en revitalización", "copiar palabras por unidades con significado", "palabra, frase, nombrar, caracterizar, modelo, variante, revisión", "modelos comunitarios que reconocen variantes gráficas", "inventar lengua o normalizar una variante sin autoridad", "Observar modelos y variantes|Escribir palabras para nombrar|Construir una frase simple|Revisar con una fuente válida"),
    "LC03 OA LR05": _p("Creaciones digitales para revitalización lingüística", "registrar palabras con fuente y permiso", "TIC, audio, video, texto, revitalización, autoría, consentimiento", "recurso local con control de acceso y alternativa analógica", "creer que publicar siempre revitaliza o reemplaza a hablantes", "Acordar propósito y límites|Seleccionar expresiones autorizadas|Diseñar un recurso pequeño|Crear sin reemplazar voces|Devolver, atribuir y controlar acceso"),
    "LC03 OA LS01": _p("Textos orales y palabras en sensibilización lingüística", "escuchar con respeto sin exigir repetición", "tradición, palabra, significado, pueblo, territorio, fuente, respeto", "relato autorizado presentado con pueblo, territorio y portador", "imitar sonidos o tratar palabras como curiosidad exótica", "Acercarse sin apropiarse|Situar relato y fuente|Reconocer palabras significativas|Relacionar saberes sin generalizar|Comunicar lo aprendido con atribución"),
    "LC03 OA LS02": _p("Comunicación oral inicial en sensibilización", "usar castellano respetuoso y escuchar palabras validadas", "idea, sentimiento, palabra, diálogo, situación, consentimiento, contexto", "situaciones ficticias y modelos aportados por una fuente pertinente", "forzar repetición o evaluar identidad mediante pronunciación", "Elegir una situación segura|Escuchar palabras y significado|Preparar una idea o sentimiento ficticio|Dialogar con apoyo|Revisar respeto y contexto"),
    "LC03 OA LS03": _p("Comprensión de textos con palabras culturalmente significativas", "reconocer título, imagen y tema", "texto, palabra, significado, contexto, emoción, fuente, evidencia", "texto breve autorizado en castellano con palabras contextualizadas", "usar la palabra como decoración o atribuir significado sin fuente", "Identificar procedencia|Anticipar sin estereotipos|Localizar palabras y pistas|Relacionar información y respuesta|Explicar con evidencia y límites"),
    "LC03 OA LS04": _p("Escritura inicial de palabras culturalmente significativas", "copiar desde un modelo visible", "palabra, nombrar, caracterizar, grafía, variante, modelo, fuente", "banco de palabras autorizado con significado y contexto", "inventar lengua, símbolos o una ortografía", "Observar modelo y procedencia|Escribir para nombrar|Escribir para caracterizar|Revisar sin jerarquizar variantes"),
    "LC03 OA LS05": _p("Creaciones digitales de sensibilización cultural y lingüística", "usar imágenes, audio o texto respetando autoría", "recurso digital, palabra, expresión, cultura, autoría, permiso, acceso", "colección autorizada y herramienta sin publicación automática", "extraer prácticas de contexto o compartir material restringido", "Definir propósito de sensibilización|Examinar autoría y permiso|Seleccionar palabras contextualizadas|Crear sin apropiarse|Revisar atribución y audiencia"),
    "LC03 OA 06": _p("Territorio, espiritualidad y vida comunitaria", "ubicar pueblo, territorio y fuente", "territorio, espiritualidad, festividad, producción, comunidad, relación, memoria", "testimonio o material comunitario autorizado que muestra relaciones situadas", "reducir territorio a mapa o generalizar una relación a todos los pueblos", "Situar territorio y voces|Relacionar territorio y vida espiritual|Relacionar festividades y producción|Comunicar conexiones y límites"),
    "LC03 OA 07": _p("Historia indígena, presente y futuro", "distinguir pasado, presente y fuente", "historia, memoria, continuidad, cambio, presente, futuro, testimonio", "dos fuentes pertinentes que permiten reconocer voces y temporalidades", "presentar al pueblo sólo en pasado o una voz como totalidad", "Formular una pregunta histórica|Leer memorias y fuentes|Reconocer cambios y continuidades|Vincular historia, presente y futuro"),
    "LC03 OA 08": _p("Aportes vivos de culturas y visiones indígenas", "reconocer diversidad cultural actual", "cultura, visión de mundo, aporte, localidad, país, continuidad, intercambio", "casos actuales documentados y atribuidos a pueblos y comunidades específicos", "folclorizar, hablar por otros o exigir identidad al estudiante", "Reconocer culturas vivas|Examinar un aporte situado|Relacionar localidad y país|Valorar sin apropiarse ni homogeneizar"),
    "LC03 OA 09": _p("Nociones indígenas de tiempo y espacio", "comparar formas de organizar experiencias sin jerarquizarlas", "tiempo, espacio, ciclo, orientación, acontecimiento, territorio, perspectiva", "fuente comunitaria sobre una concepción específica, no una síntesis panindígena", "traducir nociones a categorías occidentales como equivalencias exactas", "Situar la concepción estudiada|Explorar una noción de tiempo|Explorar una noción de espacio|Comparar reconociendo límites"),
    "LC03 OA 10": _p("Arte y técnicas ancestrales en diálogo con la naturaleza", "observar materiales, procesos y condiciones de uso", "arte, técnica ancestral, naturaleza, diálogo, material, permiso, transmisión", "demostración autorizada o registro atribuido, sin copiar diseños restringidos", "tratar la técnica como manualidad sin significado ni autoridad cultural", "Reconocer origen y portadores|Relacionar material, técnica y naturaleza|Analizar decisiones y resguardos|Responder creativamente sin copiar"),
    "LC03 OA 11": _p("Normas en eventos socioculturales y espirituales", "distinguir evento, rol y acuerdo", "norma, evento, espiritualidad, significado, participación, resguardo, consentimiento", "descripción comunitaria autorizada; nunca se simula una ceremonia", "convertir normas en exotismo o representar prácticas restringidas", "Situar evento y significado|Reconocer roles y normas|Analizar participación y resguardos|Comunicar sin reproducir lo restringido"),
    "LC03 OA 12": _p("Vida en armonía e interdependencia", "reconocer relaciones entre seres y entorno", "armonía, interdependencia, naturaleza, ser humano, reciprocidad, cuidado, equilibrio", "caso documentado que muestra decisiones y consecuencias, no una consigna abstracta", "idealizar a todos los pueblos o usar armonía como ausencia de conflicto", "Reconocer relaciones concretas|Analizar reciprocidad y consecuencias|Comparar decisiones de cuidado|Proponer una acción situada"),
    "LC03 OA 13": _p("Técnicas productivas ancestrales y vida comunitaria", "seguir procesos y cuidar materiales", "técnica, producción, ciclo, territorio, familia, comunidad, autorización", "técnica expresamente compartida para enseñanza por fuente competente", "reproducir técnicas restringidas o separarlas de territorio y relaciones", "Identificar propósito, fuente y permiso|Observar etapas y conocimientos|Practicar una versión autorizada|Relacionar producción y comunidad"),
    "LC03 OA 14": _p("Patrimonio cultural de comunidad, territorio y pueblo", "distinguir patrimonio, objeto y práctica viva", "patrimonio, comida, ceremonia, sitio, medicina, historia, protección", "casos autorizados con condiciones de acceso y atribución diferenciadas", "suponer que todo patrimonio puede recrearse o publicarse", "Reconocer manifestaciones diversas|Investigar procedencia y significado|Distinguir acceso público y restringido|Recrear sólo lo autorizado|Diseñar una acción de valoración y cuidado"),
    "LC03 OA 15": _p("Ciencia indígena en relación con naturaleza y cosmos", "observar ciclos y reconocer fuentes de conocimiento", "ciencia, observación, naturaleza, cosmos, conocimiento, evidencia, transmisión", "explicación situada por portadores o materiales oficiales comunitariamente pertinentes", "oponer ciencia indígena y ciencia escolar como bloques homogéneos", "Situar pregunta y perspectiva|Examinar observación y conocimiento|Relacionar naturaleza y cosmos|Comparar sin jerarquizar ni fusionar|Comunicar alcances de cada fuente"),
    "LC03 OA 16": _p("Creación con sonoridad y visualidad indígenas", "escuchar y observar expresiones atribuidas", "sonoridad, visualidad, creación, naturaleza, relación, autoría, símbolo", "elementos autorizados para enseñanza y alternativas de respuesta sin imitación", "copiar patrones, símbolos o sonidos restringidos como decoración", "Reconocer procedencia y resguardos|Explorar cualidades sin copiar símbolos|Crear una respuesta propia y situada|Explicar decisiones, relaciones y límites"),
}


TABLES = {"AR": AR, "EF": EF, "EN": EN, "LC": LC}
SLUGS = {
    "AR": "artes-visuales",
    "EF": "educacion-fisica-salud",
    "EN": "ingles-propuesta",
    "LC": "lengua-cultura-pueblos-originarios-ancestrales",
}


def _attitude(code: str, index: int, goal: str) -> list[dict[str, str]]:
    pool = ATTITUDES[code[:2]]
    seed = sum(ord(char) for char in code.rsplit(" ", 1)[-1])
    attitude_code, description = pool[(seed + index * 2) % len(pool)]
    return [{
        "code": attitude_code,
        "type": "Actitud",
        "application": f"Se promueve {description} durante «{goal}» mediante una acción observable y revisable; no se califica personalidad, cuerpo, acento, identidad ni origen.",
    }]


def _lesson(code: str, index: int, profile: dict) -> dict:
    prefix = code[:2]
    focus = profile["focuses"][index]
    topic = profile["topic"]
    anchor = profile["anchor"]
    misconception = profile["misconception"]
    goal = f"desarrollaré «{focus.lower()}» y mostraré una decisión propia con evidencia"

    if prefix == "AR":
        opening = f"Presenta {anchor} para «{focus.lower()}». Cada estudiante registra dos detalles y una posibilidad expresiva antes de ver cualquier demostración."
        model = f"Realiza una prueba parcial para {focus.lower()}, verbalizando cómo color, forma, textura, material o encuadre cambia el efecto. Conserva visible un intento que no funcionó y contrasta «{misconception}»."
        guided = f"En estaciones, exploran una variable de {focus.lower()}; describen efectos sin imponer una solución única y el autor elige qué incorporar."
        independent = f"Crea una respuesta visual nueva para «{focus.lower()}» sin copiar el referente ni el modelado; documenta una elección, una revisión y el efecto buscado."
        ticket = f"Muestra una decisión de «{focus.lower()}» y explica qué detalle del referente, criterio o prueba la sostiene."
        materials = f"{anchor}; papeles, lápices, pinturas o materiales reutilizables limpios según la experiencia; herramientas revisadas y protección de superficies."
        support = "Ofrece formatos y herramientas de distinta manipulación, alto contraste, demostración técnica breve y respuesta oral; nunca completa la obra ni entrega una plantilla estética."
        extension = "Cambia material, escala, audiencia o punto de vista y pide conservar la intención mediante otra decisión visual."
        evidence = f"Trabajo visual propio de «{focus.lower()}», registro de proceso y explicación con lenguaje visual."
        coordination = "El docente conduce creación y apreciación; educación diferencial acuerda acceso motor, visual o comunicativo sin ejecutar la obra, y mediación cultural verifica atribución cuando corresponde."
    elif prefix == "EF":
        opening = f"Demuestra a velocidad de observación una situación de «{focus.lower()}» usando {anchor}. El grupo identifica meta, espacio, señal de detención y condición de seguridad."
        model = f"Ejecuta lentamente {focus.lower()} y nombra mirada, apoyos, trayectoria, fuerza y regulación. Contrasta control con rapidez y aborda «{misconception}» sin presentar un cuerpo ideal."
        guided = f"Practican «{focus.lower()}» en estaciones breves, sin eliminación, con distancia suficiente y variantes equivalentes; la retroalimentación se refiere a control y seguridad."
        independent = f"Resuelve una variante nueva de «{focus.lower()}»; elige nivel, distancia, implemento o ritmo, ejecútala con seguridad y ajusta desde su propia evidencia."
        ticket = f"Demuestra o representa la decisión usada en «{focus.lower()}» y nombra una señal corporal, espacial o reglamentaria que guio el ajuste."
        materials = f"{anchor}; conos, marcas y tarjetas de variantes; agua y protocolo institucional disponibles según la actividad."
        support = "Ajusta espacio, altura, distancia, velocidad, implemento, contacto o rol; conserva la habilidad y ofrece ensayo privado sin comparar cuerpos ni rendimiento."
        extension = "Combina otra habilidad o cambia dirección, ritmo, oposición o regla manteniendo control, acceso y seguridad."
        evidence = f"Desempeño individual de «{focus.lower()}» con control, elección de variante y autoexplicación del ajuste."
        coordination = "El docente conduce progresión y seguridad; educación diferencial acuerda variantes y señales. Salud escolar actúa sólo mediante protocolo ante señales de alerta, sin diagnosticar durante la clase."
    elif prefix == "EN":
        opening = f"Presenta una vez {anchor} para «{focus.lower()}», con gesto u objeto y sin traducir completo. Cada estudiante responde mediante acción, elección, marca o chunk breve."
        model = f"Think aloud with accessible English and Spanish only when needed: model {focus.lower()} and point to the sound, word, image or pattern that carries meaning. Contrast the misconception: {misconception}."
        guided = f"Practice «{focus.lower()}» through echo, information gap, sorting or short turns; change one meaningful detail so students listen, read or compose instead of reciting."
        independent = f"Complete a new and culturally safe task for «{focus.lower()}»; select language support, communicate meaning and revise after checking the input."
        ticket = f"For «{focus.lower()}», give an action, choice, spoken chunk or short written response and point to the clue that supports it."
        materials = f"{anchor}; visible word bank, picture cards and optional audio replay; no account or personal information required."
        support = "Keep images and chunks visible, allow choral and paired rehearsal, reduce length and provide wait time; do not penalize accent, initial language mixing or self-correction."
        extension = "Change speaker, audience, quantity, place or action and adapt the message to the new communicative purpose."
        evidence = f"Comprehensible oral, written, visual or embodied response for «{focus.lower()}» linked to a word, chunk or clue in the input."
        coordination = "El docente modela inglés comprensible; educación diferencial facilita acceso auditivo, visual, motor o de respuesta sin sustituir la intención comunicativa."
    else:
        opening = f"Para «{focus.lower()}», ubica pueblo, territorio, {anchor} y autorización antes de presentar el recurso. Declara qué puede compartirse y qué requiere resguardo."
        model = f"Modela {focus.lower()} sólo con educador tradicional o fuente comunitaria pertinente: no inventa lengua, pronunciación, grafías, símbolos ni explicaciones espirituales. Contrasta «{misconception}»."
        guided = f"Con educador tradicional o fuente comunitaria cuando corresponde, analizan «{focus.lower()}», reconocen variantes y distinguen aprender, recrear, reproducir y apropiarse."
        independent = f"Elabora una comprensión o respuesta propia para «{focus.lower()}» sin apropiarse de voces ni prácticas; identifica pueblo, territorio, fuente, permiso y límites de lo afirmado."
        ticket = f"Sobre «{focus.lower()}», comunica una relación aprendida, atribuye la fuente comunitaria y nombra algo que no corresponde inventar, divulgar o generalizar."
        materials = f"{anchor}; registro autorizado, ficha de procedencia y alternativa oral, visual o escrita. No se usan recursos comunitarios sin permiso."
        support = "Permite escuchar sin repetir, responder en castellano o mediante imagen y usar modelos validados; nunca usa desconocimiento lingüístico para evaluar identidad o pertenencia."
        extension = "Compara dos fuentes autorizadas o variantes sin jerarquizarlas y explica qué territorio, situación o autoridad hace pertinente cada una."
        evidence = f"Comprensión o producción situada sobre «{focus.lower()}» que atribuye fuente y respeta límites de uso, autoría, acceso e identidad."
        coordination = "El docente no suplanta saberes comunitarios: coordina con educador tradicional, autoridad cultural o fuente comunitaria pertinente y detiene la actividad si falta validación."

    return {
        "title": focus,
        "purpose": f"Desarrollar {topic.lower()} mediante «{focus.lower()}», con una experiencia disciplinar específica, segura y revisable.",
        "goal": f"Hoy {goal}.",
        "opening": opening,
        "model": model,
        "guided": guided,
        "independent": independent,
        "ticket": ticket,
        "materials": materials,
        "support": support,
        "extension": extension,
        "evidence": evidence,
        "criteria": ["responde al foco específico de la clase", "toma una decisión disciplinar pertinente y segura", "explica o localiza evidencia y reconoce límites"],
        "next_step": "Avanza cuando decisión, evidencia y explicación coinciden; si no, cambia el acceso o modela otro caso y vuelve a recoger evidencia sin etiquetar al estudiante.",
        "short_version": "Conserva situación específica, modelado, práctica guiada, evidencia individual y cierre; reduce cantidad o turnos, no el criterio disciplinar.",
        "home_task": "Observa, practica o registra una versión breve y segura con recursos disponibles. No requiere compras, internet, datos personales ni exposición familiar, corporal o cultural.",
        "complementary": [
            "Recuperación: aísla una decisión o pista y vuelve luego a la tarea completa.",
            f"Análisis de error: revisa un caso ficticio que muestra esta confusión: {misconception}.",
            "Transferencia: cambia contexto, material, interlocutor, espacio o fuente y explica qué debe adaptarse.",
        ],
        "difficulty_actions": [
            {"signal": "Repite o imita sin tomar una decisión", "action": "Ofrece dos alternativas y pide elegir una según el propósito específico.", "check": "Puede mostrar qué eligió, para qué y con qué evidencia."},
            {"signal": misconception.capitalize(), "action": support, "check": "Resuelve un caso nuevo sin repetir la confusión."},
            {"signal": "Se inhibe, queda expuesto o no accede al formato", "action": "Reduce exposición y ofrece una vía equivalente de participación, manteniendo el objetivo.", "check": "Produce evidencia propia mediante una vía accesible y segura."},
        ],
        "specialist_coordination": coordination,
        "transversal": _attitude(code, index, goal),
    }


def build_sequence(code: str) -> dict | None:
    prefix = code[:2]
    profile = TABLES.get(prefix, {}).get(code)
    if not profile:
        return None
    slug = SLUGS[prefix]
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": f"{profile['topic']} se desarrolla mediante experiencias propias de la disciplina. La secuencia parte de {profile['prior']} y enfrenta la confusión «{profile['misconception']}».",
        "prerequisites": profile["prior"],
        "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"Eje oficial · organización interna en {len(profile['focuses'])} clases"],
            "unit_origin": "Organización interna derivada del eje y del OA; no se presenta como unidad oficial del programa de estudio.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del OA oficial",
            "source": f"https://www.curriculumnacional.cl/curriculum/1o-6o-basico/{slug}/3-basico/{code.lower().replace(' ', '-')}",
        },
        "lessons": [_lesson(code, index, profile) for index in range(len(profile["focuses"]))],
    }


def build_transversal_integration(item: dict) -> dict:
    code = item["oa_code"]
    prefix = code.split("03", 1)[0].removeprefix("de Actitud ")
    description = item["oa_text"].split("Unidad de Currículum", 1)[0].strip().rstrip(".")
    contexts = {
        "AR": ("una experiencia de creación o apreciación visual", "decisión visual o de proceso"),
        "EF": ("una tarea motriz segura y accesible", "decisión de movimiento, regulación o colaboración"),
        "EN": ("una interacción comprensible en inglés", "decisión comunicativa apoyada por lenguaje"),
        "LC": ("un aprendizaje situado de lengua o cultura", "decisión respetuosa sobre fuente, uso y comunicación"),
    }
    context, decision = contexts[prefix]
    lessons = []
    for index, (phase, _) in enumerate(item["phases"]):
        title = f"{phase}: {description.lower()} en acción {index + 1}"
        lessons.append({
            "title": title,
            "purpose": f"Integrar «{description}» dentro de {context}, sin convertir la actitud en charla aislada ni rasgo personal.",
            "goal": f"Hoy haré visible una {decision} y explicaré cómo aportó al aprendizaje.",
            "opening": f"Contrasta dos respuestas ficticias a {context}: una sólo nombra la actitud y otra la muestra mediante una acción. Localizan evidencia específica para «{title.lower()}».",
            "model": f"Modela una {decision} que manifiesta «{description}» y señala su efecto concreto en el trabajo, la seguridad, la comunicación o la revisión.",
            "guided": f"Realizan una tarea breve de «{title.lower()}», marcan una acción observable y reciben retroalimentación sobre esa acción, nunca sobre cuerpo, talento, acento, personalidad, identidad u origen.",
            "independent": f"Cada estudiante completa una nueva versión de {context}, identifica su decisión y explica cómo «{description.lower()}» influyó en el resultado.",
            "ticket": f"En «{title.lower()}», señala una evidencia propia de la actitud y completa: esta acción ayudó porque…",
            "materials": "Materiales del OA disciplinar anfitrión y una tarjeta que expresa la actitud como acción observable.",
            "support": "Ofrece dos ejemplos, frase inicial y vía equivalente de participación; conserva la decisión disciplinar y los resguardos culturales, físicos o comunicativos.",
            "extension": "Transfiere la actitud a otro OA de la asignatura y compara cómo cambia su manifestación concreta.",
            "evidence": f"Producción o desempeño disciplinar de «{title.lower()}» con acción y explicación atribuibles al estudiante.",
            "criteria": ["resuelve una tarea disciplinar pertinente", "hace visible la actitud mediante una acción", "explica su efecto sin etiquetas personales"],
            "next_step": "Integra nuevamente si depende del apoyo; cambia el contexto cuando la acción aparece con autonomía.",
            "short_version": "Conserva tarea, acción observable, evidencia individual y cierre; reduce repetición, no integración.",
            "home_task": "Explica o dibuja un ejemplo seguro de la actitud en una actividad de la asignatura; no requiere compras, internet ni exposición personal o cultural.",
            "complementary": ["Clasificar evidencia y no evidencia de la actitud.", "Revisar un caso que confunde actitud con obediencia, talento o identidad.", "Transferir la acción a otro eje."],
            "difficulty_actions": [
                {"signal": "Nombra la actitud, pero no la aplica", "action": "Pide señalar una decisión concreta dentro de la tarea.", "check": "La evidencia queda localizada."},
                {"signal": "Evalúa rasgos personales o identitarios", "action": "Reformula como acción modificable y vinculada al OA.", "check": "La retroalimentación describe qué hizo y qué puede probar."},
                {"signal": "La actitud desplaza el contenido", "action": "Recupera el criterio disciplinar y usa la actitud como medio.", "check": "El ticket demuestra contenido e integración."},
            ],
            "specialist_coordination": "El docente mantiene el OA disciplinar como foco; profesionales o educadores pertinentes acuerdan una barrera, variante y evidencia sin sustituir la decisión del estudiante.",
        })
    return {"generated_for": "3-basico", "lessons": lessons}
