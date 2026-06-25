# -*- coding: utf-8 -*-
path = r'C:\Users\anfalear\notascalculo\problemario\intdefinida.tex'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = []

# Ej.1 — Riemann sums for int_{-2}^{3}(x+3)dx
old1 = r"""\begin{example}
Evaluar $\displaystyle\int_{-2}^{3} (x+3)\,dx$ como límite de sumas de Riemann usando puntos derechos.
\end{example}

\begin{myproof}
Tomamos una partición regular con $n$ subintervalos: $\Delta x = \frac{3-(-2)}{n} = \frac{5}{n}$ y puntos derechos $x_i = -2 + i\,\Delta x = -2 + \frac{5i}{n}$. La suma de Riemann es
\[
R_n = \sum_{i=1}^{n} f(x_i)\,\Delta x
= \sum_{i=1}^{n} \left[\left(-2+\frac{5i}{n}\right)+3\right]\frac{5}{n}
= \frac{5}{n}\sum_{i=1}^{n}\left(1 + \frac{5i}{n}\right).
\]
Separamos la suma usando linealidad:
\[
R_n = \frac{5}{n}\left[\sum_{i=1}^{n}1 + \frac{5}{n}\sum_{i=1}^{n}i\right]
= \frac{5}{n}\left[n + \frac{5}{n}\cdot\frac{n(n+1)}{2}\right]
= 5 + \frac{25(n+1)}{2n}
= 5 + \frac{25}{2}\left(1+\frac{1}{n}\right).
\]
Tomando el límite cuando $n \to \infty$:
\[
\int_{-2}^{3}(x+3)\,dx = \lim_{n\to\infty} R_n = 5 + \frac{25}{2} = \frac{35}{2}.
\]
Este resultado puede verificarse geométricamente: la región es un trapecio de bases $f(-2)=1$ y $f(3)=6$ y altura $5$, cuya área es $\frac{(1+6)\cdot 5}{2} = \frac{35}{2}$. $\square$
\end{myproof}"""

new1 = r"""\begin{example}[Integral definida como límite de sumas de Riemann]
Evaluar $\displaystyle\int_{-2}^{3} (x+3)\,dx$ como límite de sumas de Riemann usando puntos derechos.

\begin{myproof}

\textbf{Paso 1: Establecer la partición y los puntos muestrales.}

Tomamos una partición regular con $n$ subintervalos: $\Delta x = \frac{3-(-2)}{n} = \frac{5}{n}$ y puntos derechos $x_i = -2 + i\,\Delta x = -2 + \frac{5i}{n}$. La suma de Riemann es
\[
R_n = \sum_{i=1}^{n} f(x_i)\,\Delta x
= \sum_{i=1}^{n} \left[\left(-2+\frac{5i}{n}\right)+3\right]\frac{5}{n}
= \frac{5}{n}\sum_{i=1}^{n}\left(1 + \frac{5i}{n}\right).
\]

\textbf{Paso 2: Simplificar usando fórmulas de sumatoria.}
\[
R_n = \frac{5}{n}\left[\sum_{i=1}^{n}1 + \frac{5}{n}\sum_{i=1}^{n}i\right]
= \frac{5}{n}\left[n + \frac{5}{n}\cdot\frac{n(n+1)}{2}\right]
= 5 + \frac{25(n+1)}{2n}
= 5 + \frac{25}{2}\left(1+\frac{1}{n}\right).
\]

\textbf{Paso 3: Tomar el límite.}
\[
\boxed{\int_{-2}^{3}(x+3)\,dx = \lim_{n\to\infty} R_n = 5 + \frac{25}{2} = \frac{35}{2}.}
\]
Este resultado puede verificarse geométricamente: la región es un trapecio de bases $f(-2)=1$ y $f(3)=6$ y altura $5$, cuya área es $\frac{(1+6)\cdot 5}{2} = \frac{35}{2}$.
\end{myproof}
\end{example}"""

