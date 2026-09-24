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

def grade_one_page(objs,classes):
 grade_objs,grade_classes,subjects=grade_one_summary(objs,classes)
 cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['classes']} clases</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(' · '.join(item['axes']))}</p><a href="../index.html?nivel={quote('1° básico')}&asignatura={quote(item['name'])}#explorar">Explorar asignatura →</a></article>''' for item in subjects)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="Mapa completo de 1° básico: 237 OA y 1.034 clases desarrolladas en 11 asignaturas."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/1-basico.html"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><title>1° básico completo | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenidos">Saltar a contenidos</a><header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al explorador</a></header>
<main id="contenidos" class="level-shell"><header class="level-hero"><div><p class="eyebrow">Nivel desarrollado · Chile</p><h1>1° básico</h1><p>Un mapa completo del nivel para pasar del Objetivo de Aprendizaje a decisiones concretas de enseñanza, práctica y evaluación.</p><div class="hero-actions"><a class="button primary" href="../index.html?nivel={quote('1° básico')}#explorar">Ver las 1.034 clases</a><a class="button dark-text" href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/docs/PRIMERO_BASICO.md">Leer documentación</a></div></div><aside><span>Estado editorial</span><strong>100% desarrollado</strong><small>Pendiente de revisión humana externa</small></aside></header>
<section class="level-metrics" aria-label="Resumen de 1° básico"><div><strong>{f'{len(grade_classes):,}'.replace(',','.')}</strong><span>clases</span></div><div><strong>{len(grade_objs)}</strong><span>objetivos</span></div><div><strong>{len(subjects)}</strong><span>asignaturas</span></div><div><strong>{sum(len(x['readings']) for x in grade_objs)}</strong><span>lecturas vinculadas</span></div></section>
<section class="level-intro"><div><p class="eyebrow">Qué encontrará</p><h2>Contenidos organizados por área</h2></div><p>Cada tarjeta muestra la cobertura real del nivel. Al abrir una asignatura puede recorrer sus clases, OA y ejes, con fuente oficial, materiales, apoyos, criterios de éxito y una decisión posterior basada en evidencia.</p></section><section class="level-grid">{cards}</section>
<section class="level-contract"><div><p class="eyebrow">Contrato pedagógico</p><h2>Una clase desarrollada no es una frase genérica.</h2></div><ol><li><strong>Propósito y meta</strong><span>Lo que hará el docente y lo que comprenderá el estudiante.</span></li><li><strong>Experiencia concreta</strong><span>Inicio, demostración, práctica guiada y desempeño individual.</span></li><li><strong>Acceso y desafío</strong><span>Apoyos que conservan el OA y profundización sin repetición mecánica.</span></li><li><strong>Evidencia y decisión</strong><span>Ticket, criterios observables y qué hacer después.</span></li></ol></section></main>
<footer class="site-footer"><div><strong>Trayectoria Escolar Chile</strong><span>1° básico · desarrollo editorial completo</span></div><div><a href="../index.html">Explorador</a><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/EDITORIAL_STATUS.md">Estado editorial</a></div></footer></body></html>'''

