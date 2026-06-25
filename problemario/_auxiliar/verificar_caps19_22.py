"""
Verifica la estructura de los 5 archivos del item 11.
Comprueba: chapter correcto, secciones presentes/ausentes,
           presencia/ausencia de contenido que no deberia estar.
"""
base = r'C:\Users\anfalear\notascalculo\problemario'

def read_lines(fname):
    with open(fr'{base}\{fname}', 'r', encoding='utf-8') as f:
        return f.readlines()

def grep(lines, pattern):
    return [(i, l.rstrip()) for i, l in enumerate(lines) if pattern in l]

def check(fname, must_have, must_not_have):
    lines = read_lines(fname)
    print(f'\n=== {fname}  ({len(lines)} lineas) ===')
    ok = True
    for pattern in must_have:
        hits = grep(lines, pattern)
        if hits:
            for i, l in hits[:2]:
                safe = l[:80].encode('ascii', 'replace').decode('ascii')
                print(f'  PRES [{i:4d}] {safe}')
        else:
            print(f'  FALTA: {pattern!r}')
            ok = False
    for pattern in must_not_have:
        hits = grep(lines, pattern)
        if hits:
            print(f'  ERROR (no debe estar): {pattern!r}')
            for i, l in hits[:2]:
                safe = l[:80].encode('ascii', 'replace').decode('ascii')
                print(f'         [{i:4d}] {safe}')
            ok = False
    if ok:
        print('  --> OK')
    return ok

all_ok = True

all_ok &= check(
    'limvariasvariables.tex',
    must_have=[
        r'\chapter{L',                              # tiene chapter
        'continuidad en',                            # titulo correcto
        r'\section{Límite y continuidad',            # seccion 1 presente
        r'\section*{Problemas propuestos}',          # bloque de problemas
        r'\section{Problemas propuestos}',           # banco
        'Cap. 19',                                   # banco etiquetado
    ],
    must_not_have=[
        r'\section{Derivadas parciales de primer',  # sec.2 NO debe estar
        r'\subsection*{Derivadas parciales}',        # subseccion NO debe estar
    ]
)

all_ok &= check(
    'planostangentes.tex',
    must_have=[
        r'\chapter{Diferenciaci',                       # tiene chapter nuevo
        r'\section{Derivadas parciales de primer',      # sec. derivadas parciales
        r'\section*{Problemas: derivadas parciales}',
        r'\section{Plano tangente, aproximaci',         # sec. plano tangente (promovida desde subsection)
        r'\subsection{Plano tangente}',                 # subsubsection promovido a subsection OK
        r'\section*{Problemas propuestos}',
        'Cap. 20',                                      # banco etiquetado
    ],
    must_not_have=[
        # El TITULO COMPLETO de la antigua subsection NO debe quedar como subsection
        r'\subsection{Plano tangente, aproximaci',      # fue promovida a \section
        r'\subsection{Regla de la cadena y derivaci',   # regla cadena NO en cap 20
        r'\chapter{L',                                  # NO el capitulo viejo
    ]
)

all_ok &= check(
    'gradientes.tex',
    must_have=[
        r'\chapter{Regla de la cadena',                 # tiene chapter nuevo
        r'\section{Regla de la cadena y derivaci',      # promovida desde subsection
        r'\subsection{Regla de la cadena (Caso 1',      # subsubsection promovido a subsection OK
        r'\subsection{Derivaci',                        # derivacion implicita como subsec OK
        r'\section*{Problemas: regla de la cadena',
        r'\section{Gradiente y derivada',               # sec. gradiente intacta
        r'\section{Problemas Propuestos}',
        'Cap. 21',                                      # banco etiquetado
    ],
    must_not_have=[
        r'\section{Valores extremos',                   # extremos NO en cap 21
        r'\chapter{Derivada Direccional',               # NO titulo viejo
        # El TITULO COMPLETO de la antigua subsection NO debe quedar como subsection
        r'\subsection{Regla de la cadena y derivaci',   # fue promovida a \section
        'Cap. 20',                                      # banco cap 20 NO aqui
    ]
)

all_ok &= check(
    'multiplicadoresintdobles.tex',
    must_have=[
        r'\chapter{Optimizaci',                     # tiene chapter nuevo
        r'\section{Valores extremos',               # sec. extremos
        r'\section{Optimizaci',                     # sec. Lagrange
        r'\section*{Problemas propuestos}',         # bloque problemas
        'Extremos absolutos',                       # probs extremos de grad
        'Multiplicadores de Lagrange',              # probs Lagrange de mult
        'Cap. 22',                                  # banco etiquetado
    ],
    must_not_have=[
        r'\section{Integrales dobles en coordenadas rect',  # int. dobles NO aqui
        r'\chapter{Lecci',                          # NO el titulo viejo
        'Integrales dobles sobre rect',             # probs int. dobles NO aqui
    ]
)

all_ok &= check(
    'apintdobles.tex',
    must_have=[
        r'\chapter{Lecci',                          # chapter (se renombra en item 12)
        r'\section{Integrales dobles en coordenadas rect', # nueva seccion al inicio
        'Integrales dobles sobre rect',             # probs int. dobles ahora aqui
        r'\section{',                               # secciones originales
        r'\section{Área, volumen',                  # primera seccion original
        r'\section{Integrales dobles en coordenadas pol',  # polar
    ],
    must_not_have=[
        'En la lección anterior construimos',  # intro vieja eliminada
    ]
)

print()
if all_ok:
    print('VERIFICACION GLOBAL: TODOS LOS ARCHIVOS OK')
else:
    print('VERIFICACION GLOBAL: HAY PROBLEMAS - revisar arriba')
