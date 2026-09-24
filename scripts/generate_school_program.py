"""Build the curriculum source, public catalog, and static lesson pages."""
import html
import json
import shutil
from pathlib import Path
from urllib.parse import quote
from build_school_curriculum import ROOT,SNAPSHOT,CURRICULUM,slugify,topic_from
from grade_one_lessons import build_grade_one_lessons
DEVELOPED=ROOT/"content"/"developed-lessons.json"
PH=[("Conectar y diagnosticar","recuperar ideas previas y detectar barreras"),("Comprender y modelar","explicar con ejemplo y contraejemplo, haciendo visible el pensamiento experto"),("Practicar con apoyo","ensayar con andamiaje y retroalimentación inmediata"),("Aplicar con autonomía","resolver una situación nueva y justificar decisiones"),("Contrastar y profundizar","comparar alternativas y examinar casos límite"),("Transferir al contexto","usar el aprendizaje en un problema situado en Chile"),("Demostrar y retroalimentar","producir evidencia final y decidir el paso siguiente")]
def dose(text,slug,reads):
 t=text.lower();n=4
 if len(text)>260 or t.count(";")>=2:n+=1
 if any(v in t for v in ("investigar","crear","producir","diseñar","evaluar","analizar","argumentar","interpretar")):n+=1
 if reads or ("leng" in slug and any(v in t for v in ("leer","escribir","obra","texto"))):n+=1
 ix={4:[0,1,3,6],5:[0,1,2,3,6],6:[0,1,2,3,4,6],7:list(range(7))}
 return [PH[i] for i in ix[min(n,7)]]
def discipline(slug):
 if "leng" in slug:return ("propósito, evidencia, inferencia, estructura, audiencia y revisión","interpretación o producción comunicativa fundamentada","resumir en vez de interpretar; opinar sin evidencia")
 if "matematica" in slug:return ("datos, representación, estrategia, estimación y verificación","solución representada, explicada y comprobada","aplicar reglas sin reconocer cuándo sirven; aceptar resultados sin estimarlos")
 if "ciencia" in slug:return ("pregunta, variable, observación, evidencia, patrón, modelo y limitación","explicación o indagación con evidencia","tratar opiniones como evidencia; cambiar varias variables")
 if "historia" in slug:return ("temporalidad, territorio, causa, continuidad, fuente y perspectiva","explicación sustentada en fuentes","juzgar el pasado solo desde el presente; tratar una fuente como verdad completa")
 if "ingles" in slug:return ("purpose, audience, key words, meaning, interaction y revision","desempeño comunicativo comprensible","traducir literalmente; esperar precisión total antes de comunicarse")
 if any(x in slug for x in ("artes-visuales","danza","teatro")):return ("elementos, técnica, materialidad, intención, contexto, proceso y apreciación","creación artística acompañada de decisiones explicadas","copiar un modelo sin tomar decisiones; confundir preferencia con apreciación fundamentada")
 if "musica" in slug:return ("pulso, ritmo, altura, timbre, intensidad, forma, interpretación y escucha","interpretación, creación o apreciación musical con criterios audibles","confundir pulso con ritmo; describir solo gustos sin referirse a lo escuchado")
 if "educacion-fisica" in slug:return ("habilidad motriz, control, coordinación, intensidad, seguridad, estrategia y autocuidado","desempeño motriz seguro observado con una pauta","priorizar velocidad sobre control; omitir calentamiento, hidratación o reglas de seguridad")
 if "tecnologia" in slug:return ("necesidad, usuario, criterio, restricción, diseño, prototipo, prueba e impacto","solución tecnológica justificada y probada contra criterios","construir antes de definir el problema; evaluar solo por apariencia")
 if "orientacion" in slug:return ("bienestar, emoción, decisión, vínculo, límite, responsabilidad y red de apoyo","reflexión o decisión personal fundada en un caso seguro","forzar exposición personal; confundir consejo con decisión responsable")
 if any(x in slug for x in ("filosofia","mundo-global","ciudadana","ambiente","bienestar","seguridad-prevencion","chile-region")):return ("pregunta, concepto, argumento, evidencia, supuesto, perspectiva y consecuencia","argumento o deliberación fundamentada","afirmar sin razones; atacar a la persona en vez de examinar el argumento")
 return ("concepto, relación, criterio, evidencia, aplicación y revisión","desempeño observable alineado al OA","memorizar sin comprender; completar sin demostrar el aprendizaje")
def cov(slug,order):
 if "ingles-propuesta" in slug:return "propuesta-mineduc"
 if "pueblos-originarios" in slug or "lengua-indigena" in slug:return "segun-contexto-y-normativa"
 if order>=11 and slug in {"artes-visuales","musica","danza","teatro"}:return "electivo-de-artes"
 if order>=11 and slug.startswith("educacion-fisica-salud-"):return "electivo-de-educacion-fisica"
 if order>=11 and slug in {"ambiente-sostenibilidad","bienestar-salud","chile-region-latinoamericana","mundo-global","seguridad-prevencion-autocuidado","tecnologia-sociedad"}:return "modulo-electivo"
 return "formacion-general-comun"
def developed_block(lesson):
 complementary="\n".join(f"- {activity}" for activity in lesson.get("complementary", []))
 difficulties="\n".join(f"| {row['signal']} | {row['action']} | {row['check']} |" for row in lesson.get("difficulty_actions", []))
 return f"""**Propósito docente:** {lesson['purpose']}

**Meta para estudiantes:** {lesson['goal']}

| Momento | Tiempo | Acción docente y experiencia |
|---|---:|---|
| Inicio | 10 min | {lesson['opening']} |
| Modelado | 20 min | {lesson['model']} |
| Práctica guiada | 25 min | {lesson['guided']} |
| Desempeño individual | 25 min | {lesson['independent']} |
| Cierre | 10 min | {lesson['ticket']} |

**Materiales y preparación:** {lesson['materials']}

**Apoyo en el mismo OA:** {lesson['support']}

**Profundización:** {lesson['extension']}

**Evidencia:** {lesson['evidence']}

**Criterios de éxito:** {'; '.join(lesson['criteria'])}.

**Decisión posterior:** {lesson['next_step']}

**Adaptación a 45 minutos:** {lesson['short_version']}

**Tarea breve y flexible:** {lesson.get('home_task', 'Consolida el aprendizaje con una evidencia breve que no requiera internet ni materiales comprados.')}

**Actividades complementarias (opcionales):**
{complementary or '- Recuperación, práctica adicional y profundización según la evidencia recogida.'}

**Control de dificultades en el aula**

| Dificultad observable | Acción inmediata | Cómo comprobar si funcionó |
|---|---|---|
{difficulties or '| No inicia o se desconecta | Reduce la consigna a un paso, modela un ejemplo distinto y ofrece una vía de respuesta accesible. | Inicia y produce una evidencia propia. |'}

**Coordinación de roles profesionales:** {lesson.get('specialist_coordination', 'El docente responsable conserva la conducción del OA y acuerda con los profesionales de apoyo una barrera, una acción y una evidencia, sin delegar ni diagnosticar durante la clase.')}
"""

