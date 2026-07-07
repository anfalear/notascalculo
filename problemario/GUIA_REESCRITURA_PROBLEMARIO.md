# GUÍA DE REESCRITURA — Problemario Completo (34 capítulos)

**Propósito:** referencia operativa para reescribir cualquier capítulo desde cero. Cubre los 34 capítulos en sus cinco materias: Cálculo I (C1), Cálculo II (C2), Álgebra Lineal (AL), Ecuaciones Diferenciales (ED) y Cálculo III (C3). Sintetiza el Criterio Apostol (R1–R3), las convenciones técnicas del proyecto, el inventario de contenido y el estado de verificación matemática de cada capítulo.

**Compilador:** LuaLaTeX — nunca pdflatex.  
**Archivo maestro:** `anfalearNotasCalculo.tex`  
**Referencia detallada C3:** `GUIA_REESCRITURA_C3.md` (figuras con label, secciones exactas).  
**Historial de trabajo:** `PROGRESO.md`, `PROGRESO_VERIFICACION.md`, `PLAN_FASE8_APOSTOL_C3.md`.

---

## 1. Criterio Apostol operativo (universal)

### R1 — Orden canónico dentro de cada capítulo

```
párrafo introductorio → secciones:
  definición → figura geométrica → teorema → prueba/esquema
  → ejemplos resueltos (4 pasos + \boxed{}) → \section{Problemas propuestos}
```

No hay excepciones. Un `\begin{rem}` de interpretación geométrica va después de la definición y antes del teorema.

### R2 — Figura obligatoria

Todo concepto con interpretación geométrica lleva figura TikZ inmediatamente después de la definición o del teorema. No se sustituye con texto ni se remite a páginas anteriores.

### R3 — Nivel de demostración

| Tipo | Tratamiento |
|---|---|
| Teoremas centrales (Green, Stokes, Divergencia, TFC, plano tangente, regla de la cadena, ε-δ, TVM) | Demostración completa o esquema con pasos clave explícitos |
| Teoremas operacionales (Fubini, criterio 2ª deriv., Gram-Schmidt, Cayley-Hamilton) | Enunciado riguroso + esquema geométrico/intuitivo |
| Propiedades de cálculo (linealidad, monotonía, homogeneidad) | Enunciado + referencia |

---

## 2. Convenciones técnicas universales

### 2.1 Entornos LaTeX

| Entorno | Uso |
|---|---|
| `\begin{definition}[Nombre]` | Definición formal |
| `\begin{theorem}[Nombre]` | Teorema, lema, corolario |
| `\begin{rem}[Nombre]` | Observación o interpretación |
| `\begin{example}[Nombre]` | Problema resuelto — siempre con myproof |
| `\begin{myproof}` | Solución con 4 pasos — SIEMPRE dentro de `example` o `prob`, nunca fuera |
| `\begin{prob}` | Problema. En `Problemas propuestos` nunca lleva `myproof`; en `Problemas resueltos adicionales` conserva su `myproof` interno (Decisión F) |
| `\begin{pasos}[Nombre]` | Protocolo o algoritmo |
| `\begin{figure}[H]` | Toda figura — siempre `[H]`, nunca `center` ni flotante libre |

**Decisión F (2026-07-06, F-i variante conservadora) — bancos heredados con soluciones dentro de `prob`:**
- Por capítulo, 3–5 probs representativos con solución se elevan a `example` (protocolo de 4 pasos + `\boxed{}`) en su sección temática.
- Todos los demás probs con solución se conservan íntegros (con su `myproof` interno) agrupados en `\section{Problemas resueltos adicionales}`, colocada inmediatamente antes de `\section{Problemas propuestos}`. Ninguna solución se borra, abrevia ni externaliza.
- `\section{Problemas propuestos}` queda solo con probs sin solución (organización §2.4). En `Problemas resueltos adicionales` el tag de graduación va sobre **cada** prob, porque el banco heredado no está ordenado por dificultad.
- Todo `myproof` huérfano (tras `\end{prob}`, estilo B) es bug estructural: se reencaja dentro de su prob antes de aplicar lo anterior.
- La Decisión G (EDOs, caps. 27–31) sigue esta misma convención sin subcaso especial, con 4–6 elevaciones por capítulo.

### 2.2 Protocolo de ejemplos resueltos

```latex
\begin{example}[Título descriptivo]
  Enunciado.
  \begin{myproof}
    \textbf{Paso 1. Análisis / Estrategia.} ...
    \textbf{Paso 2. Cálculo principal.} ...
    \textbf{Paso 3. Verificación / Caso especial.} ...
    \textbf{Paso 4. Resultado.}
    \[ \boxed{\text{resultado final}} \]
  \end{myproof}
\end{example}
```

**Reglas:**
- Punto (`.`) después de "Paso N", no dos puntos.
- `\boxed{}` obligatorio en Paso 4.
- Para sub-partes (a/b/c): Paso 1 = Estrategia, Paso 2/3/4 = sub-partes.
- Sin `\qquad\square`, sin `$\square$`, sin `\qedhere` en ejemplos.

### 2.3 Estándares de figuras TikZ / pgfplots

**TikZ 2D:**
- `\begin{figure}[H]` + `\caption{...}` + `\label{fig:nombre-kebab}` — los tres son obligatorios.
- `anchor` explícito en **todos** los `\node` (nunca omitir).
- `scale` entre 1.1 y 1.5; < 80 líneas de código TikZ.
- Colores: `blue!70!black` (curvas/regiones), `red!70!black` (vectores/énfasis), `gray!50` (guías).
- Flechas: `->` con punta `stealth` para vectores.
- Campos vectoriales: `\foreach \xi/\yi in {...}` + `\pgfmathsetmacro` para calcular los desplazamientos.
- `fillbetween`: siempre nombrar trayectorias (`name path=`) en el mismo dominio antes de `fill between[of=A and B]`.

**pgfplots 3D:**
- `shader=flat corner`, `samples≤20`, `opacity=0.70–0.80`.
- `colormap/cool` o `colormap/hot` según contraste con vectores añadidos.
- Vectores sobre superficie: `\draw[->,red!70!black] (a,b,c)--(d,e,f)`.

**pgfplots 2D:**
- `axis equal image` en figuras de círculos, cónicas y curvas polares — sin excepción.

### 2.4 Organización de problemas propuestos

```latex
\section{Problemas propuestos}
% Básico
\begin{prob} ... \end{prob}
% Intermedio
\begin{prob} ... \end{prob}
% Desafiante
\begin{prob} ... \end{prob}
```

