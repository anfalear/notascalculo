# PLAN_FASE9_EDOs.md — Criterio Apostol para Ecuaciones Diferenciales

**Inicio:** Pendiente (plan generado 2026-07-06)
**Objetivo:** Aplicar el criterio Apostol operativo (R1–R3) a los 5 capítulos de EDOs (`cap27_EDOs primer orden`, `cap28_EDOs orden n`, `cap29_Sistemas de EDOs`, `cap30_Sol EDOs Series Potencias`, `cap31_Transformada de Laplace`).
**Compilador:** LuaLaTeX. Todas las figuras en TikZ puro o pgfplots — sin pstricks, sin Asymptote. `circuitikz` ya está cargado en el preámbulo del maestro (disponible para esquemas eléctricos).
**Regla de tamaño:** cada ítem ≤ 300 líneas de código nuevo o modificado.
**Regla de contenido:** nada se elimina sin decisión explícita del autor.
**Prerequisito bloqueante:** Decisión G (formato de las soluciones de los propuestos EDO — subcaso de la Decisión F, ver `ARQUITECTURA_LIBRO.md` §3.1) — ítems marcados 🔒G.
**✅ Decisión G resuelta el 2026-07-06 (misma convención F, sin subcaso especial — ver F9ED.01): todos los ítems 🔒G quedan desbloqueados.**

---

## Criterio Apostol operativo — EDOs

**R1-ED — Orden canónico dentro de cada capítulo:**
párrafo introductorio → definición (tipo de ecuación) → **motivación física o geométrica con figura** (campo de pendientes, sistema mecánico/eléctrico) → teorema de estructura (existencia-unicidad, superposición, dimensión del espacio de soluciones) → método (entorno `pasos`) → ejemplos (4 pasos + `\boxed{}`) → aplicaciones modeladas → `\section{Problemas propuestos}`.

**Adaptaciones propias de EDOs:**
- El "teorema" en EDOs es con frecuencia un **método**: el entorno `pasos` sustituye legítimamente al par teorema/prueba cuando el resultado es un algoritmo (factor integrante, coeficientes indeterminados, Frobenius). Pero los teoremas de estructura sí exigen enunciado riguroso (R3): hoy **cap27 tiene 0 teoremas** — es el único capítulo del libro sin ninguno.
- La motivación es **física antes que geométrica**: el par (modelo físico → ecuación) es el equivalente ED del par (figura → definición) de C1. Toda familia de ecuaciones debería abrir con el fenómeno que la produce.
- El análisis **cualitativo** (campo de pendientes, plano de fases) es contenido de primera clase, no adorno: sustituye a la solución cerrada cuando no existe y es el mejor vehículo de R2 en este bloque.

**R2-ED — Figura obligatoria (tipos apropiados):**
| Concepto | Figura |
|---|---|
| EDO de 1er orden | Campo de pendientes con 2–3 curvas solución superpuestas (`\foreach` + `\pgfmathsetmacro`, patrón F8.17) |
| Modelos de 1er orden | Curvas de crecimiento/decaimiento exponencial; esquema de circuito RL (circuitikz) |
| Orden superior | Sistema masa-resorte-amortiguador (m, k, c); 4 curvas: sub/sobre/críticamente amortiguada + resonancia; circuito RLC |
| Sistemas | Masa-resorte acoplados (ya existe 1 tikz, sin entorno figure); plano de fases para los 3 casos de eigenvalores; 2 mallas eléctricas |
| Series de potencias | Gráficas de Bessel J₀,J₁,J₂ y Legendre P₀–P₃ (pgfplots); esquema de radio de convergencia alrededor de punto ordinario/singular |
| Laplace | Escalón u(t−a); delta de Dirac como límite de pulsos; convolución como solapamiento |

**Estado R2 actual: CERO figuras en entorno `figure` en los 5 capítulos** (cap29 tiene 1 tikzpicture suelto, l.1071, sin caption/label). Es el mayor déficit R2 de todo el libro.

**R3-ED — Nivel de demostración:**
| Tipo | Tratamiento |
|---|---|
| Centrales: existencia y unicidad (Picard–Lindelöf), estructura del espacio de soluciones de la lineal de orden n (Wronskiano, superposición), teorema de convolución | Enunciado riguroso + esquema con pasos clave (iteración de Picard esbozada; independencia ↔ Wronskiano ≠ 0) |
| Operacionales: fórmulas de factor integrante, coeficientes indeterminados, variación de parámetros, ecuación indicial de Frobenius, propiedades de la transformada | Enunciado riguroso + derivación en el caso modelo o entorno `pasos` |
| De cálculo: tabla de transformadas, linealidad | Enunciado + derivación de 2–3 entradas clave como ejemplo |

