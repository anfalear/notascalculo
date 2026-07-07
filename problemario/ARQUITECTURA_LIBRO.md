# ARQUITECTURA_LIBRO.md — Visión global del Problemario como unidad Apostol

**Fecha:** 2026-07-06
**Fuentes:** lectura de `anfalearNotasCalculo.tex` + 26 archivos `.tex` fuera de C3 + inventario cuantitativo automatizado (secciones, entornos, figuras, pasos) + `DIAGNOSTICO_PROBLEMARIO.md`, `PROGRESO.md`, `GUIA_REESCRITURA_PROBLEMARIO.md`, `GUIA_REESCRITURA_C3.md`, `PLAN_FASE8_APOSTOL_C3.md`.
**Alcance:** solo diagnóstico y planificación — ningún `.tex` fue modificado.

---

## 1. Mapa completo del libro

### 1.1 Orden real de compilación (35 capítulos, 2 partes)

El maestro define **dos** `\part` (Álgebra Lineal, Cálculo). El libro compilado tiene **35 capítulos**, no 34: el índice objetivo de 34 capítulos usado en todos los `.md` de seguimiento asigna el número 33 a *dos* archivos (`inttriples.tex` y `cap33.tex`). Esta discrepancia de numeración debe tenerse presente al leer los documentos históricos.

| # real | Archivo | Título | Bloque | # índice objetivo |
|---|---|---|---|---|
| 1 | `politicas.tex` | Políticas del curso | Admin | 1 |
| 2 | `complejos.tex` | Números complejos | AL | 3 |
| 3 | `vectoresrn.tex` | Espacio euclídeo n-dimensional | AL | 8 |
| 4 | `matrices.tex` | Matrices y determinantes | AL | 14 |
| 5 | `sel.tex` | Sistemas de ecuaciones lineales | AL | 15 |
| 6 | `espaciosvectoriales.tex` | Espacios vectoriales | AL | 16 |
| 7 | `prodinterno.tex` | EV con producto interno | AL | 17 |
| 8 | `vvpropios.tex` | Valores y vectores propios | AL | 23 |
| 9 | `translineales.tex` | Transformaciones lineales | AL | 24 |
| 10 | `preliminares.tex` | Preliminares | C1 | 2 |
| 11 | `funciones.tex` | Funciones | C1 | 4 |
| 12 | `limites.tex` | Límites y Continuidad | C1 | 5 |
| 13 | `derivadas.tex` | La Derivada | C1 | 6 |
| 14 | `apderivadas.tex` | Aplicaciones de la Derivada | C1 | 7 |
| 15 | `tecintegracion.tex` | Integrales indefinidas y técnicas | C1 | 9 |
| 16 | `intdefinida.tex` | La Integral Definida | C1 | 10 |
| 17 | `apintegral.tex` | Aplicaciones de la integral | C1 | 11 |
| 18 | `impropias.tex` | Integrales Impropias | C1 | 12 |
| 19 | `polares.tex` | Curvas Paramétricas y Coord. Polares | C1 | 13 |
| 20 | `sucesionesyseries.tex` | Sucesiones y Series Reales | C2 | 25 |
| 21 | `sucesionesyseriesfunciones.tex` | Sucesiones y series de funciones | C2 | 26 |
| 22–30 | `funvectoriales` … `cap34` | (9 capítulos de C3, ya intervenidos en F8) | C3 | 18–22, 32–34 |
| 31 | `cap27_EDOs primer orden.tex` | EDOs de primer orden | ED | 27 |
| 32 | `cap28_EDOs orden n.tex` | EDOs lineales de orden superior | ED | 28 |
| 33 | `cap29_Sistemas de EDOs.tex` | Sistemas lineales de EDOs | ED | 29 |
| 34 | `cap30_Sol EDOs Series Potencias.tex` | Series de potencias para EDOs | ED | 30 |
| 35 | `cap31_Transformada de Laplace.tex` | Transformada de Laplace | ED | 31 |

### 1.2 Conexiones explícitas entre capítulos (qué prepara qué)