def grade_one_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_one_summary(objs,classes)
 lines=["# 1° básico — mapa de contenidos","","> **Nivel completamente desarrollado:** 1.034 clases · 237 OA · 11 asignaturas. Estado de revisión humana: pendiente.","","[Ver el nivel en el portal](https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/1-basico.html) · [Explorar todas las clases](https://vladimiracunadev-create.github.io/chilean-school-learning-path/?nivel=1%C2%B0+b%C3%A1sico#explorar) · [Guía pedagógica](../TEACHING_GUIDE.md) · [Evaluación formativa](EVALUACION_FORMATIVA.md)","","## Cómo usar este mapa","","1. Elige una asignatura y revisa sus ejes, OA y número de clases.","2. Abre el OA en el portal y ubica la clase dentro de la secuencia completa.","3. Define la evidencia individual y los criterios que observarás.","4. Adapta materiales, apoyos y duración sin cambiar el aprendizaje central.","5. Después del ticket, decide si avanzar, reagrupar o reenseñar.","","## Progresión sugerida","","~~~mermaid","flowchart LR","    A[Experiencia concreta] --> B[Lenguaje y representación]","    B --> C[Práctica con apoyo]","    C --> D[Desempeño individual]","    D --> E[Evidencia y decisión]","~~~","","Esta progresión orienta la enseñanza, pero no obliga a avanzar por calendario. La evidencia del curso puede justificar volver a una representación concreta, ofrecer otra vía de acceso o profundizar.","","## Cobertura","","| Asignatura | OA | Clases | Ejes curriculares |","|---|---:|---:|---|"]
 for item in subjects:lines.append(f"| {item['name']} | {item['oa']} | {item['classes']} | {'; '.join(item['axes'])} |")
 lines += ["","## Cómo se ve una clase desarrollada","","Cada clase del nivel contiene:","","1. **Propósito docente** y **meta en lenguaje estudiantil**.","2. **Inicio, modelado, práctica guiada, desempeño individual y ticket de salida** con acciones concretas.","3. **Materiales y preparación** realizables sin depender de conectividad.","4. **Apoyo en el mismo OA** y **profundización** que no rebajan ni repiten mecánicamente la tarea.","5. **Evidencia, criterios observables y decisión posterior** para avanzar, reagrupar o reenseñar.","6. **Versión de 45 minutos** que conserva el núcleo del aprendizaje.","","## Criterios de diseño para 1° básico","","- Experiencias breves, concretas y con transición gradual hacia dibujo, lenguaje o símbolo.","- Respuestas simultáneas y evidencia individual para evitar que participen siempre los mismos.","- Juego con propósito pedagógico explícito, normas seguras y cierre que recupera lo aprendido.","- Lectura, oralidad, manipulación, movimiento y creación como medios de acceso, no como actividades de relleno.","- Casos ficticios y derecho a pasar en Orientación; cuidado territorial y validación comunitaria en lengua y cultura de pueblos originarios.","- Materiales disponibles, alternativas sin conexión y adaptación de 90 a 45 minutos.","","## Decisiones con evidencia","","- **Logrado con autonomía:** avanzar o proponer transferencia.","- **En desarrollo:** mantener el OA y entregar apoyo puntual.","- **Requiere otra vía de acceso:** cambiar representación, ejemplo o forma de respuesta.","- **Sin evidencia suficiente:** ofrecer otra oportunidad antes de concluir.","","Consulta la [guía de evaluación formativa](EVALUACION_FORMATIVA.md) para criterios y registro.","","## Fuente de verdad y límites","",f"Los conteos se generan desde `curriculum/catalog.json`. La fuente oficial contiene {len(grade_objs)} OA; el generador los dosifica en {len(grade_classes):,} clases.".replace(",",".")+" “Desarrollada” significa que cumple el contrato editorial automatizado; **no significa revisión humana experta**. Ninguna clase se declara revisada hasta registrar esa evidencia.","","## Verificación","","La CI regenera las fichas, valida las 1.034 clases del nivel, comprueba campos editoriales y páginas HTML, ejecuta tests y bloquea la publicación si existe deriva. La fecha de la fuente curricular se conserva en cada OA.","","## Documentos relacionados","","- [Centro de documentación](README.md)","- [Guía pedagógica](../TEACHING_GUIDE.md)","- [Metodología](../METHODOLOGY.md)","- [Estado editorial](../EDITORIAL_STATUS.md)","- [Roadmap](../ROADMAP.md)",""]
 return "\n".join(lines)

