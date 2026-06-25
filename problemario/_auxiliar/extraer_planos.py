"""
Extrae planostangentes_ORIGINAL.tex del JSONL usando el marcador unico del capitulo.
El marcador es la cadena que solo aparece en ese archivo:
  'Plano tangente, aproximaci' + 'Regla de la cadena' en el mismo bloque de texto.
"""
import json, re

jsonl_path = r'C:\Users\anfalear\.claude\projects\C--Users-anfalear-notascalculo-problemario\3bf94b73-1ff8-4772-856c-552321bbde0d.jsonl'
base = r'C:\Users\anfalear\notascalculo\problemario'

def extract_numbered_lines(text):
    lines = []
    for l in text.split('\n'):
        m = re.match(r'^\s*(\d+)\t(.*)$', l)
        if m:
            lines.append((int(m.group(1)), m.group(2) + '\n'))
    return lines

chunks = {}

with open(jsonl_path, 'r', encoding='utf-8', errors='replace') as f:
    for raw in f:
        raw = raw.strip()
        if not raw:
            continue
        # Marcador: solo aparece en planostangentes.tex
        if 'Plano tangente' not in raw or 'subsubsection' not in raw:
            continue
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            continue

        def search(node, depth=0):
            if depth > 10:
                return
            if isinstance(node, str):
                if 'subsubsection' in node and 'Plano tangente' in node and 'Regla de la cadena' in node:
                    for lineno, content in extract_numbered_lines(node):
                        chunks[lineno] = content
            elif isinstance(node, dict):
                for v in node.values():
                    search(v, depth+1)
            elif isinstance(node, list):
                for item in node:
                    search(item, depth+1)
        search(obj)

if chunks:
    sorted_lines = [content for _, content in sorted(chunks.items())]
    out = fr'{base}\planostangentes_ORIGINAL.tex'
    with open(out, 'w', encoding='utf-8') as g:
        g.writelines(sorted_lines)
    n = len(sorted_lines)
    print(f'OK  planostangentes_ORIGINAL.tex  ({n} lineas)')
    print(f'  [0]: {sorted_lines[0].strip()[:80].encode("ascii","replace").decode("ascii")!r}')
    print(f'  [2]: {sorted_lines[2].strip()[:80].encode("ascii","replace").decode("ascii")!r}')
    print(f'  [18]: {sorted_lines[18].strip()[:80].encode("ascii","replace").decode("ascii")!r}')
    print(f'  [181]: {sorted_lines[181].strip()[:80].encode("ascii","replace").decode("ascii")!r}')
else:
    print('FALTA: no se encontro el marcador en el JSONL.')