**Cadena de Álgebra Lineal:**
- `complejos` → prepara raíces de polinomio característico (`vvpropios`), ecuación característica de EDOs (`cap28`, `cap29`) y forma polar usada en raíces complejas.
- `vectoresrn` → prepara producto punto (`prodinterno`), geometría de `sel` (planos como ecuaciones) y todo C3 (rectas, planos, cuádricas). Ya hay referencias cruzadas reales: `sel.tex` cita `\ref{vegern}` y `Definición \ref{def:vectorescoordenadas}`.
- `matrices` → `sel` (la intro de `sel.tex` dice explícitamente "En el capítulo anterior se estudiaron las matrices" — conexión ya escrita) → `espaciosvectoriales` (espacios fila/columna/nulo) → `prodinterno` (Gram-Schmidt, mínimos cuadrados) → `vvpropios` → `translineales` (matriz de una transformación, cambio de base).
- `vvpropios` → prepara directamente `cap29` (sistemas X′=AX por eigenvalores) y contiene ya una sección de aplicaciones a EDOs (decisión del autor de conservarla, Fase 4 ítem 24).

**Cadena de Cálculo:**
- `preliminares` (axiomas de ℝ, sup/inf, vecindades) → `limites` (ε-δ usa vecindades) → `derivadas` → `apderivadas` → `tecintegracion` → `intdefinida` → `apintegral` → `impropias` → `polares`.
- `polares` → prepara `apintdobles` (coordenadas polares en integrales dobles) y `cap33`/`cap34` (parametrización de curvas).
- `sucesionesyseries` → `sucesionesyseriesfunciones` → prepara `cap30` (soluciones en series de potencias: su §1 es literalmente "Repaso de series de potencias").
- C3 (`funvectoriales` … `cap34`) descansa sobre `vectoresrn` (geometría de ℝ³) y `polares` (parametrización).

**Cadena de EDOs:**
- `cap27` usa `tecintegracion` (toda EDO separable/lineal es un problema de integración) y `apderivadas` (modelado con razones de cambio).
- `cap28` usa `complejos` (raíces complejas de la ecuación característica) y `sel` (coeficientes indeterminados = sistema lineal).
- `cap29` usa `vvpropios` de forma esencial (los 3 casos de eigenvalores) y `matrices`.
- `cap30` usa `sucesionesyseriesfunciones` (radio de convergencia, series de potencias).
- `cap31` usa `impropias` (la transformada es una integral impropia — condición de existencia) y `sel` (sistemas vía Laplace).

### 1.3 Agrupación por bloques temáticos

| Bloque | Capítulos reales | Estado tras F1–F8 |
|---|---|---|
| Admin | 1 | Completo (fusión A resuelta) |
| Álgebra Lineal | 2–9 | Matemática verificada; **estructura R1 y figuras R2 muy deficitarias** |
| Cálculo I | 10–19 | 4 pasos completo; **figuras sin estándar figure[H]+caption+label** |
| Cálculo II | 20–21 | Alta calidad de contenido; mismas deudas de figuras y graduación |
| Cálculo III | 22–30 | **Terminado (Fase 8)** — es el patrón de referencia |
| EDOs | 31–35 | Matemática verificada; **cero figuras en los 5 capítulos**; convención de soluciones inconsistente |

---

## 2. Diagnóstico de flujo narrativo

### 2.1 Saltos bruscos y ausencias de motivación entre capítulos

