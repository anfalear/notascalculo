# GUÍA DE REESCRITURA — Capítulos de Cálculo III

**Propósito:** referencia operativa para reescribir cualquier capítulo de C3 desde cero. Sintetiza el Criterio Apostol (R1–R3), las convenciones técnicas del proyecto y el inventario completo de contenido, figuras y problemas de cada capítulo tal como quedaron después de la Fase 8.

**Compilador:** LuaLaTeX — nunca pdflatex.  
**Archivo maestro:** `anfalearNotasCalculo.tex`  
**Fuentes de referencia:** `PLAN_FASE8_APOSTOL_C3.md`, `PROGRESO.md`, `PROGRESO_VERIFICACION.md`, `figuras_guia.tex` (solo referencia, nunca `\input`tar en el maestro).

---

## 1. Criterio Apostol operativo

### R1 — Orden canónico dentro de cada capítulo

```
definición → figura geométrica → teorema (enunciado riguroso)
→ prueba o esquema → ejemplos resueltos (4 pasos + \boxed{})
→ \section{Problemas propuestos}
```

No hay excepciones al orden. Si existe un rem de interpretación geométrica, va inmediatamente después de la definición y antes del teorema.

### R2 — Figura obligatoria

Todo concepto con interpretación geométrica lleva figura TikZ o pgfplots inmediatamente después de la definición o el teorema. No se remite a figuras posteriores ni se describe solo con texto.

### R3 — Nivel de demostración

| Tipo de teorema | Tratamiento |
|---|---|
| Centrales (Green, Stokes, Divergencia, TFC línea, plano tangente, regla de la cadena) | Demostración completa o esquema con pasos clave explícitos |
| Operacionales (Fubini, criterio 2ª deriv., propiedades de integrales) | Enunciado riguroso + esquema geométrico/intuitivo |
| Propiedades de cálculo (linealidad, monotonía, etc.) | Enunciado + referencia |

---

## 2. Convenciones técnicas universales

### 2.1 Entornos LaTeX del proyecto

| Entorno | Uso |
|---|---|
| `\begin{definition}[Nombre]` | Definición formal |
| `\begin{theorem}[Nombre]` | Teorema, lema, corolario |
| `\begin{rem}[Nombre]` | Observación, nota, interpretación |
| `\begin{example}[Nombre]` | Problema resuelto (siempre con myproof) |
| `\begin{myproof}` | Solución dentro de example o prob (4 pasos) |
| `\begin{prob}` | Problema propuesto (nunca tiene myproof dentro) |
| `\begin{pasos}[Nombre]` | Protocolo o algoritmo de pasos (no es un resuelto) |
| `\begin{figure}[H]` | Toda figura: siempre `[H]`, nunca flotante sin especificar |

### 2.2 Protocolo de ejemplos resueltos

```latex
\begin{example}[Título descriptivo]
  Enunciado del ejemplo.
  \begin{myproof}
    \textbf{Paso 1. Análisis / Estrategia.} ...
    \textbf{Paso 2. Cálculo principal.} ...
    \textbf{Paso 3. Verificación / Caso especial.} ...
    \textbf{Paso 4. Resultado.}
    \[
      \boxed{\text{resultado final}}
    \]
  \end{myproof}
\end{example}
```

**Reglas:**
- Siempre 4 pasos con `\textbf{Paso N.}` (punto, no dos puntos).
- `\boxed{}` obligatorio en el Paso 4.
- Para resueltos con múltiples sub-partes: Paso 1 = Estrategia, Paso 2/3/4 = sub-partes a/b/c.
- `\begin{myproof}` siempre DENTRO de `\begin{example}` o `\begin{prob}` — nunca fuera de ninguno de los dos.
- Los problemas propuestos (`\begin{prob}`) nunca llevan `\begin{myproof}`.

### 2.3 Figuras TikZ — estándar obligatorio

```latex
\begin{figure}[H]
\centering
\begin{tikzpicture}[scale=1.2]
  % ... código TikZ ...
  \node[anchor=west,font=\small] at (x,y) {etiqueta};   % anchor explícito siempre
\end{tikzpicture}
\caption{Descripción completa de lo que muestra la figura.}
\label{fig:nombre-kebab-case}
\end{figure}
```

**Reglas TikZ 2D:**
- `scale` entre 1.1 y 1.5 según el tamaño del contenido.
- Colores: `blue!70!black` (curvas/regiones principales), `red!70!black` (vectores/énfasis), `gray!50` (guías/fondos).
- Etiquetas: `\small` o `\scriptsize`; `anchor` explícito en **todos** los `\node` (nunca omitir anchor).
- Menos de 80 líneas de código TikZ por figura.
- Flechas: `stealth` o default; `->` para vectores.
- Para campos vectoriales: `\foreach \xi/\yi in {...}` con `\pgfmathsetmacro` para los desplazamientos.

