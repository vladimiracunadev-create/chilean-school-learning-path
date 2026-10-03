"""Build the curriculum source, public catalog, and static lesson pages."""
import html
import hashlib
import json
import os
import posixpath
import re
import shutil
from pathlib import Path
from urllib.parse import quote
from build_school_curriculum import ROOT,SNAPSHOT,CURRICULUM,slugify,topic_from
from grade_one_lessons import build_grade_one_lessons
from grade_one_math_lessons import build_math_sequence, transversal_links
from grade_one_language_lessons import attitude_link, build_language_sequence
from grade_one_science_history_arts_lessons import build_sequence as build_sha_sequence, transversal_links as sha_transversal_links
from grade_one_remaining_lessons import build_sequence as build_remaining_sequence, transversal_link as remaining_transversal_link
from grade_two_math_lessons import build_math_sequence as build_grade_two_math_sequence, build_transversal_integration as build_grade_two_math_integration, transversal_links as grade_two_transversal_links
from grade_two_language_science_history_lessons import build_sequence as build_grade_two_lsh_sequence, build_transversal_integration as build_grade_two_lsh_integration
from grade_two_arts_music_pe_lessons import build_sequence as build_grade_two_amp_sequence, build_transversal_integration as build_grade_two_amp_integration
from grade_two_remaining_lessons import build_sequence as build_grade_two_remaining_sequence, build_transversal_integration as build_grade_two_remaining_integration
from grade_three_math_language_lessons import build_sequence as build_grade_three_ml_sequence, build_transversal_integration as build_grade_three_ml_integration, complete_pilot_sequence
from grade_three_science_history_lessons import build_sequence as build_grade_three_sh_sequence, build_transversal_integration as build_grade_three_sh_integration, complete_history_pilot
from grade_three_arts_pe_english_indigenous_lessons import build_sequence as build_grade_three_apei_sequence, build_transversal_integration as build_grade_three_apei_integration
from grade_three_music_orientation_technology_lessons import build_sequence as build_grade_three_mot_sequence, build_transversal_integration as build_grade_three_mot_integration
from grade_four_math_lessons import build_sequence as build_grade_four_math_sequence, build_transversal_integration as build_grade_four_math_integration
from grade_four_remaining_lessons import build_sequence as build_grade_four_remaining_sequence, build_transversal_integration as build_grade_four_remaining_integration
from grade_five_core_lessons import build_sequence as build_grade_five_core_sequence, build_transversal_integration as build_grade_five_core_integration
from grade_five_remaining_lessons import build_sequence as build_grade_five_remaining_sequence, build_transversal_integration as build_grade_five_remaining_integration
from grade_six_math_lessons import build_sequence as build_grade_six_math_sequence, build_transversal_integration as build_grade_six_math_integration
from grade_six_remaining_lessons import build_sequence as build_grade_six_remaining_sequence, build_transversal_integration as build_grade_six_remaining_integration
from grade_seven_core_lessons import build_sequence as build_grade_seven_core_sequence, build_transversal_integration as build_grade_seven_core_integration
from grade_seven_next_five_lessons import build_sequence as build_grade_seven_next_five_sequence, build_transversal_integration as build_grade_seven_next_five_integration
from grade_seven_remaining_lessons import build_sequence as build_grade_seven_remaining_sequence, build_transversal_integration as build_grade_seven_remaining_integration
from grade_eight_core_lessons import build_sequence as build_grade_eight_core_sequence, build_transversal_integration as build_grade_eight_core_integration
from grade_eight_next_four_lessons import build_sequence as build_grade_eight_next_four_sequence, build_transversal_integration as build_grade_eight_next_four_integration
from grade_eight_remaining_lessons import build_sequence as build_grade_eight_remaining_sequence, build_transversal_integration as build_grade_eight_remaining_integration
from grade_one_middle_core_lessons import build_sequence as build_grade_one_middle_core_sequence, build_transversal_integration as build_grade_one_middle_core_integration
from grade_one_middle_next_four_lessons import build_sequence as build_grade_one_middle_next_four_sequence, build_transversal_integration as build_grade_one_middle_next_four_integration
from grade_one_middle_remaining_lessons import build_sequence as build_grade_one_middle_remaining_sequence, build_transversal_integration as build_grade_one_middle_remaining_integration
from grade_two_middle_core_lessons import build_sequence as build_grade_two_middle_core_sequence, build_transversal_integration as build_grade_two_middle_core_integration
from grade_two_middle_next_four_lessons import build_sequence as build_grade_two_middle_next_four_sequence, build_transversal_integration as build_grade_two_middle_next_four_integration
from grade_two_middle_remaining_lessons import build_sequence as build_grade_two_middle_remaining_sequence, build_transversal_integration as build_grade_two_middle_remaining_integration
from grade_three_middle_core_lessons import build_sequence as build_grade_three_middle_core_sequence
from grade_three_middle_remaining_lessons import build_sequence as build_grade_three_middle_remaining_sequence, SUBJECT_PROFILES as GRADE_THREE_MIDDLE_REMAINING_PROFILES
from grade_four_middle_lessons import build_sequence as build_grade_four_middle_sequence, SUBJECT_PROFILES as GRADE_FOUR_MIDDLE_PROFILES
from lesson_quality_enrichment import enrich_item
DEVELOPED=ROOT/"content"/"developed-lessons.json"

def version_public_data():
 site=ROOT/"site"
 app_source=(site/"app.js").read_text(encoding="utf-8").replace("\r\n","\n").replace("\r","\n")
 canonical_json=(
  json.dumps(json.loads((site/name).read_text(encoding="utf-8")),ensure_ascii=False,sort_keys=True,separators=(",",":"))
  for name in ("catalog.json","updates.json")
 )
 digest=hashlib.sha256("\0".join((app_source,*canonical_json)).encode("utf-8")).hexdigest()[:12]
 index_path=site/"index.html";index=index_path.read_text(encoding="utf-8")
 index,html_count=re.subn(r'<html lang="es" data-theme="light"(?: data-content-version="[^"]+")?>',f'<html lang="es" data-theme="light" data-content-version="{digest}">',index,count=1)
 index,script_count=re.subn(r'<script src="app\.js(?:\?v=[^"]+)?"></script>',f'<script src="app.js?v={digest}"></script>',index,count=1)
 if html_count != 1 or script_count != 1:raise RuntimeError("site/index.html no contiene marcadores únicos de versión pública")
 index_path.write_text(index,encoding="utf-8")
 return digest
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
 transversal="\n".join(f"- **{row['type']} · `{row['code']}`:** {row['application']}" for row in lesson.get("transversal", []))
 transversal_types={row["type"] for row in lesson.get("transversal", [])}
 transversal_heading="Integración de habilidad y actitud" if len(transversal_types)>1 else "Integración de actitud transversal"
 transversal_section=f"\n\n**{transversal_heading}:**\n{transversal}" if transversal else ""
 assessment="\n".join(f"| {row['level']} | {row['descriptor']} |" for row in lesson.get("assessment_levels", []))
 timing_45="\n".join(f"| {row['minutes']} min | {row['action']} |" for row in lesson.get("timing_45", []))
 teacher_checks="\n".join(f"- [ ] {value}" for value in lesson.get("teacher_checklist", []))
 app_items=[]
 for app in lesson.get("learning_support_apps", []):
  app_items += [
   f"- **[{app['name']}]({app['url']})** ({app['audience']}): {app['purpose']}",
   f"  - **Condiciones de uso:** {app['conditions']}",
   f"  - **Alternativa sin app:** {app['alternative']}",
   f"  - [Repositorio y documentación técnica]({app['repository_url']})",
  ]
 app_section=("\n\n### App de apoyo del aprendizaje (opcional)\n\n"+"\n".join(app_items)) if app_items else ""
 quality_section=f"""### Insumo concreto y consigna

**Recurso listo para usar:** {lesson['concrete_resource']}

**Consigna exacta:** {lesson['exact_prompt']}

**Referencia para modelar y corregir:** {lesson['response_reference']}

**Lista de preparación docente:**
{teacher_checks}

**Pauta de evaluación de cuatro niveles:**

| Nivel | Descriptor observable |
|---|---|
{assessment}

| Distribución de 45 minutos | Acción imprescindible |
|---:|---|
{timing_45}

""" if lesson.get("assessment_levels") else ""
 return f"""**Propósito docente:** {lesson['purpose']}

**Meta para estudiantes:** {lesson['goal']}

| Momento | Tiempo | Acción docente y experiencia |
|---|---:|---|
| Inicio | 10 min | {lesson['opening']} |
| Modelado | 20 min | {lesson['model']} |
| Práctica guiada | 25 min | {lesson['guided']} |
| Desempeño individual | 25 min | {lesson['independent']} |
| Cierre | 10 min | {lesson['ticket']} |

**Materiales y preparación:** {lesson['materials']}{app_section}

{quality_section}
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

**Coordinación de roles profesionales:** {lesson.get('specialist_coordination', 'El docente responsable conserva la conducción del OA y acuerda con los profesionales de apoyo una barrera, una acción y una evidencia, sin delegar ni diagnosticar durante la clase.')}{transversal_section}
"""

def official_alignment_markdown(item):
 data=(item.get("developed") or {}).get("official_alignment")
 if not data:return ""
 units="\n".join(f"- {value}" for value in data.get("units",[]))
 unit_heading="Organización interna de la secuencia" if data.get("unit_origin") else "Unidades relacionadas"
 unit_note=f"\n\n> **Origen:** {data['unit_origin'].rstrip('.')}." if data.get("unit_origin") else ""
 indicators="\n".join(f"- {value}" for value in data.get("indicators",[]))
 derived=bool(data.get("indicator_origin"))
 indicator_heading="Criterios de progresión derivados del OA" if derived else "Indicadores considerados para diseñar la secuencia"
 indicator_note=f"\n> **Origen:** {data['indicator_origin'].rstrip('.')}.\n" if derived else ""
 source_label="Fuente oficial del OA" if derived else "Fuente oficial de unidades e indicadores"
 return f"""## Alineación con el programa oficial
**{unit_heading}**
{units}{unit_note}

**{indicator_heading}**
{indicators}
{indicator_note}
- [{source_label}]({data['source']})

"""

def official_alignment_html(item):
 data=(item.get("developed") or {}).get("official_alignment")
 if not data:return ""
 units="".join(f"<li>{html.escape(value)}</li>" for value in data.get("units",[]))
 indicators="".join(f"<li>{html.escape(value)}</li>" for value in data.get("indicators",[]))
 source=html.escape(data["source"],quote=True)
 unit_heading="Organización interna de la secuencia" if data.get("unit_origin") else "Unidades relacionadas"
 unit_note=f'<p><strong>Origen:</strong> {html.escape(data["unit_origin"])}</p>' if data.get("unit_origin") else ""
 indicator_heading="Criterios de progresión derivados del OA" if data.get("indicator_origin") else "Indicadores considerados"
 indicator_note=f'<p><strong>Origen:</strong> {html.escape(data["indicator_origin"])}</p>' if data.get("indicator_origin") else ""
 return f'''<section class="sources-panel official-alignment"><div><p class="eyebrow">Alineación curricular</p><h2>Fuente y progresión utilizada</h2><p>Esta secuencia conserva la ficha oficial y explicita el origen de sus criterios de diseño.</p></div><div><h3>{unit_heading}</h3><ul>{units}</ul>{unit_note}<h3>{indicator_heading}</h3><ul>{indicators}</ul>{indicator_note}<p><a href="{source}" rel="noopener">Consultar fuente oficial</a></p></div></section>'''

def plan(item):
 vocab,product,errors=discipline(item["subject_slug"]);parts=[]
 content=item.get("developed") or item.get("integration") or item.get("draft")
 developed_content=item.get("developed") or {}
 if developed_content.get("pedagogical_explanation"):
  pedagogical_intro=f"**Explicación pedagógica.** {developed_content['pedagogical_explanation']}\n\n**Antes de comenzar.** {developed_content['prerequisites']}\n\n**Vocabulario explícito:** {developed_content['vocabulary']}."
 else:
  pedagogical_intro=f"**Explicación pedagógica.** El OA exige comprender, aplicar en una situación nueva y explicar evidencia; completar una actividad no basta. **Vocabulario explícito:** {vocab}. Antes de enseñar, comprueba vocabulario del enunciado, seguimiento de instrucciones y una experiencia relacionada con el tema. El diagnóstico decide apoyos, no califica ni etiqueta."
 alignment=official_alignment_markdown(item)
 content_status="Desarrollada con contenido específico" if item.get("developed") else "Integración transversal en las clases de los OA de contenido" if item.get("integration") else "Borrador estructurado pendiente de desarrollo específico"
 for i,(code,(title,focus)) in enumerate(zip(item["codes"],item["phases"]),1):
  if content:
   lesson=content["lessons"][i-1]
   parts.append(f"### Clase {i} de {len(item['phases'])}: {lesson['title']} {{#{code.lower()}}}\n**Estado editorial:** {content_status}.\n\n"+developed_block(lesson))
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

> **Derechos y procedencia:** el código y la redacción del OA anterior proceden de
> Currículum Nacional (MINEDUC) y se reproducen con enlace y fecha de consulta para
> trazabilidad. No se declaran obra del proyecto ni quedan cubiertos por la licencia
> CC BY-NC-SA 4.0 del contenido pedagógico original. Consulta
> [LICENSING.md](../../../LICENSING.md).

{pedagogical_intro}

{alignment}## Lecturas y textos
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

def grade_summary(objs,classes,course_order):
 grade_objs=[x for x in objs if x["course_order"]==course_order];grade_classes=[x for x in classes if x["course_order"]==course_order];subjects=[]
 for subject in sorted({x["subject"] for x in grade_objs}):
  os=[x for x in grade_objs if x["subject"]==subject];cs=[x for x in grade_classes if x["subject"]==subject]
  subjects.append({"name":subject,"slug":os[0]["subject_slug"],"oa":len(os),"classes":len(cs),"developed":sum(x["editorial_status"]=="desarrollada" for x in cs),"integrated":sum(x["editorial_status"]=="integrada" for x in cs),"drafts":sum(x["editorial_status"]=="borrador" for x in cs),"axes":sorted({x["axis"] for x in os}),"first":page_path(os[0])})
 return grade_objs,grade_classes,subjects

def grade_one_summary(objs,classes):
 return grade_summary(objs,classes,1)

def grade_two_summary(objs,classes):
 return grade_summary(objs,classes,2)

def grade_three_summary(objs,classes):
 return grade_summary(objs,classes,3)

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
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);drafts=sum(x["editorial_status"]=="borrador" for x in grade_classes)
 cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas · {item['integrated']} integradas · {item['drafts']} borradores</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(' · '.join(item['axes']))}</p><a href="../index.html?nivel={quote('1° básico')}&asignatura={quote(item['name'])}#explorar">Explorar asignatura →</a></article>''' for item in subjects)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="Desarrollo pedagógico interno completo de 1° básico: {developed} clases disciplinares y {integrated} experiencias integradas en 237 OA."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/1-basico.html"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><title>1° básico desarrollado | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenidos">Saltar a contenidos</a><header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al explorador</a></header>
<main id="contenidos" class="level-shell"><header class="level-hero"><div><p class="eyebrow">Desarrollo interno completo · Chile</p><h1>1° básico</h1><p>Las once asignaturas cuentan con secuencias específicas y trazables; permanece pendiente la revisión humana especializada antes de declarar el nivel revisado.</p><div class="hero-actions"><a class="button primary" href="../index.html?nivel={quote('1° básico')}#explorar">Ver las 1.034 propuestas</a><a class="button dark-text" href="../documentacion.html">Leer documentación</a></div></div><aside><span>Estado editorial real</span><strong>{developed} desarrolladas</strong><small>0 borradores · revisión humana pendiente</small></aside></header>'''+f'''
<section class="level-metrics" aria-label="Resumen de 1° básico"><div><strong>{developed}</strong><span>clases desarrolladas</span></div><div><strong>{integrated}</strong><span>experiencias transversales</span></div><div><strong>{f'{drafts:,}'.replace(',','.')}</strong><span>borradores</span></div><div><strong>{len(grade_objs)}</strong><span>objetivos inventariados</span></div></section>
<section class="level-intro"><div><p class="eyebrow">Qué encontrará</p><h2>Contenidos organizados por área</h2></div><p>Cada tarjeta muestra la cobertura real del nivel. Al abrir una asignatura puede recorrer sus clases, OA y ejes, con fuente oficial, materiales, apoyos, criterios de éxito y una decisión posterior basada en evidencia.</p></section><section class="level-grid">{cards}</section>
<section class="level-contract"><div><p class="eyebrow">Contrato pedagógico</p><h2>Una clase desarrollada no es una frase genérica.</h2></div><ol><li><strong>Propósito y meta</strong><span>Lo que hará el docente y lo que comprenderá el estudiante.</span></li><li><strong>Experiencia concreta</strong><span>Inicio, demostración, práctica guiada y desempeño individual.</span></li><li><strong>Más contenido útil</strong><span>Tarea flexible, actividades complementarias, recuperación y profundización.</span></li><li><strong>Dificultades y roles</strong><span>Acciones inmediatas, comprobación y coordinación profesional.</span></li><li><strong>Evidencia y decisión</strong><span>Ticket, criterios observables y qué hacer después.</span></li></ol></section></main>
<footer class="site-footer"><div><strong>Trayectoria Escolar Chile</strong><span>1° básico · desarrollo interno completo · revisión humana pendiente · Markdown + HTML</span></div><div><a class="star-link" href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/stargazers">⭐ Dar una estrella</a><a href="../index.html">Explorador</a><a href="../documentacion.html">Documentación</a><a href="../docs/licensing.html">Licencias</a></div></footer></body></html>'''

def grade_one_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_one_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);drafts=sum(x["editorial_status"]=="borrador" for x in grade_classes)
 lines=["# 1° básico — mapa de contenidos","",f"> **Desarrollo pedagógico interno completo:** {developed} clases desarrolladas · {integrated} experiencias transversales integradas · {drafts:,} borradores estructurados · 237 OA · 11 asignaturas · revisión humana pendiente.".replace(",","."),"","[Programa narrativo de 1° básico](1-basico/README.md) · [Índice Markdown de clases](../CURRICULUM.md) · [Guía pedagógica](../TEACHING_GUIDE.md) · [Evaluación formativa](EVALUACION_FORMATIVA.md)","","Todos los OA disciplinares del nivel cuentan con secuencias específicas. Las entradas **integradas** corresponden a habilidades o actitudes transversales incorporadas dentro de esas clases y no se cuentan como clases independientes. El estado **revisada** permanece en cero hasta registrar revisión profesional humana competente.","","## Cómo usar este mapa","","1. Elige una asignatura y revisa sus ejes, OA y número de clases.","2. Comprueba el estado editorial y la fuente antes de usar una clase.","3. Revisa la alineación, el ejemplo disciplinar, la evidencia y las acciones ante dificultades.","4. Adapta materiales, apoyos y duración sin cambiar el aprendizaje central.","5. Documenta observaciones y revisión profesional antes de declarar la secuencia revisada.","","## Progresión sugerida","","~~~mermaid","flowchart LR","    A[Experiencia concreta] --> B[Lenguaje y representación]","    B --> C[Práctica con apoyo]","    C --> D[Desempeño individual]","    D --> E[Evidencia y decisión]","~~~","","Esta progresión orienta la enseñanza, pero no sustituye el análisis específico de cada OA.","","## Cobertura","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Borradores |","|---|---:|---:|---:|---:|---:|"]
 for item in subjects:lines.append(f"| {item['name']} | {item['oa']} | {item['classes']} | {item['developed']} | {item['integrated']} | {item['drafts']} |")
 lines += ["","## Cómo se ve una clase desarrollada","","Una clase desarrollada contiene alineación curricular específica, propósito, meta estudiantil, ejemplos concretos, modelado disciplinar, práctica guiada, desempeño individual, materiales, apoyo, profundización, ticket, evidencia, criterios y decisiones ante dificultades. Un borrador solo conserva la arquitectura y debe reemplazarse.","","## Criterios de diseño para 1° básico","","- Experiencias breves, concretas y con transición gradual hacia dibujo, lenguaje o símbolo.","- Contenido y ejemplos propios del OA, no de una plantilla general de asignatura.","- Indicadores oficiales usados para construir una progresión observable.","- Respuestas simultáneas y evidencia individual.","- Materiales disponibles y alternativas de acceso sin rebajar el aprendizaje.","","## Decisiones con evidencia","","- **Logrado con autonomía:** avanzar o proponer transferencia.","- **En desarrollo:** mantener el OA y entregar apoyo puntual.","- **Requiere otra vía de acceso:** cambiar representación, ejemplo o forma de respuesta.","- **Sin evidencia suficiente:** ofrecer otra oportunidad antes de concluir.","","## Fuente de verdad y límites","",f"El catálogo registra {len(grade_objs)} OA y {len(grade_classes):,} propuestas de clase; hoy {developed} están desarrolladas y {drafts:,} siguen como borrador.".replace(",",".")+" Ninguna se declara revisada hasta registrar evidencia humana competente.","","## Verificación","","La CI comprueba estados, campos, páginas y reproducibilidad. No sustituye la revisión disciplinar o pedagógica.","","## Documentos relacionados","","- [Centro de documentación](README.md)","- [Guía pedagógica](../TEACHING_GUIDE.md)","- [Metodología](../METHODOLOGY.md)","- [Estado editorial](../EDITORIAL_STATUS.md)","- [Roadmap](../ROADMAP.md)",""]
 return "\n".join(lines)

