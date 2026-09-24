import json,re,html,urllib.request
from concurrent.futures import ThreadPoolExecutor,as_completed
from datetime import date
from pathlib import Path
P=Path("sources/mineduc-curriculum-snapshot.json");BASE="https://www.curriculumnacional.cl"
def clean(x):return re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>"," ",x))).strip()
def work(obj):
 req=urllib.request.Request(obj["url"],headers={"User-Agent":"TrayectoriaEscolarChile/1.0"})
 with urllib.request.urlopen(req,timeout=40) as r:page=r.read().decode("utf-8",errors="replace")
 found={}
 for card in re.findall(r'<article class="node node--type-recurso.*?</article>',page,re.S|re.I):
  if re.search(r'>\s*Lecturas\s*<',card,re.I):
   m=re.search(r'<h3><a href="([^"]+)"[^>]*>(.*?)</a></h3>',card,re.S|re.I)
   if m:
    url=BASE+m.group(1) if m.group(1).startswith("/") else m.group(1);found[url]={"title":clean(m.group(2)),"url":url}
 return obj,list(found.values())
d=json.loads(P.read_text(encoding="utf-8"));targets=[o for r in d["records"] if "leng" in r["subject_slug"] for o in r["objectives"]]
with ThreadPoolExecutor(max_workers=10) as pool:
 fs=[pool.submit(work,o) for o in targets]
 for n,f in enumerate(as_completed(fs),1):
  obj,reads=f.result();obj["readings"]=reads
  if n%50==0:print(f"{n}/{len(targets)}",flush=True)
d["readings_verified_at"]=date.today().isoformat();P.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(sum(len(o.get("readings",[])) for r in d["records"] for o in r["objectives"]))