**Reglas pgfplots 3D:**
- `shader=flat corner` (más rápido que `interp` o `faceted`).
- `samples=20` como máximo (o menos para superficies complejas); `samples=14–18` para paramétricas.
- `opacity=0.70–0.80` para ver detalles interiores.
- `colormap/cool` o `colormap/hot` — elegir el que mejor contraste dé con los vectores añadidos.
- Vectores sobre superficie 3D: `\addplot3[quiver, ...]{...}` o `\draw[->,red!70!black] (a,b,c)--(d,e,f)` según complejidad.

### 2.4 Organización de problemas propuestos

```latex
\section{Problemas propuestos}

% Básico
\begin{prob}
  ...
\end{prob}

% Básico
\begin{prob}
  ...
\end{prob}

% Intermedio
\begin{prob}
  ...
\end{prob}

% Desafiante
\begin{prob}
  ...
\end{prob}
```

- Comentario de grupo (`% Básico`, `% Intermedio`, `% Desafiante`) antes del **primer** problema de cada grupo, no antes de cada uno.
- Mínimo 15 propuestos por capítulo; máximo 40.
- Distribución orientativa: ~25 % Básico, ~50 % Intermedio, ~25 % Desafiante.
- Todos los subtemas del capítulo deben estar cubiertos al menos con un propuesto.

### 2.5 Convención de \label

| Tipo | Convención | Ejemplo |
|---|---|---|
| Figura | `fig:nombre-kebab` | `fig:helice_tangente` |
| Sección | `sec:nombre-kebab` | `sec:cambio-var-dobles` |
| Teorema / Def | `thm:capNN:slug` | `thm:cap20:plano-tangente` |

---

## 3. Capítulo 18 — `funvectoriales.tex`

**Título:** Funciones de varias variables y vectoriales  
**Archivo:** `funvectoriales.tex`

### 3.1 Estructura de secciones (R1)

```
\chapter{Funciones de varias variables y vectoriales}
  Párrafo introductorio (ya presente)

\section{Funciones vectoriales}
  def función vectorial → figura → ejemplo límite → ejemplo derivada → ejemplo integral → ejemplo longitud de arco

\section{Funciones de varias variables}
  def función f:R²→R → def dominio → ejemplos de dominio con figura TikZ
  \subsection{Gráfica} → def → ejemplo paraboloide/cono
  \subsection{Superficies cuádricas}  ← nueva, añadida en F8.26
    5 superficies: paraboloide elíptico, hiperbólico, cono, hiperboloide 1 hoja, hiperboloide 2 hojas
    Cada una: def ecuación + figura pgfplots 3D + ejemplo 4 pasos
  \subsection{Curvas y superficies de nivel}
    def curvas de nivel → figura → ejemplos con figura → superficies de nivel (3 ejemplos nuevos)

\section{Problemas propuestos}
```

### 3.2 Figuras presentes (post-F8)

| Label | Descripción | Dónde |
|---|---|---|
| `fig:helice_tangente` | Hélice r(t)=(cos t, sin t, t/2) + vector tangente en t=π/2 (pgfplots 3D) | Después de def función vectorial |
| `fig:paraboloide_curvas_nivel` | Minipage: curvas de nivel 2D (4 círculos) + paraboloide 3D (pgfplots, shader=flat) | Después de `\begin{pasos}[Trazado de curvas de nivel]` |
| `fig:dominio_log_raiz` | Triángulo D del dominio de f=√(x+y)/ln(x−y) con 3 rectas (sólida/rayada/punteada) | Dentro del example de dominio |
| `fig:nivel_esfera` | Esferas concéntricas k=1,4,9 (paramétrico pgfplots) | Example superficies de nivel |
| `fig:nivel_elipsoide` | Elipsoide k=1 semiejes 1,2,3 (pgfplots paramétrico) | Example superficies de nivel |
| `fig:nivel_paraboloides` | Dos paraboloides k=0,−1 superpuestos | Example superficies de nivel |
| *(5 figs cuádricas)* | Una por cada superficie: paraboloide elíptico/hiperbólico, cono, hiperboloide 1/2 hojas | Subsección cuádricas (F8.26) |
| *(9 figs preexistentes)* | Dominios en probs, curvas de nivel de ln: corregidas a figure[H] + caption + label (F8.31) | En los prob correspondientes |

### 3.3 Problemas

- **Resueltos:** 9 (myproof dentro de example; todos con 4 pasos + `\boxed{}` verificados en F8.28)
- **Propuestos:** 15 (tags % Básico / % Intermedio / % Desafiante, F8.49)
- **Temas propuestos:** límite vectorial, dominio de f:R²→R, curvas de nivel, longitud de arco, continuidad, derivada parcial básica, superficies de nivel, función vectorial en R³

### 3.4 Notas R1/R2/R3

- R1 verificado (F8.20): sin inversiones de orden.  
- Pendiente registrado (INV18.2): subsección "Reglas de derivación" no tiene ejemplo resuelto ilustrativo — no es inversión de posición, sino ausencia de ejemplo.
- R3: no hay teoremas centrales que requieran demostración completa en este capítulo.

---

## 4. Capítulo 19 — `limvariasvariables.tex`

**Título:** Límites y continuidad en Rⁿ  
**Archivo:** `limvariasvariables.tex`

