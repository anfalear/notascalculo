base = r'C:\Users\anfalear\notascalculo\problemario'

def read(fn):
    return open(fr'{base}\{fn}', encoding='utf-8').readlines()

def show(fname, indices):
    lines = read(fname)
    print(f'\n=== {fname}  ({len(lines)} lineas) ===')
    for i in indices:
        if i < len(lines):
            safe = lines[i].strip()[:80].encode('ascii', 'replace').decode('ascii')
            print(f'  [{i:4d}] {safe}')
        else:
            print(f'  [{i:4d}] FUERA DE RANGO')

show('planostangentes_ORIGINAL.tex', [2, 8, 18, 181, 341, 345, 349, 353, 357, 361, 363, 365])
show('gradientes_ORIGINAL.tex',      [0, 35, 498, 770, 773, 813, 815, 869, 872, 950, 951])
show('multiplicadoresintdobles_ORIGINAL.tex', [0, 10, 232, 426, 428, 435, 437, 439, 441, 463, 467])
show('apintdobles_ORIGINAL.tex',     [0, 2, 18, 221, 301, 344, 376])