replacements.append((old1, new1))

# Ej.2 — Acotar int_2^4 x^2 dx
old2 = r"""\begin{example}
Acotar $\displaystyle\int_{2}^{4} x^2\,dx$ sin calcularla directamente.
\end{example}

\begin{myproof}
En $[2,4]$, la función $f(x) = x^2$ es creciente, por lo que $m = f(2) = 4$ y $M = f(4) = 16$. Por la propiedad de acotamiento:
\[
4(4-2) \leq \int_{2}^{4} x^2\,dx \leq 16(4-2), \qquad \text{es decir}, \qquad 8 \leq \int_{2}^{4} x^2\,dx \leq 32.
\]
El valor exacto es $\left[\frac{x^3}{3}\right]_2^4 = \frac{64}{3} - \frac{8}{3} = \frac{56}{3} \approx 18.67$, que efectivamente cae en el intervalo $[8,32]$. $\square$
\end{myproof}"""

new2 = r"""\begin{example}[Acotamiento de una integral definida]
Acotar $\displaystyle\int_{2}^{4} x^2\,dx$ sin calcularla directamente.

\begin{myproof}

\textbf{Paso 1: Identificar el mínimo y máximo de $f$ en $[2,4]$.}

En $[2,4]$, la función $f(x) = x^2$ es creciente, por lo que $m = f(2) = 4$ y $M = f(4) = 16$.

\textbf{Paso 2: Aplicar la propiedad de acotamiento.}
\[
4(4-2) \leq \int_{2}^{4} x^2\,dx \leq 16(4-2), \qquad \text{es decir}:
\]
\[
\boxed{8 \leq \int_{2}^{4} x^2\,dx \leq 32.}
\]
El valor exacto es $\left[\frac{x^3}{3}\right]_2^4 = \frac{64}{3} - \frac{8}{3} = \frac{56}{3} \approx 18.67$, que efectivamente cae en el intervalo $[8,32]$.
\end{myproof}
\end{example}"""

replacements.append((old2, new2))

# Ej.3 — TFC1: F(x) = int_1^x t^3 dt
old3 = r"""\begin{example}
Si $F(x) = \int_{1}^{x} t^3\,dt$, calcular $F'(x)$.
\end{example}

\begin{myproof}
Por el TFC1, simplemente se sustituye $t = x$ en el integrando: $F'(x) = x^3$. $\square$
\end{myproof}"""

new3 = r"""\begin{example}[Derivada de una función de acumulación (TFC1)]
Si $F(x) = \int_{1}^{x} t^3\,dt$, calcular $F'(x)$.

\begin{myproof}

\textbf{Paso 1: Aplicar el TFC1.}

Por el TFC1, simplemente se sustituye $t = x$ en el integrando:
\[
\boxed{F'(x) = x^3.}
\]
\end{myproof}
\end{example}"""

replacements.append((old3, new3))

# Ej.4 — TFC1 with chain rule: d/dx int_2^{x^2}
old4 = r"""\begin{example}
Calcular $\dfrac{d}{dx}\displaystyle\int_{2}^{x^2} \frac{t^{3/2}}{\sqrt{t^2+17}}\,dt$.
\end{example}

\begin{myproof}
El límite superior es $u(x) = x^2$, una función de $x$. Definimos $G(u) = \int_2^u \frac{t^{3/2}}{\sqrt{t^2+17}}\,dt$, de modo que la expresión pedida es $G(u(x))$. Por regla de la cadena:
\[
\frac{d}{dx}G(u(x)) = G'(u)\cdot u'(x) = \frac{(x^2)^{3/2}}{\sqrt{(x^2)^2+17}}\cdot 2x = \frac{2x^4}{\sqrt{x^4+17}}. \qquad \square
\]
\end{myproof}"""