### 4.1 Estructura de secciones (R1)

```
\chapter{Límites y continuidad en varias variables}
  Párrafo introductorio (presente)

\section{Límites de funciones de varias variables}
  def límite (ε-δ) → figura disco → rem interpretación → ejemplo límite directo
  → example trayectorias distintas (figura de trayectorias integrada)
  → técnicas: sustitución directa, sándwich, polares, factorización

\section{Continuidad}
  def continuidad → theorem composición → ejemplos discontinuidad

\section{Límites en R³}
  (brevemente, sin nueva def formal — mismo criterio ε-δ extendido)

\section{Problemas propuestos}
```

### 4.2 Figuras presentes (post-F8)

| Label | Descripción | Dónde |
|---|---|---|
| `fig:disco_epsilon_delta` | Disco B((x₀,y₀),δ) con punto interior + nota ε lateral (TikZ 2D) | Después de def límite 2 variables |
| `fig:trayectorias_limite` | Recta y=x (rojo) y parábola y=x² (azul) hacia (0,0) con flechas y etiquetas lim | Dentro del example "trayectorias distintas", antes de myproof |

### 4.3 Problemas

- **Resueltos:** 13 (elevados en F8.P2 + originales; todos 4 pasos F8.29)
- **Propuestos:** 10 (tags F8.49)
- **Temas propuestos:** límite por trayectorias, límite en polares, límite en 3 variables, continuidad por casos, discontinuidades esenciales

### 4.4 Notas R1/R2/R3

- R1: INV19.1 registrado pero no corregido — `theorem[Composición de funciones continuas]` y su prueba vienen después de 3 probs resueltos de discontinuidad. Orden pedagógicamente justificado (los probs motivan el teorema). No invertir.
- R3: el theorem de continuidad es operacional → enunciado riguroso + referencia.

---

## 5. Capítulo 20 — `planostangentes.tex`

**Título:** Diferenciación parcial, plano tangente y diferenciabilidad  
**Archivo:** `planostangentes.tex`

### 5.1 Estructura de secciones (R1)

```
\chapter{Diferenciación parcial, plano tangente y diferenciabilidad}
  Párrafo introductorio (añadido F8.24 — conecta con Cap 19)

\section{Derivadas parciales}
  def DP vía límite → rem notación (Leibniz/∂f/∂x) → párrafo interpretación geométrica
  → figura 3D: trazas + rectas tangentes fx/fy → ejemplos (por definición, reglas, orden superior)
  → teorema Clairaut

\section{Plano tangente y aproximación lineal}
  theorem plano tangente → pasos protocolo → figura 3D plano+normal
  → def diferencial total → figura 2D Δz vs dz
  → ejemplos (4 casos: superficie explícita, implícita, paramétrica, error)

\section{Diferenciabilidad}
  def diferenciabilidad → theorem condición suficiente (DP continuas) → ejemplos

\section{Problemas propuestos}
```

### 5.2 Figuras presentes (post-F8)

| Label | Descripción | Dónde |
|---|---|---|
| `fig:dp_interpretacion_geometrica` | pgfplots 3D: paraboloide z=x²+y² + trazas y=1 (rojo) / x=1 (azul) + rectas tangentes fx/fy + punto (1,1,2) | Después de rem notación, antes de ejemplos (corregido F8.40) |
| `fig:plano_tangente_3d` | pgfplots 3D: paraboloide + plano tangente naranja + vector normal | Antes del pasos-protocolo de plano tangente (F8.06) |
| `fig:aprox_lineal_dz` | TikZ 2D: sección de superficie con Δz vs dz marcados con segmentos | Después de def diferencial total (F8.07) |

**Nota:** la figura `fig:dp_interpretacion_geometrica` existía antes de F8 (preexistente); fue corregida en F8.33 (label + anchor) y reemplazada por pgfplots 3D en F8.40. El label se mantiene el mismo.

### 5.3 Problemas

- **Resueltos:** 9 (incluyendo 6 elevados en F8.P3; todos 4 pasos F8.41 — 16 correcciones)
- **Propuestos:** 16 (añadidos 5 nuevos en F8.P3: derivación implícita F(x,y,z)=0, error de área, plano tangente implícita, diferencial w=x²e^(y/z), e^z−z=xy+1)
- **Tags:** sin confirmar si tags se añadieron en F8.49 — verificar en archivo.

### 5.4 Notas R1/R2/R3

- R1: INV20.1 **corregido** (F8.20) — párrafo de interpretación geométrica + figura movidos antes de los ejemplos.
- R3: theorem plano tangente = central → demostración completa o esquema con pasos clave.

---

## 6. Capítulo 21 — `gradientes.tex`

**Título:** Regla de la cadena y derivadas direccionales  
**Archivo:** `gradientes.tex`

### 6.1 Estructura de secciones (R1)

