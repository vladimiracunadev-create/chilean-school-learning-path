"""Build variable teacher-ready Chilean lesson sequences."""
import json
from pathlib import Path
from build_school_curriculum import ROOT,SNAPSHOT,CURRICULUM,slugify,topic_from
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
 return ("concepto, relación, criterio, evidencia, aplicación y revisión","desempeño observable alineado al OA","memorizar sin comprender; completar sin demostrar el aprendizaje")
def cov(slug,order):
 if "ingles-propuesta" in slug:return "propuesta-mineduc"
 if "pueblos-originarios" in slug or "lengua-indigena" in slug:return "segun-contexto-y-normativa"
 if order>=11 and slug in {"artes-visuales","musica","danza","teatro"}:return "electivo-de-artes"
 if order>=11 and slug.startswith("educacion-fisica-salud-"):return "electivo-de-educacion-fisica"
 if order>=11 and slug in {"ambiente-sostenibilidad","bienestar-salud","chile-region-latinoamericana","mundo-global","seguridad-prevencion-autocuidado","tecnologia-sociedad"}:return "modulo-electivo"
 return "formacion-general-comun"
def plan(item):
 vocab,product,errors=discipline(item["subject_slug"]);parts=[]
 for i,(code,(title,focus)) in enumerate(zip(item["codes"],item["phases"]),1):
  parts.append(f"""### Clase {i} de {len(item['phases'])}: {title} {{#{code.lower()}}}
**Foco:** {focus}. **Meta para estudiantes:** comprender el foco y demostrarlo con evidencia.

| Momento | Tiempo | Acción docente y experiencia |
|---|---:|---|
| Inicio | 10 min | Presenta un caso cercano, comunica la meta y obtiene una respuesta de todas y todos. |
| Explicación | 20 min | Explica la idea central con ejemplo y contraejemplo; piensa en voz alta y comprueba comprensión. |
| Práctica guiada | 25 min | Resuelven o producen con apoyo. Pregunta por evidencia y retroalimenta el procedimiento. |
| Desempeño individual | 25 min | Cada estudiante aplica, explica una decisión y entrega una producción propia. |
| Cierre | 10 min | Ticket con respuesta, evidencia y duda: logrado; próximo con apoyo; requiere otra explicación. |

**Apoyo en el mismo OA:** ejemplo resuelto, pasos visibles, vocabulario anticipado, ensayo oral y retiro gradual del apoyo. Admite respuesta oral, gráfica, manipulativa o digital si conserva la demanda; no reemplaces el OA por una tarea más fácil.

**Profundización:** comparar otra estrategia, formular una objeción o caso límite y transferir a una situación nueva. Exige razonamiento revisable en lugar de ejercicios repetidos.

**Errores previsibles:** {errors}. **Evidencia:** {product} que responda al verbo del OA y muestre razonamiento. Reenseña errores comunes; forma un grupo breve ante errores puntuales; ofrece transferencia cuando exista dominio. En 45 minutos conserva meta, modelado, práctica y ticket.
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
def main():
 snap=json.loads(SNAPSHOT.read_text(encoding="utf-8"));objs=[];classes=[];num=1
 for r in sorted(snap["records"],key=lambda x:(x["course_order"],x["subject"],x["subject_slug"])):
  for oa in r["objectives"]:
   reads=oa.get("readings",[]);phases=dose(oa["description"],r["subject_slug"],reads);codes=[f"CL-{num+i:05d}" for i in range(len(phases))];path=f"curriculum/{r['course_slug']}/{r['subject_slug']}/{slugify(oa['code'])}.md"
   item={"topic":topic_from(oa["description"]),"course":r["course"],"course_slug":r["course_slug"],"course_order":r["course_order"],"subject":r["subject"],"subject_slug":r["subject_slug"],"axis":oa["axis"],"oa_code":oa["code"],"oa_text":oa["description"],"coverage":cov(r["subject_slug"],r["course_order"]),"source_url":oa["url"],"subject_url":r["subject_url"],"verified_at":snap["verified_at"],"readings":reads,"path":path,"codes":codes,"phases":phases};objs.append(item)
   for lesson,(code,phase) in enumerate(zip(codes,phases),1):
    classes.append({"id":num,"class_code":code,"lesson":lesson,"lesson_count":len(phases),"phase":phase[0],"topic":item["topic"],"course":item["course"],"course_slug":item["course_slug"],"course_order":item["course_order"],"subject":item["subject"],"subject_slug":item["subject_slug"],"axis":item["axis"],"oa_code":item["oa_code"],"oa_text":item["oa_text"],"coverage":item["coverage"],"source_url":item["source_url"],"reading_count":len(reads),"path":path+"#"+code.lower()});num+=1
 cat={"schema_version":3,"verified_at":snap["verified_at"],"source_url":snap["source_url"],"class_count":len(classes),"objective_count":len(objs),"course_count":12,"subject_count":len({x["subject"] for x in classes}),"reading_link_count":sum(len(x["readings"]) for x in objs),"classes":classes}
 (CURRICULUM/"catalog.json").write_text(json.dumps(cat,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 for item in objs:
  target=ROOT/item["path"];target.parent.mkdir(parents=True,exist_ok=True);target.write_text(plan(item),encoding="utf-8")
 (ROOT/"site"/"catalog.json").write_text(json.dumps(cat,ensure_ascii=False)+"\n",encoding="utf-8")
 lines=["# Planificación curricular chilena","",f"## {cat['class_count']:,} clases · {cat['objective_count']:,} OA · 12 niveles".replace(",","."),"","Cada clase tiene nivel, asignatura, tema, fase y OA trazable. La dosificación de 4 a 7 clases se ajusta con evidencia.","","> Formación común, propuestas, asignaturas según contexto y electivos se distinguen; no representan una carga simultánea.",""]
 for order in range(1,13):
  cur=[x for x in classes if x["course_order"]==order];seen={}
  for x in cur:seen[(x["subject"],x["oa_code"],x["path"].split("#")[0],x["topic"],x["coverage"])]=x["lesson_count"]
  lines += [f"## {cur[0]['course']}","","| Asignatura | OA y tema | Clases | Cobertura |","|---|---|---:|---|"]
  for (sub,oa,path,topic,c),n in seen.items():lines.append(f"| {sub} | [{oa} · {topic}]({path}) | {n} | {c} |")
  lines.append("")
 (ROOT/"CURRICULUM.md").write_text("\n".join(lines),encoding="utf-8")
 print(json.dumps({k:cat[k] for k in ("class_count","objective_count","course_count","subject_count","reading_link_count")}))
if __name__=="__main__":main()