**Criterio de problemas — EDOs:**
Mínimo 15 propuestos por capítulo (todos cumplen: 19/20/20/16/21), máximo 40; graduación 25/50/25 con tags (hoy: 0 tags). **Peculiaridad del bloque:** los bancos son "resueltos" — caps 27–29 tienen la solución en un `myproof` **después** de `\end{prob}` (huérfano estructural: 19+20+20=59 casos) y caps 30–31 la tienen **dentro** del prob (16+21=37 casos). Las soluciones son breves (2–5 líneas con boxed), no de 4 pasos — formato distinto al resto del libro.

**Estado diagnóstico (inventario automatizado 2026-07-06):**

| Cap real | Archivo | Líneas | Sec/Sub | Ex (4 pasos) | Probs | Estilo solución | Theorems | Figuras |
|---|---|---|---|---|---|---|---|---|
| 31 | cap27 | 554 | 7/2 | 9 (9) | 19 | myproof tras `\end{prob}` (huérfano ×19) | **0** | **0** |
| 32 | cap28 | 689 | 7/3 | 24 (24) | 20 | myproof tras `\end{prob}` (huérfano ×20) | 5 | **0** |
| 33 | cap29 | 1 977 | 6/10 | 15 (15) | 20 | myproof tras `\end{prob}` (huérfano ×20) | 1 | 1 tikz suelto |
| 34 | cap30 | 701 | 5/2 | 9 (9) | 16 | myproof dentro del prob ×16 | 3 | **0** |
| 35 | cap31 | 1 353 | 10/3 | 30 (30) | 21 | myproof dentro del prob ×21 | 10 | **0** |

**Naturaleza del bloque vs C3:** los 5 capítulos nacieron en Fase 7 como borradores corregidos: el protocolo de 4 pasos en examples es del 100 %, la matemática está verificada (V4.10a–d, V3.5) y la estructura de secciones es buena. Lo que les falta es exactamente lo que C3 ganó en F8: **figuras** (aquí desde cero absoluto), **graduación**, **consistencia estructural del banco** (dos estilos internos, ambos fuera de la convención del libro) y **teoremas de estructura** (R3) en cap27 y cap29. A diferencia de C3, aquí la motivación es física: las figuras de aplicación (circuitos, resortes) pesan tanto como las geométricas.

**Observaciones de naturaleza por capítulo:**
- `cap27`: capítulo puerta del bloque; necesita además el párrafo de conexión con C1 (integración) y el teorema de existencia-unicidad que hoy no está ni enunciado.
- `cap28`: el más rico en métodos; sus aplicaciones (masa-resorte, RLC, viga) son las más "figurables" del bloque.
- `cap29`: el más largo (1 977 líneas) y el más conectado con AL (`vvpropios`); el plano de fases es contenido cualitativo nuevo que el capítulo menciona sin figura.
- `cap30`: depende de `sucesionesyseriesfunciones`; las funciones especiales piden gráficas pgfplots directas.
- `cap31`: el mejor dotado de teoremas (10); sus figuras naturales son señales, no geometría.

---

## Semana 0 — Decisión bloqueante

### F9ED.01 — Registrar Decisión G (formato de soluciones del banco EDO) 🔒G
**Archivo:** este `.md` + `GUIA_REESCRITURA_PROBLEMARIO.md`
**Acción:** presentar al autor las opciones, coordinadas con la Decisión F general:
- **G-i (recomendada):** elevar 4–6 propuestos representativos por capítulo a `example` con 4 pasos; los demás quedan como propuestos **sin** solución (las soluciones breves se retiran a un solucionario futuro o se convierten en respuesta final `\boxed{}` sin desarrollo, decisión del autor).
- **G-ii:** conservar el banco resuelto pero **anidando** el myproof dentro del prob (uniformar caps 27–29 al estilo de 30–31) y documentar la excepción en la GUIA.
- **G-iii:** conservar soluciones breves como "Respuesta:" (sin entorno myproof) al final de cada prob.
En todo escenario, los 59 myproof huérfanos de caps 27–29 se corrigen (anidar o retirar según la opción).
**Criterio de cierre:** decisión escrita en ambos `.md`; ítems 🔒G desbloqueados.
**Líneas estimadas:** 10–20 (Markdown)
**Estado:** Completado — 2026-07-06

