# -*- coding: utf-8 -*-
"""
Item 12 — Reorganizacion Caps. 32-34
1. Renombrar \chapter en apintdobles.tex (quitar "Leccion 2.3:")
2. Renombrar \chapter en inttriples.tex (quitar "Leccion 3.1:", titulo corto)
3. Corregir comentario de banco en inttriples.tex: Cap. 32 -> Cap. 33
4. Crear cap34_integrales_vectoriales.tex fusionando los 3 archivos
5. Actualizar maestro: 3 \input separados -> 1 \input{cap34_...}
"""
base = r'C:\Users\anfalear\notascalculo\problemario'

def read_lines(fname):
    with open(fr'{base}\{fname}', 'r', encoding='utf-8') as f:
        return f.readlines()

def write_lines(fname, lines):
    with open(fr'{base}\{fname}', 'w', encoding='utf-8', newline='') as f:
        f.writelines(lines)
    print(f'OK: {fname} ({len(lines)} lineas)')

def content_after_chapter(lines):
    """Devuelve contenido del archivo omitiendo la primera linea \\chapter{} y su \\label{}."""
    i = 0
    while i < len(lines) and not lines[i].strip().startswith('\\chapter'):
        i += 1
    i += 1  # saltar la linea \chapter
    while i < len(lines) and lines[i].strip().startswith('\\label'):
        i += 1
    return lines[i:]

# ── 1. Renombrar apintdobles.tex ──────────────────────────────────────────────
lines = read_lines('apintdobles.tex')
found = False
for i, l in enumerate(lines):
    if '\\chapter' in l and 'Lecci' in l and '2.3' in l:
        lines[i] = '\\chapter{Aplicaciones de la integral doble e integrales dobles en coordenadas polares}\n'
        print(f'  apintdobles: chapter renombrado (linea {i})')
        found = True
        break
if not found:
    print('ERROR: no se encontro chapter de apintdobles')
else:
    write_lines('apintdobles.tex', lines)

# ── 2. Renombrar inttriples.tex + comentario de banco ────────────────────────
lines = read_lines('inttriples.tex')
cap_ok = False
banco_ok = False
for i, l in enumerate(lines):
    if '\\chapter' in l and 'Lecci' in l and '3.1' in l:
        lines[i] = '\\chapter{Integrales triples}\n'
        print(f'  inttriples: chapter renombrado (linea {i})')
        cap_ok = True
    if l.strip().startswith('%') and 'Cap. 32' in l and 'Integrales' in l:
        lines[i] = l.replace('Cap. 32', 'Cap. 33')
        print(f'  inttriples: comentario banco actualizado (linea {i})')
        banco_ok = True
if not cap_ok:
    print('ERROR: no se encontro chapter de inttriples')
if not banco_ok:
    print('AVISO: no se encontro comentario "Cap. 32" en inttriples')
write_lines('inttriples.tex', lines)

# ── 3. Crear cap34_integrales_vectoriales.tex ─────────────────────────────────
campos = read_lines('camposconservativos.tex')
linea  = read_lines('integraleslineacampos.tex')
intsup = read_lines('intsuperficies.tex')

# Mostrar indices para verificacion
for nombre, arr in [('camposconservativos', campos),
                     ('integraleslineacampos', linea),
                     ('intsuperficies', intsup)]:
    for idx, l in enumerate(arr):
        if l.strip().startswith('\\chapter'):
            print(f'  {nombre}: \\chapter en linea {idx}')
            break

body_campos = content_after_chapter(campos)
body_linea  = content_after_chapter(linea)
body_intsup = content_after_chapter(intsup)

print(f'  Lineas aportadas: campos={len(body_campos)}, linea={len(body_linea)}, intsup={len(body_intsup)}')

cap34 = []
cap34.append('\\chapter{Campos vectoriales, integrales de línea y de superficie}\n')
cap34.append('\n')
cap34.extend(body_campos)
cap34.append('\n')
cap34.extend(body_linea)
cap34.append('\n')
cap34.extend(body_intsup)

write_lines('cap34_integrales_vectoriales.tex', cap34)

# ── 4. Actualizar maestro ─────────────────────────────────────────────────────
maestro = read_lines('anfalearNotasCalculo.tex')
new_maestro = []
i = 0
reemplazado = False
while i < len(maestro):
    l = maestro[i]
    if '\\input{camposconservativos}' in l:
        new_maestro.append('\\input{cap34_integrales_vectoriales}\n')
        reemplazado = True
        i += 1
        # Saltar las dos lineas siguientes: integraleslineacampos e intsuperficies
        while i < len(maestro) and (
            '\\input{integraleslineacampos}' in maestro[i] or
            '\\input{intsuperficies}' in maestro[i]
        ):
            print(f'  maestro: eliminado "{maestro[i].strip()}"')
            i += 1
    else:
        new_maestro.append(l)
        i += 1

if reemplazado:
    write_lines('anfalearNotasCalculo.tex', new_maestro)
    print('  maestro: 3 \\input reemplazados por 1 \\input{cap34_integrales_vectoriales}')
else:
    print('ERROR: no se encontro \\input{camposconservativos} en el maestro')

print()
print('ITEM 12 COMPLETO')