def grade_one_subject_documentation(subject,objectives,previous_subject=None,next_subject=None):
 profile=GRADE_ONE_SUBJECT_PROFILES[subject["slug"]]
 scope=f"{subject['oa']} OA · {subject['classes']} propuestas"
 scopes={
  "matematica":"20 OA de contenido · 83 clases desarrolladas · 16 OA transversales · 68 experiencias integradas",
  "lenguaje-comunicacion":"26 OA de contenido · 131 clases desarrolladas · 7 OA transversales · 29 experiencias integradas",
  "ciencias-naturales":"12 OA de contenido · 49 clases desarrolladas · 10 OA transversales · 40 experiencias integradas",
  "historia-geografia-ciencias-sociales":"15 OA de contenido · 68 clases desarrolladas · 16 OA transversales · 64 experiencias integradas",
  "artes-visuales":"5 OA de contenido · 24 clases desarrolladas · 7 OA transversales · 28 experiencias integradas",
  "musica":"7 OA de contenido · 29 clases desarrolladas · 7 OA transversales · 28 experiencias integradas",
  "educacion-fisica-salud":"11 OA de contenido · 48 clases desarrolladas · 8 OA transversales · 32 experiencias integradas",
  "orientacion":"8 OA de contenido · 35 clases desarrolladas",
  "tecnologia":"6 OA de contenido · 26 clases desarrolladas · 5 OA transversales · 20 experiencias integradas",
  "ingles-propuesta":"14 OA de contenido · 69 clases desarrolladas · 4 OA transversales · 16 experiencias integradas",
  "lengua-cultura-pueblos-originarios-ancestrales":"29 OA de contenido · 129 clases desarrolladas · 4 OA transversales · 18 experiencias integradas",
 }
 scope=scopes.get(subject["slug"],scope)
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
  f"**{scope} · {len(subject['axes'])} ejes curriculares · bloques adaptables a 45 o 90 minutos**","",
  f"> **Estado editorial:** {subject['developed']} clases desarrolladas, {subject['integrated']} experiencias transversales integradas y {subject['drafts']} borradores estructurados. Ninguna revisión humana registrada.","",
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
  lines.append(f"| {item['oa_code']} | {item['topic']} | {item['axis']} | {len(item['phases'])} | [Abrir ficha Markdown](../../{item['path']}) |")
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
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);drafts=sum(x["editorial_status"]=="borrador" for x in grade_classes)
 lines=["# 📚 1° básico con desarrollo interno completo","",
  "> [⬅️ Volver al programa](../../README.md) · [🗂️ Índice Markdown](../../CURRICULUM.md) · [📘 Syllabus](../SYLLABUS.md) · [📊 Rúbrica](../RUBRICA_EVALUACION.md)","",
  f"**1.034 propuestas · 237 OA · 11 asignaturas · {developed} clases desarrolladas · {integrated} experiencias integradas · {drafts:,} borradores · revisión humana pendiente**".replace(",","."),"",
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

def grade_two_page(objs,classes):
 grade_objs,grade_classes,subjects=grade_two_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);sequenced=sum(x["editorial_status"]=="secuenciada" for x in grade_classes)
 cards=[]
 for item in subjects:
  state="Desarrollo interno completo"
  target=f"../docs/2-basico/{item['slug']}.html"
  cards.append(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas · {item['integrated']} integradas · {item['classes']-item['developed']-item['integrated']} secuenciadas</span></div><h2>{html.escape(item['name'])}</h2><p><strong>{state}.</strong> {html.escape(' · '.join(item['axes']))}</p><a href="{target}">Explorar asignatura →</a></article>''')
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="2° básico completo: 721 clases desarrolladas y 351 experiencias integradas en 11 asignaturas."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/2-basico.html"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><title>2° básico completo | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenidos">Saltar a contenidos</a><header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al explorador</a></header>
<main id="contenidos" class="level-shell"><header class="level-hero"><div><p class="eyebrow">Desarrollo pedagógico interno completo · Chile</p><h1>2° básico</h1><p>Las 1.072 propuestas de las once asignaturas están resueltas como 721 clases disciplinares y 351 experiencias transversales integradas. Ninguna se declara revisada sin evidencia humana competente.</p><div class="hero-actions"><a class="button primary" href="../docs/2-basico/index.html">Abrir mapa del nivel</a><a class="button dark-text" href="../index.html?nivel={quote('2° básico')}#explorar">Explorar clases</a></div></div><aside><span>Estado editorial real</span><strong>{developed} desarrolladas</strong><small>{integrated} integradas · {sequenced} secuenciadas · revisión humana pendiente</small></aside></header>
<section class="level-metrics" aria-label="Resumen de 2° básico"><div><strong>{len(grade_objs)}</strong><span>OA inventariados</span></div><div><strong>11</strong><span>asignaturas completas</span></div><div><strong>{developed}</strong><span>clases disciplinares</span></div><div><strong>{integrated}</strong><span>experiencias integradas</span></div></section>
<section class="level-intro"><div><p class="eyebrow">Nivel completo</p><h2>Once recorridos disciplinares, sin plantillas genéricas.</h2></div><p>Cada asignatura incluye ejemplos propios, modelado, práctica guiada, desempeño individual, apoyo, profundización, evidencia, criterios y decisiones posteriores.</p></section><section class="level-grid">{''.join(cards)}</section>
<section class="level-contract"><div><p class="eyebrow">Lectura honesta</p><h2>Completo no significa revisado.</h2></div><ol><li><strong>721 clases disciplinares</strong><span>Los 161 OA de contenido tienen secuencias específicas.</span></li><li><strong>351 experiencias integradas</strong><span>Los 86 OA transversales se observan dentro del contenido y no duplican clases.</span></li><li><strong>0 propuestas pendientes</strong><span>No quedan fichas sólo secuenciadas ni borradores en 2° básico.</span></li><li><strong>0 revisiones humanas</strong><span>La verificación automática no sustituye revisión profesional.</span></li></ol></section></main>
<footer class="site-footer"><div><strong>Trayectoria Escolar Chile</strong><span>2° básico completo · revisión humana pendiente</span></div><div><a href="../levels/1-basico.html">1° básico</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''

def grade_two_index_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_two_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes)
 lines=["# 📚 2° básico con desarrollo interno completo","","> [⬅️ Volver al programa](../../README.md) · [🗂️ Índice Markdown](../../CURRICULUM.md) · [📘 Syllabus](../SYLLABUS.md) · [📊 Rúbrica](../RUBRICA_EVALUACION.md)","",f"**{len(grade_classes):,} propuestas · {len(grade_objs)} OA · 11 asignaturas · {developed} clases desarrolladas · {integrated} experiencias integradas · 0 propuestas pendientes · revisión humana pendiente**".replace(",","."),"",
  "## 🎯 De qué trata este nivel","","2° básico consolida los lenguajes iniciados en 1° y aumenta gradualmente rango, precisión y autonomía: lectura y escritura con propósito, número hasta 1.000, indagación y explicación, uso de fuentes y mapas, creación artística y musical, combinación motriz, convivencia, identidad y diseño tecnológico. Cada disciplina conserva su método y explicita la continuidad con el nivel anterior.","",
  "## 🧩 Problemas que busca resolver","","- Convertir 247 OA en secuencias enseñables sin tratarlos como actividades aisladas.","- Hacer explícita la continuidad con 1° sin suponer aprendizajes automatizados.","- Evitar clases intercambiables entre asignaturas o repetidas dentro de un OA.","- Recoger evidencia individual y usarla para avanzar, apoyar o reenseñar.","- Integrar habilidades y actitudes sin inflar el número de clases.","- Mantener resguardos de privacidad, seguridad, contexto cultural y autoría.","",
  "## 🎓 Resultados transversales","","Al terminar el nivel, y según los OA oficiales de cada asignatura, se espera que el estudiante amplíe su capacidad para:","","- comprender, producir y revisar mensajes mediante oralidad, escritura, cuerpo, imagen, sonido y símbolo;","- representar cantidades, relaciones, tiempo, espacio, datos y fenómenos con mayor precisión;","- observar, preguntar, contrastar fuentes y explicar usando evidencia;","- crear, probar, revisar y justificar decisiones;","- participar de forma segura, respetuosa y progresivamente autónoma;","- relacionar identidad, territorio, comunidad y diversidad sin estereotipos.","",
  "## 🧱 Prerrequisitos y continuidad","","El punto de entrada es la evidencia, no la etiqueta del curso. Cada secuencia recupera conocimientos de 1° mediante una tarea breve; cuando una base no está disponible, la reincorpora con modelado y apoyo antes de ampliar el desafío. Las guías de asignatura indican qué continuidad se espera y cómo comprobarla.","",
  "## 🧭 Cómo recorrer el programa","","1. Elige asignatura y eje.","2. Lee la continuidad con 1° y la progresión completa de la guía.","3. Abre el OA y revisa todas sus clases antes de enseñar la primera.","4. Define evidencia y criterios; luego prepara materiales, seguridad y accesos.","5. Enseña, observa y adapta. El calendario no reemplaza la evidencia.","",
  "## 🗂️ Las 11 asignaturas","","| Asignatura | OA | Propuestas | Qué aporta | Guía |","|---|---:|---:|---|---|"]
 for subject in subjects:
  profile=GRADE_TWO_SUBJECT_PROFILES[subject["slug"]]
  lines.append(f"| {subject['name']} | {subject['oa']} | {subject['classes']} | {profile['purpose']} | [📘 Leer](./{subject['slug']}.md) |")
 lines += ["","## 🧠 Progresión pedagógica común","","~~~mermaid","flowchart TD","    A[Recuperar y diagnosticar 1°] --> B[Lenguaje disciplinar]","    B --> C[Modelado con ejemplo y error]","    C --> D[Práctica guiada]","    D --> E[Desempeño individual]","    E --> F[Evidencia y criterios]","    F --> G{¿Qué necesita el curso?}","    G -->|Dominio| H[Profundizar y transferir]","    G -->|Apoyo puntual| D","    G -->|Otra explicación| B","~~~","",
  "## ⏱️ Ritmo y planificación","","Las 1.072 propuestas representan una biblioteca asociada a toda la oferta curricular registrada, no un horario para cursarlas simultáneamente. La selección depende del plan aplicable, las horas disponibles, el contexto lingüístico y cultural y la evidencia del curso.","","| Escala | Uso recomendado |","|---|---|","| Año | Seleccionar OA aplicables, hitos, evaluaciones y conexiones con 1° |","| Unidad | Ordenar OA, prerrequisitos, productos y evidencia acumulativa |","| Semana | Elegir clases, anticipar materiales, grupos, seguridad y apoyos |","| Clase | Ajustar tiempos y recoger evidencia para la decisión siguiente |","",
  "## 🧱 Anatomía de una clase","","| Sección | Para qué sirve |","|---|---|","| Propósito docente y meta estudiantil | Alinear enseñanza y comprensión esperada |","| Inicio | Recuperar 1° y diagnosticar |","| Modelado | Hacer visible contenido, decisión y error |","| Práctica guiada | Ensayar con apoyo |","| Desempeño individual | Comprobar aprendizaje atribuible |","| Apoyo y profundización | Ajustar acceso y desafío |","| Ticket y criterios | Reunir evidencia breve y observable |","| Decisión posterior | Avanzar, reagrupar o reenseñar |","",
  "## 📊 Cómo se evalúa","","La evaluación es formativa y descriptiva. La [rúbrica](../RUBRICA_EVALUACION.md) distingue logro autónomo, aprendizaje en desarrollo, necesidad de otra vía de acceso y ausencia de evidencia suficiente. Las integraciones transversales se observan en desempeños concretos y no como rasgos de personalidad.","",
  "## 🔎 Estados y límites","","- **Desarrollada:** contenido disciplinar específico con modelado, práctica, evidencia, apoyo y decisión posterior.","- **Integrada:** habilidad o actitud observada dentro de una clase de contenido; no se cuenta como clase autónoma.","- **Secuenciada:** OA ubicado y dosificado, todavía sin desarrollo; quedan 0 en este nivel.","- **Revisada:** requiere evidencia humana competente; actualmente hay 0.","",
  "## 🔗 Documentos relacionados","","- [Mapa técnico del nivel](../SEGUNDO_BASICO.md)","- [Syllabus completo](../SYLLABUS.md)","- [Guía docente](../../TEACHING_GUIDE.md)","- [Rúbrica de evaluación](../RUBRICA_EVALUACION.md)","- [Preguntas frecuentes](../FAQ.md)","- [Guía para familias](../GUIA_FAMILIAS.md)","- [Protocolo de revisión humana](../REVISION_HUMANA.md)","- [Fuentes oficiales](../../OFFICIAL_REFERENCES.md)",""]
 return "\n".join(lines)

def grade_two_math_documentation(objs,classes):
 grade_objs,_,_=grade_two_summary(objs,classes)
 math=[item for item in grade_objs if item["subject_slug"]=="matematica"]
 core=[item for item in math if item["oa_code"].startswith("MA02 OA ")]
 transverse=[item for item in math if not item["oa_code"].startswith("MA02 OA ")]
 lines=["# Matemática · 2° básico","","> [⬅️ Mapa de 2° básico](README.md) · [🗂️ Índice curricular](../../CURRICULUM.md) · [📊 Rúbrica](../RUBRICA_EVALUACION.md)","","**22 OA de contenido · 93 clases desarrolladas · 15 OA transversales · 64 experiencias integradas · 5 ejes · revisión humana pendiente**","","> **Estado editorial:** desarrollo interno completo para Matemática. Esto no declara revisión disciplinar humana.","","## Propósito del recorrido","","Consolidar el sentido numérico hasta 1.000, las operaciones y estrategias hasta 100, la multiplicación inicial, patrones, relaciones de igualdad, geometría, calendario, tiempo, longitud y representación de datos. La progresión exige pasar entre objetos, dibujos, lenguaje y símbolos, y comprobar antes de aceptar un resultado.","","## Continuidad con 1° básico","","La secuencia recupera conteo, representación hasta 20, composición, problemas aditivos, formas, medición informal y datos simples. No asume que todos esos aprendizajes estén automatizados: cada OA diagnostica el punto de entrada y conserva apoyos concretos antes de ampliar rango o simbolización.","","## Estructura por ejes","","| Eje | OA de contenido | Clases |","|---|---:|---:|"]
 for axis in sorted({item["axis"] for item in core}):
  pool=[item for item in core if item["axis"]==axis]
  lines.append(f"| {axis} | {len(pool)} | {sum(len(item['phases']) for item in pool)} |")
 lines += ["","## Recorrido OA por OA","","| OA | Tema | Eje | Clases | Planificación |","|---|---|---|---:|---|"]
 for item in core:
  lines.append(f"| `{item['oa_code']}` | {item['topic']} | {item['axis']} | {len(item['phases'])} | [Abrir Markdown](../../{item['path']}) |")
 lines += ["","## Integración transversal","",f"Los {len(transverse)} OA de habilidades y actitudes se distribuyen en 64 experiencias dentro de las 93 clases de contenido. Cada clase identifica una habilidad y una actitud observables; no se evalúan como personalidad, rapidez u obediencia.","","## Contrato de calidad","","- Cada clase usa un ejemplo numérico, geométrico, de medición o de datos propio del OA.","- La práctica guiada y el ticket no repiten el modelo con los mismos datos.","- El apoyo mantiene la relación matemática y cambia la vía de acceso.","- La profundización modifica condiciones, compara estrategias o exige generalizar.","- Toda respuesta se acompaña de representación o comprobación pertinente.","","## Fuentes y límites","",f"- [Currículum Nacional · Matemática 2° básico]({math[0]['subject_url']})","- [Protocolo de revisión humana](../REVISION_HUMANA.md)","- [Metodología](../../METHODOLOGY.md)","","La alineación de cada OA conserva la ficha oficial. Los criterios de progresión se rotulan como internos cuando fueron derivados del OA y no se presentan como indicadores oficiales del programa.",""]
 return "\n".join(lines)

GRADE_TWO_PURPOSES={
 "artes-visuales":"Observar, experimentar y crear con línea, color, forma, materialidad y referentes artísticos diversos, explicando decisiones sin copiar un modelo único.",
 "ciencias-naturales":"Investigar seres vivos, cuerpo humano, agua y tiempo atmosférico mediante preguntas, observaciones, registros y explicaciones prudentes.",
 "educacion-fisica-salud":"Ampliar habilidades motrices, actividad física, autocuidado, seguridad y colaboración con progresiones accesibles y sin comparar cuerpos.",
 "historia-geografia-ciencias-sociales":"Comprender diversidad cultural, territorio, patrimonio y convivencia usando fuentes, mapas, tiempo histórico y decisiones ciudadanas.",
 "ingles-propuesta":"Comprender y producir mensajes breves en inglés mediante escucha, lectura, interacción y escritura apoyadas, sin exigir acento nativo.",
 "lengua-cultura-pueblos-originarios-ancestrales":"Aprender desde lengua, territorio, memoria y saberes de cada pueblo con fuentes comunitarias pertinentes, sin inventar ni apropiarse.",
 "lenguaje-comunicacion":"Integrar lectura, escritura y oralidad para comprender textos, producir con propósito, conversar y ampliar vocabulario.",
 "matematica":"Consolidar sentido numérico hasta 1.000, operaciones y estrategias hasta 100, multiplicación inicial, patrones, igualdad, geometría, tiempo, longitud y datos mediante representación, explicación y comprobación.",
 "musica":"Escuchar, representar, interpretar, improvisar y compartir música mediante cualidades sonoras, pulso, patrones y contextos diversos.",
 "orientacion":"Fortalecer identidad, emociones, autocuidado, convivencia, pertenencia y hábitos de aprendizaje mediante casos seguros y decisiones aplicables.",
 "tecnologia":"Diseñar, elaborar, probar y mejorar soluciones; usar dibujo digital, textos e internet con propósito, seguridad y respeto de autoría.",
}

GRADE_TWO_CONTINUITY={
 "artes-visuales":"Retoma la exploración libre de 1° y exige observar referentes con más detalle, combinar materialidades y explicar cómo una decisión visual comunica una idea.",
 "ciencias-naturales":"Parte de observar y comparar el entorno en 1° para avanzar hacia preguntas investigables, registros más sistemáticos y explicaciones apoyadas en evidencia.",
 "educacion-fisica-salud":"Recupera habilidades motrices básicas y amplía control, combinación de movimientos, cooperación, autocuidado y lectura de las señales del propio cuerpo.",
 "historia-geografia-ciencias-sociales":"Profundiza las nociones de identidad, tiempo y espacio de 1° mediante fuentes, mapas, patrimonio, diversidad cultural y decisiones de convivencia.",
 "ingles-propuesta":"Amplía las rutinas orales y el vocabulario de 1° hacia comprensión de textos breves, interacciones con seguimiento y producciones apoyadas con propósito.",
 "lengua-cultura-pueblos-originarios-ancestrales":"Continúa el vínculo entre lengua, memoria y territorio con mayor producción situada, siempre según el contexto lingüístico real y la validación comunitaria pertinente.",
 "lenguaje-comunicacion":"Consolida decodificación, comprensión, escritura emergente y conversación de 1° para leer textos más variados, revisar producciones y justificar interpretaciones.",
 "matematica":"Amplía el sentido numérico hasta 1.000, las estrategias aditivas, la multiplicación inicial, la geometría, la medición y los datos sin abandonar representaciones ni comprobación.",
 "musica":"Retoma escucha, pulso e interpretación de 1° y amplía la capacidad de representar, variar, improvisar y comentar decisiones musicales.",
 "orientacion":"Da continuidad al reconocimiento emocional, el autocuidado y la convivencia de 1° mediante decisiones más autónomas, hábitos y estrategias para resolver situaciones ficticias.",
 "tecnologia":"Profundiza el ciclo de diseño de 1° incorporando criterios de prueba, mejora documentada y uso inicial seguro de herramientas digitales.",
}

GRADE_TWO_SUBJECT_PROFILES={
 slug: GRADE_ONE_SUBJECT_PROFILES[slug] | {"purpose":purpose,"continuity":GRADE_TWO_CONTINUITY[slug]}
 for slug,purpose in GRADE_TWO_PURPOSES.items()
}

def grade_two_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_two_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);pending=sum(x["editorial_status"]=="secuenciada" for x in grade_classes)
 lines=["# 2° básico — mapa de contenidos","",f"> **Desarrollo pedagógico interno completo:** {developed} clases desarrolladas · {integrated} experiencias transversales integradas · {pending} propuestas pendientes · 247 OA · 11 asignaturas · revisión humana pendiente.","","[Programa narrativo de 2° básico](2-basico/README.md) · [Índice Markdown de clases](../CURRICULUM.md) · [Guía pedagógica](../TEACHING_GUIDE.md) · [Evaluación formativa](EVALUACION_FORMATIVA.md)","","Todos los OA disciplinares del nivel cuentan con secuencias específicas. Las entradas **integradas** corresponden a habilidades o actitudes observadas dentro de esas clases y no se cuentan como clases independientes. El estado **revisada** permanece en cero hasta registrar revisión profesional competente.","",
  "## Cómo usar este mapa","","1. Elige una asignatura y revisa continuidad, ejes, OA y propuestas.","2. Comprueba el estado editorial y la fuente antes de usar una clase.","3. Revisa ejemplo disciplinar, evidencia, seguridad y acciones ante dificultades.","4. Adapta materiales, apoyos y duración sin cambiar el aprendizaje central.","5. Documenta observaciones y revisión profesional antes de declarar la secuencia revisada.","",
  "## Continuidad con 1° básico","","Cada secuencia comienza recuperando una representación, estrategia, práctica o vocabulario trabajado en 1°. Esa recuperación es diagnóstica: no presume automatización y determina el apoyo necesario antes de ampliar rango, precisión o autonomía.","",
  "## Progresión sugerida","","~~~mermaid","flowchart LR","    A[Recuperar 1°] --> B[Lenguaje y representación]","    B --> C[Práctica con apoyo]","    C --> D[Desempeño individual]","    D --> E[Evidencia y decisión]","~~~","","Esta progresión orienta la enseñanza, pero no sustituye el análisis específico de cada OA.","",
  "## Cobertura","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Pendientes |","|---|---:|---:|---:|---:|---:|"]
 for item in subjects:
  subject_pending=item["classes"]-item["developed"]-item["integrated"]
  lines.append(f"| {item['name']} | {item['oa']} | {item['classes']} | {item['developed']} | {item['integrated']} | {subject_pending} |")
 lines += ["","## Cómo se ve una clase desarrollada","","Una clase desarrollada contiene alineación curricular específica, propósito, meta estudiantil, continuidad con aprendizajes previos, ejemplo concreto, modelado disciplinar, práctica guiada, desempeño individual, materiales, apoyo, profundización, ticket, evidencia, criterios y decisión posterior.","",
  "## Criterios de diseño para 2° básico","","- Recuperación explícita de aprendizajes de 1° sin asumir automatización.","- Aumento gradual de rango, vocabulario, precisión y autonomía.","- Contenido y ejemplos propios del OA y de la disciplina.","- Respuestas simultáneas y evidencia individual.","- Integración observable de habilidades y actitudes sin duplicar clases.","- Materiales viables, seguridad, privacidad, contexto cultural y alternativa sin conectividad.","",
  "## Decisiones con evidencia","","- **Logrado con autonomía:** avanzar o proponer transferencia.","- **En desarrollo:** mantener el OA y entregar apoyo puntual.","- **Requiere otra vía de acceso:** cambiar representación, ejemplo o forma de respuesta.","- **Sin evidencia suficiente:** ofrecer otra oportunidad antes de concluir.","",
  "## Fuente de verdad y límites","",f"El catálogo registra {len(grade_objs)} OA y {len(grade_classes):,} propuestas; {developed} están desarrolladas, {integrated} integradas y {pending} permanecen pendientes.".replace(",",".")+" Ninguna se declara revisada hasta registrar evidencia humana competente.","",
  "## Verificación","","La CI comprueba estados, campos, páginas, paridad documental y reproducibilidad. No sustituye la revisión disciplinar o pedagógica.","",
  "## Documentos relacionados","","- [Centro de documentación](README.md)","- [Guía pedagógica](../TEACHING_GUIDE.md)","- [Metodología](../METHODOLOGY.md)","- [Estado editorial](../EDITORIAL_STATUS.md)","- [Roadmap](../ROADMAP.md)",""]
 return "\n".join(lines)

def grade_two_subject_documentation(subject,objectives,previous_subject=None,next_subject=None):
 profile=GRADE_TWO_SUBJECT_PROFILES[subject["slug"]]
 core=[item for item in objectives if item.get("developed")]
 transverse=[item for item in objectives if item.get("integration")]
 class_count=sum(len(item["phases"]) for item in core)
 integrated_count=sum(len(item["phases"]) for item in transverse)
 axes=sorted({item["axis"] for item in objectives})
 nav=["[⬅️ Índice de 2° básico](README.md)"]
 if previous_subject:nav.append(f"[← {previous_subject['name']}]({previous_subject['slug']}.md)")
 if next_subject:nav.append(f"[{next_subject['name']} →]({next_subject['slug']}.md)")
 lines=[f"# {subject['name']} · 2° básico",""," · ".join(nav),"",f"**{len(core)} OA de contenido · {class_count} clases desarrolladas · {len(transverse)} OA transversales · {integrated_count} experiencias integradas · {len(axes)} ejes curriculares · bloques adaptables a 45 o 90 minutos**","",f"> **Estado editorial:** {class_count} clases desarrolladas y {integrated_count} experiencias transversales integradas. Ninguna revisión humana registrada.","",
  "## 🎯 De qué trata esta asignatura","",profile["purpose"],"",
  "## 🔁 Continuidad con 1° básico","",profile["continuity"],"",
  "## 🧩 Qué problema pedagógico resuelve","",f"La secuencia evita convertir el OA en una actividad aislada. Cada objetivo avanza desde activación y modelado hacia práctica, desempeño individual y evidencia. **Alerta principal:** {profile['barrier']}","",
  "## 🎓 Resultados de aprendizaje del recorrido","","Al trabajar los OA del nivel, se busca que cada estudiante pueda:"
 ]
 lines += ["",*[f"- {value.capitalize()}." for value in profile["outcomes"]],"",
  "## 🧱 Prerrequisitos y punto de entrada","","Cada OA recupera lo aprendido en 1° mediante una tarea breve y observable. No se presupone automatización: si falta una base, se reincorpora con objetos, imágenes, oralidad o demostración antes de ampliar el rango, el vocabulario o la autonomía.","",
  "## 🧭 Cómo recorrer la asignatura","","1. Revisa el OA completo y su eje antes de elegir una clase.","2. Mantén el orden de la secuencia mientras la evidencia confirme que el curso puede avanzar.","3. Usa la adaptación de 45 minutos sin eliminar el desempeño individual.","4. Registra el patrón observado y decide si avanzar, reagrupar o reenseñar.","",f"**Método disciplinar:** {profile['method']}","",
  "## 🧱 Anatomía estable de cada clase","","| Momento | Función pedagógica | Evidencia |","|---|---|---|","| Inicio | Recuperar 1° y diagnosticar sin calificar | Respuesta inicial de todo el curso |","| Modelado | Hacer visible contenido, decisión y error | Reconstrucción del ejemplo o contraste |","| Práctica guiada | Ensayar con apoyo y retroalimentación | Producción compartida y ajustes observables |","| Desempeño individual | Comprobar qué puede hacer cada estudiante | Producto, acción o explicación individual |",f"| Cierre | Contrastar criterios y decidir | {profile['evidence'].capitalize()} |","",
  "## 🗺️ Estructura por ejes","","| Eje | OA | Clases o experiencias |","|---|---:|---:|"]
 for axis in axes:
  pool=[item for item in objectives if item["axis"]==axis]
  if pool:lines.append(f"| {axis} | {len(pool)} | {sum(len(item['phases']) for item in pool)} |")
 lines += ["","~~~mermaid","flowchart LR","    A[Recuperar 1°] --> B[Modelado disciplinar]","    B --> C[Práctica guiada]","    C --> D[Desempeño individual]","    D --> E[Evidencia]","    E --> F{Decisión docente}","    F -->|Avanzar| G[Transferir o profundizar]","    F -->|Apoyar| C","    F -->|Reenseñar| B","~~~","",
  "## 📖 Recorrido OA por OA","","La tabla funciona como índice completo de la asignatura. Distingue clases disciplinares de experiencias transversales integradas y no prescribe un calendario rígido.","","| OA | Tema de la secuencia | Eje | Propuestas | Estado | Planificación |","|---|---|---|---:|---|---|"]
 for item in objectives:
  state="Desarrollada" if item.get("developed") else "Integrada"
  lines.append(f"| `{item['oa_code']}` | {item['topic']} | {item['axis']} | {len(item['phases'])} | {state} | [Abrir ficha Markdown](../../{item['path']}) |")
 lines += ["","## 🔎 Qué observar","",f"**Evidencia central:** {profile['evidence']}.","",f"Los {len(transverse)} OA transversales se distribuyen en {integrated_count} experiencias dentro de las {class_count} clases de contenido. No evalúes personalidad, obediencia, identidad, talento, rapidez, volumen de voz ni presentación como sustitutos del OA.","",
  "## 🧰 Preparación y materiales","","Cada ficha declara materiales concretos. Comprueba disponibilidad, seguridad, tiempo de distribución, alternativa sin conectividad y qué producciones deben conservarse para comparar progreso. Prepara también el apoyo que permite acceder al mismo OA.","",
  "## ⚠️ Error frecuente y recuperación","",f"**Señal de alerta:** {profile['barrier']}","","Recupera el propósito, muestra otro ejemplo o representación, ofrece práctica breve con retroalimentación y solicita una nueva evidencia. Repetir la misma explicación más fuerte o más rápido no constituye reenseñanza.","",
  "## ♿ Acceso y profundización","","- **Acceso:** anticipar vocabulario, fragmentar instrucciones, permitir ensayo oral, usar apoyos concretos o visuales y ofrecer formas pertinentes de respuesta.","- **Profundización:** comparar estrategias, justificar decisiones, crear un caso, mejorar el producto o transferir a una situación nueva.","",
  "## 🔗 Fuente y límites","",f"- [Currículum Nacional · {subject['name']} · 2° básico]({objectives[0]['subject_url']})","- [Guía pedagógica](../../TEACHING_GUIDE.md)","- [Rúbrica de evaluación](../RUBRICA_EVALUACION.md)","- [Protocolo de revisión humana](../REVISION_HUMANA.md)","","El contenido cumple el contrato automatizado del proyecto, pero no se declara revisado por especialistas hasta que exista evidencia registrada.",""]
 if subject["slug"]=="lengua-cultura-pueblos-originarios-ancestrales":
  lines += ["## Resguardos culturales","","- No se inventan palabras, pronunciaciones, grafías, relatos ni significados espirituales.","- La enseñanza se coordina con educador tradicional, autoridad cultural o fuente comunitaria pertinente cuando corresponda.","- Fortalecimiento, rescate y sensibilización se mantienen como contextos diferentes.","- No se reproducen ceremonias, símbolos o prácticas restringidas sin autorización.",""]
 return "\n".join(lines)

GRADE_THREE_CONTINUITY={
 "artes-visuales":"Amplía la exploración de 2° hacia propósitos expresivos más conscientes, decisiones de color, textura y forma, dominio técnico y retroalimentación basada en criterios.",
 "ciencias-naturales":"Avanza desde observación y clasificación hacia investigaciones guiadas con variables, mediciones, modelos, evidencia y comunicación científica segura.",
 "educacion-fisica-salud":"Combina habilidades motrices, incorpora principios predeportivos y aumenta autonomía para regular esfuerzo, seguridad, hábitos y participación equitativa.",
 "historia-geografia-ciencias-sociales":"Pasa de comunidad y patrimonio cercano a sociedades antiguas, referencias planetarias, zonas climáticas, fuentes históricas, instituciones y ciudadanía.",
 "ingles-propuesta":"Amplía textos orales y escritos breves, estrategias de comprensión, interacción flexible, pronunciación inteligible y escritura apoyada con intención comunicativa.",
 "lengua-cultura-pueblos-originarios-ancestrales":"Profundiza oralidad, lectura, escritura, territorio, memoria, cosmovisión y patrimonio según contexto lingüístico, fuente comunitaria y autorización pertinente.",
 "lenguaje-comunicacion":"Aumenta autonomía para comprender, inferir, investigar, conversar, planificar, escribir y revisar textos literarios y no literarios con evidencia.",
 "matematica":"Amplía rango numérico, estrategias de cálculo, multiplicación y división, fracciones, geometría, medición y datos conectando representaciones y comprobación.",
 "musica":"Profundiza cualidades, patrones, forma y contexto musical mediante escucha abundante, canto, instrumentos, improvisación, creación, presentación y reflexión.",
 "orientacion":"Aumenta autonomía en autoconocimiento, regulación emocional, autocuidado, vínculos, intimidad, convivencia, participación y hábitos escolares con protección explícita.",
 "tecnologia":"Amplía el ciclo problema-diseño-planificación-elaboración-prueba-mejora e incorpora presentaciones, documentos y búsquedas seguras con respeto de autoría.",
}

GRADE_THREE_SUBJECT_PROFILES={
 slug: GRADE_ONE_SUBJECT_PROFILES[slug] | {"continuity":continuity}
 for slug,continuity in GRADE_THREE_CONTINUITY.items()
}

def grade_three_page(objs,classes):
 grade_objs,grade_classes,subjects=grade_three_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);pending=sum(x["editorial_status"] in {"secuenciada","borrador"} for x in grade_classes)
 cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas · {item['integrated']} integradas · {item['classes']-item['developed']-item['integrated']} pendientes</span></div><h2>{html.escape(item['name'])}</h2><p><strong>Desarrollo interno completo.</strong> {html.escape(' · '.join(item['axes']))}</p><a href="../docs/3-basico/{item['slug']}.html">Explorar asignatura →</a></article>''' for item in subjects)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="3° básico completo: {developed} clases desarrolladas y {integrated} experiencias integradas en 11 asignaturas."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/3-basico.html"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><title>3° básico completo | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenidos">Saltar a contenidos</a><header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al explorador</a></header>
<main id="contenidos" class="level-shell"><header class="level-hero"><div><p class="eyebrow">Desarrollo pedagógico interno completo · Chile</p><h1>3° básico</h1><p>Las 1.136 propuestas de las once asignaturas están resueltas como {developed} clases disciplinares y {integrated} experiencias transversales integradas. La revisión humana especializada continúa pendiente.</p><div class="hero-actions"><a class="button primary" href="../docs/3-basico/index.html">Abrir mapa del nivel</a><a class="button dark-text" href="../index.html?nivel={quote('3° básico')}#explorar">Explorar clases</a></div></div><aside><span>Estado editorial real</span><strong>{developed} desarrolladas</strong><small>{integrated} integradas · {pending} pendientes · revisión humana pendiente</small></aside></header>
<section class="level-metrics" aria-label="Resumen de 3° básico"><div><strong>{len(grade_objs)}</strong><span>OA inventariados</span></div><div><strong>11</strong><span>asignaturas completas</span></div><div><strong>{developed}</strong><span>clases disciplinares</span></div><div><strong>{integrated}</strong><span>experiencias integradas</span></div></section>
<section class="level-intro"><div><p class="eyebrow">Nivel completo</p><h2>Once recorridos disciplinares con continuidad explícita.</h2></div><p>Cada guía conecta 2° y 3° básico, distingue contenido e integración transversal y documenta propósito, modelado, práctica, evidencia, dificultades, seguridad, acceso y decisión posterior.</p></section><section class="level-grid">{cards}</section>
<section class="level-contract"><div><p class="eyebrow">Lectura honesta</p><h2>Completo no significa revisado.</h2></div><ol><li><strong>{developed} clases disciplinares</strong><span>Los 165 OA de contenido tienen secuencias específicas.</span></li><li><strong>{integrated} experiencias integradas</strong><span>Los 92 OA transversales se observan dentro del contenido.</span></li><li><strong>0 propuestas pendientes</strong><span>No quedan fichas sólo secuenciadas ni borradores.</span></li><li><strong>0 revisiones humanas</strong><span>La verificación automática no sustituye revisión profesional.</span></li></ol></section></main>
<footer class="site-footer"><div><strong>Trayectoria Escolar Chile</strong><span>3° básico completo · revisión humana pendiente</span></div><div><a href="../levels/2-basico.html">2° básico</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''

def grade_three_index_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_three_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes)
 lines=["# 📚 3° básico con desarrollo interno completo","","> [⬅️ Volver al programa](../../README.md) · [🗂️ Índice Markdown](../../CURRICULUM.md) · [📘 Syllabus](../SYLLABUS.md) · [📊 Rúbrica](../RUBRICA_EVALUACION.md)","",f"**{len(grade_classes):,} propuestas · {len(grade_objs)} OA · 11 asignaturas · {developed} clases desarrolladas · {integrated} experiencias integradas · 0 propuestas pendientes · revisión humana pendiente**".replace(",","."),"",
  "## 🎯 De qué trata este nivel","","3° básico amplía autonomía, precisión y capacidad de justificar: lectura y escritura con evidencia, número y relaciones multiplicativas, indagación con variables, pensamiento histórico y geográfico, creación artística y musical, combinación motriz, comunicación en inglés, lengua y cultura situada, convivencia y diseño tecnológico. Cada disciplina conserva su método y explicita continuidad con 2°.","",
  "## 🧩 Problemas que busca resolver","","- Convertir 257 OA en secuencias enseñables y diferenciadas.","- Aumentar complejidad sin suponer automatización de 2°.","- Recoger evidencia individual y usarla para decidir el paso siguiente.","- Integrar habilidades y actitudes sin contarlas como clases adicionales.","- Mantener seguridad física, emocional, digital, cultural y de autoría.","- Separar desarrollo interno, publicación automática y revisión humana.","",
  "## 🎓 Resultados transversales","","Al completar los recorridos del nivel, se espera que cada estudiante pueda:","","- explicar procedimientos, elecciones e interpretaciones con evidencia pertinente;","- trabajar con mayor autonomía sin perder acceso a modelado y apoyos;","- comunicar mediante los lenguajes propios de cada disciplina;","- revisar un producto, estrategia o desempeño usando criterios claros;","- colaborar, cuidarse y cuidar a otras personas sin convertir actitudes en juicios de personalidad.","",
  "## 🧱 Prerrequisitos","","3° básico recupera aprendizajes de 2° mediante evidencia breve y observable. No supone dominio automático: cuando una base falta, reincorpora vocabulario, representación, demostración o práctica focalizada antes de ampliar el desafío.","",
  "## 🧭 Cómo recorrer el programa","","1. Elige asignatura y eje.","2. Lee la continuidad con 2° y la progresión completa.","3. Abre el OA y revisa todas sus clases antes de enseñar.","4. Define evidencia, seguridad, materiales y accesos.","5. Enseña, observa y adapta según resultados.","",
  "## 🗂️ Las 11 asignaturas","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Guía |","|---|---:|---:|---:|---:|---|"]
 for subject in subjects:
  lines.append(f"| {subject['name']} | {subject['oa']} | {subject['classes']} | {subject['developed']} | {subject['integrated']} | [📘 Leer](./{subject['slug']}.md) |")
 lines += ["","## 🧠 Progresión pedagógica común","","~~~mermaid","flowchart TD","    A[Recuperar evidencia de 2°] --> B[Modelado disciplinar]","    B --> C[Práctica guiada]","    C --> D[Desempeño individual]","    D --> E[Evidencia y criterios]","    E --> F{¿Qué necesita el curso?}","    F -->|Dominio| G[Transferir y profundizar]","    F -->|Apoyo puntual| C","    F -->|Otra explicación| B","~~~","",
  "## ⏱️ Ritmo y planificación","","Las secuencias orientan una progresión, no un calendario rígido. Una ficha de 90 minutos puede dividirse o usar su adaptación de 45 minutos, pero debe conservar modelado, práctica focalizada, evidencia individual y decisión posterior.","",
  "## 🧱 Anatomía de una clase","","Cada clase explicita propósito, meta estudiantil, inicio, modelado, práctica guiada, desempeño individual, cierre, materiales, apoyo, profundización, ticket, evidencia, criterios, decisión, tarea flexible, actividades complementarias y acciones ante dificultades.","",
  "## 📊 Cómo se evalúa","","La evidencia se interpreta para avanzar, apoyar, reenseñar o recoger otra muestra. No se transforman automáticamente tickets o actitudes en calificaciones, ni se confunden velocidad, conducta, volumen de voz o presentación con dominio del OA.","",
  "## 🔎 Estados y límites","","- **Desarrollada:** secuencia disciplinar con contenido, evidencia, apoyos y decisiones específicas.","- **Integrada:** habilidad o actitud observada dentro del contenido; no es una clase adicional.","- **Pendiente:** quedan 0 propuestas secuenciadas o borradores en este nivel.","- **Revisada:** requiere evidencia humana competente; actualmente hay 0.","",
  "## 🔗 Documentos relacionados","","- [Mapa técnico de 3° básico](../TERCERO_BASICO.md)","- [Syllabus completo](../SYLLABUS.md)","- [Guía docente](../../TEACHING_GUIDE.md)","- [Rúbrica de evaluación](../RUBRICA_EVALUACION.md)","- [Protocolo de revisión humana](../REVISION_HUMANA.md)","- [Fuentes oficiales](../../OFFICIAL_REFERENCES.md)",""]
 return "\n".join(lines)

def grade_three_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_three_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);pending=sum(x["editorial_status"] in {"secuenciada","borrador"} for x in grade_classes)
 lines=["# 3° básico — mapa de contenidos","",f"> **Desarrollo pedagógico interno completo:** {developed} clases desarrolladas · {integrated} experiencias transversales integradas · {pending} propuestas pendientes · 257 OA · 11 asignaturas · revisión humana pendiente.","","[Programa narrativo de 3° básico](3-basico/README.md) · [Índice Markdown de clases](../CURRICULUM.md) · [Guía pedagógica](../TEACHING_GUIDE.md) · [Evaluación formativa](EVALUACION_FORMATIVA.md)","",
  "Todos los OA disciplinares del nivel cuentan con secuencias específicas. Las entradas integradas corresponden a habilidades o actitudes observadas dentro de esas clases; no duplican el horario. El estado revisada permanece en cero hasta registrar revisión profesional.","",
  "## Cobertura","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Pendientes |","|---|---:|---:|---:|---:|---:|"]
 for item in subjects:
  lines.append(f"| {item['name']} | {item['oa']} | {item['classes']} | {item['developed']} | {item['integrated']} | {item['classes']-item['developed']-item['integrated']} |")
 lines += ["","## Continuidad con 2° básico","","Cada secuencia diagnostica la base disponible y amplía rango, precisión, vocabulario, autonomía o complejidad. Cuando falta un prerrequisito, reincorpora modelado y apoyo sin sustituir el OA de 3°.","",
  "## Contrato de calidad","","- Ejemplos, materiales y errores propios de cada disciplina y OA.","- Inicio, modelado, práctica guiada, desempeño individual y cierre.","- Apoyo que conserva el objetivo y profundización que cambia una condición.","- Tarea flexible, actividades complementarias y matriz de dificultades.","- Integraciones transversales observables, sin evaluar personalidad o identidad.","- Resguardos físicos, emocionales, digitales, culturales y de autoría.","",
  "## Decisiones con evidencia","","- **Logrado con autonomía:** avanzar o transferir.","- **En desarrollo:** mantener el OA con apoyo puntual.","- **Requiere otra vía de acceso:** cambiar representación, ejemplo o forma de respuesta.","- **Sin evidencia suficiente:** ofrecer una nueva oportunidad antes de concluir.","",
  "## Verificación y límite","",f"El catálogo registra {len(grade_objs)} OA y {len(grade_classes):,} propuestas: {developed} desarrolladas, {integrated} integradas y {pending} pendientes.".replace(",",".")," La CI comprueba estructura, cobertura, unicidad, fuentes, licencias y reproducción del contenido. Esto no sustituye revisión disciplinar o pedagógica humana.",""]
 return "\n".join(lines)

