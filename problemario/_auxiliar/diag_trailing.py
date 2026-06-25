#!/usr/bin/env python3
# Verifica espacios finales en líneas clave de limites.tex
with open('limites.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

targets = [246, 247, 248, 249, 250, 251, 262, 263, 264, 265, 266, 267]
print("=== Ej.3 (|x|/x) y Ej.4 (función por partes) ===")
for i in targets:
    print(f"L{i+1}: {repr(lines[i])}")
