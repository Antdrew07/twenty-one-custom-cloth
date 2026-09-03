#!/usr/bin/env python3
"""Rebuild index.html with embedded menswear photography and SVG brand marks."""
import base64, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
tpl = (root / "src/tpl.html").read_text()
for name in sorted(set(re.findall(r"\{\{IMG:([\w]+)\}\}", tpl))):
    b64 = base64.b64encode((root / f"assets/web/{name}.jpg").read_bytes()).decode()
    tpl = tpl.replace("{{IMG:%s}}" % name, "data:image/jpeg;base64," + b64)
for name in sorted(set(re.findall(r"\{\{SVG:([\w-]+)\}\}", tpl))):
    b64 = base64.b64encode((root / f"assets/brand/{name}.svg").read_bytes()).decode()
    tpl = tpl.replace("{{SVG:%s}}" % name, "data:image/svg+xml;base64," + b64)
assert "{{IMG:" not in tpl and "{{SVG:" not in tpl
head = []
for pat in [r"<title>.*?</title>", r"<meta[^>]*>", r"<link[^>]*>", r"<style>.*?</style>"]:
    head += re.findall(pat, tpl, re.S); tpl = re.sub(pat, "", tpl, flags=re.S)
out = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
       + "\n".join(head) + "\n</head>\n<body>\n" + tpl.strip() + "\n</body>\n</html>\n")
(root / "index.html").write_text(out)
print(f"index.html rebuilt: {len(out)/1024/1024:.2f} MB")