def grade_three_subject_documentation(subject,objectives,previous_subject=None,next_subject=None,level="3°",previous_level="2°",profiles=None):
 profile=(profiles or GRADE_THREE_SUBJECT_PROFILES)[subject["slug"]]
 level_slug="4-basico" if level=="4°" else "3-basico"
 core=[item for item in objectives if item.get("developed")];transverse=[item for item in objectives if item.get("integration")]
 class_count=sum(len(item["phases"]) for item in core);integrated_count=sum(len(item["phases"]) for item in transverse);axes=sorted({item["axis"] for item in objectives})
 nav=[f"[⬅️ Índice de {level} básico](README.md)"]
 if previous_subject:nav.append(f"[← {previous_subject['name']}]({previous_subject['slug']}.md)")
 if next_subject:nav.append(f"[{next_subject['name']} →]({next_subject['slug']}.md)")
 lines=[f"# {subject['name']} · {level} básico",""," · ".join(nav),"",f"**{len(core)} OA de contenido · {class_count} clases desarrolladas · {len(transverse)} OA transversales · {integrated_count} experiencias integradas · {len(axes)} ejes curriculares · revisión humana pendiente**","",
  "## 🎯 De qué trata esta asignatura","",profile["purpose"],"",f"## 🔁 Continuidad con {previous_level} básico","",profile["continuity"],"",
  "## 🧩 Qué problema pedagógico resuelve","",f"La secuencia evita convertir el OA en una actividad aislada. Cada objetivo avanza hacia una evidencia disciplinar. **Alerta principal:** {profile['barrier']}","",
  "## 🎓 Resultados de aprendizaje del recorrido","",*[f"- {value.capitalize()}." for value in profile["outcomes"]],"",
  "## 🧱 Prerrequisitos y punto de entrada","",f"Cada OA comienza con una evidencia breve de {previous_level}. Si la base no está disponible, se reincorpora con representación, oralidad, demostración o práctica focalizada antes de ampliar el desafío.","",
  "## 🧭 Cómo recorrer la asignatura","","1. Revisa el OA completo y su eje antes de elegir una clase.","2. Conserva la secuencia mientras la evidencia permita avanzar.","3. Usa la adaptación de 45 minutos sin eliminar el desempeño individual.","4. Registra el patrón observado y decide si avanzar, apoyar o reenseñar.","",f"**Método disciplinar:** {profile['method']}","",
  "## 🧱 Anatomía estable de cada clase","","| Momento | Función pedagógica | Evidencia |","|---|---|---|",f"| Inicio | Recuperar {previous_level} y diagnosticar sin calificar | Respuesta inicial de todo el curso |","| Modelado | Hacer visible contenido, decisión y error | Reconstrucción del ejemplo o contraste |","| Práctica guiada | Ensayar con apoyo y retroalimentación | Producción compartida y ajustes observables |","| Desempeño individual | Comprobar qué puede hacer cada estudiante | Producto, acción o explicación individual |",f"| Cierre | Contrastar criterios y decidir | {profile['evidence'].capitalize()} |","",
  "## 🗺️ Estructura por ejes","","| Eje | OA | Clases o experiencias |","|---|---:|---:|"]
 for axis in axes:
  pool=[item for item in objectives if item["axis"]==axis];lines.append(f"| {axis} | {len(pool)} | {sum(len(item['phases']) for item in pool)} |")
 lines += ["","## 📖 Recorrido OA por OA","","| OA | Tema | Eje | Propuestas | Estado | Planificación |","|---|---|---|---:|---|---|"]
 for item in objectives:
  state="Desarrollada" if item.get("developed") else "Integrada"
  lines.append(f"| `{item['oa_code']}` | {item['topic']} | {item['axis']} | {len(item['phases'])} | {state} | [Abrir ficha Markdown](../../{item['path']}) |")
 if level in {"3° medio", "4° medio"}:
  lines += ["", "## 🧠 Explicación pedagógica OA por OA", "", "Esta sección traduce cada OA a decisiones de enseñanza sin reemplazar su redacción oficial. La explicación, la progresión y la evidencia son elaboración pedagógica interna; el enlace lleva siempre a la fuente MINEDUC."]
  for item in core:
   sequence=item["developed"]
   stages=[lesson["title"].split(":",1)[0].strip() for lesson in sequence.get("lessons",[]) if lesson.get("title")]
   evidence=sequence["lessons"][-1]["evidence"] if sequence.get("lessons") else profile["evidence"]
   lines += [
    "", f"### `{item['oa_code']}` — {item['topic']}", "",
    f"**Qué significa para la enseñanza.** {sequence['pedagogical_explanation']}", "",
    f"**Punto de entrada.** {sequence['prerequisites']}", "",
    f"**Conceptos que deben explicitarse.** {sequence['vocabulary']}.", "",
    f"**Cómo progresa.** {' → '.join(stages)}.", "",
    f"**Qué evidencia demuestra aprendizaje.** {evidence}", "",
    f"**Fuente oficial.** [Currículum Nacional · {item['oa_code']}]({item['source_url']})",
   ]
 lines += ["","## 🔎 Qué observar","",f"**Evidencia central:** {profile['evidence']}.","","La observación se concentra en decisiones, producciones y explicaciones atribuibles al OA, no en personalidad, obediencia, identidad, talento, rapidez o presentación.","",
  "## 🧰 Preparación y materiales","","Cada ficha declara materiales concretos. Comprueba disponibilidad, seguridad, tiempo de distribución, alternativa sin conectividad y qué producciones conservar para comparar progreso. Prepara también el apoyo que permite acceder al mismo OA.","",
  "## ⚠️ Error frecuente y recuperación","",f"**Señal de alerta:** {profile['barrier']}","","Cada clase propone tres dificultades observables con acción inmediata y comprobación. Recupera el propósito, muestra otra representación, ofrece práctica breve y solicita una nueva evidencia; repetir lo mismo más fuerte o más rápido no es reenseñar.","",
  "## ♿ Acceso y profundización","","- Anticipa vocabulario, fragmenta instrucciones y permite ensayo o formatos equivalentes cuando conservan el OA.","- Ajusta materiales, tiempo, espacio, apoyo sensorial o vía de respuesta sin hacer el trabajo por el estudiante.","- Profundiza comparando estrategias, justificando decisiones, mejorando el producto o transfiriendo a un caso nuevo.","",
  "## 🔗 Fuente y límites","",f"- [Currículum Nacional · {subject['name']} · {level} básico]({objectives[0]['subject_url']})","- [Guía pedagógica](../../TEACHING_GUIDE.md)","- [Rúbrica de evaluación](../RUBRICA_EVALUACION.md)","- [Protocolo de revisión humana](../REVISION_HUMANA.md)","","El contenido cumple el contrato automatizado, pero no se declara revisado por especialistas hasta registrar evidencia competente.",""]
 if subject["slug"]=="orientacion":lines += ["## Resguardos de intimidad y protección","","- Se trabaja con casos ficticios y derecho a pasar o responder en privado.","- No se solicitan revelaciones personales, familiares, corporales o emocionales.","- Las situaciones reales se derivan al protocolo institucional; no se investigan ni median en clase.",""]
 if subject["slug"] in {"lengua-cultura-pueblos-originarios-ancestrales", "lengua-indigena"}:lines += ["## Resguardos culturales","","- No se inventan palabras, pronunciaciones, grafías, relatos ni significados espirituales.","- Se coordina con educador tradicional, autoridad cultural o fuente comunitaria pertinente.","- No se reproducen ceremonias, símbolos o prácticas restringidas sin autorización.",""]
 if level=="5°" and subject["slug"] in {"musica", "educacion-fisica-salud"}:
  if subject["slug"]=="musica":
   lines += ["## 📱 Apps de apoyo del aprendizaje","","Algunas clases de `MU05 OA 01`, `MU05 OA 03`, `MU05 OA 04`, `MU05 OA 07` y `MU05 OA 08` incorporan de manera opcional Pañuelo al Viento, Mi Aventura con el Violín o Mi Aventura con la Guitarra. Cada ficha indica propósito, mediación adulta o docente, límite de la evidencia y alternativa equivalente sin aplicación.","","[Consultar análisis, correspondencia curricular y resguardos](../APPS_APOYO_APRENDIZAJE.md)",""]
  else:
   lines += ["## 📱 App de apoyo del aprendizaje","","Dos clases de `EF05 OA 05` incorporan opcionalmente Pañuelo al Viento para observar, ensayar y ajustar pulso, trayectoria y coordinación. La ejecución segura y la explicación motriz constituyen la evidencia; la app no reemplaza demostración, consentimiento, contextualización cultural ni alternativa sin dispositivo.","","[Consultar análisis, correspondencia curricular y resguardos](../APPS_APOYO_APRENDIZAJE.md)",""]
 return "\n".join(lines)

def grade_four_math_documentation(objs,classes):
 objectives=[item for item in objs if item["course_order"]==4 and item["subject_slug"]=="matematica"]
 math_classes=[item for item in classes if item["course_order"]==4 and item["subject_slug"]=="matematica"]
 core=[item for item in objectives if item.get("developed")];transverse=[item for item in objectives if item.get("integration")]
 developed=sum(item["editorial_status"]=="desarrollada" for item in math_classes);integrated=sum(item["editorial_status"]=="integrada" for item in math_classes)
 lines=["# Matemática · 4° básico","","[⬅️ Centro de documentación](../README.md) · [Índice curricular](../../CURRICULUM.md) · [Guía pedagógica](../../TEACHING_GUIDE.md)","",f"**{len(core)} OA de contenido · {developed} clases desarrolladas · {len(transverse)} OA transversales · {integrated} experiencias integradas · 0 propuestas pendientes en la asignatura · revisión humana pendiente**","",
  "## 🎯 De qué trata esta asignatura","","Matemática de 4° básico amplía el sistema decimal hasta 10.000, consolida las cuatro operaciones, introduce decimales y profundiza fracciones, patrones, ecuaciones, geometría, medición, área, volumen, datos y azar. Cada secuencia exige representar, explicar y comprobar; la rapidez no sustituye la comprensión.","",
  "## 🔁 Continuidad con 3° básico","","Recupera valor posicional, hechos multiplicativos, división, fracciones, transformaciones, ángulos, tiempo, longitud y gráficos de 3°. El diagnóstico inicial determina qué representación o modelado reincorporar antes de aumentar rango, formalización y autonomía.","",
  "## 🎓 Resultados de aprendizaje del recorrido","","- Seleccionar estrategias y representaciones según la estructura del problema.","- Explicar el valor posicional y comprobar operaciones con estimación o inversas.","- Coordinar fracciones, decimales y medidas sin perder la unidad de referencia.","- Construir y analizar figuras, áreas, volúmenes, tablas y gráficos con criterios matemáticos.","- Comunicar conclusiones y revisar errores sin asociar desempeño con rapidez o capacidad fija.","",
  "## 🧱 Prerrequisitos y punto de entrada","","Cada OA comienza con evidencia breve sobre la base de 3°. Si falta, se reduce temporalmente rango o carga, se recuperan materiales, dibujos, tablas o rectas y luego se retorna al desafío de 4°; el apoyo no reemplaza la decisión matemática del estudiante.","",
  "## 🧭 Cómo recorrer la asignatura","","1. Lee el OA y todas sus clases antes de calendarizar.","2. Define la evidencia individual y la comprobación esperada.","3. Prepara representaciones concretas, pictóricas y simbólicas pertinentes.","4. Mantén el orden mientras la evidencia muestre progresión; reenseña con otro caso cuando no.","5. Integra habilidades y actitudes durante la resolución, sin duplicarlas como clases.","",
  "## 🧱 Anatomía estable de cada clase","","| Momento | Función | Evidencia |","|---|---|---|","| Inicio | Recuperar una base y anticipar una decisión | Respuesta inicial de todo el curso |","| Modelado | Hacer visible representación, estrategia y comprobación | Reconstrucción o contraste del ejemplo |","| Práctica guiada | Comparar dos variaciones y retroalimentar | Solución compartida mejorada |","| Desempeño individual | Resolver un caso nuevo | Representación, procedimiento y respuesta |","| Cierre | Explicar y decidir el paso siguiente | Ticket con criterio de comprobación |","",
  "## 🗺️ Estructura por ejes","","| Eje | OA de contenido | Clases |","|---|---:|---:|"]
 for axis in sorted({item["axis"] for item in core}):
  pool=[item for item in core if item["axis"]==axis];lines.append(f"| {axis} | {len(pool)} | {sum(len(item['phases']) for item in pool)} |")
 lines += ["","## 📖 Recorrido OA por OA","","| OA | Tema | Eje | Clases | Planificación |","|---|---|---|---:|---|"]
 for item in core:
  lines.append(f"| `{item['oa_code']}` | {item['topic']} | {item['axis']} | {len(item['phases'])} | [Abrir ficha Markdown](../../{item['path']}) |")
 lines += ["","## 🔎 Qué observar","","La evidencia central combina una representación pertinente, un procedimiento comprensible, una respuesta con unidad cuando corresponde y una comprobación independiente. Los 20 OA transversales se distribuyen en 87 experiencias dentro de las 118 clases; no se evalúan como personalidad, obediencia o rapidez.","",
  "## 🧰 Preparación y materiales","","Comprueba disponibilidad y legibilidad de bloques base diez, tarjetas, rectas, cuadrículas, fracciones, relojes, reglas, transportadores, cubos y datos ficticios según el OA. Toda actividad digital conserva alternativa manual y ningún problema exige revelar información económica o familiar real.","",
  "## ⚠️ Error frecuente y recuperación","","Cuando aparece una respuesta correcta sin explicación, una regla aplicada fuera de contexto o una confusión de unidad, vuelve a dos casos contrastantes y una representación que haga visible la relación. Solicita después una nueva evidencia individual; repetir más ejercicios iguales no constituye reenseñanza.","",
  "## ♿ Acceso y profundización","","- **Acceso:** anticipar vocabulario, segmentar datos, permitir manipulación, tablas o lectura compartida y ofrecer formas pertinentes de respuesta.","- **Profundización:** cambiar una condición, comparar estrategias, crear un contraejemplo, optimizar una solución o transferirla a otra representación.","",
  "## 🔗 Fuente y límites","","- [Currículum Nacional · Matemática · 4° básico](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico)","- [Guía pedagógica](../../TEACHING_GUIDE.md)","- [Rúbrica de evaluación](../RUBRICA_EVALUACION.md)","- [Protocolo de revisión humana](../REVISION_HUMANA.md)","","La asignatura cumple el contrato automatizado del proyecto, pero permanece pendiente de revisión humana disciplinar y pedagógica.",""]
 return "\n".join(lines)

GRADE_FOUR_SUBJECT_PROFILES={
 slug: GRADE_ONE_SUBJECT_PROFILES[slug] | {"continuity":f"Desde 3° básico, {continuity[0].lower()+continuity[1:]} La secuencia de 4° aumenta precisión, autonomía, contraste de evidencia y transferencia sin retirar apoyos por calendario."}
 for slug,continuity in GRADE_THREE_CONTINUITY.items()
}

def grade_four_summary(objs,classes):
 return grade_summary(objs,classes,4)

def grade_four_page(objs,classes):
 grade_objs,grade_classes,subjects=grade_four_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);pending=sum(x["editorial_status"] in {"secuenciada","borrador"} for x in grade_classes)
 cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas · {item['integrated']} integradas · {item['classes']-item['developed']-item['integrated']} pendientes</span></div><h2>{html.escape(item['name'])}</h2><p><strong>Desarrollo interno completo.</strong> {html.escape(' · '.join(item['axes']))}</p><a href="../docs/4-basico/{item['slug']}.html">Explorar asignatura →</a></article>''' for item in subjects)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="4° básico completo: {developed} clases desarrolladas y {integrated} experiencias integradas en 11 asignaturas."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/4-basico.html"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><title>4° básico completo | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenidos">Saltar a contenidos</a><header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al explorador</a></header>
<main id="contenidos" class="level-shell"><header class="level-hero"><div><p class="eyebrow">Desarrollo pedagógico interno completo · Chile</p><h1>4° básico</h1><p>Las {len(grade_classes):,} propuestas de las once asignaturas están resueltas como {developed} clases disciplinares y {integrated} experiencias transversales integradas. La revisión humana especializada continúa pendiente.</p><div class="hero-actions"><a class="button primary" href="../docs/4-basico/index.html">Abrir mapa del nivel</a><a class="button dark-text" href="../index.html?nivel={quote('4° básico')}#explorar">Explorar clases</a></div></div><aside><span>Estado editorial real</span><strong>{developed} desarrolladas</strong><small>{integrated} integradas · {pending} pendientes · revisión humana pendiente</small></aside></header>
<section class="level-metrics" aria-label="Resumen de 4° básico"><div><strong>{len(grade_objs)}</strong><span>OA inventariados</span></div><div><strong>11</strong><span>asignaturas completas</span></div><div><strong>{developed}</strong><span>clases disciplinares</span></div><div><strong>{integrated}</strong><span>experiencias integradas</span></div></section>
<section class="level-intro"><div><p class="eyebrow">Nivel completo</p><h2>Once recorridos con método disciplinar y continuidad desde 3°.</h2></div><p>Las clases no comparten una receta vacía: lectura y escritura trabajan con textos y audiencias; ciencias con preguntas y evidencia; historia con fuentes y contexto; artes con decisiones expresivas; movimiento, música, orientación, tecnología, inglés y lengua/cultura aplican sus propios resguardos.</p></section><section class="level-grid">{cards}</section>
<section class="level-contract"><div><p class="eyebrow">Lectura honesta</p><h2>Completo no significa revisado.</h2></div><ol><li><strong>{developed} clases disciplinares</strong><span>Los OA de contenido tienen secuencias específicas y diferenciadas.</span></li><li><strong>{integrated} experiencias integradas</strong><span>Habilidades y actitudes se observan dentro del contenido.</span></li><li><strong>0 propuestas pendientes</strong><span>No quedan fichas sólo secuenciadas ni borradores.</span></li><li><strong>0 revisiones humanas</strong><span>La verificación automática no sustituye revisión profesional.</span></li></ol></section></main>
<footer class="site-footer"><div><strong>Trayectoria Escolar Chile</strong><span>4° básico completo · revisión humana pendiente</span></div><div><a href="../levels/3-basico.html">3° básico</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''.replace("1,195","1.195")

def grade_four_index_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_four_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes)
 lines=["# 📚 4° básico con desarrollo interno completo","","> [⬅️ Volver al programa](../../README.md) · [🗂️ Índice Markdown](../../CURRICULUM.md) · [📘 Syllabus](../SYLLABUS.md) · [📊 Rúbrica](../RUBRICA_EVALUACION.md)","",f"**{len(grade_classes):,} propuestas · {len(grade_objs)} OA · 11 asignaturas · {developed} clases desarrolladas · {integrated} experiencias integradas · 0 propuestas pendientes · revisión humana pendiente**".replace(",","."),"",
  "## 🎯 De qué trata este nivel","","4° básico consolida aprendizajes del primer ciclo y exige mayor precisión, autonomía y fundamentación: lectura y escritura sostenidas, números hasta 10.000, indagación de ecosistemas, materia, fuerzas y Tierra, civilizaciones americanas, ciudadanía, creación artística y musical, control motriz, inglés comunicativo, lengua y cultura situada, desarrollo afectivo y diseño tecnológico.","",
  "## 🧩 Problemas que busca resolver","",f"- Convertir {len(grade_objs)} OA en secuencias enseñables, claras y diferenciadas.","- Elevar la demanda de 4° sin suponer dominio automático de 3°.","- Evitar clases robóticas mediante anclas, errores, evidencias y decisiones propias de cada OA.","- Integrar habilidades y actitudes sin contarlas como clases adicionales.","- Mantener seguridad física, emocional, digital, cultural y de autoría.","",
  "## 🧭 Cómo recorrer el programa","","1. Elige asignatura y eje.","2. Lee continuidad, prerrequisitos y progresión completa.","3. Abre el OA y revisa todas sus clases antes de enseñar.","4. Define evidencia, materiales, seguridad y accesos.","5. Enseña, observa y adapta según resultados.","",
  "## 🗂️ Las 11 asignaturas","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Guía |","|---|---:|---:|---:|---:|---|"]
 for subject in subjects:lines.append(f"| {subject['name']} | {subject['oa']} | {subject['classes']} | {subject['developed']} | {subject['integrated']} | [📘 Leer](./{subject['slug']}.md) |")
 lines += ["","## 🧠 Progresión pedagógica común","","~~~mermaid","flowchart TD","    A[Recuperar evidencia de 3°] --> B[Modelado disciplinar]","    B --> C[Práctica guiada]","    C --> D[Desempeño individual]","    D --> E[Evidencia y criterios]","    E --> F{¿Qué necesita el curso?}","    F -->|Dominio| G[Transferir y profundizar]","    F -->|Apoyo puntual| C","    F -->|Otra explicación| B","~~~","",
  "## 🎓 Resultados transversales","","Al completar los recorridos, se espera que cada estudiante pueda explicar decisiones con evidencia, comunicar mediante lenguajes disciplinares, revisar productos o desempeños con criterios y transferir lo aprendido a situaciones nuevas.","",
  "## 🧱 Prerrequisitos","","4° recupera evidencia de 3° y no supone automatización. Cuando una base falta, la secuencia reincorpora vocabulario, representación, demostración o práctica focalizada antes de ampliar el desafío.","",
  "## 🧱 Anatomía y diferenciación","","Cada clase explicita propósito, meta, ancla disciplinar, modelado, práctica guiada, desempeño individual, evidencia, criterios, apoyo, profundización, dificultades observables, decisión posterior y alternativa sin conectividad. La estructura es estable; el contenido, las decisiones y las evidencias cambian OA por OA y asignatura por asignatura.","",
  "## 📊 Cómo se evalúa","","La evidencia sirve para avanzar, apoyar, reenseñar o recoger otra muestra. No se confunden velocidad, conducta, volumen de voz, presentación, identidad o cumplimiento con dominio del OA.","",
  "## 🔎 Estados y límites","","- **Desarrollada:** secuencia disciplinar con decisiones, evidencia y apoyos específicos.","- **Integrada:** habilidad o actitud observada dentro del contenido; no es una clase adicional.","- **Pendiente:** quedan 0 propuestas secuenciadas o borradores en este nivel.","- **Revisada:** requiere evidencia humana competente; actualmente hay 0.","",
  "## 🔗 Documentos relacionados","","- [Mapa técnico de 4° básico](../CUARTO_BASICO.md)","- [Syllabus completo](../SYLLABUS.md)","- [Guía docente](../../TEACHING_GUIDE.md)","- [Rúbrica de evaluación](../RUBRICA_EVALUACION.md)","- [Protocolo de revisión humana](../REVISION_HUMANA.md)",""]
 return "\n".join(lines)

def grade_four_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_four_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);pending=sum(x["editorial_status"] in {"secuenciada","borrador"} for x in grade_classes)
 lines=["# 4° básico — mapa de contenidos","",f"> **Desarrollo pedagógico interno completo:** {developed} clases desarrolladas · {integrated} experiencias transversales integradas · {pending} propuestas pendientes · {len(grade_objs)} OA · 11 asignaturas · revisión humana pendiente.","","[Programa narrativo de 4° básico](4-basico/README.md) · [Índice Markdown de clases](../CURRICULUM.md) · [Guía pedagógica](../TEACHING_GUIDE.md) · [Evaluación formativa](EVALUACION_FORMATIVA.md)","",
  "Todos los OA disciplinares cuentan con secuencias específicas. Las entradas integradas corresponden a habilidades o actitudes observadas dentro de esas clases; no duplican el horario. El estado revisada permanece en cero hasta registrar revisión profesional.","","## Cobertura","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Pendientes |","|---|---:|---:|---:|---:|---:|"]
 for item in subjects:lines.append(f"| {item['name']} | {item['oa']} | {item['classes']} | {item['developed']} | {item['integrated']} | {item['classes']-item['developed']-item['integrated']} |")
 lines += ["","## Continuidad con 3° básico","","Cada secuencia diagnostica la base disponible y amplía precisión, vocabulario, autonomía, contraste y transferencia. Cuando falta un prerrequisito, reincorpora modelado y apoyo sin sustituir el OA de 4°.","",
  "## Contrato de calidad","","- Anclas, ejemplos, materiales, decisiones y errores propios de cada disciplina y OA.","- Inicio, modelado, práctica guiada, desempeño individual y cierre.","- Apoyo que conserva el objetivo y profundización que cambia una condición.","- Integraciones transversales observables sin evaluar personalidad, identidad o cuerpo.","- Resguardos físicos, emocionales, digitales, culturales, de privacidad y autoría.","",
  "## Verificación y límite","",f"El catálogo registra {len(grade_objs)} OA y {len(grade_classes):,} propuestas: {developed} desarrolladas, {integrated} integradas y {pending} pendientes.".replace(",","."),"La CI comprueba estructura, cobertura, unicidad, fuentes, licencias y reproducción del contenido. Esto no sustituye revisión disciplinar o pedagógica humana.",""]
 return "\n".join(lines)

def grade_five_summary(objs,classes):
 return grade_summary(objs,classes,5)
GRADE_FIVE_SLUGS=("matematica","lenguaje-comunicacion","ciencias-naturales","historia-geografia-ciencias-sociales","artes-visuales","musica","educacion-fisica-salud","ingles","ingles-propuesta","lengua-cultura-pueblos-originarios-ancestrales","orientacion","tecnologia")
GRADE_FIVE_SUBJECT_PROFILES={
 slug: GRADE_ONE_SUBJECT_PROFILES["ingles-propuesta" if slug=="ingles" else slug] | {
  "continuity":f"Desde 4° básico, {GRADE_THREE_CONTINUITY['ingles-propuesta' if slug=='ingles' else slug][0].lower()+GRADE_THREE_CONTINUITY['ingles-propuesta' if slug=='ingles' else slug][1:]} En 5° aumenta la autonomía, el contraste de evidencia y la transferencia sin retirar apoyos por calendario."
 }
 for slug in GRADE_FIVE_SLUGS
}

def grade_five_page(objs,classes):
 grade_objs,grade_classes,subjects=grade_five_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);pending=sum(x["editorial_status"] in {"secuenciada","borrador"} for x in grade_classes)
 cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas · {item['integrated']} integradas · {item['classes']-item['developed']-item['integrated']} pendientes</span></div><h2>{html.escape(item['name'])}</h2><p><strong>Desarrollo interno completo.</strong> {html.escape(' · '.join(item['axes']))}</p><a href="../docs/5-basico/{item['slug']}.html">Explorar asignatura →</a></article>''' for item in subjects)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="5° básico completo: {developed} clases desarrolladas y {integrated} experiencias integradas en 12 denominaciones curriculares."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/5-basico.html"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><title>5° básico completo | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenidos">Saltar a contenidos</a><header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al explorador</a></header>
<main id="contenidos" class="level-shell"><header class="level-hero"><div><p class="eyebrow">Desarrollo pedagógico interno completo · Chile</p><h1>5° básico</h1><p>Las {len(grade_classes):,} propuestas de las doce denominaciones curriculares están resueltas como {developed} clases disciplinares y {integrated} experiencias transversales integradas. La revisión humana especializada continúa pendiente.</p><div class="hero-actions"><a class="button primary" href="../docs/5-basico/index.html">Abrir mapa del nivel</a><a class="button dark-text" href="../index.html?nivel={quote('5° básico')}#explorar">Explorar clases</a></div></div><aside><span>Estado editorial real</span><strong>{developed} desarrolladas</strong><small>{integrated} integradas · {pending} pendientes · revisión humana pendiente</small></aside></header>
<section class="level-metrics" aria-label="Resumen de 5° básico"><div><strong>{len(grade_objs)}</strong><span>OA inventariados</span></div><div><strong>12</strong><span>denominaciones completas</span></div><div><strong>{developed}</strong><span>clases disciplinares</span></div><div><strong>{integrated}</strong><span>experiencias integradas</span></div></section>
<section class="level-intro"><div><p class="eyebrow">Nivel completo</p><h2>Doce recorridos con método disciplinar y continuidad desde 4°.</h2></div><p>Las clases mantienen una anatomía clara, pero no una receta vacía: textos y audiencias, problemas y representaciones, indagaciones, fuentes históricas, decisiones expresivas, movimiento seguro, escucha, comunicación en inglés, aprendizaje cultural situado, autocuidado y diseño tecnológico.</p></section><section class="level-grid">{cards}</section>
<section class="level-contract"><div><p class="eyebrow">Lectura honesta</p><h2>Completo no significa revisado.</h2></div><ol><li><strong>{developed} clases disciplinares</strong><span>Los OA de contenido tienen secuencias específicas y diferenciadas.</span></li><li><strong>{integrated} experiencias integradas</strong><span>Habilidades y actitudes se observan dentro del contenido.</span></li><li><strong>0 propuestas pendientes</strong><span>No quedan fichas sólo secuenciadas ni borradores.</span></li><li><strong>0 revisiones humanas</strong><span>La verificación automática no sustituye revisión profesional.</span></li></ol></section></main>
<footer class="site-footer"><div><strong>Trayectoria Escolar Chile</strong><span>5° básico completo · revisión humana pendiente</span></div><div><a href="../levels/4-basico.html">4° básico</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''.replace("1,340","1.340")

def grade_five_index_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_five_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);pending=sum(x["editorial_status"] in {"secuenciada","borrador"} for x in grade_classes)
 lines=["# 📚 5° básico con desarrollo interno completo","","> [⬅️ Volver al programa](../../README.md) · [🗂️ Índice Markdown](../../CURRICULUM.md) · [📘 Syllabus](../SYLLABUS.md) · [📊 Rúbrica](../RUBRICA_EVALUACION.md)","",f"**{len(grade_classes):,} propuestas · {len(grade_objs)} OA · 12 denominaciones curriculares · {developed} clases desarrolladas · {integrated} experiencias integradas · {pending} propuestas pendientes · revisión humana pendiente**".replace(",","."),"",
  "## 🎯 De qué trata este nivel","","5° básico amplía lectura, argumentación, razonamiento matemático, indagación científica, historia colonial, geografía de Chile, ciudadanía, creación artística y musical, desempeño motriz, comunicación en inglés, aprendizaje situado de lengua y cultura, desarrollo afectivo y diseño tecnológico.","",
  "## 🧩 Problemas que busca resolver","",f"- Convertir {len(grade_objs)} OA en secuencias enseñables, claras y diferenciadas.","- Elevar la demanda sin suponer dominio automático de 4°.","- Evitar clases robóticas mediante anclas, errores, evidencias y decisiones propias de cada OA.","- Integrar habilidades y actitudes sin contarlas como clases adicionales.","- Mantener seguridad física, emocional, digital, cultural y de autoría.","",
  "## 🧭 Cómo recorrer el programa","","1. Elige asignatura y eje.","2. Lee continuidad, prerrequisitos y progresión completa.","3. Abre el OA y revisa todas sus clases antes de enseñar.","4. Define evidencia, materiales, seguridad y accesos.","5. Enseña, observa y adapta según resultados.","",
  "## 🗂️ Las 12 denominaciones curriculares","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Guía |","|---|---:|---:|---:|---:|---|"]
 for subject in subjects:lines.append(f"| {subject['name']} | {subject['oa']} | {subject['classes']} | {subject['developed']} | {subject['integrated']} | [📘 Leer](./{subject['slug']}.md) |")
 lines += ["","## 🧠 Progresión pedagógica común","","~~~mermaid","flowchart TD","    A[Recuperar evidencia de 4°] --> B[Modelado disciplinar]","    B --> C[Práctica guiada]","    C --> D[Desempeño individual]","    D --> E[Evidencia y criterios]","    E --> F{¿Qué necesita el curso?}","    F -->|Dominio| G[Transferir y profundizar]","    F -->|Apoyo puntual| C","    F -->|Otra explicación| B","~~~","",
  "## 🎓 Resultados transversales","","Al completar los recorridos, se espera explicar decisiones con evidencia, comunicar mediante lenguajes disciplinares, revisar productos o desempeños con criterios y transferir lo aprendido a situaciones nuevas.","",
  "## 🧱 Prerrequisitos","","5° recupera evidencia de 4° y no supone automatización. Cuando una base falta, reincorpora vocabulario, representación, demostración o práctica focalizada antes de ampliar el desafío.","",
  "## 🧱 Anatomía y diferenciación","","Cada clase explicita propósito, meta, ancla disciplinar, modelado, práctica guiada, desempeño individual, evidencia, criterios, apoyo, profundización, dificultades observables, decisión posterior y alternativa sin conectividad. La estructura es estable; el contenido, las decisiones y las evidencias cambian OA por OA.","",
  "## 📊 Cómo se evalúa","","La evidencia sirve para avanzar, apoyar, reenseñar o recoger otra muestra. No se confunden velocidad, conducta, volumen de voz, presentación, identidad o cumplimiento con dominio del OA.","",
  "## 🔎 Estados y límites","","- **Desarrollada:** secuencia disciplinar con decisiones, evidencia y apoyos específicos.","- **Integrada:** habilidad o actitud observada dentro del contenido; no es una clase adicional.","- **Pendiente:** quedan 0 propuestas secuenciadas o borradores en este nivel.","- **Revisada:** requiere evidencia humana competente; actualmente hay 0.","",
  "## 🔗 Documentos relacionados","","- [Mapa técnico de 5° básico](../QUINTO_BASICO.md)","- [Apps de apoyo del aprendizaje](../APPS_APOYO_APRENDIZAJE.md)","- [Syllabus completo](../SYLLABUS.md)","- [Guía docente](../../TEACHING_GUIDE.md)","- [Rúbrica de evaluación](../RUBRICA_EVALUACION.md)","- [Protocolo de revisión humana](../REVISION_HUMANA.md)",""]
 return "\n".join(lines)

def grade_five_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_five_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);pending=sum(x["editorial_status"] in {"secuenciada","borrador"} for x in grade_classes)
 lines=["# 5° básico — mapa de contenidos","",f"> **Desarrollo pedagógico interno completo:** {developed} clases desarrolladas · {integrated} experiencias transversales integradas · {pending} propuestas pendientes · {len(grade_objs)} OA · 12 denominaciones curriculares · revisión humana pendiente.","","[Programa narrativo de 5° básico](5-basico/README.md) · [Índice Markdown de clases](../CURRICULUM.md) · [Guía pedagógica](../TEACHING_GUIDE.md) · [Evaluación formativa](EVALUACION_FORMATIVA.md) · [Apps de apoyo](APPS_APOYO_APRENDIZAJE.md)","","Todos los OA disciplinares cuentan con secuencias específicas. Las entradas integradas corresponden a habilidades o actitudes observadas dentro de esas clases; no duplican el horario. El estado revisada permanece en cero hasta registrar revisión profesional.","","## Cobertura","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Pendientes |","|---|---:|---:|---:|---:|---:|"]
 for item in subjects:lines.append(f"| {item['name']} | {item['oa']} | {item['classes']} | {item['developed']} | {item['integrated']} | {item['classes']-item['developed']-item['integrated']} |")
 lines += ["","## Continuidad con 4° básico","","Cada secuencia diagnostica la base disponible y amplía precisión, vocabulario, autonomía, contraste y transferencia. Cuando falta un prerrequisito, reincorpora modelado y apoyo sin sustituir el OA de 5°.","","## Contrato de calidad","","- Anclas, ejemplos, materiales, decisiones y errores propios de cada disciplina y OA.","- Inicio, modelado, práctica guiada, desempeño individual y cierre.","- Apoyo que conserva el objetivo y profundización que cambia una condición.","- Integraciones transversales observables sin evaluar personalidad, identidad o cuerpo.","- Resguardos físicos, emocionales, digitales, culturales, de privacidad y autoría.","","## Verificación y límite","",f"El catálogo registra {len(grade_objs)} OA y {len(grade_classes):,} propuestas: {developed} desarrolladas, {integrated} integradas y {pending} pendientes.".replace(",","."),"La CI comprueba estructura, cobertura, unicidad, fuentes, licencias y reproducción del contenido. Esto no sustituye revisión disciplinar o pedagógica humana.",""]
 return "\n".join(lines)

GRADE_SIX_SUBJECT_PROFILES={
 slug:profile | {"continuity":f"Desde 5° básico, {profile['continuity'][0].lower()+profile['continuity'][1:]} En 6° aumenta la autonomía, la formalización, el contraste de evidencia y la transferencia hacia el cierre de la educación básica inicial."}
 for slug,profile in GRADE_FIVE_SUBJECT_PROFILES.items()
}
GRADE_SIX_SUBJECT_PROFILES["matematica"] |= {
 "continuity":"Desde 5° básico, amplía números, fracciones y decimales hacia razones y porcentajes; formaliza relaciones con letras y ecuaciones; y profundiza construcción geométrica, superficie, volumen, ángulos, distribuciones y azar.",
 "barrier":"aplicar una regla por apariencia sin conservar la relación, la unidad o una comprobación independiente",
}

def grade_six_summary(objs,classes):
 return grade_summary(objs,classes,6)