def plan(item):
 vocab,product,errors=discipline(item["subject_slug"]);parts=[]
 for i,(code,(title,focus)) in enumerate(zip(item["codes"],item["phases"]),1):
  if item.get("developed"):
   lesson=item["developed"]["lessons"][i-1]
   parts.append(f"### Clase {i} de {len(item['phases'])}: {lesson['title']} {{#{code.lower()}}}\n"+developed_block(lesson))
   continue
  oa_excerpt=item["oa_text"].rstrip(".")
  parts.append(f"""### Clase {i} de {len(item['phases'])}: {title} {{#{code.lower()}}}
**Foco:** {focus}. **Meta para estudiantes:** hoy voy a trabajar «{item['topic'].lower()}» y demostrarlo mediante {product}.

| Momento | Tiempo | Acción docente y experiencia |
|---|---:|---|
| Inicio | 10 min | Presenta una situación breve vinculada a **{item['topic'].lower()}**. Recupera qué saben y registra una respuesta inicial de todo el curso. |
| Explicación | 20 min | Modela cómo abordar «{oa_excerpt}». Hace visible el uso de {vocab} y contrasta un ejemplo logrado con el error: {errors}. |
| Práctica guiada | 25 min | Construyen juntos {product}. Pregunta: “¿qué evidencia demuestra el aprendizaje del OA?” Respuesta esperada: una decisión explicada con vocabulario de la asignatura. |
| Desempeño individual | 25 min | Cada estudiante produce {product} sobre **{item['topic'].lower()}**, explica una decisión y revisa su trabajo con los criterios. |
| Cierre | 10 min | Ticket: nombra una decisión, aporta evidencia y corrige el error previsible. Clasifica: logrado; próximo con apoyo; requiere otra explicación. |

**Apoyo en el mismo OA:** ejemplo resuelto, pasos visibles, vocabulario anticipado, ensayo oral y retiro gradual del apoyo. Admite respuesta oral, gráfica, manipulativa o digital si conserva la demanda; no reemplaces el OA por una tarea más fácil.

**Profundización:** comparar otra estrategia, formular una objeción o caso límite y transferir a una situación nueva. Exige razonamiento revisable en lugar de ejercicios repetidos.

**Errores previsibles:** {errors}. **Evidencia:** {product} que responda al verbo del OA y muestre razonamiento. **Criterios de éxito:** aborda el OA, usa evidencia pertinente, explica una decisión y revisa el resultado. Reenseña errores comunes; forma un grupo breve ante errores puntuales; ofrece transferencia cuando exista dominio. En 45 minutos conserva meta, modelado, práctica y ticket.
""")
 reads=item["readings"]
 reading="\n".join(f"- [{r['title']}]({r['url']}) — lectura vinculada por MINEDUC." for r in reads) if reads else "La ficha oficial no registra una lectura específica. Selecciona un texto pertinente del plan lector del establecimiento o de recursos oficiales."
 return f"""# {item['oa_code']} — {item['topic']}
| Nivel | Asignatura | Tema/eje | Cobertura | Dosificación |
|---|---|---|---|---|
| {item['course']} | {item['subject']} | {item['axis']} | {item['coverage']} | {len(item['phases'])} clases de 90 min |

## Qué se debe aprender
> {item['oa_text']}

**Explicación pedagógica.** El OA exige comprender, aplicar en una situación nueva y explicar evidencia; completar una actividad no basta. **Vocabulario explícito:** {vocab}. Antes de enseñar, comprueba vocabulario del enunciado, seguimiento de instrucciones y una experiencia relacionada con el tema. El diagnóstico decide apoyos, no califica ni etiqueta.

## Lecturas y textos
{reading}

Estos recursos asociados no constituyen una lista nacional obligatoria. Este repositorio enlaza y no reproduce obras protegidas.

## Planificación clase a clase
La dosificación responde a la amplitud y demanda cognitiva del OA. Intercala recuperación o amplía transferencia según evidencia, manteniendo el objetivo.

{chr(10).join(parts)}
## Evaluación integradora y realidad escolar
Evalúa contenido, respuesta al verbo, evidencia o razonamiento y comunicación/revisión. Registra evidencia individual. La propuesta funciona con pizarra, cuaderno y materiales disponibles; la conectividad no es requisito. En cursos numerosos usa respuestas simultáneas, estaciones y grupos temporales. Considera diversidad lingüística, cultural, sensorial y motriz.

## Fuente
- [Ficha oficial del OA]({item['source_url']})
- [Asignatura y nivel]({item['subject_url']})
- Snapshot: {item['verified_at']}
- [Volver a la malla](../../../CURRICULUM.md)
"""

def page_path(item):
 return f"classes/{item['course_slug']}/{item['subject_slug']}/{slugify(item['oa_code'])}.html"

def grade_one_summary(objs,classes):
 grade_objs=[x for x in objs if x["course_order"]==1];grade_classes=[x for x in classes if x["course_order"]==1];subjects=[]
 for subject in sorted({x["subject"] for x in grade_objs}):
  os=[x for x in grade_objs if x["subject"]==subject];cs=[x for x in grade_classes if x["subject"]==subject]
  subjects.append({"name":subject,"slug":os[0]["subject_slug"],"oa":len(os),"classes":len(cs),"axes":sorted({x["axis"] for x in os}),"first":page_path(os[0])})
 return grade_objs,grade_classes,subjects

