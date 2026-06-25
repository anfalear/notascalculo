base = r'C:\Users\anfalear\notascalculo\problemario'

def read(fn):
    return open(fr'{base}\{fn}', encoding='utf-8').readlines()

def show_structure(fname):
    lines = read(fname)
    print(f'\n=== {fname}  ({len(lines)} lineas) ===')
    for i, l in enumerate(lines):
        s = l.strip()
        safe = s[:90].encode('ascii', 'replace').decode('ascii')
        if (s.startswith(r'\chapter') or s.startswith(r'\section') or
                s.startswith(r'\subsection') or s.startswith(r'\begin{prob') or
                s.startswith(r'\end{prob') or '% Cap.' in s or
                'Leccion' in s or 'Lecci' in safe):
            print(f'  [{i:4d}] {safe}')
    print(f'  Total lineas: {len(lines)}')

show_structure('apintdobles.tex')
show_structure('inttriples.tex')
show_structure('camposconservativos.tex')
show_structure('integraleslineacampos.tex')
show_structure('intsuperficies.tex')