def grade_six_page(objs,classes):
 grade_objs,grade_classes,subjects=grade_six_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);pending=sum(x["editorial_status"] in {"secuenciada","borrador"} for x in grade_classes)
 cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas · {item['integrated']} integradas · {item['classes']-item['developed']-item['integrated']} pendientes</span></div><h2>{html.escape(item['name'])}</h2><p><strong>Desarrollo interno completo.</strong> {html.escape(' · '.join(item['axes']))}</p><a href="../docs/6-basico/{item['slug']}.html">Explorar asignatura →</a></article>''' for item in subjects)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="6° básico completo: {developed} clases desarrolladas y {integrated} experiencias integradas en 12 denominaciones curriculares."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/6-basico.html"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><title>6° básico completo | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenidos">Saltar a contenidos</a><header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al explorador</a></header>
<main id="contenidos" class="level-shell"><header class="level-hero"><div><p class="eyebrow">Desarrollo pedagógico interno completo · Chile</p><h1>6° básico</h1><p>Las {len(grade_classes):,} propuestas de las doce denominaciones curriculares están resueltas como {developed} clases disciplinares y {integrated} experiencias transversales integradas. La revisión humana especializada continúa pendiente.</p><div class="hero-actions"><a class="button primary" href="../docs/6-basico/index.html">Abrir mapa del nivel</a><a class="button dark-text" href="../index.html?nivel={quote('6° básico')}#explorar">Explorar clases</a></div></div><aside><span>Estado editorial real</span><strong>{developed} desarrolladas</strong><small>{integrated} integradas · {pending} pendientes · revisión humana pendiente</small></aside></header>
<section class="level-metrics"><div><strong>{len(grade_objs)}</strong><span>OA inventariados</span></div><div><strong>12</strong><span>denominaciones completas</span></div><div><strong>{developed}</strong><span>clases disciplinares</span></div><div><strong>{integrated}</strong><span>experiencias integradas</span></div></section><section class="level-intro"><div><p class="eyebrow">Nivel completo</p><h2>Doce recorridos con método disciplinar y continuidad desde 5°.</h2></div><p>Las clases sostienen una anatomía clara sin uniformar las disciplinas: textos y audiencias, problemas y representaciones, indagaciones, fuentes, decisiones expresivas, movimiento seguro, escucha, comunicación en inglés, aprendizaje cultural situado, autocuidado y diseño tecnológico.</p></section><section class="level-grid">{cards}</section><section class="level-contract"><div><p class="eyebrow">Lectura honesta</p><h2>Completo no significa revisado.</h2></div><ol><li><strong>{developed} clases disciplinares</strong><span>Todos los OA de contenido tienen secuencias específicas.</span></li><li><strong>{integrated} experiencias integradas</strong><span>Habilidades y actitudes se observan dentro del contenido.</span></li><li><strong>0 propuestas pendientes</strong><span>No quedan fichas sólo secuenciadas ni borradores.</span></li><li><strong>0 revisiones humanas</strong><span>La verificación automática no sustituye revisión profesional.</span></li></ol></section></main><footer class="site-footer"><div><strong>6° básico completo</strong><span>Desarrollo interno completo · revisión humana pendiente</span></div><div><a href="../levels/5-basico.html">5° básico</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''.replace("1,374","1.374")

def grade_six_index_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_six_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);pending=sum(x["editorial_status"] in {"secuenciada","borrador"} for x in grade_classes)
 lines=["# 📚 6° básico con desarrollo interno completo","","> [⬅️ Volver al programa](../../README.md) · [🗂️ Índice Markdown](../../CURRICULUM.md) · [📘 Syllabus](../SYLLABUS.md) · [📊 Rúbrica](../RUBRICA_EVALUACION.md)","",f"**{len(grade_classes):,} propuestas · {len(grade_objs)} OA · 12 denominaciones curriculares · {developed} clases desarrolladas · {integrated} experiencias integradas · {pending} propuestas pendientes · revisión humana pendiente**".replace(",","."),"","## 🎯 De qué trata este nivel","","6° básico consolida el segundo ciclo inicial: aumenta formalización matemática, lectura y producción sostenidas, indagación científica, comprensión histórica y territorial, ciudadanía, creación, desempeño motriz, comunicación en inglés, aprendizaje cultural situado, autocuidado y diseño tecnológico.","","## 🧩 Problemas que busca resolver","",f"- Convertir {len(grade_objs)} OA en secuencias enseñables, claras y diferenciadas.","- Cerrar la continuidad con 5° sin suponer dominio automático.","- Evitar clases robóticas mediante anclas, errores, evidencias y decisiones propias de cada OA.","- Integrar habilidades y actitudes sin contarlas como clases adicionales.","- Mantener seguridad física, emocional, digital, cultural y de autoría.","","## 🗂️ Las 12 denominaciones curriculares","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Guía |","|---|---:|---:|---:|---:|---|"]
 for subject in subjects:
  lines.append(f"| {subject['name']} | {subject['oa']} | {subject['classes']} | {subject['developed']} | {subject['integrated']} | [📘 Leer](./{subject['slug']}.md) |")
 lines += ["","## ✅ Resultados esperados del nivel","","Al finalizar los recorridos, el estudiantado produce evidencia cada vez más autónoma: explica decisiones, contrasta fuentes o estrategias, revisa sus producciones y transfiere lo aprendido sin perder los criterios propios de cada asignatura.","","## 🧠 Progresión pedagógica común","","~~~mermaid","flowchart TD","    A[Recuperar evidencia de 5°] --> B[Modelado disciplinar]","    B --> C[Práctica guiada]","    C --> D[Desempeño individual]","    D --> E[Evidencia y criterios]","    E --> F{¿Qué necesita el curso?}","    F -->|Dominio| G[Transferir y profundizar]","    F -->|Apoyo puntual| C","    F -->|Otra explicación| B","~~~","","## 🧱 Anatomía y diferenciación","","Cada clase explicita propósito, meta, ancla disciplinar, modelado, práctica guiada, desempeño individual, evidencia, criterios, apoyo, profundización, dificultades observables, decisión posterior y alternativa sin conectividad. La estructura es estable; el contenido y las decisiones cambian OA por OA.","","## ⏱️ Ritmo y uso del mapa","","Cada OA propone de cuatro a siete clases, no un calendario obligatorio. El equipo docente selecciona, combina o pausa según evidencia, tiempo disponible y planificación del establecimiento, conservando el propósito curricular.","","## 📊 Evaluación y decisiones","","Los tickets, criterios y producciones individuales sirven para decidir entre avanzar, practicar de otra manera o volver a modelar. Una actividad realizada no equivale por sí sola a aprendizaje demostrado.","","## 🛠️ Recuperación y profundización","","El apoyo cambia representación, vocabulario, agrupamiento o cantidad de pasos sin reducir el OA. La profundización exige transferencia, comparación, justificación o creación con nuevos límites.","","## 🔎 Estados y límites","","- **Desarrollada:** secuencia disciplinar con decisiones, evidencia y apoyos específicos.","- **Integrada:** habilidad o actitud observada dentro del contenido; no es una clase adicional.","- **Pendiente:** quedan 0 propuestas secuenciadas o borradores en este nivel.","- **Revisada:** requiere evidencia humana competente; actualmente hay 0.","","## 🔗 Documentos relacionados","","- [Mapa técnico de 6° básico](../SEXTO_BASICO.md)","- [Syllabus de 1° a 7° básico](../SYLLABUS.md)","- [Rúbrica transversal](../RUBRICA_EVALUACION.md)","- [Protocolo de revisión humana](../REVISION_HUMANA.md)",""]
 return "\n".join(lines).replace("Syllabus de 1° a 7° básico", "Syllabus de 1° a 8° básico")

def grade_six_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_six_summary(objs,classes)
 developed=sum(x["editorial_status"]=="desarrollada" for x in grade_classes);integrated=sum(x["editorial_status"]=="integrada" for x in grade_classes);pending=sum(x["editorial_status"] in {"secuenciada","borrador"} for x in grade_classes)
 lines=["# 6° básico — mapa de contenidos","",f"> **Desarrollo pedagógico interno completo:** {developed} clases desarrolladas · {integrated} experiencias transversales integradas · {pending} propuestas pendientes · {len(grade_objs)} OA · 12 denominaciones curriculares · revisión humana pendiente.","","[Programa narrativo de 6° básico](6-basico/README.md) · [Índice Markdown de clases](../CURRICULUM.md) · [Guía pedagógica](../TEACHING_GUIDE.md) · [Evaluación formativa](EVALUACION_FORMATIVA.md)","","Todos los OA disciplinares cuentan con secuencias específicas. Las entradas integradas corresponden a habilidades o actitudes observadas dentro de esas clases; no duplican el horario.","","## Cobertura","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Pendientes |","|---|---:|---:|---:|---:|---:|"]
 for item in subjects:lines.append(f"| {item['name']} | {item['oa']} | {item['classes']} | {item['developed']} | {item['integrated']} | {item['classes']-item['developed']-item['integrated']} |")
 lines += ["","## Continuidad con 5° básico","","Cada secuencia diagnostica la base disponible y amplía precisión, vocabulario, autonomía, contraste y transferencia sin sustituir el OA de 6°.","","## Verificación y límite","",f"El catálogo registra {len(grade_objs)} OA y {len(grade_classes):,} propuestas: {developed} desarrolladas, {integrated} integradas y {pending} pendientes.".replace(",","."),"La CI comprueba estructura, cobertura, unicidad, fuentes, licencias y reproducción. Esto no sustituye revisión humana.",""]
 return "\n".join(lines)

def documentation_output_path(source):
 relative=source.relative_to(ROOT)
 if relative.parent == Path("."):
  return Path("docs")/(relative.stem.lower().replace("_","-")+".html")
 if relative.name.lower() == "readme.md":
  return relative.parent/"index.html"
 return relative.with_suffix(".html").with_name(relative.stem.lower().replace("_","-")+".html")

def documentation_sources():
 root_docs=[path for path in ROOT.glob("*.md") if path.name not in {"README.md","CURRICULUM.md"}]
 return sorted(root_docs+list((ROOT/"docs").rglob("*.md")),key=lambda path:path.relative_to(ROOT).as_posix().lower())

def inline_markdown(value,source,output,mapping):
 def plain(fragment):
  escaped=html.escape(fragment)
  escaped=re.sub(r"`([^`]+)`",r"<code>\1</code>",escaped)
  escaped=re.sub(r"\*\*([^*]+)\*\*",r"<strong>\1</strong>",escaped)
  return escaped
 def link(match):
  label,destination=match.group(1),match.group(2)
  if destination.startswith(("http://","https://","mailto:","#")):
   href=destination
  else:
   path_part,separator,fragment=destination.partition("#")
   target=(source.parent/path_part).resolve() if path_part else source.resolve()
   if target in mapping:
    href=posixpath.relpath(mapping[target].as_posix(),output.parent.as_posix())
   elif target == (ROOT/"README.md").resolve() or target == (ROOT/"CURRICULUM.md").resolve():
    href=posixpath.relpath("index.html",output.parent.as_posix())
   elif target.suffix.lower()==".md" and ROOT/"curriculum" in target.parents:
    curriculum_relative=target.relative_to(ROOT/"curriculum").with_suffix(".html")
    href=posixpath.relpath((Path("classes")/curriculum_relative).as_posix(),output.parent.as_posix())
   else:
    href=destination
   if separator:href += "#"+fragment
  return f'<a href="{html.escape(href,quote=True)}">{plain(label)}</a>'
 parts=[];cursor=0
 for match in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)",value):
  parts.append(plain(value[cursor:match.start()]));parts.append(link(match));cursor=match.end()
 parts.append(plain(value[cursor:]))
 return "".join(parts)

def markdown_body(source,output,mapping):
 lines=source.read_text(encoding="utf-8").splitlines();result=[];index=0
 while index<len(lines):
  line=lines[index].rstrip()
  if not line:index+=1;continue
  if line.startswith(("```","~~~")):
   marker=line[:3];language=line[3:].strip();block=[];index+=1
   while index<len(lines) and not lines[index].startswith(marker):block.append(lines[index]);index+=1
   result.append(f'<pre class="doc-code {html.escape(language)}"><code>{html.escape(chr(10).join(block))}</code></pre>');index+=1;continue
  heading=re.match(r"^(#{1,6})\s+(.+)$",line)
  if heading:
   level=len(heading.group(1));title=heading.group(2).strip();anchor=slugify(re.sub(r"[^\w\s-]","",title))
   result.append(f'<h{level} id="{anchor}">{inline_markdown(title,source,output,mapping)}</h{level}>');index+=1;continue
  if line.startswith("|") and index+1<len(lines) and re.match(r"^\|?[\s:|-]+\|?$",lines[index+1].strip()):
   rows=[]
   while index<len(lines) and lines[index].strip().startswith("|"):
    rows.append([cell.strip() for cell in lines[index].strip().strip("|").split("|")]);index+=1
   header=rows[0];body=rows[2:]
   result.append('<div class="table-scroll"><table><thead><tr>'+"".join(f"<th>{inline_markdown(cell,source,output,mapping)}</th>" for cell in header)+"</tr></thead><tbody>"+"".join("<tr>"+"".join(f"<td>{inline_markdown(cell,source,output,mapping)}</td>" for cell in row)+"</tr>" for row in body)+"</tbody></table></div>");continue
  if line.startswith(">"):
   result.append(f'<blockquote>{inline_markdown(line.lstrip("> "),source,output,mapping)}</blockquote>');index+=1;continue
  if re.match(r"^[-*]\s+",line):
   items=[]
   while index<len(lines) and re.match(r"^[-*]\s+",lines[index].strip()):items.append(re.sub(r"^[-*]\s+","",lines[index].strip()));index+=1
   result.append("<ul>"+"".join(f"<li>{inline_markdown(item,source,output,mapping)}</li>" for item in items)+"</ul>");continue
  if re.match(r"^\d+\.\s+",line):
   items=[]
   while index<len(lines) and re.match(r"^\d+\.\s+",lines[index].strip()):items.append(re.sub(r"^\d+\.\s+","",lines[index].strip()));index+=1
   result.append("<ol>"+"".join(f"<li>{inline_markdown(item,source,output,mapping)}</li>" for item in items)+"</ol>");continue
  if re.match(r"^---+$",line):result.append("<hr>");index+=1;continue
  result.append(f"<p>{inline_markdown(line,source,output,mapping)}</p>");index+=1
 return "\n".join(result)

def documentation_html_page(source,output,mapping):
 text=source.read_text(encoding="utf-8")
 title_match=re.search(r"^#\s+(.+)$",text,re.MULTILINE);title=title_match.group(1) if title_match else source.stem.replace("_"," ").title()
 stylesheet=posixpath.relpath("styles.css",output.parent.as_posix());home=posixpath.relpath("documentacion.html",output.parent.as_posix());portal=posixpath.relpath("index.html",output.parent.as_posix())
 licensing=mapping.get((ROOT/"LICENSING.md").resolve(),Path("docs/licensing.html"));license_href=posixpath.relpath(licensing.as_posix(),output.parent.as_posix())
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="{html.escape(title,quote=True)} · documentación pedagógica de Trayectoria Escolar Chile."><link rel="stylesheet" href="{stylesheet}"><title>{html.escape(title)} | Trayectoria Escolar Chile</title></head><body class="doc-page"><a class="skip-link" href="#contenido">Saltar al contenido</a><header class="detail-topbar"><a class="brand" href="{portal}"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Documentación HTML</small></span></a><a class="back-link" href="{home}">← Centro documental</a></header><main id="contenido" class="doc-shell"><div class="doc-format"><span>GitHub Pages</span><strong>Versión HTML</strong></div><article class="doc-article">{markdown_body(source,output,mapping)}</article></main><footer class="site-footer"><div><strong>Trayectoria Escolar Chile</strong><span>Documento HTML para GitHub Pages</span></div><div><a href="{home}">Documentación</a><a href="{license_href}">Licencias</a></div></footer></body></html>'''

def generate_documentation_pages():
 sources=documentation_sources();mapping={source.resolve():documentation_output_path(source) for source in sources}
 docs_root=ROOT/"site"/"docs"
 if docs_root.exists():shutil.rmtree(docs_root)
 for source in sources:
  output=mapping[source.resolve()];target=ROOT/"site"/output;target.parent.mkdir(parents=True,exist_ok=True)
  target.write_text(documentation_html_page(source,output,mapping),encoding="utf-8")
 return list(mapping.values())

GRADE_SEVEN_CORE_PROFILES={
 "matematica":{
  "purpose":"Construir pensamiento matemático con enteros, fracciones, porcentajes, potencias, álgebra, proporcionalidad, geometría, datos y probabilidad mediante problemas, representaciones, argumentos y comprobaciones.",
  "continuity":"Desde 6° básico, amplía razones, porcentajes, ecuaciones, ángulos, superficie y azar hacia enteros, formalización algebraica, proporcionalidad directa e inversa, construcciones, muestreo e inferencia.",
  "barrier":"aplicar reglas de signos, fórmulas o modelos sin conservar la relación matemática, la unidad ni una comprobación independiente",
  "outcomes":["representar y operar con números y expresiones conservando significado","modelar relaciones y justificar ecuaciones, inecuaciones y proporciones","construir y analizar figuras con propiedades verificables","interpretar muestras, distribuciones y probabilidades con límites explícitos"],
  "method":"Comienza con una situación o representación, hace visible la decisión matemática, conecta registros concretos, gráficos y simbólicos, y exige estimar o comprobar antes de aceptar el resultado.",
  "evidence":"solución representada, procedimiento justificable, respuesta situada y comprobación independiente",
 },
 "lengua-literatura":{
  "purpose":"Leer literatura y medios con profundidad, escribir para propósitos y audiencias reales, dialogar con evidencia, exponer con claridad e investigar respetando fuentes, autoría y diversidad de perspectivas.",
  "continuity":"Desde 6° básico, profundiza comprensión, producción y oralidad hacia interpretación literaria situada, análisis crítico de argumentos y medios, escritura por procesos, reflexión gramatical e investigación autónoma.",
  "barrier":"resumir en vez de interpretar, opinar sin evidencia o corregir la superficie de un texto sin atender propósito, audiencia y sentido",
  "outcomes":["interpretar obras con evidencia textual y contexto","evaluar argumentos y recursos multimodales sin atribuir intenciones infundadas","planificar, escribir y revisar textos según propósito, género y audiencia","dialogar, exponer e investigar con fuentes y autoría trazables"],
  "method":"Trabaja con textos breves originales, de dominio público o enlazados; modela cómo seleccionar evidencia y tomar decisiones, permite voces diversas y revisa con criterios sin imponer una respuesta única.",
  "evidence":"interpretación, texto, intervención oral o síntesis individual con propósito, evidencia y revisión",
 },
 "ciencias-naturales":{
  "purpose":"Comprender sistemas biológicos, fuerzas, Tierra, clima y materia mediante modelos, indagaciones seguras y explicaciones que distinguen evidencia, inferencia y límite.",
  "continuity":"Desde 6° básico, profundiza investigación y modelación hacia pubertad y salud sexual, inmunidad, microorganismos, fuerzas, tectónica, clima, gases, mezclas y cambios de la materia.",
  "barrier":"presentar modelos como copias exactas, cambiar varias variables a la vez o convertir una conclusión prudente en certeza",
  "outcomes":["explicar sistemas biológicos y decisiones de cuidado sin estigma ni exposición personal","planificar y evaluar indagaciones con variables, datos y seguridad","usar modelos de fuerzas, Tierra, clima y materia declarando sus límites","argumentar conclusiones proporcionales a la evidencia disponible"],
  "method":"Parte de fenómenos, datos, modelos o casos protegidos; separa observación e interpretación, hace visibles variables y límites, y vuelve a decisiones seguras basadas en evidencia.",
  "evidence":"registro, modelo o explicación individual con datos, comparación, conclusión y limitación",
 },
 "historia-geografia-ciencias-sociales":{
  "purpose":"Comprender sociedades antiguas y medievales, ciudadanía, diversidad y relaciones sociedad-ambiente mediante fuentes contextualizadas, mapas, cronologías y argumentos con perspectiva.",
  "continuity":"Desde 6° básico, amplía el análisis histórico y geográfico hacia hominización, primeras civilizaciones, mundo clásico y medieval, América precolombina, conceptos políticos y ambiente.",
  "barrier":"mezclar épocas, tratar una fuente como verdad completa, jerarquizar culturas o trasladar conceptos del presente sin explicar diferencias",
  "outcomes":["ubicar procesos en escalas temporales y espaciales pertinentes","contrastar fuentes, actores y perspectivas sin anacronismos","explicar causas, consecuencias, continuidades y cambios de forma multicausal","argumentar decisiones ciudadanas y ambientales con evidencia contextualizada"],
  "method":"Combina mapas, líneas de tiempo y fuentes con procedencia visible; modela cómo describir antes de interpretar, contrastar perspectivas y limitar cada conclusión.",
  "evidence":"explicación, mapa, argumento o investigación individual apoyada en fuentes contextualizadas",
 },
 "ingles":{
  "purpose":"Comprender y producir mensajes orales y escritos en inglés para propósitos reales, usando pistas, chunks, estrategias, interacción y revisión sin penalizar acento ni mezcla lingüística inicial.",
  "continuity":"Desde 6° básico, avanza hacia escucha y lectura de textos auténticos simples, interacción sostenida, presentaciones multimodales y escritura narrativa, informativa y de opinión.",
  "barrier":"traducir cada palabra, recitar modelos sin atender al interlocutor o esperar precisión total antes de comunicar",
  "outcomes":["localizar idea general, detalles y relaciones mediante pistas verificables","interactuar, pedir aclaración y reparar significado","leer textos literarios y funcionales según propósito","planificar, producir y revisar mensajes comprensibles para una audiencia"],
  "method":"Usa textos breves autorizados, apoyos visuales y tareas con vacío de información; modela estrategias y retira apoyos mientras mantiene un propósito comunicativo genuino.",
  "evidence":"respuesta oral, escrita, visual o corporal comprensible vinculada con pistas del mensaje",
 },
 "educacion-fisica-salud":{
  "purpose":"Desarrollar habilidades motrices, estrategias, condición física y participación autónoma mediante experiencias seguras, inclusivas y reguladas desde evidencia propia.",
  "continuity":"Desde 6° básico, profundiza combinaciones motrices y autocuidado hacia habilidades deportivas específicas, tácticas, metas personales y práctica en diversos entornos.",
  "barrier":"priorizar rendimiento sobre control, comparar cuerpos, excluir por error o normalizar dolor y riesgo como señales de aprendizaje",
  "outcomes":["combinar habilidades y adaptar decisiones a la situación","leer espacio, reglas, compañeros y oposición para ajustar tácticas","regular intensidad y metas respecto del propio proceso","participar en entornos variados con seguridad, inclusión y mínimo impacto"],
  "method":"Organiza estaciones sin eliminación, variantes equivalentes, señales de detención y retroalimentación sobre conductas observables; nunca usa un cuerpo o marca ideal.",
  "evidence":"desempeño motriz seguro con elección de variante, ajuste observable y autoexplicación",
 },
 "artes-visuales":{
  "purpose":"Crear, interpretar y difundir producciones visuales con intención, experimentación, contexto, sustentabilidad, autoría y decisiones propias.",
  "continuity":"Desde 6° básico, profundiza lenguaje visual y apreciación hacia referentes patrimoniales y contemporáneos, materiales sustentables, medios digitales y espacios de difusión.",
  "barrier":"copiar referentes, evaluar por gusto o talento, usar efectos sin intención o ignorar autoría, contexto, privacidad y seguridad",
  "outcomes":["transformar percepciones e ideas en decisiones visuales propias","experimentar materiales y medios según intención y sustentabilidad","interpretar manifestaciones con evidencia visual y contexto","revisar y difundir trabajos cuidando autoría, audiencia y acceso"],
  "method":"Trabaja con referentes atribuidos y pruebas de taller; demuestra procedimientos sin entregar soluciones estéticas, conserva intentos y devuelve cada decisión expresiva a su autor.",
  "evidence":"trabajo visual o interpretación propia con registro de proceso, decisión y fundamento visual",
 },
 "ingles-propuesta":{
  "purpose":"Comprender y producir textos orales y escritos simples en inglés mediante estrategias, interacción, funciones comunicativas y revisión orientadas al significado.",
  "continuity":"Desde 6° básico, amplía la comprensión de textos variados, las presentaciones multimodales, la interacción sostenida y la escritura por procesos para informar, opinar y narrar.",
  "barrier":"traducir palabra por palabra, recitar modelos sin atender al interlocutor o asociar aprendizaje con acento, velocidad y precisión inmediata",
  "outcomes":["comprender ideas, detalles y relaciones mediante pistas verificables","interactuar y reparar significado con apoyos gradualmente retirados","responder a textos de manera personal y fundamentada","planificar, escribir y revisar mensajes para propósito y audiencia"],
  "method":"Usa textos breves autorizados, guiones originales, vacíos de información y tareas reales; acepta distintas vías de respuesta y evalúa significado antes que imitación de acento.",
  "evidence":"respuesta oral, escrita, visual o corporal comprensible, vinculada con pistas y revisada según propósito",
 },
 "lengua-indigena":{
  "purpose":"Comprender, valorar y producir respuestas vinculadas con lengua, relatos y prácticas discursivas indígenas desde territorio, fuentes autorizadas y mediación cultural pertinente.",
  "continuity":"Desde 6° básico, profundiza relatos, oralidad, lectura, escritura e interculturalidad, declarando siempre pueblo, territorio, fuente, autorización y límites de circulación.",
  "barrier":"inventar lengua o explicaciones culturales, generalizar una fuente a todos los pueblos o divulgar saberes, relatos e imágenes sin autorización",
  "outcomes":["situar relatos y prácticas por pueblo, territorio y fuente","comprender y producir respuestas sin suplantar voces comunitarias","analizar situaciones interculturales sin jerarquizar culturas","respetar autorización, variantes, identidad y límites de circulación"],
  "method":"Trabaja con educador tradicional, autoridad cultural o fuentes comunitarias pertinentes; permite responder sin pronunciar ni representar pertenencia y detiene actividades sin validación.",
  "evidence":"comprensión o producción situada que atribuye fuente, declara límites y evita inventar, generalizar o apropiarse",
 },
 "musica":{
  "purpose":"Escuchar, interpretar, improvisar, crear y reflexionar sobre música mediante rasgos audibles, decisiones expresivas, trabajo colectivo y contextos atribuidos.",
  "continuity":"Desde 6° básico, profundiza precisión, expresividad y creación hacia interpretación a varias voces, procedimientos compositivos, registro y análisis del rol social de la música.",
  "barrier":"describir sólo gusto, confundir logro con volumen o velocidad, o presentar una música como representación total de una cultura",
  "outcomes":["describir música con evidencia audible y vocabulario pertinente","interpretar repertorio cuidando control, expresividad y escucha colectiva","improvisar y crear con decisiones comprobables","reflexionar sobre crecimiento, contexto y rol social sin jerarquías culturales"],
  "method":"Escucha antes de nombrar, compara versiones cambiando una variable, ensaya con volumen seguro y formula retroalimentación que pueda comprobarse al volver a oír.",
  "evidence":"interpretación, creación o comentario individual con decisión musical, ajuste y evidencia audible",
 },
 "orientacion":{
  "purpose":"Fortalecer autoconocimiento, bienestar, relaciones respetuosas, protección, participación y autonomía mediante casos ficticios, derechos, decisiones y redes de apoyo.",
  "continuity":"Desde 6° básico, profundiza identidad, sexualidad integral, prevención, convivencia presencial y digital, participación y gestión del aprendizaje sin solicitar revelaciones personales.",
  "barrier":"pedir experiencias íntimas, moralizar o diagnosticar, o presentar secreto, culpa y obediencia como respuestas universales de seguridad",
  "outcomes":["analizar casos desde dignidad, derechos, consentimiento y consecuencias","reconocer riesgos y activar redes de ayuda pertinentes","resolver conflictos y construir acuerdos sin violencia","gestionar participación y aprendizaje mediante metas revisables"],
  "method":"Utiliza siempre casos ficticios y tercera persona; enseña rutas de ayuda, aplica protocolos ante revelaciones espontáneas y permite evidencia sin datos personales.",
  "evidence":"decisión escrita, oral o representada para un caso ficticio, con criterio, consecuencias y ruta de apoyo",
 },
 "tecnologia":{
  "purpose":"Resolver necesidades de reparación, adaptación o mejora mediante diseño, implementación, prueba, comunicación y evaluación de impactos.",
  "continuity":"Desde 6° básico, amplía proyectos tecnológicos hacia soluciones eficientes, criterios técnicos, comunicación con TIC y análisis social y ambiental situado.",
  "barrier":"construir antes de definir la necesidad, evaluar sólo apariencia o usar herramientas, imágenes y datos sin cuidar seguridad, privacidad y autoría",
  "outcomes":["definir necesidades, usuarios, criterios y restricciones verificables","representar e implementar soluciones con uso eficiente y seguro de recursos","probar, evaluar y mejorar desde evidencia","comunicar procesos e impactos respetando privacidad y autoría"],
  "method":"Parte de una necesidad documentada, compara alternativas, representa antes de construir, prueba una variable y revisa función, seguridad, reparación e impacto.",
  "evidence":"representación o solución con criterios, registro de prueba, mejora justificada y evaluación de impacto",
 },
}

GRADE_EIGHT_CORE_PROFILES={
 "matematica":{
  "purpose":"Profundizar números racionales, potencias y raíces; modelar con expresiones, ecuaciones, inecuaciones y funciones; construir geometría y evaluar datos y azar con argumentos verificables.",
  "continuity":"Desde 7° básico, amplía enteros, álgebra, proporcionalidad, geometría y probabilidad hacia operaciones racionales completas, función afín, Pitágoras, transformaciones compuestas, cuartiles y combinatoria.",
  "barrier":"aplicar reglas o fórmulas sin representar la relación, conservar unidades, declarar restricciones ni comprobar el resultado",
  "outcomes":["operar y estimar con enteros, racionales, potencias y raíces","modelar relaciones mediante expresiones, ecuaciones, inecuaciones y funciones","derivar y aplicar relaciones geométricas con propiedades explícitas","evaluar distribuciones, gráficos y eventos compuestos con sentido crítico"],
  "method":"Parte de un problema o representación, hace visible cada decisión, conecta registros concretos, gráficos y simbólicos, y exige estimación, argumento o comprobación independiente.",
  "evidence":"solución individual representada, procedimiento justificable, respuesta situada y comprobación independiente",
 },
 "lengua-literatura":{
  "purpose":"Leer literatura, drama, epopeya, argumentos y medios críticamente; escribir y hablar para audiencias reales; investigar, sintetizar y revisar cuidando fuentes, diversidad y privacidad.",
  "continuity":"Desde 7° básico, profundiza interpretación y análisis de medios, e incorpora texto dramático, epopeya, comedia, escritura explicativa y persuasiva, correferencia, modos verbales e investigación más autónoma.",
  "barrier":"resumir en vez de analizar, opinar sin evidencia, atribuir intenciones no demostrables o corregir solo la superficie sin atender propósito y audiencia",
  "outcomes":["interpretar narraciones, poemas y textos dramáticos con evidencia y contexto","comparar argumentos y medios atendiendo fuentes y multimodalidad","planificar, escribir y revisar textos creativos, explicativos y persuasivos","dialogar, exponer, investigar y sintetizar con autoría trazable"],
  "method":"Trabaja con textos originales, de dominio público o enlazados; modela selección de evidencia y decisiones de producción, admite interpretaciones plausibles y revisa con criterios sin uniformar voces.",
  "evidence":"interpretación, texto, intervención oral o síntesis individual con propósito, evidencia, fuentes y revisión",
 },
 "ciencias-naturales":{
  "purpose":"Explicar células, sistemas corporales, electricidad, calor y materia mediante modelos, investigaciones seguras y argumentos proporcionados a la evidencia.",
  "continuity":"Desde 7° básico, profundiza el trabajo con sistemas, modelos e indagaciones hacia la célula, la interacción corporal, la electricidad, la energía térmica y los modelos de la materia.",
  "barrier":"memorizar partes o fórmulas sin relacionar mecanismo, evidencia, variables, seguridad y límites del modelo",
  "outcomes":["explicar estructura y función celular y la interacción de sistemas","investigar electricidad y transferencia térmica de forma segura","usar modelos atómicos y tabla periódica para explicar y predecir","evaluar evidencia, salud, tecnología e impacto sin exagerar conclusiones"],
  "method":"Parte de preguntas investigables, contrasta modelos, controla variables en experiencias seguras y separa observación, patrón, explicación y límite.",
  "evidence":"registro individual con modelo, datos o fuentes, explicación causal, limitación y decisión segura",
 },
 "historia-geografia-ciencias-sociales":{
  "purpose":"Comprender la modernidad, conquista, sociedad colonial, Ilustración, independencias y regiones mediante fuentes contextualizadas, escalas y perspectivas contrastadas.",
  "continuity":"Desde 7° básico, amplía el análisis de procesos y fuentes hacia la modernidad y la historia colonial, conecta derechos e independencias y aplica herramientas geográficas a las regiones de Chile.",
  "barrier":"narrar procesos como inevitables, monocausales o protagonizados por un solo grupo, y trasladar categorías actuales sin contextualización",
  "outcomes":["explicar cambios entre mundo medieval y moderno","analizar conquista y sociedad colonial sin borrar violencia, agencia ni diversidad","relacionar Ilustración, revoluciones, derechos e independencias con sus límites","evaluar regiones, conectividad y desarrollo sustentable usando datos y mapas"],
  "method":"Contextualiza fuentes, cruza mapas y cronologías, contrasta actores y escalas y construye argumentos proporcionales a la evidencia disponible.",
  "evidence":"argumento, mapa o explicación individual con fuentes identificadas, contexto, perspectiva y límite",
 },
 "artes-visuales":{
  "purpose":"Crear, analizar, revisar y difundir trabajos visuales sobre ambiente, materialidad, instalación, patrimonio y públicos, conservando autoría y contexto.",
  "continuity":"Desde 7° básico, profundiza la creación situada y la apreciación hacia materiales sustentables, instalación, montaje, mediación y aporte comunitario.",
  "barrier":"copiar referentes, acumular materiales sin intención o evaluar por talento, gusto y parecido",
  "outcomes":["crear respuestas visuales sobre personas y medioambiente","experimentar con impresión, papel, textil e instalación","analizar manifestaciones patrimoniales y contemporáneas con evidencia visual","evaluar y difundir obras según propósito, espacio, público y aporte comunitario"],
  "method":"Observa y contextualiza antes de interpretar, explora materiales de forma segura, toma decisiones visuales propias y revisa desde criterios sin uniformar resultados.",
  "evidence":"bitácora, pruebas, obra o propuesta de montaje con decisiones visuales justificadas y revisión documentada",
 },
 "musica":{
  "purpose":"Escuchar, describir, interpretar, crear y reflexionar sobre músicas diversas mediante evidencia audible, registro y trabajo colectivo seguro.",
  "continuity":"Desde 7° básico, aumenta precisión, autonomía y reflexión en escucha, interpretación, acompañamiento, variación, registro y contextualización social de la música.",
  "barrier":"reducir el aprendizaje a gusto, volumen, velocidad o ejecución uniforme y presentar una obra como voz total de una cultura",
  "outcomes":["comunicar respuestas multimodales sustentadas en lo audible","relacionar lenguaje musical y procedimientos con propósito expresivo","interpretar, acompañar, variar e improvisar con precisión y expresividad","reconocer fortalezas, áreas de crecimiento y funciones sociales de la música"],
  "method":"Escucha antes de categorizar, alterna interpretación y autoescucha, registra para revisar y sitúa cada repertorio con autoría, contexto y volumen seguro.",
  "evidence":"registro, interpretación, creación o comentario individual que localiza un rasgo audible y explica una decisión",
 },
 "educacion-fisica-salud":{
  "purpose":"Consolidar habilidades motrices, decisiones tácticas, condición física saludable, autocuidado y participación activa de la comunidad.",
  "continuity":"Desde 7° básico, aumenta autonomía para combinar habilidades, regular cargas, resolver problemas de juego y organizar experiencias inclusivas y seguras.",
  "barrier":"confundir dominio con rendimiento único, imponer la misma carga o variante y evaluar solo resultados competitivos",
  "outcomes":["seleccionar y combinar habilidades en deportes y danza","resolver problemas mediante estrategias y tácticas","regular condición física con frecuencia, intensidad, tiempo, recuperación y progresión","promover actividad física segura, inclusiva y sostenible"],
  "method":"Trabaja con estaciones, juegos reducidos y variantes equivalentes; hace visibles seguridad, autorregulación, cooperación y decisiones tácticas sin comparar cuerpos.",
  "evidence":"desempeño o representación individual con decisión motriz, regulación, criterio de seguridad y ajuste explicado",
 },
 "orientacion":{
  "purpose":"Fortalecer autoconocimiento, sexualidad integral, prevención, bienestar, relaciones respetuosas, participación y autonomía para aprender.",
  "continuity":"Desde 7° básico, profundiza decisiones personales y colectivas mediante derechos, consecuencias, redes de ayuda, acuerdos democráticos y metas revisables.",
  "barrier":"exigir experiencias personales, moralizar decisiones, diagnosticar o presentar el silencio y la obediencia como respuestas universales",
  "outcomes":["construir una representación positiva y situada de sí","analizar cuidado, intimidad, riesgo y relaciones desde derechos","resolver conflictos y participar democráticamente","gestionar metas de aprendizaje y proyectos personales"],
  "method":"Usa casos ficticios en tercera persona, opciones y consecuencias, comunicación ensayada y rutas de ayuda; protege intimidad y activa protocolos ante revelaciones espontáneas.",
  "evidence":"decisión individual sobre un caso ficticio con derecho, consecuencia, comunicación y apoyo pertinente",
 },
 "tecnologia":{
  "purpose":"Identificar oportunidades, diseñar productos sustentables, probarlos, mejorarlos y comunicar sus procesos e impactos con responsabilidad ética.",
  "continuity":"Desde 7° básico, integra usuario, eficiencia, sustentabilidad y TIC en ciclos completos de creación y evaluación técnica.",
  "barrier":"construir antes de documentar la necesidad, evaluar solo apariencia o usar recursos y datos sin seguridad, privacidad ni autoría",
  "outcomes":["documentar necesidades y destinatarios","diseñar y crear con criterios de eficiencia y sustentabilidad","probar y mejorar con evidencia técnica","comunicar procesos e impactos éticos, ambientales y sociales"],
  "method":"Parte de evidencia local, compara alternativas, representa antes de construir, prueba criterios medibles y comunica decisiones, límites e impactos.",
  "evidence":"propuesta o producto con necesidad, usuario, criterios, registro de prueba, mejora y evaluación de impactos",
 },
 "ingles":{
  "purpose":"Comprender, interactuar, leer, escribir y presentar en inglés para propósitos y audiencias reconocibles, usando estrategias y evidencia del mensaje.",
  "continuity":"Desde 7° básico, amplía autonomía para procesar textos auténticos simples, relacionar ideas, reparar comunicación y producir mensajes multimodales.",
  "barrier":"traducir cada palabra, memorizar guiones sin responder a la audiencia o usar acento y velocidad como medida de aprendizaje",
  "outcomes":["comprender ideas y detalles en textos orales y escritos","usar estrategias antes, durante y después de escuchar o leer","interactuar y presentar con funciones comunicativas del nivel","escribir, revisar y publicar textos breves para audiencias reales"],
  "method":"Propone escucha y lectura con propósito, brechas reales de información, bancos de expresiones y revisión centrada en significado, claridad y audiencia.",
  "evidence":"respuesta individual oral, escrita o multimodal que comunica significado e identifica la pista o decisión lingüística utilizada",
 },
 "ingles-propuesta":{
  "purpose":"Articular comprensión, interacción y producción en inglés mediante textos literarios y funcionales, estrategias explícitas y tareas comunicativas.",
  "continuity":"Desde 7° básico, profundiza relaciones de secuencia, causa, condición, tiempo y proceso, con mayor revisión autónoma.",
  "barrier":"traducir linealmente, completar formas sin propósito o repetir modelos sin comprobar comprensión ni efecto en la audiencia",
  "outcomes":["comprender y relacionar evidencia oral y escrita","usar estrategias para sostener comprensión","interactuar y presentar para una audiencia","producir y revisar textos multimodales breves"],
  "method":"Usa textos breves autorizados, audios docentes originales, tareas con información distribuida y modelos flexibles que se revisan desde el significado.",
  "evidence":"mensaje individual comprensible, situado y revisado con pista textual, propósito y decisión lingüística explícitos",
 },
 "lengua-indigena":{
  "purpose":"Aprender desde relatos, lenguas, autorías y contextos indígenas vivos mediante fuentes autorizadas, territorio y validación cultural pertinente.",
  "continuity":"Desde 7° básico, avanza hacia creación, interacción, lectura contemporánea, escritura e investigación de tradición oral con mayor responsabilidad.",
  "barrier":"inventar lengua o espiritualidad, generalizar una fuente y divulgar conocimientos o relatos sin autorización",
  "outcomes":["crear y comunicar desde fuentes validadas","reconocer diversidad lingüística y cultural sin jerarquías","leer autorías y contextos indígenas actuales","escribir e investigar respetando territorio, atribución y límites"],
  "method":"Sitúa pueblo, territorio, autoría y permiso antes de trabajar; coordina con educador tradicional o fuente comunitaria y detiene usos no validados.",
  "evidence":"respuesta oral, visual o escrita atribuida que distingue fuente, interpretación, permiso y límite cultural",
 },
}