new4 = r"""\begin{example}[TFC1 con regla de la cadena]
Calcular $\dfrac{d}{dx}\displaystyle\int_{2}^{x^2} \frac{t^{3/2}}{\sqrt{t^2+17}}\,dt$.

\begin{myproof}

\textbf{Paso 1: Identificar el límite superior variable y definir la función auxiliar.}

El límite superior es $u(x) = x^2$, una función de $x$. Definimos $G(u) = \int_2^u \frac{t^{3/2}}{\sqrt{t^2+17}}\,dt$, de modo que la expresión pedida es $G(u(x))$.

\textbf{Paso 2: Aplicar TFC1 y la regla de la cadena.}
\[
\boxed{\frac{d}{dx}\int_{2}^{x^2} \frac{t^{3/2}}{\sqrt{t^2+17}}\,dt = \frac{(x^2)^{3/2}}{\sqrt{(x^2)^2+17}}\cdot 2x = \frac{2x^4}{\sqrt{x^4+17}}.}
\]
\end{myproof}
\end{example}"""

replacements.append((old4, new4))

# Ej.5 — TFC2: int_0^2 (2x^2-3x+2) dx
old5 = r"""\begin{example}
Calcular $\displaystyle\int_{0}^{2}(2x^2 - 3x + 2)\,dx$.
\end{example}

\begin{myproof}
Una antiderivada de $2x^2 - 3x + 2$ es $G(x) = \frac{2x^3}{3} - \frac{3x^2}{2} + 2x$. Por el TFC2:
\[
\int_{0}^{2}(2x^2-3x+2)\,dx = \left[\frac{2x^3}{3} - \frac{3x^2}{2} + 2x\right]_0^2
= \left(\frac{16}{3} - 6 + 4\right) - 0 = \frac{16}{3} - 2 = \frac{10}{3}. \qquad \square
\]
\end{myproof}"""

new5 = r"""\begin{example}[Integral definida por el TFC2]
Calcular $\displaystyle\int_{0}^{2}(2x^2 - 3x + 2)\,dx$.

\begin{myproof}

\textbf{Paso 1: Hallar una antiderivada.}

Una antiderivada de $2x^2 - 3x + 2$ es $G(x) = \frac{2x^3}{3} - \frac{3x^2}{2} + 2x$.

\textbf{Paso 2: Evaluar en los límites de integración (TFC2).}
\[
\int_{0}^{2}(2x^2-3x+2)\,dx = \left[\frac{2x^3}{3} - \frac{3x^2}{2} + 2x\right]_0^2
= \left(\frac{16}{3} - 6 + 4\right) - 0 = \frac{16}{3} - 2.
\]

\textbf{Paso 3: Simplificar.}
\[
\boxed{\int_{0}^{2}(2x^2 - 3x + 2)\,dx = \frac{10}{3}.}
\]
\end{myproof}
\end{example}"""

replacements.append((old5, new5))

# Ej.6 — substitution: int_0^1 (x+1)/(x^2+2x+6)^2 dx
old6 = r"""\begin{example}
Calcular $\displaystyle\int_{0}^{1}\frac{x+1}{(x^2+2x+6)^2}\,dx$ usando sustitución.
\end{example}

\begin{myproof}
Sea $u = x^2 + 2x + 6$, de modo que $du = (2x+2)\,dx = 2(x+1)\,dx$, es decir, $(x+1)\,dx = \frac{du}{2}$. Cambiamos los límites: para $x=0$, $u=6$; para $x=1$, $u = 1+2+6 = 9$. Entonces:
\[
\int_{0}^{1}\frac{x+1}{(x^2+2x+6)^2}\,dx
= \frac{1}{2}\int_{6}^{9} u^{-2}\,du
= \frac{1}{2}\left[-\frac{1}{u}\right]_6^9
= \frac{1}{2}\left(-\frac{1}{9}+\frac{1}{6}\right)
= \frac{1}{2}\cdot\frac{1}{18} = \frac{1}{36}. \qquad \square
\]
\end{myproof}"""