1. **`translineales` (cap 9) → `preliminares` (cap 10):** el salto AL→Cálculo ocurre sin transición; la `\part{Cálculo}` no tiene texto introductorio (ninguna `\part` lo tiene). Un lector lineal pasa de cambio de base a axiomas de ℝ sin aviso. **Falta:** párrafo de apertura de parte.
2. **`vvpropios` (cap 8) carece de párrafo introductorio de capítulo** — es el único capítulo del libro que abre con `\chapter{...}` seguido inmediatamente de una `definition`, sin una sola línea de motivación (verificado en lectura directa). Todos los demás capítulos fuera de C3 tienen intro (impropias, preliminares, sucesiones×2 verificados explícitamente).
3. **`polares` (cap 19) → `sucesionesyseries` (cap 20):** cambio de tema total (geometría → análisis) sin transición; es de hecho el corte C1→C2. Aceptable si se subdivide en partes; si no, necesita párrafo de conexión.
4. **`sucesionesyseriesfunciones` (cap 21) → `funvectoriales` (cap 22):** corte C2→C3 sin transición (Taylor → funciones vectoriales).
5. **`cap34` (cap 30) → `cap27` EDOs (cap 31):** el corte más brusco del libro — de teoremas integrales a EDOs de primer orden, dentro de la misma `\part{Cálculo}`. Las EDOs no dependen de C3; su posición tras C3 es defendible (cap29 necesita vvpropios y cap30 necesita series), pero necesitan su propia `\part`.
6. **`complejos` (cap 2) → `vectoresrn` (cap 3):** funciona (plano complejo → ℝⁿ), pero la conexión no está escrita.
7. **Salto de dificultad interno en AL:** `matrices` y `sel` son operativos y computacionales; `espaciosvectoriales` sube abruptamente al nivel axiomático (10 axiomas, demostraciones). Es el salto natural de la materia, pero la transición merece un párrafo que lo anuncie (el de `espaciosvectoriales` existe pero no menciona el cambio de nivel de abstracción).

### 2.2 Dónde el orden actual no es óptimo pedagógicamente

1. **`vvpropios` (8) antes de `translineales` (9).** El orden estándar (Grossman, Lay, Apostol vol. II) es transformaciones lineales → valores propios: los valores propios se motivan como direcciones invariantes de una transformación, y la diagonalización se lee naturalmente como cambio de base de la matriz de T. Hoy `vvpropios` debe motivar Av=λv sin disponer del lenguaje de transformaciones, y `translineales` cierra la parte sin culminar en nada.
2. **`tecintegracion` (15) antes de `intdefinida` (16).** Defendible (antiderivada como operación inversa, luego la integral definida y el TFC como puente) y coincide con el índice objetivo (9→10). No se propone cambio, pero exige que `intdefinida` remita hacia atrás ("las técnicas del capítulo anterior") y que `tecintegracion` no use integrales definidas sin avisar — su subsección "Sustitución en integrales definidas" (línea 221) **sí las usa antes de definirlas**: inconsistencia de dependencia a revisar como decisión editorial.
3. **EDOs dentro de `\part{Cálculo}`.** Cinco capítulos de una materia distinta sin parte propia.

### 2.3 Propuesta de orden lógico (Decisiones para el autor)

**Propuesta P1 — Partes (bajo riesgo, alta ganancia):** pasar de 2 a 5 partes sin mover ningún capítulo de bloque:

```latex
\part{Álgebra Lineal}          % politicas ... translineales
\part{Cálculo Diferencial e Integral}   % preliminares ... polares
\part{Sucesiones y Series}     % sucesionesyseries, sucesionesyseriesfunciones
\part{Cálculo en Varias Variables}      % funvectoriales ... cap34
\part{Ecuaciones Diferenciales}         % cap27 ... cap31
```
Alternativa mínima: conservar 2 partes y añadir solo `\part{Ecuaciones Diferenciales}` antes de `\input{cap27...}`. **Decisión E1 del autor.**

**Propuesta P2 — Intercambiar `vvpropios` y `translineales`:** nuevo orden AL: … espaciosvectoriales → prodinterno → **translineales → vvpropios**. Justificación en §2.2.1; además `vvpropios` quedaría contiguo a su consumidor real (`cap29` está más cerca en el flujo y las "aplicaciones a EDOs" de vvpropios cierran la parte apuntando hacia adelante). Coste: revisar referencias cruzadas entre ambos archivos y renumerar los `.md`. **Decisión E2 del autor.** Si se rechaza, `vvpropios` necesita como mínimo un párrafo introductorio que motive Av=λv geométricamente sin usar el lenguaje de T (previsto en F9AL.19).

**Propuesta P3 — Texto de apertura por parte:** 4–8 líneas tras cada `\part` describiendo el bloque y su conexión con el anterior. No existe hoy en ninguna parte.

---

## 3. Conceptos transversales que exigen tratamiento consistente