GRADE_ONE_MIDDLE_CORE_PROFILES={
 "matematica":{
  "purpose":"Profundizar el razonamiento con racionales y potencias; modelar mediante productos notables, sistemas y relaciones lineales; justificar geometría de círculos, conos, homotecia y semejanza; y evaluar datos bivariados y azar.",
  "continuity":"Desde 8° básico, aumenta la formalización algebraica, la demostración geométrica, la modelación de varias variables y la evaluación crítica de modelos probabilísticos y estadísticos.",
  "barrier":"aplicar identidades, fórmulas o reglas sin declarar condiciones, representar la relación, conservar unidades ni comprobar el resultado",
  "outcomes":["operar y argumentar con racionales y potencias","modelar relaciones mediante expresiones, sistemas y ecuaciones lineales","derivar y aplicar relaciones geométricas con condiciones explícitas","evaluar asociaciones, modelos de azar y reglas de probabilidad con límites"],
  "method":"Parte de un problema o representación, hace visibles condiciones y decisiones, conecta registros concretos, gráficos y simbólicos y exige estimación, argumento y comprobación independiente.",
  "evidence":"solución individual con representación pertinente, procedimiento justificable, respuesta situada y comprobación o límite explícito",
 },
 "lengua-literatura":{
  "purpose":"Construir una trayectoria lectora autónoma; interpretar literatura situada; evaluar discursos, medios y recursos multimodales; y producir textos y exposiciones investigados para propósitos y audiencias reales.",
  "continuity":"Desde 8° básico, profundiza análisis de narraciones, poesía y drama; incorpora tragedia y Romanticismo; y aumenta autonomía para argumentar, investigar, escribir, revisar y comunicar.",
  "barrier":"reemplazar análisis por resumen, opinión o etiquetas; usar contexto sin evidencia textual; o corregir productos sin atender propósito, audiencia, fuentes y decisiones de autor",
  "outcomes":["seleccionar y sostener lecturas con propósitos propios","interpretar obras mediante evidencia, contexto y perspectivas revisables","evaluar argumentos, medios y recursos orales o multimodales","investigar, escribir, dialogar y exponer con fuentes, revisión y responsabilidad"],
  "method":"Trabaja con corpus breves y obras de procedencia identificada, lectura y escucha con propósito, conversación protegida, escritura por procesos y revisión centrada en evidencia, audiencia y efecto.",
  "evidence":"interpretación, texto, intervención oral o informe individual que usa evidencia precisa, reconoce contexto y justifica decisiones para una audiencia",
 },
 "ciencias-naturales":{
  "purpose":"Explicar evolución y ecología con evidencia; modelar ondas, sonido, luz, sismos y astronomía; e investigar reacciones, conservación de materia, compuestos y estequiometría con seguridad.",
  "continuity":"Desde 8° básico, integra modelos biológicos, físicos y químicos con datos más complejos, control de variables, escalas, incertidumbre y evaluación de impactos.",
  "barrier":"confundir observación con explicación, afirmar causalidad con un solo dato, usar modelos como copias literales o experimentar sin controlar variables y seguridad",
  "outcomes":["argumentar evolución, clasificación y dinámica ecosistémica con evidencias convergentes","modelar ondas, percepción, sismos y sistemas astronómicos declarando escalas y límites","investigar reacciones y conservar átomos y masa mediante representaciones coherentes","relacionar estequiometría, aplicaciones e impactos sin exagerar conclusiones"],
  "method":"Parte de fenómenos, datos o discrepancias; separa observación e inferencia, modela mecanismos, diseña comparaciones seguras y exige conclusiones proporcionales a la evidencia.",
  "evidence":"informe, modelo o explicación individual que identifica variables, usa datos pertinentes, conecta representación y mecanismo y declara una limitación",
 },
 "historia-geografia-ciencias-sociales":{
  "purpose":"Interpretar las transformaciones mundiales y chilenas del siglo XIX y comienzos del XX; analizar territorio, economía y ciudadanía; y construir argumentos con fuentes, escalas y perspectivas contrastadas.",
  "continuity":"Desde 8° básico, amplía la temporalidad hacia el orden liberal, industrial e imperial, la formación republicana de Chile y problemas económicos y ciudadanos del presente.",
  "barrier":"narrar procesos como inevitables, usar una fuente como verdad completa, juzgar el pasado sin contexto o trasladar conflictos históricos a estereotipos actuales",
  "outcomes":["explicar liberalismo, industrialización, imperialismo y guerra mediante causas, actores y consecuencias","analizar la formación republicana, territorial y social de Chile con fuentes diversas","interpretar escasez, mercados, finanzas y consumo mediante casos protegidos","deliberar sobre diversidad, conflicto y sostenibilidad con evidencia contextualizada"],
  "method":"Sitúa tiempo, territorio, autoría y propósito; cruza mapas, cronologías, datos y testimonios; contrasta perspectivas y construye conclusiones proporcionales a los límites de las fuentes.",
  "evidence":"argumento histórico, geográfico, económico o ciudadano individual que contextualiza fuentes, relaciona escalas y reconoce perspectivas y límites",
 },
 "ingles":{
  "purpose":"Comprender, interactuar, leer y escribir en inglés mediante textos auténticos o adaptados, estrategias explícitas, funciones del nivel y decisiones ajustadas a propósito, audiencia y evidencia.",
  "continuity":"Desde 8° básico, aumenta la autonomía para inferir, aclarar, relacionar ideas, sostener interacciones, usar recursos multimodales y revisar producciones conectadas.",
  "barrier":"traducir palabra por palabra, recitar modelos sin escuchar a la audiencia, evaluar inteligencia por acento o rapidez y corregir forma antes de construir significado",
  "outcomes":["comprender ideas globales, detalles y relaciones en textos orales","interactuar y presentar con estrategias de reparación y recursos pertinentes","interpretar textos literarios y funcionales mediante evidencia","escribir para audiencias reales mediante planificación, revisión y funciones del nivel"],
  "method":"Usa audio docente original, textos breves autorizados, vacíos de información y tareas comunicativas; anticipa propósito, ofrece reescucha o relectura y revisa significado antes de precisión formal.",
  "evidence":"respuesta, interacción, presentación o texto individual comprensible que usa evidencia, lenguaje del nivel y una revisión explicada",
 },
 "ingles-propuesta":{
  "purpose":"Integrar comprensión auditiva y lectora, expresión oral y escritura en inglés mediante tareas comunicativas protegidas, textos variados y revisión centrada primero en significado.",
  "continuity":"Desde 8° básico, profundiza inferencia, interacción, respuesta crítica, funciones temporales e hipotéticas y producción multimodal para audiencias definidas.",
  "barrier":"resolver comprensión por traducción total, repetir sin intercambio real, copiar un modelo sin decisiones propias o confundir precisión inmediata con competencia comunicativa",
  "outcomes":["escuchar y leer con propósito, estrategias y evidencia localizada","responder críticamente y conectar textos, culturas y otras asignaturas","presentar e interactuar adaptando lenguaje y recursos a la audiencia","planificar, escribir, revisar y publicar textos conectados"],
  "method":"Trabaja con audios originales, textos autorizados, información distribuida y encargos de escritura ficticios; alterna apoyo, producción independiente y revisión desde criterios comunicativos.",
  "evidence":"desempeño oral o escrito individual que comunica significado, incorpora funciones del nivel, atiende una audiencia y documenta una mejora",
 },
 "artes-visuales":{
  "purpose":"Crear, analizar y difundir proyectos visuales vinculados con arquitectura, espacio público, sustentabilidad, libro de artista y medios digitales, sosteniendo decisiones de autoría y contexto.",
  "continuity":"Desde 8° básico, amplía investigación de referentes, experimentación material, juicio crítico, montaje y comunicación hacia audiencias escolares y locales.",
  "barrier":"copiar referentes, reducir el juicio a gusto personal o difundir obras e imágenes sin consentimiento, crédito ni cuidado del espacio",
  "outcomes":["investigar arquitectura, espacio y diseño urbano mediante observación situada","experimentar con grabado, mural, libro de artista y medios digitales","fundamentar juicios sobre obras propias, de pares y del entorno","diseñar una difusión accesible, ética y pertinente"],
  "method":"Alterna observación contextualizada, pruebas materiales seguras, bitácora, producción autoral, crítica con criterios y montaje o difusión con permisos explícitos.",
  "evidence":"proyecto o juicio visual individual con referentes atribuidos, decisiones de lenguaje y materialidad, revisión documentada y propósito de comunicación",
 },
 "musica":{
  "purpose":"Apreciar músicas diversas; interpretar, improvisar, crear y registrar repertorio; y evaluar cómo las decisiones musicales participan en identidades, culturas y trabajo colectivo.",
  "continuity":"Desde 8° básico, aumenta precisión técnica, autonomía de ensayo, comparación estilística, creación mediante arreglos y reflexión sobre identidad y memoria.",
  "barrier":"confundir calidad con volumen o velocidad, imitar sin reconocer estilo ni intención o evaluar personas en vez de evidencia audible y proceso",
  "outcomes":["comparar músicas mediante rasgos audibles, propósito y contexto","interpretar repertorio a una o más voces con decisiones expresivas","improvisar, crear y arreglar ideas musicales","evaluar fortalezas, crecimiento e identidad mediante registros de proceso"],
  "method":"Escucha antes de nombrar, ubica evidencia temporal precisa, ensaya por focos breves, registra versiones y justifica ajustes desde el efecto audible y el contexto.",
  "evidence":"registro, interpretación, creación o análisis individual que localiza rasgos audibles, explica una decisión musical y documenta una mejora",
 },
 "educacion-fisica-salud":{
  "purpose":"Perfeccionar habilidades motrices; modificar estrategias y tácticas; diseñar entrenamiento saludable; practicar con autocuidado y primeros auxilios; y promover actividad física inclusiva.",
  "continuity":"Desde 8° básico, aumenta autonomía para regular carga, evaluar decisiones tácticas, elegir variantes equivalentes y organizar prácticas seguras en distintos entornos.",
  "barrier":"equiparar aprendizaje con rendimiento competitivo, imponer la misma carga a todos o evaluar el resultado sin observar regulación, estrategia y seguridad",
  "outcomes":["aplicar habilidades específicas con control y seguridad","modificar estrategias según espacio, reglas y respuesta de otras personas","diseñar y ajustar un plan personal sin comparar cuerpos","promover prácticas comunitarias inclusivas y seguras"],
  "method":"Usa estaciones y juegos reducidos sin eliminación, variantes equivalentes, escala de esfuerzo percibido, pausas tácticas y registros privados centrados en decisiones y seguridad.",
  "evidence":"desempeño o plan individual que explica una decisión motriz, táctica o de carga, aplica autocuidado y ajusta una condición con evidencia",
 },
 "orientacion":{
  "purpose":"Tomar decisiones protegidas sobre proyectos de vida, sexualidad, salud, relaciones, conflictos y participación, mediante derechos, consecuencias, apoyos y revisión de alternativas.",
  "continuity":"Desde 8° básico, profundiza autonomía, deliberación, participación institucional y diseño flexible de proyectos académicos, laborales, familiares y comunitarios.",
  "barrier":"exigir experiencias personales, moralizar o diagnosticar, prometer confidencialidad absoluta o reducir un proyecto de vida a una decisión irreversible",
  "outcomes":["comparar alternativas de proyectos de vida sin fijar identidades ni destinos","analizar sexualidad, riesgos y bienestar mediante casos protegidos y fuentes confiables","resolver conflictos y relaciones digitales en un marco de derechos","diseñar iniciativas de participación, buen trato y bien común"],
  "method":"Trabaja siempre con casos ficticios en tercera persona, rutas institucionales de ayuda, matrices de opciones y consecuencias y participación sin exposición íntima.",
  "evidence":"análisis individual de un caso ficticio que distingue hechos, derechos y límites, compara alternativas y propone una acción segura con apoyo pertinente",
 },
 "tecnologia":{
  "purpose":"Identificar necesidades, desarrollar y evaluar servicios con recursos digitales u otros medios, comunicar procesos y analizar cómo tecnologías y entornos cambian y producen efectos sociales.",
  "continuity":"Desde 8° básico, pasa de productos a servicios y aumenta autonomía para investigar usuarios, definir criterios, probar procesos y evaluar impactos éticos y sociales.",
  "barrier":"producir antes de comprender la necesidad, evaluar solo funcionamiento o apariencia y usar datos, herramientas o imágenes sin revisar privacidad, autoría y seguridad",
  "outcomes":["definir oportunidades de servicio desde evidencia de usuarios","planificar y desarrollar con criterios técnicos, éticos y de seguridad","probar, evaluar y mejorar procesos y resultados","comunicar a distintas audiencias y analizar efectos de la evolución tecnológica"],
  "method":"Parte de una necesidad ficticia o documentada sin datos personales, representa el servicio, prueba un criterio por vez y comunica decisiones, fallas e impactos con trazabilidad.",
  "evidence":"propuesta o evaluación individual de un servicio que declara usuario, necesidad, criterios, prueba, mejora e impactos éticos, sociales o ambientales",
 },
}


def grade_seven_index_documentation(objs,classes):
 grade_objs=[item for item in objs if item["course_order"]==7]
 grade_classes=[item for item in classes if item["course_order"]==7]
 core_objs=[item for item in grade_objs if item["subject_slug"] in GRADE_SEVEN_CORE_PROFILES]
 core_classes=[item for item in grade_classes if item["subject_slug"] in GRADE_SEVEN_CORE_PROFILES]
 developed=sum(item["editorial_status"]=="desarrollada" for item in core_classes)
 integrated=sum(item["editorial_status"]=="integrada" for item in core_classes)
 pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 lines=["# 📚 7° básico con desarrollo interno completo","",
  "> [⬅️ Volver al programa](../../README.md) · [🗂️ Índice curricular](../../CURRICULUM.md) · [🧭 Guía docente](../../TEACHING_GUIDE.md) · [📊 Rúbrica](../RUBRICA_EVALUACION.md)","",
  f"**{len(grade_classes):,} propuestas · 12 denominaciones curriculares · {len(core_objs)} OA · {developed} clases disciplinares · {integrated} experiencias transversales integradas · {pending} pendientes · revisión humana pendiente**".replace(",","."),"",
  "> **Alcance honesto:** todos los objetivos inventariados del nivel cuentan con secuencia disciplinar o integración transversal. Completo describe desarrollo interno automatizado; la revisión humana especializada sigue pendiente.","",
  "## 🗂️ Recorridos disponibles","","| Asignatura | OA | Desarrolladas | Integradas | Pendientes | Guía |","|---|---:|---:|---:|---:|---|"]
 for slug in ("matematica","lengua-literatura","ciencias-naturales","historia-geografia-ciencias-sociales","ingles","ingles-propuesta","educacion-fisica-salud","artes-visuales","musica","orientacion","tecnologia","lengua-indigena"):
  pool=[item for item in core_objs if item["subject_slug"]==slug]
  name=pool[0]["subject"]
  d=sum(len(item["phases"]) for item in pool if item.get("developed"))
  i=sum(len(item["phases"]) for item in pool if item.get("integration"))
  lines.append(f"| {name} | {len(pool)} | {d} | {i} | 0 | [📘 Leer](./{slug}.md) |")
 lines += ["","## 🧠 Progresión común","","~~~mermaid","flowchart LR","    A[Recuperar evidencia de 6°] --> B[Modelado disciplinar]","    B --> C[Práctica guiada y retroalimentación]","    C --> D[Desempeño individual]","    D --> E[Evidencia y decisión]","~~~","","La anatomía es estable para facilitar la planificación, pero los textos, problemas, materiales, errores previsibles, productos y criterios cambian según cada OA.","","## 🔎 Estado del nivel","",f"Las {len(grade_classes):,} propuestas están clasificadas como desarrolladas o integradas; permanecen {pending} fichas secuenciadas o borradores.".replace(",","."),"","## Límites","","- Las clases cumplen el contrato automatizado, pero continúan pendientes de revisión humana disciplinar y pedagógica.","- Los recursos externos se enlazan; no se reproducen obras protegidas.","- La adaptación de 45 minutos conserva modelado, práctica y evidencia individual.",""]
 return "\n".join(lines)


def grade_seven_page(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,7)
 subjects=[item for item in subjects if item["slug"] in GRADE_SEVEN_CORE_PROFILES]
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas · {item['integrated']} integradas · {item['classes']-item['developed']-item['integrated']} pendientes</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_SEVEN_CORE_PROFILES[item['slug']]['purpose'])}</p><a href="../docs/7-basico/{item['slug']}.html">Explorar asignatura →</a></article>''' for item in subjects)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="7° básico completo: {developed} clases desarrolladas y {integrated} experiencias integradas en 12 denominaciones curriculares."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/7-basico.html"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><title>7° básico completo | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenidos">Saltar a contenidos</a><header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al explorador</a></header>
<main id="contenidos" class="level-shell"><header class="level-hero"><div><p class="eyebrow">Desarrollo pedagógico interno completo · Chile</p><h1>7° básico</h1><p>Las {len(grade_classes):,} propuestas de las doce denominaciones curriculares están resueltas como {developed} clases disciplinares y {integrated} experiencias transversales integradas. La revisión humana especializada continúa pendiente.</p><div class="hero-actions"><a class="button primary" href="../docs/7-basico/index.html">Abrir mapa del nivel</a><a class="button dark-text" href="../index.html?nivel={quote('7° básico')}#explorar">Explorar clases</a></div></div><aside><span>Estado editorial real</span><strong>{developed} desarrolladas</strong><small>{integrated} integradas · {pending} pendientes · revisión humana pendiente</small></aside></header>
<section class="level-metrics"><div><strong>{len(grade_objs)}</strong><span>OA inventariados</span></div><div><strong>12</strong><span>denominaciones completas</span></div><div><strong>{developed}</strong><span>clases disciplinares</span></div><div><strong>{integrated}</strong><span>experiencias integradas</span></div></section><section class="level-intro"><div><p class="eyebrow">Nivel completo</p><h2>Doce recorridos con método disciplinar y continuidad desde 6°.</h2></div><p>La estructura común facilita planificar, pero cada disciplina conserva sus decisiones: problemas y argumentos, textos y audiencias, investigación y fuentes, creación y escucha, movimiento seguro, comunicación en inglés, aprendizaje cultural situado, autocuidado y diseño tecnológico.</p></section><section class="level-grid">{cards}</section><section class="level-contract"><div><p class="eyebrow">Lectura honesta</p><h2>Completo no significa revisado.</h2></div><ol><li><strong>{developed} clases disciplinares</strong><span>Todos los objetivos de contenido tienen secuencias específicas.</span></li><li><strong>{integrated} experiencias integradas</strong><span>Habilidades y actitudes se observan dentro del contenido.</span></li><li><strong>{pending} propuestas pendientes</strong><span>No quedan fichas sólo secuenciadas ni borradores.</span></li><li><strong>0 revisiones humanas</strong><span>La verificación automática no sustituye revisión profesional.</span></li></ol></section></main><footer class="site-footer"><div><strong>7° básico completo</strong><span>Desarrollo interno completo · revisión humana pendiente</span></div><div><a href="../levels/6-basico.html">6° básico</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''.replace("1,","1.")


def grade_seven_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,7)
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 lines=["# 7° básico — mapa de contenidos","",f"> **Desarrollo pedagógico interno completo:** {developed} clases desarrolladas · {integrated} experiencias transversales integradas · {pending} propuestas pendientes · {len(grade_objs)} OA · 12 denominaciones curriculares · revisión humana pendiente.","","[Programa narrativo de 7° básico](7-basico/README.md) · [Índice Markdown de clases](../CURRICULUM.md) · [Guía pedagógica](../TEACHING_GUIDE.md) · [Evaluación formativa](EVALUACION_FORMATIVA.md)","","Todos los objetivos de contenido cuentan con secuencias específicas. Las entradas integradas corresponden a habilidades o actitudes observadas dentro de esas clases; no duplican el horario.","","## Cobertura","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Pendientes |","|---|---:|---:|---:|---:|---:|"]
 for item in subjects:lines.append(f"| {item['name']} | {item['oa']} | {item['classes']} | {item['developed']} | {item['integrated']} | {item['classes']-item['developed']-item['integrated']} |")
 lines += ["","## Continuidad con 6° básico","","Cada secuencia recupera evidencia previa y amplía precisión, autonomía, contraste, creación y transferencia sin sustituir el objetivo de 7°.","","## Verificación y límite","",f"El catálogo registra {len(grade_objs)} OA y {len(grade_classes):,} propuestas: {developed} desarrolladas, {integrated} integradas y {pending} pendientes.".replace(",","."),"La CI comprueba estructura, cobertura, unicidad, fuentes, licencias y reproducción. Esto no sustituye revisión humana.",""]
 return "\n".join(lines)


def grade_eight_index_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,8)
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 lines=["# 📚 8° básico con desarrollo interno completo","","> [⬅️ Volver al programa](../../README.md) · [🗂️ Índice curricular](../../CURRICULUM.md) · [🧭 Guía docente](../../TEACHING_GUIDE.md) · [📊 Rúbrica](../RUBRICA_EVALUACION.md),".rstrip(","),"",f"**{len(grade_classes):,} propuestas · 12 denominaciones curriculares · {len(grade_objs)} OA · {developed} clases disciplinares · {integrated} experiencias transversales integradas · {pending} pendientes · revisión humana pendiente**".replace(",","."),"","> **Alcance honesto:** todos los objetivos inventariados de 8° cuentan con secuencia disciplinar o integración transversal. Completo describe desarrollo interno automatizado; la revisión humana especializada sigue pendiente.","","## 🗂️ Estado por asignatura","","| Asignatura | OA | Desarrolladas | Integradas | Pendientes | Guía |","|---|---:|---:|---:|---:|---|"]
 for item in subjects:
  pending_subject=item["classes"]-item["developed"]-item["integrated"]
  guide=f"[📘 Leer](./{item['slug']}.md)" if item["slug"] in GRADE_EIGHT_CORE_PROFILES else "Pendiente"
  lines.append(f"| {item['name']} | {item['oa']} | {item['developed']} | {item['integrated']} | {pending_subject} | {guide} |")
 lines += ["","## 🧠 Progresión común","","~~~mermaid","flowchart LR","    A[Recuperar evidencia de 7°] --> B[Problema, texto o desafío situado]","    B --> C[Modelado disciplinar]","    C --> D[Práctica guiada con retroalimentación]","    D --> E[Desempeño individual]","    E --> F[Evidencia y decisión]","~~~","","## Límites","","- Completo significa que no quedan fichas secuenciadas o borradores dentro del nivel; no significa revisión humana, certificación ni pilotaje de aula.","- Las clases desarrolladas cumplen el contrato automatizado, pero continúan pendientes de revisión humana disciplinar y pedagógica.","- Los recursos externos se enlazan y cada adaptación breve conserva modelado, práctica y evidencia individual.",""]
 return "\n".join(lines)


def grade_eight_page(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,8)
 subjects=[item for item in subjects if item["slug"] in GRADE_EIGHT_CORE_PROFILES]
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas · {item['integrated']} integradas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_EIGHT_CORE_PROFILES[item['slug']]['purpose'])}</p><a href="../docs/8-basico/{item['slug']}.html">Explorar asignatura →</a></article>''' for item in subjects)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="8° básico completo: {developed} clases desarrolladas y {integrated} experiencias integradas en 12 denominaciones curriculares."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/8-basico.html"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><title>8° básico completo | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenidos">Saltar a contenidos</a><header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al explorador</a></header>
<main id="contenidos" class="level-shell"><header class="level-hero"><div><p class="eyebrow">Desarrollo pedagógico interno completo · Chile</p><h1>8° básico</h1><p>Las {len(grade_classes):,} propuestas de las doce denominaciones curriculares están resueltas como {developed} clases disciplinares y {integrated} experiencias transversales integradas. La revisión humana especializada continúa pendiente.</p><div class="hero-actions"><a class="button primary" href="../docs/8-basico/index.html">Abrir mapa del nivel</a><a class="button dark-text" href="../index.html?nivel={quote('8° básico')}#explorar">Explorar clases</a></div></div><aside><span>Estado editorial real</span><strong>{developed} desarrolladas</strong><small>{integrated} integradas · {pending} pendientes · revisión humana pendiente</small></aside></header>
<section class="level-metrics"><div><strong>{len(grade_objs)}</strong><span>OA inventariados</span></div><div><strong>{len(subjects)}</strong><span>denominaciones completas</span></div><div><strong>{developed}</strong><span>clases disciplinares</span></div><div><strong>{integrated}</strong><span>experiencias integradas</span></div></section><section class="level-intro"><div><p class="eyebrow">Nivel completo</p><h2>Doce recorridos con continuidad desde 7°.</h2></div><p>El nivel articula problemas y textos, indagación y fuentes, creación y escucha, movimiento seguro, comunicación en inglés, aprendizaje cultural situado, autocuidado, participación y diseño tecnológico.</p></section><section class="level-grid">{cards}</section><section class="level-contract"><div><p class="eyebrow">Lectura honesta</p><h2>Completo no significa revisado.</h2></div><ol><li><strong>{developed} clases disciplinares</strong><span>Todos los objetivos de contenido tienen secuencias específicas.</span></li><li><strong>{integrated} experiencias integradas</strong><span>Habilidades y actitudes se observan dentro del contenido.</span></li><li><strong>{pending} propuestas pendientes</strong><span>No quedan fichas sólo secuenciadas ni borradores.</span></li><li><strong>0 revisiones humanas</strong><span>La verificación automática no sustituye revisión profesional.</span></li></ol></section></main><footer class="site-footer"><div><strong>8° básico completo</strong><span>Desarrollo interno completo · revisión humana pendiente</span></div><div><a href="../levels/7-basico.html">7° básico</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''.replace("1,","1.")


def grade_eight_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,8)
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 lines=["# 8° básico — mapa de contenidos","",f"> **Desarrollo pedagógico interno completo:** {developed} clases desarrolladas · {integrated} experiencias transversales integradas · {pending} propuestas pendientes · {len(grade_objs)} OA · 12 denominaciones curriculares · revisión humana pendiente.","","[Programa narrativo de 8° básico](8-basico/README.md) · [Índice Markdown de clases](../CURRICULUM.md) · [Guía pedagógica](../TEACHING_GUIDE.md) · [Evaluación formativa](EVALUACION_FORMATIVA.md)","","Todos los objetivos inventariados cuentan con secuencias específicas o integraciones transversales; no quedan propuestas sólo secuenciadas ni borradores en el nivel.","","## Cobertura","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Pendientes |","|---|---:|---:|---:|---:|---:|"]
 for item in subjects:lines.append(f"| {item['name']} | {item['oa']} | {item['classes']} | {item['developed']} | {item['integrated']} | {item['classes']-item['developed']-item['integrated']} |")
 lines += ["","## Continuidad con 7° básico","","Las doce denominaciones recuperan evidencias de 7° y elevan formalización, autonomía, lectura crítica, producción, modelación, investigación, creación, comunicación, participación y transferencia sin suponer dominio por calendario.","","## Verificación y límite","",f"El catálogo registra {len(grade_objs)} OA y {len(grade_classes):,} propuestas: {developed} desarrolladas, {integrated} integradas y {pending} pendientes.".replace(",","."),"La CI comprueba estructura, cobertura, unicidad, fuentes, licencias y reproducción. Esto no sustituye revisión humana.",""]
 return "\n".join(lines)


def grade_one_middle_index_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,9)
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 lines=["# 🎓 1° medio con desarrollo interno completo","","> [⬅️ Volver al programa](../../README.md) · [🗂️ Índice curricular](../../CURRICULUM.md) · [🧭 Guía docente](../../TEACHING_GUIDE.md) · [📊 Rúbrica](../RUBRICA_EVALUACION.md)","",f"**{len(grade_classes):,} propuestas · 11 denominaciones curriculares · {len(grade_objs)} OA · {developed} clases disciplinares desarrolladas · {integrated} experiencias transversales integradas · {pending} propuestas pendientes · revisión humana pendiente**".replace(",","."),"","> **Alcance honesto:** todos los objetivos inventariados del nivel cuentan con secuencia disciplinar o integración transversal. Completo describe desarrollo interno automatizado; la revisión humana especializada sigue pendiente.","","## 🗂️ Estado por asignatura","","| Asignatura | OA | Desarrolladas | Integradas | Pendientes | Guía |","|---|---:|---:|---:|---:|---|"]
 for item in subjects:
  guide=f"[📘 Leer](./{item['slug']}.md)" if item["slug"] in GRADE_ONE_MIDDLE_CORE_PROFILES else "Pendiente"
  lines.append(f"| {item['name']} | {item['oa']} | {item['developed']} | {item['integrated']} | {item['classes']-item['developed']-item['integrated']} | {guide} |")
 lines += ["","## 🧠 Progresión común","","~~~mermaid","flowchart LR","    A[Recuperar evidencia de 8°] --> B[Problema, texto o desafío situado]","    B --> C[Modelado disciplinar]","    C --> D[Práctica guiada con retroalimentación]","    D --> E[Desempeño individual]","    E --> F[Evidencia y decisión]","~~~","","## Límites","","- Completo significa que no quedan fichas secuenciadas o borradores dentro del nivel; no significa revisión humana, certificación ni pilotaje de aula.","- Las clases cumplen el contrato automatizado, pero siguen pendientes de revisión humana disciplinar y pedagógica.","- La oferta completa no constituye un horario obligatorio ni sustituye la planificación institucional.",""]
 return "\n".join(lines)