GRADE_ONE_SUBJECT_PROFILES={
 "artes-visuales":{
  "purpose":"Aprender a observar, imaginar y tomar decisiones visuales. El foco no es copiar un modelo adulto, sino explorar materiales, comunicar ideas y conversar sobre las propias obras y las de otros.",
  "outcomes":["crear imágenes a partir de observaciones, recuerdos e imaginación","explorar línea, color, forma y textura con distintas materialidades","explicar una elección visual usando vocabulario accesible","apreciar obras y producciones de pares sin reducir la conversación a me gusta/no me gusta"],
  "method":"Modela una posibilidad técnica sin convertirla en plantilla. Ofrece materiales limitados pero combinables, conserva rastros del proceso y cierra con una conversación breve sobre decisiones visuales.",
  "barrier":"Cuando todos los trabajos se parecen, la demostración se convirtió en receta. Vuelve a abrir decisiones: tema, encuadre, color, textura o material.",
  "evidence":"obra o exploración visual, explicación oral de una decisión y registro del proceso"
 },
 "ciencias-naturales":{
  "purpose":"Construir curiosidad disciplinada: observar con atención, formular preguntas, comparar evidencia y explicar patrones del mundo vivo, físico y terrestre próximo.",
  "outcomes":["formular preguntas investigables a partir de fenómenos cercanos","registrar observaciones mediante dibujos, tablas simples u oralidad","comparar características y reconocer patrones","comunicar una explicación distinguiendo observación de suposición"],
  "method":"Parte de un fenómeno observable, pide una predicción, acuerda qué mirar, registra antes de explicar y vuelve a la evidencia al cerrar. Cambia una variable cuando corresponda.",
  "barrier":"Una actividad llamativa no es todavía indagación. Si no hay pregunta, observación registrada y conclusión contrastada, explicita esas tres piezas.",
  "evidence":"registro de observación, comparación y explicación breve apoyada en evidencia"
 },
 "educacion-fisica-salud":{
  "purpose":"Desarrollar habilidades motrices, autocuidado, participación segura y disfrute del movimiento mediante desafíos progresivos y observables.",
  "outcomes":["combinar acciones motrices básicas con mayor control","seguir reglas de seguridad y juego limpio","reconocer señales corporales asociadas al esfuerzo","proponer y probar estrategias sencillas en juegos"],
  "method":"Demuestra desde varios ángulos, delimita zonas y señales, ofrece estaciones con niveles de desafío y observa calidad del movimiento, no solo velocidad o resultado.",
  "barrier":"Eliminar a quien falla reduce práctica y evidencia. Prefiere juegos de participación continua, intentos repetidos y roles rotativos.",
  "evidence":"desempeño motriz seguro observado con pauta, autoevaluación corporal y explicación de una decisión"
 },
 "historia-geografia-ciencias-sociales":{
  "purpose":"Ayudar a ubicarse en el tiempo, el espacio y la vida comunitaria, usando experiencias cercanas, mapas, testimonios e imágenes como fuentes que se interrogan.",
  "outcomes":["ordenar hechos y reconocer cambios y continuidades","leer representaciones espaciales simples","obtener información explícita de una fuente","participar y justificar acuerdos de convivencia"],
  "method":"Distingue experiencia personal, fuente e interpretación. Trabaja con preguntas concretas: quién, cuándo, dónde, qué muestra y qué no permite saber.",
  "barrier":"Memorizar fechas o símbolos sin contexto no construye pensamiento histórico ni ciudadano. Vuelve a relaciones temporales, espaciales y causales cercanas.",
  "evidence":"secuencia temporal, lectura de fuente o mapa y explicación situada"
 },
 "ingles-propuesta":{
  "purpose":"Construir confianza para comprender y comunicar significados muy frecuentes mediante escucha, interacción, juego lingüístico, imágenes y textos breves.",
  "outcomes":["reconocer palabras y expresiones frecuentes en mensajes breves","responder oralmente con apoyo gestual o visual","participar en intercambios predecibles","producir palabras o frases breves con propósito"],
  "method":"Primero ofrece input comprensible, luego respuesta coral o gestual, práctica en parejas y finalmente una producción breve. Corrige sin interrumpir toda intención comunicativa.",
  "barrier":"Traducir cada palabra impide escuchar por sentido. Usa contexto, repetición con variación, imágenes y rutinas antes de recurrir a la traducción.",
  "evidence":"comprensión demostrada por acción y producción oral o escrita comprensible"
 },
 "lengua-cultura-pueblos-originarios-ancestrales":{
  "purpose":"Fortalecer lengua, identidad, memoria, territorio y conocimientos de pueblos originarios desde el contexto lingüístico real y con respeto por la diversidad entre comunidades.",
  "outcomes":["escuchar y usar expresiones pertinentes al contexto lingüístico","reconocer vínculos entre lengua, territorio, memoria y prácticas culturales","participar en relatos, conversaciones o producciones con sentido","distinguir saber situado de generalización folclorizante"],
  "method":"Ajusta la propuesta al pueblo y territorio del establecimiento, incorpora voces y validación comunitaria cuando sea posible, y nunca presenta una práctica local como universal.",
  "barrier":"Una actividad genérica sobre pueblos originarios puede reproducir estereotipos. Nombra el contexto, la fuente, quién valida y qué diversidad queda fuera.",
  "evidence":"uso situado de lengua o relato, conexión territorial y explicación respetuosa de una práctica"
 },
 "lenguaje-comunicacion":{
  "purpose":"Integrar oralidad, lectura y escritura para comprender, imaginar, conversar y producir mensajes con propósito, sin reducir el aprendizaje a decodificación mecánica.",
  "outcomes":["comprender información explícita y construir inferencias iniciales","relatar y conversar respetando turnos y propósito","producir textos breves mediante planificación, escritura y revisión","ampliar vocabulario a partir de lecturas y experiencias"],
  "method":"Lee y piensa en voz alta, pregunta por evidencia del texto, permite ensayo oral antes de escribir y separa generación de ideas de revisión convencional.",
  "barrier":"La caligrafía o velocidad lectora pueden ocultar comprensión. Recoge también respuestas orales, dibujos secuenciados y selección justificada cuando el OA lo permita.",
  "evidence":"respuesta de comprensión con evidencia, producción oral o texto breve revisado"
 },
 "matematica":{
  "purpose":"Construir sentido numérico y espacial mediante problemas, representaciones y conversación matemática; el procedimiento importa junto con la explicación y la verificación.",
  "outcomes":["representar cantidades, relaciones y patrones de distintas maneras","seleccionar y explicar una estrategia de resolución","estimar y comprobar si un resultado es razonable","comunicar semejanzas y diferencias usando lenguaje matemático inicial"],
  "method":"Comienza con material o situación, registra estrategias distintas, conecta objeto-dibujo-símbolo y pide siempre una forma de comprobar.",
  "barrier":"Llegar al número correcto no demuestra comprensión. Solicita representación y explicación; un error consistente informa mejor que una respuesta adivinada.",
  "evidence":"solución representada, estrategia explicada y comprobación"
 },
 "musica":{
  "purpose":"Desarrollar escucha atenta, expresión, coordinación e imaginación sonora mediante repertorios diversos, interpretación, creación y conversación musical.",
  "outcomes":["reconocer y describir cualidades del sonido","mantener pulso y reproducir patrones simples","interpretar y crear usando voz, cuerpo, objetos o instrumentos","expresar una apreciación vinculada a lo escuchado"],
  "method":"Alterna escuchar, imitar, variar, crear y nombrar. Evita explicar durante demasiado tiempo lo que puede experimentarse primero con el cuerpo y el sonido.",
  "barrier":"Cantar fuerte o memorizar una canción no equivale por sí solo a escuchar o comprender. Observa pulso, entrada, contraste, intención y capacidad de ajustar.",
  "evidence":"interpretación o creación audible y comentario referido a elementos musicales"
 },
 "orientacion":{
  "purpose":"Construir bienestar, autoconocimiento, vínculos respetuosos, participación y hábitos de trabajo mediante situaciones protegidas y decisiones practicables.",
  "outcomes":["reconocer emociones, necesidades y fortalezas sin etiquetar a otros","ensayar formas de pedir ayuda, poner límites y resolver desacuerdos","participar en acuerdos de curso","organizar acciones sencillas de autocuidado y trabajo escolar"],
  "method":"Usa casos ficticios, lenguaje no clínico, derecho a pasar y alternativas privadas de respuesta. Enseña conductas concretas; no fuerces revelaciones personales.",
  "barrier":"Convertir la conversación en exposición pública puede dañar. Si el OA puede demostrarse con un caso ficticio, nunca exijas autobiografía.",
  "evidence":"decisión justificada ante un caso, práctica de una habilidad interpersonal y plan breve"
 },
 "tecnologia":{
  "purpose":"Comprender que una solución tecnológica responde a una necesidad y mejora al diseñar, construir, probar y revisar con criterios, materiales y seguridad.",
  "outcomes":["identificar necesidad, usuario y condiciones","representar una idea antes de construir","seleccionar materiales o herramientas con criterio","probar una solución y proponer una mejora basada en resultados"],
  "method":"Haz visible el ciclo necesidad-diseño-construcción-prueba-mejora. Limita materiales, acuerda criterios antes de construir y valora el registro del proceso.",
  "barrier":"Una manualidad terminada no demuestra diseño. Pregunta qué problema resuelve, qué criterio cumple, qué falló en la prueba y qué cambiaría.",
  "evidence":"boceto, producto o procedimiento probado y mejora justificada"
 }
}

def grade_one_page(objs,classes):
 grade_objs,grade_classes,subjects=grade_one_summary(objs,classes)
 cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['classes']} clases</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(' · '.join(item['axes']))}</p><a href="../index.html?nivel={quote('1° básico')}&asignatura={quote(item['name'])}#explorar">Explorar asignatura →</a></article>''' for item in subjects)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="Mapa completo de 1° básico: 237 OA y 1.034 clases desarrolladas en 11 asignaturas."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/1-basico.html"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><title>1° básico completo | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenidos">Saltar a contenidos</a><header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al explorador</a></header>
<main id="contenidos" class="level-shell"><header class="level-hero"><div><p class="eyebrow">Nivel desarrollado · Chile</p><h1>1° básico</h1><p>Un mapa completo del nivel para pasar del Objetivo de Aprendizaje a decisiones concretas de enseñanza, práctica y evaluación.</p><div class="hero-actions"><a class="button primary" href="../index.html?nivel={quote('1° básico')}#explorar">Ver las 1.034 clases</a><a class="button dark-text" href="../documentacion.html">Leer documentación</a></div></div><aside><span>Estado editorial</span><strong>100% desarrollado</strong><small>Pendiente de revisión humana externa</small></aside></header>
<section class="level-metrics" aria-label="Resumen de 1° básico"><div><strong>{f'{len(grade_classes):,}'.replace(',','.')}</strong><span>clases</span></div><div><strong>{len(grade_objs)}</strong><span>objetivos</span></div><div><strong>{len(subjects)}</strong><span>asignaturas</span></div><div><strong>{sum(len(x['readings']) for x in grade_objs)}</strong><span>lecturas vinculadas</span></div></section>
<section class="level-intro"><div><p class="eyebrow">Qué encontrará</p><h2>Contenidos organizados por área</h2></div><p>Cada tarjeta muestra la cobertura real del nivel. Al abrir una asignatura puede recorrer sus clases, OA y ejes, con fuente oficial, materiales, apoyos, criterios de éxito y una decisión posterior basada en evidencia.</p></section><section class="level-grid">{cards}</section>
<section class="level-contract"><div><p class="eyebrow">Contrato pedagógico</p><h2>Una clase desarrollada no es una frase genérica.</h2></div><ol><li><strong>Propósito y meta</strong><span>Lo que hará el docente y lo que comprenderá el estudiante.</span></li><li><strong>Experiencia concreta</strong><span>Inicio, demostración, práctica guiada y desempeño individual.</span></li><li><strong>Más contenido útil</strong><span>Tarea flexible, actividades complementarias, recuperación y profundización.</span></li><li><strong>Dificultades y roles</strong><span>Acciones inmediatas, comprobación y coordinación profesional.</span></li><li><strong>Evidencia y decisión</strong><span>Ticket, criterios observables y qué hacer después.</span></li></ol></section></main>
<footer class="site-footer"><div><strong>Trayectoria Escolar Chile</strong><span>1° básico · desarrollo editorial completo · Markdown + HTML</span></div><div><a class="star-link" href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/stargazers">⭐ Dar una estrella</a><a href="../index.html">Explorador</a><a href="../documentacion.html">Documentación</a><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/LICENSING.md">Licencias</a></div></footer></body></html>'''