Estas inconsistencias son **de nivel libro**: deben resolverse por decisión única antes de intervenir capítulo por capítulo, porque cada plan de Fase 9 las aplica.

### 3.1 Convención de soluciones en `\begin{prob}` — **la inconsistencia más grave del libro**

Hoy conviven **tres convenciones** incompatibles con la regla C3 ("prob nunca lleva myproof"):

| Estilo | Capítulos | Evidencia (conteo automatizado) |
|---|---|---|
| A. myproof **dentro** de prob (banco resuelto) | complejos (24/24), vectoresrn (26/28), matrices (17/25), sel (15/30), espaciosvectoriales (15/36), prodinterno (22/23), vvpropios (13/14), translineales (22/22), cap30 (16/16), cap31 (21/21) | `prob_con_myproof_dentro` |
| B. myproof **después** de `\end{prob}` (huérfano estructural) | cap27 (19), cap28 (20), cap29 (20), y residuos en matrices (8), sel (8), derivadas (3), limites (2), tecintegracion (2) | `myproof_huerfanos` |
| C. prob **sin** solución (convención C3/GUIA) | todos los C1/C2 principales y todo C3 | — |

**Decisión F del autor (bloqueante para F9AL y F9ED):** elegir una de:
- **F-i (recomendada en los planes):** los propuestos representativos con solución se **elevan a `example`** con 4 pasos; el resto pierde el myproof o se conserva como "banco resuelto" claramente separado de la sección "Problemas propuestos" (p. ej. `\section{Problemas resueltos adicionales}`).
- **F-ii:** legalizar el estilo A como "banco con solución" y actualizar la GUIA (rompe la regla C3 ya aplicada).
En cualquier caso, el estilo B (huérfanos) es un bug estructural en todos los escenarios y se corrige siempre.

> **Resuelta 2026-07-06:** se adoptó **F-i en variante conservadora** (ninguna solución se borra; sección `Problemas resueltos adicionales` antes de `Problemas propuestos`). Texto completo de la resolución en §7.

### 3.2 Notación trigonométrica: `\sen` vs `\sin`
Los 5 capítulos de EDOs usan `\sen` (macro de babel-spanish, conversión hecha en Fase 7); **todo el resto del libro usa `\sin`** (imprime "sin"). El PDF muestra ambas grafías. **Decisión E3:** unificar (recomendado: `\sen` en todo el libro por coherencia con el idioma, vía conversión masiva por bloque; o revertir EDOs a `\sin`). Debe resolverse antes de reescrituras para no propagar la mezcla.

> **Resuelta 2026-07-06:** grafía única `\sen` en todo el libro, vía sustitución mecánica (C3 incluido, solo esta sustitución). Texto completo en §7.

### 3.3 Encabezado de la sección de propuestos — 4 variantes actuales
`\section{Problemas propuestos}` (estándar C3) vs `\section{Problemas Propuestos}` (vectoresrn, limites, derivadas, apderivadas, intdefinida, impropias) vs `\section{Problemas propuestos para el capítulo}` (complejos, sel, espaciosvectoriales) vs `\section{Ejercicios propuestos}` (tecintegracion). Además: `matrices`, `vvpropios`, `translineales`, `prodinterno` **no tienen sección de propuestos** (los probs están dispersos en el cuerpo), y `apderivadas`/`sucesionesyseries`/`sucesionesyseriesfunciones` organizan propuestos **por subsección temática** (patrón distinto pero defendible). **Convención propuesta:** `\section{Problemas propuestos}` única al final; subsecciones temáticas internas permitidas en capítulos largos (se conserva el patrón de apderivadas). **Decisión E4** (los planes la asumen).

> **Resuelta 2026-07-06:** convención propuesta adoptada; `Problemas propuestos` siempre última sección, precedida por `Problemas resueltos adicionales` cuando exista (Decisión F). Texto completo en §7.