- Comentario `% Básico`, `% Intermedio`, `% Desafiante` antes del **primer** problema de cada grupo.
- Mínimo 15 propuestos; máximo 40.
- Distribución orientativa: ~25 % Básico, ~50 % Intermedio, ~25 % Desafiante.
- Todos los subtemas del capítulo deben estar cubiertos.

### 2.5 Convención de `\label`

| Tipo | Convención | Ejemplo |
|---|---|---|
| Figura | `fig:nombre-kebab` | `fig:helice_tangente` |
| Sección | `sec:nombre-kebab` | `sec:cambio-var-dobles` |
| Teorema / Def | `thm:capNN:slug` | `thm:cap06:regla-cadena` |

*(La fase de labeling sistemático de teoremas/definiciones está pendiente — ver Sección 8.)*

---

## 3. Checklist universal de cierre

Antes de dar un capítulo por completo, verificar:

- [ ] Párrafo introductorio presente antes de la primera `\section`
- [ ] Orden R1 respetado: def → figura → theorem → prueba → ejemplo → propuestos
- [ ] Ningún `\begin{myproof}` fuera de `\begin{example}` o `\begin{prob}`
- [ ] Ningún `\begin{myproof}` dentro de `\section{Problemas propuestos}`
- [ ] Todos los resueltos tienen 4 pasos con `\textbf{Paso N.}` y `\boxed{}`
- [ ] Todas las figuras: `figure[H]` + `\caption` + `\label{fig:...}` + `anchor` en todos los `\node`
- [ ] Sin `\qquad\square`, `$\square$`, ni `\qedhere` en ejemplos
- [ ] Sin pstricks ni Asymptote
- [ ] Propuestos organizados: `% Básico`, `% Intermedio`, `% Desafiante`
- [ ] Compilación limpia con LuaLaTeX (2 pasadas; 0 errores `!`)

---

## 4. CÁLCULO I — Capítulos 2, 4–13

### Cap. 2 — `preliminares.tex`

**Título:** Preliminares matemáticos  
**Estado ejemplos:** 4/5 con 4 pasos (Fase 3 completo). 1 ejemplo ilustrativo sin cálculo — aceptable.  
**Problemas:** 7 propuestos, 0 con solución.

**Secciones principales:**
- Axiomas de los números reales, inducción matemática
- Valor absoluto (def + propiedades + desigualdades triangular/inversa)
- Intervalos, vecindades, interior/frontera/clausura
- Supremo e ínfimo (Axioma de completitud)

**Verificación matemática (Fase 1):**
- AM-GM corregida: `>` → `\geq` en `l.658`.
- Prob 3 ítem 9 corregido: `4x³-37x²+75` → `4x³-23x²+75` (raíz racional x=5).
- Prob 5 ítem 6 corregido: simplificación `12p²q²/5·15/(4pq)÷3` — reemplazado por `(x²-2x-3)/(x+2) ≥ 0`.

**Figuras recomendadas (R2, pendientes):**
- Recta numérica con intervalo `(a,b)` y vecindad `Vε(x₀)` — TikZ 2D simple.
- Diagrama ε-δ para definición de supremo (punto s con franja `s-ε` visible).

**Pendientes:** Propuestos tienen 0 soluciones — considerar elevar 2–3 a resueltos para cubrir: demostración por inducción, demostración de desigualdad por casos, cálculo de sup/inf.

---

### Cap. 4 — `funciones.tex`

**Título:** Funciones  
**Estado ejemplos:** 11 examples en total: 4 ya formateados, 5 galerías de figuras (sin cálculo), 2 reformateados con 4 pasos (paridad + función por tramos). (Fase 3 completo.)  
**Problemas:** 17 propuestos; verificación V4.3 (muestreo 5/17, 2 typos tipográficos corregidos — no matemáticos).

**Secciones principales:**
- Dominio, rango, gráfica (con galería de figuras pgfplots)
- Funciones pares e impares
- Funciones por tramos; composición; inversa
- Funciones trigonométricas, exponencial, logaritmo
- Funciones definidas por ecuaciones implícitas

**Figuras preexistentes:** galerías de pgfplots 2D para catálogo de funciones (no auditadas con el protocolo F8 de label/caption/anchor — pendiente).

**Figuras recomendadas (R2, pendientes):**
- Gráfica genérica mostrando dominio y rango con flechas.
- Función por tramos con punto relleno/vacío en discontinuidad.
- Reflexión sobre y=x para función inversa.

**Correcciones aplicadas:** Prob17-sub10: "cm" → "m"; caption figura → "Patrón para la tienda de acampar".

**Pendientes:** Auditoría de figuras preexistentes (protocol figure[H] + caption + label + anchor).

---

### Cap. 5 — `limites.tex`

**Título:** Límites y Continuidad  
**Estado ejemplos:** 10/10 reformateados con 4 pasos (Fase 3). Ej.2 (ε-δ) tenía myproof fuera y faltaba `\end{example}` — corregido.  
**Problemas:** ~30 propuestos, 0 con solución en banco.

**Secciones principales:**
- Definición intuitiva de límite → definición ε-δ → unicidad
- Propiedades algebraicas de límites (teoremas)
- Límites laterales; continuidad en punto y en intervalo
- Tipos de discontinuidad; teorema del valor intermedio (TVI)
- Límites al infinito; asíntotas

**Verificación matemática (Fase 1):**
- Error crítico corregido (`l.921`): `p(x)=x^{11}+x-x+2` simplificaba a `x^{11}+2` (siempre positivo → TVI no aplicaba). Corregido a `p(x)=x^{11}+x-1` (p(0)=-1<0, p(1)=1>0 → raíz en (0,1)). ✓

**Figuras recomendadas (R2, pendientes):**
- Diagrama ε-δ (disco agujereado en x₀, banda ε en y) — análogo a `fig:disco_epsilon_delta` de Cap.19.
- Curva con discontinuidad removible / de salto / esencial — TikZ 2D.
- Gráfica con asíntota horizontal y vertical (pgfplots 2D).

**Pendientes:** Ningún propuesto tiene solución — considerar elevar 4–5 a resueltos: ε-δ para un límite lineal, límite indeterminado 0/0 por factorización, límite trigonométrico (sin x/x), continuidad en punto, aplicación TVI.

---

### Cap. 6 — `derivadas.tex`

**Título:** La Derivada  
**Estado ejemplos:** 26/26 reformateados con 4 pasos + `\boxed{}` (Fase 3). Casos especiales: Ej.5 (enunciado en una sola línea), Ej.19-20 (sin línea en blanco entre entornos), Ej.25 (contenido en misma línea que myproof).  
**Problemas:** 37 propuestos; verificación V4.1 (muestreo 10/37, 0 errores).

