"""
Extrae el contenido de limvariasvariables.tex de la sesion JSONL previa,
donde el archivo completo (1233 lineas) fue leido antes de ser modificado.
Guarda el resultado en limvariasvariables_ORIGINAL.tex
"""
import json, re

jsonl_path = r'C:\Users\anfalear\.claude\projects\C--Users-anfalear-notascalculo-problemario\3bf94b73-1ff8-4772-856c-552321bbde0d.jsonl'
target = 'limvariasvariables.tex'
out_path = r'C:\Users\anfalear\notascalculo\problemario\limvariasvariables_ORIGINAL.tex'

found = False
with open(jsonl_path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        # Buscar en mensajes del tipo tool_result que contengan el texto del archivo
        msg = obj.get('message', obj)
        content = msg.get('content', '')
        if isinstance(content, list):
            for block in content:
                if isinstance(block, dict):
                    text = block.get('text', '') or block.get('content', '')
                    if isinstance(text, str) and target in text and '\\chapter{' in text and len(text) > 50000:
                        # Extraer el contenido LaTeX del bloque de texto
                        # El Read tool devuelve lineas con formato: "NNN\tCONTENIDO"
                        lines_out = []
                        for l in text.split('\n'):
                            # Formato: "  453\t\\end{myproof}"
                            m = re.match(r'^\s*\d+\t(.*)$', l)
                            if m:
                                lines_out.append(m.group(1) + '\n')
                        if len(lines_out) > 500:
                            with open(out_path, 'w', encoding='utf-8') as g:
                                g.writelines(lines_out)
                            print(f'Guardado: {len(lines_out)} lineas en {out_path}')
                            found = True
                            break
            if found:
                break
        elif isinstance(content, str) and target in content and '\\chapter{' in content and len(content) > 50000:
            lines_out = []
            for l in content.split('\n'):
                m = re.match(r'^\s*\d+\t(.*)$', l)
                if m:
                    lines_out.append(m.group(1) + '\n')
            if len(lines_out) > 500:
                with open(out_path, 'w', encoding='utf-8') as g:
                    g.writelines(lines_out)
                print(f'Guardado: {len(lines_out)} lineas en {out_path}')
                found = True
                break

if not found:
    print('No se encontro el contenido del archivo en el JSONL.')
    print('Buscando fragmentos parciales...')
    count = 0
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            if 'Derivadas parciales de primer orden' in line:
                count += 1
    print(f'  Menciones de "Derivadas parciales de primer orden": {count}')