def grade_one_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_one_summary(objs,classes)
 lines=["# 1° básico — mapa de contenidos","","> **Nivel completamente desarrollado:** 1.034 clases · 237 OA · 11 asignaturas. Estado de revisión humana: pendiente.","","[Programa narrativo completo](1-basico/README.md) · [Ver el nivel en el portal](https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/1-basico.html) · [Explorar todas las clases](https://vladimiracunadev-create.github.io/chilean-school-learning-path/?nivel=1%C2%B0+b%C3%A1sico#explorar) · [Guía pedagógica](../TEACHING_GUIDE.md) · [Evaluación formativa](EVALUACION_FORMATIVA.md)","","Este mapa resume cifras y ejes. Para propósito, resultados, prerrequisitos, método, recorrido OA por OA y decisiones específicas, utiliza el [programa completo de 1° básico](1-basico/README.md) y sus 11 guías de asignatura.","","## Cómo usar este mapa","","1. Elige una asignatura y revisa sus ejes, OA y número de clases.","2. Abre el OA en el portal y ubica la clase dentro de la secuencia completa.","3. Define la evidencia individual y los criterios que observarás.","4. Adapta materiales, apoyos y duración sin cambiar el aprendizaje central.","5. Después del ticket, decide si avanzar, reagrupar o reenseñar.","","## Progresión sugerida","","~~~mermaid","flowchart LR","    A[Experiencia concreta] --> B[Lenguaje y representación]","    B --> C[Práctica con apoyo]","    C --> D[Desempeño individual]","    D --> E[Evidencia y decisión]","~~~","","Esta progresión orienta la enseñanza, pero no obliga a avanzar por calendario. La evidencia del curso puede justificar volver a una representación concreta, ofrecer otra vía de acceso o profundizar.","","## Cobertura","","| Asignatura | OA | Clases | Ejes curriculares |","|---|---:|---:|---|"]
 for item in subjects:lines.append(f"| {item['name']} | {item['oa']} | {item['classes']} | {'; '.join(item['axes'])} |")
 lines += ["","## Cómo se ve una clase desarrollada","","Cada clase del nivel contiene:","","1. **Propósito docente** y **meta en lenguaje estudiantil**.","2. **Inicio, modelado, práctica guiada, desempeño individual y ticket de salida** con acciones concretas.","3. **Materiales y preparación** realizables sin depender de conectividad.","4. **Apoyo en el mismo OA** y **profundización** que no rebajan ni repiten mecánicamente la tarea.","5. **Evidencia, criterios observables y decisión posterior** para avanzar, reagrupar o reenseñar.","6. **Versión de 45 minutos** que conserva el núcleo del aprendizaje.","","## Criterios de diseño para 1° básico","","- Experiencias breves, concretas y con transición gradual hacia dibujo, lenguaje o símbolo.","- Respuestas simultáneas y evidencia individual para evitar que participen siempre los mismos.","- Juego con propósito pedagógico explícito, normas seguras y cierre que recupera lo aprendido.","- Lectura, oralidad, manipulación, movimiento y creación como medios de acceso, no como actividades de relleno.","- Casos ficticios y derecho a pasar en Orientación; cuidado territorial y validación comunitaria en lengua y cultura de pueblos originarios.","- Materiales disponibles, alternativas sin conexión y adaptación de 90 a 45 minutos.","","## Decisiones con evidencia","","- **Logrado con autonomía:** avanzar o proponer transferencia.","- **En desarrollo:** mantener el OA y entregar apoyo puntual.","- **Requiere otra vía de acceso:** cambiar representación, ejemplo o forma de respuesta.","- **Sin evidencia suficiente:** ofrecer otra oportunidad antes de concluir.","","Consulta la [guía de evaluación formativa](EVALUACION_FORMATIVA.md) para criterios y registro.","","## Fuente de verdad y límites","",f"Los conteos se generan desde `curriculum/catalog.json`. La fuente oficial contiene {len(grade_objs)} OA; el generador los dosifica en {len(grade_classes):,} clases.".replace(",",".")+" “Desarrollada” significa que cumple el contrato editorial automatizado; **no significa revisión humana experta**. Ninguna clase se declara revisada hasta registrar esa evidencia.","","## Verificación","","La CI regenera las fichas, valida las 1.034 clases del nivel, comprueba campos editoriales y páginas HTML, ejecuta tests y bloquea la publicación si existe deriva. La fecha de la fuente curricular se conserva en cada OA.","","## Documentos relacionados","","- [Centro de documentación](README.md)","- [Guía pedagógica](../TEACHING_GUIDE.md)","- [Metodología](../METHODOLOGY.md)","- [Estado editorial](../EDITORIAL_STATUS.md)","- [Roadmap](../ROADMAP.md)",""]
 return "\n".join(lines)