new6 = r"""\begin{example}[Integral definida por sustitución]
Calcular $\displaystyle\int_{0}^{1}\frac{x+1}{(x^2+2x+6)^2}\,dx$ usando sustitución.

\begin{myproof}

\textbf{Paso 1: Elegir la sustitución y calcular $du$.}

Sea $u = x^2 + 2x + 6$, de modo que $du = (2x+2)\,dx = 2(x+1)\,dx$, es decir, $(x+1)\,dx = \frac{du}{2}$.

\textbf{Paso 2: Cambiar los límites de integración.}

Para $x=0$: $u=6$; para $x=1$: $u = 1+2+6 = 9$.

\textbf{Paso 3: Evaluar la integral transformada.}
\[
\int_{0}^{1}\frac{x+1}{(x^2+2x+6)^2}\,dx
= \frac{1}{2}\int_{6}^{9} u^{-2}\,du
= \frac{1}{2}\left[-\frac{1}{u}\right]_6^9
= \frac{1}{2}\left(-\frac{1}{9}+\frac{1}{6}\right)
= \frac{1}{2}\cdot\frac{1}{18}.
\]
\[
\boxed{\int_{0}^{1}\frac{x+1}{(x^2+2x+6)^2}\,dx = \frac{1}{36}.}
\]
\end{myproof}
\end{example}"""

replacements.append((old6, new6))

# Ej.7 — Mean value: f(x)=x^2 on [1,4]
old7 = r"""\begin{example}
Encontrar el valor promedio de $f(x) = x^2$ en $[1,4]$ y el punto $c$ garantizado por el teorema.
\end{example}

\begin{myproof}
El valor promedio es
\[
\bar{f} = \frac{1}{4-1}\int_{1}^{4} x^2\,dx
= \frac{1}{3}\left[\frac{x^3}{3}\right]_1^4
= \frac{1}{3}\cdot\frac{64-1}{3} = \frac{63}{9} = 7.
\]
El punto $c$ satisface $f(c) = c^2 = 7$, de donde $c = \sqrt{7} \approx 2.646$. Como $\sqrt{7} \in (1,4)$, el teorema queda verificado. $\square$
\end{myproof}"""

new7 = r"""\begin{example}[Valor promedio y teorema del valor medio para integrales]
Encontrar el valor promedio de $f(x) = x^2$ en $[1,4]$ y el punto $c$ garantizado por el teorema.

\begin{myproof}

\textbf{Paso 1: Calcular el valor promedio.}
\[
\bar{f} = \frac{1}{4-1}\int_{1}^{4} x^2\,dx
= \frac{1}{3}\left[\frac{x^3}{3}\right]_1^4
= \frac{1}{3}\cdot\frac{64-1}{3} = \frac{63}{9} = 7.
\]

\textbf{Paso 2: Encontrar el punto $c$.}

El punto $c$ satisface $f(c) = c^2 = 7$, de donde $c = \sqrt{7} \approx 2.646$. Como $\sqrt{7} \in (1,4)$, el teorema queda verificado.
\[
\boxed{\bar{f} = 7, \qquad c = \sqrt{7} \approx 2.646.}
\]
\end{myproof}
\end{example}"""

replacements.append((old7, new7))

