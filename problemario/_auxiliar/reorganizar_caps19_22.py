"""
Item 11 - Decision B: Reorganizacion de Caps. 19-22 y preparacion de Cap. 32.

Cap. 19 (limvariasvariables.tex) ya fue escrito en ejecucion previa.
Este script escribe los 4 archivos restantes.

Fuentes:
  limvariasvariables_ORIGINAL.tex  -> fuente para datos de Cap. 20
  planostangentes.tex              -> Cap. 20 (plano tangente) y Cap. 21 (regla cadena)
  gradientes.tex                   -> Cap. 21 (gradiente) y Cap. 22 (extremos)
  multiplicadoresintdobles.tex     -> Cap. 22 (Lagrange) y Cap. 32 (int. dobles)
  apintdobles.tex                  -> Cap. 32 (recibe int. dobles al inicio)

Indices clave (0-based):

limvariasvariables_ORIGINAL.tex:
  chapter       7    -> cap.19 title (ya no se usa, solo para verificar)
  sec2 start    459  -> \\section{Derivadas parciales...}
  sec*prob      863  -> \\section*{Problemas propuestos}
  subsec*limite 865  -> \\subsection*{Limite y continuidad}  (se omite)
  subsec*deriv  921  -> \\subsection*{Derivadas parciales}
  bank section  1006 -> \\section{Problemas propuestos}

planostangentes.tex:
  outer sec     2    -> descartado (wrapper sin capitulo)
  subsec plano  18   -> Cap. 20, se promueve a \\section
  subsec regla  181  -> Cap. 21, se promueve a \\section
  subsec concl  341  -> descartado
  begin{prob}   345,349,353,357,361
  end{prob}     347,351,355,359,363
  Probs 1-2 (345-351) -> Cap. 20
  Probs 3-5 (353-363) -> Cap. 21

gradientes.tex:
  chapter       0
  sec1 grad     35   -> Cap. 21
  sec2 extremos 498  -> Cap. 22
  sec Problemas 770
  end{prob} p4  813  -> ultimo prob Cap. 21
  begin{prob}5  815  -> primer prob Cap. 22
  end{prob} p10 869
  Cap.20 comment 872
  Cap.21 comment 951

multiplicadoresintdobles.tex:
  chapter       0
  sec1 Lagrange 10   -> Cap. 22
  sec2 IntDobles 232 -> Cap. 32
  sec Problemas  426
  end{prob}p2   439  -> ultimo prob Cap. 22 (Hessiano)
  begin{prob}3  441  -> primer prob Cap. 32 (int. dobles)
  end{prob}p5   463  -> ultimo prob Cap. 32
  Cap.22 comment 467
"""

import re

base = r'C:\Users\anfalear\notascalculo\problemario'

def read_lines(fname):
    with open(fr'{base}\{fname}', 'r', encoding='utf-8') as f:
        return f.readlines()