def grade_one_middle_page(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,9)
 subjects=[item for item in subjects if item["slug"] in GRADE_ONE_MIDDLE_CORE_PROFILES]
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas · {item['integrated']} integradas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_ONE_MIDDLE_CORE_PROFILES[item['slug']]['purpose'])}</p><a href="../docs/1-medio/{item['slug']}.html">Explorar asignatura →</a></article>''' for item in subjects)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="1° medio completo: {developed} clases desarrolladas y {integrated} experiencias integradas en 11 denominaciones curriculares."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/1-medio.html"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><title>1° medio completo | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenidos">Saltar a contenidos</a><header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al explorador</a></header>
<main id="contenidos" class="level-shell"><header class="level-hero"><div><p class="eyebrow">Desarrollo pedagógico interno completo · Chile</p><h1>1° medio</h1><p>Las {len(grade_classes):,} propuestas de las once denominaciones curriculares están resueltas como {developed} clases disciplinares y {integrated} experiencias transversales integradas. La revisión humana especializada continúa pendiente.</p><div class="hero-actions"><a class="button primary" href="../docs/1-medio/index.html">Abrir mapa del nivel</a><a class="button dark-text" href="../index.html?nivel={quote('1° medio')}#explorar">Explorar clases</a></div></div><aside><span>Estado editorial real</span><strong>{developed} desarrolladas</strong><small>{integrated} integradas · {pending} pendientes · revisión humana pendiente</small></aside></header>
<section class="level-metrics"><div><strong>{len(grade_objs)}</strong><span>OA inventariados</span></div><div><strong>11</strong><span>denominaciones completas</span></div><div><strong>{developed}</strong><span>clases disciplinares</span></div><div><strong>{integrated}</strong><span>experiencias integradas</span></div></section><section class="level-intro"><div><p class="eyebrow">Nivel completo</p><h2>Once recorridos con continuidad desde 8° básico.</h2></div><p>El nivel articula razonamiento matemático, literatura, ciencias, historia, comunicación en inglés, creación visual y musical, movimiento seguro, proyectos de vida, participación y servicios tecnológicos.</p></section><section class="level-grid">{cards}</section><section class="level-contract"><div><p class="eyebrow">Lectura honesta</p><h2>Completo no significa revisado.</h2></div><ol><li><strong>{developed} clases disciplinares</strong><span>Todos los objetivos de contenido tienen secuencias específicas.</span></li><li><strong>{integrated} experiencias integradas</strong><span>Habilidades y actitudes se observan dentro del contenido.</span></li><li><strong>{pending} propuestas pendientes</strong><span>No quedan fichas sólo secuenciadas ni borradores.</span></li><li><strong>0 revisiones humanas</strong><span>La verificación automática no sustituye revisión profesional.</span></li></ol></section></main><footer class="site-footer"><div><strong>1° medio completo</strong><span>Desarrollo interno completo · revisión humana pendiente</span></div><div><a href="../levels/8-basico.html">8° básico</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''.replace("1,209","1.209")


def grade_one_middle_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,9)
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 lines=["# 1° medio — mapa de contenidos","",f"> **Desarrollo pedagógico interno completo:** {developed} clases desarrolladas · {integrated} experiencias transversales integradas · {pending} propuestas pendientes · {len(grade_objs)} OA · 11 denominaciones curriculares · revisión humana pendiente.","","[Programa narrativo de 1° medio](1-medio/README.md) · [Índice Markdown de clases](../CURRICULUM.md) · [Guía pedagógica](../TEACHING_GUIDE.md) · [Evaluación formativa](EVALUACION_FORMATIVA.md)","","Todos los objetivos inventariados cuentan con secuencias específicas o integraciones transversales; no quedan propuestas sólo secuenciadas ni borradores en el nivel.","","## Cobertura","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Pendientes |","|---|---:|---:|---:|---:|---:|"]
 for item in subjects:lines.append(f"| {item['name']} | {item['oa']} | {item['classes']} | {item['developed']} | {item['integrated']} | {item['classes']-item['developed']-item['integrated']} |")
 lines += ["","## Continuidad con 8° básico","","Las once denominaciones recuperan evidencias de 8° y elevan formalización, autonomía, lectura crítica, modelación, investigación, creación, comunicación, participación y transferencia sin suponer dominio por calendario.","","## Verificación y límite","",f"El catálogo registra {len(grade_objs)} OA y {len(grade_classes):,} propuestas: {developed} desarrolladas, {integrated} integradas y {pending} pendientes.".replace(",","."),"La CI comprueba estructura, cobertura, unicidad, fuentes, licencias y reproducción. Esto no sustituye revisión humana.",""]
 return "\n".join(lines)


GRADE_TWO_MIDDLE_CORE_PROFILES={
 "matematica":{
  "purpose":"Razonar con números reales, raíces y logaritmos; modelar funciones y ecuaciones cuadráticas, inversas y cambio porcentual; justificar geometría de esfera y trigonometría; y evaluar distribuciones, conteo y decisiones probabilísticas.",
  "continuity":"Desde 1° medio, aumenta la formalización funcional, la selección de modelos, la argumentación trigonométrica y la lectura crítica de probabilidades en contextos sociales.",
  "barrier":"aplicar fórmulas o comandos sin declarar dominio, condiciones, unidades, representación ni una comprobación independiente",
  "outcomes":["operar y argumentar con raíces, potencias y logaritmos","modelar relaciones cuadráticas, inversas y cambios porcentuales","derivar y aplicar relaciones geométricas y trigonométricas","evaluar distribuciones, conteos y afirmaciones probabilísticas con límites"],
  "method":"Parte de una situación o representación, hace visibles dominio y condiciones, conecta registros numéricos, gráficos y simbólicos y exige estimación, argumento, unidad y comprobación.",
  "evidence":"solución individual con representación pertinente, procedimiento justificable, interpretación situada y comprobación o limitación explícita",
 },
 "lengua-literatura":{
  "purpose":"Sostener una trayectoria lectora; interpretar narrativa, poesía, drama, Siglo de Oro y cuento latinoamericano; evaluar argumentos y medios; y producir textos, diálogos, exposiciones e investigaciones para audiencias definidas.",
  "continuity":"Desde 1° medio, profundiza arquitectura narrativa, soneto, atmósfera escénica, contexto cultural, falacias, modalización, escritura académica, correferencia y evaluación retórica.",
  "barrier":"reemplazar análisis por resumen, opinión o etiquetas; usar contexto sin evidencia; o revisar productos sin atender propósito, audiencia, fuentes y decisiones de autor",
  "outcomes":["seleccionar y sostener lecturas con propósitos propios","interpretar obras mediante evidencia, forma, contexto y perspectivas revisables","evaluar argumentación, medios y discursos multimodales","investigar, escribir, dialogar y exponer con fuentes, revisión y responsabilidad"],
  "method":"Trabaja con corpus atribuidos, lectura y escucha con propósito, conversación protegida, escritura por procesos y revisión centrada en evidencia, progresión, audiencia y efecto.",
  "evidence":"interpretación, texto, intervención oral o informe individual que usa evidencia precisa, reconoce contexto y justifica decisiones para una audiencia",
 },
}

GRADE_TWO_MIDDLE_CORE_PROFILES.update({
 "ciencias-naturales":{
  **GRADE_ONE_MIDDLE_CORE_PROFILES["ciencias-naturales"],
  "purpose":"Explicar regulación nerviosa y hormonal, sexualidad y herencia; investigar movimiento, fuerzas, energía y gravitación; y modelar soluciones y compuestos orgánicos con evidencia, seguridad y responsabilidad.",
  "continuity":"Desde 1° medio, conecta modelos biológicos, físicos y químicos con mecanismos de regulación, análisis cuantitativo, diseño experimental, incertidumbre e implicancias éticas y sociales.",
  "outcomes":["modelar regulación, reproducción y herencia con evidencia y resguardos","analizar movimiento, fuerzas, energía y momentum con sistemas y unidades explícitas","explicar gravitación y cambio de modelos astronómicos","investigar soluciones y carbono mediante partículas, propiedades, seguridad y límites"],
 },
 "historia-geografia-ciencias-sociales":{
  **GRADE_ONE_MIDDLE_CORE_PROFILES["historia-geografia-ciencias-sociales"],
  "purpose":"Interpretar transformaciones mundiales y chilenas del siglo XX; analizar democracia, dictadura, derechos humanos y globalización; y deliberar sobre diversidad y desafíos actuales con fuentes contrastadas.",
  "continuity":"Desde 1° medio, prolonga la historia contemporánea hacia guerras mundiales, Guerra Fría y Chile reciente, aumentando contraste historiográfico, memoria, ciudadanía y argumentación democrática.",
  "outcomes":["explicar crisis, guerras y orden mundial mediante causas, actores y consecuencias","analizar transformaciones sociales, económicas y políticas de Chile en el siglo XX","comparar interpretaciones sobre quiebre democrático, dictadura y transición","deliberar sobre derechos, diversidad y desafíos del país con evidencia contextualizada"],
 },
 "ingles":{
  **GRADE_ONE_MIDDLE_CORE_PROFILES["ingles"],
  "purpose":"Comprender, interactuar, leer y escribir en inglés con textos más variados, estrategias explícitas, funciones del nivel y decisiones ajustadas a propósito, audiencia, cultura y evidencia.",
  "continuity":"Desde 1° medio, amplía inferencia, relaciones entre ideas, toma de notas, reparación oral y escritura independiente mediante funciones temporales, hipotéticas y de reporte.",
  "outcomes":["comprender ideas, detalles y relaciones en escucha y lectura","interactuar y presentar con reparación, recursos multimodales y conciencia de audiencia","responder críticamente y formular hipótesis con evidencia","escribir de modo más independiente para analizar, narrar e informar"],
 },
 "ingles-propuesta":{
  **GRADE_ONE_MIDDLE_CORE_PROFILES["ingles-propuesta"],
  "purpose":"Integrar escucha, lectura, interacción y escritura en inglés mediante textos literarios y funcionales, estrategias transferibles y tareas comunicativas con propósito y revisión.",
  "continuity":"Desde 1° medio, profundiza síntesis, respuesta crítica, presentación multimodal, funciones del nivel y publicación independiente para audiencias definidas.",
  "outcomes":["escuchar y leer textos variados con propósito y evidencia localizada","relacionar información, sintetizar y responder críticamente","presentar e interactuar con fluidez reparable y recursos pertinentes","escribir, revisar y publicar textos conectados con funciones del nivel"],
 },
 "artes-visuales":{
  **GRADE_ONE_MIDDLE_CORE_PROFILES["artes-visuales"],
  "purpose":"Crear proyectos sobre problemáticas sociales y juveniles mediante espacio público, escultura, diseño, video y multimedia; construir criterios estéticos; y difundir con aporte comunitario.",
  "continuity":"Desde 1° medio, desplaza el foco hacia problemáticas contemporáneas, sustentabilidad material, medios audiovisuales, criterios personales y gestión comunitaria de la difusión.",
  "outcomes":["investigar problemáticas y contextos antes de crear","experimentar con escultura, diseño, video y multimedia","argumentar criterios estéticos y revisar proyectos propios y de pares","implementar difusión accesible, ética y pertinente para la comunidad"],
 },
 "musica":{
  **GRADE_ONE_MIDDLE_CORE_PROFILES["musica"],
  "purpose":"Valorar y contrastar músicas de Chile y el mundo; seleccionar, dirigir, interpretar, registrar y difundir repertorio; innovar en arreglos; y diseñar mejoras desde evidencia audible.",
  "continuity":"Desde 1° medio, aumenta autonomía de selección y dirección, exigencia crítica, fluidez creativa y comprensión del papel de las tecnologías de registro y transmisión.",
  "outcomes":["valorar y contrastar músicas mediante rasgos, contexto y propósito","interpretar y dirigir repertorio con conciencia estilística","improvisar y crear arreglos fluidos e innovadores","evaluar registros y convertir hallazgos en un plan de mejora"],
 },
 "educacion-fisica-salud":{
  **GRADE_ONE_MIDDLE_CORE_PROFILES["educacion-fisica-salud"],
  "purpose":"Perfeccionar habilidades motrices; diseñar y evaluar tácticas; aplicar un plan personal de entrenamiento saludable; practicar con seguridad; y liderar actividad física comunitaria inclusiva.",
  "continuity":"Desde 1° medio, aumenta precisión, autonomía para evaluar táctica y carga, continuidad del entrenamiento, primeros auxilios y liderazgo distribuido en la comunidad.",
  "outcomes":["aplicar habilidades específicas con precisión y variantes equivalentes","diseñar, probar y ajustar estrategias deportivas","regular un plan personal de entrenamiento sin comparar cuerpos","liderar prácticas comunitarias inclusivas, seguras y sostenibles"],
 },
 "orientacion":{
  **GRADE_ONE_MIDDLE_CORE_PROFILES["orientacion"],
  "purpose":"Comparar y diseñar proyectos de vida; analizar sexualidad, riesgos y bienestar; promover relaciones y resolución de conflictos con derechos; y desarrollar iniciativas democráticas de bien común.",
  "continuity":"Desde 1° medio, eleva la autonomía para contrastar trayectorias, recurrir a redes, promover bienestar y convertir deliberación sobre derechos en iniciativas colectivas protegidas.",
  "outcomes":["comparar opciones académicas, laborales y vitales sin fijar destinos","analizar sexualidad, riesgos y bienestar mediante casos y redes confiables","resolver relaciones y conflictos en un marco de dignidad e inclusión","diseñar y evaluar iniciativas democráticas de justicia y buen trato"],
 },
 "tecnologia":{
  **GRADE_ONE_MIDDLE_CORE_PROFILES["tecnologia"],
  "purpose":"Identificar impactos energéticos y materiales; diseñar soluciones sustentables con TIC; evaluarlas mediante dilemas éticos, legales, económicos, sociales y ambientales; y proyectar escenarios de innovación.",
  "continuity":"Desde 1° medio, concentra el diseño tecnológico en sustentabilidad, evaluación multivariable, colaboración digital responsable y proyección razonada de impactos positivos y negativos.",
  "barrier":"proponer una solución antes de medir la necesidad, declarar sustentabilidad por una sola ventaja o proyectar impactos sin supuestos, evidencia, privacidad, autoría y seguridad",
  "outcomes":["identificar necesidades energéticas y materiales con evidencia","diseñar colaborativamente soluciones sustentables y trazables","evaluar dilemas e impactos mediante varios criterios","comunicar escenarios y supuestos a audiencias distintas con seguridad"],
 },
})


def grade_two_middle_index_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,10)
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 lines=["# 🏫 2° medio con desarrollo interno completo","","> [⬅️ Volver al programa](../../README.md) · [🗂️ Índice curricular](../../CURRICULUM.md) · [🧭 Guía docente](../../TEACHING_GUIDE.md) · [📊 Rúbrica](../RUBRICA_EVALUACION.md)","",f"**{len(grade_classes):,} propuestas · {len(grade_objs)} OA · {developed} clases disciplinares desarrolladas · {integrated} experiencias transversales integradas · {pending} propuestas pendientes · revisión humana pendiente**".replace(",","."),"","> **Alcance honesto:** las once denominaciones curriculares tienen desarrollo interno completo y no quedan propuestas pendientes. Completo no significa revisión humana, certificación ni pilotaje de aula.","","## 🗂️ Estado por asignatura","","| Asignatura | OA | Desarrolladas | Integradas | Pendientes | Guía |","|---|---:|---:|---:|---:|---|"]
 for item in subjects:
  guide=f"[📘 Leer](./{item['slug']}.md)" if item["slug"] in GRADE_TWO_MIDDLE_CORE_PROFILES else "Pendiente"
  lines.append(f"| {item['name']} | {item['oa']} | {item['developed']} | {item['integrated']} | {item['classes']-item['developed']-item['integrated']} | {guide} |")
 lines += ["","## 🧠 Progresión común","","~~~mermaid","flowchart LR","    A[Recuperar evidencia de 1° medio] --> B[Problema, texto o desafío situado]","    B --> C[Modelado disciplinar]","    C --> D[Práctica guiada con retroalimentación]","    D --> E[Desempeño individual]","    E --> F[Evidencia, revisión y transferencia]","~~~","","## Límites","","- Completo significa que no quedan fichas secuenciadas ni borradores dentro del nivel; no significa revisión humana, certificación ni pilotaje de aula.","- Las clases cumplen el contrato automatizado, pero siguen pendientes de revisión humana disciplinar y pedagógica.","- La oferta no constituye un horario obligatorio ni sustituye la planificación institucional.",""]
 return "\n".join(lines)


def grade_two_middle_page(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,10)
 subjects=[item for item in subjects if item["slug"] in GRADE_TWO_MIDDLE_CORE_PROFILES]
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas · {item['integrated']} integradas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_TWO_MIDDLE_CORE_PROFILES[item['slug']]['purpose'])}</p><a href="../docs/2-medio/{item['slug']}.html">Explorar asignatura →</a></article>''' for item in subjects)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="2° medio completo: {developed} clases y {integrated} experiencias integradas en once denominaciones curriculares."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/2-medio.html"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><title>2° medio completo | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenidos">Saltar a contenidos</a><header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al explorador</a></header>
<main id="contenidos" class="level-shell"><header class="level-hero"><div><p class="eyebrow">Desarrollo pedagógico interno completo · Chile</p><h1>2° medio</h1><p>Las {len(grade_classes):,} propuestas de las once denominaciones curriculares están resueltas como {developed} clases disciplinares y {integrated} experiencias transversales integradas. La revisión humana especializada continúa pendiente.</p><div class="hero-actions"><a class="button primary" href="../docs/2-medio/index.html">Abrir mapa del nivel</a><a class="button dark-text" href="../index.html?nivel={quote('2° medio')}#explorar">Explorar clases</a></div></div><aside><span>Estado editorial real</span><strong>{developed} desarrolladas</strong><small>{integrated} integradas · {pending} pendientes · revisión humana pendiente</small></aside></header>
<section class="level-metrics"><div><strong>{len(grade_objs)}</strong><span>OA inventariados</span></div><div><strong>{len(subjects)}</strong><span>denominaciones completas</span></div><div><strong>{developed}</strong><span>clases disciplinares</span></div><div><strong>{integrated}</strong><span>experiencias integradas</span></div></section><section class="level-intro"><div><p class="eyebrow">Nivel completo</p><h2>Once recorridos con continuidad desde 1° medio.</h2></div><p>El nivel articula modelación matemática, lectura y escritura, investigación científica e histórica, comunicación en inglés, creación artística y musical, movimiento seguro, proyectos de vida y diseño tecnológico sustentable.</p></section><section class="level-grid">{cards}</section><section class="level-contract"><div><p class="eyebrow">Lectura honesta</p><h2>Completo no significa revisado.</h2></div><ol><li><strong>{developed} clases disciplinares</strong><span>Todos los OA de contenido tienen secuencias específicas.</span></li><li><strong>{integrated} experiencias integradas</strong><span>Habilidades y actitudes se observan dentro del contenido.</span></li><li><strong>{pending} propuestas pendientes</strong><span>No quedan fichas sólo secuenciadas ni borradores.</span></li><li><strong>0 revisiones humanas</strong><span>La verificación automática no sustituye revisión profesional.</span></li></ol></section></main><footer class="site-footer"><div><strong>2° medio completo</strong><span>Desarrollo interno completo · revisión humana pendiente</span></div><div><a href="../levels/1-medio.html">1° medio</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''.replace("1,200","1.200")


def grade_two_middle_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,10)
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 lines=["# 2° medio — mapa de contenidos","",f"> **Desarrollo pedagógico interno completo:** {developed} clases desarrolladas · {integrated} experiencias transversales integradas · {pending} propuestas pendientes · {len(grade_objs)} OA · once denominaciones curriculares · revisión humana pendiente.","","[Programa narrativo de 2° medio](2-medio/README.md) · [Índice Markdown de clases](../CURRICULUM.md) · [Guía pedagógica](../TEACHING_GUIDE.md) · [Evaluación formativa](EVALUACION_FORMATIVA.md)","","Todos los objetivos inventariados cuentan con secuencias específicas o integraciones transversales; no quedan propuestas sólo secuenciadas ni borradores en el nivel.","","## Cobertura","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Pendientes |","|---|---:|---:|---:|---:|---:|"]
 for item in subjects:lines.append(f"| {item['name']} | {item['oa']} | {item['classes']} | {item['developed']} | {item['integrated']} | {item['classes']-item['developed']-item['integrated']} |")
 lines += ["","## Continuidad con 1° medio","","Las once denominaciones recuperan evidencias de 1° medio y elevan formalización, autonomía, lectura crítica, modelación, investigación, creación, comunicación, participación y transferencia sin suponer dominio por calendario.","","## Verificación y límite","",f"El catálogo registra {len(grade_objs)} OA y {len(grade_classes):,} propuestas: {developed} desarrolladas, {integrated} integradas y {pending} pendientes.".replace(",","."),"La CI comprueba estructura, cobertura, unicidad, fuentes, licencias y reproducción. Esto no sustituye revisión humana.",""]
 return "\n".join(lines)


GRADE_THREE_MIDDLE_CORE_PROFILES={
 "matematica-3o-medio":{
  "purpose":"Resolver y justificar operaciones con números complejos; tomar decisiones bajo incerteza mediante dispersión y probabilidad condicional; modelar crecimiento y decrecimiento con funciones exponenciales y logarítmicas; y argumentar relaciones métricas en la circunferencia.",
  "continuity":"Desde 2° medio, eleva la formalización algebraica y geométrica, la selección crítica de modelos, el análisis de datos y la comprobación mediante representaciones manuscritas y tecnológicas.",
  "barrier":"aplicar una regla o comando sin declarar condiciones, representación, supuestos, dominio, fuente de datos ni una comprobación independiente",
  "outcomes":["operar números complejos conectando plano, símbolo y comprobación","comparar variabilidad y calcular probabilidades condicionales para decidir con límites","construir y evaluar modelos exponenciales y logarítmicos con fuentes trazables","justificar relaciones entre ángulos, arcos, cuerdas, tangentes y secantes"],
  "method":"Parte de una situación o representación, explicita condiciones y supuestos, conecta registros gráficos, numéricos y simbólicos y exige argumento, interpretación, fuente y comprobación.",
  "evidence":"solución individual con representación pertinente, procedimiento justificable, interpretación situada, fuente cuando usa datos y comprobación o limitación explícita",
 },
 "lengua-literatura-3o-medio":{
  "purpose":"Interpretar obras y sus efectos estéticos; analizar críticamente discursos y comunidades digitales; comprender y producir recursos lingüísticos y multimodales; dialogar argumentativamente e investigar con fuentes válidas, confiables y citadas.",
  "continuity":"Desde 2° medio, concentra la lectura, producción y oralidad en posicionamiento, comunidades discursivas, relaciones intertextuales, ética digital, multimodalidad e investigación autónoma.",
  "barrier":"reemplazar análisis por resumen u opinión, atribuir intenciones sin evidencia, usar recursos como decoración o investigar sin evaluar autoría, validez, alcance y trazabilidad",
  "outcomes":["formular interpretaciones literarias mediante recursos, intertextualidad y efectos estéticos","evaluar géneros discursivos y comunidades digitales desde contexto, razonamiento, evidencia y ética","producir textos coherentes y multimodales ajustados a propósito, género y audiencia","dialogar e investigar con evidencia, citación, revisión y responsabilidad"],
  "method":"Trabaja con corpus atribuidos y legalmente utilizables, lectura o escucha con propósito, conversación protegida, escritura por procesos y verificación explícita de fuentes y efectos multimodales.",
  "evidence":"interpretación, análisis, producción, intervención oral o informe individual que usa evidencia precisa, atribuye fuentes y justifica decisiones para una audiencia",
 },
}
GRADE_THREE_MIDDLE_CORE_PROFILES.update(GRADE_THREE_MIDDLE_REMAINING_PROFILES)


def grade_three_middle_index_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,11)
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 lines=["# 🏫 3° medio · Formación General completo","","> [⬅️ Volver al programa](../../README.md) · [🗂️ Índice curricular](../../CURRICULUM.md) · [🧭 Guía docente](../../TEACHING_GUIDE.md) · [📊 Rúbrica](../RUBRICA_EVALUACION.md)","",f"**{len(grade_classes):,} propuestas · {len(grade_objs)} OA · {developed} clases disciplinares desarrolladas · {integrated} experiencias integradas · {pending} propuestas pendientes · revisión humana pendiente**".replace(",","."),"","> **Alcance honesto:** las dieciocho denominaciones curriculares tienen desarrollo pedagógico interno completo y fuentes oficiales. Ninguna clase se declara revisada por especialistas ni pilotada en aula.","","## 🗂️ Estado por asignatura","","| Asignatura | OA | Desarrolladas | Integradas | Pendientes | Guía |","|---|---:|---:|---:|---:|---|"]
 for item in subjects:
  guide=f"[📘 Leer](./{item['slug']}.md)" if item["slug"] in GRADE_THREE_MIDDLE_CORE_PROFILES else "Pendiente"
  lines.append(f"| {item['name']} | {item['oa']} | {item['developed']} | {item['integrated']} | {item['classes']-item['developed']-item['integrated']} | {guide} |")
 lines += ["","## ✅ Qué está resuelto","",f"Los {len(grade_objs)} OA están desarrollados en {developed} clases disciplinares independientes. No hay experiencias transversales contadas como clases adicionales ni propuestas pendientes.","","Cada guía incluye una explicación pedagógica por OA: significado para la enseñanza, punto de entrada, conceptos explícitos, progresión, evidencia esperada y enlace a la fuente oficial.","","**No está resuelto todavía:** revisión profesional humana, pilotaje de aula y certificación externa.","","## 🧠 Progresión común","","~~~mermaid","flowchart LR","    A[Recuperar evidencia de 2° medio] --> B[Problema, texto o corpus con fuente]","    B --> C[Modelado disciplinar]","    C --> D[Práctica guiada y contraste]","    D --> E[Desempeño individual]","    E --> F[Comprobación, revisión y transferencia]","~~~","","## Fuentes y límites","","- Cada ficha enlaza el OA y la asignatura oficiales en Currículum Nacional.","- Los criterios de progresión se identifican como elaboración pedagógica interna derivada del OA, no como indicadores oficiales.","- Los textos, datos y piezas multimodales deben ser propios, autorizados, de dominio público o enlazados sin reproducción indebida.","- Desarrollo interno no significa revisión humana, certificación ni pilotaje de aula.",""]
 return "\n".join(lines)