```
\chapter{Regla de la cadena y derivadas direccionales}
  Párrafo introductorio (presente)

\section{Regla de la cadena}
  theorem (Caso 1: z=f(x(t),y(t))) → rem → ejemplos (razones de cambio, triángulo)
  theorem (Caso 2: z=f(x(s,t),y(s,t))) → ejemplos
  → derivación implícita F(x,y)=0 y F(x,y,z)=0

\section{El gradiente y la derivada direccional}
  def derivada direccional → theorem fórmula (∇f·u) → figura "pendiente de sección"
  def gradiente → figura curvas de nivel + vectores ∇f → rem interpretación geométrica
  → theorem propiedades (dirección de max/min, ⊥ a curva de nivel)

\section{Aplicaciones del gradiente}
  plano tangente a superficie implícita F(x,y,z)=0 → recta normal
  → ejemplos (3 superficies distintas)

\section{Problemas propuestos}
```

### 6.2 Figuras presentes (post-F8)

| Label | Descripción | Dónde |
|---|---|---|
| `fig:gradiente_curvas_nivel` | TikZ 2D: 5 elipses f=x²+y²/4 (c=1,2,3,4,5) + 4 vectores ∇f perpendiculares | Antes de subsección interpretación geométrica (F8.08) |
| `fig:derivada_direccional` | pgfplots 3D: z=x²+y² + plano vertical en dirección u + pendiente D_u f indicada | Antes del theorem fórmula gradiente (F8.09) |
| `fig:triangulo_cadena` | TikZ 2D: triángulo con lados x, y y ángulo θ (preexistente, corregido F8.34) | Dentro de prob de razón de cambio |

### 6.3 Problemas

- **Resueltos:** 9 (5 elevados en F8.P4; 12 correcciones 4 pasos en F8.42)
- **Propuestos:** 15 (tags F8.49)
- **Temas propuestos:** razón de cambio relacionada, regla cadena Caso 1/2, derivación implícita, gradiente en punto, derivada direccional, dirección de máx. crecimiento, plano tangente / recta normal superficie

### 6.4 Notas R1/R2/R3

- R1: INV21.1 registrado pero no corregido — `fig:gradiente_curvas_nivel` viene después del `theorem[Propiedades del gradiente]`. Coherencia interna mantenida (la figura ilustra la lista de interpretación geométrica que la precede). No invertir.
- R3: theorem de la derivada direccional = operacional → enunciado + esquema geométrico.

---

## 7. Capítulo 22 — `multiplicadoresintdobles.tex`

**Título:** Optimización: extremos libres y multiplicadores de Lagrange  
**Archivo:** `multiplicadoresintdobles.tex`

### 7.1 Estructura de secciones (R1)

```
\chapter{Optimización: extremos libres y multiplicadores de Lagrange}
  Párrafo introductorio (verificar presencia)

\section{Extremos de funciones de dos variables}
  def punto crítico → figura punto de silla → theorem criterio 2ª derivada (D-test)
  → rem D=0 (criterio no concluye) → ejemplos (máx, mín, silla, frontera)

\section{Valores extremos en regiones cerradas acotadas}
  theorem extremo absoluto (compacto) → pasos-protocolo → ejemplos

\section{Multiplicadores de Lagrange}
  def problema de optimización con restricción → theorem Lagrange
  → rem condición necesaria (no suficiente) → figura región factible
  → pasos-protocolo → ejemplos (1 restricción, 2 restricciones, geométrico)

\section{Problemas propuestos}
```

### 7.2 Figuras presentes (post-F8)

| Label | Descripción | Dónde |
|---|---|---|
| `fig:punto_silla` | pgfplots 3D: z=x²−y² con curvas de curvatura opuesta (F8.10) | Después de rem punto crítico |
| `fig:lagrange_region_factible` | TikZ 2D: elipses f=c + recta g=0 + punto tangencia + ∇f∥∇g (F8.11) | Antes del pasos-protocolo de Lagrange |
| `fig:trapecio_canal` | TikZ 2D: sección transversal del canal trapecio (preexistente, corregido F8.35) | Dentro de myproof ejemplo canal |
| `fig:cuspide_lagrange_falla` | TikZ 2D: cúspide y³=x² mostrando falla del teorema (preexistente, corregido F8.35) | Dentro de example "candidato falso" |

### 7.3 Problemas

- **Resueltos:** 9 (1 nuevo en F8.P5: minimizar f=x²+y² s.t. x+y=1 con Hessiano orlado; 10 correcciones 4 pasos en F8.43)
- **Propuestos:** 20 (2 probs de ley de Ohm movidos al Cap 21 en F8.P5; tags F8.49)
- **Temas propuestos:** extremos libres (D>0 máx/mín, silla, D=0), extremo en región compacta, Lagrange 1 restricción, Lagrange 2 restricciones, aplicación geométrica, Hardy-Weinberg

### 7.4 Notas R1/R2/R3

- R1: sin inversiones (F8.20).
- R3: theorem criterio 2ª derivada = operacional; theorem Lagrange = operacional con esquema geométrico.
- **Verificado matemáticamente:** V1.3 (27/27 probs) + V1.3b + muestreo Ej/Teo (1 error corregido: det Hessiano orlado 6d²+d√2 → 8d², `l.514`).

---

## 8. Capítulo 32 — `apintdobles.tex`

