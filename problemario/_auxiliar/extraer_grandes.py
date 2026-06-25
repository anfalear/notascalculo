"""
Extrae gradientes_ORIGINAL.tex y multiplicadoresintdobles_ORIGINAL.tex del JSONL.
Los archivos grandes pudieron haberse leido en multiples chunks; los concatenamos.
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
    return lines  # lista de (lineno, content)

# Marcadores unicos de cada archivo
grad_marker   = 'Derivada Direccional y Valores Extremos'  # titulo del chapter original
mult_marker   = r'Lección 2.2'  # "Leccion 2.2" en el chapter original

# Coleccionar todos los bloques con lineas numeradas para cada archivo
grad_chunks = {}   # lineno -> content
mult_chunks = {}

with open(jsonl_path, 'r', encoding='utf-8', errors='replace') as f:
    for raw in f:
        raw = raw.strip()
        if not raw:
            continue
        # Filtro rapido
        has_grad = 'Derivada Direccional' in raw or ('gradientes' in raw and r'\chapter' in raw)
        has_mult = 'Lecci' in raw and '2.2' in raw and 'multiplicadores' in raw
        if not (has_grad or has_mult):
            continue
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            continue

        def search(node, depth=0):
            if depth > 10:
                return
            if isinstance(node, str):
                if 'Derivada Direccional y Valores Extremos' in node:
                    for lineno, content in extract_numbered_lines(node):
                        grad_chunks[lineno] = content
                if 'Lecci' in node and '2.2' in node and 'Multiplicadores' in node and len(node) > 1000:
                    for lineno, content in extract_numbered_lines(node):
                        mult_chunks[lineno] = content
            elif isinstance(node, dict):
                for v in node.values():
                    search(v, depth+1)
            elif isinstance(node, list):
                for item in node:
                    search(item, depth+1)
        search(obj)

# Reconstruir archivos desde chunks (ordenados por numero de linea)
def reconstruct(chunks, outname, expected_min):
    if not chunks:
        print(f'  FALTA  {outname}  (0 lineas)')
        return
    sorted_lines = [content for _, content in sorted(chunks.items())]
    out = fr'{base}\{outname}'
    with open(out, 'w', encoding='utf-8') as g:
        g.writelines(sorted_lines)
    n = len(sorted_lines)
    status = 'OK' if n >= expected_min else 'PARCIAL'
    print(f'  {status}  {outname}  ({n} lineas, minimo esperado: {expected_min})')

reconstruct(grad_chunks, 'gradientes_ORIGINAL.tex', 900)
reconstruct(mult_chunks, 'multiplicadoresintdobles_ORIGINAL.tex', 700)