**Secciones principales:**
- Definición de derivada como límite de cociente incremental → figura tangente
- Reglas de derivación: potencia, producto, cociente, cadena
- Derivadas de trigonométricas, exponencial, logaritmo, inversas
- Derivación implícita
- Derivadas de orden superior; notación Leibniz vs. f'(x)

**Figuras recomendadas (R2, pendientes):**
- Recta secante → recta tangente (límite geométrico), curva con pendiente en punto — TikZ 2D.
- Árbol de regla de la cadena (diagrama de ramas) — TikZ 2D con nodos.

**Pendientes:** Solo 3/37 propuestos tienen solución. Considerar elevar 3–4: derivada por definición de función no-polinomial, regla de la cadena anidada, derivación implícita, derivada de función inversa.

---

### Cap. 7 — `apderivadas.tex`

**Título:** Aplicaciones de la Derivada  
**Estado ejemplos:** 19/19 reformateados con 4 pasos (Fase 3). 7 completados desde cero: TVM demo, 4 L'Hôpital, 2 Newton-Raphson. Nueva `\section{Diferenciales y Aproximaciones Lineales}` añadida.  
**Problemas:** 50 propuestos, 0 con solución en banco; verificación V2.2 (21/21, 1 error corregido).

**Secciones principales:**
- Funciones crecientes/decrecientes (criterio 1ª derivada)
- Extremos locales y globales (criterio 1ª y 2ª derivada)
- Concavidad, puntos de inflexión; trazado de curvas
- Teorema del Valor Medio (TVM) — demostración completa (R3)
- Regla de L'Hôpital (casos ∞/∞ y 0/0)
- Optimización aplicada (máximos/mínimos en contexto)
- Newton-Raphson
- Diferenciales y aproximaciones lineales ← nueva sección (Fase 3)

**Verificación matemática (V2.2):** Ej11 (costo mínimo tubería): resultado `1292.8 USD` → `300√3+800 ≈ 1319.6 USD` corregido.

**Figuras preexistentes:** Figuras TikZ de cuerpos cónicos y geométricos en tasas de cambio relacionadas (aceptables; no auditadas en F8).

**Figuras recomendadas (R2, pendientes):**
- Gráfica con primera derivada positiva/negativa (zonas sombreadas) y extremo local.
- Concavidad: curva con tangentes girando (convexa / cóncava hacia arriba/abajo).
- Setup de optimización geométrica (prisma, cilindro) — TikZ 2D.
- Figura TVM: curva entre A y B con recta secante y recta tangente paralela.

---

### Cap. 9 — `tecintegracion.tex`

**Título:** Integrales indefinidas y técnicas de integración  
**Estado ejemplos:** 25/25 reformateados con 4 pasos (Fase 3). Casos especiales: Ej.10 (tabla tabular preservada), Ej.11/15 (integral cíclica, 3 pasos), Ej.9 (partes repetida).  
**Problemas:** 4 propuestos (muy pocos); verificación V4.2 (4/4 — 100%, 0 errores).

**Secciones principales:**
- Antiderivada y reglas básicas (potencia, trigonométricas, exponencial)
- Sustitución simple (u-sustitución)
- Integración por partes (fórmula + casos: repetición, cíclica)
- Fracciones parciales (casos: distintos/iguales/complejos)
- Sustitución trigonométrica (3 casos: √(a²-x²), √(a²+x²), √(x²-a²))
- Integrales trigonométricas (seno×coseno, tangente×secante)

**Pendientes críticos:**
- Solo 4 propuestos — mínimo recomendado 15. Necesita expansión urgente.
- Distribución sugerida: 5 Básico (sustitución simple), 7 Intermedio (por partes, fracciones parciales), 3 Desafiante (sustitución trig, combinadas).
- No hay figuras de triángulos de referencia para sustitución trigonométrica — necesarios (R2).

**Figuras recomendadas (R2, pendientes):**
- 3 triángulos rectángulos de referencia para sustitución trig (TikZ 2D, minipage triple).

---

### Cap. 10 — `intdefinida.tex`

**Título:** La Integral Definida  
**Estado ejemplos:** 7/7 reformateados con 4 pasos (Fase 3).  
**Problemas:** 15 creados desde cero (Fase 3); verificación V2.1 (15/15, 0 errores).

**Secciones principales:**
- Sumas de Riemann (partición, suma inferior/superior, límite)
- Definición de integral definida como límite
- Propiedades algebraicas (linealidad, monotonía, aditiva)
- Teorema Fundamental del Cálculo (TFC1 y TFC2) — demostración completa (R3)
- Regla de sustitución para integrales definidas
- Valor promedio de una función

**Verificación matemática (V2.1):** 15/15 correctos. Respuestas documentadas en `PROGRESO_VERIFICACION.md` fila V2.1.

**Figuras recomendadas (R2, pendientes):**
- Suma de Riemann: rectángulos bajo la curva con partición etiquetada — TikZ 2D con fillbetween.
- TFC geométrico: área acumulada A(x) como función de x — TikZ 2D.

---

### Cap. 11 — `apintegral.tex`

**Título:** Aplicaciones de la integral  
**Estado ejemplos:** 24/24 ya completos con 4 pasos + `\boxed{}` — **capítulo modelo**. (Fase 1, verificado como capítulo de referencia.)  
**Problemas:** 41 propuestos, 0 con solución.

**Secciones principales:**
- Área entre curvas (tipo I / tipo II)
- Volúmenes de sólidos de revolución: discos, arandelas, cascarones
- Longitud de arco de curva plana
- Superficie de revolución
- Trabajo (resorte, bombeo de fluido)
- Centroide y centro de masa (lámina homogénea)
- Momento de inercia + teorema de Steiner
- Fuerza hidrostática

**Figuras preexistentes:** 19 instancias de `fillbetween` (verificadas en Fase 1 — correctas). Figuras de cuerpos de revolución y geométricos. Usar como modelo de calidad para otros capítulos.

**Nota:** este es el capítulo de mayor calidad pedagógica del libro. Al reescribir cualquier otro capítulo, tomar este como referencia de estructura y densidad de ejemplos.

---

### Cap. 12 — `impropias.tex`

**Título:** Integrales Impropias  
**Estado ejemplos:** 7/7 con 4 pasos y `\boxed{}` (Fase 1, capítulo completo). Prob 15 (elipse/tangente) movido a `apderivadas.tex`.  
**Problemas:** 17 propuestos, 0 con solución.