**Título:** Aplicaciones de la integral doble e integrales en coordenadas polares  
**Archivo:** `apintdobles.tex`

### 8.1 Estructura de secciones (R1)

```
\chapter{Aplicaciones de la integral doble e integrales dobles en coordenadas polares}
  Párrafo introductorio (presente)

\section{Integral doble sobre rectángulo}
  def integral doble (suma de Riemann) → theorem Fubini (rectángulo) → ejemplos

\section{Integral doble sobre región general}
  [figura región tipo I y tipo II]
  def región tipo I / tipo II → theorem Fubini (tipo I, tipo II)
  → pasos-protocolo integración → ejemplos

\section{Cambio de orden de integración}
  [figura cambio de orden]
  → ejemplos (estrategia: cuándo invertir)

\section{Cambio de variables y Jacobiano}
  def transformación T(u,v) → def Jacobiano 2×2 (determinante)
  [figura geométrica Jacobiano: cuadrado → paralelogramo]
  theorem cambio de variables (enunciado) → rem J=0
  → ejemplo: polares como caso del Jacobiano (e^(r²), disco r≤2, resultado π(e⁴−1))

\section{Coordenadas polares}
  [figura coordenadas polares: rectángulo polar dA=r dr dθ]
  def coord. polares → theorem integral en polares
  → ejemplos

\section{Aplicaciones: área, volumen, masa, momentos}
  def área por integral doble → def volumen → def masa/cm/momentos → ejemplos

\section{Problemas propuestos}
```

### 8.2 Figuras presentes (post-F8)

| Label | Descripción | Dónde |
|---|---|---|
| `fig:region_tipo_I_II` | Minipages TikZ 2D: (a) tipo I g₁/g₂ franjas verticales, (b) tipo II h₁/h₂ franjas horizontales (F8.15) | Antes del pasos-protocolo integración sobre región |
| `fig:cambio_orden_integracion` | Minipages TikZ 2D: región y=x²/y=x con franja vertical (a) y horizontal (b) (F8.16) | Después del `\end{rem}` correspondiente |
| `fig:jacobiano_2x2` | Minipage doble: cuadrado [0,1]² ← T → paralelogramo, "área=\|J\|" (F8.14) | Dentro de la sección Jacobiano, entre def y theorem |
| `fig:coordenadas_polares` | TikZ 2D: rectángulo polar r·Δr·Δθ con punto P(r,θ), proyecciones x=rcosθ/y=rsinθ, dA (F8.48) | Después del párrafo de dA, antes de "Una región D se dice r-simple" |
| `fig:lamina_rect_masa` | Lámina rectangular x∈[0,4] (preexistente, corregido F8.36) | En ejemplo masa |
| `fig:lamina_exp_masa` | Lámina y=e^x (preexistente, corregido F8.36) | En ejemplo masa |
| `fig:lamina_rect_inercia` | Lámina rectangular b×h, momento inercia (preexistente, corregido F8.36) | En ejemplo inercia |
| `fig:lamina_polar_masa` | Lámina polar r=2sinθ (preexistente, corregido F8.36) | En ejemplo polares |
| `fig:region_cuadricas_1/2` | Regiones cuádricas en probs (preexistente, renombrados de fig1.1/fig1.2, F8.36) | En probs correspondientes |
| `fig:region_polar_1/2` | Regiones polares en probs (preexistente, renombrados de fig3.2, F8.36) | En probs correspondientes |

### 8.3 Problemas

- **Resueltos:** 11 (todos originales; todos 4 pasos F8.44 — 21 de 27 myproof corregidos)
- **Propuestos:** 18 (añadidos en F8.P6: 5 directos + 8 intermedios + 5 desafiantes; tags F8.49)
- **Temas propuestos:** Fubini rectangular, tipo I/II, cambio de orden, polares, área de región, volumen bajo superficie, masa, CM, momento de inercia, área superficial, Jacobiano en polares, integral anular

### 8.4 Notas R1/R2/R3

- R3: theorem Fubini = operacional (enunciado + esquema geométrico de rebanadas).
- **Verificado matemáticamente:** V3.4 (11/11 probs verificados; 0 errores); respuestas numéricas documentadas en `PROGRESO_VERIFICACION.md` fila V3.4.

---

## 9. Capítulo 33 — `inttriples.tex`

**Título:** Integrales triples  
**Archivo:** `inttriples.tex`

### 9.1 Estructura de secciones (R1)