def developed_lesson_html(item,index,code,lesson):
 def esc(value): return html.escape(str(value), quote=True)
 criteria="".join(f"<li>{esc(value)}</li>" for value in lesson["criteria"])
 return f'''<article class="lesson lesson-developed" id="{esc(code.lower())}">
<header><span class="lesson-number">{index:02d}</span><div><p>Clase {index} de {len(item['phases'])}</p><h2>{esc(lesson['title'])}</h2></div><span class="status-badge developed">Desarrollada</span></header>
<p class="lesson-focus"><strong>Propósito docente:</strong> {esc(lesson['purpose'])}</p><p class="student-goal"><strong>Meta para estudiantes:</strong> {esc(lesson['goal'])}</p>
<div class="lesson-grid"><section><h3>Inicio · 10 min</h3><p>{esc(lesson['opening'])}</p></section><section><h3>Modelado · 20 min</h3><p>{esc(lesson['model'])}</p></section><section><h3>Práctica guiada · 25 min</h3><p>{esc(lesson['guided'])}</p></section><section><h3>Desempeño individual · 25 min</h3><p>{esc(lesson['independent'])}</p></section></div>
<div class="material-callout"><h3>Materiales y preparación</h3><p>{esc(lesson['materials'])}</p></div>
<div class="support-grid"><p><strong>Apoyo:</strong> {esc(lesson['support'])}</p><p><strong>Profundización:</strong> {esc(lesson['extension'])}</p></div>
<div class="assessment-grid"><section><h3>Ticket de salida · 10 min</h3><p>{esc(lesson['ticket'])}</p><p><strong>Evidencia:</strong> {esc(lesson['evidence'])}</p></section><section><h3>Criterios observables</h3><ul>{criteria}</ul></section></div>
<p class="next-step"><strong>Decisión posterior:</strong> {esc(lesson['next_step'])}</p><p class="short-version"><strong>Si dispone de 45 minutos:</strong> {esc(lesson['short_version'])}</p>
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
<section class="oa-panel" aria-labelledby="oa-title"><p class="eyebrow">Objetivo oficial</p><h2 id="oa-title">Qué se espera aprender</h2><blockquote>{esc(item['oa_text'])}</blockquote><div class="oa-meta"><span>{len(item['phases'])} clases</span><span>Bloques adaptables a 45 o 90 min</span><span>{esc(item['coverage'])}</span></div></section>
<section class="content-section"><div class="section-heading"><div><p class="eyebrow">Secuencia propuesta</p><h2>De la activación a la evidencia</h2></div><p>La dosificación responde a la amplitud y demanda cognitiva del OA. El docente ajusta el ritmo según la evidencia.</p></div>{''.join(sessions)}</section>
<section class="sources-panel"><div><p class="eyebrow">Trazabilidad</p><h2>Fuentes y lecturas</h2><p>Los recursos asociados no constituyen una lista nacional obligatoria. Se enlazan sin reproducir obras protegidas.</p></div><ul>{reading_items}<li><a href="{esc(item['source_url'])}" rel="noopener">Ficha oficial del OA</a><span>Currículum Nacional · consulta {esc(item['verified_at'])}</span></li></ul></section>
<nav class="sequence-nav" aria-label="Objetivos anterior y siguiente">{nav_link(previous_item,'Objetivo anterior')}{nav_link(next_item,'Objetivo siguiente')}</nav></main>
<footer class="site-footer"><span>Proyecto educativo independiente</span><a href="https://github.com/vladimiracunadev-create/chilean-school-learning-path">Código y documentación</a></footer></body></html>'''
def main():
 snap=json.loads(SNAPSHOT.read_text(encoding="utf-8"));developed=json.loads(DEVELOPED.read_text(encoding="utf-8"))["objectives"];objs=[];classes=[];num=1
 for r in sorted(snap["records"],key=lambda x:(x["course_order"],x["subject"],x["subject_slug"])):
  for oa in r["objectives"]:
   reads=oa.get("readings",[]);phases=dose(oa["description"],r["subject_slug"],reads);codes=[f"CL-{num+i:05d}" for i in range(len(phases))];path=f"curriculum/{r['course_slug']}/{r['subject_slug']}/{slugify(oa['code'])}.md"
   item={"topic":topic_from(oa["description"]),"course":r["course"],"course_slug":r["course_slug"],"course_order":r["course_order"],"subject":r["subject"],"subject_slug":r["subject_slug"],"axis":oa["axis"],"oa_code":oa["code"],"oa_text":oa["description"],"coverage":cov(r["subject_slug"],r["course_order"]),"source_url":oa["url"],"subject_url":r["subject_url"],"verified_at":snap["verified_at"],"readings":reads,"path":path,"codes":codes,"phases":phases,"developed":developed.get(oa["code"])}
   if r["course_order"]==1 and not item["developed"]:item["developed"]=build_grade_one_lessons(item)
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
 docs_root=ROOT/"docs";docs_root.mkdir(parents=True,exist_ok=True)
 (docs_root/"PRIMERO_BASICO.md").write_text(grade_one_documentation(objs,classes),encoding="utf-8")
 (ROOT/"site"/"catalog.json").write_text(json.dumps(cat,ensure_ascii=False)+"\n",encoding="utf-8")
 lines=["# Planificación curricular chilena","",f"## {cat['class_count']:,} clases · {cat['objective_count']:,} OA · 12 niveles".replace(",","."),"","Cada clase tiene nivel, asignatura, tema, fase y OA trazable. La dosificación de 4 a 7 clases se ajusta con evidencia.","","> Formación común, propuestas, asignaturas según contexto y electivos se distinguen; no representan una carga simultánea.",""]
 for order in range(1,13):
  cur=[x for x in classes if x["course_order"]==order];seen={}
  for x in cur:seen[(x["subject"],x["oa_code"],x["path"].split("#")[0],x["topic"],x["coverage"])]=x["lesson_count"]
  lines += [f"## {cur[0]['course']}","","| Asignatura | OA y tema | Clases | Cobertura |","|---|---|---:|---|"]
  for (sub,oa,path,topic,c),n in seen.items():lines.append(f"| {sub} | [{oa} · {topic}]({path}) | {n} | {c} |")
  lines.append("")
 (ROOT/"CURRICULUM.md").write_text("\n".join(lines),encoding="utf-8")
 urls=["https://vladimiracunadev-create.github.io/chilean-school-learning-path/","https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/1-basico.html"]+[f"https://vladimiracunadev-create.github.io/chilean-school-learning-path/{page_path(item)}" for item in objs]
 sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"\n".join(f"  <url><loc>{url}</loc></url>" for url in urls)+"\n</urlset>\n"
 (ROOT/"site"/"sitemap.xml").write_text(sitemap,encoding="utf-8")
 print(json.dumps({k:cat[k] for k in ("class_count","objective_count","course_count","subject_count","reading_link_count")}))
if __name__=="__main__":main()

