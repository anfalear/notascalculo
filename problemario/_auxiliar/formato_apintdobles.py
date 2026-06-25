# -*- coding: utf-8 -*-
with open('apintdobles.tex', 'r', encoding='utf-8') as f:
    content = f.read()

results = []

def R(content, old, new, label):
    if old in content:
        results.append(f'OK  {label}')
        return content.replace(old, new, 1)
    else:
        results.append(f'MISS {label}')
        return content

# ==== EJEMPLO 1: título + Paso 1-3 + \boxed{} ====
content = R(content,
    '\\begin{example}\nCalcular $\\displaystyle\\iint_R',
    '\\begin{example}[Integral doble sobre un rect\\\'angulo]\nCalcular $\\displaystyle\\iint_R',
    'Ex1 título')

content = R(content,
    'Usamos el orden $dy\\,dx$ (primero en $y$):\n',
    '\\textbf{Paso 1. Integral iterada.} Usamos el orden $dy\\,dx$:\n',
    'Ex1 Paso 1')

content = R(content,
    'Interior:\n\\[\n\\int_0^2 (x^2 y + y^2)',
    '\\textbf{Paso 2. Integral interior.}\n\\[\n\\int_0^2 (x^2 y + y^2)',
    'Ex1 Paso 2')

content = R(content,
    'Luego\n\\[\n\\int_0^1 \\left(2x^2',
    '\\textbf{Paso 3. Integral exterior.}\n\\[\n\\int_0^1 \\left(2x^2',
    'Ex1 Paso 3')

content = R(content,
    'Por tanto, $\\displaystyle\\iint_R (x^2 y + y^2)\\,dA = \\frac{10}{3}$.',
    '$\\displaystyle\\boxed{\\iint_R (x^2 y + y^2)\\,dA = \\tfrac{10}{3}}$.',
    'Ex1 boxed')

# ==== EJEMPLO 2: Paso 1-3 + \boxed{} ====
content = R(content,
    'La región es tipo I: para cada $x\\in[0,1]$, $y$ varía entre $x^2$ y $x$. Por tanto,\n',
    '\\textbf{Paso 1. Región e integral iterada.} La región es tipo I: para cada $x\\in[0,1]$, $y$ varía entre $x^2$ y $x$. Por tanto,\n',
    'Ex2 Paso 1')

content = R(content,
    'Interior:\n\\[\n\\int_{x^2}^{x} xy',
    '\\textbf{Paso 2. Integral interior.}\n\\[\n\\int_{x^2}^{x} xy',
    'Ex2 Paso 2')

content = R(content,
    'Luego\n\\[\n\\int_0^1 \\left(\\frac{x^3}{2}',
    '\\textbf{Paso 3. Integral exterior.}\n\\[\n\\int_0^1 \\left(\\frac{x^3}{2}',
    'Ex2 Paso 3')

content = R(content,
    'Por tanto, $\\displaystyle\\iint_D xy\\,dA = \\frac{1}{24}$.',
    '$\\displaystyle\\boxed{\\iint_D xy\\,dA = \\tfrac{1}{24}}$.',
    'Ex2 boxed')

# ==== EJEMPLO 3: Paso 1-4 + \boxed{} ====
content = R(content,
    'Los puntos de intersección de $y^2$ y $y+2$ satisfacen',
    '\\textbf{Paso 1. Identificar la región.} Los puntos de intersección de $y^2$ y $y+2$ satisfacen',
    'Ex3 Paso 1')

content = R(content,
    'Entonces\n\\[\n\\iint_D (x+y)\\,dA = \\int_{-1}^{2}',
    '\\textbf{Paso 2. Integral iterada.}\n\\[\n\\iint_D (x+y)\\,dA = \\int_{-1}^{2}',
    'Ex3 Paso 2')

content = R(content,
    'Interior:\n\\[\n\\int_{y^2}^{y+2} (x+y)',
    '\\textbf{Paso 3. Integral interior.}\n\\[\n\\int_{y^2}^{y+2} (x+y)',
    'Ex3 Paso 3')

content = R(content,
    'Ahora integramos respecto a $y$:\n',
    '\\textbf{Paso 4. Integral exterior.}\n',
    'Ex3 Paso 4')

content = R(content,
    'Por tanto, $\\displaystyle\\iint_D (x+y)\\,dA = \\frac{189}{20}$.',
    '$\\displaystyle\\boxed{\\iint_D (x+y)\\,dA = \\tfrac{189}{20}}$.',
    'Ex3 boxed')