### 3.4 Estándar de figuras — 3 regímenes conviviendo
- **C3 (post-F8):** `figure[H]` + `\caption` + `\label{fig:kebab}` + `anchor` explícito. ✔ patrón objetivo.
- **C1/C2:** figuras mayoritariamente en `\begin{center}` sin caption/label: apintegral **26**, apderivadas **21**, polares **12**, sucesionesyseriesfunciones **12**, sucesionesyseries **10**, impropias **7**, intdefinida **5**, preliminares **5** (conteo `\begin{center}`; los tikz dentro coinciden).
- **AL:** figuras en `figure` pero sin caption/label: translineales **19/19 sin ambos**, matrices **8/8**, complejos **7/7**, vectoresrn **24/26 sin ambos** (+ label duplicado `figrayo`).
Los tres planes de Fase 9 incluyen ítems de conversión/auditoría con el protocolo F8.31.

### 3.5 Graduación de propuestos
Tags `% Básico / % Intermedio / % Desafiante`: presentes **solo en C3** (verificado: 0 tags en los 26 archivos fuera de C3). Todos los planes incluyen ítems de graduación con la distribución 25/50/25 de la GUIA.

### 3.6 Protocolo de 4 pasos y marcas residuales
- Formato consolidado en C1/C2/C3/ED para `example` (verificación automatizada: derivadas 26/26, tecintegracion 25/25, apintegral 24/24, EDOs 87/87…).
- **AL es el rezagado:** dentro de `example`, marcas de Paso solo en matrices 19/32, sel 4/5, espaciosvectoriales 10/15, prodinterno 8/9, vvpropios 5/10, translineales 3/10 (el resto son ilustrativos aceptados en Fase 4 — verificar caso a caso en F9AL).
- `vectoresrn` usa el formato antiguo `Paso 1:` (dos puntos) en soluciones de probs.
- Marcas residuales `\square`/`\qedhere` detectadas: **apintegral 17**, derivadas 3, tecintegracion 2, prodinterno 2 (pueden ser legítimas dentro de `proof`; auditar antes de tocar).
- **`impropias.tex`: los 7 ejemplos tienen el myproof FUERA del example** (patrón `\end{example}\begin{myproof}` verificado línea a línea). El capítulo se consideraba "Alto/completo" en Fase 1, pero nunca recibió la corrección de anidamiento que sí recibieron los demás. Bug estructural sistemático.

### 3.7 Etiquetado formal
- Labels de capítulo inconsistentes o ausentes: `\label{numcomp}`, `\label{matrdet}`, `\label{sel}`, `\label{evcpir}`, `\label{funciones}`… sin convención; muchos capítulos sin label.
- Fase Labeling (`thm:capNN:slug`) sigue pospuesta para todo el libro; los planes F9 la aplican solo a resultados centrales nuevos o tocados (aplicarla globalmente es una fase propia posterior).

### 3.8 Nivel de rigor (R3) por bloque — huecos detectados
- `cap27` tiene **cero** entornos `theorem` (ni existencia/unicidad de Picard–Lindelöf ni estructura de la solución lineal). Es el único capítulo del libro sin un solo teorema.
- `cap29` tiene 1 teorema (déficit para sistemas: superposición, estructura de soluciones).
- `vectoresrn` tiene 1 teorema en 2 421 líneas (Cauchy-Schwarz, desigualdad triangular, propiedades del producto cruz están como prosa o definición).
- C1 tiene los centrales demostrados (TVM, TFC, ε-δ, sándwich — verificado en PROGRESO/GUIA).

---

## 4. Capítulos que necesitan párrafo de conexión (anterior ← cap → siguiente)

| Capítulo | Con el anterior | Con el siguiente | Prioridad |
|---|---|---|---|
| `vvpropios` | **Falta TODO el párrafo introductorio** | Falta (→ translineales o → cap29 según Decisión E2) | Alta |
| `preliminares` | Falta: apertura de la parte Cálculo tras AL | Existe (→ funciones implícito) | Alta |
| `cap27` (EDOs) | Falta: apertura del bloque ED tras C3 | Existe cadena interna ED | Alta |
| `sucesionesyseries` | Falta: corte C1→C2 tras polares | Existe (→ series de funciones) | Media |
| `funvectoriales` | Falta: corte C2→C3 (fuera del alcance F9; registrar) | Ya tiene intro propia | Media |
| `complejos` | n/a (primero tras políticas) | Falta (→ vectoresrn) | Media |
| `matrices` | Falta (→ desde vectoresrn) | Ya existe en `sel` (escrita desde el lado de sel) | Baja |
| `translineales` | Existe intro rica | Falta cierre de la parte AL | Baja |
| `polares` | Existe | Falta (→ series o → parte siguiente) | Baja |
| `cap31` | Existe | Falta cierre del libro (opcional: epílogo) | Baja |

