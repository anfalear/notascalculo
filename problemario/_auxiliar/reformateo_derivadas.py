# -*- coding: utf-8 -*-
path = r'C:\Users\anfalear\notascalculo\problemario\derivadas.tex'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = []

# ===== EJEMPLO 1: f(x)=x^2 =====
replacements.append((
r"""\begin{example}
Calcular $f'(x)$ para $f(x) = x^2$ usando la definición.
\end{example}

\begin{myproof}
\[
f'(x) = \lim_{h\to 0}\frac{(x+h)^2 - x^2}{h}
= \lim_{h\to 0}\frac{x^2+2xh+h^2-x^2}{h}
= \lim_{h\to 0}\frac{2xh+h^2}{h}
= \lim_{h\to 0}(2x+h) = 2x. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Derivada de $x^2$ por definición]
Calcular $f'(x)$ para $f(x) = x^2$ usando la definición.

\begin{myproof}

\textbf{Paso 1: Plantear el cociente incremental.}
\[
f'(x) = \lim_{h\to 0}\frac{(x+h)^2 - x^2}{h}.
\]

\textbf{Paso 2: Expandir y simplificar.}
\[
= \lim_{h\to 0}\frac{x^2+2xh+h^2-x^2}{h}
= \lim_{h\to 0}\frac{2xh+h^2}{h}
= \lim_{h\to 0}(2x+h).
\]

\textbf{Paso 3: Tomar el límite.}
\[
\boxed{f'(x) = 2x.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 2: f(x)=sqrt(x) =====
replacements.append((
r"""\begin{example}
Calcular $f'(x)$ para $f(x) = \sqrt{x}$ usando la definición.
\end{example}

\begin{myproof}
Racionalizamos el numerador multiplicando por el conjugado:
\[
f'(x) = \lim_{h\to 0}\frac{\sqrt{x+h}-\sqrt{x}}{h}
= \lim_{h\to 0}\frac{(\sqrt{x+h}-\sqrt{x})(\sqrt{x+h}+\sqrt{x})}
  {h(\sqrt{x+h}+\sqrt{x})}
= \lim_{h\to 0}\frac{h}{h(\sqrt{x+h}+\sqrt{x})}
= \frac{1}{2\sqrt{x}}. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Derivada de $\sqrt{x}$ por definición]
Calcular $f'(x)$ para $f(x) = \sqrt{x}$ usando la definición.

\begin{myproof}

\textbf{Paso 1: Plantear el cociente incremental.}
\[
f'(x) = \lim_{h\to 0}\frac{\sqrt{x+h}-\sqrt{x}}{h}.
\]

\textbf{Paso 2: Racionalizar el numerador.}
\[
= \lim_{h\to 0}\frac{(\sqrt{x+h}-\sqrt{x})(\sqrt{x+h}+\sqrt{x})}
  {h(\sqrt{x+h}+\sqrt{x})}
= \lim_{h\to 0}\frac{h}{h(\sqrt{x+h}+\sqrt{x})}.
\]

\textbf{Paso 3: Tomar el límite.}
\[
\boxed{f'(x) = \frac{1}{2\sqrt{x}}.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 3: regla del producto =====
replacements.append((
r"""\begin{example}
Derivar $f(x) = (3x^2-5x+1)(2x^3+x)$.
\end{example}

\begin{myproof}
Por la regla del producto con $u=3x^2-5x+1$, $v=2x^3+x$:
\[
f'(x) = (6x-5)(2x^3+x)+(3x^2-5x+1)(6x^2+1).
\]
Expandiendo y simplificando:
\[
f'(x) = 12x^4+6x^2-10x^3-5x+18x^4+3x^2-30x^3-5x+6x^2+1
= 30x^4-40x^3+15x^2-10x+1. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Regla del producto]
Derivar $f(x) = (3x^2-5x+1)(2x^3+x)$.

\begin{myproof}

\textbf{Paso 1: Identificar los factores.}
$u=3x^2-5x+1$, $v=2x^3+x$; $u'=6x-5$, $v'=6x^2+1$.

\textbf{Paso 2: Aplicar la regla del producto.}
\[
f'(x) = (6x-5)(2x^3+x)+(3x^2-5x+1)(6x^2+1).
\]

\textbf{Paso 3: Expandir y simplificar.}
\[
\boxed{f'(x) = 30x^4-40x^3+15x^2-10x+1.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 4: regla del cociente =====
replacements.append((
r"""\begin{example}
Derivar $f(x) = \dfrac{x^2+3}{x^3-1}$.
\end{example}

\begin{myproof}
Por la regla del cociente:
\[
f'(x) = \frac{(x^3-1)(2x)-(x^2+3)(3x^2)}{(x^3-1)^2}
= \frac{2x^4-2x-3x^4-9x^2}{(x^3-1)^2}
= \frac{-x^4-9x^2-2x}{(x^3-1)^2}. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Regla del cociente]
Derivar $f(x) = \dfrac{x^2+3}{x^3-1}$.

\begin{myproof}

\textbf{Paso 1: Aplicar la regla del cociente.}
\[
f'(x) = \frac{(x^3-1)(2x)-(x^2+3)(3x^2)}{(x^3-1)^2}.
\]

\textbf{Paso 2: Simplificar el numerador.}
\[
\boxed{f'(x) = \frac{-x^4-9x^2-2x}{(x^3-1)^2}.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 5: D_x(sin x) = cos x  (ESPECIAL: una sola línea) =====
replacements.append((
r"""\begin{example} Demuestre que $D_x(\sin x) = \cos x$\end{example}

\begin{myproof}
Por definición y la identidad de suma del seno:
\begin{align*}
D_x(\sin x)
&= \lim_{h\to 0}\frac{\sin(x+h)-\sin x}{h}
= \lim_{h\to 0}\frac{\sin x\cos h+\cos x\sin h-\sin x}{h}\\
&= \lim_{h\to 0}\left[\sin x\cdot\frac{\cos h-1}{h}
  +\cos x\cdot\frac{\sin h}{h}\right].
\end{align*}
Aplicando los límites trigonométricas fundamentales
$\lim_{h\to 0}\frac{\sin h}{h}=1$ y $\lim_{h\to 0}\frac{\cos h-1}{h}=0$:
\[
D_x(\sin x) = \sin x\cdot 0 + \cos x\cdot 1 = \cos x. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Derivada de $\sin x$ por definición]
Demuestre que $D_x(\sin x) = \cos x$.

\begin{myproof}

\textbf{Paso 1: Aplicar la identidad de suma del seno.}
\begin{align*}
D_x(\sin x)
&= \lim_{h\to 0}\frac{\sin(x+h)-\sin x}{h}
= \lim_{h\to 0}\frac{\sin x\cos h+\cos x\sin h-\sin x}{h}\\
&= \lim_{h\to 0}\left[\sin x\cdot\frac{\cos h-1}{h}
  +\cos x\cdot\frac{\sin h}{h}\right].
\end{align*}

\textbf{Paso 2: Aplicar los límites trigonométricos fundamentales.}
\[
\boxed{D_x(\sin x) = \sin x\cdot 0 + \cos x\cdot 1 = \cos x.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 6: sin(x^2) =====
replacements.append((
r"""\begin{example}
Derivar $y = \sin(x^2)$.
\end{example}

\begin{myproof}
$f(u)=\sin u$, $g(x)=x^2$; $f'(u)=\cos u$, $g'(x)=2x$:
\[
y' = \cos(x^2)\cdot 2x = 2x\cos(x^2). \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Regla de la cadena: $\sin(x^2)$]
Derivar $y = \sin(x^2)$.

\begin{myproof}

\textbf{Paso 1: Identificar las capas.}
$f(u)=\sin u$, $g(x)=x^2$; $f'(u)=\cos u$, $g'(x)=2x$.

\textbf{Paso 2: Aplicar la regla de la cadena.}
\[
\boxed{y' = \cos(x^2)\cdot 2x = 2x\cos(x^2).}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 7: (3x^2+5)^10 =====
replacements.append((
r"""\begin{example}
Derivar $y = (3x^2+5)^{10}$.
\end{example}

\begin{myproof}
$f(u)=u^{10}$, $g(x)=3x^2+5$:
\[
y' = 10(3x^2+5)^9\cdot 6x = 60x(3x^2+5)^9. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Regla de la cadena: $(3x^2+5)^{10}$]
Derivar $y = (3x^2+5)^{10}$.

\begin{myproof}

\textbf{Paso 1: Identificar las capas.}
$f(u)=u^{10}$, $g(x)=3x^2+5$; $f'(u)=10u^9$, $g'(x)=6x$.

\textbf{Paso 2: Aplicar la regla de la cadena.}
\[
\boxed{y' = 10(3x^2+5)^9\cdot 6x = 60x(3x^2+5)^9.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 8: sqrt(sin(e^x)) =====
replacements.append((
r"""\begin{example}
Derivar $y = \sqrt{\sin(e^x)}$.
\end{example}

\begin{myproof}
Tres capas: $f(u)=\sqrt{u}$, $g(v)=\sin v$, $p(x)=e^x$:
\[
y' = \frac{1}{2\sqrt{\sin(e^x)}}\cdot\cos(e^x)\cdot e^x
= \frac{e^x\cos(e^x)}{2\sqrt{\sin(e^x)}}. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Regla de la cadena: $\sqrt{\sin(e^x)}$]
Derivar $y = \sqrt{\sin(e^x)}$.

\begin{myproof}

\textbf{Paso 1: Identificar las tres capas.}
$f(u)=\sqrt{u}$, $g(v)=\sin v$, $p(x)=e^x$.

\textbf{Paso 2: Aplicar la regla de la cadena.}
\[
\boxed{y' = \frac{1}{2\sqrt{\sin(e^x)}}\cdot\cos(e^x)\cdot e^x
= \frac{e^x\cos(e^x)}{2\sqrt{\sin(e^x)}}.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 9: tan^3(5x)  (\qquad\square en línea propia) =====
replacements.append((
r"""\begin{example}
Derivar $y = \tan^3(5x)$.
\end{example}

\begin{myproof}
Reescribimos $y = [\tan(5x)]^3$; tres capas: potencia, tangente, lineal:
\[
y' = 3\tan^2(5x)\cdot\sec^2(5x)\cdot 5 = 15\tan^2(5x)\sec^2(5x).
\qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Regla de la cadena: $\tan^3(5x)$]
Derivar $y = \tan^3(5x)$.

\begin{myproof}

\textbf{Paso 1: Reescribir e identificar las capas.}
$y = [\tan(5x)]^3$; tres capas: potencia, tangente, función lineal.

\textbf{Paso 2: Aplicar la regla de la cadena.}
\[
\boxed{y' = 3\tan^2(5x)\cdot\sec^2(5x)\cdot 5 = 15\tan^2(5x)\sec^2(5x).}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 10: D_x(ln x) = 1/x  ($\square fuera de math) =====
replacements.append((
r"""\begin{example}
Demuestre que $D_x(\ln x) = \frac{1}{x}.$
\end{example}

\begin{myproof}
\begin{align*}
D_x(\ln x) &= \lim_{h\to 0}\frac{\ln(x+h)-\ln x}{h}
= \lim_{h\to 0}\frac{1}{h}\ln\!\left(\frac{x+h}{x}\right)
= \lim_{h\to 0}\frac{1}{x}\cdot\frac{x}{h}\ln\!\left(1+\frac{h}{x}\right).
\end{align*}
Sea $t = \frac{h}{x}$; cuando $h\to 0$, $t\to 0$:
\[
= \frac{1}{x}\lim_{t\to 0}\frac{\ln(1+t)}{t} = \frac{1}{x}\cdot 1
= \frac{1}{x},
\]
donde se usó la equivalencia $\ln(1+t)\sim t$ demostrada en el capítulo
anterior. $\square$
\end{myproof}""",
r"""\begin{example}[Derivada de $\ln x$ por definición]
Demuestre que $D_x(\ln x) = \dfrac{1}{x}$.

\begin{myproof}

\textbf{Paso 1: Plantear el cociente incremental y simplificar.}
\begin{align*}
D_x(\ln x) &= \lim_{h\to 0}\frac{\ln(x+h)-\ln x}{h}
= \lim_{h\to 0}\frac{1}{h}\ln\!\left(\frac{x+h}{x}\right)
= \lim_{h\to 0}\frac{1}{x}\cdot\frac{x}{h}\ln\!\left(1+\frac{h}{x}\right).
\end{align*}

\textbf{Paso 2: Cambiar variable y aplicar el límite fundamental.}
Sea $t = \frac{h}{x}$; cuando $h\to 0$, $t\to 0$:
\[
= \frac{1}{x}\lim_{t\to 0}\frac{\ln(1+t)}{t} = \frac{1}{x}\cdot 1.
\]

\textbf{Paso 3: Concluir.}
\[
\boxed{D_x(\ln x) = \frac{1}{x}.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 11: e^{3x^2-1} =====
replacements.append((
r"""\begin{example}
Derivar $f(x) = e^{3x^2-1}$.
\end{example}

\begin{myproof}
Regla de la cadena con $u=3x^2-1$:
$f'(x) = e^{3x^2-1}\cdot 6x = 6xe^{3x^2-1}$. $\square$
\end{myproof}""",
r"""\begin{example}[Derivada de $e^{3x^2-1}$]
Derivar $f(x) = e^{3x^2-1}$.

\begin{myproof}

\textbf{Paso 1: Aplicar la regla de la cadena con $u=3x^2-1$.}
\[
\boxed{f'(x) = e^{3x^2-1}\cdot 6x = 6xe^{3x^2-1}.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 12: ln(sin x) =====
replacements.append((
r"""\begin{example}
Derivar $f(x) = \ln(\sin x)$.
\end{example}

\begin{myproof}
$f'(x) = \dfrac{1}{\sin x}\cdot\cos x = \cot x$. $\square$
\end{myproof}""",
r"""\begin{example}[Derivada de $\ln(\sin x)$]
Derivar $f(x) = \ln(\sin x)$.

\begin{myproof}

\textbf{Paso 1: Aplicar la regla de la cadena.}
\[
\boxed{f'(x) = \dfrac{1}{\sin x}\cdot\cos x = \cot x.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 13: x^2 * 3^x =====
replacements.append((
r"""\begin{example}
Derivar $f(x) = x^2\cdot 3^x$.
\end{example}

\begin{myproof}
Regla del producto:
$f'(x) = 2x\cdot 3^x + x^2\cdot 3^x\ln 3 = x\,3^x(2+x\ln 3)$. $\square$
\end{myproof}""",
r"""\begin{example}[Derivada de $x^2\cdot 3^x$]
Derivar $f(x) = x^2\cdot 3^x$.

\begin{myproof}

\textbf{Paso 1: Aplicar la regla del producto.}
\[
\boxed{f'(x) = 2x\cdot 3^x + x^2\cdot 3^x\ln 3 = x\,3^x(2+x\ln 3).}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 14: derivadas de orden superior =====
replacements.append((
r"""\begin{example}
Sea $y = x^4 - 3x^3 + 2x$. Calcular todas las derivadas no nulas.
\end{example}

\begin{myproof}
\[
y' = 4x^3-9x^2+2, \quad y'' = 12x^2-18x, \quad y''' = 24x-18,
\quad y^{(4)} = 24, \quad y^{(5)} = 0. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Derivadas de orden superior de un polinomio]
Sea $y = x^4 - 3x^3 + 2x$. Calcular todas las derivadas no nulas.

\begin{myproof}

\textbf{Paso 1: Derivar sucesivamente.}
\[
y' = 4x^3-9x^2+2, \quad y'' = 12x^2-18x, \quad y''' = 24x-18.
\]

\textbf{Paso 2: Continuar hasta anularse.}
\[
\boxed{y^{(4)} = 24, \quad y^{(5)} = 0.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 15: y=e^x sin x satisface EDO =====
replacements.append((
r"""\begin{example}
Demostrar que $y = e^x\sin x$ satisface $y''-2y'+2y=0$.
\end{example}

\begin{myproof}
$y' = e^x\sin x + e^x\cos x = e^x(\sin x+\cos x)$.
$y'' = e^x(\sin x+\cos x)+e^x(\cos x-\sin x) = 2e^x\cos x$.
Sustituyendo:
\[
y''-2y'+2y = 2e^x\cos x - 2e^x(\sin x+\cos x) + 2e^x\sin x
= 2e^x\cos x - 2e^x\cos x = 0. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Verificación de una ecuación diferencial]
Demostrar que $y = e^x\sin x$ satisface $y''-2y'+2y=0$.

\begin{myproof}

\textbf{Paso 1: Calcular $y'$ y $y''$.}
\[
y' = e^x(\sin x+\cos x), \qquad y'' = 2e^x\cos x.
\]

\textbf{Paso 2: Sustituir y verificar.}
\[
\boxed{y''-2y'+2y = 2e^x\cos x - 2e^x(\sin x+\cos x) + 2e^x\sin x = 0.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 16: folio de Descartes (\qquad\square en línea propia) =====
replacements.append((
r"""\begin{example}
Encontrar $\dfrac{dy}{dx}$ para $x^3+y^3 = 6xy.$ Esta ecuación es conocida como el folio de Descartes.
\end{example}

\begin{myproof}
Derivando implícitamente:
\[
3x^2 + 3y^2\frac{dy}{dx} = 6y + 6x\frac{dy}{dx}.
\]
Agrupando y factorizando:
\[
(3y^2-6x)\frac{dy}{dx} = 6y-3x^2
\implies
\frac{dy}{dx} = \frac{6y-3x^2}{3y^2-6x} = \frac{2y-x^2}{y^2-2x}.
\qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Derivación implícita: folio de Descartes]
Encontrar $\dfrac{dy}{dx}$ para $x^3+y^3 = 6xy$ (folio de Descartes).

\begin{myproof}

\textbf{Paso 1: Derivar implícitamente.}
\[
3x^2 + 3y^2\frac{dy}{dx} = 6y + 6x\frac{dy}{dx}.
\]

\textbf{Paso 2: Agrupar y despejar.}
\[
(3y^2-6x)\frac{dy}{dx} = 6y-3x^2
\implies
\boxed{\frac{dy}{dx} = \frac{2y-x^2}{y^2-2x}.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 17: y^4+xy=1 =====
replacements.append((
r"""\begin{example}
Encontrar $\dfrac{dy}{dx}$ para $y^4+xy = 1$.
\end{example}

\begin{myproof}
\[
4y^3\frac{dy}{dx} + y + x\frac{dy}{dx} = 0
\implies
(4y^3+x)\frac{dy}{dx} = -y
\implies
\frac{dy}{dx} = \frac{-y}{4y^3+x}. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Derivación implícita: $y^4+xy=1$]
Encontrar $\dfrac{dy}{dx}$ para $y^4+xy = 1$.

\begin{myproof}

\textbf{Paso 1: Derivar implícitamente y agrupar.}
\[
4y^3\frac{dy}{dx} + y + x\frac{dy}{dx} = 0
\implies
(4y^3+x)\frac{dy}{dx} = -y.
\]

\textbf{Paso 2: Despejar.}
\[
\boxed{\frac{dy}{dx} = \frac{-y}{4y^3+x}.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 18: tangente a x^2+y^2=25 =====
replacements.append((
r"""\begin{example}
Encontrar la ecuación de la recta tangente a $x^2+y^2=25$ en el punto
$(3,4)$.
\end{example}

\begin{myproof}
Derivando: $2x+2y\frac{dy}{dx}=0$, así que $\frac{dy}{dx}=-\frac{x}{y}$. En el punto $(3,4)$, la pendiente de la recta es $ -\frac{3}{4}$ y así la ecuación de la tangente es:
\[
y-4 = -\frac{3}{4}(x-3) \implies 3x+4y = 25. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Recta tangente a una circunferencia]
Encontrar la ecuación de la recta tangente a $x^2+y^2=25$ en el punto $(3,4)$.

\begin{myproof}

\textbf{Paso 1: Hallar la pendiente por derivación implícita.}
\[
2x+2y\frac{dy}{dx}=0 \implies \frac{dy}{dx}=-\frac{x}{y}.
\quad\text{En }(3,4):\quad m = -\frac{3}{4}.
\]

\textbf{Paso 2: Escribir la ecuación de la tangente.}
\[
y-4 = -\frac{3}{4}(x-3) \implies \boxed{3x+4y = 25.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 19: (f^{-1})'(2) para f(x)=x^3+x  (SIN línea en blanco entre \end{example} y \begin{myproof}) =====
replacements.append((
r"""\begin{example}
Sea $f(x) = x^3 + x$. Calcula la derivada de la función inversa en el punto
$x = 2$, es decir, halla $(f^{-1})'(2)$.
\end{example}
\begin{myproof}

Sabemos por el teorema de la derivada de la función inversa que:
\[
    (f^{-1})'(2) = \frac{1}{f'(f^{-1}(2))}
\]
Primero, necesitamos encontrar el valor de $f^{-1}(2)$. Esto equivale a
encontrar el valor de $x$ tal que $f(x) = 2$:
\[
    x^3 + x = 2
\]
Por inspección, es fácil ver que $x = 1$ es una solución, ya que
$1^3 + 1 = 2$. Como la derivada $f'(x) = 3x^2 + 1$ es estrictamente
positiva para todo número real, la función $f$ es estrictamente creciente
e inyectiva. Por lo tanto, $x = 1$ es la única solución y $f^{-1}(2) = 1$.

A continuación, calculamos la derivada de $f(x)$:
\[
    f'(x) = 3x^2 + 1
\]
Evaluamos la derivada en el punto encontrado, $x = 1$:
\[
    f'(1) = 3(1)^2 + 1 = 4
\]
Finalmente, sustituimos este valor en la fórmula del teorema:
\[
    (f^{-1})'(2) = \frac{1}{f'(1)} = \frac{1}{4}
\]
\end{myproof}""",
r"""\begin{example}[Derivada de la función inversa: $f(x)=x^3+x$]
Sea $f(x) = x^3 + x$. Calcula la derivada de la función inversa en el punto $x = 2$, es decir, halla $(f^{-1})'(2)$.

\begin{myproof}

\textbf{Paso 1: Hallar $f^{-1}(2)$.}
Resolver $x^3 + x = 2$: por inspección $x=1$ (ya que $1^3+1=2$). Como $f'(x)=3x^2+1>0$, $f$ es inyectiva, luego $f^{-1}(2)=1$.

\textbf{Paso 2: Calcular $f'(1)$.}
\[
    f'(x) = 3x^2 + 1, \qquad f'(1) = 4.
\]

\textbf{Paso 3: Aplicar la fórmula de la derivada de la inversa.}
\[
    \boxed{(f^{-1})'(2) = \frac{1}{f'(1)} = \frac{1}{4}.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 20: (f^{-1})'(1) para f(x)=e^x+x  (SIN línea en blanco entre \end{example} y \begin{myproof}) =====
replacements.append((
r"""\begin{example}
Sea $f(x) = e^x + x$. Halla el valor de $(f^{-1})'(1)$.
\end{example}
\begin{myproof}

Nuevamente, aplicamos la fórmula de la derivada de la función inversa:
\[
    (f^{-1})'(1) = \frac{1}{f'(f^{-1}(1))}
\]
Primero buscamos $f^{-1}(1)$, lo que requiere resolver la ecuación
$f(x) = 1$:
\[
    e^x + x = 1
\]
Observamos que si $x = 0$, la ecuación se satisface puesto que
$e^0 + 0 = 1 + 0 = 1$. Dado que $f(x)$ es la suma de dos funciones
estrictamente crecientes, también es estrictamente creciente e inyectiva.
Así, deducimos que $f^{-1}(1) = 0$.

Luego, derivamos la función original $f(x)$:
\[
    f'(x) = e^x + 1
\]
Evaluamos dicha derivada en $x = 0$:
\[
    f'(0) = e^0 + 1 = 1 + 1 = 2
\]
Para concluir, sustituimos este resultado en la fórmula del teorema:
\[
    (f^{-1})'(1) = \frac{1}{f'(0)} = \frac{1}{2}
\]
\end{myproof}""",
r"""\begin{example}[Derivada de la función inversa: $f(x)=e^x+x$]
Sea $f(x) = e^x + x$. Halla el valor de $(f^{-1})'(1)$.

\begin{myproof}

\textbf{Paso 1: Hallar $f^{-1}(1)$.}
Resolver $e^x + x = 1$: $x=0$ satisface $e^0+0=1$. Como $f'(x)=e^x+1>0$, $f$ es inyectiva, luego $f^{-1}(1)=0$.

\textbf{Paso 2: Calcular $f'(0)$.}
\[
    f'(x) = e^x + 1, \qquad f'(0) = 2.
\]

\textbf{Paso 3: Aplicar la fórmula de la derivada de la inversa.}
\[
    \boxed{(f^{-1})'(1) = \frac{1}{f'(0)} = \frac{1}{2}.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 21: derivación logarítmica fracción (\qquad\square en línea propia L705) =====
replacements.append((
r"""\begin{example}
Derivar $y = \dfrac{x^{3/4}\sqrt{x^2+1}}{(3x+2)^5}$.
\end{example}

\begin{myproof}
Tomamos $\ln y = \frac{3}{4}\ln x + \frac{1}{2}\ln(x^2+1) - 5\ln(3x+2)$.
Derivando implícitamente:
\[
\frac{y'}{y} = \frac{3}{4x} + \frac{x}{x^2+1} - \frac{15}{3x+2}.
\]
Multiplicando por $y$:
\[
y' = \frac{x^{3/4}\sqrt{x^2+1}}{(3x+2)^5}
\left(\frac{3}{4x} + \frac{x}{x^2+1} - \frac{15}{3x+2}\right).
\qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Derivación logarítmica: fracción con raíces y potencias]
Derivar $y = \dfrac{x^{3/4}\sqrt{x^2+1}}{(3x+2)^5}$.

\begin{myproof}

\textbf{Paso 1: Tomar logaritmo natural y simplificar.}
\[
\ln y = \frac{3}{4}\ln x + \frac{1}{2}\ln(x^2+1) - 5\ln(3x+2).
\]

\textbf{Paso 2: Derivar implícitamente.}
\[
\frac{y'}{y} = \frac{3}{4x} + \frac{x}{x^2+1} - \frac{15}{3x+2}.
\]

\textbf{Paso 3: Multiplicar por $y$.}
\[
\boxed{y' = \frac{x^{3/4}\sqrt{x^2+1}}{(3x+2)^5}
\left(\frac{3}{4x} + \frac{x}{x^2+1} - \frac{15}{3x+2}\right).}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 22: y=x^x =====
replacements.append((
r"""\begin{example}
Derivar $y = x^x$ \quad $(x>0)$.
\end{example}

\begin{myproof}
$\ln y = x\ln x$. Derivando implícitamente:
\[
\frac{y'}{y} = \ln x + x\cdot\frac{1}{x} = \ln x+1.
\]
\[
y' = x^x(\ln x+1). \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Derivación logarítmica: $y = x^x$]
Derivar $y = x^x$ \quad $(x>0)$.

\begin{myproof}

\textbf{Paso 1: Tomar logaritmo.}
\[
\ln y = x\ln x.
\]

\textbf{Paso 2: Derivar implícitamente y despejar.}
\[
\frac{y'}{y} = \ln x + 1 \implies
\boxed{y' = x^x(\ln x+1).}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 23: y=(sin x)^{cos x}  (\qquad\square al final de L735) =====
replacements.append((
r"""\begin{example}
Derivar $y = (\sin x)^{\cos x}$.
\end{example}

\begin{myproof}
$\ln y = \cos x\cdot\ln(\sin x)$. Derivando:
\[
\frac{y'}{y} = -\sin x\ln(\sin x)+\cos x\cdot\frac{\cos x}{\sin x}
= -\sin x\ln(\sin x)+\frac{\cos^2 x}{\sin x}.
\]
\[
y' = (\sin x)^{\cos x}\!\left(\frac{\cos^2 x}{\sin x}
-\sin x\ln(\sin x)\right). \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Derivación logarítmica: $y = (\sin x)^{\cos x}$]
Derivar $y = (\sin x)^{\cos x}$.

\begin{myproof}

\textbf{Paso 1: Tomar logaritmo y derivar implícitamente.}
\[
\ln y = \cos x\cdot\ln(\sin x) \implies
\frac{y'}{y} = -\sin x\ln(\sin x)+\frac{\cos^2 x}{\sin x}.
\]

\textbf{Paso 2: Despejar $y'$.}
\[
\boxed{y' = (\sin x)^{\cos x}\!\left(\frac{\cos^2 x}{\sin x}
-\sin x\ln(\sin x)\right).}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 24: D_x(arcsin x) =====
replacements.append((
r"""\begin{example}
Demuestre que $D_x(\arcsin x) = \frac{1}{\sqrt{1-x^2}}$
\end{example}

\begin{myproof}
Sea $y=\arcsin x$, de modo que $\sin y = x$ con $y\in\left[-\frac{\pi}{2},
\frac{\pi}{2}\right]$. Derivando implícitamente respecto a $x$:
\[
\cos y\cdot\frac{dy}{dx} = 1 \implies \frac{dy}{dx} = \frac{1}{\cos y}.
\]
En el intervalo considerado, $\cos y \geq 0$, por lo que
$\cos y = \sqrt{1-\sin^2 y} = \sqrt{1-x^2}$. Sustituyendo:
\[
D_x(\arcsin x) = \frac{1}{\sqrt{1-x^2}}. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Derivada de $\arcsin x$ por derivación implícita]
Demuestre que $D_x(\arcsin x) = \dfrac{1}{\sqrt{1-x^2}}$.

\begin{myproof}

\textbf{Paso 1: Reformular y derivar implícitamente.}
Sea $y=\arcsin x$, es decir, $\sin y = x$ con $y\in\left[-\frac{\pi}{2},
\frac{\pi}{2}\right]$:
\[
\cos y\cdot\frac{dy}{dx} = 1 \implies \frac{dy}{dx} = \frac{1}{\cos y}.
\]

\textbf{Paso 2: Eliminar $y$ con la identidad pitagórica.}
En el intervalo dado $\cos y \geq 0$, luego
$\cos y = \sqrt{1-\sin^2 y} = \sqrt{1-x^2}$.

\textbf{Paso 3: Sustituir.}
\[
\boxed{D_x(\arcsin x) = \frac{1}{\sqrt{1-x^2}}.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 25: arctan(x^2)  (ESPECIAL: contenido en misma línea que \begin{myproof}) =====
replacements.append((
r"""\begin{example}
Derive $f(x)=\arctan(x^2)$.
\end{example}

\begin{myproof} Aplicando la regla de la cadena:
$f'(x) = \dfrac{1}{1+(x^2)^2}\cdot 2x = \dfrac{2x}{1+x^4}$. $\square$
\end{myproof}""",
r"""\begin{example}[Derivada de $\arctan(x^2)$]
Derive $f(x)=\arctan(x^2)$.

\begin{myproof}

\textbf{Paso 1: Aplicar la regla de la cadena.}
\[
\boxed{f'(x) = \dfrac{1}{1+(x^2)^2}\cdot 2x = \dfrac{2x}{1+x^4}.}
\]
\end{myproof}
\end{example}"""
))

# ===== EJEMPLO 26: x arcsin x + sqrt(1-x^2) =====
replacements.append((
r"""\begin{example}
Derivar $f(x) = x\arcsin x + \sqrt{1-x^2}$.
\end{example}

\begin{myproof}
\[
f'(x) = \arcsin x + \frac{x}{\sqrt{1-x^2}} + \frac{-2x}{2\sqrt{1-x^2}}
= \arcsin x + \frac{x}{\sqrt{1-x^2}} - \frac{x}{\sqrt{1-x^2}}
= \arcsin x. \qquad\square
\]
\end{myproof}""",
r"""\begin{example}[Derivada con arco seno]
Derivar $f(x) = x\arcsin x + \sqrt{1-x^2}$.

\begin{myproof}

\textbf{Paso 1: Derivar término a término.}
\[
f'(x) = \arcsin x + \frac{x}{\sqrt{1-x^2}} + \frac{-2x}{2\sqrt{1-x^2}}
= \arcsin x + \frac{x}{\sqrt{1-x^2}} - \frac{x}{\sqrt{1-x^2}}.
\]

\textbf{Paso 2: Simplificar.}
\[
\boxed{f'(x) = \arcsin x.}
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
        print(f"ERROR ej.{i}: se encontraron {count} coincidencias (esperaba 1).")
        print(f"  Inicio del old: {repr(old[:60])}")
        n_err += 1
    else:
        text = text.replace(old, new)
        print(f"OK ej.{i}")
        n_ok += 1

print(f"\nResultado: {n_ok} reemplazos OK, {n_err} errores.")

if n_err == 0:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Archivo guardado.")
else:
    print("NO se guardó el archivo debido a errores.")