**Secciones principales:**
- Integral impropia de 1er tipo (límite infinito) — definición como límite
- Integral impropia de 2do tipo (discontinuidad interior) — definición
- Criterios de convergencia (comparación, límite de comparación)
- Función Gamma Γ(n) y sus propiedades básicas

**Figuras preexistentes:** 9 instancias de `fillbetween` (muestreadas en Fase 1 — correctas). Área bajo curva con región infinita sombreada.

**Figuras recomendadas (R2, pendientes):**
- Integral impropia como límite de área (región que "crece" hacia ∞) — TikZ 2D con fillbetween.

---

### Cap. 13 — `polares.tex`

**Título:** Curvas Paramétricas y Coordenadas Polares  
**Estado ejemplos:** 8/8 con 4 pasos y `\boxed{}`. 7 instancias de `axis equal image` (correctas).  
**Problemas:** 12 propuestos; ~4 con solución.

**Secciones principales:**
- Curvas paramétricas: pendiente, longitud de arco, área
- Sistema de coordenadas polares: puntos, curvas básicas
- Conversión cartesiano ↔ polar
- Curvas polares: cardioide, rosas, lemniscata, caracol
- Área en polares (entre curvas)
- Longitud de arco en polares

**Verificación matemática (Fase 1):**
- Ej.2 `l.235`: `32/3-24 = -16/3` → `-40/3` (área correcta = 40/3).
- Ej.7 `l.943+951`: área parcial cardioides `9π/8-√2` → `3π/4-√2`. ✓

**Figuras preexistentes:** 7 figuras pgfplots 2D de curvas polares con `axis equal image`. Las figuras con `domain=0:2*pi` con variable `x` generan advertencias en log (no son errores funcionales).

**Figuras recomendadas (R2):** Sistema de coordenadas polares (punto P con r, θ) ya existe en `apintdobles.tex` como `fig:coordenadas_polares` — referencia cruzada posible.

---

## 5. CÁLCULO II — Capítulos 25–26

### Cap. 25 — `sucesionesyseries.tex`

**Título:** Sucesiones y Series de Números Reales  
**Estado ejemplos:** 13/14 con 4 pasos. Ej.1 descriptivo (sin cálculo, aceptable). Ej.5 `\boxed{}` añadido. Ej.13 placeholder completado. Ej.14 valores a₁–a₅ corregidos.  
**Problemas:** 16 propuestos; ~12 con solución; verificación: en Fase 1 como capítulo completo.

