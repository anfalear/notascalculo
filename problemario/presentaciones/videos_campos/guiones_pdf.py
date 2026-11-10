"""
guiones_pdf.py -- Convierte guion_video_N.txt en guion_video_N.pdf para leer
mientras se graba la voz: letra grande, un bloque por diapositiva y una marca
de PAUSA (3 s de silencio) entre bloques, que es lo que usa el montaje
automático para cortar el audio.

    python guiones_pdf.py        (desde esta carpeta; usa lualatex)
"""
import re, subprocess
from pathlib import Path

AQUI = Path(__file__).resolve().parent


def esc(t):
    rep = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
           "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\^{}"}
    return "".join(rep.get(c, c) for c in t)


PRE = r"""\documentclass[14pt]{extarticle}
\usepackage[a4paper,margin=2cm]{geometry}
\usepackage{fontspec}
\setmainfont{Segoe UI}
\usepackage{xcolor}
\definecolor{navy}{HTML}{1B2A4A}\definecolor{tealx}{HTML}{1F7A6C}
\definecolor{brick}{HTML}{A34A3E}\definecolor{gray60}{HTML}{8A8A85}
\usepackage{fancyhdr}\pagestyle{fancy}\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\color{gray60}\small TITULO \quad·\quad \thepage}
\setlength{\parindent}{0pt}\setlength{\parskip}{6pt}
\linespread{1.25}
\newcommand{\capitulo}[1]{\vspace{14pt}{\color{tealx}\Large\bfseries #1}\par\vspace{2pt}}
\newcommand{\bloque}[3]{\needspace{5\baselineskip}\vspace{4pt}%
  {\color{navy}\bfseries #1}\hfill{\color{gray60}\small #2}\par
  \ifx&#3&\else{\color{brick}\small\bfseries #3}\par\fi}
\newcommand{\pausa}{\par\vspace{4pt}{\centering\color{brick}\bfseries — PAUSA 3 s —\par}\vspace{4pt}}
\usepackage{needspace}
\begin{document}
"""


def convertir(txt):
    lineas = txt.read_text(encoding="utf8").splitlines()
    titulo = {"video_1_green.tex": "Video 1 — Teorema de Green",
              "video_2_superficie_flujo_divergencia.tex": "Video 2 — Superficies, flujo y divergencia",
              "video_3_stokes.tex": "Video 3 — Teorema de Stokes"}[lineas[0].replace("GUION --- ", "").strip()]
    resumen = lineas[1]
    cuerpo = [PRE.replace("TITULO", esc(titulo)),
              r"{\color{navy}\LARGE\bfseries " + esc(titulo) + r"}\par",
              r"{\color{gray60}" + esc(resumen) + r"}\par",
              r"\fbox{\parbox{\linewidth}{\small\textbf{Para grabar:} lea de corrido. "
              r"En cada \textcolor{brick}{\textbf{— PAUSA 3 s —}} quédese callado unos 3 segundos "
              r"(así se cambia de diapositiva). Si se equivoca: pausa y repita el bloque desde el comienzo.}}\par"]
    primero = True
    pausa_hecha = False
    parrafo = []

    def volcar():
        if parrafo:
            cuerpo.append(esc(" ".join(parrafo)) + r"\par")
            parrafo.clear()

    for l in lineas[3:]:
        m_cap = re.match(r"^=== (.*) ===$", l)
        m_blo = re.match(r"^\[(\d+:\d\d)\] Frame (\d+): (.*?)\s+\((.*)\)\s*$", l)
        if m_cap:
            volcar()
            if not primero:
                cuerpo.append(r"\pausa")
                pausa_hecha = True
            cuerpo.append(r"\capitulo{" + esc(m_cap.group(1)) + "}")
        elif m_blo:
            volcar()
            if not primero and not pausa_hecha:
                cuerpo.append(r"\pausa")
            primero = False
            pausa_hecha = False
            t, n, nombre, info = m_blo.groups()
            manim = ""
            if nombre.startswith("Manim:"):
                nombre = nombre.replace("Manim:", "").strip()
                manim = "▶ aquí va una animación"
            cuerpo.append(r"\bloque{" + f"{n}. " + esc(nombre) + "}{" + esc(f"{t} · {info}") + "}{" + manim + "}")
        elif l.strip():
            parrafo.append(l.strip())
        else:
            volcar()
    volcar()
    cuerpo.append(r"\pausa{\centering\color{gray60}(fin)\par}\end{document}")
    tex = txt.with_suffix(".tex")
    tex.write_text("\n".join(cuerpo), encoding="utf8")
    for _ in range(2):
        r = subprocess.run(["lualatex", "-interaction=nonstopmode", tex.name], cwd=AQUI,
                           capture_output=True, text=True, encoding="utf8", errors="replace")
    print(tex.with_suffix(".pdf").name, "OK" if r.returncode == 0 else "ERROR (ver .log)")


for n in (1, 2, 3):
    convertir(AQUI / f"guion_video_{n}.txt")
