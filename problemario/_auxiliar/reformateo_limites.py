#!/usr/bin/env python3
# Reformateo limites.tex: 10 ejemplos al formato 4-pasos + boxed
with open('limites.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Normalizar: quitar espacios finales de cada línea (limpia trailing spaces)
content = '\n'.join(line.rstrip() for line in content.split('\n'))

replacements = []

# ============================================================
# Ej.1 — discontinuidad evitable (myproof YA dentro, sin pasos)
# ============================================================
replacements.append((
r"""\begin{example}
Considere \(   f(x) = \frac{x^2-1}{x-1} \) en $x=1$.

\begin{myproof}
Note que la función no está definida en $x=1$, pero para $x\neq 1$ se
simplifica a $f(x)=x+1$. Al acercarse a $1$, $f(x)\to 2$. Es decir,
$\lim_{x\to 1}f(x)=2$, aunque $f(1)$ no exista.

La figura~\ref{fig:limite_ejemplo} ilustra este comportamiento:""",

r"""\begin{example}[Discontinuidad evitable en $f(x)=(x^2-1)/(x-1)$]
Calcule $\displaystyle\lim_{x\to 1}\frac{x^2-1}{x-1}$.

\begin{myproof}
\textbf{Paso 1: Simplificar para $x\neq 1$.} La función no está definida en $x=1$, pero para $x\neq 1$:
\[
  \frac{x^2-1}{x-1} = \frac{(x-1)(x+1)}{x-1} = x+1.
\]

\textbf{Paso 2: Calcular el límite.} Al acercarse a $1$, $f(x)=x+1\to 2$:
\[
  \boxed{\lim_{x\to 1}\frac{x^2-1}{x-1} = 2,}
\]
aunque $f(1)$ no exista. La figura~\ref{fig:limite_ejemplo} ilustra este comportamiento:"""
))

# ============================================================
# Ej.2 — demostración épsilon-delta (myproof FUERA del example)
# ============================================================
replacements.append((
r"""\begin{example}
Demostrar que $\lim_{x \to 3}(2x-1) = 5$ mediante la definición
$\epsilon$-$\delta$.
\end{example}

\begin{myproof}
Dado $\epsilon > 0$, buscamos $\delta > 0$ tal que
\[
  0 < |x-3| < \delta \implies |(2x-1)-5| < \epsilon.
\]
Observamos que $|(2x-1)-5| = |2x-6| = 2|x-3|$. Para garantizar
$2|x-3| < \epsilon$, basta exigir $|x-3| < \epsilon/2$. Elegimos
$\delta = \epsilon/2$. Entonces, si $0 < |x-3| < \delta$:
\[
  |(2x-1)-5| = 2|x-3| < 2\cdot\frac{\epsilon}{2} = \epsilon. \qquad\square
\]""",

r"""\begin{example}[Demostración $\epsilon$-$\delta$: $\lim_{x\to 3}(2x-1)=5$]
Demostrar que $\lim_{x \to 3}(2x-1) = 5$ mediante la definición
$\epsilon$-$\delta$.

\begin{myproof}
\textbf{Paso 1: Análisis preliminar.} Se busca $\delta>0$ tal que
\[
  0 < |x-3| < \delta \implies |(2x-1)-5| < \epsilon.
\]
Observamos que $|(2x-1)-5| = |2x-6| = 2|x-3|$. Para garantizar
$2|x-3| < \epsilon$, basta exigir $|x-3| < \epsilon/2$.

\textbf{Paso 2: Demostración formal.} Elegimos $\delta = \epsilon/2$. Entonces, si $0 < |x-3| < \delta$:
\[
  |(2x-1)-5| = 2|x-3| < 2\cdot\frac{\epsilon}{2} = \epsilon.
\]
\[
  \boxed{\lim_{x\to 3}(2x-1) = 5.}
\]"""
))

# Ej.2: agregar \end{example} que faltaba (el myproof se cerró pero el example no)
replacements.append((
r"""\label{fig:epsilon_delta_demo}
\end{figure}
\end{myproof}

\begin{theorem}[Unicidad del límite]""",

r"""\label{fig:epsilon_delta_demo}
\end{figure}
\end{myproof}
\end{example}

\begin{theorem}[Unicidad del límite]"""
))

# ============================================================
# Unicidad — quitar $\square$ del myproof del teorema
# ============================================================
replacements.append((
r"""lo cual es absurdo. Por tanto, $L_1 = L_2$. $\square$""",
r"""lo cual es absurdo. Por tanto, $L_1 = L_2$."""
))

# ============================================================
# Ej.3 — límite de |x|/x (myproof FUERA)
# ============================================================
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\lim_{x\to 0}\frac{|x|}{x}$.
\end{example}

\begin{myproof}
El límite por la derecha es $1$ y por la izquierda es $-1$; como difieren,
$\lim_{x\to 0}\dfrac{|x|}{x}$ no existe.
\end{myproof}""",

r"""\begin{example}[Límite lateral de $|x|/x$ en $x=0$]
Calcular $\displaystyle\lim_{x\to 0}\frac{|x|}{x}$.

\begin{myproof}
\textbf{Paso 1: Límite por la derecha.} Para $x>0$, $|x|=x$, luego
\[
  \lim_{x\to 0^+}\frac{|x|}{x} = \lim_{x\to 0^+}\frac{x}{x} = 1.
\]

\textbf{Paso 2: Límite por la izquierda.} Para $x<0$, $|x|=-x$, luego
\[
  \lim_{x\to 0^-}\frac{|x|}{x} = \lim_{x\to 0^-}\frac{-x}{x} = -1.
\]

\textbf{Paso 3: Conclusión.} Como los límites laterales difieren:
\[
  \boxed{\lim_{x\to 0}\frac{|x|}{x} \;\text{no existe.}}
\]
\end{myproof}
\end{example}"""
))

# ============================================================
# Ej.4 — función definida por partes (myproof FUERA)
# ============================================================
replacements.append((
r"""\begin{example}
Sea
\[
  f(x) =
  \begin{cases}
    x^2+1 & \text{si } x < 2,\\
    3x-1  & \text{si } x \geq 2.
  \end{cases}
\]
Determinar si $\lim_{x\to 2}f(x)$ existe.
\end{example}

\begin{myproof}
$\lim_{x\to 2^-}(x^2+1)=5$ \;y\; $\lim_{x\to 2^+}(3x-1)=5$. Como ambos
límites laterales coinciden, $\lim_{x\to 2}f(x) = 5$.
\end{myproof}""",

r"""\begin{example}[Límite de función definida por partes en $x=2$]
Sea
\[
  f(x) =
  \begin{cases}
    x^2+1 & \text{si } x < 2,\\
    3x-1  & \text{si } x \geq 2.
  \end{cases}
\]
Determinar si $\lim_{x\to 2}f(x)$ existe.

\begin{myproof}
\textbf{Paso 1: Límite por la izquierda.}
\[
  \lim_{x\to 2^-}f(x) = \lim_{x\to 2^-}(x^2+1) = 4+1 = 5.
\]

\textbf{Paso 2: Límite por la derecha.}
\[
  \lim_{x\to 2^+}f(x) = \lim_{x\to 2^+}(3x-1) = 6-1 = 5.
\]

\textbf{Paso 3: Conclusión.} Como ambos límites laterales coinciden:
\[
  \boxed{\lim_{x\to 2}f(x) = 5.}
\]
\end{myproof}
\end{example}"""
))

# ============================================================
# Ej.5 — raíz de x³+2x-1 en (0,1) por TVI (myproof FUERA)
# ============================================================
replacements.append((
r"""\begin{example}
Demostrar que $f(x)=x^3+2x-1$ tiene al menos una raíz en $(0,1)$.
\end{example}

\begin{myproof}
$f$ es continua en $[0,1]$ por ser polinómica. $f(0)=-1<0$ y $f(1)=2>0$.
Como $f(0)\cdot f(1)<0$, el Corolario de Bolzano garantiza la existencia de
$c\in(0,1)$ con $f(c)=0$. $\square$
\end{myproof}""",

r"""\begin{example}[Localización de raíz de $x^3+2x-1$ por el TVI]
Demostrar que $f(x)=x^3+2x-1$ tiene al menos una raíz en $(0,1)$.

\begin{myproof}
\textbf{Paso 1: Verificar hipótesis del TVI.} $f$ es continua en $[0,1]$ por ser polinómica. Se evalúa en los extremos:
\[
  f(0) = 0+0-1 = -1 < 0, \qquad f(1) = 1+2-1 = 2 > 0.
\]

\textbf{Paso 2: Aplicar el corolario de Bolzano.} Como $f(0)\cdot f(1)=(-1)(2)<0$, existe al menos un $c\in(0,1)$ tal que:
\[
  \boxed{f(c) = 0.}
\]
\end{myproof}
\end{example}"""
))

# ============================================================
# Ej.6 — x = cos x en (0, pi/2) (myproof FUERA)
# ============================================================
replacements.append((
r"""\begin{example}
Demostrar que $x=\cos x$ tiene solución en $\left(0,\dfrac{\pi}{2}\right)$.
\end{example}

\begin{myproof}
Sea $g(x)=x-\cos x$, continua en $\left[0,\dfrac{\pi}{2}\right]$.
$g(0)=-1<0$ \;y\; $g\!\left(\dfrac{\pi}{2}\right)=\dfrac{\pi}{2}>0$.
Por Bolzano existe $c\in\!\left(0,\dfrac{\pi}{2}\right)$ con $g(c)=0$,
es decir, $c=\cos c$. $\square$
\end{myproof}""",

r"""\begin{example}[La ecuación $x=\cos x$ tiene solución en $(0,\pi/2)$]
Demostrar que $x=\cos x$ tiene solución en $\left(0,\dfrac{\pi}{2}\right)$.

\begin{myproof}
\textbf{Paso 1: Reducir a un problema de raíces.} Sea $g(x)=x-\cos x$, continua en $\left[0,\dfrac{\pi}{2}\right]$. Se evalúa en los extremos:
\[
  g(0) = 0-\cos 0 = -1 < 0, \qquad
  g\!\left(\tfrac{\pi}{2}\right) = \tfrac{\pi}{2}-\cos\tfrac{\pi}{2} = \tfrac{\pi}{2} > 0.
\]

\textbf{Paso 2: Aplicar Bolzano.} Como $g(0)\cdot g(\pi/2)<0$, existe $c\in\!\left(0,\dfrac{\pi}{2}\right)$ con $g(c)=0$, es decir:
\[
  \boxed{c = \cos c.}
\]
\end{myproof}
\end{example}"""
))

# ============================================================
# Ej.7 — ln(1+3x)/sin(2x) (myproof FUERA)
# ============================================================
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\lim_{x\to 0}\frac{\ln(1+3x)}{\sin 2x}$.
\end{example}

\begin{myproof}
Como $\ln(1+3x)\sim 3x$ y $\sin 2x\sim 2x$:
\[
  \lim_{x\to 0}\frac{\ln(1+3x)}{\sin 2x}
  = \lim_{x\to 0}\frac{3x}{2x} = \frac{3}{2}. \qquad\square
\]
\end{myproof}""",

r"""\begin{example}[Límite por equivalentes: $\ln(1+3x)/\sin 2x$]
Calcular $\displaystyle\lim_{x\to 0}\frac{\ln(1+3x)}{\sin 2x}$.

\begin{myproof}
\textbf{Paso 1: Identificar infinitesimales equivalentes.} Cuando $x\to 0$:
\[
  \ln(1+3x)\sim 3x, \qquad \sin 2x\sim 2x.
\]

\textbf{Paso 2: Sustituir y simplificar.}
\[
  \lim_{x\to 0}\frac{\ln(1+3x)}{\sin 2x}
  = \lim_{x\to 0}\frac{3x}{2x} = \boxed{\dfrac{3}{2}.}
\]
\end{myproof}
\end{example}"""
))