```
\chapter{Integrales triples}
  Párrafo introductorio (presente)

\section{Integral triple en coordenadas rectangulares}
  def integral triple (iterada) → theorem Fubini triple → ejemplos

\section{Cambio de variables en integrales dobles}   ← nueva sección (F8.12)
  def transformación + Jacobiano 2×2 → [figura geométrica: cuadrado→paralelogramo]
  theorem cambio de variables 2D → rem J=0
  → ejemplo: polares (e^(x²+y²), disco → π(e⁴−1))

\section{Cambio de variables en integrales triples}   ← nueva sección (F8.13)
  def Jacobiano 3×3 (determinante) → theorem cambio de variables triple
  → párrafo de conexión con cilíndricas/esféricas

\section{Coordenadas cilíndricas}
  def (r,θ,z) con cálculo explícito del Jacobiano → theorem integral cilíndrica
  [figura cilíndricas: vista superior r,θ + vista lateral r,z; dV]
  → ejemplos

\section{Coordenadas esféricas}
  def (ρ,φ,θ) → nota sobre Jacobiano referenciando sección anterior
  [figura esféricas: plano xz con ρ,φ,θ; dV=ρ²sinφ dρ dφ dθ]
  theorem integral esférica → ejemplos

\section{Aplicaciones: masa, momentos, centro de masa}
  → ejemplos

\section{Problemas propuestos}
```

**Nota sobre Jacobiano:** las secciones "Cambio de variables en integrales dobles" y "Cambio de variables en integrales triples" fueron insertadas en este archivo (F8.12/F8.13). Sin embargo, la figura `fig:jacobiano_2x2` quedó insertada en `apintdobles.tex` (ver F8.37). Si se reescribe este capítulo, la figura del Jacobiano 2×2 debe ir aquí, en la sección correspondiente.

### 9.2 Figuras presentes (post-F8)

| Label | Descripción | Dónde |
|---|---|---|
| `fig:coordenadas_cilindricas` | Minipage doble TikZ 2D: vista superior (r,θ en plano xy) + vista lateral (r,z); dV=r dr dθ dz (F8.48) | Entre `\end{definition}` cilíndricas y `\begin{theorem}` cilíndricas |
| `fig:coordenadas_esfericas` | TikZ 2D en plano xz: ρ,φ,θ, punto P, proyecciones; dV=ρ²sinφ dρ dφ dθ (F8.48) | Entre `\end{definition}` esféricas y `\begin{theorem}` esféricas |

### 9.3 Problemas

- **Resueltos:** 9 (4 elevados en F8.P7: volumen z=2−x−y, masa rect. ρ=xyz, cilíndricas, esféricas; todos 4 pasos F8.45 — 5 corregidos)
- **Propuestos:** ~53 (sobre el máximo de 40 — pendiente decisión editorial futura; 16 eliminados en F8.P7 por redundancia/duplicados; tags F8.49)
- **Temas propuestos:** integral triple rectangular, cilíndricas, esféricas, Jacobiano 2D/3D, masa/momentos en R³

### 9.4 Notas R1/R2/R3

- R3: theorem Fubini triple = operacional.
- **Pendiente editorial:** ~53 propuestos superan el máximo recomendado de 40. Requiere decisión del autor sobre cuáles consolidar o marcar como opcionales.
- **Verificado matemáticamente:** V2.3 (2 ejemplos esféricas; 0 errores).

---

## 10. Capítulo 33 — `cap33.tex`

**Título:** Campos vectoriales e integrales de línea  
**Archivo:** `cap33.tex`  
*(Este archivo fue creado en Decisión C como primera mitad de `cap34_integrales_vectoriales.tex`.)*

### 10.1 Estructura de secciones (R1)

```
\chapter{Campos vectoriales e integrales de línea}
  Párrafo introductorio

\section{Campos vectoriales}
  def campo vectorial F:R²→R² y F:R³→R³
  def divergencia y rotacional → rem interpretación física
  [figura campo vectorial rotacional F=(-y,x) con quiver]

  def campo vectorial gradiente → [figura campo gradiente ∇f + curvas de nivel]
  rem interpretación geométrica del gradiente

  def campo vectorial conservativo → [figura campo conservativo con trayectoria cerrada]
  theorem caracterización campos conservativos en el plano
  theorem criterio (∂P/∂y = ∂Q/∂x ↔ conservativo en dominio s.c.)

\section{Integrales de línea}
  def integral de línea escalar ∫_C f ds → theorem parametrización
  def integral de línea vectorial ∫_C F·dr → theorem formula
  → rem orientación → ejemplos (escalar y vectorial)

\section{Campos conservativos y teorema fundamental}
  theorem TFC para integrales de línea
  def función potencial → def conjunto simplemente conexo
  theorem en dominio s.c.: rot F=0 ↔ conservativo ↔ existe potencial
  → algoritmo para hallar función potencial → ejemplos

\section{Teorema de Green}
  theorem Green (enunciado) → proof completa (tipo I + tipo II → suma)
  [figura región tipo I con borde orientado, franjas verticales, C₁/C₂]
  → rem Green como caso particular de Stokes
  → aplicaciones (área, integral de línea vía Green) → ejemplos

\section{Problemas propuestos}
```

### 10.2 Figuras presentes (post-F8)

