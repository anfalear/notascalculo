"""
Fix caps 27-31: Paso N: -> Paso N., and \sin -> \sen in caps 27, 29, 31.
"""
import re

base = r"C:\Users\anfalear\notascalculo\problemario"

files_all = [
    f"{base}\\cap27_EDOs primer orden.tex",
    f"{base}\\cap28_EDOs orden n.tex",
    f"{base}\\cap29_Sistemas de EDOs.tex",
    f"{base}\\cap30_Sol EDOs Series Potencias.tex",
    f"{base}\\cap31_Transformada de Laplace.tex",
]

# Only these three need \sin -> \sen
files_sin = [
    f"{base}\\cap27_EDOs primer orden.tex",
    f"{base}\\cap29_Sistemas de EDOs.tex",
    f"{base}\\cap31_Transformada de Laplace.tex",
]

total_paso = 0
total_sin = 0

for filepath in files_all:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix Paso N: -> Paso N.
    new_content, n = re.subn(
        r'(\\textbf\{Paso \d+):\}',
        r'\1.}',
        content
    )
    total_paso += n
    if n:
        print(f"  Paso fixes in {filepath.split(chr(92))[-1]}: {n}")

    # Fix \sin -> \sen (not \sinh)
    if filepath in files_sin:
        new_content, m = re.subn(r'\\sin(?!h)', r'\\sen', new_content)
        total_sin += m
        if m:
            print(f"  \\sin->\\sen in {filepath.split(chr(92))[-1]}: {m}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print(f"\nTotal Paso fixes: {total_paso}")
print(f"Total \\sin->\\sen fixes: {total_sin}")
