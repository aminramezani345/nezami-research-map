#!/usr/bin/env python3
"""Inline data/research-map.json into src/template.html -> index.html.

Run after editing the JSON:  python3 build.py
"""
import json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent
data = json.loads((root / "data" / "research-map.json").read_text(encoding="utf-8"))

# light validation so typos are caught before publishing
ids, problems = set(), []
statuses = set(data["statuses"])
for a in data["areas"]:
    for key in ("id", "label", "short", "color", "subtopics"):
        if key not in a: problems.append(f"area missing '{key}': {a.get('id')}")
    for t in a["subtopics"]:
        if not t["items"]: problems.append(f"subtopic has no items: {t['id']}")
        for it in t["items"]:
            for obj_id in (it["id"],):
                if obj_id in ids: problems.append(f"duplicate id: {obj_id}")
                ids.add(obj_id)
            if it["status"] not in statuses: problems.append(f"unknown status '{it['status']}' in {it['id']}")
            if it.get("url") and it.get("linkType") in (None, "none"): problems.append(f"url without linkType in {it['id']}")
if problems:
    print("Data problems:\n  " + "\n  ".join(problems)); sys.exit(1)

payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
html = (root / "src" / "template.html").read_text(encoding="utf-8").replace("/*__DATA__*/", payload)
(root / "index.html").write_text(html, encoding="utf-8")
n = sum(len(t["items"]) for a in data["areas"] for t in a["subtopics"])
print(f"Built index.html: {len(data['areas'])} areas, {sum(len(a['subtopics']) for a in data['areas'])} subtopics, {n} items")