**Decisión del autor: misma convención F (F-i variante conservadora), sin subcaso especial para EDOs:**
- Por capítulo (cap27–cap31), 4–6 propuestos representativos con solución se elevan a `example` con protocolo de 4 pasos + `\boxed{}`.
- TODOS los demás conservan su desarrollo completo dentro del capítulo, agrupados en `\section{Problemas resueltos adicionales}` inmediatamente antes de `\section{Problemas propuestos}`, igual que en AL. Ninguna solución se borra, se abrevia ni se mueve a un archivo externo.
- No se crea solucionario aparte en ninguna fase (queda descartada la variante de G-i que planteaba retirar soluciones a un solucionario futuro).
- Los myproof huérfanos de cap27–cap29 (estilo B) se reencajan dentro de su prob antes de aplicar lo anterior, igual que en F.
- Quedan desbloqueados todos los ítems 🔒G de este plan (F9ED.05, .10, .16, .19, .23).

---

## Semana 1 — cap27_EDOs primer orden.tex

### F9ED.02 — cap27: teoremas de estructura (R3 — capítulo con CERO teoremas)
**Acción:** añadir en §Definiciones básicas: (a) `theorem` de existencia y unicidad (Picard–Lindelöf, enunciado riguroso con hipótesis de continuidad de f y ∂f/∂y en un rectángulo) + `rem` con esquema de la iteración de Picard y un contraejemplo de no-unicidad (y′=y^{2/3}); (b) `theorem` de la solución general de la lineal de 1er orden (existencia global en el intervalo de continuidad de P, Q). Labels `thm:cap27:existencia-unicidad`, `thm:cap27:lineal-general`.
**Criterio de cierre:** 2 teoremas enunciados con esquema/rem; orden R1 respetado (def → teorema → método); compilación limpia.
**Líneas estimadas:** 60–100
**Estado:** Pendiente

### F9ED.03 — cap27: figura campo de pendientes + curvas solución
**Acción:** figura TikZ (`\foreach` + `\pgfmathsetmacro`, patrón F8.17) del campo de pendientes de una EDO concreta (p. ej. y′=y−x o y′=−y/2) en grilla, con 2–3 curvas solución superpuestas en `blue!70!black`. Insertar inmediatamente después de la definición de solución/campo de pendientes (R2).
**Criterio de cierre:** figura estándar F8 (`figure[H]` + caption + `\label{fig:campo_pendientes}` + anchors); compilación limpia.
**Líneas estimadas:** 50–80
**Estado:** Pendiente

### F9ED.04 — cap27: figuras de aplicaciones (RL + decaimiento/enfriamiento)
**Acción:** (a) esquema del circuito RL con fuente senoidal (circuitikz: R, L, fuente) en §Circuito RL (l.383); (b) familia de curvas de la ley de enfriamiento T(t)=T_a+(T₀−T_a)e^{−kt} (pgfplots, 2–3 valores de T₀) en §Ley de enfriamiento (l.345).
**Criterio de cierre:** 2 figuras estándar F8 dentro de sus subsecciones de aplicación.
**Líneas estimadas:** 60–110
**Estado:** Pendiente

### F9ED.05 — cap27: aplicar Decisión G a los 19 propuestos + graduación 🔒G
**Acción:** corregir los 19 myproof huérfanos según la opción G elegida; si G-i, elevar 4–5 representativos (separable con PVI, lineal con factor integrante, exacta, Bernoulli, aplicación de mezcla) a example con 4 pasos; tags `% Básico / % Intermedio / % Desafiante`.
**Criterio de cierre:** `myproof_huerfanos = 0`; banco graduado con tags; convención G aplicada al 100 %.
**Líneas estimadas:** 60–160 (según opción G)
**Estado:** Pendiente

### F9ED.06 — cap27: párrafo de conexión del bloque ED
**Acción:** ampliar el párrafo introductorio del capítulo para que abra el **bloque** ED: conexión hacia atrás (toda EDO de 1er orden es un problema de integración — `tecintegracion`/`intdefinida`; el modelado con razones de cambio — `apderivadas`) y mapa de los 5 capítulos. Si se aprueba la Decisión E1 (parte propia de EDOs), este texto puede subir a la apertura de la `\part`.
**Criterio de cierre:** párrafo de 6–10 líneas; coherente con la decisión E1.
**Líneas estimadas:** 8–15
**Estado:** Pendiente