Si se adopta P1 (5 partes), las conexiones de frontera de bloque se resuelven con los textos de apertura de parte (P3) y solo quedan las intra-bloque.

---

## 5. Criterio Apostol adaptado por bloque

R1 (orden canónico), R2 (figura obligatoria) y R3 (nivel de demostración) son universales; lo que cambia por materia es **qué significa "motivación geométrica"** y **qué teoremas son centrales**.

### 5.1 Álgebra Lineal (detalle operativo en `PLAN_FASE9_AL.md`)
- **R1-AL:** definición → motivación (geométrica en ℝ²/ℝ³ cuando exista; **algebraica-estructural** cuando el objeto es abstracto: para espacios vectoriales la "figura" puede ser un diagrama de inclusiones o un ejemplo canónico ℝⁿ/polinomios/matrices que ancle la abstracción) → teorema → prueba o esquema → ejemplo 4 pasos → propuestos.
- **R2-AL:** las figuras naturales son: transformaciones del cuadrado unitario en ℝ², proyecciones y ortogonalidad, curvas de nivel de formas cuadráticas, diagramas de subespacios/espacios fundamentales, acción de A sobre vectores propios. No forzar figura donde el concepto es puramente algebraico (axiomas de campo): ahí R2 se satisface con el ejemplo canónico.
- **R3-AL:** centrales (demostración o esquema con pasos): rango-nulidad, Gram-Schmidt (constructiva), caracterización de diagonalizabilidad, Cauchy-Schwarz, unicidad de la RREF (esquema). Operacionales: Cramer, propiedades del determinante, Cayley-Hamilton (esquema). De cálculo: propiedades de operaciones matriciales.

### 5.2 Cálculo I/II (detalle en `PLAN_FASE9_C1C2.md`)
- **R1-C1:** el orden Apostol clásico con **motivación geométrica fuerte y previa**: la figura suele ir *antes* del formalismo (secante→tangente antes de la definición de derivada; área bajo la curva antes de la integral). La variante "figura → definición" es aceptable y hasta preferible en C1; se registra como adaptación explícita de R1.
- **R2-C1:** curvas con tangentes, regiones sombreadas (fillbetween), rectángulos de Riemann, bandas ε-δ, asíntotas, sólidos de revolución; en C2: puntos en la recta acercándose a L, bandas de convergencia uniforme, radios de convergencia.
- **R3-C1:** centrales con demostración completa: ε-δ de límites básicos, sándwich, TVI (esquema), TVM, TFC 1 y 2, criterios de series principales (comparación, razón). Operacionales: reglas de derivación (algunas demostradas, resto referencia), L'Hôpital (esquema), criterios de convergencia avanzados (Raabe: enunciado+ejemplo).

### 5.3 EDOs (detalle en `PLAN_FASE9_EDOs.md`)
- **R1-ED:** definición/tipo de ecuación → **motivación física o geométrica** (campo de pendientes, sistema mecánico/eléctrico) → teorema (existencia-unicidad, estructura de la solución) → método (entorno `pasos`) → ejemplo 4 pasos → aplicaciones modeladas → propuestos. La adaptación clave: en EDOs el "teorema" a menudo es un *método* — se admite `pasos` como sustituto del par teorema/prueba cuando el resultado es un algoritmo, pero los teoremas de estructura (existencia/unicidad, superposición, dimensión del espacio de soluciones) sí exigen enunciado riguroso.
- **R2-ED:** campos de pendientes con curvas solución superpuestas, esquemas físicos (masa-resorte, RL/RLC con `circuitikz` — ya cargado en el preámbulo), familias de soluciones, plano de fases, gráficas de funciones especiales (Bessel, Legendre), señales discontinuas (Heaviside, Dirac). Hoy: **0 figuras en los 5 capítulos** — es el mayor déficit R2 del libro.
- **R3-ED:** centrales: existencia y unicidad (enunciado + esquema de Picard), estructura del espacio de soluciones de la lineal de orden n (Wronskiano), teorema de convolución. Operacionales: fórmulas de coeficientes indeterminados, tabla de transformadas (derivación de entradas clave como ejemplos). Cualitativo: se agrega el análisis por campo de pendientes/plano de fases como sustituto legítimo de la solución cerrada cuando no existe.

