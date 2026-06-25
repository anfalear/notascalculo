# -*- coding: utf-8 -*-
with open('inttriples.tex', 'r', encoding='utf-8') as f:
    content = f.read()

results = []

def R(content, old, new, label):
    if old in content:
        results.append(f'OK  {label}')
        return content.replace(old, new, 1)
    else:
        results.append(f'MISS {label}')
        return content

# ==== EJEMPLO 2: Integral de una función sobre el tetraedro ====
content = R(content,
    'Usamos el mismo orden y los mismos límites. La integral es\n',
    '\\textbf{Paso 1. Plantear la integral.} Usamos el mismo orden y los mismos límites. La integral es\n',
    'Ex2 Paso 1')

content = R(content,
    'Primero integramos respecto a \\(z\\):\n',
    '\\textbf{Paso 2. Integrar en $z$.}\n',
    'Ex2 Paso 2')

content = R(content,
    'Para la integral interior, fijamos \\(x\\) y hacemos el cambio \\(u = x+y\\).',
    '\\textbf{Paso 3. Integral interior (cambio $u=x+y$).}',
    'Ex2 Paso 3')

content = R(content,
    'Ahora integramos respecto a \\(x\\):\n',
    '\\textbf{Paso 4. Integrar en $x$.}\n',
    'Ex2 Paso 4')

# ==== EJEMPLO 3: Volumen bajo paraboloide ====
content = R(content,
    'El sólido se proyecta sobre el cuadrado \\(R = [0,1]\\times[0,1]\\).',
    '\\textbf{Paso 1. Plantear la integral triple.} El sólido se proyecta sobre el cuadrado \\(R = [0,1]\\times[0,1]\\).',
    'Ex3 Paso 1')

content = R(content,
    'Integramos en \\(y\\):\n',
    '\\textbf{Paso 2. Integrar en $y$.}\n',
    'Ex3 Paso 2')

content = R(content,
    'Luego,\n\\[\nV = \\int_{0}^{1}',
    '\\textbf{Paso 3. Integrar en $x$.}\n\\[\nV = \\int_{0}^{1}',
    'Ex3 Paso 3')

# ==== EJEMPLO 4: Cambio de orden (quitar \qedhere, boxear resultado) ====
content = R(content,
    'Observamos los límites del orden original:',
    '\\textbf{Paso 1. Identificar el sólido.} Observamos los límites del orden original:',
    'Ex4 Paso 1')

content = R(content,
    'Queremos integrar primero \\(z\\), luego \\(x\\), luego \\(y\\).',
    '\\textbf{Paso 2. Nuevo orden $dz\\,dx\\,dy$.} Queremos integrar primero \\(z\\), luego \\(x\\), luego \\(y\\).',
    'Ex4 Paso 2')

content = R(content,
    'I = \\int_{y=0}^{1}\\int_{x=y}^{1}\\int_{z=0}^{x+y} f(x,y,z)\\,dz\\,dx\\,dy.\n',
    '\\boxed{I = \\int_{y=0}^{1}\\int_{x=y}^{1}\\int_{z=0}^{x+y} f(x,y,z)\\,dz\\,dx\\,dy.}\n',
    'Ex4 boxed')

content = R(content,
    'desigualdades que definen el sólido. \\qedhere\n',
    'desigualdades que definen el sólido.\n',
    'Ex4 qedhere')

# ==== EJEMPLO 5: Masa y CM con densidad constante ====
content = R(content,
    'La masa es\n',
    '\\textbf{Paso 1. Masa.}\nLa masa es\n',
    'Ex5 Paso 1')

content = R(content,
    'Por simetría del tetraedro con respecto a las tres coordenadas,',
    '\\textbf{Paso 2. Centro de masa (argumento de simetría).} Por simetría del tetraedro con respecto a las tres coordenadas,',
    'Ex5 Paso 2')

content = R(content,
    'Calculemos \\(\\iiint_D x\\,dV\\):\n',
    '\\textbf{Paso 3. Calcular $\\iiint_D x\\,dV$.}\n',
    'Ex5 Paso 3')

# ==== EJEMPLO 6: Masa con densidad variable ====
content = R(content,
    'Primero integramos en \\(z\\):\n',
    '\\textbf{Paso 1. Integrar en $z$.}\n',
    'Ex6 Paso 1')

content = R(content,
    'Luego,\n\\[\nM = \\frac12',
    '\\textbf{Paso 2. Integral doble resultante.}\n\\[\nM = \\frac12',
    'Ex6 Paso 2')

content = R(content,
    'Para la integral interior, fijamos \\(x\\):\n',
    '\\textbf{Paso 3. Integral interior (sustitución).}\n',
    'Ex6 Paso 3')

content = R(content,
    'Por tanto,\n\\[\nM = \\frac{1}{24}',
    '\\textbf{Paso 4. Resultado final.}\n\\[\nM = \\frac{1}{24}',
    'Ex6 Paso 4')

# ==== EJEMPLO 7: Momento de inercia Iz ====
content = R(content,
    'Integramos en \\(z\\):\n',
    '\\textbf{Paso 1. Integrar en $z$.}\n',
    'Ex7 Paso 1')

content = R(content,
    'Luego,\n\\[\nI_z = \\int_{0}^{1}',
    '\\textbf{Paso 2. Integrar la doble integral.}\n\\[\nI_z = \\int_{0}^{1}',
    'Ex7 Paso 2')

with open('inttriples.tex', 'w', encoding='utf-8') as f:
    f.write(content)

ok   = sum(1 for r in results if r.startswith('OK'))
miss = sum(1 for r in results if r.startswith('MISS'))
for r in results:
    print(r)
print(f'\n{ok} OK, {miss} missed')