def grade_one_subject_documentation(subject,objectives,previous_subject=None,next_subject=None):
 profile=GRADE_ONE_SUBJECT_PROFILES[subject["slug"]]
 axis_rows=[]
 for axis in subject["axes"]:
  axis_objectives=[item for item in objectives if item["axis"]==axis]
  axis_rows.append((axis,len(axis_objectives),sum(len(item["phases"]) for item in axis_objectives)))
 nav=["[⬅️ Índice de 1° básico](README.md)"]
 if previous_subject:nav.append(f"[← {previous_subject['name']}]({previous_subject['slug']}.md)")
 if next_subject:nav.append(f"[{next_subject['name']} →]({next_subject['slug']}.md)")
 lines=[
  f"# {subject['name']} · 1° básico","",
  " · ".join(nav),"",
  f"**{subject['oa']} OA · {subject['classes']} clases · {len(subject['axes'])} ejes curriculares · bloques adaptables a 45 o 90 minutos**","",
  f"> **Estado editorial:** todas las clases de esta asignatura están desarrolladas y publicadas. La revisión humana disciplinar y pedagógica sigue pendiente.","",
  "## 🎯 De qué trata esta asignatura","",profile["purpose"],"",
  "## 🧩 Qué problema pedagógico resuelve","",
  f"La secuencia evita convertir el OA en una actividad aislada. Cada objetivo avanza desde activación y modelado hacia práctica, desempeño individual y evidencia. **Alerta principal:** {profile['barrier']}","",
  "## 🎓 Resultados de aprendizaje del recorrido","",
  "Al trabajar los OA del nivel, se busca que cada estudiante pueda:",""
 ]
 lines += [f"- {value.capitalize()}." for value in profile["outcomes"]]
 lines += ["","## 🧱 Prerrequisitos y punto de entrada","",
  "No se asume dominio formal previo. La primera clase de cada OA recupera experiencias, lenguaje y representaciones disponibles para identificar desde dónde enseñar. Cuando un conocimiento previo no aparece, se incorpora al modelado sin convertirlo en requisito de exclusión.","",
  "## 🧭 Cómo recorrer la asignatura","",
  "1. Revisa el OA completo y su eje antes de elegir una clase.","2. Mantén el orden de la secuencia mientras la evidencia confirme que el curso puede avanzar.","3. Usa la adaptación de 45 minutos cuando corresponda, sin eliminar el desempeño individual.","4. Registra el patrón observado y decide si avanzar, reagrupar o reenseñar.","",
  f"**Método disciplinar:** {profile['method']}","",
  "## 🧱 Anatomía estable de cada clase","",
  "| Momento | Función pedagógica | Evidencia |","|---|---|---|",
  "| Inicio | Activar y diagnosticar sin calificar | Respuesta inicial de todo el curso |",
  "| Modelado | Hacer visible el contenido y el razonamiento | Reconstrucción del ejemplo o contraste con un error |",
  "| Práctica guiada | Ensayar con apoyo y retroalimentación | Producción compartida y ajustes observables |",
  "| Desempeño individual | Comprobar qué puede hacer cada estudiante | Producto, acción o explicación individual |",
  f"| Cierre | Contrastar criterios y decidir | {profile['evidence'].capitalize()} |","",
  "## 🗺️ Estructura por ejes","",
  "| Eje | OA | Clases |","|---|---:|---:|"
 ]
 lines += [f"| {axis} | {oa_count} | {class_count} |" for axis,oa_count,class_count in axis_rows]
 lines += ["","~~~mermaid","flowchart LR","    A[Experiencia y diagnóstico] --> B[Modelado disciplinar]","    B --> C[Práctica guiada]","    C --> D[Desempeño individual]","    D --> E[Evidencia]","    E --> F{Decisión docente}","    F -->|Avanzar| G[Transferir o profundizar]","    F -->|Apoyar| C","    F -->|Reenseñar| B","~~~","",
  "## 📖 Recorrido OA por OA","",
  "La tabla funciona como índice completo de la asignatura. El número de clases expresa la dosificación inicial, no una obligación de calendario.","",
  "| OA | Tema de la secuencia | Eje | Clases | Planificación |","|---|---|---|---:|---|"
 ]
 for item in objectives:
  lines.append(f"| {item['oa_code']} | {item['topic']} | {item['axis']} | {len(item['phases'])} | [Abrir Markdown](../../{item['path']}) · [Ver en portal](https://vladimiracunadev-create.github.io/chilean-school-learning-path/{page_path(item)}) |")
 lines += ["","## 🔎 Qué observar","",
  f"**Evidencia central:** {profile['evidence']}.","",
  "No uses velocidad, presentación, volumen de voz o conducta general como sustitutos del aprendizaje. Si una barrera de lectura, escritura, movilidad, percepción o comunicación es ajena al OA, cambia la vía de acceso y vuelve a observar.","",
  "## 🧰 Preparación y materiales","",
  "Cada ficha declara sus materiales concretos. Antes de enseñar, comprueba disponibilidad, seguridad, tiempo de distribución y una alternativa sin conectividad. En 1° básico conviene preparar menos materiales, bien organizados, que una variedad que consuma la clase en transiciones.","",
  "## ⚠️ Error frecuente y recuperación","",
  f"**Señal de alerta:** {profile['barrier']}","",
  "Recupera el propósito del OA, muestra otro ejemplo o representación, ofrece práctica breve con retroalimentación y solicita una nueva evidencia. Repetir la misma explicación más fuerte o más rápido no constituye reenseñanza.","",
  "## ♿ Acceso y profundización","",
  "- **Acceso:** anticipar vocabulario, fragmentar instrucciones, permitir ensayo oral, usar apoyos concretos o visuales y ofrecer distintas formas pertinentes de respuesta.","- **Profundización:** comparar estrategias, justificar decisiones, crear un caso, mejorar el producto o transferir a una situación nueva.","",
  "## 🔗 Fuente y límites","",
  f"- [Fuente curricular de la asignatura]({objectives[0]['subject_url']})","- [Guía pedagógica](../../TEACHING_GUIDE.md)","- [Rúbrica de evaluación](../RUBRICA_EVALUACION.md)","- [Protocolo de revisión humana](../REVISION_HUMANA.md)","",
  "El contenido desarrollado cumple el contrato automatizado del proyecto, pero no se declara revisado por especialistas hasta que exista evidencia registrada.",""
 ]
 return "\n".join(lines)

def grade_one_index_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_one_summary(objs,classes)
 lines=["# 📚 Programa completo de 1° básico","",
  "> [⬅️ Volver al programa](../../README.md) · [🌐 Abrir vista visual](https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/1-basico.html) · [📘 Syllabus](../SYLLABUS.md) · [📊 Rúbrica](../RUBRICA_EVALUACION.md)","",
  "**1.034 clases · 237 OA · 11 asignaturas · desarrollo editorial completo · revisión humana pendiente**","",
  "## 🎯 De qué trata este nivel","",
  "1° básico construye los lenguajes con los que niñas y niños seguirán aprendiendo: oralidad, lectura y escritura inicial, número y representación, observación del entorno, orientación temporal y espacial, expresión artística y musical, movimiento, convivencia, identidad y diseño de soluciones. El programa no trata estas áreas como compartimentos cerrados: mantiene la especificidad de cada disciplina y favorece conexiones cuando ayudan a comprender.","",
  "## 🧩 Problemas que busca resolver","",
  "- Pasar de una lista extensa de OA a secuencias enseñables y navegables.","- Evitar clases genéricas que podrían pertenecer a cualquier asignatura.","- Recoger evidencia de cada estudiante, no solo de quienes participan espontáneamente.","- Apoyar dificultades sin rebajar el OA y profundizar sin entregar más repetición.","- Trabajar con materiales alcanzables, conectividad opcional y bloques de 45 o 90 minutos.","- Separar con transparencia contenido generado, desarrollado, revisado y publicado.","",
  "## 🎓 Resultados transversales","",
  "Al terminar el nivel, y según los OA oficiales de cada asignatura, se espera que el estudiante amplíe su capacidad para:","",
  "- comunicar ideas y experiencias mediante oralidad, escritura emergente, cuerpo, imagen, sonido y símbolo;","- representar cantidades, relaciones, secuencias, espacios y fenómenos;","- observar, preguntar, comparar y explicar usando evidencia cercana;","- crear, probar, revisar y conversar sobre sus decisiones;","- participar de forma segura, respetuosa y progresivamente autónoma;","- reconocer identidad, territorio, comunidad y diversidad sin estereotipos.","",
  "## 🧱 Prerrequisitos","",
  "No se exige que el estudiante llegue leyendo, escribiendo o calculando de manera convencional. El nivel parte de experiencias, lenguaje oral, juego, exploración, trazos, conteo espontáneo, movimiento y conocimientos familiares o comunitarios. Cada OA comienza diagnosticando lo disponible para decidir el andamiaje.","",
  "## 🧭 Cómo recorrer el programa","",
  "1. Elige asignatura y eje.","2. Abre una guía de asignatura para comprender su progresión completa.","3. Selecciona el OA y revisa todas sus clases antes de enseñar la primera.","4. Define evidencia y criterios; luego prepara materiales y accesos.","5. Enseña, observa y adapta. El calendario no reemplaza la evidencia.","",
  "## 🗂️ Las 11 asignaturas","",
  "| Asignatura | OA | Clases | Qué aporta | Guía |","|---|---:|---:|---|---|"
 ]
 for subject in subjects:
  profile=GRADE_ONE_SUBJECT_PROFILES[subject["slug"]]
  lines.append(f"| {subject['name']} | {subject['oa']} | {subject['classes']} | {profile['purpose']} | [📘 Leer](./{subject['slug']}.md) |")
 lines += ["","## 🧠 Progresión pedagógica común","",
  "~~~mermaid","flowchart TD","    A[Experiencia concreta y diagnóstico] --> B[Lenguaje disciplinar]","    B --> C[Modelado con ejemplo y error]","    C --> D[Práctica guiada]","    D --> E[Desempeño individual]","    E --> F[Evidencia y criterios]","    F --> G{¿Qué necesita el curso?}","    G -->|Dominio| H[Profundizar y transferir]","    G -->|Apoyo puntual| D","    G -->|Otra explicación| B","~~~","",
  "## ⏱️ Ritmo y planificación","",
  "Las 1.034 clases representan una biblioteca de propuestas asociadas a toda la oferta curricular registrada, no un horario anual para cursarlas simultáneamente. La selección depende del plan de estudios aplicable, el establecimiento, el contexto lingüístico y cultural y las horas disponibles.","",
  "| Escala | Uso recomendado |","|---|---|","| Año | Seleccionar OA aplicables, hitos, periodos de evaluación y conexiones |","| Unidad | Ordenar OA, conocimientos previos, productos y evidencia acumulativa |","| Semana | Elegir clases, anticipar materiales, grupos y apoyos |","| Clase | Ajustar tiempos y recoger evidencia para la decisión siguiente |","",
  "## 🧱 Anatomía de una clase","",
  "| Sección | Para qué sirve |","|---|---|","| Propósito docente y meta estudiantil | Alinear enseñanza y comprensión esperada |","| Inicio | Recuperar y diagnosticar |","| Modelado | Hacer visible el contenido y el pensamiento |","| Práctica guiada | Ensayar con apoyo |","| Desempeño individual | Evitar inferir aprendizaje solo desde el grupo |","| Apoyo y profundización | Ajustar acceso y desafío |","| Ticket y criterios | Reunir evidencia breve y observable |","| Decisión posterior | Avanzar, reagrupar o reenseñar |","",
  "## 📊 Cómo se evalúa","",
  "La evaluación es formativa y descriptiva. La [rúbrica](../RUBRICA_EVALUACION.md) distingue logro autónomo, aprendizaje en desarrollo, necesidad de otra vía de acceso y ausencia de evidencia suficiente. Estas categorías orientan decisiones; no son calificaciones automáticas.","",
  "## 🔗 Documentos relacionados","",
  "- [Syllabus completo](../SYLLABUS.md)","- [Guía docente](../../TEACHING_GUIDE.md)","- [Rúbrica de evaluación](../RUBRICA_EVALUACION.md)","- [Preguntas frecuentes](../FAQ.md)","- [Guía para familias](../GUIA_FAMILIAS.md)","- [Protocolo de revisión humana](../REVISION_HUMANA.md)","- [Fuentes oficiales](../../OFFICIAL_REFERENCES.md)",""
 ]
 return "\n".join(lines)

