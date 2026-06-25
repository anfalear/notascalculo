# -*- coding: utf-8 -*-
path = r'C:\Users\anfalear\notascalculo\problemario\tecintegracion.tex'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = []

# ===== EJEMPLO 1: sin^5 x cos x =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int \sin^5 x \cos x\, dx$.
\end{example}

\begin{myproof}
Observamos que $\cos x$ es la derivada de $\sin x$. Tomamos $u = \sin x$,
$du = \cos x\, dx$:
\[
\int \sin^5 x \cos x\, dx = \int u^5\, du = \frac{u^6}{6} + C
= \frac{\sin^6 x}{6} + C. \qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Sustitución simple: potencia de seno]
Calcular $\displaystyle\int \sin^5 x \cos x\, dx$.

\begin{myproof}

\textbf{Paso 1: Elegir la sustitución.}
$\cos x$ es la derivada de $\sin x$: $u = \sin x$, $du = \cos x\, dx$.

\textbf{Paso 2: Cambiar de variable e integrar.}
\[
\int \sin^5 x \cos x\, dx = \int u^5\, du = \frac{u^6}{6} + C.
\]

\textbf{Paso 3: Regresar a la variable original.}
\[
\boxed{\int \sin^5 x \cos x\, dx = \frac{\sin^6 x}{6} + C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 2: dx/(x ln x) =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int \frac{dx}{x \ln x}$.
\end{example}

\begin{myproof}
Como $\frac{1}{x}$ es la derivada de $\ln x$, tomamos $u = \ln x$,
$du = \frac{dx}{x}$:
\[
\int \frac{dx}{x \ln x} = \int \frac{du}{u} = \ln|u| + C
= \ln|\ln x| + C. \qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Sustitución simple: logaritmo anidado]
Calcular $\displaystyle\int \dfrac{dx}{x \ln x}$.

\begin{myproof}

\textbf{Paso 1: Elegir la sustitución.}
$\frac{1}{x}$ es la derivada de $\ln x$: $u = \ln x$, $du = \frac{dx}{x}$.

\textbf{Paso 2: Cambiar de variable e integrar.}
\[
\int \frac{dx}{x \ln x} = \int \frac{du}{u} = \ln|u| + C.
\]

\textbf{Paso 3: Regresar a la variable original.}
\[
\boxed{\int \frac{dx}{x \ln x} = \ln|\ln x| + C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 3: sqrt(2x+1) dx =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int \sqrt{2x+1}\, dx$.
\end{example}

\begin{myproof}
Sea $u = 2x+1$, $du = 2\,dx$:
\[
\int \sqrt{2x+1}\, dx = \frac{1}{2}\int u^{1/2}\, du
= \frac{1}{2}\cdot\frac{u^{3/2}}{3/2} + C
= \frac{1}{3}(2x+1)^{3/2} + C. \qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Sustitución simple: raíz lineal]
Calcular $\displaystyle\int \sqrt{2x+1}\, dx$.

\begin{myproof}

\textbf{Paso 1: Sustituir.}
$u = 2x+1$, $du = 2\,dx$, $dx = \frac{du}{2}$.

\textbf{Paso 2: Integrar en $u$.}
\[
\int \sqrt{2x+1}\, dx = \frac{1}{2}\int u^{1/2}\, du
= \frac{1}{2}\cdot\frac{u^{3/2}}{3/2} + C.
\]

\textbf{Paso 3: Regresar a $x$.}
\[
\boxed{\int \sqrt{2x+1}\, dx = \frac{1}{3}(2x+1)^{3/2} + C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 4: tan x dx  (\qquad \square en línea propia) =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int \tan x\, dx$.
\end{example}

\begin{myproof}
Escribimos $\tan x = \frac{\sin x}{\cos x}$ y tomamos $u = \cos x$,
$du = -\sin x\, dx$:
\[
\int \tan x\, dx = -\int \frac{du}{u} = -\ln|u| + C = \ln|\sec x| + C.
\qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Sustitución simple: integral de la tangente]
Calcular $\displaystyle\int \tan x\, dx$.

\begin{myproof}

\textbf{Paso 1: Reescribir e identificar la sustitución.}
$\tan x = \frac{\sin x}{\cos x}$; tomamos $u = \cos x$, $du = -\sin x\, dx$.

\textbf{Paso 2: Integrar.}
\[
\int \tan x\, dx = -\int \frac{du}{u} = -\ln|u| + C.
\]

\textbf{Paso 3: Regresar a $x$.}
\[
\boxed{\int \tan x\, dx = \ln|\sec x| + C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 5: integral definida x/sqrt(x^2+9) =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int_0^4 \frac{x}{\sqrt{x^2+9}}\, dx$.
\end{example}

\begin{myproof}
Sea $u = x^2+9$, $du = 2x\,dx$. Límites: $x=0 \Rightarrow u=9$;
$x=4 \Rightarrow u=25$:
\[
\int_0^4 \frac{x}{\sqrt{x^2+9}}\, dx
= \frac{1}{2}\int_9^{25} u^{-1/2}\, du
= \Big[\sqrt{u}\Big]_9^{25}
= \sqrt{25} - \sqrt{9} = 2. \qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Sustitución en integral definida]
Calcular $\displaystyle\int_0^4 \dfrac{x}{\sqrt{x^2+9}}\, dx$.

\begin{myproof}

\textbf{Paso 1: Elegir la sustitución y transformar los límites.}
$u = x^2+9$, $du = 2x\,dx$. Límites: $x=0 \Rightarrow u=9$; $x=4 \Rightarrow u=25$.

\textbf{Paso 2: Integrar en $u$.}
\[
\int_0^4 \frac{x}{\sqrt{x^2+9}}\, dx
= \frac{1}{2}\int_9^{25} u^{-1/2}\, du
= \Big[\sqrt{u}\Big]_9^{25}.
\]

\textbf{Paso 3: Evaluar.}
\[
\boxed{\int_0^4 \frac{x}{\sqrt{x^2+9}}\, dx = \sqrt{25} - \sqrt{9} = 2.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 6: x e^x dx =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int x e^x\, dx$.
\end{example}

\begin{myproof}
Por LIATE: $u = x$, $dv = e^x\,dx$; $du = dx$, $v = e^x$:
\[
\int x e^x\, dx = x e^x - \int e^x\, dx = e^x(x-1) + C. \qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Integración por partes: $x e^x$]
Calcular $\displaystyle\int x e^x\, dx$.

\begin{myproof}

\textbf{Paso 1: Elegir $u$ y $dv$ (regla LIATE).}
$u = x$, $dv = e^x\,dx$; $du = dx$, $v = e^x$.

\textbf{Paso 2: Aplicar $\int u\,dv = uv - \int v\,du$.}
\[
\boxed{\int x e^x\, dx = x e^x - \int e^x\, dx = e^x(x-1) + C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 7: ln x dx =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int \ln x\, dx$.
\end{example}

\begin{myproof}
Escribimos $\ln x = \ln x \cdot 1$; tomamos $u = \ln x$, $dv = dx$;
$du = \frac{dx}{x}$, $v = x$:
\[
\int \ln x\, dx = x\ln x - \int x\cdot\frac{1}{x}\, dx
= x\ln x - x + C. \qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Integración por partes: $\ln x$]
Calcular $\displaystyle\int \ln x\, dx$.

\begin{myproof}

\textbf{Paso 1: Escribir $\ln x = \ln x \cdot 1$ y elegir $u$, $dv$.}
$u = \ln x$, $dv = dx$; $du = \frac{dx}{x}$, $v = x$.

\textbf{Paso 2: Aplicar la fórmula y simplificar.}
\[
\boxed{\int \ln x\, dx = x\ln x - \int x\cdot\frac{1}{x}\, dx = x\ln x - x + C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 8: arcsin x dx =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int \arcsin x\, dx$.
\end{example}

\begin{myproof}
$u = \arcsin x$, $dv = dx$; $du = \frac{dx}{\sqrt{1-x^2}}$, $v = x$:
\[
\int \arcsin x\, dx = x\arcsin x - \int \frac{x}{\sqrt{1-x^2}}\, dx.
\]
La integral residual se resuelve con $w = 1-x^2$, $dw = -2x\,dx$:
\[
-\frac{1}{2}\int w^{-1/2}\, dw = -\sqrt{w} + C = -\sqrt{1-x^2}+C.
\]
Por tanto:
\[
\int \arcsin x\, dx = x\arcsin x + \sqrt{1-x^2} + C. \qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Integración por partes: $\arcsin x$]
Calcular $\displaystyle\int \arcsin x\, dx$.

\begin{myproof}

\textbf{Paso 1: Elegir $u$ y $dv$.}
$u = \arcsin x$, $dv = dx$; $du = \dfrac{dx}{\sqrt{1-x^2}}$, $v = x$.

\textbf{Paso 2: Aplicar la fórmula.}
\[
\int \arcsin x\, dx = x\arcsin x - \int \frac{x}{\sqrt{1-x^2}}\, dx.
\]

\textbf{Paso 3: Resolver la integral residual con $w = 1-x^2$.}
\[
-\frac{1}{2}\int w^{-1/2}\, dw = -\sqrt{1-x^2}+C.
\]

\textbf{Paso 4: Combinar.}
\[
\boxed{\int \arcsin x\, dx = x\arcsin x + \sqrt{1-x^2} + C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 9: x^2 sin x dx (aplicación repetida) =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int x^2 \sin x\, dx$.
\end{example}

\begin{myproof}
Se aplican dos rondas de integración por partes.

\noindent\textit{Primera ronda:} $u = x^2$, $dv = \sin x\,dx$;
$du = 2x\,dx$, $v = -\cos x$:
\[
\int x^2 \sin x\, dx = -x^2\cos x + 2\int x\cos x\, dx.
\]
\textit{Segunda ronda sobre $\int x\cos x\,dx$:} $u = x$,
$dv = \cos x\,dx$; $du = dx$, $v = \sin x$:
\[
\int x\cos x\, dx = x\sin x - \int \sin x\, dx = x\sin x + \cos x + C.
\]
Combinando:
\[
\int x^2 \sin x\, dx = -x^2\cos x + 2x\sin x + 2\cos x + C.
\qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Integración por partes repetida: $x^2 \sin x$]
Calcular $\displaystyle\int x^2 \sin x\, dx$.

\begin{myproof}

\textbf{Paso 1: Primera ronda.}
$u = x^2$, $dv = \sin x\,dx$; $du = 2x\,dx$, $v = -\cos x$:
\[
\int x^2 \sin x\, dx = -x^2\cos x + 2\int x\cos x\, dx.
\]

\textbf{Paso 2: Segunda ronda sobre $\int x\cos x\,dx$.}
$u = x$, $dv = \cos x\,dx$; $du = dx$, $v = \sin x$:
\[
\int x\cos x\, dx = x\sin x - \int \sin x\, dx = x\sin x + \cos x + C.
\]

\textbf{Paso 3: Combinar.}
\[
\boxed{\int x^2 \sin x\, dx = -x^2\cos x + 2x\sin x + 2\cos x + C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 10: x^3 e^{2x} dx (tabular) =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int x^3 e^{2x}\, dx$ usando integración por partes
tabular.
\end{example}

\begin{myproof}
Cuando el integrando es un polinomio multiplicado por una función que se
integra conservando su forma (exponencial, seno, coseno), la
\textbf{integración por partes tabular} organiza las rondas sucesivas en una
tabla, evitando la repetición algebraica. Se construyen dos columnas: la de
\textbf{derivadas sucesivas} del factor polinómico (hasta anularse) y la de
\textbf{antiderivadas sucesivas} del factor trascendente. Los signos
alternan $+, -, +, -,\ldots$

\begin{center}
\renewcommand{\arraystretch}{1.6}
\begin{tabular}{c c c}
\toprule
\textbf{Signo} & \textbf{Derivadas} & \textbf{Antiderivadas} \\
\midrule
$+$ & $x^3$ & $e^{2x}$ \\
$-$ & $3x^2$ & $\dfrac{1}{2}e^{2x}$ \\
$+$ & $6x$ & $\dfrac{1}{4}e^{2x}$ \\
$-$ & $6$ & $\dfrac{1}{8}e^{2x}$ \\
$+$ & $0$ & $\dfrac{1}{16}e^{2x}$ \\
\bottomrule
\end{tabular}
\end{center}

El resultado es la suma de los productos diagonales (elemento de la columna
de derivadas por el elemento inmediatamente abajo en la columna de
antiderivadas), con los signos indicados:
\[
\int x^3 e^{2x}\, dx
= x^3\cdot\frac{e^{2x}}{2}
- 3x^2\cdot\frac{e^{2x}}{4}
+ 6x\cdot\frac{e^{2x}}{8}
- 6\cdot\frac{e^{2x}}{16} + C
= e^{2x}\!\left(\frac{x^3}{2} - \frac{3x^2}{4} + \frac{3x}{4} -
\frac{3}{8}\right) + C. \qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Integración por partes tabular: $x^3 e^{2x}$]
Calcular $\displaystyle\int x^3 e^{2x}\, dx$ usando integración por partes tabular.

\begin{myproof}

\textbf{Paso 1: Construir la tabla.}
Columna izquierda: derivadas sucesivas de $x^3$; columna derecha: antiderivadas sucesivas de $e^{2x}$; signos alternados $+,-,+,-,\ldots$

\begin{center}
\renewcommand{\arraystretch}{1.6}
\begin{tabular}{c c c}
\toprule
\textbf{Signo} & \textbf{Derivadas} & \textbf{Antiderivadas} \\
\midrule
$+$ & $x^3$ & $e^{2x}$ \\
$-$ & $3x^2$ & $\dfrac{1}{2}e^{2x}$ \\
$+$ & $6x$ & $\dfrac{1}{4}e^{2x}$ \\
$-$ & $6$ & $\dfrac{1}{8}e^{2x}$ \\
$+$ & $0$ & $\dfrac{1}{16}e^{2x}$ \\
\bottomrule
\end{tabular}
\end{center}

\textbf{Paso 2: Sumar los productos diagonales con sus signos.}
\[
\int x^3 e^{2x}\, dx
= x^3\cdot\frac{e^{2x}}{2}
- 3x^2\cdot\frac{e^{2x}}{4}
+ 6x\cdot\frac{e^{2x}}{8}
- 6\cdot\frac{e^{2x}}{16} + C.
\]

\textbf{Paso 3: Simplificar.}
\[
\boxed{\int x^3 e^{2x}\, dx = e^{2x}\!\left(\frac{x^3}{2} - \frac{3x^2}{4} + \frac{3x}{4} -
\frac{3}{8}\right) + C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 11: e^x sin x dx (cíclica; \qquad \square en línea propia) =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int e^x \sin x\, dx$.
\end{example}

\begin{myproof}
$u = \sin x$, $dv = e^x\,dx$; $du = \cos x\,dx$, $v = e^x$:
\[
\int e^x \sin x\, dx = e^x \sin x - \int e^x \cos x\, dx.
\]
Sobre $\int e^x\cos x\,dx$: $u = \cos x$, $dv = e^x\,dx$;
$du = -\sin x\,dx$, $v = e^x$:
\[
\int e^x \cos x\, dx = e^x\cos x + \int e^x \sin x\, dx.
\]
Sustituyendo en la primera ecuación:
\[
\int e^x \sin x\, dx = e^x\sin x - e^x\cos x - \int e^x\sin x\, dx.
\]
La integral original reaparece. Sumando $\int e^x\sin x\,dx$ a ambos lados:
\[
2\int e^x\sin x\, dx = e^x(\sin x - \cos x) + C
\implies \int e^x\sin x\, dx = \frac{e^x(\sin x - \cos x)}{2} + C.
\qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Integral cíclica: $e^x \sin x$]
Calcular $\displaystyle\int e^x \sin x\, dx$.

\begin{myproof}

\textbf{Paso 1: Primera aplicación de partes.}
$u = \sin x$, $dv = e^x\,dx$; $du = \cos x\,dx$, $v = e^x$:
\[
\int e^x \sin x\, dx = e^x \sin x - \int e^x \cos x\, dx.
\]

\textbf{Paso 2: Segunda aplicación sobre $\int e^x\cos x\,dx$.}
$u = \cos x$, $dv = e^x\,dx$; $du = -\sin x\,dx$, $v = e^x$:
\[
\int e^x \cos x\, dx = e^x\cos x + \int e^x \sin x\, dx.
\]

\textbf{Paso 3: Despejar la integral cíclica.}
\[
\int e^x \sin x\, dx = e^x\sin x - e^x\cos x - \int e^x\sin x\, dx.
\]
\[
\boxed{\int e^x\sin x\, dx = \frac{e^x(\sin x - \cos x)}{2} + C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 12: sin^3 x cos^2 x dx =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int \sin^3 x \cos^2 x \, dx$.
\end{example}

\begin{myproof}
El exponente de $\sin x$ es impar ($m=3$): aplicamos el Caso 1.
\[
\int \sin^3 x \cos^2 x \, dx
= \int \sin^2 x \cos^2 x \cdot \sin x \, dx.
\]
Sea $u = \cos x$, $du = -\sin x\,dx$; reemplazamos $\sin^2 x = 1-u^2$:
\[
= -\int (1-u^2)u^2\, du = -\int(u^2 - u^4)\, du
= -\frac{u^3}{3} + \frac{u^5}{5} + C
= -\frac{\cos^3 x}{3} + \frac{\cos^5 x}{5} + C. \qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Potencias trigonométricas: $\sin^3 x \cos^2 x$]
Calcular $\displaystyle\int \sin^3 x \cos^2 x \, dx$.

\begin{myproof}

\textbf{Paso 1: Identificar el caso y separar el diferencial.}
Exponente de $\sin x$ impar ($m=3$): Caso~1. Reservamos $\sin x\,dx$ para $u=\cos x$:
\[
\int \sin^3 x \cos^2 x \, dx
= \int \sin^2 x \cos^2 x \cdot \sin x \, dx.
\]

\textbf{Paso 2: Sustituir $u = \cos x$, $\sin^2 x = 1-u^2$.}
\[
= -\int (1-u^2)u^2\, du = -\int(u^2 - u^4)\, du
= -\frac{u^3}{3} + \frac{u^5}{5} + C.
\]

\textbf{Paso 3: Regresar a $x$.}
\[
\boxed{\int \sin^3 x \cos^2 x \, dx = -\frac{\cos^3 x}{3} + \frac{\cos^5 x}{5} + C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 13: sin^2 x cos^2 x dx (\qquad \square en línea propia) =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int \sin^2 x \cos^2 x \, dx$.
\end{example}

\begin{myproof}
Ambos exponentes son pares: Caso 3. Usamos $\sin x\cos x = \frac{\sin 2x}{2}$:
\[
\sin^2 x\cos^2 x = \frac{\sin^2 2x}{4} = \frac{1-\cos 4x}{8}.
\]
\[
\int \sin^2 x\cos^2 x\, dx = \frac{x}{8} - \frac{\sin 4x}{32} + C.
\qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Potencias pares: $\sin^2 x \cos^2 x$]
Calcular $\displaystyle\int \sin^2 x \cos^2 x \, dx$.

\begin{myproof}

\textbf{Paso 1: Aplicar identidades de reducción.}
Ambos exponentes pares (Caso~3). Usamos $\sin x\cos x = \frac{\sin 2x}{2}$:
\[
\sin^2 x\cos^2 x = \frac{\sin^2 2x}{4} = \frac{1-\cos 4x}{8}.
\]

\textbf{Paso 2: Integrar.}
\[
\boxed{\int \sin^2 x\cos^2 x\, dx = \frac{x}{8} - \frac{\sin 4x}{32} + C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 14: tan^3 x sec^4 x dx =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int \tan^3 x \sec^4 x \, dx$.
\end{example}

\begin{myproof}
$n=4$ es par: Caso 1. Reservamos $\sec^2 x\,dx$ y escribimos
$\sec^2 x = 1+\tan^2 x$:
\[
\int \tan^3 x(1+\tan^2 x)\sec^2 x\, dx.
\]
Sea $u = \tan x$, $du = \sec^2 x\,dx$:
\[
= \int u^3(1+u^2)\, du = \frac{u^4}{4} + \frac{u^6}{6} + C
= \frac{\tan^4 x}{4} + \frac{\tan^6 x}{6} + C. \qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Potencias de tangente y secante: $\tan^3 x \sec^4 x$]
Calcular $\displaystyle\int \tan^3 x \sec^4 x \, dx$.

\begin{myproof}

\textbf{Paso 1: Aplicar Caso~1 ($n=4$ par).}
Reservamos $\sec^2 x\,dx$ y usamos $\sec^2 x = 1+\tan^2 x$:
\[
\int \tan^3 x(1+\tan^2 x)\sec^2 x\, dx.
\]

\textbf{Paso 2: Sustituir $u = \tan x$, $du = \sec^2 x\,dx$ e integrar.}
\[
= \int u^3(1+u^2)\, du = \frac{u^4}{4} + \frac{u^6}{6} + C.
\]

\textbf{Paso 3: Regresar a $x$.}
\[
\boxed{\int \tan^3 x \sec^4 x \, dx = \frac{\tan^4 x}{4} + \frac{\tan^6 x}{6} + C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 15: sec^3 x dx (\qquad \square en línea propia) =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int \sec^3 x\, dx$.
\end{example}

\begin{myproof}
Este es el caso arquetípico del Caso 3 con $m=0$, $n=3$ (impar). Escribimos
$\sec^3 x = \sec x \cdot \sec^2 x$ e integramos por partes:
$u = \sec x$, $dv = \sec^2 x\,dx$; $du = \sec x\tan x\,dx$, $v = \tan x$:
\[
\int \sec^3 x\, dx = \sec x\tan x - \int \sec x\tan^2 x\, dx.
\]
Usamos $\tan^2 x = \sec^2 x - 1$:
\[
= \sec x\tan x - \int \sec^3 x\, dx + \int \sec x\, dx.
\]
La integral original reaparece. Sumándola a ambos lados y usando
$\int \sec x\,dx = \ln|\sec x + \tan x|$:
\[
2\int \sec^3 x\, dx = \sec x\tan x + \ln|\sec x+\tan x| + C,
\]
\[
\int \sec^3 x\, dx = \frac{\sec x\tan x + \ln|\sec x+\tan x|}{2} + C.
\qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Integral arquetípica: $\sec^3 x$]
Calcular $\displaystyle\int \sec^3 x\, dx$.

\begin{myproof}

\textbf{Paso 1: Aplicar integración por partes.}
Caso~3 ($m=0$, $n=3$ impar). $u = \sec x$, $dv = \sec^2 x\,dx$; $du = \sec x\tan x\,dx$, $v = \tan x$:
\[
\int \sec^3 x\, dx = \sec x\tan x - \int \sec x\tan^2 x\, dx.
\]

\textbf{Paso 2: Usar $\tan^2 x = \sec^2 x - 1$.}
\[
= \sec x\tan x - \int \sec^3 x\, dx + \int \sec x\, dx.
\]

\textbf{Paso 3: Despejar la integral cíclica.}
\[
2\int \sec^3 x\, dx = \sec x\tan x + \ln|\sec x+\tan x| + C.
\]
\[
\boxed{\int \sec^3 x\, dx = \frac{\sec x\tan x + \ln|\sec x+\tan x|}{2} + C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 16: sin(3x)cos(5x) dx =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int \sin(3x)\cos(5x)\, dx$.
\end{example}

\begin{myproof}
Aplicamos $\sin A\cos B = \frac{1}{2}[\sin(A+B)+\sin(A-B)]$ con $A=3x$,
$B=5x$:
\[
\sin(3x)\cos(5x) = \tfrac{1}{2}[\sin 8x + \sin(-2x)]
= \tfrac{1}{2}[\sin 8x - \sin 2x].
\]
\[
\int\sin(3x)\cos(5x)\,dx
= \frac{1}{2}\!\left(-\frac{\cos 8x}{8}+\frac{\cos 2x}{2}\right)+C
= -\frac{\cos 8x}{16}+\frac{\cos 2x}{4}+C. \qquad \square
\]
\end{myproof}""",
r"""\begin{example}[Producto de trigonométricas con distintos ángulos]
Calcular $\displaystyle\int \sin(3x)\cos(5x)\, dx$.

\begin{myproof}

\textbf{Paso 1: Convertir el producto a suma.}
\[
\sin(3x)\cos(5x) = \tfrac{1}{2}[\sin 8x + \sin(-2x)]
= \tfrac{1}{2}[\sin 8x - \sin 2x].
\]

\textbf{Paso 2: Integrar término a término.}
\[
\boxed{\int\sin(3x)\cos(5x)\,dx
= -\frac{\cos 8x}{16}+\frac{\cos 2x}{4}+C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 17: dx/sqrt(9-x^2) =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int \frac{dx}{\sqrt{9-x^2}}$.
\end{example}

\begin{myproof}
Con $a=3$: $x=3\sin\theta$, $dx=3\cos\theta\,d\theta$,
$\sqrt{9-x^2}=3\cos\theta$:
\[
\int\frac{3\cos\theta\,d\theta}{3\cos\theta}=\int d\theta=\theta+C
=\arcsin\!\left(\frac{x}{3}\right)+C. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Sustitución trigonométrica: $\sqrt{a^2-x^2}$]
Calcular $\displaystyle\int \dfrac{dx}{\sqrt{9-x^2}}$.

\begin{myproof}

\textbf{Paso 1: Aplicar $x=3\sin\theta$.}
$dx=3\cos\theta\,d\theta$, $\sqrt{9-x^2}=3\cos\theta$.

\textbf{Paso 2: Integrar.}
\[
\int\frac{3\cos\theta\,d\theta}{3\cos\theta}=\int d\theta=\theta+C.
\]

\textbf{Paso 3: Regresar a $x$.}
\[
\boxed{\int \frac{dx}{\sqrt{9-x^2}} =\arcsin\!\left(\frac{x}{3}\right)+C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 18: x^2 sqrt(4-x^2) dx =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int x^2\sqrt{4-x^2}\,dx$.
\end{example}

\begin{myproof}
Con $a=2$: $x=2\sin\theta$, $dx=2\cos\theta\,d\theta$,
$\sqrt{4-x^2}=2\cos\theta$, $x^2=4\sin^2\theta$:
\[
\int 4\sin^2\!\theta\cdot 2\cos\theta\cdot 2\cos\theta\,d\theta
= 16\int\sin^2\!\theta\cos^2\!\theta\,d\theta
= 16\int\frac{\sin^2\!2\theta}{4}\,d\theta
= 4\int\frac{1-\cos 4\theta}{2}\,d\theta
= 2\theta - \frac{\sin 4\theta}{2}+C.
\]
Del triángulo: $\theta=\arcsin\!\left(\frac{x}{2}\right)$,
$\sin\theta=\frac{x}{2}$, $\cos\theta=\frac{\sqrt{4-x^2}}{2}$.
Usando $\sin 4\theta=4\sin\theta\cos\theta(1-2\sin^2\theta)$:
\[
\int x^2\sqrt{4-x^2}\,dx
= 2\arcsin\!\left(\frac{x}{2}\right)
- \frac{x\sqrt{4-x^2}(4-2x^2)}{8}+C. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Sustitución trigonométrica: $x^2\sqrt{4-x^2}$]
Calcular $\displaystyle\int x^2\sqrt{4-x^2}\,dx$.

\begin{myproof}

\textbf{Paso 1: Aplicar $x=2\sin\theta$.}
$dx=2\cos\theta\,d\theta$, $\sqrt{4-x^2}=2\cos\theta$, $x^2=4\sin^2\theta$:
\[
\int 4\sin^2\!\theta\cdot 2\cos\theta\cdot 2\cos\theta\,d\theta
= 16\int\sin^2\!\theta\cos^2\!\theta\,d\theta
= 4\int\frac{1-\cos 4\theta}{2}\,d\theta
= 2\theta - \frac{\sin 4\theta}{2}+C.
\]

\textbf{Paso 2: Regresar a $x$ con el triángulo de referencia.}
$\theta=\arcsin\!\left(\frac{x}{2}\right)$, $\sin\theta=\frac{x}{2}$, $\cos\theta=\frac{\sqrt{4-x^2}}{2}$; $\sin 4\theta=4\sin\theta\cos\theta(1-2\sin^2\theta)$:
\[
\boxed{\int x^2\sqrt{4-x^2}\,dx
= 2\arcsin\!\left(\frac{x}{2}\right)
- \frac{x\sqrt{4-x^2}(4-2x^2)}{8}+C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 19: dx/sqrt(x^2+16) =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int\frac{dx}{\sqrt{x^2+16}}$.
\end{example}

\begin{myproof}
Con $a=4$: $x=4\tan\theta$, $dx=4\sec^2\theta\,d\theta$,
$\sqrt{x^2+16}=4\sec\theta$:
\[
\int\frac{4\sec^2\theta\,d\theta}{4\sec\theta}=\int\sec\theta\,d\theta
=\ln|\sec\theta+\tan\theta|+C.
\]
Del triángulo: $\tan\theta=\frac{x}{4}$,
$\sec\theta=\frac{\sqrt{x^2+16}}{4}$:
\[
\int\frac{dx}{\sqrt{x^2+16}}
=\ln\left|\frac{\sqrt{x^2+16}+x}{4}\right|+C
=\ln\left|\sqrt{x^2+16}+x\right|+C_1. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Sustitución trigonométrica: $\sqrt{x^2+a^2}$]
Calcular $\displaystyle\int\dfrac{dx}{\sqrt{x^2+16}}$.

\begin{myproof}

\textbf{Paso 1: Aplicar $x=4\tan\theta$.}
$dx=4\sec^2\theta\,d\theta$, $\sqrt{x^2+16}=4\sec\theta$:
\[
\int\frac{4\sec^2\theta\,d\theta}{4\sec\theta}=\int\sec\theta\,d\theta
=\ln|\sec\theta+\tan\theta|+C.
\]

\textbf{Paso 2: Regresar a $x$.}
Del triángulo: $\tan\theta=\frac{x}{4}$, $\sec\theta=\frac{\sqrt{x^2+16}}{4}$:
\[
\boxed{\int\frac{dx}{\sqrt{x^2+16}}=\ln\left|\sqrt{x^2+16}+x\right|+C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 20: sqrt(x^2-9)/x dx (\qquad\square en línea propia) =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int\frac{\sqrt{x^2-9}}{x}\,dx$.
\end{example}

\begin{myproof}
Con $a=3$: $x=3\sec\theta$, $dx=3\sec\theta\tan\theta\,d\theta$,
$\sqrt{x^2-9}=3\tan\theta$:
\[
\int\frac{3\tan\theta\cdot 3\sec\theta\tan\theta\,d\theta}{3\sec\theta}
=3\int\tan^2\!\theta\,d\theta
=3\int(\sec^2\theta-1)\,d\theta
=3\tan\theta-3\theta+C.
\]
Del triángulo: $\tan\theta=\frac{\sqrt{x^2-9}}{3}$,
$\theta=\operatorname{arcsec}\!\!\left(\frac{x}{3}\right)$:
\[
\int\frac{\sqrt{x^2-9}}{x}\,dx
=\sqrt{x^2-9}-3\operatorname{arcsec}\!\!\left(\frac{x}{3}\right)+C.
\qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Sustitución trigonométrica: $\sqrt{x^2-a^2}$]
Calcular $\displaystyle\int\dfrac{\sqrt{x^2-9}}{x}\,dx$.

\begin{myproof}

\textbf{Paso 1: Aplicar $x=3\sec\theta$.}
$dx=3\sec\theta\tan\theta\,d\theta$, $\sqrt{x^2-9}=3\tan\theta$:
\[
\int\frac{3\tan\theta\cdot 3\sec\theta\tan\theta\,d\theta}{3\sec\theta}
=3\int\tan^2\!\theta\,d\theta
=3\int(\sec^2\theta-1)\,d\theta
=3\tan\theta-3\theta+C.
\]

\textbf{Paso 2: Regresar a $x$.}
$\tan\theta=\frac{\sqrt{x^2-9}}{3}$, $\theta=\operatorname{arcsec}\!\!\left(\frac{x}{3}\right)$:
\[
\boxed{\int\frac{\sqrt{x^2-9}}{x}\,dx
=\sqrt{x^2-9}-3\operatorname{arcsec}\!\!\left(\frac{x}{3}\right)+C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 21: dx/(x^2-5x+6) =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int\frac{dx}{x^2-5x+6}$.
\end{example}

\begin{myproof}
$x^2-5x+6=(x-2)(x-3)$. Caso I:
\[
\frac{1}{(x-2)(x-3)}=\frac{A}{x-2}+\frac{B}{x-3}
\implies 1=A(x-3)+B(x-2).
\]
Con $x=3$: $B=1$; con $x=2$: $A=-1$. Integrando:
\[
\int\frac{dx}{x^2-5x+6}
=-\ln|x-2|+\ln|x-3|+C
=\ln\left|\frac{x-3}{x-2}\right|+C. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Fracciones parciales: factores lineales distintos]
Calcular $\displaystyle\int\dfrac{dx}{x^2-5x+6}$.

\begin{myproof}

\textbf{Paso 1: Factorizar y plantear la descomposición.}
$x^2-5x+6=(x-2)(x-3)$; Caso~I:
\[
\frac{1}{(x-2)(x-3)}=\frac{A}{x-2}+\frac{B}{x-3}
\implies 1=A(x-3)+B(x-2).
\]

\textbf{Paso 2: Determinar las constantes.}
Con $x=3$: $B=1$; con $x=2$: $A=-1$.

\textbf{Paso 3: Integrar.}
\[
\boxed{\int\frac{dx}{x^2-5x+6}=\ln\left|\frac{x-3}{x-2}\right|+C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 22: (x^2+2x-1)/(2x^3+3x^2-2x) dx =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int\frac{x^2+2x-1}{2x^3+3x^2-2x}\,dx$.
\end{example}

\begin{myproof}
$2x^3+3x^2-2x=x(2x-1)(x+2)$. Caso I:
\[
\frac{x^2+2x-1}{x(2x-1)(x+2)}=\frac{A}{x}+\frac{B}{2x-1}+\frac{C}{x+2}.
\]
Multiplicando: $x^2+2x-1=A(2x-1)(x+2)+Bx(x+2)+Cx(2x-1)$.
Con $x=0$: $A=\frac{1}{2}$; con $x=\frac{1}{2}$: $B=\frac{1}{5}$;
con $x=-2$: $C=-\frac{1}{10}$. Integrando:
\[
\int\frac{x^2+2x-1}{2x^3+3x^2-2x}\,dx
=\frac{1}{2}\ln|x|+\frac{1}{10}\ln|2x-1|-\frac{1}{10}\ln|x+2|+C.
\qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Fracciones parciales: tres factores lineales]
Calcular $\displaystyle\int\dfrac{x^2+2x-1}{2x^3+3x^2-2x}\,dx$.

\begin{myproof}

\textbf{Paso 1: Factorizar y plantear la descomposición.}
$2x^3+3x^2-2x=x(2x-1)(x+2)$; Caso~I:
\[
\frac{x^2+2x-1}{x(2x-1)(x+2)}=\frac{A}{x}+\frac{B}{2x-1}+\frac{C}{x+2}.
\]

\textbf{Paso 2: Determinar las constantes.}
$x^2+2x-1=A(2x-1)(x+2)+Bx(x+2)+Cx(2x-1)$.
Con $x=0$: $A=\tfrac{1}{2}$; con $x=\tfrac{1}{2}$: $B=\tfrac{1}{5}$; con $x=-2$: $C=-\tfrac{1}{10}$.

\textbf{Paso 3: Integrar.}
\[
\boxed{\int\frac{x^2+2x-1}{2x^3+3x^2-2x}\,dx
=\frac{1}{2}\ln|x|+\frac{1}{10}\ln|2x-1|-\frac{1}{10}\ln|x+2|+C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 23: (2x+2)/(x^2-4x+8) dx =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int\frac{2x+2}{x^2-4x+8}\,dx$.
\end{example}

\begin{myproof}
$\Delta = 16-32=-16<0$: denominador irreducible, Caso III. Separamos:
\[
2x+2=(2x-4)+6.
\]
\[
\int\frac{2x+2}{x^2-4x+8}\,dx
=\int\frac{2x-4}{x^2-4x+8}\,dx+6\int\frac{dx}{x^2-4x+8}
=\ln(x^2-4x+8)+6\int\frac{dx}{(x-2)^2+4}.
\]
Completando el cuadrado y usando la arcotangente:
\[
6\cdot\frac{1}{2}\arctan\!\left(\frac{x-2}{2}\right)+C
=3\arctan\!\left(\frac{x-2}{2}\right)+C.
\]
Resultado:
\[
\int\frac{2x+2}{x^2-4x+8}\,dx
=\ln(x^2-4x+8)+3\arctan\!\left(\frac{x-2}{2}\right)+C.
\qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Fracciones parciales: cuadrática irreducible]
Calcular $\displaystyle\int\dfrac{2x+2}{x^2-4x+8}\,dx$.

\begin{myproof}

\textbf{Paso 1: Identificar el caso y separar el numerador.}
$\Delta = 16-32<0$: Caso~III. Escribimos $2x+2=(2x-4)+6$:
\[
\int\frac{2x+2}{x^2-4x+8}\,dx
=\int\frac{2x-4}{x^2-4x+8}\,dx+6\int\frac{dx}{(x-2)^2+4}.
\]

\textbf{Paso 2: Integrar cada parte.}
\[
=\ln(x^2-4x+8)+6\cdot\frac{1}{2}\arctan\!\left(\frac{x-2}{2}\right)+C.
\]

\textbf{Paso 3: Simplificar.}
\[
\boxed{\int\frac{2x+2}{x^2-4x+8}\,dx
=\ln(x^2-4x+8)+3\arctan\!\left(\frac{x-2}{2}\right)+C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 24: (x^3+x)/(x^2-1) dx (fracción impropia) =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int\frac{x^3+x}{x^2-1}\,dx$ (fracción impropia).
\end{example}

\begin{myproof}
$\deg P=3>\deg Q=2$: división larga. $x^3+x=(x^2-1)\cdot x+2x$, así que
$\frac{x^3+x}{x^2-1}=x+\frac{2x}{x^2-1}$. Factorizamos $x^2-1=(x-1)(x+1)$;
Caso I sobre el residuo: $\frac{2x}{(x-1)(x+1)}=\frac{A}{x-1}+\frac{B}{x+1}$,
$A=B=1$. Integrando:
\[
\int\frac{x^3+x}{x^2-1}\,dx
=\frac{x^2}{2}+\ln|x-1|+\ln|x+1|+C. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Fracciones parciales: fracción impropia]
Calcular $\displaystyle\int\dfrac{x^3+x}{x^2-1}\,dx$.

\begin{myproof}

\textbf{Paso 1: División polinómica.}
$\deg P=3>\deg Q=2$: $x^3+x=(x^2-1)\cdot x+2x$, luego $\dfrac{x^3+x}{x^2-1}=x+\dfrac{2x}{x^2-1}$.

\textbf{Paso 2: Descomponer el residuo.}
$x^2-1=(x-1)(x+1)$; Caso~I: $\dfrac{2x}{(x-1)(x+1)}=\dfrac{A}{x-1}+\dfrac{B}{x+1}$; $A=B=1$.

\textbf{Paso 3: Integrar.}
\[
\boxed{\int\frac{x^3+x}{x^2-1}\,dx
=\frac{x^2}{2}+\ln|x-1|+\ln|x+1|+C.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 25: dx/(x^2(x-1)) (factor lineal repetido) =====
replacements.append((
r"""\begin{example}
Calcular $\displaystyle\int\frac{dx}{x^2(x-1)}$ (factor lineal repetido).
\end{example}

\begin{myproof}
Casos I y II combinados:
\[
\frac{1}{x^2(x-1)}=\frac{A}{x}+\frac{B}{x^2}+\frac{C}{x-1}
\implies 1=Ax(x-1)+B(x-1)+Cx^2.
\]
Con $x=0$: $B=-1$; con $x=1$: $C=1$; con $x=-1$: $A=-1$. Integrando:
\[
\int\frac{dx}{x^2(x-1)}
=-\ln|x|+\frac{1}{x}+\ln|x-1|+C
=\ln\left|\frac{x-1}{x}\right|+\frac{1}{x}+C. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Fracciones parciales: factor lineal repetido]
Calcular $\displaystyle\int\dfrac{dx}{x^2(x-1)}$.

\begin{myproof}

\textbf{Paso 1: Plantear la descomposición (Casos~I y II).}
\[
\frac{1}{x^2(x-1)}=\frac{A}{x}+\frac{B}{x^2}+\frac{C}{x-1}
\implies 1=Ax(x-1)+B(x-1)+Cx^2.
\]

\textbf{Paso 2: Determinar las constantes.}
Con $x=0$: $B=-1$; con $x=1$: $C=1$; con $x=-1$: $A=-1$.

\textbf{Paso 3: Integrar.}
\[
\boxed{\int\frac{dx}{x^2(x-1)}
=\ln\left|\frac{x-1}{x}\right|+\frac{1}{x}+C.}
\]
\end{myproof}
\end{example}"""
))

# ===== APLICAR REEMPLAZOS =====
n_ok = 0
n_err = 0
for i, (old, new) in enumerate(replacements, 1):
    count = text.count(old)
    if count != 1:
        print(f"ERROR ej.{i}: {count} coincidencias. Inicio: {repr(old[:60])}")
        n_err += 1
    else:
        text = text.replace(old, new)
        print(f"OK ej.{i}")
        n_ok += 1

print(f"\nResultado: {n_ok} OK, {n_err} errores.")

if n_err == 0:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Archivo guardado.")
else:
    print("NO se guardó el archivo.")
