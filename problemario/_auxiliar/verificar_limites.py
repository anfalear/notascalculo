#!/usr/bin/env python3
# Verifica el reformateo de limites.tex
import re

with open('limites.tex', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# 1) Contar examples con y sin título
ex_con_titulo = re.findall(r'\\begin\{example\}\[', content)
ex_sin_titulo = re.findall(r'\\begin\{example\}\n', content)
print(f"Examples con título []: {len(ex_con_titulo)}")
print(f"Examples sin título  : {len(ex_sin_titulo)}")

# 2) Detectar myproof huérfanos (\\end{example} seguido de \\begin{myproof} sin \\begin{example} entre medio)
huerfanos = re.findall(r'\\end\{example\}\s*\n\s*\n\s*\\begin\{myproof\}', content)
print(f"myproof huérfanos    : {len(huerfanos)}")

# 3) Contar \boxed
boxed = re.findall(r'\\boxed\{', content)
print(f"\\boxed encontrados   : {len(boxed)}")

# 4) Residuos de square
squares = re.findall(r'\\square|\\qquad\\square', content)
print(f"\\square residuales   : {len(squares)}")

# 5) Contar \textbf{Paso
pasos = re.findall(r'\\textbf\{Paso', content)
print(f"\\textbf{{Paso...}}     : {len(pasos)}")

# 6) Mostrar los títulos de los examples
print("\n=== Títulos de examples ===")
for m in re.finditer(r'\\begin\{example\}(\[.*?\])?', content):
    titulo = m.group(1) if m.group(1) else "(SIN TÍTULO)"
    print(f"  {titulo}")