def documentation_page(objs,classes):
 _,_,subjects=grade_one_summary(objs,classes)
 cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['classes']} clases</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_ONE_SUBJECT_PROFILES[item['slug']]['purpose'])}</p><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/docs/1-basico/{item['slug']}.md">Leer guía completa →</a></article>''' for item in subjects)
 levels=[]
 for order in range(1,13):
  level_classes=[item for item in classes if item["course_order"]==order]
  level_oas={item["oa_code"] for item in level_classes}
  developed=sum(item["editorial_status"]=="desarrollada" for item in level_classes)
  levels.append({"name":level_classes[0]["course"],"oa":len(level_oas),"classes":len(level_classes),"developed":developed})
 coverage_cards="".join(f'''<a class="coverage-card" href="index.html?nivel={quote(item['name'])}#explorar"><span>{html.escape(item['name'])}</span><strong>{item['classes']:,}</strong><small>{item['oa']} OA · {item['developed']} desarrolladas</small></a>'''.replace(",",".") for item in levels)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="Documentación completa de Trayectoria Escolar Chile y del programa desarrollado de 1° básico."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/documentacion.html"><link rel="icon" href="icon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><title>Documentación | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#documentacion">Saltar a documentación</a><header class="detail-topbar"><a class="brand" href="index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="index.html">← Volver al portal</a></header>
<main id="documentacion" class="level-shell"><header class="level-hero docs-hero"><div><p class="eyebrow">Documentación pedagógica</p><h1>Del currículum a decisiones de aula.</h1><p>Una arquitectura completa para comprender qué enseñar, cómo recorrer 1° básico, qué evidencia observar y cómo revisar la calidad sin confundir publicación con validación humana.</p><div class="hero-actions"><a class="button primary" href="levels/1-basico.html">Ver 1° básico</a><a class="button dark-text" href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/docs/SYLLABUS.md">Abrir syllabus</a></div></div><aside><span>Documentos principales</span><strong>10 guías marco</strong><small>más 11 guías completas de asignatura</small></aside></header>
<section class="level-metrics"><div><strong>1.034</strong><span>clases desarrolladas</span></div><div><strong>237</strong><span>OA de 1° básico</span></div><div><strong>11</strong><span>guías de asignatura</span></div><div><strong>0</strong><span>revisiones humanas registradas</span></div></section>
<section class="level-intro"><div><p class="eyebrow">Empieza según tu tarea</p><h2>Documentos que responden preguntas concretas</h2></div><p><strong>Syllabus:</strong> alcance y planificación. <strong>Guía docente:</strong> conducción de clases. <strong>Rúbrica:</strong> evidencia y decisiones. <strong>FAQ:</strong> límites y uso. <strong>Familias:</strong> acompañamiento. <strong>Revisión:</strong> cómo validar responsablemente.</p></section>
<section class="doc-link-grid"><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/docs/QUE_ES_UN_OA.md"><span>01</span><strong>¿Qué es un OA?</strong><small>Explicación simple con ejemplo</small></a><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/docs/SYLLABUS.md"><span>02</span><strong>Syllabus</strong><small>Programa, ritmo y planificación</small></a><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/TEACHING_GUIDE.md"><span>03</span><strong>Guía docente</strong><small>Preparar, enseñar y adaptar</small></a><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/docs/ROLES_DOCENTES.md"><span>04</span><strong>Roles en el aula</strong><small>Responsabilidades y coordinación</small></a><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/docs/DIFICULTADES_EN_EL_AULA.md"><span>05</span><strong>Dificultades y acciones</strong><small>Observar, actuar y comprobar</small></a><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/docs/RUBRICA_EVALUACION.md"><span>06</span><strong>Rúbrica</strong><small>Observar y decidir</small></a><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/docs/COBERTURA.md"><span>07</span><strong>Cobertura total</strong><small>12 niveles con acceso directo</small></a><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/docs/FORMATOS.md"><span>08</span><strong>Markdown + HTML</strong><small>Cómo se publica cada clase</small></a><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/docs/LICENCIAS.md"><span>09</span><strong>Licencias</strong><small>Qué puede reutilizarse</small></a><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/docs/FAQ.md"><span>10</span><strong>Preguntas frecuentes</strong><small>Uso, alcance y límites</small></a></section>
<section class="oa-explainer"><div><p class="eyebrow">Sin siglas misteriosas</p><h2>OA significa Objetivo de Aprendizaje.</h2></div><div><p>Describe lo que una o un estudiante debe llegar a comprender o hacer. <strong>No es una clase, una tarea ni una actividad.</strong></p><p><code>MA01 OA 01</code> se lee: Matemática · 1° básico · Objetivo de Aprendizaje número 1. El proyecto convierte cada OA en una secuencia de clases con evidencia.</p></div></section>
<section class="level-intro"><div><p class="eyebrow">Cobertura navegable</p><h2>Los 12 niveles, sin callejones sin salida</h2></div><p>Cada tarjeta abre el explorador ya filtrado. Las cifras separan cobertura curricular, desarrollo editorial y revisión humana.</p></section><section class="coverage-grid">{coverage_cards}</section>
<section class="level-intro"><div><p class="eyebrow">Programa desarrollado</p><h2>1° básico, asignatura por asignatura</h2></div><p>Cada guía explica propósito, resultados, prerrequisitos, método disciplinar, estructura por ejes, recorrido OA por OA, evidencia, barreras frecuentes, acceso y profundización.</p></section><section class="level-grid">{cards}</section>
<section class="level-contract"><div><p class="eyebrow">Lectura honesta</p><h2>Profundidad documental sin inflar el estado.</h2></div><ol><li><strong>Desarrollada</strong><span>La clase contiene decisiones pedagógicas y disciplinares específicas.</span></li><li><strong>Publicada</strong><span>Está disponible y navegable en Markdown y HTML.</span></li><li><strong>Revisada</strong><span>Solo cuando una persona competente registra evidencia de revisión.</span></li><li><strong>Adaptable</strong><span>El docente conserva el OA y ajusta la vía de acceso según su curso.</span></li></ol></section></main>
<footer class="site-footer"><div><strong>Trayectoria Escolar Chile</strong><span>Documentación abierta y trazable · MIT + CC BY-NC-SA 4.0</span></div><div><a class="star-link" href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/stargazers">⭐ Dar una estrella</a><a href="index.html">Portal</a><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/LICENSING.md">Licencias</a></div></footer></body></html>'''

def developed_lesson_html(item,index,code,lesson):
 def esc(value): return html.escape(str(value), quote=True)
 criteria="".join(f"<li>{esc(value)}</li>" for value in lesson["criteria"])
 complementary="".join(f"<li>{esc(value)}</li>" for value in lesson.get("complementary", []))
 difficulties="".join(f"<tr><td>{esc(row['signal'])}</td><td>{esc(row['action'])}</td><td>{esc(row['check'])}</td></tr>" for row in lesson.get("difficulty_actions", []))
 return f'''<article class="lesson lesson-developed" id="{esc(code.lower())}">
