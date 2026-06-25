"""
Segunda busqueda: extrae el contenido de limvariasvariables.tex del JSONL
probando diferentes formatos de respuesta del Read tool.
"""
import json, re

jsonl_path = r'C:\Users\anfalear\.claude\projects\C--Users-anfalear-notascalculo-problemario\3bf94b73-1ff8-4772-856c-552321bbde0d.jsonl'
out_path = r'C:\Users\anfalear\notascalculo\problemario\limvariasvariables_ORIGINAL.tex'

def extract_numbered_lines(text):
    """Extrae lineas del formato '  NNN\tCONTENIDO' o 'NNN  CONTENIDO'."""
    lines_out = []
    for l in text.split('\n'):
        # Formato con tab: "  453\t\\end{myproof}"
        m = re.match(r'^\s*(\d+)\t(.*)$', l)
        if m:
            lines_out.append(m.group(2) + '\n')
            continue
    return lines_out

best = None
best_len = 0

with open(jsonl_path, 'r', encoding='utf-8', errors='replace') as f:
    for lineno, raw in enumerate(f):
        raw = raw.strip()
        if not raw:
            continue
        # Busqueda rapida: la linea del JSON debe contener el patron
        if 'Derivadas parciales de primer orden' not in raw:
            continue
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            continue

        # Buscar recursivamente en el objeto
        def search(node, depth=0):
            global best, best_len
            if depth > 10:
                return
            if isinstance(node, str):
                if 'Derivadas parciales de primer orden' in node and '\\chapter{' in node:
                    lines = extract_numbered_lines(node)
                    if len(lines) > best_len:
                        best_len = len(lines)
                        best = lines
                        print(f'  Encontrado fragmento: {len(lines)} lineas (JSON linea {lineno})')
            elif isinstance(node, dict):
                for v in node.values():
                    search(v, depth+1)
            elif isinstance(node, list):
                for item in node:
                    search(item, depth+1)

        search(obj)

if best and best_len > 400:
    with open(out_path, 'w', encoding='utf-8') as g:
        g.writelines(best)
    print(f'\nGuardado: {best_len} lineas en limvariasvariables_ORIGINAL.tex')
else:
    print(f'\nFragmento mas largo encontrado: {best_len} lineas — insuficiente.')
    # Mostrar las 5 primeras lineas del fragmento mas largo
    if best:
        print('Primeras lineas:')
        for l in best[:5]:
            print('  ' + repr(l))