| Label | Descripción | Dónde |
|---|---|---|
| — | *(El archivo cap33.tex no tenía figuras antes de F8; F8.38 confirmó 0 correcciones)* | — |
| `fig:campo_vectorial_rotacional` | TikZ `\foreach` grilla 5×5: F=(−y,x) × escala | (**En cap34.tex**, F8.17) — si se mueve a cap33 en reescritura, va antes de def Divergencia |
| `fig:campo_gradiente` | TikZ 2D: `\foreach` 4×4 flechas ∇f=(2x,y/2) rojas + 3 elipses azules f=1/4,1/2,1 (F8.50) | Entre def campo gradiente y rem interpretación geométrica |
| `fig:campo_conservativo` | TikZ 2D: `\foreach` flechas radiales F=(x,y) + círculo azul orientado + etiqueta ∮F·dr=0 (F8.51) | Entre def campo conservativo y theorem caracterización |
| `fig:curva_orientacion_positiva` | TikZ 2D: curva cerrada C con región R sombreada y orientación + (F8.18 — **en cap34.tex**) | Antes del Teorema de Green |
| `fig:green_region_tipo_I` | TikZ 2D: elipse R + franja vertical clipeada + orientación CCW + C₁/C₂/g₁/g₂ (F8.21 — **en cap34.tex**) | Después de `\end{proof}` de Green |

**Nota importante:** las figuras `fig:campo_vectorial_rotacional`, `fig:curva_orientacion_positiva` y `fig:green_region_tipo_I` están en `cap34.tex` según lo ejecutado en F8.17/F8.18/F8.21. Al reescribir, si el contenido de campos vectoriales y Green se consolida en cap33.tex, estas figuras deben trasladarse.

### 10.3 Problemas

- **Resueltos:** 6 (incluidos ejemplos de campo conservativo e integral de línea; 2 corregidos a 4 pasos en F8.46)
- **Propuestos:** 15 (7 originales + 8 nuevos en F8.52; grupos: 4 Básico + 7 Intermedio + 4 Desafiante)
- **Temas propuestos:** integral de línea escalar, integral de línea vectorial (3 casos), TFC (f=x²e^y), campo conservativo en R³ + potencial + TFC, campo F=(2xy+e^y, x²+xe^y), Green directa (2 casos), Green para áreas (elipse + astroide), campo de vórtice dominio no simplemente conexo (4 partes), Green estratégico

### 10.4 Notas R1/R2/R3

- R3: theorem de Green = central → demostración completa está presente (tipo I + tipo II).
- El theorem TFC para integrales de línea = central → demostración o esquema con pasos clave.

---

## 11. Capítulo 34 — `cap34.tex`

**Título:** Integrales de superficie y teoremas integrales  
**Archivo:** `cap34.tex`  
*(Este archivo fue creado en Decisión C como segunda mitad de `cap34_integrales_vectoriales.tex`. Contiene Green, Stokes y Gauss.)*

### 11.1 Estructura de secciones (R1)

```
\chapter{Integrales de superficie y teoremas integrales}
  Párrafo introductorio

\section{Integrales de superficie escalares}
  def integral superficial escalar ∫∫_S f dS → theorem parametrización (||r_u × r_v||)
  → ejemplos (cilindro, esfera, paraboloide)

\section{Integrales de superficie vectoriales (flujo)}
  def superficie orientada → def vector normal coherente
  [figura superficie orientada con vectores n en varios puntos]
  def flujo ∫∫_S F·n dS → theorem fórmula via parametrización
  → ejemplos

\section{Divergencia y rotacional en R³}
  def divergencia (escalar) → def rotacional (vector) → rem interpretación física
  [figura campo vectorial con quiver — puede usar fig:campo_vectorial_rotacional]

\section{Teorema de Green}  ← (si no está en cap33.tex)
  (ver cap33.tex, sección 4)

\section{Teorema de Stokes}
  theorem Stokes (enunciado) → proof esquema clave
  [figura superficie S + borde ∂S orientado (regla mano derecha) + vectores n + micro-circulaciones]
  rem: Green como caso particular (S plana)
  → ejemplos

\section{Teorema de la Divergencia (Gauss)}
  theorem Divergencia (enunciado) → proof esquema
  [figura grilla de celdas + cancelación interna (rojo) + flujo ∂E exterior (azul)]
  → rem: flujo neto = fuentes − sumideros
  → ejemplos

\section{Problemas propuestos}
```

### 11.2 Figuras presentes (post-F8)

| Label | Descripción | Dónde |
|---|---|---|
| `fig:campo_vectorial_rotacional` | TikZ `\foreach` 5×5: F=(−y,x) (F8.17) | Antes de def Divergencia |
| `fig:curva_orientacion_positiva` | TikZ 2D: curva C orientada + región R sombreada (F8.18) | Antes del Teorema de Green |
| `fig:superficie_orientada` | pgfplots 3D: paraboloide z=4−x²−y² + 4 vectores n en rojo (F8.19) | Antes de def Flujo |
| `fig:green_region_tipo_I` | TikZ 2D: elipse R + franja clipeada + CCW + C₁/C₂/g₁/g₂ (F8.21) | Después de `\end{proof}` Green |
| `fig:stokes_superficie` | TikZ 2D: superficie S + ∂S orientado + n (azul) + micro-circulaciones arc CCW (gris) (F8.22) | Antes de `\begin{proof}` de Stokes |
| `fig:divergencia_cancelacion` | TikZ 2D: grilla 2×2 celdas + flechas cancelación interior (rojo) + flujo exterior (azul) (F8.23) | Después de `\end{proof}` Divergencia |