**Secciones principales:**
- Sucesiones: def, límite, monotonía, acotación
- Criterios de convergencia de series: telescópica, geométrica, p-series
- Criterios comparación, razón (D'Alembert), raíz (Cauchy), integral
- Criterio de Leibniz para series alternantes; convergencia absoluta/condicional
- Criterio de Raabe (avanzado)

**Verificación matemática (Fase 1):** Ej.13 placeholder `\ln 2·?/?` → `≈0.605`. Ej.14 valores `a₁=1/6, a₂=3/40` (eran el doble). Cálculo Raabe verificado y correcto. ✓

**Figuras recomendadas (R2, pendientes):**
- Sucesión convergente: puntos en recta numérica acercándose a L — TikZ 2D.
- Serie geométrica: rectángulos de área 1/2ⁿ (demostración geométrica) — TikZ 2D.

---

### Cap. 26 — `sucesionesyseriesfunciones.tex`

**Título:** Sucesiones y Series de Funciones  
**Estado ejemplos:** 12/12 con 4 pasos. (Fase 1, capítulo de alta calidad.)  
**Problemas:** 48 propuestos, 0 con solución en banco.

**Secciones principales:**
- Convergencia puntual vs. convergencia uniforme
- Intercambio de límite con integral/derivada (criterios)
- Series de potencias: radio de convergencia (criterio razón), intervalo de convergencia
- Series de Taylor y Maclaurin; aproximaciones
- Serie de Fourier (si aplica al programa)

**Verificación matemática (Fase 1):** Ej.8 caso 4 (cos x): diagrama TikZ mostraba R=1 en [-1,1] — corregido a R=∞, dom=ℝ. (El texto ya era correcto; solo el diagrama estaba mal.) ✓

**Figuras recomendadas (R2, pendientes):**
- Diagrama de radios de convergencia: recta con punto centro, radio R hacia ambos lados — TikZ 2D.
- Convergencia uniforme: banda de ε alrededor de f con funciones fₙ encerradas — TikZ 2D.

---

## 6. ÁLGEBRA LINEAL — Capítulos 3, 8, 14–17, 23–24

### Cap. 3 — `complejos.tex`

**Título:** Números complejos  
**Estado ejemplos:** no aplica (son demostraciones y cálculos, sin formato 4 pasos en la mayoría). 1 bug estructural corregido: myproof triángulo equilátero dentro de su `\begin{prob}`.  
**Problemas:** ~24 en banco; verificación V3.1 (24/24, 3 errores corregidos).

**Secciones principales:**
- Forma algebraica (a+bi), operaciones, conjugado, módulo
- Representación geométrica (plano complejo, argumento)
- Forma polar / trigonométrica; De Moivre
- Fórmula de Euler (e^{iθ})
- Raíces n-ésimas
- Teorema Fundamental del Álgebra (enunciado)

**Verificación matemática (V3.1):**
- Prob1b: z₁z₂z₃ = -15+i → -9+7i (error en multiplicación).
- Prob1c: numerador (-8-8i)(-5+14i) = 152+152i → 152-72i (signo en paso intermedio).
- Prob4: w̄ en "cuarto" cuadrante → "tercer" cuadrante. ✓

**Figuras preexistentes:** 8 pspicture convertidos a TikZ (círculos, elipses, curvas de nivel elípticas) en Fase 4. Verificar que tienen `figure[H]` + `\caption` + `\label` + `axis equal image` en plano complejo (pendiente auditoría de figuras).

**Figuras recomendadas (R2):**
- Plano complejo con punto z=a+bi, módulo |z|, argumento θ — TikZ 2D con ejes y, `axis equal`.
- De Moivre: puntos raíces n-ésimas distribuidas en círculo de radio 1 — TikZ 2D.

---

### Cap. 8 — `vectoresrn.tex`

**Título:** Espacio euclídeo n-dimensional  
**Estado ejemplos:** 8 examples (5 con 4 pasos; 3 descriptivos aceptables).  
**Problemas:** 23 orgánicos (~20 con solución); verificación V3.2 (23/23, 2 errores corregidos).

**Secciones principales:**
- Vectores en Rⁿ: operaciones, norma, distancia
- Producto punto: definición, ángulo, proyección, desigualdad Cauchy-Schwarz
- Producto vectorial (R³): def como determinante, propiedades geométricas
- Producto mixto (triple escalar): volumen del paralelepípedo
- Rectas en R³ (paramétricas, simétricas)
- Planos en R³ (ecuación normal, distancia punto-plano)
- Cónicas y cuádricas (descripción básica; figuras pgfplots)

**Verificación matemática (V3.2):**
- Prob3e: x=(3,-7/3,-1) → (3,-7/3,**1**) (signo de z).
- Banco P1: mismo error + typo `2u-v+w` → `2u-v-w`. ✓
- Prob12 (9 partes: baricentro, ortocentro, recta de Euler): verificado numéricamente. ✓

**Figuras preexistentes:** figuras pgfplots 3D de cuádricas y planos. Algunas figuras de círculos/elipses 2D faltan `axis equal image` (advertencia DIAGNOSTICO, aún pendiente).

**Pendientes:** añadir `axis equal image` en figuras de cónicas 2D en `vectoresrn.tex` (warning label `figrayo` duplicado en L.1221 y L.1264 — no bloquea compilación pero debe corregirse).

---

### Cap. 14 — `matrices.tex`

**Título:** Matrices y determinantes  
**Estado ejemplos:** 32/32 con título. 20 reformateados con 4 pasos + `\boxed{}`. 12 ilustrativos definitórios (título solo, aceptables).  
**Problemas:** 25 problemas (~25 con solución); verificación V4.4 (25/25, 11 errores corregidos — escaló a Completo).

**Secciones principales:**
- Tipos de matrices (cuadrada, simétrica, triangular, escalonada)
- Operaciones: suma, producto, transpuesta
- Determinante: regla de Sarrus, expansión por cofactores, propiedades
- Inversión de matrices: adjunta, Gauss-Jordan, propiedades
- Rango de una matriz
- Aplicaciones: sistemas, transformaciones

**Verificación matemática (V4.4 — 11 errores, Lote 1 principalmente):**
- Errores en cálculos de determinantes y productos matriciales en primeros 11 problemas.
- Prob23: presentación `A²=[A]=[A]` → `A²=[A]·[A]` (operador faltante).
- Nota estructural: `\begin{myproof}` fuera de `\begin{prob}` en Probs 5, 8, 21, 22 — corregido. ✓

**Figuras recomendadas (R2, pendientes):**
- Representación gráfica de producto matricial AB (filas × columnas con flechas) — TikZ 2D.
- Expansión por cofactores: matriz 3×3 con submatrices sombreadas — TikZ 2D.

---

### Cap. 15 — `sel.tex`

**Título:** Sistemas de ecuaciones lineales  
**Estado ejemplos:** 5/5 con título. Ejs. 2 y 3 con `\boxed{}`. Ej.5 bug estructural corregido (myproof fuera del example).  
**Problemas:** 30 propuestos (~30 con solución); verificación V4.5 (30/30, 4 errores corregidos — escaló a Completo).

**Secciones principales:**
- Sistemas lineales: representación matricial `Ax=b`
- Eliminación gaussiana y Gauss-Jordan
- RREF y pivotes; consistencia y soluciones
- Conjunto solución: única / infinitas / vacío; interpretación geométrica (planos)
- Sistemas homogéneos; dependencia/independencia lineal de filas
- Regla de Cramer (para sistemas de orden pequeño)

**Verificación matemática (V4.5):**
- Env#9: texto pivote `-2` → `-1` (error en demostración pivot).
- Prob11: XB subscript → respuesta incorrecta (corregido con Kronecker).
- Prob13: eliminación con fracciones incorrectas.
- Prob20: RREF incorrecta → coeficientes y P(20) totalmente mal; corregido con NumPy (sistema Vandermonde mal condicionado, cond ≈ 2.7e8). ✓

**Figuras recomendadas (R2, pendientes):**
- 3 planos en R³ (intersección en punto / recta / sin intersección) — pgfplots 3D, minipages.

---

### Cap. 16 — `espaciosvectoriales.tex`

**Título:** Espacios vectoriales  
**Estado ejemplos:** 15/15 con título. 10 computacionales reformateados con Paso N + `\boxed{}`. 5 ilustrativos (título solo).  
**Problemas:** 36 (probs 1-15 con solución, 16-36 "propuestos" sin solución); verificación V4.6 (36/36, 8 errores corregidos — escaló a Completo).

**Secciones principales:**
- Def espacio vectorial (8 axiomas) + ejemplos (Rⁿ, matrices m×n, funciones continuas)
- Subespacios: def + criterio (cerrado bajo suma y escalar)
- Dependencia/independencia lineal
- Base y dimensión; teorema de la base
- Espacios fila, columna, nulo; relaciones dimensionales (Sylvester)
- Cambio de base; coordenadas

**Verificación matemática (V4.6 — 8 errores):**
- Prob5c: det=0 → det=201 (conjunto SÍ era base).
- Prob8: det=2t-3 → t-3 (cálculo incorrecto), t≠3/2 → t≠3.
- Prob9: multiplicación matricial incorrecta.
- Prob12a/b: RREF con rango incorrecto (2→3 / 3→4), bases corregidas.
- Prob13: N(A) generador (-1,2,1,0,0) → (-1,2,1,0,0) [signo en 1er componente].
- Prob14: RREF incorrecta; A corregida.
- Prob15b: cofactores erróneos, det=6t²+15t-9 → 6t²-15t+9. ✓

**Figuras recomendadas (R2, pendientes):**
- Diagrama Venn: subespacio W ⊂ V, con 0 en W — TikZ 2D.
- Representación de base: 2 vectores no colineales en R² generando el plano — TikZ 2D.

---

### Cap. 17 — `prodinterno.tex`

**Título:** Espacios vectoriales con producto interno  
**Estado ejemplos:** 9/9 con título (2 duplicados eliminados). 7 computacionales con Paso N + `\boxed{}`. 2 bugs estructurales corregidos (W⊥ y Gram-Schmidt en R³).  
**Problemas:** 23 (~20 con solución); verificación V3.3 (23/23, 5 errores corregidos).

**Secciones principales:**
- Def producto interno (4 axiomas) + ejemplos (Rⁿ, funciones)
- Norma y distancia inducidas; desigualdad de Cauchy-Schwarz
- Ortogonalidad; complemento ortogonal W⊥
- Proceso de Gram-Schmidt (ortogonalización y ortonormalización)
- Teorema de la proyección ortogonal; mínimos cuadrados
- Base ortonormal; expansión de Fourier

**Verificación matemática (V3.3 — 5 errores):**
- Prob3: error en producto interno.
- Prob5: error en cálculo de norma.
- Prob7: error en Gram-Schmidt paso 2.
- Prob9: error en proyección ortogonal.
- Prob13: error en mínimos cuadrados. (Correcciones aplicadas por el autor.) ✓

**Figuras recomendadas (R2, pendientes):**
- Proyección ortogonal de u sobre v: TikZ 2D con ángulo recto marcado.
- Gram-Schmidt: 3 vectores (original, ortogonalizado, ortonormalizado) — TikZ 2D en R².

---

### Cap. 23 — `vvpropios.tex`

**Título:** Valores y vectores propios  
**Estado ejemplos:** 10/10 con título. 6 computacionales reformateados con Paso N + `\boxed{}`. 4 ilustrativos (título solo). `\begin{myproof}` huérfano del teorema Cayley-Hamilton → `\begin{proof}`. EDOs conservadas por decisión del autor.  
**Problemas:** 14 propuestos (~14 con solución); verificación V4.7 (14/14, 6 errores — escaló a Completo).

**Secciones principales:**
- Def valor/vector propio como `Av=λv`; polinomio característico
- Diagonalización: condición (n vectores propios LI), proceso
- Matrices similares; invariantes bajo similaridad
- Teorema de Cayley-Hamilton
- Potencias de matrices vía diagonalización
- Aplicaciones a sistemas de EDOs y a la diagonalización de formas cuadráticas

**Verificación matemática (V4.7 — 6 errores):**
- Prob1a: mult. geométrica λ=2 es 1 (no 2), (2,0,1) no es eigenvector → A no diagonalizable.
- Prob9a: eigenvalores 2,3,-5 → **0,1,-1** con eigenvectores corregidos.
- Prob9b: A²⁰u corregido con nuevos eigenvalores.
- Prob12c: pol. car. (λ-1)²(λ-5) → (λ-1)(λ-2)(λ-3), eigs 1,2,3. ✓

**Figuras recomendadas (R2, pendientes):**
- Transformación lineal A aplicada al vector propio v: escala pero no rota — TikZ 2D con flechas.
- Diagonalización: diagrama de cambio de base P AP⁻¹ = D — TikZ 2D con cajas.

---

### Cap. 24 — `translineales.tex`

**Título:** Transformaciones lineales  
**Estado ejemplos:** 10/10 con título. 3 computacionales reformateados. 4 ilustrativos (título solo). Eliminados todos los `\qedhere` (3 en Ej.1). 2 bugs estructurales corregidos.  
**Problemas:** 22 propuestos (~22 con solución); verificación V4.8 (22/22, 4 errores — escaló a Completo).

**Secciones principales:**
- Def transformación lineal `T:V→W`; ejemplos (rotación, reflexión, proyección)
- Núcleo (kernel) e imagen; teorema rango-nulidad
- Matriz de transformación respecto a bases dadas
- Cambio de base para la representación matricial
- Composición e inversas de transformaciones
- Transformaciones en R² y R³ (rotación, reflexión, escalado, cizallamiento)

**Verificación matemática (V4.8):**
- Env33: det = -11 → **-10**.
- Prob2k: kernel (1,-1,1) → **(3,-3,2)**.
- Env24: teorema dual dividido en dos (inyectivas → composición inyectiva; invertibles → inversa de composición).
- Prob12: def T reformulada a `T(f)=(f(0),f(π),f(2π))ᵀ` con soluciones reescritas. ✓

**Figuras recomendadas (R2, pendientes):**
- Transformación en R²: cuadrado unitario → paralelogramo bajo rotación de θ° — TikZ 2D.
- Diagrama conmutativo: T∘S con flechas entre espacios V, W, Z — TikZ 2D con nodos.

---

## 7. ECUACIONES DIFERENCIALES — Capítulos 27–31

*(Todos los capítulos ED fueron creados desde cero en Fase 7.)*

### Cap. 27 — `cap27_EDOs primer orden.tex`

**Título:** Ecuaciones Diferenciales de Primer Orden  
**Estado ejemplos:** 8/8 correctamente anidados (myproof dentro de example). 36 `Paso N:` → `Paso N.` corregidos. 17 `\sin` → `\sen`.  
**Problemas:** 19 con myproof separado; verificación V4.10a (muestreo 5/19, 0 errores).

**Secciones principales:**
- Def EDO, orden, solución general/particular/singular; campo de pendientes
- Variables separables: método + ejemplos
- Lineales de 1er orden: factor integrante `μ(x)=e^{∫P dx}`
- Exactas: condición `∂M/∂y = ∂N/∂x`; método de potencial
- Ecuación de Bernoulli: sustitución `v=y^{1-n}`
- Aplicaciones: crecimiento/decaimiento (Malthus), decaimiento radiactivo, circuito RL, mezcla

**Verificación matemática (V4.10a):** muestreo 5/19, 0 errores; 3 entornos Ej/Teo, todos correctos. Sin escalación. ✓

**Figuras recomendadas (R2, pendientes):**
- Campo de pendientes (slope field) de una EDO simple — pgfplots 2D con `quiver`.
- Curva solución superpuesta al campo de pendientes.
- Circuito RL: esquema eléctrico (resistencia, inductancia, fuente) — TikZ 2D.

---

### Cap. 28 — `cap28_EDOs orden n.tex`

**Título:** EDOs Lineales de Orden Superior  
**Estado ejemplos:** 24+ ejemplos correctamente anidados. 83 `Paso N:` → `Paso N.` corregidos. `\sen` correcto.  
**Problemas:** 18 propuestos; verificación V4.10b (20/20, 3 errores corregidos — escaló a Completo).

**Secciones principales:**
- Ecuaciones homogéneas con coeficientes constantes: ecuación característica (3 casos: raíces reales distintas, complejas, repetidas)
- Wronskiano y independencia lineal de soluciones
- Método de coeficientes indeterminados
- Método de variación de parámetros (general)
- Ecuación de Cauchy-Euler: sustitución `x=eᵗ`
- Aplicaciones: masa-resorte (amortiguado/no amortiguado/resonancia), circuito RLC, viga elástica

**Verificación matemática (V4.10b — 3 errores):**
- Prob8: `y''-4y'+4y=e^{2x}cosx` → A=0, B=1 → **A=-1, B=0**.
- Prob19: variación de parámetros, u₁=ln(e^x+1) → **u₁=x-ln(e^x+1)**.
- Ej/Teo23 `y''+4y=tan(2x)`: integral errónea propagó factor 2 en yₚ. ✓

**Figuras recomendadas (R2, pendientes):**
- Masa-resorte: sistema mecánico con masa m, resorte k, amortiguador c — TikZ 2D.
- Soluciones: sub/sobre/críticamente amortiguada + resonancia — pgfplots 2D, 4 curvas.
- Circuito RLC: esquema eléctrico — TikZ 2D.

---

### Cap. 29 — `cap29_Sistemas de EDOs.tex`

**Título:** Sistemas Lineales de EDOs  
**Estado ejemplos:** correctamente anidados. 58 `Paso N:` → `Paso N.`. 76 `\sin` → `\sen`. TikZ figura masa-resorte acoplados presente.  
**Problemas:** 16 propuestos; verificación V4.10c (20/20, 1 error corregido — escaló a Completo).

**Secciones principales:**
- Sistemas `x'=Ax`: conversión a sistema matricial
- Solución por eigenvalores: 3 casos (reales distintos, complejos, repetidos)
- Método de eliminación (para sistemas de orden bajo)
- Sistemas no homogéneos: variación de parámetros matricial
- Aplicaciones: masa-resorte acoplados, modelo depredador-presa (Lotka-Volterra), 2 mallas eléctricas

**Verificación matemática (V4.10c — 1 error):**
- Prob4 (eliminación): `x''-4x'-4x=0` → **x''-4x'+4x=0**; eigenvalor doble λ=2, solución `(c₁+c₂t)e^{2t}`. ✓

**Figuras recomendadas (R2, pendientes):**
- Masa-resorte acoplados (esquema de 2 masas y 3 resortes) — TikZ 2D (preexistente, verificar estándar).
- Trayectorias en plano de fase para los 3 casos de eigenvalores — pgfplots 2D.
- Diagrama de 2 mallas eléctricas — TikZ 2D.

---

### Cap. 30 — `cap30_Sol EDOs Series Potencias.tex`

**Título:** Soluciones en Series de Potencias para EDOs  
**Estado ejemplos:** correctamente anidados. 42 `Paso N:` → `Paso N.`. `\sen` correcto.  
**Problemas:** 16 propuestos; verificación V4.10d (muestreo 5/16, 1 error corregido — sin escalación).

**Secciones principales:**
- Puntos ordinarios: solución en serie de potencias `Σaₙxⁿ`
- Radio de convergencia de la solución
- Método de Frobenius (puntos singulares regulares): ecuación indicial, 3 casos
- Funciones especiales:
  - Bessel cilíndrico `Jₙ(x)`, `Yₙ(x)`
  - Legendre esférico `Pₙ(x)`
  - Hermite `Hₙ(x)`
  - Airy `Ai(x)`, `Bi(x)`

**Verificación matemática (V4.10d — 1 error):**
- Prob14 (Hermite n=1): `y=a₀(1-2x²)` era para n=2. Corrección: serie impar (a₀=0), `y=a₁x` = `H₁(x)=2x`. Verificado: `y=x → 0-2x·1+2x=0`. ✓

**Figuras recomendadas (R2, pendientes):**
- Gráficas de Bessel J₀, J₁, J₂ en [0,20] — pgfplots 2D, diferentes líneas.
- Primeros 4 polinomios de Legendre P₀–P₃ en [-1,1] — pgfplots 2D.

---

### Cap. 31 — `cap31_Transformada de Laplace.tex`

**Título:** Transformada de Laplace  
**Estado ejemplos:** correctamente anidados. 153 `Paso N:` → `Paso N.`. 96 `\sin` → `\sen`. Bug corregido: en Ej `cos(bt)`, parámetro `b` como límite de integración y como frecuencia → límite renombrado `T`.  
**Problemas:** 17 propuestos; verificación V3.5 (21/21, 0 errores; muestreo 9/46 Ej/Teo correctos). ✓

**Secciones principales:**
- Definición `ℒ{f}(s)=∫₀^∞ e^{-st}f(t)dt`; condiciones de existencia
- Tabla de transformadas básicas (con derivaciones)
- Propiedades: linealidad, traslación en s y t, derivada e integral de la transformada
- Transformada inversa: fracciones parciales
- Función escalón de Heaviside; delta de Dirac
- Convolución y teorema de convolución
- Solución de PVI (problema de valor inicial) con condiciones iniciales no nulas
- Sistemas de EDOs via Laplace

**Figuras recomendadas (R2, pendientes):**
- Función escalón `u(t-a)`: salto de 0 a 1 en t=a — TikZ 2D.
- Delta de Dirac como límite de rectángulos unitarios — TikZ 2D.
- Convolución: dos funciones y su convolución (integral de solapamiento) — pgfplots 2D.

---

## 8. CÁLCULO III — Capítulos 18–22, 32–34

Los capítulos de C3 están documentados en detalle en `GUIA_REESCRITURA_C3.md` (inventario de figuras con labels, secciones exactas, correcciones matemáticas por ítem). A continuación se incluye el resumen de cada capítulo para tener la visión completa del libro.

| Cap | Archivo | Título | Resueltos | Propuestos | Figuras F8 | Pendiente |
|---|---|---|---|---|---|---|
| 18 | `funvectoriales.tex` | Funciones de varias variables y vectoriales | 9 | 15 | 8+ (hélice, paraboloide, cuádricas, nivel) | Auditoría figuras non-F8 |
| 19 | `limvariasvariables.tex` | Límites y continuidad en Rⁿ | 13 | 10 | fig:disco_epsilon_delta, fig:trayectorias_limite | — |
| 20 | `planostangentes.tex` | Diferenciación parcial, plano tangente | 9 | 16 | fig:dp_interpretacion_geometrica, fig:plano_tangente_3d, fig:aprox_lineal_dz | — |
| 21 | `gradientes.tex` | Regla de la cadena y derivadas direccionales | 9 | 15 | fig:gradiente_curvas_nivel, fig:derivada_direccional | — |
| 22 | `multiplicadoresintdobles.tex` | Optimización: extremos y Lagrange | 9 | 20 | fig:punto_silla, fig:lagrange_region_factible | — |
| 32 | `apintdobles.tex` | Integrales dobles y aplicaciones | 11 | 18 | fig:region_tipo_I_II, fig:cambio_orden, fig:jacobiano_2x2, fig:coordenadas_polares | — |
| 33 | `inttriples.tex` | Integrales triples | 9 | ~53* | fig:coordenadas_cilindricas, fig:coordenadas_esfericas | *exceso de propuestos |
| 33 | `cap33.tex` | Campos vectoriales e integrales de línea | 6 | 15 | fig:campo_gradiente, fig:campo_conservativo | Figuras de cap34 (rotacional, Green, curva orientada) |
| 34 | `cap34.tex` | Integrales de superficie y teoremas integrales | 18 | 16 | fig:superficie_orientada, fig:green_region_tipo_I, fig:stokes_superficie, fig:divergencia_cancelacion | — |

*`inttriples.tex`: ~53 propuestos superan el máximo de 40. Requiere decisión del autor.

---

## 9. Advertencias y decisiones pendientes (todo el libro)

1. **`inttriples.tex` — exceso de propuestos:** ~53 propuestos > máximo de 40. Decidir cuáles consolidar o marcar como opcionales.

2. **`tecintegracion.tex` — déficit crítico de propuestos:** solo 4 propuestos. Necesita expansión a mínimo 15 antes de que el capítulo sea usable como material de examen.

3. **Figuras no auditadas (non-C3):** los capítulos de C1, C2 y AL no pasaron por la auditoría F8 (protocol figure[H] + caption + label + anchor). Antes de reutilizar figuras preexistentes de estos capítulos, verificar que cumplen el estándar de `figuras_guia.tex`.

4. **`axis equal image` pendiente en AL:** figuras de cónicas, círculos y elipses en `vectoresrn.tex` y `complejos.tex` pueden estar distorsionadas (DIAGNOSTICO Paso 4). Revisar y añadir `axis equal image` donde corresponda.

5. **Etiquetado formal pendiente (Fase Labeling):** ningún entorno de resultado matemático (theorem, definition, etc.) tiene `\label` sistemático del tipo `thm:capNN:slug`. Esta fase fue pospuesta hasta después de F8. Al reescribir, aplicar desde el inicio la convención `tipo:capNN:slug-corto`.

6. **Warning `figrayo` duplicado** en `vectoresrn.tex` L.1221 y L.1264 — dos figuras con el mismo label. No bloquea compilación pero debe corregirse. Requiere decisión del autor sobre cuál figura conserva el label original.

7. **36 "Citation undefined":** preexistentes. Requieren ejecutar BibTeX por separado (`anfalearNotasCalculo.bbl` fue eliminado y regenerado; si desaparecen de nuevo, re-ejecutar BibTeX).

8. **Propuestos sin solución en C1 / C2 / AL:** muchos bancos de propuestos tienen 0 soluciones (especialmente C1: caps 5, 6, 7, 9, 12). En una reescritura, considerar elevar 3–4 propuestos a resueltos en cada uno de estos capítulos para garantizar al menos un ejemplo de cada técnica central.

9. **Figuras de EDO pendientes:** los 5 capítulos de ED (Caps 27–31) tienen 0 figuras TikZ/pgfplots. Son los capítulos que más figuras necesitan según R2 (campos de pendientes, masa-resorte, circuitos, plano de fase, funciones especiales).

---

## 10. Estado de verificación matemática por capítulo

| Cap | Archivo | Estado verificación | Tipo | Errores encontrados | Errores corregidos |
|---|---|---|---|---|---|
| 2 | preliminares.tex | Completo (Fase 1) | Completo | 3 | 3 |
| 3 | complejos.tex | Completo (V3.1) | Completo | 3 | 3 |
| 4 | funciones.tex | Muestreo (V4.3) | 5/17 | 2 (tipográficos) | 2 |
| 5 | limites.tex | Completo (Fase 1) | Completo | 1 | 1 |
| 6 | derivadas.tex | Muestreo (V4.1) | 10/37 | 0 | 0 |
| 7 | apderivadas.tex | Completo (V2.2) | Completo | 1 | 1 |
| 8 | vectoresrn.tex | Completo (V3.2) | Completo | 2 | 2 |
| 9 | tecintegracion.tex | Completo (V4.2) | 4/4 (100%) | 0 | 0 |
| 10 | intdefinida.tex | Completo (V2.1) | Completo | 0 | 0 |
| 11 | apintegral.tex | Fase 1 | Completo | 0 | 0 |
| 12 | impropias.tex | Fase 1 | Completo | 0 | 0 |
| 13 | polares.tex | Fase 1 | Completo | 2 | 2 |
| 14 | matrices.tex | Completo (V4.4) | Completo (escalado) | 11 | 11 |
| 15 | sel.tex | Completo (V4.5) | Completo (escalado) | 4 | 4 |
| 16 | espaciosvectoriales.tex | Completo (V4.6) | Completo (escalado) | 8 | 8 |
| 17 | prodinterno.tex | Completo (V3.3) | Completo | 5 | 5 |
| 18 | funvectoriales.tex | Completo (V1.1) | Completo | 1 (typo) | 1 |
| 19 | limvariasvariables.tex | Completo (V1.4) | Completo | 2 | 2 |
| 20 | planostangentes.tex | Completo (V1.5) | Completo | 1 | 1 |
| 21 | gradientes.tex | Completo (V1.2) | Completo | 6 | 6 |
| 22 | multiplicadoresintdobles.tex | Completo (V1.3) | Completo | 5+6+1 | 12 |
| 23 | vvpropios.tex | Completo (V4.7) | Completo (escalado) | 6 | 6 |
| 24 | translineales.tex | Completo (V4.8) | Completo (escalado) | 4 | 4 |
| 25 | sucesionesyseries.tex | Fase 1 | Completo | 3 | 3 |
| 26 | sucesionesyseriesfunciones.tex | Fase 1 | Completo | 1 (diagrama) | 1 |
| 27 | cap27_EDOs primer orden.tex | Muestreo (V4.10a) | 5/19 | 0 | 0 |
| 28 | cap28_EDOs orden n.tex | Completo (V4.10b) | Completo (escalado) | 3 | 3 |
| 29 | cap29_Sistemas de EDOs.tex | Completo (V4.10c) | Completo (escalado) | 1 | 1 |
| 30 | cap30_Sol EDOs Series.tex | Muestreo (V4.10d) | 5/16 | 1 | 1 |
| 31 | cap31_Transformada Laplace.tex | Completo (V3.5) | Completo | 0 | 0 |
| 32 | apintdobles.tex | Completo (V3.4) | Completo | 0 | 0 |
| 33 | inttriples.tex | Completo (V2.3) | Completo | 0 | 0 |
| 33 | cap33.tex | — | — | — | — |
| 34 | cap34.tex | Completo (V4.9) | Completo (escalado) | 2 | 2 |