---

## Semana 2 — cap28_EDOs orden n.tex

### F9ED.07 — cap28: figura sistema masa-resorte-amortiguador
**Acción:** TikZ 2D del sistema mecánico: pared, resorte k (zigzag), masa m, amortiguador c, eje x(t) con origen en equilibrio. Insertar al inicio de §Aplicaciones/Oscilador armónico (l.462), antes de la deducción mx″+cx′+kx=F(t).
**Criterio de cierre:** figura estándar F8; compilación limpia.
**Líneas estimadas:** 45–70
**Estado:** Pendiente

### F9ED.08 — cap28: figura 4 regímenes de amortiguamiento + resonancia
**Acción:** pgfplots 2D con 4 curvas x(t): subamortiguado (oscilante decreciente), críticamente amortiguado, sobreamortiguado y resonancia (amplitud creciente) — minipage doble o leyenda; colores estándar. Insertar tras la discusión de los 3 casos de la ecuación característica aplicados al oscilador.
**Criterio de cierre:** figura estándar F8 con las 4 curvas etiquetadas sin solapamiento.
**Líneas estimadas:** 60–100
**Estado:** Pendiente

### F9ED.09 — cap28: figura circuito RLC en serie
**Acción:** esquema circuitikz (R, L, C, fuente) en §Circuitos RLC (l.498), con la analogía mecánico↔eléctrico en el caption o en una `rem` adyacente (m↔L, c↔R, k↔1/C).
**Criterio de cierre:** figura estándar F8; analogía explícita.
**Líneas estimadas:** 40–70
**Estado:** Pendiente

### F9ED.10 — cap28: aplicar Decisión G a los 20 propuestos + graduación 🔒G
**Acción:** corregir los 20 myproof huérfanos según G; si G-i, elevar 4–5 (raíces complejas, coeficientes indeterminados con resonancia, variación de parámetros, Cauchy-Euler, masa-resorte con PVI); tags.
**Criterio de cierre:** 0 huérfanos; banco graduado; convención G al 100 %.
**Líneas estimadas:** 60–160
**Estado:** Pendiente

### F9ED.11 — cap28: auditoría R3 (Wronskiano y superposición)
**Acción:** verificar que los 5 teoremas existentes cubren: superposición, dimensión n del espacio de soluciones, Wronskiano ↔ independencia (central: exigir esquema de prueba), solución general = homogénea + particular. Completar esquema donde solo haya enunciado; labels `thm:cap28:slug` a los centrales.
**Criterio de cierre:** tabla teorema→tratamiento en Notas; esquemas añadidos donde falten (≤60 líneas c/u).
**Líneas estimadas:** 30–120
**Estado:** Pendiente

---

## Semana 3 — cap29_Sistemas de EDOs.tex

### F9ED.12 — cap29: encapsular el tikz existente (masa-resorte acoplados)
**Acción:** el tikzpicture de l.1071 está fuera de entorno figure: envolver en `figure[H]` + caption + `\label{fig:masas_acopladas}` + verificar anchors de todos los nodos.
**Criterio de cierre:** 0 tikz fuera de figure en el archivo.
**Líneas estimadas:** 10–25
**Estado:** Pendiente

### F9ED.13 — cap29: figura plano de fases — 3 casos de eigenvalores
**Acción:** minipage triple TikZ/pgfplots 2D: (a) nodo (reales del mismo signo — trayectorias entrando/saliendo), (b) espiral (complejos — foco estable/inestable), (c) silla (reales de signo opuesto — separatrices). Flechas de dirección en cada trayectoria. Insertar tras la presentación de los 3 casos (§l.281–740), donde mejor respete R1.
**Criterio de cierre:** 3 subfiguras estándar F8, etiquetadas por caso, sin solapamiento.
**Líneas estimadas:** 90–150
**Estado:** Pendiente

### F9ED.14 — cap29: figura 2 mallas eléctricas
**Acción:** esquema circuitikz de las dos mallas (fuente, resistencias, inductancias, corrientes i₁, i₂ con sentidos) en §Circuitos eléctricos con dos mallas (l.1160).
**Criterio de cierre:** figura estándar F8 consistente con las ecuaciones del texto (mismos nombres de componentes).
**Líneas estimadas:** 40–70
**Estado:** Pendiente