# ============================================================
# Ej.8 — (e^5x-1)/tan(3x) (myproof FUERA)
# ============================================================
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\lim_{x\to 0}\frac{e^{5x}-1}{\tan 3x}$.
\end{example}

\begin{myproof}
Como $e^{5x}-1\sim 5x$ y $\tan 3x\sim 3x$:
\[
  \lim_{x\to 0}\frac{e^{5x}-1}{\tan 3x}
  = \lim_{x\to 0}\frac{5x}{3x} = \frac{5}{3}. \qquad\square
\]
\end{myproof}""",

r"""\begin{example}[Límite por equivalentes: $(e^{5x}-1)/\tan 3x$]
Calcular $\displaystyle\lim_{x\to 0}\frac{e^{5x}-1}{\tan 3x}$.

\begin{myproof}
\textbf{Paso 1: Identificar infinitesimales equivalentes.} Cuando $x\to 0$:
\[
  e^{5x}-1\sim 5x, \qquad \tan 3x\sim 3x.
\]

\textbf{Paso 2: Sustituir y simplificar.}
\[
  \lim_{x\to 0}\frac{e^{5x}-1}{\tan 3x}
  = \lim_{x\to 0}\frac{5x}{3x} = \boxed{\dfrac{5}{3}.}
\]
\end{myproof}
\end{example}"""
))

# ============================================================
# Ej.9 — (1-cos x)/(x sin x) (myproof FUERA)
# ============================================================
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\lim_{x\to 0}\frac{1-\cos x}{x\sin x}$.
\end{example}

\begin{myproof}
Como $1-\cos x\sim\dfrac{x^2}{2}$ y $\sin x\sim x$:
\[
  \lim_{x\to 0}\frac{1-\cos x}{x\sin x}
  = \lim_{x\to 0}\frac{x^2/2}{x\cdot x}
  = \frac{1}{2}. \qquad\square
\]
\end{myproof}""",