---

## 6. Resumen ejecutivo de brechas por bloque (contra criterio Apostol)

| Brecha | AL (7+1 caps) | C1/C2 (11+1 caps) | ED (5 caps) |
|---|---|---|---|
| R1 estructura de secciones | **Crítica**: prodinterno 0 secciones; vectoresrn, sel, vvpropios, translineales 1 sección en 1.3k–2.9k líneas | Buena (todas seccionadas) | Buena |
| R1 párrafo introductorio | vvpropios sin intro | Completo | Completo |
| R1 sección de propuestos | Ausente en matrices, prodinterno, vvpropios, translineales | Presente (naming inconsistente) | Presente |
| R2 figuras nuevas | Media (conceptos clave sin figura) | Media (lista GUIA §4–5) | **Crítica** (0 figuras) |
| Estándar de figuras | **Crítica** (54+ figuras sin caption/label) | **Crítica** (98+ tikz en `center`) | n/a (no hay) |
| R3 demostraciones | vectoresrn 1 thm | Sólido | **cap27 0 thm**, cap29 1 thm |
| 4 pasos en examples | Parcial (AL rezagado) | Completo | Completo |
| myproof huérfanos | matrices 8, sel 8 | impropias **7/7**, derivadas 3, limites 2, tecintegracion 2 | cap27 19, cap28 20, cap29 20 |
| Graduación propuestos | 0 tags | 0 tags; limites 50 y sucfun 48 exceden máx. 40; tecintegracion solo 4 | 0 tags |

**Capítulo con más brechas por grupo:** AL → `matrices.tex` (3 123 líneas con 2 secciones, 8 huérfanos, 8 figuras sin estándar, sin sección de propuestos, banco mixto), con `translineales.tex` y `prodinterno.tex` inmediatamente detrás. C1/C2 → `tecintegracion.tex` (0 figuras, 4 propuestos, heading no estándar, 2 huérfanos, dependencia adelantada de integral definida). ED → `cap27` (0 teoremas, 0 figuras, 19 huérfanos).

---

## 7. Decisiones editoriales (consolidado)

| ID | Decisión | Bloqueante para | Estado |
|---|---|---|---|
| E1 | Estructura de partes (5 partes vs mínimo `\part{ED}`) | Ninguno (independiente) | Abierta |
| E2 | Intercambio translineales ↔ vvpropios | F9AL semanas 4–5 (solo el orden de ejecución) | Abierta |
| E3 | `\sen` vs `\sin` global | Cualquier reescritura masiva | **Resuelta 2026-07-06** — grafía única `\sen` en todo el libro (ver resolución bajo la tabla) |
| E4 | Heading único de propuestos + patrón subsecciones | F9AL/F9C1/F9ED ítems de graduación | **Resuelta 2026-07-06** — cierra F9C1.01 (ver resolución) |
| E5 | Numeración 35 capítulos reales vs índice objetivo de 34 | Referencias en todos los `.md` | **Resuelta 2026-07-06** — el índice de 34 queda obsoleto; toda referencia nueva usa el "# real" de §1.1; nota añadida al inicio de `PROGRESO.md` |
| F | Convención de soluciones en `prob` (§3.1) | F9AL y F9ED casi completos | **Resuelta 2026-07-06** — F-i variante conservadora; cierra F9AL.01 (ver resolución) |
| G | Formato de soluciones EDO (subcaso de F) | F9ED | **Resuelta 2026-07-06** — misma convención F, sin subcaso; cierra F9ED.01 (ver resolución) |
| F9C1.02 | Exceso de propuestos: limites 50, sucesionesyseriesfunciones 48 | F9C1.10 y F9C1.37 | **Resuelta 2026-07-06** — nada se elimina; `% Banco extendido` (ver resolución) |
| — | `figrayo` duplicado en vectoresrn (cuál conserva el label) | F9AL.36 | Abierta |
| — | Exceso de propuestos en inttriples ~53 (pendiente C3 previo) | Fuera de F9 | Abierta |
| — | Dependencia adelantada en tecintegracion §"Sustitución en integrales definidas" | F9C1 semana 4 (nota, no ejecución) | Abierta |