### F9ED.15 — cap29: teorema de estructura de sistemas (R3 — solo 1 teorema actual)
**Acción:** añadir `theorem` de estructura: el conjunto solución de X′=AX es un espacio vectorial de dimensión n; matriz fundamental y superposición; conexión explícita con `vvpropios` mediante `\ref` (los 3 casos = espectro de A). Esquema de prueba (independencia vía Wronskiano de vectores solución).
**Criterio de cierre:** teorema enunciado con esquema; `\ref` funcional hacia vvpropios; label `thm:cap29:estructura`.
**Líneas estimadas:** 40–80
**Estado:** Pendiente

### F9ED.16 — cap29: aplicar Decisión G a los 20 propuestos + graduación 🔒G
**Acción:** corregir 20 huérfanos según G; si G-i, elevar 4–5 (eliminación, eigenvalores reales/complejos/repetidos, no homogéneo, aplicación); tags.
**Criterio de cierre:** 0 huérfanos; banco graduado; convención G al 100 %.
**Líneas estimadas:** 60–160
**Estado:** Pendiente

---

## Semana 4 — cap30_Sol EDOs Series Potencias.tex

### F9ED.17 — cap30: figuras de funciones especiales
**Acción:** (a) pgfplots 2D de Bessel J₀, J₁, J₂ en [0,20] (tres trazos distinguibles; evaluar con serie truncada o muestras precalculadas — pgfplots no trae Bessel nativa: precalcular puntos con Python y embutir coordenadas); (b) pgfplots 2D de Legendre P₀–P₃ en [−1,1] (polinomios explícitos, plot directo). Insertar en §Aplicaciones y funciones especiales (l.459).
**Criterio de cierre:** 2 figuras estándar F8 con leyendas; compilación limpia (sin dependencias externas).
**Líneas estimadas:** 80–140
**Estado:** Pendiente

### F9ED.18 — cap30: figura esquema de puntos ordinarios/singulares y radio
**Acción:** TikZ 2D: recta (o plano complejo esquemático) con el punto de expansión x₀, los puntos singulares de la ecuación marcados, y el radio de convergencia R = distancia a la singularidad más próxima (círculo/segmento punteado). Insertar tras el teorema de existencia de soluciones en serie (§Soluciones alrededor de puntos ordinarios).
**Criterio de cierre:** figura estándar F8 en posición R2.
**Líneas estimadas:** 40–65
**Estado:** Pendiente

### F9ED.19 — cap30: aplicar Decisión G a los 16 propuestos + graduación 🔒G
**Acción:** los 16 tienen myproof **dentro** del prob (estilo A): aplicar la convención G elegida (si G-i, elevar 3–4: punto ordinario completo, Frobenius con ecuación indicial, Hermite/Legendre; si G-ii, ya están anidados — solo documentar); tags.
**Criterio de cierre:** convención G aplicada; banco graduado.
**Líneas estimadas:** 30–140 (según opción G)
**Estado:** Pendiente

### F9ED.20 — cap30: auditoría R3 (existencia de soluciones en serie + Frobenius)
**Acción:** verificar los 3 teoremas existentes: existencia de solución en serie alrededor de punto ordinario (con radio ≥ distancia a la singularidad) y teorema de Frobenius (3 casos de la ecuación indicial) — enunciados rigurosos; completar esquema/enunciado donde falte; conexión `\ref` con `sucesionesyseriesfunciones` (radio de convergencia).
**Criterio de cierre:** tabla teorema→tratamiento en Notas; `\ref` funcional hacia C2.
**Líneas estimadas:** 20–80
**Estado:** Pendiente

---

## Semana 5 — cap31_Transformada de Laplace.tex + cierre de bloque

### F9ED.21 — cap31: figuras de señales (Heaviside + Dirac)
**Acción:** (a) TikZ 2D del escalón u(t−a): valor 0 hasta a, salto a 1 (punto vacío/lleno), en §Heaviside (l.449); (b) TikZ 2D de la delta de Dirac como límite de pulsos rectangulares de área 1 (3 pulsos de anchura decreciente y altura creciente + flecha vertical δ), en §Delta de Dirac (l.533).
**Criterio de cierre:** 2 figuras estándar F8 en posición R2.
**Líneas estimadas:** 60–100
**Estado:** Pendiente