<header><span class="lesson-number">{index:02d}</span><div><p>Clase {index} de {len(item['phases'])}</p><h2>{esc(lesson['title'])}</h2></div><span class="status-badge developed">Desarrollada</span></header>
<p class="lesson-focus"><strong>Propósito docente:</strong> {esc(lesson['purpose'])}</p><p class="student-goal"><strong>Meta para estudiantes:</strong> {esc(lesson['goal'])}</p>
<div class="lesson-grid"><section><h3>Inicio · 10 min</h3><p>{esc(lesson['opening'])}</p></section><section><h3>Modelado · 20 min</h3><p>{esc(lesson['model'])}</p></section><section><h3>Práctica guiada · 25 min</h3><p>{esc(lesson['guided'])}</p></section><section><h3>Desempeño individual · 25 min</h3><p>{esc(lesson['independent'])}</p></section></div>
<div class="material-callout"><h3>Materiales y preparación</h3><p>{esc(lesson['materials'])}</p></div>
<div class="support-grid"><p><strong>Apoyo:</strong> {esc(lesson['support'])}</p><p><strong>Profundización:</strong> {esc(lesson['extension'])}</p></div>
<div class="assessment-grid"><section><h3>Ticket de salida · 10 min</h3><p>{esc(lesson['ticket'])}</p><p><strong>Evidencia:</strong> {esc(lesson['evidence'])}</p></section><section><h3>Criterios observables</h3><ul>{criteria}</ul></section></div>
<p class="next-step"><strong>Decisión posterior:</strong> {esc(lesson['next_step'])}</p><p class="short-version"><strong>Si dispone de 45 minutos:</strong> {esc(lesson['short_version'])}</p>
<div class="extension-grid"><section><p class="eyebrow">Consolidación</p><h3>Tarea breve y flexible</h3><p>{esc(lesson.get('home_task','Consolida el aprendizaje con una evidencia breve sin internet ni materiales comprados.'))}</p></section><section><p class="eyebrow">Banco opcional</p><h3>Actividades complementarias</h3><ul>{complementary}</ul></section></div>
<section class="difficulty-panel"><p class="eyebrow">Respuesta durante la clase</p><h3>Control de dificultades con acciones</h3><div class="table-scroll"><table><thead><tr><th>Dificultad observable</th><th>Acción inmediata</th><th>Comprobación</th></tr></thead><tbody>{difficulties}</tbody></table></div><p class="role-note"><strong>Coordinación profesional:</strong> {esc(lesson.get('specialist_coordination','El docente responsable conserva la conducción del OA y acuerda barrera, acción y evidencia con los profesionales de apoyo.'))}</p></section>
</article>'''

def lesson_page(item, previous_item=None, next_item=None):
 def esc(value): return html.escape(str(value), quote=True)
 def nav_link(other, label):
  if not other:return ""
  return f'<a class="sequence-link" href="../../../{page_path(other)}"><span>{label}</span><strong>{esc(other["oa_code"])}</strong></a>'
 reading_items="".join(
  f'<li><a href="{esc(r["url"])}" rel="noopener">{esc(r["title"])}</a><span>Lectura vinculada por MINEDUC</span></li>'
  for r in item["readings"]
 ) or '<li><span>Sin lectura específica registrada en la ficha oficial.</span><span>El establecimiento selecciona un recurso pertinente.</span></li>'
 vocab,product,errors=discipline(item["subject_slug"])
 sessions=[]
 for index,(code,(title,focus)) in enumerate(zip(item["codes"],item["phases"]),1):
  if item.get("developed"):
   sessions.append(developed_lesson_html(item,index,code,item["developed"]["lessons"][index-1]))
   continue
  sessions.append(f'''<article class="lesson" id="{esc(code.lower())}">