def grade_three_middle_page(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,11)
 subjects=[item for item in subjects if item["slug"] in GRADE_THREE_MIDDLE_CORE_PROFILES]
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_THREE_MIDDLE_CORE_PROFILES[item['slug']]['purpose'])}</p><a href="../docs/3-medio/{item['slug']}.html">Explorar asignatura →</a></article>''' for item in subjects)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="3° medio Formación General completo: dieciocho denominaciones con secuencias pedagógicas y fuentes oficiales."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/3-medio.html"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><title>3° medio completo | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenidos">Saltar a contenidos</a><header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al explorador</a></header>
<main id="contenidos" class="level-shell"><header class="level-hero"><div><p class="eyebrow">Desarrollo pedagógico interno completo · Formación General · Chile</p><h1>3° medio</h1><p>Las dieciocho denominaciones reúnen {developed} clases desarrolladas con fuentes oficiales, progresión pedagógica, evaluación formativa y continuidad desde 2° medio.</p><div class="hero-actions"><a class="button primary" href="../docs/3-medio/index.html">Abrir mapa del nivel</a><a class="button dark-text" href="../index.html?nivel={quote('3° medio · Formación General')}#explorar">Explorar clases</a></div></div><aside><span>Estado editorial real</span><strong>{developed} desarrolladas</strong><small>{pending} pendientes · revisión humana pendiente</small></aside></header>
<section class="level-metrics"><div><strong>{len(grade_objs)}</strong><span>OA inventariados</span></div><div><strong>{len(subjects)}</strong><span>denominaciones completas</span></div><div><strong>{developed}</strong><span>clases disciplinares</span></div><div><strong>{pending}</strong><span>propuestas pendientes</span></div></section><section class="level-intro"><div><p class="eyebrow">Nivel completo</p><h2>Dieciocho recorridos con continuidad desde 2° medio.</h2></div><p>Las secuencias abarcan ciencias, ciudadanía, filosofía, lenguas, artes, actividad física, territorio y tecnología mediante evidencias específicas y fuentes trazables.</p></section><section class="level-grid">{cards}</section><section class="level-contract"><div><p class="eyebrow">Lectura honesta</p><h2>Completo no significa revisado.</h2></div><ol><li><strong>{developed} clases desarrolladas</strong><span>Los {len(grade_objs)} OA tienen secuencias específicas.</span></li><li><strong>Fuentes explícitas</strong><span>Cada ficha conserva los enlaces oficiales y rotula la elaboración interna.</span></li><li><strong>{pending} propuestas pendientes</strong><span>No quedan fichas solo secuenciadas ni borradores en el nivel.</span></li><li><strong>0 revisiones humanas</strong><span>La verificación automática no sustituye revisión profesional.</span></li></ol></section></main><footer class="site-footer"><div><strong>3° medio completo</strong><span>Desarrollo interno completo · revisión humana pendiente</span></div><div><a href="../levels/2-medio.html">2° medio</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''


def grade_three_middle_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,11)
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 lines=["# 3° medio · Formación General — mapa de contenidos","",f"> **Desarrollo pedagógico interno completo:** {developed} clases desarrolladas · {integrated} experiencias integradas · {pending} propuestas pendientes · {len(grade_objs)} OA · dieciocho denominaciones curriculares · revisión humana pendiente.","","[Programa narrativo de 3° medio](3-medio/README.md) · [Índice Markdown de clases](../CURRICULUM.md) · [Guía pedagógica](../TEACHING_GUIDE.md) · [Evaluación formativa](EVALUACION_FORMATIVA.md)","","Todos los objetivos inventariados cuentan con secuencias específicas; no quedan propuestas solo secuenciadas ni borradores en el nivel.","","## Cobertura","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Pendientes |","|---|---:|---:|---:|---:|---:|"]
 for item in subjects:lines.append(f"| {item['name']} | {item['oa']} | {item['classes']} | {item['developed']} | {item['integrated']} | {item['classes']-item['developed']-item['integrated']} |")
 lines += ["","## Continuidad con 2° medio","","Las dieciocho denominaciones recuperan evidencias de 2° medio y elevan formalización, autonomía, lectura crítica, modelación, investigación, creación, participación y comunicación sin suponer dominio por calendario.","","## Fuentes, verificación y límite","",f"El catálogo registra {len(grade_objs)} OA y {len(grade_classes):,} propuestas del nivel: {developed} desarrolladas, {integrated} integradas y {pending} pendientes.".replace(",","."),"Cada ficha enlaza Currículum Nacional y separa el texto oficial de la progresión pedagógica interna. La CI comprueba estructura, cobertura, unicidad, fuentes, licencias y reproducción; no sustituye revisión humana.",""]
 return "\n".join(lines)


def grade_four_middle_index_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,12)
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 lines=["# 🏫 4° medio · Formación General completo","","> [⬅️ Volver al programa](../../README.md) · [🗂️ Índice curricular](../../CURRICULUM.md) · [🧭 Guía docente](../../TEACHING_GUIDE.md) · [📊 Rúbrica](../RUBRICA_EVALUACION.md)","",f"**{len(grade_classes):,} propuestas · {len(grade_objs)} OA · {developed} clases disciplinares desarrolladas · {integrated} experiencias integradas · {pending} propuestas pendientes · revisión humana pendiente**".replace(",","."),"","> **Alcance honesto:** las diecisiete denominaciones curriculares tienen desarrollo pedagógico interno completo y fuentes oficiales. Ninguna clase se declara revisada por especialistas ni pilotada en aula.","","## 🗂️ Estado por asignatura","","| Asignatura | OA | Desarrolladas | Integradas | Pendientes | Guía |","|---|---:|---:|---:|---:|---|"]
 for item in subjects:
  guide=f"[📘 Leer](./{item['slug']}.md)" if item["slug"] in GRADE_FOUR_MIDDLE_PROFILES else "Pendiente"
  lines.append(f"| {item['name']} | {item['oa']} | {item['developed']} | {item['integrated']} | {item['classes']-item['developed']-item['integrated']} | {guide} |")
 lines += ["","## ✅ Qué está resuelto","",f"Los {len(grade_objs)} OA están desarrollados en {developed} clases disciplinares independientes. No hay experiencias transversales contadas como clases adicionales ni propuestas pendientes.","","Cada guía incluye una explicación pedagógica por OA: significado para la enseñanza, punto de entrada, conceptos explícitos, progresión, evidencia esperada y enlace a la fuente oficial.","","**No está resuelto todavía:** revisión profesional humana, pilotaje de aula y certificación externa.","","## 🧠 Progresión común","","~~~mermaid","flowchart LR","    A[Recuperar evidencia de 3° medio] --> B[Problema, texto, corpus o desafío con fuente]","    B --> C[Modelado y explicitación de criterios]","    C --> D[Práctica guiada, contraste y retroalimentación]","    D --> E[Desempeño individual autónomo]","    E --> F[Comprobación, revisión, límites y transferencia]","~~~","","## Fuentes y límites","","- Cada ficha enlaza el OA y la asignatura oficiales en Currículum Nacional.","- Los criterios y la dosificación se rotulan como elaboración pedagógica interna, no como indicadores oficiales.","- Los recursos deben ser propios, autorizados, de dominio público o enlazados con atribución.","- Desarrollo interno completo no significa revisión humana, certificación ni pilotaje de aula.",""]
 return "\n".join(lines)


def grade_four_middle_page(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,12)
 subjects=[item for item in subjects if item["slug"] in GRADE_FOUR_MIDDLE_PROFILES]
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_FOUR_MIDDLE_PROFILES[item['slug']]['purpose'])}</p><a href="../docs/4-medio/{item['slug']}.html">Explorar asignatura →</a></article>''' for item in subjects)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="4° medio Formación General completo: diecisiete denominaciones con secuencias pedagógicas y fuentes oficiales."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/4-medio.html"><link rel="icon" href="../icon.svg" type="image/svg+xml"><link rel="stylesheet" href="../styles.css"><title>4° medio completo | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#contenidos">Saltar a contenidos</a><header class="detail-topbar"><a class="brand" href="../index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="../index.html">← Volver al explorador</a></header>
<main id="contenidos" class="level-shell"><header class="level-hero"><div><p class="eyebrow">Desarrollo pedagógico interno completo · Formación General · Chile</p><h1>4° medio</h1><p>Las diecisiete denominaciones reúnen {developed} clases desarrolladas con fuentes oficiales, autonomía de egreso, evaluación formativa y continuidad desde 3° medio.</p><div class="hero-actions"><a class="button primary" href="../docs/4-medio/index.html">Abrir mapa del nivel</a><a class="button dark-text" href="../index.html?nivel={quote('4° medio · Formación General')}#explorar">Explorar clases</a></div></div><aside><span>Estado editorial real</span><strong>{developed} desarrolladas</strong><small>{pending} pendientes · revisión humana pendiente</small></aside></header>
<section class="level-metrics"><div><strong>{len(grade_objs)}</strong><span>OA inventariados</span></div><div><strong>{len(subjects)}</strong><span>denominaciones completas</span></div><div><strong>{developed}</strong><span>clases disciplinares</span></div><div><strong>{pending}</strong><span>propuestas pendientes</span></div></section><section class="level-intro"><div><p class="eyebrow">Trayectoria completa</p><h2>Diecisiete recorridos con continuidad desde 3° medio.</h2></div><p>El nivel consolida decisiones matemáticas, interpretación y producción, ciudadanía, filosofía, inglés, ciencias, artes, actividad física, territorio y tecnología con evidencias específicas y fuentes trazables.</p></section><section class="level-grid">{cards}</section><section class="level-contract"><div><p class="eyebrow">Lectura honesta</p><h2>Completo no significa revisado.</h2></div><ol><li><strong>{developed} clases desarrolladas</strong><span>Los {len(grade_objs)} OA tienen secuencias específicas.</span></li><li><strong>Fuentes explícitas</strong><span>Cada ficha conserva enlaces oficiales y rotula la elaboración interna.</span></li><li><strong>{pending} propuestas pendientes</strong><span>No quedan fichas solo secuenciadas ni borradores.</span></li><li><strong>0 revisiones humanas</strong><span>La verificación automática no sustituye revisión profesional.</span></li></ol></section></main><footer class="site-footer"><div><strong>4° medio completo</strong><span>Desarrollo interno completo · revisión humana pendiente</span></div><div><a href="../levels/3-medio.html">3° medio</a><a href="../documentacion.html">Documentación</a></div></footer></body></html>'''


def grade_four_middle_documentation(objs,classes):
 grade_objs,grade_classes,subjects=grade_summary(objs,classes,12)
 developed=sum(item["editorial_status"]=="desarrollada" for item in grade_classes);integrated=sum(item["editorial_status"]=="integrada" for item in grade_classes);pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in grade_classes)
 lines=["# 4° medio · Formación General — mapa de contenidos","",f"> **Desarrollo pedagógico interno completo:** {developed} clases desarrolladas · {integrated} experiencias integradas · {pending} propuestas pendientes · {len(grade_objs)} OA · diecisiete denominaciones curriculares · revisión humana pendiente.","","[Programa narrativo de 4° medio](4-medio/README.md) · [Índice Markdown de clases](../CURRICULUM.md) · [Guía pedagógica](../TEACHING_GUIDE.md) · [Evaluación formativa](EVALUACION_FORMATIVA.md)","","Todos los objetivos inventariados cuentan con secuencias específicas; no quedan propuestas solo secuenciadas ni borradores en el nivel.","","## Cobertura","","| Asignatura | OA | Propuestas | Desarrolladas | Integradas | Pendientes |","|---|---:|---:|---:|---:|---:|"]
 for item in subjects:lines.append(f"| {item['name']} | {item['oa']} | {item['classes']} | {item['developed']} | {item['integrated']} | {item['classes']-item['developed']-item['integrated']} |")
 lines += ["","## Continuidad con 3° medio","","Las diecisiete denominaciones recuperan evidencias de 3° medio y consolidan autonomía para seleccionar fuentes y estrategias, modelar, interpretar, crear, deliberar, comprobar, revisar y comunicar límites antes del egreso.","","## Fuentes, verificación y límite","",f"El catálogo registra {len(grade_objs)} OA y {len(grade_classes):,} propuestas del nivel: {developed} desarrolladas, {integrated} integradas y {pending} pendientes.".replace(",","."),"Cada ficha enlaza Currículum Nacional y separa el texto oficial de la progresión pedagógica interna. La CI comprueba estructura, cobertura, unicidad, fuentes, licencias y reproducción; no sustituye revisión humana.",""]
 return "\n".join(lines)


def documentation_page(objs,classes):
 _,_,first_subjects=grade_one_summary(objs,classes);_,_,second_subjects=grade_two_summary(objs,classes);_,_,third_subjects=grade_three_summary(objs,classes);_,_,fourth_subjects=grade_four_summary(objs,classes);_,_,fifth_subjects=grade_five_summary(objs,classes);_,_,sixth_subjects=grade_six_summary(objs,classes);_,_,seventh_subjects=grade_summary(objs,classes,7);_,_,eighth_subjects=grade_summary(objs,classes,8);_,_,one_middle_subjects=grade_summary(objs,classes,9);_,_,two_middle_subjects=grade_summary(objs,classes,10);_,_,three_middle_subjects=grade_summary(objs,classes,11);_,_,four_middle_subjects=grade_summary(objs,classes,12)
 seventh_subjects=[item for item in seventh_subjects if item["slug"] in GRADE_SEVEN_CORE_PROFILES]
 eighth_subjects=[item for item in eighth_subjects if item["slug"] in GRADE_EIGHT_CORE_PROFILES]
 one_middle_subjects=[item for item in one_middle_subjects if item["slug"] in GRADE_ONE_MIDDLE_CORE_PROFILES]
 two_middle_subjects=[item for item in two_middle_subjects if item["slug"] in GRADE_TWO_MIDDLE_CORE_PROFILES]
 three_middle_subjects=[item for item in three_middle_subjects if item["slug"] in GRADE_THREE_MIDDLE_CORE_PROFILES]
 four_middle_subjects=[item for item in four_middle_subjects if item["slug"] in GRADE_FOUR_MIDDLE_PROFILES]
 first_grade=[item for item in classes if item["course_order"]==1];first_developed=sum(item["editorial_status"]=="desarrollada" for item in first_grade);first_integrated=sum(item["editorial_status"]=="integrada" for item in first_grade);first_drafts=sum(item["editorial_status"]=="borrador" for item in first_grade)
 second_grade=[item for item in classes if item["course_order"]==2];second_developed=sum(item["editorial_status"]=="desarrollada" for item in second_grade);second_integrated=sum(item["editorial_status"]=="integrada" for item in second_grade);second_sequenced=sum(item["editorial_status"]=="secuenciada" for item in second_grade)
 third_grade=[item for item in classes if item["course_order"]==3];third_developed=sum(item["editorial_status"]=="desarrollada" for item in third_grade);third_integrated=sum(item["editorial_status"]=="integrada" for item in third_grade);third_pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in third_grade)
 fourth_grade=[item for item in classes if item["course_order"]==4];fourth_pending=sum(item["editorial_status"] in {"secuenciada","borrador"} for item in fourth_grade)
 total_developed=sum(item["editorial_status"]=="desarrollada" for item in classes);total_integrated=sum(item["editorial_status"]=="integrada" for item in classes)
 pending_through_four_middle=sum(item["editorial_status"] in {"secuenciada","borrador"} and item["course_order"]<=12 for item in classes)
 first_cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['classes']} propuestas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_ONE_SUBJECT_PROFILES[item['slug']]['purpose'])}</p><a href="docs/1-basico/{item['slug']}.html">Leer guía de 1° completa →</a></article>''' for item in first_subjects)
 second_cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['classes']} propuestas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_TWO_SUBJECT_PROFILES[item['slug']]['purpose'])}</p><a href="docs/2-basico/{item['slug']}.html">Leer guía de 2° completa →</a></article>''' for item in second_subjects)
 third_cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['classes']} propuestas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_THREE_SUBJECT_PROFILES[item['slug']]['purpose'])}</p><a href="docs/3-basico/{item['slug']}.html">Leer guía de 3° completa →</a></article>''' for item in third_subjects)
 fourth_cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['classes']} propuestas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_FOUR_SUBJECT_PROFILES[item['slug']]['purpose'])}</p><a href="docs/4-basico/{item['slug']}.html">Leer guía de 4° completa →</a></article>''' for item in fourth_subjects)
 fifth_cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['classes']} propuestas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_FIVE_SUBJECT_PROFILES[item['slug']]['purpose'])}</p><a href="docs/5-basico/{item['slug']}.html">Leer guía de 5° completa →</a></article>''' for item in fifth_subjects)
 sixth_cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['classes']} propuestas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_SIX_SUBJECT_PROFILES[item['slug']]['purpose'])}</p><a href="docs/6-basico/{item['slug']}.html">Leer guía de 6° completa →</a></article>''' for item in sixth_subjects)
 seventh_cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas · {item['integrated']} integradas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_SEVEN_CORE_PROFILES[item['slug']]['purpose'])}</p><a href="docs/7-basico/{item['slug']}.html">Leer guía de 7° completa →</a></article>''' for item in seventh_subjects)
 eighth_cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas · {item['integrated']} integradas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_EIGHT_CORE_PROFILES[item['slug']]['purpose'])}</p><a href="docs/8-basico/{item['slug']}.html">Leer guía de 8° →</a></article>''' for item in eighth_subjects)
 one_middle_cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas · {item['integrated']} integradas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_ONE_MIDDLE_CORE_PROFILES[item['slug']]['purpose'])}</p><a href="docs/1-medio/{item['slug']}.html">Leer guía de 1° medio →</a></article>''' for item in one_middle_subjects)
 two_middle_cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas · {item['integrated']} integradas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_TWO_MIDDLE_CORE_PROFILES[item['slug']]['purpose'])}</p><a href="docs/2-medio/{item['slug']}.html">Leer guía de 2° medio →</a></article>''' for item in two_middle_subjects)
 three_middle_cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_THREE_MIDDLE_CORE_PROFILES[item['slug']]['purpose'])}</p><a href="docs/3-medio/{item['slug']}.html">Leer guía de 3° medio →</a></article>''' for item in three_middle_subjects)
 four_middle_cards="".join(f'''<article class="level-card"><div><span>{item['oa']} OA</span><span>{item['developed']} desarrolladas</span></div><h2>{html.escape(item['name'])}</h2><p>{html.escape(GRADE_FOUR_MIDDLE_PROFILES[item['slug']]['purpose'])}</p><a href="docs/4-medio/{item['slug']}.html">Leer guía de 4° medio →</a></article>''' for item in four_middle_subjects)
 levels=[]
 for order in range(1,13):
  level_classes=[item for item in classes if item["course_order"]==order]
  level_oas={item["oa_code"] for item in level_classes}
  developed=sum(item["editorial_status"]=="desarrollada" for item in level_classes)
  levels.append({"name":level_classes[0]["course"],"oa":len(level_oas),"classes":len(level_classes),"developed":developed})
 coverage_cards="".join(f'''<a class="coverage-card" href="index.html?nivel={quote(item['name'])}#explorar"><span>{html.escape(item['name'])}</span><strong>{item['classes']:,}</strong><small>{item['oa']} OA · {item['developed']} desarrolladas</small></a>'''.replace(",",".") for item in levels)
 return f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#071c2c"><meta name="description" content="Documentación completa de 1° a 8° básico, con 12 denominaciones curriculares por nivel cuando corresponden al inventario."><link rel="canonical" href="https://vladimiracunadev-create.github.io/chilean-school-learning-path/documentacion.html"><link rel="icon" href="icon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><title>Documentación | Trayectoria Escolar Chile</title></head>
<body class="level-page"><a class="skip-link" href="#documentacion">Saltar a documentación</a><header class="detail-topbar"><a class="brand" href="index.html"><span class="brand-mark">TE</span><span>Trayectoria Escolar<small>Currículum chileno abierto</small></span></a><a class="back-link" href="index.html">← Volver al portal</a></header>
<main id="documentacion" class="level-shell"><header class="level-hero docs-hero"><div><p class="eyebrow">Documentación pedagógica</p><h1>Del currículum a decisiones de aula.</h1><p>Una arquitectura para recorrer los doce niveles completos hasta 4° medio, con estado editorial verificable.</p><div class="hero-actions"><a class="button primary" href="docs/4-medio/index.html">Abrir 4° medio</a><a class="button dark-text" href="levels/4-medio.html">Ver mapa de 4° medio</a></div></div><aside><span>Documentación por nivel</span><strong>149 guías de asignatura</strong><small>doce niveles completos · 17 guías de 4° medio</small></aside></header>
<section class="level-metrics"><div><strong>{total_developed}</strong><span>clases desarrolladas en el catálogo</span></div><div><strong>{total_integrated}</strong><span>experiencias integradas</span></div><div><strong>{pending_through_four_middle}</strong><span>pendientes desde 1° básico a 4° medio</span></div><div><strong>0</strong><span>revisiones humanas registradas</span></div></section>
<section class="level-intro"><div><p class="eyebrow">Empieza según tu tarea</p><h2>Documentos que responden preguntas concretas</h2></div><p><strong>Syllabus:</strong> alcance y planificación. <strong>Guía docente:</strong> conducción de clases. <strong>Rúbrica:</strong> evidencia y decisiones. <strong>FAQ:</strong> límites y uso. <strong>Familias:</strong> acompañamiento. <strong>Revisión:</strong> cómo validar responsablemente.</p></section>
<section class="doc-link-grid"><a href="docs/que-es-un-oa.html"><span>01</span><strong>¿Qué es un OA?</strong><small>Explicación simple con ejemplo</small></a><a href="docs/syllabus.html"><span>02</span><strong>Syllabus</strong><small>Programa, ritmo y planificación</small></a><a href="docs/teaching-guide.html"><span>03</span><strong>Guía docente</strong><small>Preparar, enseñar y adaptar</small></a><a href="docs/roles-docentes.html"><span>04</span><strong>Roles en el aula</strong><small>Responsabilidades y coordinación</small></a><a href="docs/dificultades-en-el-aula.html"><span>05</span><strong>Dificultades y acciones</strong><small>Observar, actuar y comprobar</small></a><a href="docs/rubrica-evaluacion.html"><span>06</span><strong>Rúbrica</strong><small>Observar y decidir</small></a><a href="docs/cobertura.html"><span>07</span><strong>Cobertura total</strong><small>12 niveles con acceso directo</small></a><a href="docs/formatos.html"><span>08</span><strong>Markdown + HTML</strong><small>Cómo se publica cada clase</small></a><a href="docs/licencias.html"><span>09</span><strong>Licencias</strong><small>Qué puede reutilizarse</small></a><a href="docs/faq.html"><span>10</span><strong>Preguntas frecuentes</strong><small>Uso, alcance y límites</small></a><a href="docs/pilotaje-aula.html"><span>11</span><strong>Pilotaje de aula</strong><small>Aplicar, observar y registrar sin datos personales</small></a><a href="competencias/"><span>12</span><strong>Competencias</strong><small>Qué existe, qué falta y cómo se conecta</small></a><a href="competencias/marcos-evaluacion.html"><span>13</span><strong>PAES y otros marcos</strong><small>Qué se implementó y qué no significa</small></a><a href="competencias/banco-tareas.html"><span>14</span><strong>Banco de tareas</strong><small>Estímulos, soluciones, rúbricas y OA</small></a></section>
<section class="oa-explainer"><div><p class="eyebrow">Sin siglas misteriosas</p><h2>OA significa Objetivo de Aprendizaje.</h2></div><div><p>Describe lo que una o un estudiante debe llegar a comprender o hacer. <strong>No es una clase, una tarea ni una actividad.</strong></p><p><code>MA01 OA 01</code> se lee: Matemática · 1° básico · Objetivo de Aprendizaje número 1. El proyecto convierte cada OA en una secuencia de clases con evidencia.</p></div></section>
<section class="level-intro"><div><p class="eyebrow">Cobertura navegable</p><h2>Los 12 niveles, sin callejones sin salida</h2></div><p>Cada tarjeta abre el explorador ya filtrado. Las cifras separan cobertura curricular, desarrollo editorial y revisión humana.</p></section><section class="coverage-grid">{coverage_cards}</section>
<section class="level-intro"><div><p class="eyebrow">Primer nivel completo</p><h2>1° básico, asignatura por asignatura</h2></div><p>Once guías con propósito, resultados, prerrequisitos, método, anatomía, recorrido OA por OA, evaluación, recuperación y acceso.</p></section><div class="hero-actions"><a class="button primary" href="levels/1-basico.html">Abrir mapa de 1°</a><a class="button dark-text" href="docs/1-basico/index.html">Ver índice documental</a></div><section class="level-grid">{first_cards}</section>
<section class="level-intro"><div><p class="eyebrow">Segundo nivel completo</p><h2>2° básico, asignatura por asignatura</h2></div><p>El mismo contrato documental de 1°, más continuidad explícita con el nivel anterior: propósito, resultados, prerrequisitos, método, anatomía, recorrido OA por OA, evaluación, recuperación y acceso.</p></section><div class="hero-actions"><a class="button primary" href="levels/2-basico.html">Abrir mapa de 2°</a><a class="button dark-text" href="docs/2-basico/index.html">Ver índice documental</a></div><section class="level-grid">{second_cards}</section>
<section class="level-intro"><div><p class="eyebrow">Tercer nivel completo</p><h2>3° básico, asignatura por asignatura</h2></div><p>Once guías con continuidad explícita desde 2°, progresión disciplinar, recorrido OA por OA, evidencia, dificultades, acceso y resguardos específicos.</p></section><div class="hero-actions"><a class="button primary" href="levels/3-basico.html">Abrir mapa de 3°</a><a class="button dark-text" href="docs/3-basico/index.html">Ver índice documental</a></div><section class="level-grid">{third_cards}</section>
<section class="level-intro"><div><p class="eyebrow">Cuarto nivel completo</p><h2>4° básico, asignatura por asignatura</h2></div><p>Once guías con continuidad explícita desde 3°, progresión propia de cada disciplina, recorrido OA por OA, evidencia, dificultades, acceso y resguardos específicos.</p></section><div class="hero-actions"><a class="button primary" href="levels/4-basico.html">Abrir mapa de 4°</a><a class="button dark-text" href="docs/4-basico/index.html">Ver índice documental</a></div><section class="level-grid">{fourth_cards}</section>
<section class="level-intro"><div><p class="eyebrow">Quinto nivel completo</p><h2>5° básico, asignatura por asignatura</h2></div><p>Doce guías con continuidad explícita desde 4°, dos denominaciones oficiales de Inglés cuando corresponden al inventario, progresión disciplinar, evidencia, dificultades, acceso y resguardos específicos.</p></section><div class="hero-actions"><a class="button primary" href="levels/5-basico.html">Abrir mapa de 5°</a><a class="button dark-text" href="docs/5-basico/index.html">Ver índice documental</a></div><section class="level-grid">{fifth_cards}</section>
<section class="level-intro"><div><p class="eyebrow">Sexto nivel completo</p><h2>6° básico, asignatura por asignatura</h2></div><p>Doce guías con continuidad explícita desde 5°, progresión disciplinar propia, recorrido por 301 OA, evidencia, dificultades, acceso y resguardos específicos.</p></section><div class="hero-actions"><a class="button primary" href="levels/6-basico.html">Abrir mapa de 6°</a><a class="button dark-text" href="docs/6-basico/index.html">Ver índice documental</a></div><section class="level-grid">{sixth_cards}</section>
<section class="level-intro"><div><p class="eyebrow">Séptimo nivel completo</p><h2>Doce denominaciones desarrolladas en 7° básico.</h2></div><p>Todos los objetivos de contenido cuentan con recorridos específicos, continuidad desde 6°, insumos concretos, progresión OA por OA y resguardos disciplinares. Habilidades y actitudes se integran sin duplicar clases.</p></section><div class="hero-actions"><a class="button primary" href="docs/7-basico/index.html">Abrir índice de 7°</a><a class="button dark-text" href="levels/7-basico.html">Ver mapa de 7°</a></div><section class="level-grid">{seventh_cards}</section>
<section class="level-intro"><div><p class="eyebrow">Octavo nivel completo</p><h2>Doce denominaciones desarrolladas en 8° básico.</h2></div><p>Todos los objetivos de contenido cuentan con recorridos específicos, continuidad desde 7°, recursos concretos, evidencias individuales y resguardos disciplinares. Habilidades y actitudes se integran sin duplicar clases.</p></section><div class="hero-actions"><a class="button primary" href="docs/8-basico/index.html">Abrir índice de 8°</a><a class="button dark-text" href="levels/8-basico.html">Ver mapa de 8°</a></div><section class="level-grid">{eighth_cards}</section>
<section class="level-intro"><div><p class="eyebrow">Primer nivel de Enseñanza Media completo</p><h2>Once denominaciones desarrolladas en 1° medio.</h2></div><p>Todos los objetivos de contenido cuentan con recorridos específicos, continuidad desde 8°, recursos concretos, evaluación formativa y resguardos disciplinares. Habilidades y actitudes se integran sin duplicar clases.</p></section><div class="hero-actions"><a class="button primary" href="docs/1-medio/index.html">Abrir índice de 1° medio</a><a class="button dark-text" href="levels/1-medio.html">Ver mapa de 1° medio</a></div><section class="level-grid">{one_middle_cards}</section>
<section class="level-intro"><div><p class="eyebrow">Segundo nivel de Enseñanza Media completo</p><h2>Once denominaciones desarrolladas en 2° medio.</h2></div><p>Todos los objetivos de contenido cuentan con recorridos específicos, continuidad desde 1° medio, recursos concretos, evaluación formativa y resguardos disciplinares. Habilidades y actitudes se integran sin duplicar clases.</p></section><div class="hero-actions"><a class="button primary" href="docs/2-medio/index.html">Abrir índice de 2° medio</a><a class="button dark-text" href="levels/2-medio.html">Ver mapa de 2° medio</a></div><section class="level-grid">{two_middle_cards}</section>
<section class="level-intro"><div><p class="eyebrow">Tercer nivel de Enseñanza Media completo</p><h2>Dieciocho denominaciones desarrolladas en 3° medio.</h2></div><p>Los 98 OA del nivel cuentan con 495 clases específicas, continuidad desde 2° medio, fuentes oficiales, recursos concretos, evaluación formativa y resguardos disciplinares.</p></section><div class="hero-actions"><a class="button primary" href="docs/3-medio/index.html">Abrir índice de 3° medio</a><a class="button dark-text" href="levels/3-medio.html">Ver mapa de 3° medio</a></div><section class="level-grid">{three_middle_cards}</section>
<section class="level-intro"><div><p class="eyebrow">Cuarto nivel de Enseñanza Media completo</p><h2>Diecisiete denominaciones desarrolladas en 4° medio.</h2></div><p>Los 91 OA del nivel cuentan con 466 clases específicas, continuidad desde 3° medio, fuentes oficiales, autonomía de egreso, evaluación formativa y resguardos disciplinares.</p></section><div class="hero-actions"><a class="button primary" href="docs/4-medio/index.html">Abrir índice de 4° medio</a><a class="button dark-text" href="levels/4-medio.html">Ver mapa de 4° medio</a></div><section class="level-grid">{four_middle_cards}</section>
<section class="level-contract"><div><p class="eyebrow">Lectura honesta</p><h2>Profundidad documental sin inflar el estado.</h2></div><ol><li><strong>Desarrollada</strong><span>La clase contiene decisiones pedagógicas y disciplinares específicas.</span></li><li><strong>Publicada</strong><span>Está disponible y navegable en Markdown y HTML.</span></li><li><strong>Revisada</strong><span>Solo cuando una persona competente registra evidencia de revisión.</span></li><li><strong>Adaptable</strong><span>El docente conserva el OA y ajusta la vía de acceso según su curso.</span></li></ol></section></main>
<footer class="site-footer"><div><strong>Trayectoria Escolar Chile</strong><span>Documentación abierta y trazable · MIT + CC BY-NC-SA 4.0</span></div><div><a class="star-link" href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/stargazers">⭐ Dar una estrella</a><a href="index.html">Portal</a><a href="docs/licencias.html">Licencias</a></div></footer></body></html>'''