# ==== EJEMPLO 4: Paso 1-3 ====
content = R(content,
    'El volumen está dado por\n',
    '\\textbf{Paso 1. Plantear el volumen.} El volumen está dado por\n',
    'Ex4 Paso 1')

content = R(content,
    'Primero integramos en \\(y\\):\n',
    '\\textbf{Paso 2. Integral interior en $y$.}\n',
    'Ex4 Paso 2')

content = R(content,
    'Luego integramos en \\(x\\):\n',
    '\\textbf{Paso 3. Integral exterior en $x$.}\n',
    'Ex4 Paso 3')

# ==== EJEMPLO 5: Paso 1 ====
content = R(content,
    'El área es \\(A=\\iint_D 1\\,dA\\).',
    '\\textbf{Paso 1. Plantear e integrar el área.} El área es \\(A=\\iint_D 1\\,dA\\).',
    'Ex5 Paso 1')

# ==== EJEMPLO 6: Paso 1-3 ====
content = R(content,
    'Calculamos la masa:\n',
    '\\textbf{Paso 1. Masa.}\n',
    'Ex6 Paso 1')

content = R(content,
    'Ahora los momentos:\n',
    '\\textbf{Paso 2. Momentos estáticos.}\n',
    'Ex6 Paso 2')

content = R(content,
    'Entonces\n\\[\n\\bar{x}=\\frac{M_y}{m}',
    '\\textbf{Paso 3. Centro de masa.}\n\\[\n\\bar{x}=\\frac{M_y}{m}',
    'Ex6 Paso 3')

# ==== EJEMPLO 7: Paso 1-4 ====
content = R(content,
    'Por definición,\n\\[\nI_x',
    '\\textbf{Paso 1. Plantear las integrales.}\n\\[\nI_x',
    'Ex7 Paso 1')

content = R(content,
    'Calculamos \\(I_x\\):\n',
    '\\textbf{Paso 2. Calcular $I_x$.}\n',
    'Ex7 Paso 2')

content = R(content,
    'Calculamos \\(I_y\\):\n',
    '\\textbf{Paso 3. Calcular $I_y$.}\n',
    'Ex7 Paso 3')

content = R(content,
    'Entonces\n\\[\nI_0 = I_x+I_y',
    '\\textbf{Paso 4. Momento polar.}\n\\[\nI_0 = I_x+I_y',
    'Ex7 Paso 4')

# ==== EJEMPLO 8: Paso 1 ====
content = R(content,
    'En polares, \\(D: 0\\le r\\le 1',
    '\\textbf{Paso 1. Conversión a polares y evaluación.} En polares, \\(D: 0\\le r\\le 1',
    'Ex8 Paso 1')

# ==== EJEMPLO 9: Paso 1-3 ====
content = R(content,
    'El área está dada por \\(\\iint_D 1\\,dA\\)',
    '\\textbf{Paso 1. Plantear el área.} El área está dada por \\(\\iint_D 1\\,dA\\)',
    'Ex9 Paso 1')

content = R(content,
    'Desarrollamos:\n',
    '\\textbf{Paso 2. Simplificar $(1+\\cos\\theta)^2$.}\n',
    'Ex9 Paso 2')

content = R(content,
    'Integrando:\n',
    '\\textbf{Paso 3. Integrar.}\n',
    'Ex9 Paso 3')

# ==== EJEMPLO 10: Paso 1-3 ====
content = R(content,
    'Tenemos \\(f(x,y)=x^2+y^2\\), luego\n',
    '\\textbf{Paso 1. Derivadas parciales.} Tenemos \\(f(x,y)=x^2+y^2\\), luego\n',
    'Ex10 Paso 1')

content = R(content,
    'El área es\n\\[\nA(S)=\\iint_D \\sqrt{1+4x^2+4y^2}',
    '\\textbf{Paso 2. Área de la superficie.}\n\\[\nA(S)=\\iint_D \\sqrt{1+4x^2+4y^2}',
    'Ex10 Paso 2')

content = R(content,
    'Pasamos a polares: \\(D:0\\le r\\le1',
    '\\textbf{Paso 3. Coordenadas polares.} Pasamos a polares: \\(D:0\\le r\\le1',
    'Ex10 Paso 3')

with open('apintdobles.tex', 'w', encoding='utf-8') as f:
    f.write(content)

ok = sum(1 for r in results if r.startswith('OK'))
miss = sum(1 for r in results if r.startswith('MISS'))
for r in results:
    print(r)
print(f'\n{ok} OK, {miss} missed')