<header><span class="lesson-number">{index:02d}</span><div><p>Clase {index} de {len(item['phases'])}</p><h2>{esc(title)}</h2></div><span class="status-badge">Secuenciada</span></header>
<p class="lesson-focus"><strong>Meta:</strong> {esc(focus.capitalize())} para avanzar en «{esc(item['topic'].lower())}» y demostrarlo mediante {esc(product)}.</p>
<div class="lesson-grid"><section><h3>Inicio · 10 min</h3><p>Presenta una situación vinculada a <strong>{esc(item['topic'].lower())}</strong> y recoge una respuesta inicial de todo el curso.</p></section><section><h3>Modelado · 20 min</h3><p>Modela el OA usando {esc(vocab)}. Contrasta un ejemplo logrado con este error: {esc(errors)}.</p></section><section><h3>Práctica · 50 min</h3><p>Construyen juntos y luego individualmente {esc(product)}. Cada estudiante explica una decisión y revisa su resultado.</p></section><section><h3>Cierre · 10 min</h3><p>Ticket: decisión, evidencia y corrección del error previsible. Decide si avanzar, reagrupar o reenseñar.</p></section></div>
<div class="support-grid"><p><strong>Apoyo:</strong> anticipa {esc(vocab)}, muestra un ejemplo resuelto y admite distintas formas de respuesta sin reducir el OA.</p><p><strong>Profundización:</strong> compara otra estrategia, examina un caso límite y transfiere el aprendizaje a una situación nueva.</p></div>
<p class="success-criteria"><strong>Criterios de éxito:</strong> responde al OA, usa evidencia pertinente, explica una decisión y revisa el resultado.</p>
</article>''')
 editorial="Desarrollada" if item.get("developed") else "Secuenciada"
 editorial_note="Contenido disciplinar específico; pendiente de revisión humana." if item.get("developed") else "No equivale aún a una clase disciplinar revisada."
 canonical=f"https://vladimiracunadev-create.github.io/chilean-school-learning-path/{page_path(item)}"
 description=f"{item['course']} · {item['subject']} · {item['oa_code']}: {item['topic']}"
 return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#071c2c"><meta name="description" content="{esc(description)}">
<meta property="og:type" content="article"><meta property="og:title" content="{esc(item['oa_code']+' · '+item['topic'])}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{canonical}">
<link rel="canonical" href="{canonical}"><link rel="icon" href="../../../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../../../styles.css">
<title>{esc(item['oa_code'])} · {esc(item['topic'])} | Trayectoria Escolar Chile</title></head>
<body class="detail-page"><a class="skip-link" href="#contenido">Saltar al contenido</a>
<header class="detail-topbar"><a class="brand" href="../../../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../../../index.html">← Volver al explorador</a></header>
<main id="contenido" class="detail-shell"><nav class="breadcrumbs" aria-label="Migas de pan"><a href="../../../index.html">Inicio</a><span>›</span><span>{esc(item['course'])}</span><span>›</span><span>{esc(item['subject'])}</span></nav>
<header class="lesson-hero"><div><p class="eyebrow">{esc(item['course'])} · {esc(item['subject'])}</p><h1>{esc(item['topic'])}</h1><p class="oa-code">{esc(item['oa_code'])} · {esc(item['axis'])}</p></div><div class="hero-status"><span>Estado editorial</span><strong>{editorial}</strong><small>{editorial_note}</small></div></header>
<section class="oa-panel" aria-labelledby="oa-title"><p class="eyebrow">Objetivo oficial</p><h2 id="oa-title">Qué se espera aprender</h2><p class="oa-help"><strong>OA significa Objetivo de Aprendizaje:</strong> el resultado que debe alcanzar el estudiante. No es una actividad ni una clase; por eso este OA se desarrolla en una secuencia.</p><blockquote>{esc(item['oa_text'])}</blockquote><div class="oa-meta"><span>{len(item['phases'])} clases</span><span>Bloques adaptables a 45 o 90 min</span><span>{esc(item['coverage'])}</span></div></section>
<section class="content-section"><div class="section-heading"><div><p class="eyebrow">Secuencia propuesta</p><h2>De la activación a la evidencia</h2></div><p>La dosificación responde a la amplitud y demanda cognitiva del OA. El docente ajusta el ritmo según la evidencia.</p></div>{''.join(sessions)}</section>
<section class="sources-panel"><div><p class="eyebrow">Trazabilidad y formatos</p><h2>Fuente, Markdown y HTML</h2><p>Cada clase de esta secuencia existe en esta página HTML y como ancla estable dentro de su archivo Markdown.</p></div><ul><li><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/{esc(item['path'])}">Abrir fuente Markdown</a><span>Mismo OA y mismas clases en formato editable</span></li>{reading_items}<li><a href="{esc(item['source_url'])}" rel="noopener">Ficha oficial del OA</a><span>Currículum Nacional · consulta {esc(item['verified_at'])}</span></li></ul></section>
<nav class="sequence-nav" aria-label="Objetivos anterior y siguiente">{nav_link(previous_item,'Objetivo anterior')}{nav_link(next_item,'Objetivo siguiente')}</nav></main>
<footer class="site-footer"><div><strong>Proyecto educativo independiente</strong><span>Clase disponible en Markdown y HTML · contenido original CC BY-NC-SA 4.0</span></div><div><a class="star-link" href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/stargazers">⭐ Dar una estrella</a><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/LICENSING.md">Licencias</a></div></footer></body></html>'''
def main():
 snap=json.loads(SNAPSHOT.read_text(encoding="utf-8"));developed=json.loads(DEVELOPED.read_text(encoding="utf-8"))["objectives"];objs=[];classes=[];num=1
 for r in sorted(snap["records"],key=lambda x:(x["course_order"],x["subject"],x["subject_slug"])):
  for oa in r["objectives"]:
   reads=oa.get("readings",[]);phases=dose(oa["description"],r["subject_slug"],reads);codes=[f"CL-{num+i:05d}" for i in range(len(phases))];path=f"curriculum/{r['course_slug']}/{r['subject_slug']}/{slugify(oa['code'])}.md"
   item={"topic":topic_from(oa["description"]),"course":r["course"],"course_slug":r["course_slug"],"course_order":r["course_order"],"subject":r["subject"],"subject_slug":r["subject_slug"],"axis":oa["axis"],"oa_code":oa["code"],"oa_text":oa["description"],"coverage":cov(r["subject_slug"],r["course_order"]),"source_url":oa["url"],"subject_url":r["subject_url"],"verified_at":snap["verified_at"],"readings":reads,"path":path,"codes":codes,"phases":phases,"developed":developed.get(oa["code"])}
   if r["course_order"]==1:
    generated=build_grade_one_lessons(item)
    if not item["developed"]:item["developed"]=generated
    else:item["developed"]["lessons"]=[base | current for base,current in zip(generated["lessons"],item["developed"]["lessons"])]
   if item["developed"] and len(item["developed"]["lessons"]) != len(phases):raise ValueError(f"{oa['code']}: el contenido desarrollado debe tener {len(phases)} clases")
   objs.append(item)
   for lesson,(code,phase) in enumerate(zip(codes,phases),1):
    classes.append({"id":num,"class_code":code,"lesson":lesson,"lesson_count":len(phases),"phase":phase[0],"topic":item["topic"],"course":item["course"],"course_slug":item["course_slug"],"course_order":item["course_order"],"subject":item["subject"],"subject_slug":item["subject_slug"],"axis":item["axis"],"oa_code":item["oa_code"],"oa_text":item["oa_text"],"coverage":item["coverage"],"source_url":item["source_url"],"reading_count":len(reads),"editorial_status":"desarrollada" if item["developed"] else "secuenciada","publication_status":"publicada","path":path+"#"+code.lower(),"web_path":page_path(item)+"#"+code.lower()});num+=1
 developed_count=sum(x["editorial_status"]=="desarrollada" for x in classes)
 cat={"schema_version":5,"verified_at":snap["verified_at"],"source_url":snap["source_url"],"class_count":len(classes),"objective_count":len(objs),"course_count":12,"subject_count":len({x["subject"] for x in classes}),"reading_link_count":sum(len(x["readings"]) for x in objs),"editorial_counts":{"inventariada":len(classes),"secuenciada":len(classes),"desarrollada":developed_count,"revisada":0,"publicada":len(classes)},"classes":classes}
 (CURRICULUM/"catalog.json").write_text(json.dumps(cat,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 pages_root=ROOT/"site"/"classes"
 if pages_root.exists():
  shutil.rmtree(pages_root)
 for index,item in enumerate(objs):
  target=ROOT/item["path"];target.parent.mkdir(parents=True,exist_ok=True);target.write_text(plan(item),encoding="utf-8")
  web_target=ROOT/"site"/page_path(item);web_target.parent.mkdir(parents=True,exist_ok=True)
  web_target.write_text(lesson_page(item,objs[index-1] if index else None,objs[index+1] if index+1<len(objs) else None),encoding="utf-8")
 levels_root=ROOT/"site"/"levels";levels_root.mkdir(parents=True,exist_ok=True)
 (levels_root/"1-basico.html").write_text(grade_one_page(objs,classes),encoding="utf-8")
 (ROOT/"site"/"documentacion.html").write_text(documentation_page(objs,classes),encoding="utf-8")
 docs_root=ROOT/"docs";docs_root.mkdir(parents=True,exist_ok=True)
 (docs_root/"PRIMERO_BASICO.md").write_text(grade_one_documentation(objs,classes),encoding="utf-8")
 grade_docs_root=docs_root/"1-basico";grade_docs_root.mkdir(parents=True,exist_ok=True)
 grade_objs,_,grade_subjects=grade_one_summary(objs,classes)
 (grade_docs_root/"README.md").write_text(grade_one_index_documentation(objs,classes),encoding="utf-8")
 for subject_index,subject in enumerate(grade_subjects):
  subject_objectives=[item for item in grade_objs if item["subject_slug"]==subject["slug"]]
  previous_subject=grade_subjects[subject_index-1] if subject_index else None
  next_subject=grade_subjects[subject_index+1] if subject_index+1<len(grade_subjects) else None
  (grade_docs_root/f"{subject['slug']}.md").write_text(grade_one_subject_documentation(subject,subject_objectives,previous_subject,next_subject),encoding="utf-8")
 (ROOT/"site"/"catalog.json").write_text(json.dumps(cat,ensure_ascii=False)+"\n",encoding="utf-8")
 lines=["# Planificación curricular chilena","",f"## {cat['class_count']:,} clases · {cat['objective_count']:,} OA · 12 niveles".replace(",","."),"","Cada clase tiene nivel, asignatura, tema, fase y OA trazable. La dosificación de 4 a 7 clases se ajusta con evidencia.","","> Formación común, propuestas, asignaturas según contexto y electivos se distinguen; no representan una carga simultánea.",""]
 for order in range(1,13):
  cur=[x for x in classes if x["course_order"]==order];seen={}
  for x in cur:seen[(x["subject"],x["oa_code"],x["path"].split("#")[0],x["topic"],x["coverage"])]=x["lesson_count"]
  lines += [f"## {cur[0]['course']}","","| Asignatura | OA y tema | Clases | Cobertura |","|---|---|---:|---|"]
  for (sub,oa,path,topic,c),n in seen.items():lines.append(f"| {sub} | [{oa} · {topic}]({path}) | {n} | {c} |")
  lines.append("")
 (ROOT/"CURRICULUM.md").write_text("\n".join(lines),encoding="utf-8")
 urls=["https://vladimiracunadev-create.github.io/chilean-school-learning-path/","https://vladimiracunadev-create.github.io/chilean-school-learning-path/documentacion.html","https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/1-basico.html"]+[f"https://vladimiracunadev-create.github.io/chilean-school-learning-path/{page_path(item)}" for item in objs]
 sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"\n".join(f"  <url><loc>{url}</loc></url>" for url in urls)+"\n</urlset>\n"
 (ROOT/"site"/"sitemap.xml").write_text(sitemap,encoding="utf-8")
 print(json.dumps({k:cat[k] for k in ("class_count","objective_count","course_count","subject_count","reading_link_count")}))
if __name__=="__main__":main()