### Resoluciones registradas (2026-07-06, decisión del autor)

**Decisión F — F-i variante conservadora (cierra F9AL.01):**
- Por capítulo, 3–5 probs representativos con solución se elevan a `example` con protocolo de 4 pasos + `\boxed{}`.
- **Todos los demás probs con myproof interno se conservan íntegros**, agrupados en `\section{Problemas resueltos adicionales}` inmediatamente antes de `\section{Problemas propuestos}`. Ninguna solución se borra.
- La sección `Problemas propuestos` queda solo con probs sin solución (convención C3/GUIA).
- El estilo B (myproof huérfano tras `\end{prob}`) es bug estructural: cada huérfano se reencaja dentro de su prob y el prob resultante se trata según las reglas anteriores.
- Desbloquea todos los ítems 🔒F de `PLAN_FASE9_AL.md`.

**Decisión G — misma convención F, sin subcaso especial para EDOs (cierra F9ED.01):**
- Por capítulo (cap27–cap31), 4–6 propuestos representativos con solución se elevan a `example` con 4 pasos + `\boxed{}`.
- **Todos los demás conservan su desarrollo completo dentro del capítulo**, agrupados en `\section{Problemas resueltos adicionales}` inmediatamente antes de `\section{Problemas propuestos}`, igual que en AL. Ninguna solución se borra, se abrevia ni se mueve a un archivo externo.
- No se crea solucionario aparte en ninguna fase.
- Los myproof huérfanos de cap27–cap29 (estilo B) se reencajan dentro de su prob antes de aplicar lo anterior, igual que en F.
- Desbloquea todos los ítems 🔒G de `PLAN_FASE9_EDOs.md`.

**Decisión E3 — grafía única `\sen`:**
- Todo el libro usa `\sen` (y las variantes en español que el preámbulo/babel definan — verificar disponibilidad global antes de ejecutar).
- La ejecución es una sustitución mecánica `\sin` → `\sen` (respetando `\sinh` y palabras que contengan "sin") en los ~30 archivos que usan `\sin`.
- **El bloque C3, aunque cerrado desde F8, recibe únicamente esta sustitución mecánica y nada más.**

**Decisión E4 — heading y organización de propuestos (cierra F9C1.01):**
- Heading único: `\section{Problemas propuestos}` (minúscula en "propuestos"), siempre **última sección del capítulo** (precedida por `Problemas resueltos adicionales` cuando exista, según F).
- En capítulos largos se permiten subsecciones temáticas internas (patrón apderivadas), con tags de graduación dentro de cada subsección.
- Las 4 variantes actuales de heading se renombran cuando cada capítulo sea intervenido en su ítem correspondiente (no de forma masiva anticipada).

**Decisión F9C1.02 — exceso de propuestos (limites 50, sucesionesyseriesfunciones 48):**
- **No se elimina ningún problema.** Los bancos que excedan 40 se reorganizan por subsección temática (amparado en E4); los problemas que superen la cuota se marcan con el comentario `% Banco extendido` y cuentan fuera del mínimo/máximo.
- La aplicación queda en F9C1.10 y F9C1.37.

**Decisión E5 — numeración de capítulos:**
- El libro tiene 35 capítulos reales; el índice objetivo de 34 queda obsoleto. Toda referencia nueva en los `.md` usa el "# real" de §1.1. Los números de capítulo en documentos anteriores al 2026-07-06 siguen el índice viejo (nota añadida al inicio de `PROGRESO.md`).
