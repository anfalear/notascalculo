"""
Extrae los 5 archivos originales del JSONL de la sesion previa.
Los guarda con sufijo _ORIGINAL.tex para que el script de reorganizacion los use.
"""
import json, re

jsonl_path = r'C:\Users\anfalear\.claude\projects\C--Users-anfalear-notascalculo-problemario\3bf94b73-1ff8-4772-856c-552321bbde0d.jsonl'
base = r'C:\Users\anfalear\notascalculo\problemario'

targets = {
    'planostangentes.tex':          ('planostangentes_ORIGINAL.tex',         100),
    'gradientes.tex':               ('gradientes_ORIGINAL.tex',              500),
    'multiplicadoresintdobles.tex': ('multiplicadoresintdobles_ORIGINAL.tex', 400),
    'apintdobles.tex':              ('apintdobles_ORIGINAL.tex',             100),
}
found = {k: None for k in targets}
found_len = {k: 0 for k in targets}

def extract_numbered_lines(text):
    lines_out = []
    for l in text.split('\n'):
        m = re.match(r'^\s*(\d+)\t(.*)$', l)
        if m:
            lines_out.append(m.group(2) + '\n')
    return lines_out

def search(node, depth=0):
    if depth > 10:
        return
    if isinstance(node, str):
        for fname, (outname, min_lines) in targets.items():
            if fname in node and len(node) > min_lines * 30:
                lines = extract_numbered_lines(node)
                if len(lines) > found_len[fname]:
                    found_len[fname] = len(lines)
                    found[fname] = lines
    elif isinstance(node, dict):
        for v in node.values():
            search(v, depth + 1)
    elif isinstance(node, list):
        for item in node:
            search(item, depth + 1)

with open(jsonl_path, 'r', encoding='utf-8', errors='replace') as f:
    for raw in f:
        raw = raw.strip()
        if not raw:
            continue
        # Solo parsear lineas que contengan alguno de los archivos buscados
        if not any(t in raw for t in targets):
            continue
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            continue
        search(obj)

print('Resultados:')
for fname, (outname, min_lines) in targets.items():
    lines = found[fname]
    if lines and len(lines) >= min_lines:
        out = fr'{base}\{outname}'
        with open(out, 'w', encoding='utf-8') as g:
            g.writelines(lines)
        print(f'  OK  {outname}  ({len(lines)} lineas)')
    else:
        n = found_len[fname]
        print(f'  FALTA  {fname}  (mejor fragmento: {n} lineas, minimo requerido: {min_lines})')
