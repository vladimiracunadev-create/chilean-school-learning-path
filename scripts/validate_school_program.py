import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1];cat=json.loads((R/"curriculum/catalog.json").read_text(encoding="utf-8"));snap=json.loads((R/"sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"));errors=[];classes=cat["classes"];oas=sum(len(r["objectives"]) for r in snap["records"])
if cat["objective_count"]!=oas:errors.append("OA count mismatch")
if len(classes)!=cat["class_count"]:errors.append("class count mismatch")
if cat["course_count"]!=12:errors.append("expected 12 levels")
for x in classes:
 for key in ("class_code","topic","course","subject","axis","oa_code","oa_text","coverage","path"):
  if not x.get(key):errors.append("missing "+key)
 path,anchor=x["path"].split("#",1);p=R/path
 if not p.exists():errors.append("missing "+path)
 elif anchor not in p.read_text(encoding="utf-8"):errors.append("missing anchor "+anchor)
 if not 4<=x["lesson_count"]<=7:errors.append("invalid dosage")
if errors:print("\n".join(errors[:50]));sys.exit(1)
print(f"OK: {cat['class_count']} classes, {oas} OA, {cat['reading_link_count']} reading links")