r"""\begin{example}[Límite por equivalentes: $(1-\cos x)/(x\sin x)$]
Calcular $\displaystyle\lim_{x\to 0}\frac{1-\cos x}{x\sin x}$.

\begin{myproof}
\textbf{Paso 1: Identificar infinitesimales equivalentes.} Cuando $x\to 0$:
\[
  1-\cos x\sim\frac{x^2}{2}, \qquad \sin x\sim x.
\]

\textbf{Paso 2: Sustituir y simplificar.}
\[
  \lim_{x\to 0}\frac{1-\cos x}{x\sin x}
  = \lim_{x\to 0}\frac{x^2/2}{x\cdot x}
  = \lim_{x\to 0}\frac{x^2/2}{x^2} = \boxed{\dfrac{1}{2}.}
\]
\end{myproof}
\end{example}"""
))

# ============================================================
# Ej.10 — arcsin(2x)/ln(1+4x) (myproof FUERA)
# ============================================================
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\lim_{x\to 0}\frac{\arcsin 2x}{\ln(1+4x)}$.
\end{example}

\begin{myproof}
Como $\arcsin 2x\sim 2x$ y $\ln(1+4x)\sim 4x$:
\[
  \lim_{x\to 0}\frac{\arcsin 2x}{\ln(1+4x)}
  = \lim_{x\to 0}\frac{2x}{4x} = \frac{1}{2}. \qquad\square
\]
\end{myproof}""",

r"""\begin{example}[Límite por equivalentes: $\arcsin 2x/\ln(1+4x)$]
Calcular $\displaystyle\lim_{x\to 0}\frac{\arcsin 2x}{\ln(1+4x)}$.

\begin{myproof}
\textbf{Paso 1: Identificar infinitesimales equivalentes.} Cuando $x\to 0$:
\[
  \arcsin 2x\sim 2x, \qquad \ln(1+4x)\sim 4x.
\]

\textbf{Paso 2: Sustituir y simplificar.}
\[
  \lim_{x\to 0}\frac{\arcsin 2x}{\ln(1+4x)}
  = \lim_{x\to 0}\frac{2x}{4x} = \boxed{\dfrac{1}{2}.}
\]
\end{myproof}
\end{example}"""
))

# ============================================================
# Aplicar todos los reemplazos
# ============================================================
for i, (old, new) in enumerate(replacements):
    if old in content:
        content = content.replace(old, new, 1)
        print(f"OK  reemplazo {i+1:2d}")
    else:
        print(f"*** NO ENCONTRADO reemplazo {i+1:2d}")

with open('limites.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nListo.")