def developed_lesson_html(item,index,code,lesson,status):
 def esc(value): return html.escape(str(value), quote=True)
 is_developed=status=="desarrollada"
 status_label="Desarrollada" if is_developed else "Integración transversal" if status=="integrada" else "Borrador estructurado"
 status_class="developed" if is_developed else "integrated" if status=="integrada" else ""
 criteria="".join(f"<li>{esc(value)}</li>" for value in lesson["criteria"])
 complementary="".join(f"<li>{esc(value)}</li>" for value in lesson.get("complementary", []))
 difficulties="".join(f"<tr><td>{esc(row['signal'])}</td><td>{esc(row['action'])}</td><td>{esc(row['check'])}</td></tr>" for row in lesson.get("difficulty_actions", []))
 transversal="".join(f"<li><strong>{esc(row['type'])} · {esc(row['code'])}:</strong> {esc(row['application'])}</li>" for row in lesson.get("transversal", []))
 transversal_types={row["type"] for row in lesson.get("transversal", [])}
 transversal_heading="Habilidad y actitud en esta clase" if len(transversal_types)>1 else "Actitud transversal en esta clase"
 transversal_panel=f'<section class="transversal-panel"><p class="eyebrow">Integración curricular</p><h3>{transversal_heading}</h3><ul>{transversal}</ul></section>' if transversal else ""
 teacher_checks="".join(f"<li>{esc(value)}</li>" for value in lesson.get("teacher_checklist", []))
 assessment_rows="".join(f"<tr><td><strong>{esc(row['level'])}</strong></td><td>{esc(row['descriptor'])}</td></tr>" for row in lesson.get("assessment_levels", []))
 timing_rows="".join(f"<tr><td>{esc(row['minutes'])} min</td><td>{esc(row['action'])}</td></tr>" for row in lesson.get("timing_45", []))
 app_items="".join(
  f'<li><h4><a href="{esc(app["url"])}" rel="noopener">{esc(app["name"])}</a></h4><p><strong>{esc(app["audience"].capitalize())}.</strong> {esc(app["purpose"])}</p><p><strong>Condiciones de uso:</strong> {esc(app["conditions"])}</p><p><strong>Alternativa sin app:</strong> {esc(app["alternative"])}</p><a href="{esc(app["repository_url"])}" rel="noopener">Repositorio y documentación técnica</a></li>'
  for app in lesson.get("learning_support_apps", [])
 )
 app_panel=(f'<section class="learning-app-panel"><p class="eyebrow">Recurso opcional</p><h3>App de apoyo del aprendizaje</h3><p>La evidencia se obtiene en la actividad del OA, no en el avance dentro de la aplicación.</p><ul>{app_items}</ul></section>' if app_items else "")
 quality_pack=(f'<section class="quality-pack"><p class="eyebrow">Insumo concreto y consigna</p><h3>Recurso listo para usar</h3><p>{esc(lesson["concrete_resource"])}</p><h3>Consigna exacta</h3><p>{esc(lesson["exact_prompt"])}</p><h3>Referencia para modelar y corregir</h3><p>{esc(lesson["response_reference"])}</p><h3>Preparación docente</h3><ul>{teacher_checks}</ul></section>' if is_developed else "")
 quality_tables=(f'<section class="quality-tables"><h3>Pauta de evaluación de cuatro niveles</h3><div class="table-scroll"><table><thead><tr><th>Nivel</th><th>Descriptor observable</th></tr></thead><tbody>{assessment_rows}</tbody></table></div><h3>Distribución de 45 minutos</h3><div class="table-scroll"><table><thead><tr><th>Tiempo</th><th>Acción preservada</th></tr></thead><tbody>{timing_rows}</tbody></table></div></section>' if is_developed else "")
 return f'''<article class="lesson {'lesson-developed' if is_developed else 'lesson-draft'}" id="{esc(code.lower())}">
<header><span class="lesson-number">{index:02d}</span><div><p>Clase {index} de {len(item['phases'])}</p><h2>{esc(lesson['title'])}</h2></div><span class="status-badge {status_class}">{status_label}</span></header>
<p class="lesson-focus"><strong>Propósito docente:</strong> {esc(lesson['purpose'])}</p><p class="student-goal"><strong>Meta para estudiantes:</strong> {esc(lesson['goal'])}</p>
<div class="lesson-grid"><section><h3>Inicio · 10 min</h3><p>{esc(lesson['opening'])}</p></section><section><h3>Modelado · 20 min</h3><p>{esc(lesson['model'])}</p></section><section><h3>Práctica guiada · 25 min</h3><p>{esc(lesson['guided'])}</p></section><section><h3>Desempeño individual · 25 min</h3><p>{esc(lesson['independent'])}</p></section></div>
<div class="material-callout"><h3>Materiales y preparación</h3><p>{esc(lesson['materials'])}</p></div>
{app_panel}{quality_pack}
<div class="support-grid"><p><strong>Apoyo:</strong> {esc(lesson['support'])}</p><p><strong>Profundización:</strong> {esc(lesson['extension'])}</p></div>
<div class="assessment-grid"><section><h3>Ticket de salida · 10 min</h3><p>{esc(lesson['ticket'])}</p><p><strong>Evidencia:</strong> {esc(lesson['evidence'])}</p></section><section><h3>Criterios observables</h3><ul>{criteria}</ul></section></div>
{quality_tables}
<p class="next-step"><strong>Decisión posterior:</strong> {esc(lesson['next_step'])}</p><p class="short-version"><strong>Si dispone de 45 minutos:</strong> {esc(lesson['short_version'])}</p>
<div class="extension-grid"><section><p class="eyebrow">Consolidación</p><h3>Tarea breve y flexible</h3><p>{esc(lesson.get('home_task','Consolida el aprendizaje con una evidencia breve sin internet ni materiales comprados.'))}</p></section><section><p class="eyebrow">Banco opcional</p><h3>Actividades complementarias</h3><ul>{complementary}</ul></section></div>
<section class="difficulty-panel"><p class="eyebrow">Respuesta durante la clase</p><h3>Control de dificultades con acciones</h3><div class="table-scroll"><table><thead><tr><th>Dificultad observable</th><th>Acción inmediata</th><th>Comprobación</th></tr></thead><tbody>{difficulties}</tbody></table></div><p class="role-note"><strong>Coordinación profesional:</strong> {esc(lesson.get('specialist_coordination','El docente responsable conserva la conducción del OA y acuerda barrera, acción y evidencia con los profesionales de apoyo.'))}</p></section>
{transversal_panel}</article>'''

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
 content=item.get("developed") or item.get("integration") or item.get("draft")
 content_status="desarrollada" if item.get("developed") else "integrada" if item.get("integration") else "borrador"
 sessions=[]
 for index,(code,(title,focus)) in enumerate(zip(item["codes"],item["phases"]),1):
  if content:
   sessions.append(developed_lesson_html(item,index,code,content["lessons"][index-1],content_status))
   continue
  sessions.append(f'''<article class="lesson" id="{esc(code.lower())}">
<header><span class="lesson-number">{index:02d}</span><div><p>Clase {index} de {len(item['phases'])}</p><h2>{esc(title)}</h2></div><span class="status-badge">Secuenciada</span></header>
<p class="lesson-focus"><strong>Meta:</strong> {esc(focus.capitalize())} para avanzar en «{esc(item['topic'].lower())}» y demostrarlo mediante {esc(product)}.</p>
<div class="lesson-grid"><section><h3>Inicio · 10 min</h3><p>Presenta una situación vinculada a <strong>{esc(item['topic'].lower())}</strong> y recoge una respuesta inicial de todo el curso.</p></section><section><h3>Modelado · 20 min</h3><p>Modela el OA usando {esc(vocab)}. Contrasta un ejemplo logrado con este error: {esc(errors)}.</p></section><section><h3>Práctica · 50 min</h3><p>Construyen juntos y luego individualmente {esc(product)}. Cada estudiante explica una decisión y revisa su resultado.</p></section><section><h3>Cierre · 10 min</h3><p>Ticket: decisión, evidencia y corrección del error previsible. Decide si avanzar, reagrupar o reenseñar.</p></section></div>
<div class="support-grid"><p><strong>Apoyo:</strong> anticipa {esc(vocab)}, muestra un ejemplo resuelto y admite distintas formas de respuesta sin reducir el OA.</p><p><strong>Profundización:</strong> compara otra estrategia, examina un caso límite y transfiere el aprendizaje a una situación nueva.</p></div>
<p class="success-criteria"><strong>Criterios de éxito:</strong> responde al OA, usa evidencia pertinente, explica una decisión y revisa el resultado.</p>
</article>''')
 editorial="Desarrollada" if item.get("developed") else "Integración transversal" if item.get("integration") else "Borrador estructurado" if item.get("draft") else "Secuenciada"
 editorial_note="Contenido disciplinar específico; pendiente de revisión humana." if item.get("developed") else "Habilidad o actitud incorporada dentro de las 83 clases de contenido; no se cuenta como clase independiente." if item.get("integration") else "Plantilla navegable pendiente de desarrollo disciplinar específico." if item.get("draft") else "No equivale aún a una clase disciplinar revisada."
 alignment_html=official_alignment_html(item)
 if alignment_html:alignment_html+="\n"
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
<section class="oa-panel" aria-labelledby="oa-title"><p class="eyebrow">Objetivo oficial</p><h2 id="oa-title">Qué se espera aprender</h2><p class="oa-help"><strong>OA significa Objetivo de Aprendizaje:</strong> el resultado que debe alcanzar el estudiante. No es una actividad ni una clase; por eso este OA se desarrolla en una secuencia.</p><blockquote>{esc(item['oa_text'])}</blockquote><p class="rights-note"><strong>Derechos y procedencia:</strong> el código y la redacción del OA proceden de Currículum Nacional (MINEDUC), se muestran con enlace y fecha de consulta y no se declaran obra del proyecto ni se relicencian bajo CC BY-NC-SA 4.0.</p><div class="oa-meta"><span>{len(item['phases'])} clases</span><span>Bloques adaptables a 45 o 90 min</span><span>{esc(item['coverage'])}</span></div></section>
{alignment_html}<section class="content-section"><div class="section-heading"><div><p class="eyebrow">Secuencia propuesta</p><h2>De la activación a la evidencia</h2></div><p>La dosificación responde a la amplitud y demanda cognitiva del OA. El docente ajusta el ritmo según la evidencia.</p></div>{''.join(sessions)}</section>
<section class="sources-panel"><div><p class="eyebrow">Trazabilidad HTML</p><h2>Fuente oficial y navegación web</h2><p>Esta página conserva el OA oficial, la fecha de consulta y la secuencia completa sin abandonar el árbol de GitHub Pages.</p></div><ul><li><a href="../../../docs/formatos.html">Cómo se publican los formatos</a><span>Separación entre navegación HTML y navegación Markdown</span></li>{reading_items}<li><a href="{esc(item['source_url'])}" rel="noopener">Ficha oficial del OA</a><span>Currículum Nacional · consulta {esc(item['verified_at'])}</span></li></ul></section>
<nav class="sequence-nav" aria-label="Objetivos anterior y siguiente">{nav_link(previous_item,'Objetivo anterior')}{nav_link(next_item,'Objetivo siguiente')}</nav></main>
<footer class="site-footer"><div><strong>Proyecto educativo independiente</strong><span>Elaboración pedagógica original: CC BY-NC-SA 4.0 · texto oficial MINEDUC: derechos de su titular</span></div><div><a class="star-link" href="https://github.com/vladimiracunadev-create/chilean-school-learning-path/stargazers">⭐ Dar una estrella</a><a href="../../../docs/licensing.html">Licencias</a></div></footer></body></html>'''
def changelog_updates(limit=3):
 text=(ROOT/"CHANGELOG.md").read_text(encoding="utf-8")
 updates=[];current=None
 for line in text.splitlines():
  match=re.match(r"^## (\d{4}-\d{2}-\d{2}) · (.+)$",line)
  if match:
   if current:updates.append(current)
   if len(updates)>=limit:break
   current={"date":match.group(1),"title":match.group(2),"summary":[]}
  elif current and line.startswith("- "):
   current["summary"].append(line[2:].strip())
 if current and len(updates)<limit:updates.append(current)
 if not updates or not updates[0]["summary"]:
  raise RuntimeError("CHANGELOG.md debe comenzar con una novedad fechada y al menos un resumen.")
 return {"schema_version":1,"source":"CHANGELOG.md","latest_date":updates[0]["date"],"updates":updates}
def main():
 defer_generic_docs=os.environ.get("DEFER_GENERIC_DOCS")=="1" or (ROOT/".defer-generic-docs").is_file()
 snap=json.loads(SNAPSHOT.read_text(encoding="utf-8"));developed=json.loads(DEVELOPED.read_text(encoding="utf-8"))["objectives"];objs=[];classes=[];num=1
 for r in sorted(snap["records"],key=lambda x:(x["course_order"],x["subject"],x["subject_slug"])):
  for oa in r["objectives"]:
   reads=oa.get("readings",[]);phases=dose(oa["description"],r["subject_slug"],reads);codes=[f"CL-{num+i:05d}" for i in range(len(phases))];path=f"curriculum/{r['course_slug']}/{r['subject_slug']}/{slugify(oa['code'])}.md"
   developed_content=build_remaining_sequence(oa["code"]) or build_sha_sequence(oa["code"]) or build_grade_two_math_sequence(oa["code"]) or build_grade_two_lsh_sequence(oa["code"]) or build_grade_two_amp_sequence(oa["code"]) or build_grade_two_remaining_sequence(oa["code"]) or build_grade_three_ml_sequence(oa["code"]) or build_grade_three_sh_sequence(oa["code"]) or build_grade_three_apei_sequence(oa["code"]) or build_grade_three_mot_sequence(oa["code"]) or build_grade_four_math_sequence(oa["code"]) or build_grade_four_remaining_sequence(oa["code"]) or build_grade_five_core_sequence(oa["code"]) or build_grade_five_remaining_sequence(oa["code"]) or build_grade_six_math_sequence(oa["code"]) or build_grade_six_remaining_sequence(oa["code"]) or build_grade_seven_core_sequence(oa["code"]) or build_grade_seven_next_five_sequence(oa["code"]) or build_grade_seven_remaining_sequence(oa["code"]) or build_grade_eight_core_sequence(oa["code"]) or build_grade_eight_next_four_sequence(oa["code"]) or build_grade_eight_remaining_sequence(oa["code"]) or build_grade_one_middle_core_sequence(oa["code"]) or build_grade_one_middle_next_four_sequence(oa["code"]) or build_grade_one_middle_remaining_sequence(oa["code"]) or build_grade_two_middle_core_sequence(oa["code"]) or build_grade_two_middle_next_four_sequence(oa["code"]) or build_grade_two_middle_remaining_sequence(oa["code"]) or build_grade_three_middle_core_sequence(oa["code"]) or (build_grade_three_middle_remaining_sequence(oa["code"]) if r["course_order"]==11 else None) or (build_grade_four_middle_sequence(oa["code"]) if r["course_order"]==12 else None) or developed.get(oa["code"]) or build_math_sequence(oa["code"]) or build_language_sequence(oa["code"])
   if oa["code"]=="MA03 OA 11":developed_content=complete_pilot_sequence(developed_content)
   if oa["code"]=="HI03 OA 05":developed_content=complete_history_pilot(developed_content)
   item={"topic":(developed_content or {}).get("topic",topic_from(oa["description"])),"course":r["course"],"course_slug":r["course_slug"],"course_order":r["course_order"],"subject":r["subject"],"subject_slug":r["subject_slug"],"axis":oa["axis"],"oa_code":oa["code"],"oa_text":oa["description"],"coverage":cov(r["subject_slug"],r["course_order"]),"source_url":oa["url"],"subject_url":r["subject_url"],"verified_at":snap["verified_at"],"readings":reads,"path":path,"codes":codes,"phases":phases,"developed":developed_content}
   integrated_attitude_subjects={"matematica","lenguaje-comunicacion","ciencias-naturales","historia-geografia-ciencias-sociales","artes-visuales","musica","educacion-fisica-salud","tecnologia","ingles-propuesta","lengua-cultura-pueblos-originarios-ancestrales"}
   transversal_integration=r["course_order"]==1 and ((r["subject_slug"] in {"matematica","ciencias-naturales","historia-geografia-ciencias-sociales"} and oa["code"].startswith("de Habilidad")) or (r["subject_slug"] in integrated_attitude_subjects and oa["code"].startswith("de Actitud")))
   if r["course_order"]==1:
    generated=build_grade_one_lessons(item)
    if transversal_integration:item["integration"]=generated
    elif not item["developed"]:item["draft"]=generated
    else:item["developed"]["lessons"]=[base | current for base,current in zip(generated["lessons"],item["developed"]["lessons"])]
   if r["course_order"]==2 and r["subject_slug"]=="matematica" and oa["code"].startswith(("de Habilidad MA02 ","de Actitud MA02 ")):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_two_math_integration(item)
   if r["course_order"]==2 and r["subject_slug"] in {"lenguaje-comunicacion","ciencias-naturales","historia-geografia-ciencias-sociales"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_two_lsh_integration(item)
   if r["course_order"]==2 and r["subject_slug"] in {"artes-visuales","musica","educacion-fisica-salud"} and oa["code"].startswith("de Actitud "):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_two_amp_integration(item)
   if r["course_order"]==2 and r["subject_slug"] in {"tecnologia","ingles-propuesta","lengua-cultura-pueblos-originarios-ancestrales"} and oa["code"].startswith("de Actitud "):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_two_remaining_integration(item)
   if r["course_order"]==3 and r["subject_slug"] in {"matematica","lenguaje-comunicacion"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_three_ml_integration(item)
   if r["course_order"]==3 and r["subject_slug"] in {"ciencias-naturales","historia-geografia-ciencias-sociales"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_three_sh_integration(item)
   if r["course_order"]==3 and r["subject_slug"] in {"artes-visuales","educacion-fisica-salud","ingles-propuesta","lengua-cultura-pueblos-originarios-ancestrales"} and oa["code"].startswith("de Actitud "):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_three_apei_integration(item)
   if r["course_order"]==3 and r["subject_slug"] in {"musica","tecnologia"} and oa["code"].startswith("de Actitud "):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_three_mot_integration(item)
   if r["course_order"]==4 and r["subject_slug"]=="matematica" and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_four_math_integration(item)
   if r["course_order"]==4 and r["subject_slug"]!="matematica" and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_four_remaining_integration(item)
   if r["course_order"]==5 and r["subject_slug"] in {"matematica","lenguaje-comunicacion","ciencias-naturales"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_five_core_integration(item)
   if r["course_order"]==5 and r["subject_slug"] not in {"matematica","lenguaje-comunicacion","ciencias-naturales","orientacion","lengua-cultura-pueblos-originarios-ancestrales"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_five_remaining_integration(item)
   if r["course_order"]==6 and r["subject_slug"]=="matematica" and oa["code"].startswith(("de Habilidad MA06 ","de Actitud MA06 ")):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_six_math_integration(item)
   if r["course_order"]==6 and r["subject_slug"]!="matematica" and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_six_remaining_integration(item)
   if r["course_order"]==7 and r["subject_slug"] in {"matematica","lengua-literatura"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_seven_core_integration(item)
   if r["course_order"]==7 and r["subject_slug"] in {"ciencias-naturales","historia-geografia-ciencias-sociales","ingles","educacion-fisica-salud","artes-visuales"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["developed"]=None
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_seven_next_five_integration(item)
   if r["course_order"]==7 and r["subject_slug"] in {"ingles-propuesta","musica","tecnologia"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["developed"]=None
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_seven_remaining_integration(item)
   if r["course_order"]==8 and r["subject_slug"] in {"matematica","lengua-literatura"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["developed"]=None
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_eight_core_integration(item)
   if r["course_order"]==8 and r["subject_slug"] in {"ciencias-naturales","historia-geografia-ciencias-sociales","artes-visuales","musica"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["developed"]=None
    item["integration"]=build_grade_eight_next_four_integration(item)
   if r["course_order"]==8 and r["subject_slug"] in {"educacion-fisica-salud","ingles","tecnologia"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["developed"]=None
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_eight_remaining_integration(item)
   if r["course_order"]==9 and r["subject_slug"] in {"matematica","lengua-literatura"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["developed"]=None
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_one_middle_core_integration(item)
   if r["course_order"]==9 and r["subject_slug"] in {"ciencias-naturales","historia-geografia-ciencias-sociales","ingles"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["developed"]=None
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_one_middle_next_four_integration(item)
   if r["course_order"]==9 and r["subject_slug"] in {"artes-visuales","musica","educacion-fisica-salud","tecnologia"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["developed"]=None
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_one_middle_remaining_integration(item)
   if r["course_order"]==10 and r["subject_slug"] in {"matematica","lengua-literatura"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["developed"]=None
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_two_middle_core_integration(item)
   if r["course_order"]==10 and r["subject_slug"] in {"ciencias-naturales","historia-geografia-ciencias-sociales","ingles"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["developed"]=None
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_two_middle_next_four_integration(item)
   if r["course_order"]==10 and r["subject_slug"] in {"artes-visuales","musica","educacion-fisica-salud","tecnologia"} and oa["code"].startswith(("de Habilidad ","de Actitud ")):
    item["developed"]=None
    item["topic"]=oa["description"].split("Unidad de Currículum",1)[0].strip().rstrip(".")
    item["integration"]=build_grade_two_middle_remaining_integration(item)
   if item["developed"] and r["course_order"]==1 and r["subject_slug"]=="matematica" and oa["code"].startswith("MA01 OA "):
    oa_number=int(oa["code"].rsplit(" ",1)[-1])
    for lesson_index,lesson in enumerate(item["developed"]["lessons"]):
     lesson["transversal"]=transversal_links(oa_number,lesson_index,lesson["goal"].removeprefix("Hoy ").rstrip("."))
   if item["developed"] and r["course_order"]==1 and r["subject_slug"]=="lenguaje-comunicacion" and oa["code"].startswith("LE01 OA "):
    oa_number=int(oa["code"].rsplit(" ",1)[-1])
    for lesson_index,lesson in enumerate(item["developed"]["lessons"]):
     lesson["transversal"]=[attitude_link(oa_number,lesson_index,lesson["goal"].removeprefix("Hoy ").rstrip("."))]
   if item["developed"] and r["course_order"]==1 and r["subject_slug"] in {"ciencias-naturales","historia-geografia-ciencias-sociales","artes-visuales"} and oa["code"].startswith(("CN01 OA ","HI01 OA ","AR01 OA ")):
    for lesson_index,lesson in enumerate(item["developed"]["lessons"]):
     lesson["transversal"]=sha_transversal_links(oa["code"],lesson_index,lesson["goal"].removeprefix("Hoy ").rstrip("."))
   if item["developed"] and r["course_order"]==1 and oa["code"].startswith(("MU01 OA ","EF01 OA ","OR01 OA ","TE01 OA ","EN01 OA ","LC01 OA ")):
    for lesson_index,lesson in enumerate(item["developed"]["lessons"]):
     lesson["transversal"]=remaining_transversal_link(oa["code"],lesson_index,lesson["goal"].removeprefix("Hoy ").rstrip("."))
   if item["developed"]:enrich_item(item)
   if item["developed"] and len(item["developed"]["lessons"]) != len(phases):raise ValueError(f"{oa['code']}: el contenido desarrollado debe tener {len(phases)} clases")
   if item.get("draft") and len(item["draft"]["lessons"]) != len(phases):raise ValueError(f"{oa['code']}: el borrador debe tener {len(phases)} clases")
   if item.get("integration") and len(item["integration"]["lessons"]) != len(phases):raise ValueError(f"{oa['code']}: la integración debe tener {len(phases)} experiencias")
   objs.append(item)
   for lesson,(code,phase) in enumerate(zip(codes,phases),1):
    classes.append({"id":num,"class_code":code,"lesson":lesson,"lesson_count":len(phases),"phase":phase[0],"topic":item["topic"],"course":item["course"],"course_slug":item["course_slug"],"course_order":item["course_order"],"subject":item["subject"],"subject_slug":item["subject_slug"],"axis":item["axis"],"oa_code":item["oa_code"],"oa_text":item["oa_text"],"coverage":item["coverage"],"source_url":item["source_url"],"reading_count":len(reads),"editorial_status":"desarrollada" if item["developed"] else "integrada" if item.get("integration") else "borrador" if item.get("draft") else "secuenciada","publication_status":"publicada","path":path+"#"+code.lower(),"web_path":page_path(item)+"#"+code.lower()});num+=1
   developed_count=sum(x["editorial_status"]=="desarrollada" for x in classes)
 draft_count=sum(x["editorial_status"]=="borrador" for x in classes)
 integrated_count=sum(x["editorial_status"]=="integrada" for x in classes)
 cat={"schema_version":8,"verified_at":snap["verified_at"],"source_url":snap["source_url"],"rights_notice":snap["rights_notice"],"class_count":len(classes),"objective_count":len(objs),"course_count":12,"subject_count":len({x["subject"] for x in classes}),"reading_link_count":sum(len(x["readings"]) for x in objs),"editorial_counts":{"inventariada":len(classes),"secuenciada":len(classes),"borrador":draft_count,"desarrollada":developed_count,"integrada":integrated_count,"revisada":0,"publicada":len(classes)},"classes":classes}
 (CURRICULUM/"catalog.json").write_text(json.dumps(cat,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 pages_root=ROOT/"site"/"classes"
 if pages_root.exists():
  shutil.rmtree(pages_root)
 for index,item in enumerate(objs):
  target=ROOT/item["path"];target.parent.mkdir(parents=True,exist_ok=True);target.write_text(plan(item),encoding="utf-8")
  web_target=ROOT/"site"/page_path(item);web_target.parent.mkdir(parents=True,exist_ok=True)
  web_target.write_text(lesson_page(item,objs[index-1] if index else None,objs[index+1] if index+1<len(objs) else None),encoding="utf-8")
 levels_root=ROOT/"site"/"levels";levels_root.mkdir(parents=True,exist_ok=True)
 if not defer_generic_docs:
  (levels_root/"1-basico.html").write_text(grade_one_page(objs,classes),encoding="utf-8")
  (levels_root/"2-basico.html").write_text(grade_two_page(objs,classes),encoding="utf-8")
  (levels_root/"3-basico.html").write_text(grade_three_page(objs,classes),encoding="utf-8")
  (levels_root/"4-basico.html").write_text(grade_four_page(objs,classes),encoding="utf-8")
  (levels_root/"5-basico.html").write_text(grade_five_page(objs,classes),encoding="utf-8")
  (levels_root/"6-basico.html").write_text(grade_six_page(objs,classes),encoding="utf-8")
  (levels_root/"7-basico.html").write_text(grade_seven_page(objs,classes),encoding="utf-8")
  (levels_root/"8-basico.html").write_text(grade_eight_page(objs,classes),encoding="utf-8")
  (levels_root/"1-medio.html").write_text(grade_one_middle_page(objs,classes),encoding="utf-8")
  (levels_root/"2-medio.html").write_text(grade_two_middle_page(objs,classes),encoding="utf-8")
  (levels_root/"3-medio.html").write_text(grade_three_middle_page(objs,classes),encoding="utf-8")
  (levels_root/"4-medio.html").write_text(grade_four_middle_page(objs,classes),encoding="utf-8")
  (ROOT/"site"/"documentacion.html").write_text(documentation_page(objs,classes),encoding="utf-8")
 docs_root=ROOT/"docs";docs_root.mkdir(parents=True,exist_ok=True)
 if not defer_generic_docs:(docs_root/"PRIMERO_BASICO.md").write_text(grade_one_documentation(objs,classes),encoding="utf-8")
 grade_docs_root=docs_root/"1-basico";grade_docs_root.mkdir(parents=True,exist_ok=True)
 grade_objs,_,grade_subjects=grade_one_summary(objs,classes)
 if not defer_generic_docs:
  (grade_docs_root/"README.md").write_text(grade_one_index_documentation(objs,classes),encoding="utf-8")
  for subject_index,subject in enumerate(grade_subjects):
   subject_objectives=[item for item in grade_objs if item["subject_slug"]==subject["slug"]]
   previous_subject=grade_subjects[subject_index-1] if subject_index else None
   next_subject=grade_subjects[subject_index+1] if subject_index+1<len(grade_subjects) else None
   (grade_docs_root/f"{subject['slug']}.md").write_text(grade_one_subject_documentation(subject,subject_objectives,previous_subject,next_subject),encoding="utf-8")
 grade_two_docs_root=docs_root/"2-basico";grade_two_docs_root.mkdir(parents=True,exist_ok=True)
 if not defer_generic_docs:
  (grade_two_docs_root/"README.md").write_text(grade_two_index_documentation(objs,classes),encoding="utf-8")
  (docs_root/"SEGUNDO_BASICO.md").write_text(grade_two_documentation(objs,classes),encoding="utf-8")
  grade_two_objs,_,grade_two_subjects=grade_two_summary(objs,classes)
  for subject_index,subject in enumerate(grade_two_subjects):
   subject_objectives=[item for item in grade_two_objs if item["subject_slug"]==subject["slug"]]
   previous_subject=grade_two_subjects[subject_index-1] if subject_index else None
   next_subject=grade_two_subjects[subject_index+1] if subject_index+1<len(grade_two_subjects) else None
   content=grade_two_subject_documentation(subject,subject_objectives,previous_subject,next_subject)
   (grade_two_docs_root/f"{subject['slug']}.md").write_text(content,encoding="utf-8")
  grade_three_docs_root=docs_root/"3-basico";grade_three_docs_root.mkdir(parents=True,exist_ok=True)
  (grade_three_docs_root/"README.md").write_text(grade_three_index_documentation(objs,classes),encoding="utf-8")
  (docs_root/"TERCERO_BASICO.md").write_text(grade_three_documentation(objs,classes),encoding="utf-8")
  grade_three_objs,_,grade_three_subjects=grade_three_summary(objs,classes)
  for subject_index,subject in enumerate(grade_three_subjects):
   subject_objectives=[item for item in grade_three_objs if item["subject_slug"]==subject["slug"]]
   previous_subject=grade_three_subjects[subject_index-1] if subject_index else None
   next_subject=grade_three_subjects[subject_index+1] if subject_index+1<len(grade_three_subjects) else None
   content=grade_three_subject_documentation(subject,subject_objectives,previous_subject,next_subject)
   (grade_three_docs_root/f"{subject['slug']}.md").write_text(content,encoding="utf-8")
  grade_four_docs_root=docs_root/"4-basico";grade_four_docs_root.mkdir(parents=True,exist_ok=True)
  if not defer_generic_docs:
   (grade_four_docs_root/"README.md").write_text(grade_four_index_documentation(objs,classes),encoding="utf-8")
   (docs_root/"CUARTO_BASICO.md").write_text(grade_four_documentation(objs,classes),encoding="utf-8")
   grade_four_objs,_,grade_four_subjects=grade_four_summary(objs,classes)
   for subject_index,subject in enumerate(grade_four_subjects):
    subject_objectives=[item for item in grade_four_objs if item["subject_slug"]==subject["slug"]]
    previous_subject=grade_four_subjects[subject_index-1] if subject_index else None
    next_subject=grade_four_subjects[subject_index+1] if subject_index+1<len(grade_four_subjects) else None
    content=grade_three_subject_documentation(subject,subject_objectives,previous_subject,next_subject,"4°","3°",GRADE_FOUR_SUBJECT_PROFILES)
    (grade_four_docs_root/f"{subject['slug']}.md").write_text(content,encoding="utf-8")
  grade_five_docs_root=docs_root/"5-basico";grade_five_docs_root.mkdir(parents=True,exist_ok=True)
  (grade_five_docs_root/"README.md").write_text(grade_five_index_documentation(objs,classes),encoding="utf-8")
  (docs_root/"QUINTO_BASICO.md").write_text(grade_five_documentation(objs,classes),encoding="utf-8")
  grade_five_objs,_,grade_five_subjects=grade_five_summary(objs,classes)
  for subject_index,subject in enumerate(grade_five_subjects):
   subject_objectives=[item for item in grade_five_objs if item["subject_slug"]==subject["slug"]]
   previous_subject=grade_five_subjects[subject_index-1] if subject_index else None
   next_subject=grade_five_subjects[subject_index+1] if subject_index+1<len(grade_five_subjects) else None
   content=grade_three_subject_documentation(subject,subject_objectives,previous_subject,next_subject,"5°","4°",GRADE_FIVE_SUBJECT_PROFILES)
   (grade_five_docs_root/f"{subject['slug']}.md").write_text(content,encoding="utf-8")
  grade_six_docs_root=docs_root/"6-basico";grade_six_docs_root.mkdir(parents=True,exist_ok=True)
  (grade_six_docs_root/"README.md").write_text(grade_six_index_documentation(objs,classes),encoding="utf-8")
  (docs_root/"SEXTO_BASICO.md").write_text(grade_six_documentation(objs,classes),encoding="utf-8")
  grade_six_objs,_,grade_six_subjects=grade_six_summary(objs,classes)
  for subject_index,subject in enumerate(grade_six_subjects):
   subject_objectives=[item for item in grade_six_objs if item["subject_slug"]==subject["slug"]]
   previous_subject=grade_six_subjects[subject_index-1] if subject_index else None
   next_subject=grade_six_subjects[subject_index+1] if subject_index+1<len(grade_six_subjects) else None
   content=grade_three_subject_documentation(subject,subject_objectives,previous_subject,next_subject,"6°","5°",GRADE_SIX_SUBJECT_PROFILES)
   (grade_six_docs_root/f"{subject['slug']}.md").write_text(content,encoding="utf-8")
  grade_seven_docs_root=docs_root/"7-basico";grade_seven_docs_root.mkdir(parents=True,exist_ok=True)
  (grade_seven_docs_root/"README.md").write_text(grade_seven_index_documentation(objs,classes),encoding="utf-8")
  (docs_root/"SEPTIMO_BASICO.md").write_text(grade_seven_documentation(objs,classes),encoding="utf-8")
  grade_seven_objs,_,grade_seven_subjects=grade_summary(objs,classes,7)
  grade_seven_subjects=[subject for subject in grade_seven_subjects if subject["slug"] in GRADE_SEVEN_CORE_PROFILES]
  for subject_index,subject in enumerate(grade_seven_subjects):
   subject_objectives=[item for item in grade_seven_objs if item["subject_slug"]==subject["slug"]]
   previous_subject=grade_seven_subjects[subject_index-1] if subject_index else None
   next_subject=grade_seven_subjects[subject_index+1] if subject_index+1<len(grade_seven_subjects) else None
   content=grade_three_subject_documentation(subject,subject_objectives,previous_subject,next_subject,"7°","6°",GRADE_SEVEN_CORE_PROFILES)
   (grade_seven_docs_root/f"{subject['slug']}.md").write_text(content,encoding="utf-8")
  grade_eight_docs_root=docs_root/"8-basico";grade_eight_docs_root.mkdir(parents=True,exist_ok=True)
  (grade_eight_docs_root/"README.md").write_text(grade_eight_index_documentation(objs,classes),encoding="utf-8")
  (docs_root/"OCTAVO_BASICO.md").write_text(grade_eight_documentation(objs,classes),encoding="utf-8")
  grade_eight_objs,_,grade_eight_subjects=grade_summary(objs,classes,8)
  grade_eight_subjects=[subject for subject in grade_eight_subjects if subject["slug"] in GRADE_EIGHT_CORE_PROFILES]
  for subject_index,subject in enumerate(grade_eight_subjects):
   subject_objectives=[item for item in grade_eight_objs if item["subject_slug"]==subject["slug"]]
   previous_subject=grade_eight_subjects[subject_index-1] if subject_index else None
   next_subject=grade_eight_subjects[subject_index+1] if subject_index+1<len(grade_eight_subjects) else None
   content=grade_three_subject_documentation(subject,subject_objectives,previous_subject,next_subject,"8°","7°",GRADE_EIGHT_CORE_PROFILES)
   (grade_eight_docs_root/f"{subject['slug']}.md").write_text(content,encoding="utf-8")
  grade_one_middle_docs_root=docs_root/"1-medio";grade_one_middle_docs_root.mkdir(parents=True,exist_ok=True)
  (grade_one_middle_docs_root/"README.md").write_text(grade_one_middle_index_documentation(objs,classes),encoding="utf-8")
  (docs_root/"PRIMERO_MEDIO.md").write_text(grade_one_middle_documentation(objs,classes),encoding="utf-8")
  grade_one_middle_objs,_,grade_one_middle_subjects=grade_summary(objs,classes,9)
  grade_one_middle_subjects=[subject for subject in grade_one_middle_subjects if subject["slug"] in GRADE_ONE_MIDDLE_CORE_PROFILES]
  for subject_index,subject in enumerate(grade_one_middle_subjects):
   subject_objectives=[item for item in grade_one_middle_objs if item["subject_slug"]==subject["slug"]]
   previous_subject=grade_one_middle_subjects[subject_index-1] if subject_index else None
   next_subject=grade_one_middle_subjects[subject_index+1] if subject_index+1<len(grade_one_middle_subjects) else None
   content=grade_three_subject_documentation(subject,subject_objectives,previous_subject,next_subject,"1° medio","8° básico",GRADE_ONE_MIDDLE_CORE_PROFILES).replace("1° medio básico","1° medio").replace("8° básico básico","8° básico")
   (grade_one_middle_docs_root/f"{subject['slug']}.md").write_text(content,encoding="utf-8")
  grade_two_middle_docs_root=docs_root/"2-medio";grade_two_middle_docs_root.mkdir(parents=True,exist_ok=True)
  (grade_two_middle_docs_root/"README.md").write_text(grade_two_middle_index_documentation(objs,classes),encoding="utf-8")
  (docs_root/"SEGUNDO_MEDIO.md").write_text(grade_two_middle_documentation(objs,classes),encoding="utf-8")
  grade_two_middle_objs,_,grade_two_middle_subjects=grade_summary(objs,classes,10)
  grade_two_middle_subjects=[subject for subject in grade_two_middle_subjects if subject["slug"] in GRADE_TWO_MIDDLE_CORE_PROFILES]
  for subject_index,subject in enumerate(grade_two_middle_subjects):
   subject_objectives=[item for item in grade_two_middle_objs if item["subject_slug"]==subject["slug"]]
   previous_subject=grade_two_middle_subjects[subject_index-1] if subject_index else None
   next_subject=grade_two_middle_subjects[subject_index+1] if subject_index+1<len(grade_two_middle_subjects) else None
   content=grade_three_subject_documentation(subject,subject_objectives,previous_subject,next_subject,"2° medio","1° medio",GRADE_TWO_MIDDLE_CORE_PROFILES).replace("2° medio básico","2° medio").replace("1° medio básico","1° medio")
   (grade_two_middle_docs_root/f"{subject['slug']}.md").write_text(content,encoding="utf-8")
  grade_three_middle_docs_root=docs_root/"3-medio";grade_three_middle_docs_root.mkdir(parents=True,exist_ok=True)
  (grade_three_middle_docs_root/"README.md").write_text(grade_three_middle_index_documentation(objs,classes),encoding="utf-8")
  (docs_root/"TERCERO_MEDIO.md").write_text(grade_three_middle_documentation(objs,classes),encoding="utf-8")
  grade_three_middle_objs,_,grade_three_middle_subjects=grade_summary(objs,classes,11)
  grade_three_middle_subjects=[subject for subject in grade_three_middle_subjects if subject["slug"] in GRADE_THREE_MIDDLE_CORE_PROFILES]
  for subject_index,subject in enumerate(grade_three_middle_subjects):
   subject_objectives=[item for item in grade_three_middle_objs if item["subject_slug"]==subject["slug"]]
   previous_subject=grade_three_middle_subjects[subject_index-1] if subject_index else None
   next_subject=grade_three_middle_subjects[subject_index+1] if subject_index+1<len(grade_three_middle_subjects) else None
   content=(
    grade_three_subject_documentation(subject,subject_objectives,previous_subject,next_subject,"3° medio","2° medio",GRADE_THREE_MIDDLE_CORE_PROFILES)
    .replace("3° medio básico","3° medio")
    .replace("2° medio básico","2° medio")
    .replace(" · 1 ejes curriculares ·"," · 1 eje curricular ·")
   )
   (grade_three_middle_docs_root/f"{subject['slug']}.md").write_text(content,encoding="utf-8")
  grade_four_middle_docs_root=docs_root/"4-medio";grade_four_middle_docs_root.mkdir(parents=True,exist_ok=True)
  (grade_four_middle_docs_root/"README.md").write_text(grade_four_middle_index_documentation(objs,classes),encoding="utf-8")
  (docs_root/"CUARTO_MEDIO.md").write_text(grade_four_middle_documentation(objs,classes),encoding="utf-8")
  grade_four_middle_objs,_,grade_four_middle_subjects=grade_summary(objs,classes,12)
  grade_four_middle_subjects=[subject for subject in grade_four_middle_subjects if subject["slug"] in GRADE_FOUR_MIDDLE_PROFILES]
  for subject_index,subject in enumerate(grade_four_middle_subjects):
   subject_objectives=[item for item in grade_four_middle_objs if item["subject_slug"]==subject["slug"]]
   previous_subject=grade_four_middle_subjects[subject_index-1] if subject_index else None
   next_subject=grade_four_middle_subjects[subject_index+1] if subject_index+1<len(grade_four_middle_subjects) else None
   content=(
    grade_three_subject_documentation(subject,subject_objectives,previous_subject,next_subject,"4° medio","3° medio",GRADE_FOUR_MIDDLE_PROFILES)
    .replace("4° medio básico","4° medio")
    .replace("3° medio básico","3° medio")
    .replace(" · 1 ejes curriculares ·"," · 1 eje curricular ·")
   )
   (grade_four_middle_docs_root/f"{subject['slug']}.md").write_text(content,encoding="utf-8")
  documentation_pages=generate_documentation_pages()
 else:documentation_pages=[]
 (ROOT/"site"/"catalog.json").write_text(json.dumps(cat,ensure_ascii=False)+"\n",encoding="utf-8")
 (ROOT/"site"/"updates.json").write_text(json.dumps(changelog_updates(),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 version_public_data()
 version_public_data()
 reviews_site=ROOT/"site"/"reviews";reviews_site.mkdir(parents=True,exist_ok=True)
 for schema_name in ("review-record.schema.json","pilot-record.schema.json"):
  shutil.copyfile(ROOT/"reviews"/schema_name,reviews_site/schema_name)
 reviews_site=ROOT/"site"/"reviews";reviews_site.mkdir(parents=True,exist_ok=True)
 for schema_name in ("review-record.schema.json","pilot-record.schema.json"):
  shutil.copyfile(ROOT/"reviews"/schema_name,reviews_site/schema_name)
 lines=["# Planificación curricular chilena","",f"## {developed_count:,} clases · {integrated_count:,} experiencias integradas · {cat['objective_count']:,} OA · 12 niveles".replace(",","."),"",f"El catálogo contiene {len(classes):,} registros pedagógicos: {developed_count:,} clases disciplinares y {integrated_count:,} experiencias de integración transversal. Las experiencias integradas no son clases independientes.".replace(",","."),"","> Formación común, propuestas, asignaturas según contexto y electivos se distinguen; no representan una carga simultánea.",""]
 for order in range(1,13):
  cur=[x for x in classes if x["course_order"]==order];seen={}
  for x in cur:seen[(x["subject"],x["oa_code"],x["path"].split("#")[0],x["topic"],x["coverage"],x["editorial_status"])]=x["lesson_count"]
  lines += [f"## {cur[0]['course']}","","| Asignatura | OA y tema | Tipo | Bloques | Cobertura |","|---|---|---|---:|---|"]
  for (sub,oa,path,topic,c,status),n in seen.items():
   kind="Clases disciplinares" if status=="desarrollada" else "Experiencias integradas" if status=="integrada" else "Propuestas pendientes"
   lines.append(f"| {sub} | [{oa} · {topic}]({path}) | {kind} | {n} | {c} |")
  lines.append("")
 if not defer_generic_docs:(ROOT/"CURRICULUM.md").write_text("\n".join(lines),encoding="utf-8")
 urls=["https://vladimiracunadev-create.github.io/chilean-school-learning-path/","https://vladimiracunadev-create.github.io/chilean-school-learning-path/documentacion.html","https://vladimiracunadev-create.github.io/chilean-school-learning-path/competencias/","https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/1-basico.html","https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/2-basico.html","https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/3-basico.html","https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/4-basico.html","https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/5-basico.html","https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/6-basico.html","https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/7-basico.html","https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/8-basico.html","https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/1-medio.html","https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/2-medio.html","https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/3-medio.html","https://vladimiracunadev-create.github.io/chilean-school-learning-path/levels/4-medio.html"]+[f"https://vladimiracunadev-create.github.io/chilean-school-learning-path/{page_path(item)}" for item in objs]+[f"https://vladimiracunadev-create.github.io/chilean-school-learning-path/{path.as_posix()}" for path in documentation_pages]
 sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"\n".join(f"  <url><loc>{url}</loc></url>" for url in urls)+"\n</urlset>\n"
 if not defer_generic_docs:(ROOT/"site"/"sitemap.xml").write_text(sitemap,encoding="utf-8")
 print(json.dumps({"entry_count":cat["class_count"],"developed_class_count":developed_count,"integration_experience_count":integrated_count,**{k:cat[k] for k in ("objective_count","course_count","subject_count","reading_link_count")}}))
if __name__=="__main__":main()

