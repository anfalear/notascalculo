base = r'C:\Users\anfalear\notascalculo\problemario'

def read_lines(fname):
    with open(fr'{base}\{fname}', 'r', encoding='utf-8') as f:
        return f.readlines()

def find_line(lines, pattern, start=0):
    for i in range(start, len(lines)):
        if pattern in lines[i]:
            return i
    return -1

limvar = read_lines('limvariasvariables.tex')
planos = read_lines('planostangentes.tex')
grad   = read_lines('gradientes.tex')
mult   = read_lines('multiplicadoresintdobles.tex')
apint  = read_lines('apintdobles.tex')

print('=== limvariasvariables.tex ===')
i_chap  = find_line(limvar, r'\chapter{')
i_sec2c = find_line(limvar, 'DERIVADAS PARCIALES DE PRIMER ORDEN')
i_sec2  = find_line(limvar, r'\section{Derivadas parciales de primer')
i_sprob = find_line(limvar, r'\section*{Problemas propuestos}')
i_slim  = find_line(limvar, r'\subsection*{Límite y continuidad}')
i_sder  = find_line(limvar, r'\subsection*{Derivadas parciales}')
i_bank  = find_line(limvar, r'\section{Problemas propuestos}')
print(f'  chapter:            {i_chap}  -> {limvar[i_chap].strip()!r}')
print(f'  sec2 comment:       {i_sec2c}')
print(f'  sec2 start:         {i_sec2}  -> {limvar[i_sec2].strip()!r}')
print(f'  section*{{Prob}}:   {i_sprob} -> {limvar[i_sprob].strip()!r}')
print(f'  subsec* limite:     {i_slim}  -> {limvar[i_slim].strip()!r}')
print(f'  subsec* derivadas:  {i_sder}  -> {limvar[i_sder].strip()!r}')
print(f'  bank section:       {i_bank}  -> {limvar[i_bank].strip()!r}')
# last \end{prob} in limits block (between i_slim and i_sder)
for i in range(i_sder - 1, i_slim, -1):
    if r'\end{prob}' in limvar[i]:
        print(f'  last lim prob:      {i}  -> {limvar[i].strip()!r}')
        break
# last \end{prob} in derivadas block (between i_sder and i_bank)
for i in range(i_bank - 1, i_sder, -1):
    if r'\end{prob}' in limvar[i]:
        print(f'  last der prob:      {i}  -> {limvar[i].strip()!r}')
        break
# line just before sec2 comment
print(f'  line before sec2c:  {i_sec2c-1} -> {limvar[i_sec2c-1].strip()!r}')

print()
print('=== planostangentes.tex ===')
for i, line in enumerate(planos):
    s = line.strip()
    if s.startswith(r'\section') or s.startswith(r'\subsection') or s.startswith(r'\subsubsection'):
        print(f'  {i}: {s!r}')
print('  -- probs --')
for i, line in enumerate(planos):
    s = line.strip()
    if r'\begin{prob}' in s or r'\end{prob}' in s:
        print(f'  {i}: {s!r}')

print()
print('=== gradientes.tex ===')
i_gchap  = find_line(grad, r'\chapter{')
i_gsec1  = find_line(grad, r'\section{Gradiente y derivada')
i_gsec2  = find_line(grad, r'\section{Valores extremos')
i_gsprob = find_line(grad, r'\section{Problemas Propuestos}')
i_gcap20 = find_line(grad, 'Cap. 20')
i_gcap21 = find_line(grad, 'Cap. 21')
print(f'  chapter:            {i_gchap}  -> {grad[i_gchap].strip()!r}')
print(f'  sec1 gradient:      {i_gsec1}  -> {grad[i_gsec1].strip()!r}')
print(f'  sec2 valores ext:   {i_gsec2}  -> {grad[i_gsec2].strip()!r}')
print(f'  section Prob:       {i_gsprob} -> {grad[i_gsprob].strip()!r}')
print(f'  Cap.20 comment:     {i_gcap20} -> {grad[i_gcap20].strip()!r}')
print(f'  Cap.21 comment:     {i_gcap21} -> {grad[i_gcap21].strip()!r}')
# problems in the Problemas Propuestos section
print('  -- probs in Problemas Propuestos section --')
for i in range(i_gsprob, min(i_gcap20, len(grad))):
    s = grad[i].strip()
    if r'\begin{prob}' in s or r'\end{prob}' in s:
        print(f'  {i}: {s!r}')
# line right before Cap.20 comment
print(f'  line before cap20:  {i_gcap20-1} -> {grad[i_gcap20-1].strip()!r}')
print(f'  line before cap21:  {i_gcap21-1} -> {grad[i_gcap21-1].strip()!r}')

print()
print('=== multiplicadoresintdobles.tex ===')
i_mchap  = find_line(mult, r'\chapter{')
i_msec1  = find_line(mult, r'\section{Optimización restringida')
i_msec2  = find_line(mult, r'\section{Integrales dobles en coordenadas rect')
i_msprob = find_line(mult, r'\section{Problemas propuestos}')
i_mcap22 = find_line(mult, 'Cap. 22')
print(f'  chapter:            {i_mchap}  -> {mult[i_mchap].strip()!r}')
print(f'  sec1 Lagrange:      {i_msec1}  -> {mult[i_msec1].strip()!r}')
print(f'  sec2 IntDobles:     {i_msec2}  -> {mult[i_msec2].strip()!r}')
print(f'  section Prob:       {i_msprob} -> {mult[i_msprob].strip()!r}')
print(f'  Cap.22 comment:     {i_mcap22} -> {mult[i_mcap22].strip()!r}')
# end of sec1 Lagrange (last line before sec2)
print(f'  line before sec2:   {i_msec2-1} -> {mult[i_msec2-1].strip()!r}')
# probs in Problemas section
print('  -- probs in Problemas section --')
for i in range(i_msprob, i_mcap22):
    s = mult[i].strip()
    if r'\begin{prob}' in s or r'\end{prob}' in s:
        print(f'  {i}: {s!r}')

print()
print('=== apintdobles.tex ===')
for i, line in enumerate(apint[:30]):
    print(f'  {i}: {line.rstrip()!r}')