### F9ED.22 — cap31: figura convolución
**Acción:** pgfplots/TikZ 2D: dos funciones simples (p. ej. dos pulsos o e^{−t} y sen t) y su convolución (f∗g)(t), o esquema del solapamiento f(τ)g(t−τ) con el área sombreada. Insertar antes/después del teorema de convolución (§l.634) según R1.
**Criterio de cierre:** figura estándar F8; coherente con el ejemplo resuelto contiguo.
**Líneas estimadas:** 50–90
**Estado:** Pendiente

### F9ED.23 — cap31: aplicar Decisión G a los 21 propuestos + graduación 🔒G
**Acción:** los 21 tienen myproof dentro del prob: aplicar G (si G-i, elevar 3–4: transformada por definición, inversa con fracciones parciales, PVI con Heaviside, convolución); tags.
**Criterio de cierre:** convención G aplicada; banco graduado.
**Líneas estimadas:** 30–140
**Estado:** Pendiente

### F9ED.24 — cap31: tabla de transformadas — formato y R3
**Acción:** verificar que la tabla de transformadas básicas está en entorno `table`/`figure[H]` referenciable con `\label`, que 2–3 entradas clave se derivan como ejemplo (R3 "de cálculo"), y que el teorema de convolución (central) tiene esquema de prueba; completar lo que falte.
**Criterio de cierre:** tabla etiquetada y referenciada; convolución con esquema; lista en Notas.
**Líneas estimadas:** 20–70
**Estado:** Pendiente

### F9ED.25 — Transversal ED: conexiones inter-capítulo del bloque
**Acción:** verificar/añadir remisiones: cap28→complejos (raíces características, `\ref`), cap29→vvpropios (`\ref`, coordinado con F9AL.22), cap30→sucesionesyseriesfunciones (`\ref`, coordinado con F9ED.20), cap31→impropias (la transformada como integral impropia, `\ref` en la definición). Un párrafo o `rem` de 2–4 líneas por conexión donde falte.
**Criterio de cierre:** las 4 conexiones presentes y compilando (refs resueltas en 2ª pasada).
**Líneas estimadas:** 20–50
**Estado:** Pendiente

### F9ED.26 — Transversal ED: verificación de headings y de huérfanos residuales
**Acción:** confirmar `\section{Problemas propuestos}` estándar en los 5 capítulos (ya lo son — verificar tras las intervenciones); re-escanear myproof huérfanos y `prob_con_myproof_dentro` para confirmar consistencia con la Decisión G en los 5 archivos.
**Criterio de cierre:** grep de variantes = 0; inventario consistente con G en el bloque completo.
**Líneas estimadas:** 5–15
**Estado:** Pendiente

### F9ED.27 — Cierre de bloque: compilación y re-inventario
**Acción:** compilar el maestro (2 pasadas LuaLaTeX); re-ejecutar inventario sobre los 5 archivos; confirmar: ≥12 figuras nuevas en el bloque (antes: 0), 0 huérfanos, tags completos, teoremas de estructura presentes (cap27 ≥2, cap29 ≥2).
**Criterio de cierre:** 0 errores `!`; tabla de re-inventario en Notas; páginas registradas.
**Líneas estimadas:** 0 (verificación)
**Estado:** Pendiente

---

## Registro de progreso