# --- Sección de problemas propuestos (se añade al final del archivo) ---
problems_section = r"""

\section{Problemas Propuestos}

\begin{prob}
Evaluar $\displaystyle\int_{0}^{3}(2x-1)\,dx$ como límite de sumas de Riemann usando puntos derechos con $n$ subintervalos iguales. Verifique el resultado usando el TFC2.
\end{prob}

\begin{prob}
Se sabe que $\displaystyle\int_{1}^{5} f(x)\,dx = 7$ y $\displaystyle\int_{1}^{3} f(x)\,dx = 4$. Calcular $\displaystyle\int_{3}^{5} f(x)\,dx$.
\end{prob}

\begin{prob}
Acotar $\displaystyle\int_{0}^{1} e^x\,dx$ usando la propiedad de acotamiento. Verifique que el valor exacto $e-1 \approx 1.718$ cae en el intervalo obtenido.
\end{prob}

\begin{prob}
Calcular $\displaystyle\int_{-3}^{3}(x^5 - 4x^3 + 2x)\,dx$ sin integrar directamente. Justifique usando propiedades de simetría.
\end{prob}

\begin{prob}
Calcular las siguientes integrales usando el TFC2:
\begin{enumerate}[(a)]
    \item $\displaystyle\int_{0}^{\pi} \sin x\,dx$
    \item $\displaystyle\int_{1}^{4}\!\left(\sqrt{x} - \dfrac{1}{x}\right)dx$
    \item $\displaystyle\int_{-1}^{2}(3x^2 - 2x + 1)\,dx$
    \item $\displaystyle\int_{0}^{\pi/4} \sec^2 x\,dx$
\end{enumerate}
\end{prob}

\begin{prob}
Sea $G(x) = \displaystyle\int_{0}^{x^3} \sin(t^2)\,dt$. Calcular $G'(x)$.
\end{prob}

\begin{prob}
Sea $F(x) = \displaystyle\int_{x}^{x^2} \cos t\,dt$. Calcular $F'(x)$ usando el TFC1 y la propiedad de aditividad de la integral.
\end{prob}

\begin{prob}
Calcular $\displaystyle\int_{0}^{4} \frac{x}{x^2+1}\,dx$ usando sustitución.
\end{prob}

\begin{prob}
Calcular $\displaystyle\int_{0}^{2} |x-1|\,dx$. \textit{Sugerencia}: escriba $|x-1|$ como función a trozos y use aditividad.
\end{prob}

\begin{prob}
Encontrar el valor promedio de $f(x) = \sin x$ en $[0,\pi]$ y el punto $c \in (0,\pi)$ garantizado por el Teorema del Valor Medio para Integrales.
\end{prob}

\begin{prob}
Si $f$ es continua, $\displaystyle\int_{0}^{3} f(x)\,dx = 10$ y $\displaystyle\int_{3}^{5} f(x)\,dx = -2$, calcular $\displaystyle\int_{0}^{5} f(x)\,dx$ y $\displaystyle\int_{5}^{0} f(x)\,dx$.
\end{prob}

\begin{prob}
Calcular $\displaystyle\int_{0}^{1} x\,e^{x^2}\,dx$.
\end{prob}

\begin{prob}
Una partícula se mueve con velocidad $v(t) = t^2 - 4t + 3$ m/s. Calcular:
\begin{enumerate}[(a)]
    \item El desplazamiento neto en el intervalo $[0,4]$.
    \item La distancia total recorrida en $[0,4]$.
\end{enumerate}
\end{prob}

\begin{prob}
Encontrar el valor de $c$ garantizado por el Teorema del Valor Medio para Integrales para $f(x) = x^3$ en $[0,2]$. Verificar que $c \in (0,2)$.
\end{prob}

\begin{prob}
Usando el TFC1, hallar $\dfrac{d}{dx}\displaystyle\int_{\cos x}^{0} \sqrt{1+t^4}\,dt$.
\end{prob}"""

# --- Execute ---
n_err = 0
for i, (old, new) in enumerate(replacements, 1):
    count = text.count(old)
    if count != 1:
        print(f"ERROR ej.{i}: {count} coincidencias.")
        n_err += 1
    else:
        text = text.replace(old, new)
        print(f"OK ej.{i}")

if n_err == 0:
    text = text + problems_section
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Archivo guardado con 7 ejemplos reformateados y sección de problemas añadida.")
else:
    print(f"No se guardó: {n_err} error(es).")