**Todos los nodos fueron corregidos con `anchor` explícito en F8.39.**

### 11.3 Problemas

- **Resueltos:** 18 (10 en `example` originales + 8 elevados desde propuestos en F8.P8; 6 corregidos a 4 pasos en F8.47)
- **Propuestos:** 16 (reordenados de 29 originales por dificultad; grupos: 5 Básico + 7 Intermedio + 4 Desafiante; F8.53)
- **Temas propuestos:** divergencia/rotacional cálculo, interpretación física, Green cuadrado, Green círculo, integral escalar en curva, TFC, campo conservativo (3 partes), Green verificar, integral sup. cilindro, circulación Stokes, flujo Divergencia, campo potencial R³, área toro, ∇·(∇×F)=0, lámina z=xy masa+CM, demostración conservativo

### 11.4 Notas R1/R2/R3

- R3: Green = central (prueba completa ya presente); Stokes = central (esquema presente); Divergencia = central (esquema presente).
- **Verificado matemáticamente:** V4.9 (29/29 probs; 2 errores encontrados y corregidos: centro de masa esfera primer octante + divergencia de F=(y,xz,z²)).

---

## 12. Checklist universal para reescribir un capítulo

Al comenzar la reescritura de cualquier capítulo C3, verificar:

### Estructura (R1)
- [ ] El capítulo tiene párrafo introductorio antes de la primera `\section`
- [ ] Cada definición va seguida de figura (si tiene interpretación geométrica)
- [ ] El orden es: def → figura → theorem → prueba/esquema → ejemplo → propuestos
- [ ] No hay ejemplos resueltos dentro de `\section{Problemas propuestos}`

### Ejemplos resueltos
- [ ] Todos los `\begin{example}` tienen `\begin{myproof}` con 4 pasos y `\boxed{}`
- [ ] Los 4 pasos usan `\textbf{Paso N.}` (punto, no dos puntos)
- [ ] No hay `\begin{myproof}` fuera de `\begin{example}` ni de `\begin{prob}`
- [ ] No hay `\qquad\square` ni `$\square$` — usar `\boxed{}` en su lugar

### Figuras
- [ ] Toda figura usa `\begin{figure}[H]` (nunca `\begin{center}`)
- [ ] Toda figura tiene `\caption{...}` descriptivo
- [ ] Toda figura tiene `\label{fig:...}` con convención kebab-case
- [ ] Todos los `\node` tienen `anchor` explícito
- [ ] Las figuras pgfplots 3D usan `shader=flat corner` y `samples≤20`

### Problemas
- [ ] Mínimo 8 resueltos (con myproof) y 15 propuestos (sin myproof)
- [ ] Máximo 40 propuestos
- [ ] Los propuestos tienen comentarios de grupo: `% Básico`, `% Intermedio`, `% Desafiante`
- [ ] Ningún propuesto contiene `\begin{myproof}`
- [ ] Los temas cubren todos los subtemas del capítulo

### Compilación
- [ ] Compilar con **LuaLaTeX** (nunca pdflatex)
- [ ] Compilar dos veces para resolver referencias cruzadas
- [ ] 0 errores `!` en el log (los warnings de pgfplots y fonts son inocuos si preexistían)
- [ ] El PDF resultante tiene el número de páginas esperado (referencia: 772 páginas al cierre de F8)

---

## 13. Advertencias y decisiones pendientes

1. **`inttriples.tex` — exceso de propuestos:** ~53 propuestos, por encima del máximo de 40. Requiere decisión del autor para consolidar o marcar algunos como opcionales/desafío. No eliminar sin autorización explícita.

2. **`cap33.tex` vs `cap34.tex` — contenido solapado:** según la Decisión C, cap33 tiene campos vectoriales + integrales de línea + Green; cap34 tiene integrales de superficie + Stokes + Divergencia. Sin embargo, varias figuras que conceptualmente pertenecen a cap33 (rotacional, curva orientada, Green) quedaron físicamente en cap34.tex durante F8. En una reescritura limpia, conviene consolidar la pertenencia de figuras.

3. **Etiquetado formal pendiente (Fase Labeling):** todos los entornos de resultado matemático (theorem, definition, proposition, etc.) aún no tienen `\label` sistemático del tipo `thm:capNN:slug`. Esta fase fue pospuesta hasta después de F8 (ver `PLAN_VERIFICACION_MATEMATICA.md` Sección 7). Al reescribir, aplicar la convención `tipo:capNN:slug-corto` desde el inicio.

4. **Warning `figrayo` duplicado en `vectoresrn.tex`:** label `figrayo` aparece dos veces (L.1221 y L.1264). No bloquea compilación pero debe corregirse. Solo se puede hacer cuando el autor decida cuál de las dos figuras debe conservar el label original.

5. **36 "Citation undefined":** preexistentes de `.bbl` incompleto. Requieren ejecutar BibTeX separadamente en `anfalearNotasCalculo.tex`.