def write_lines(fname, lines):
    with open(fr'{base}\{fname}', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print(f'  OK  {fname}  ({len(lines)} lineas)')

def promote_headers(lines):
    r"""Promueve UN nivel: \subsubsection -> \subsection, \subsection -> \section.
    Cada linea se promueve exactamente un nivel (sin doble promocion)."""
    result = []
    for line in lines:
        new = re.sub(r'^(\s*)\\subsubsection', r'\1\\subsection', line)
        if new == line:
            # No era subsubsection: intentar promover subsection -> section
            new = re.sub(r'^(\s*)\\subsection', r'\1\\section', line)
        result.append(new)
    return result

# Leer TODOS los archivos fuente (versiones originales recuperadas del JSONL)
# ANTES de escribir cualquier salida, para evitar leer archivos ya modificados.
limvar = read_lines('limvariasvariables_ORIGINAL.tex')
planos = read_lines('planostangentes_ORIGINAL.tex')
grad   = read_lines('gradientes_ORIGINAL.tex')
mult   = read_lines('multiplicadoresintdobles_ORIGINAL.tex')
apint  = read_lines('apintdobles.tex')   # apintdobles ya esta correcto en disco

print(f'Fuentes leidas: limvar={len(limvar)}, planos={len(planos)}, grad={len(grad)}, mult={len(mult)}, apint={len(apint)}')

# ============================================================
# VERIFICACION de indices criticos
# ============================================================
assert r'\section{Derivadas parciales de primer orden' in limvar[459], \
    f'ERROR: limvar[459] = {limvar[459]!r}'
assert r'\section*{Problemas propuestos}' in limvar[863], \
    f'ERROR: limvar[863] = {limvar[863]!r}'
assert r'\subsection*{Derivadas parciales}' in limvar[921], \
    f'ERROR: limvar[921] = {limvar[921]!r}'
assert r'\section{Problemas propuestos}' in limvar[1006], \
    f'ERROR: limvar[1006] = {limvar[1006]!r}'
assert r'\subsection{Plano tangente' in planos[18], \
    f'ERROR: planos[18] = {planos[18]!r}'
assert r'\subsection{Regla de la cadena' in planos[181], \
    f'ERROR: planos[181] = {planos[181]!r}'
assert r'\section{Gradiente y derivada' in grad[35], \
    f'ERROR: grad[35] = {grad[35]!r}'
assert r'\section{Valores extremos' in grad[498], \
    f'ERROR: grad[498] = {grad[498]!r}'
assert r'\section{Problemas Propuestos}' in grad[770], \
    f'ERROR: grad[770] = {grad[770]!r}'
assert r'\section{Optimizaci' in mult[10], \
    f'ERROR: mult[10] = {mult[10]!r}'
assert r'\section{Integrales dobles en coordenadas rect' in mult[232], \
    f'ERROR: mult[232] = {mult[232]!r}'
assert r'\section{Problemas propuestos}' in mult[426], \
    f'ERROR: mult[426] = {mult[426]!r}'
print('Indices verificados OK.')

# ============================================================
# ARCHIVOS YA CORRECTOS EN DISCO -- solo verificar y saltar
# ============================================================
def verify_skip(fname, marker, label):
    lines = read_lines(fname)
    ok = any(marker in l for l in lines[:10])
    status = 'SKIP-OK' if ok else 'SKIP-ERROR'
    print(f'  {status}  {fname}  ({len(lines)} lineas)  [{label}]')
    return ok

verify_skip('limvariasvariables.tex',       'continuidad en', 'Cap.19 OK')
verify_skip('multiplicadoresintdobles.tex', r'\chapter{Optimizaci', 'Cap.22 OK')
verify_skip('apintdobles.tex',              r'\section{Integrales dobles en coordenadas rect', 'Cap.32 OK')

# ============================================================
# CAP. 20 -- planostangentes.tex
# Contenido:
#   Cabecera nueva del capitulo
#   limvar[455:863]   -- seccion derivadas parciales (con CONCLUSION y comentario PROBLEMAS)
#   limvar[922:1006]  -- 9 problemas de derivadas parciales
#   planos[18:181]    -- subseccion plano tangente (promovida a section)
#   planos[345:352]   -- probs 1-2 (plano tangente + linealizacion)
#   grad[872:951]     -- banco Cap. 20
# ============================================================
print('Escribiendo Cap. 20 (planostangentes.tex)...')

cap20 = []
cap20 += [
    '% ============================================================\n',
    '% CAPITULO 20: DIFERENCIACION PARCIAL, PLANO TANGENTE Y DIFERENCIABILIDAD\n',
    '% ============================================================\n',
    '\n',
    '\\chapter{Diferenciaci\\u00f3n parcial, plano tangente y diferenciabilidad}\n',
    '\n',
]

# --- Sustituir la secuencia Unicode por el caracter directo ---
# (write_lines usa encoding=utf-8 asi que los caracteres directos son seguros)
cap20_header = [
    '% ============================================================\n',
    '% CAPITULO 20: DIFERENCIACION PARCIAL, PLANO TANGENTE Y DIFERENCIABILIDAD\n',
    '% ============================================================\n',
    '\n',
    '\\chapter{Diferenciación parcial, plano tangente y diferenciabilidad}\n',
    '\n',
]
cap20 = list(cap20_header)

# Seccion derivadas parciales de limvar: desde borde (455) hasta antes de \section*{Prob} (863)
# Incluye: comentario SECCION 1.4, la seccion con su contenido, CONCLUSION y comentario PROBLEMAS
cap20 += limvar[455:863]

# Problemas de derivadas parciales (limvar 922-1005): 9 probs
# Se omite el indice 921 (\subsection*{Derivadas parciales} — sustituido por encabezado propio)
cap20 += ['\n', '\\section*{Problemas: derivadas parciales}\n', '\n']
cap20 += limvar[922:1006]

cap20 += ['\n']

# Subseccion plano tangente de planos (18-180), promovida:
#   \subsection{Plano tangente...} -> \section{...}
#   \subsubsection{...}            -> \subsection{...}
cap20 += promote_headers(planos[18:181])

# Probs plano tangente: probs 1-2 de planos (indices 345-351)
cap20 += ['\n', '\\section*{Problemas propuestos}\n', '\n']
cap20 += planos[345:352]

cap20 += ['\n']

# Banco Cap. 20 de gradientes (872-950)
cap20 += grad[872:951]

write_lines('planostangentes.tex', cap20)

# ============================================================
# CAP. 21 -- gradientes.tex
# Contenido:
#   Cabecera nueva del capitulo
#   planos[181:341]   -- subseccion regla de cadena (promovida a section)
#   planos[353:364]   -- probs 3-5 (regla cadena + derivacion implicita)
#   grad[35:498]      -- seccion gradiente y derivada direccional (sin cambios)
#   grad[770:814]     -- \section{Problemas Propuestos} + probs 1-4
#   grad[951:]        -- banco Cap. 21
# ============================================================
print('Escribiendo Cap. 21 (gradientes.tex)...')

cap21 = [
    '% ============================================================\n',
    '% CAPITULO 21: REGLA DE LA CADENA, DERIVADA DIRECCIONAL Y GRADIENTE\n',
    '% ============================================================\n',
    '\n',
    '\\chapter{Regla de la cadena, derivada direccional y gradiente}\n',
    '\n',
]

# Subseccion regla de cadena de planos (181-340), promovida:
#   \subsection{Regla de la cadena...}        -> \section{...}
#   \subsubsection{Caso 1/2, Derivacion impl} -> \subsection{...}
cap21 += promote_headers(planos[181:341])

# Probs regla de cadena y derivacion implicita (probs 3-5 de planos: 353-363)
cap21 += ['\n', '\\section*{Problemas: regla de la cadena y derivación implícita}\n', '\n']
cap21 += planos[353:364]

cap21 += ['\n']

# Seccion gradiente y derivada direccional de grad (35-497): sin cambios de nivel
cap21 += grad[35:498]

# \section{Problemas Propuestos} + probs 1-4 (gradiente/deriv. dir.) de grad
cap21 += ['\n']
cap21 += grad[770:814]
cap21 += [grad[814]]   # blank despues del ultimo \end{prob}

cap21 += ['\n']

# Banco Cap. 21 (951-fin de grad)
cap21 += grad[951:]

write_lines('gradientes.tex', cap21)

# ============================================================
# CAP. 22 y CAP. 32 -- YA ESCRITOS CORRECTAMENTE (no usan promote_headers)
# No se regeneran.
# ============================================================

print('  SKIP  multiplicadoresintdobles.tex  (Cap.22 ya correcto en disco)')
print('  SKIP  apintdobles.tex              (Cap.32 ya correcto en disco)')

print('\nReorganizacion completada.')
print('El maestro anfalearNotasCalculo.tex NO requiere cambios (inputs iguales).')
print('Proximo item: 12 -- Caps. 32-34, renombrar encabezados "Leccion X.Y".')
