base = r'C:\Users\anfalear\notascalculo\problemario'
lines = open(fr'{base}\anfalearNotasCalculo.tex', encoding='utf-8').readlines()
print(f'Total lineas: {len(lines)}')
for i, l in enumerate(lines):
    s = l.strip()
    safe = s[:100].encode('ascii', 'replace').decode('ascii')
    if (s.startswith(r'\part') or s.startswith(r'\chapter') or
            s.startswith(r'\input') or s.startswith(r'\include') or
            s.startswith('%% PARTE') or s.startswith('% CAP') or
            s.startswith(r'\begin{document}') or s.startswith(r'\end{document}')):
        print(f'  [{i:3d}] {safe}')
