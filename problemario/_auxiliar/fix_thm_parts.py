import re, os

base = r"C:\Users\anfalear\notascalculo\problemario"

# ── 1. thm -> theorem en caps 28-31 ──────────────────────────────────────────
thm_files = [
    "cap28_EDOs orden n.tex",
    "cap29_Sistemas de EDOs.tex",
    "cap30_Sol EDOs Series Potencias.tex",
    "cap31_Transformada de Laplace.tex",
]

for name in thm_files:
    path = os.path.join(base, name)
    txt = open(path, encoding="utf-8").read()
    orig = txt
    txt = txt.replace(r"\begin{thm}", r"\begin{theorem}")
    txt = txt.replace(r"\end{thm}",   r"\end{theorem}")
    n = orig.count(r"\begin{thm}") + orig.count(r"\end{thm}")
    open(path, "w", encoding="utf-8").write(txt)
    print(f"  thm->theorem en {name}: {n} reemplazos")

# ── 2. parts -> enumerate en inttriples, limvariasvariables, multiplicadores ──
parts_files = [
    "inttriples.tex",
    "limvariasvariables.tex",
    "multiplicadoresintdobles.tex",
]

for name in parts_files:
    path = os.path.join(base, name)
    txt = open(path, encoding="utf-8").read()
    orig = txt
    txt = txt.replace(r"\begin{parts}",  r"\begin{enumerate}[(a)]")
    txt = txt.replace(r"\end{parts}",    r"\end{enumerate}")
    # \part seguido de espacio o newline (no \part{) — solo el exam-style
    txt = re.sub(r"\\part(?=[ \t\n])", r"\\item", txt)
    nb = orig.count(r"\begin{parts}")
    ne = orig.count(r"\end{parts}")
    np_ = len(re.findall(r"\\part(?=[ \t\n])", orig))
    print(f"  parts->enumerate en {name}: {nb} begin, {ne} end, {np_} \\part->\\item")
    open(path, "w", encoding="utf-8").write(txt)

print("\nListo.")