| Ítem | Archivo(s) | Acción | Estado | Fecha | Notas |
|---|---|---|---|---|---|
| F9ED.01 | `.md` | Decisión G registrada | Completado | 2026-07-06 | Misma convención F (F-i conservadora), sin subcaso EDO: elevar 4–6 por cap.; resto íntegro en `Problemas resueltos adicionales`; sin solucionario aparte; huérfanos 27–29 se reencajan. Ítems 🔒G desbloqueados. |
| F9ED.02 | `cap27` | Teoremas existencia-unicidad + lineal (R3) | Completado | 2026-07-24 | `thm:cap27:existencia-unicidad` (Picard–Lindelöf + rem iteración de Picard + contraejemplo `y'=y^{2/3}`); `thm:cap27:lineal-general` colocado en §lineales (mejor R1 que en Definiciones). |
| F9ED.03 | `cap27` | Figura campo de pendientes + soluciones | Completado | 2026-07-24 | `fig:campo_pendientes` (TikZ `\foreach` de `y'=x-y` + 3 curvas `y=x-1+Ce^{-x}`, `\clip`). |
| F9ED.04 | `cap27` | Figuras RL (circuitikz) + enfriamiento | Completado | 2026-07-24 | `fig:circuito_rl` (circuitikz, fuente senoidal); `fig:enfriamiento_curvas` (pgfplots, 3 T₀ incl. uno que se calienta). |
| F9ED.05 | `cap27` | Decisión G ×19 + tags | Completado | 2026-07-24 | 4 elevaciones (#1 sep+PVI, #11 lineal trig, #12 homogénea, #16 inversión x(y)); **nueva §Ecuaciones homogéneas**; 15 resueltos adicionales anidados+tagged; 15 propuestos nuevos SymPy-OK (4B/8I/3D). |
| F9ED.06 | `cap27` | Párrafo de conexión del bloque ED | Completado | 2026-07-24 | Párrafo de apertura (integración `\ref{cap:tecintegracion}` + mapa de los 5 caps). |
| F9ED.07 | `cap28` | Figura masa-resorte-amortiguador | Completado | 2026-07-24 | `fig:masa_resorte` (TikZ 2D, resorte zigzag MANUAL — no hay `decorations.pathmorphing`, aunque circuitikz sí lo carga; pared `pattern`, dashpot). |
| F9ED.08 | `cap28` | Figura 4 regímenes + resonancia | Completado | 2026-07-24 | `fig:regimenes_amortiguamiento` (pgfplots, sub/crít/sobre + resonancia). Trig en pgfplots: `cos(deg(3*x))`. |
| F9ED.09 | `cap28` | Figura RLC + analogía | Completado | 2026-07-24 | `fig:circuito_rlc` (circuitikz) + analogía m↔L, c↔R, k↔1/C en prosa y caption. |
| F9ED.10 | `cap28` | Decisión G ×20 + tags | Completado | 2026-07-24 | 5 elevaciones (#7 resonancia, #9 var. tan x, #11 C-E, #15 osc PVI, #17 RLC forzado); **#20 placeholder retirado (autor OK)**; 14 resueltos adicionales (3B/7I/4D); 15 propuestos nuevos SymPy-OK. |
| F9ED.11 | `cap28` | Auditoría R3 Wronskiano/superposición | Completado | 2026-07-24 | Labels `thm:cap28:superposicion/wronskiano/estructura`; rem con **fórmula de Abel** (W'=−a_{n-1}W ⇒ nunca nula o idénticamente nula). |
| F9ED.12 | `cap29` | Encapsular tikz masas acopladas | Completado | 2026-07-24 | `center`→`figure[H]`+caption+`fig:masas_acopladas`. |
| F9ED.13 | `cap29` | Figura plano de fases (3 casos) | Completado | 2026-07-24 | `fig:plano_fases` (3 minipages: nodo/foco/silla). **Bug corregido:** espiral con `deg(90*t/3.6)` desbordaba «Dimension too large» → ángulo directo en grados `domain=0:900`. |
| F9ED.14 | `cap29` | Figura 2 mallas (circuitikz) | Completado | 2026-07-24 | `fig:dos_mallas` (circuitikz, 2 mallas + M mutua dashed + i₁,i₂ loop arcs). Leve estrechez i₂/E₂ (cosmética, legible). |
| F9ED.15 | `cap29` | Teorema estructura sistemas (R3) | Completado | 2026-07-24 | `thm:cap29:estructura` (espacio vect. dim n, matriz fundamental, Abel) + rem con `\ref{vvpropios}`; label al teorema existente `thm:cap29:solucion-general`. |
| F9ED.16 | `cap29` | Decisión G ×20 + tags | Completado | 2026-07-24 | 5 elevaciones (#3 elim, #5 reales, #7 complejos, #9 repetido defectivo, #11 coef indet); 15 resueltos adicionales (5B/7I/3D, reorg. por script `reorg_cap29_banco.py`); 15 propuestos nuevos SymPy-OK. |
| F9ED.17 | `cap30` | Figuras Bessel + Legendre | Completado | 2026-07-24 | `fig:bessel` (J₀,J₁,J₂ con coords precalculadas por scipy) en §Bessel; `fig:legendre` (P₀–P₃ plot directo) tras Rodrigues. |
| F9ED.18 | `cap30` | Figura puntos singulares + radio | Completado | 2026-07-24 | `fig:radio_singularidades` (plano complejo: x₀ + 2 singularidades + círculo R a la más cercana) tras el teo. de existencia en serie. |
| F9ED.19 | `cap30` | Decisión G ×16 + tags | Completado | 2026-07-24 | 3 elevaciones (#3 serie→e^x, #6 ec. indicial, #11 P₂ Rodrigues); 13 resueltos adicionales (5B/7I/1D, ya estilo A) + 13 propuestos nuevos. Script `reorg_cap30_banco.py`. |
| F9ED.20 | `cap30` | Auditoría R3 + \ref a C2 | Completado | 2026-07-24 | §Repaso referencia `cap:ssfunciones`/`def:serie_potencias`/`thm:radio_convergencia`/`thm:prop_pot`; labels `thm:cap30:existencia-serie` (con `\ref` a radio C2) y `thm:cap30:frobenius`. |
| F9ED.21 | `cap31` | Figuras Heaviside + Dirac | Completado | 2026-07-24 | `fig:heaviside` (salto en $a$, punto lleno/vacío) y `fig:dirac` (2 pulsos anidados de área 1 + flecha δ). |
| F9ED.22 | `cap31` | Figura convolución | Completado | 2026-07-24 | `fig:convolucion` (pgfplots: $e^{-t}$, $e^{-2t}$, $(f*g)=e^{-t}-e^{-2t}$). |
| F9ED.23 | `cap31` | Decisión G ×21 + tags | Completado | 2026-07-24 | 3 elevaciones (#12 inversa por convolución, #16 PVI por tramos, #17 sistema 2×2); 18 resueltos adicionales (6B/9I/3D) + 15 propuestos nuevos. Script `reorg_cap31_banco.py`. |
| F9ED.24 | `cap31` | Tabla transformadas + R3 convolución | Completado | 2026-07-24 | **`tab:transformadas`** creada (no existía; 10 pares $f\!\to\!F$) + ref en el ejemplo de linealidad; label `thm:cap31:convolucion` + rem con **esquema de prueba** (integral doble + cambio $t=\tau+\sigma$). |
| F9ED.25 | 5 caps | Conexiones inter-capítulo (\ref) | Completado | 2026-07-24 | cap28→`\ref{numcomp}` (Euler en raíces complejas); cap31→`\ref{cap:impropias}` (label nuevo en impropias); cap29→`vvpropios` y cap30→`ssfunciones` ya hechas. |
| F9ED.26 | 5 caps | Headings + verificación huérfanos | Completado | 2026-07-24 | Script `check_edos.py`: **0 huérfanos**, 1 §propuestos + 1 §resueltos adicionales por cap, 0 variantes de heading. |
| F9ED.27 | maestro | Compilación + re-inventario | Completado | 2026-07-24 | 2 pasadas lualatex, **842 pp, 0 errores, 0 refs indefinidas, 0 overfull graves**. 8 figuras nuevas del bloque cap30/cap31 verificadas visualmente. |

**Total: 27 ítems — FASE F9-EDOs COMPLETA (27/27) al 2026-07-24.**

**Cierre F9-EDOs (2026-07-24):** completados F9ED.02–.27 en la sesión (F9ED.01 ya estaba). Aportes del bloque: **13 figuras nuevas** (0 antes en los 5 caps), **~10 teoremas/esquemas de estructura** (cap27 pasó de 0 a 2 teoremas), 1 sección nueva (§Ecuaciones homogéneas), 1 tabla de transformadas, **18 elevaciones a `example`**, **73 propuestos nuevos** SymPy-verificados, bancos graduados B/I/D y anidados, y conexiones `\ref` inter-capítulo. PDF **842 pp, 0 errores**. **Contenido del libro congelado → listo para Fase 10 (F10.01 índice analítico).**

---

## Notas de protocolo

- Cada ítem se ejecuta en Claude Code; compilar con LuaLaTeX tras cada ítem; si falla, revertir antes de continuar.
- Antes de cada ítem: leer las primeras 50 líneas del `.tex` destino, recontar entornos reales, compilar al cerrar.
- Ítems 🔒G no arrancan sin F9ED.01 cerrado.
- Este bloque ya usa `\sen`: cualquier texto/figura nueva debe usar `\sen` (no `\sin`) para no reintroducir la mezcla — pendiente de la Decisión E3 global.
- Las figuras pgfplots respetan `shader=flat corner`, `samples≤20`, y las TikZ 2D <80 líneas (estándar `figuras_guia.tex`).
- Elevaciones a resuelto (opción G-i): cada myproof nuevo se presenta al autor antes de escribirlo.
- La matemática está verificada (V4.10a–d, V3.5): no se re-derivan soluciones; inconsistencias detectadas se registran y escalan.
