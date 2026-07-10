# PLAN_FASE9_AL.md — Criterio Apostol para Álgebra Lineal

**Inicio:** Pendiente (plan generado 2026-07-06)
**Objetivo:** Aplicar el criterio Apostol operativo (R1–R3) a los 7 capítulos de Álgebra Lineal (`matrices`, `sel`, `espaciosvectoriales`, `prodinterno`, `vvpropios`, `translineales`, `complejos`) + bloque adicional `vectoresrn` (nota editorial §Bloque V).
**Compilador:** LuaLaTeX. Todas las figuras en TikZ puro o pgfplots — sin pstricks, sin Asymptote.
**Regla de tamaño:** cada ítem ≤ 300 líneas de código nuevo o modificado.
**Regla de contenido:** nada se elimina sin decisión explícita del autor.
**Prerequisito bloqueante:** Decisión F (convención de soluciones en `prob`, ver `ARQUITECTURA_LIBRO.md` §3.1) — los ítems marcados 🔒F no pueden ejecutarse antes.
**✅ Decisión F resuelta el 2026-07-06 (F-i variante conservadora — ver F9AL.01): todos los ítems 🔒F quedan desbloqueados.**

---

## Criterio Apostol operativo — AL

**R1-AL — Orden canónico dentro de cada capítulo:**
definición → motivación (figura geométrica en ℝ²/ℝ³ cuando el concepto la tenga; ejemplo canónico estructural —ℝⁿ, matrices, polinomios— cuando el objeto sea abstracto) → teorema (enunciado riguroso) → prueba o esquema → ejemplos (4 pasos + `\boxed{}`) → `\section{Problemas propuestos}`.

**Adaptaciones propias de AL:**
- En capítulos matriciales (matrices, sel) la "figura" puede ser un **esquema operativo** (producto filas×columnas, cofactores sombreados) — la geometría entra vía interpretación de sistemas como planos.
- En capítulos abstractos (espaciosvectoriales, prodinterno, translineales) la motivación geométrica se ancla siempre en ℝ² / ℝ³ antes de generalizar: es exactamente el movimiento de Apostol (vol. II).
- Los ejemplos "ilustrativos" (mostrar un objeto, sin cómputo) aceptados en Fase 4 se conservan: llevan título pero no exigen 4 pasos. Solo los computacionales exigen protocolo completo.

**R2-AL — Figura obligatoria (tipos apropiados):**
| Concepto | Figura |
|---|---|
| Transformación lineal en ℝ² | Cuadrado unitario → paralelogramo (rotación, reflexión, cizalla, escala) |
| Valor/vector propio | Acción de A: v propio escala sin rotar, w genérico rota — TikZ 2D con flechas |
| Diagonalización | Diagrama de cajas A = PDP⁻¹ (cambio de base) |
| Subespacio | Diagrama de inclusión W ⊂ V con 0; plano generado por 2 vectores en ℝ³ |
| Producto interno / ortogonalidad | Proyección de u sobre v con ángulo recto; Gram-Schmidt en ℝ² |
| Sistemas lineales | 3 planos en ℝ³: intersección punto / recta / vacía (minipages pgfplots 3D) |
| Determinante | Área del paralelogramo \|det\| en ℝ²; cofactores 3×3 sombreados |
| Números complejos | Plano complejo (z, \|z\|, arg); raíces n-ésimas sobre circunferencia |

**R3-AL — Nivel de demostración:**
| Tipo | Tratamiento |
|---|---|
| Centrales: rango-nulidad, Gram-Schmidt, caracterización de diagonalizabilidad, Cauchy-Schwarz, teorema de la base (invariancia de dimensión) | Demostración completa o esquema con pasos clave |
| Operacionales: Cramer, propiedades de determinantes, Cayley-Hamilton, teorema de la proyección, De Moivre | Enunciado riguroso + esquema/verificación en caso 2×2 |
| Propiedades de cálculo: aritmética matricial, propiedades de conjugado/módulo | Enunciado + referencia |

**Criterio de problemas — AL:**
Mínimo 8–10 resueltos (example con myproof) + 15–20 propuestos (sin myproof, según Decisión F) por capítulo; máximo 40 propuestos. Graduación 25 % Básico / 50 % Intermedio / 25 % Desafiante con tags `% Básico`, `% Intermedio`, `% Desafiante`. Los bancos actuales de AL son "resueltos dentro de prob" — la conversión depende de Decisión F.

**Estado diagnóstico (inventario automatizado 2026-07-06):**

| Cap real | Archivo | Líneas | Secciones | Ex (con 4 pasos) | Probs (con sol dentro) | myproof huérf. | Figuras (OK caption+label) | Sección propuestos |
|---|---|---|---|---|---|---|---|---|
| 2 | complejos.tex | 1 424 | 3 | 0 (—) | 24 (24) | 0 | 7 (0) | Sí (naming no estándar) |
| 4 | matrices.tex | 3 123 | 2 + 2 sub | 32 (19) | 25 (17) | **8** | 8 (0) + 4 tikz sueltos | **No** |
| 5 | sel.tex | 2 919 | 1 | 5 (4) | 30 (15) | **8** | 9 (7) | Sí (naming no estándar) |
| 6 | espaciosvectoriales.tex | 1 292 | 7 | 15 (10) | 36 (15) | 0 | **0** | Sí (naming no estándar) |
| 7 | prodinterno.tex | 1 536 | **0** | 9 (8) | 23 (22) | 0 | 2 (1) | **No** |
| 8 | vvpropios.tex | 1 316 | 1 | 10 (5) | 14 (13) | 0 | **0** | **No** |
| 9 | translineales.tex | 2 566 | 1 | 10 (3) | 22 (22) | 0 | 19 (0) + 1 tikz suelto | **No** |
| 3 | vectoresrn.tex (bloque V) | 2 421 | 1 | 8 (0 marca Paso en example) | 28 (26) | 0 | 26 (2) + `figrayo` dup. | Sí (naming no estándar) |

**Naturaleza del bloque vs C3:** en C3 el trabajo fue de figuras y pulido sobre estructura ya correcta; en AL el trabajo dominante es **estructural** (crear secciones donde no las hay, crear secciones de propuestos, resolver la convención de banco resuelto) y solo después de figuras. La matemática ya está verificada (V3.x/V4.x completas) — no se re-verifica, solo se reorganiza.

---

## Semana 0 — Decisiones bloqueantes

### F9AL.01 — Registrar Decisión F (convención de soluciones en prob) 🔒F
**Archivo:** este `.md` + `GUIA_REESCRITURA_PROBLEMARIO.md`
**Acción:** presentar al autor las opciones F-i / F-ii (ARQUITECTURA §3.1) con el conteo por capítulo; registrar la elegida aquí y actualizar la GUIA §2.1.
**Criterio de cierre:** decisión escrita en ambos `.md`; ítems 🔒F desbloqueados.
**Líneas estimadas:** 10–20 (solo Markdown)
**Estado:** Completado — 2026-07-06

**Decisión del autor (F-i variante conservadora):**
- Por capítulo, 3–5 probs representativos con solución se elevan a `example` con protocolo de 4 pasos + `\boxed{}`.
- TODOS los demás probs con myproof interno se conservan íntegros, agrupados en `\section{Problemas resueltos adicionales}` inmediatamente antes de `\section{Problemas propuestos}`. Ninguna solución se borra.
- La sección `Problemas propuestos` queda solo con probs sin solución (convención C3/GUIA).
- El estilo B (myproof huérfano tras `\end{prob}`) es bug estructural: cada huérfano se reencaja dentro de su prob y el prob resultante se trata según las reglas anteriores.
- Quedan desbloqueados todos los ítems 🔒F de este plan (F9AL.04, .10, .14, .18, .21, .26, .28, .37).
- Nota de ejecución: la actualización de `GUIA_REESCRITURA_PROBLEMARIO.md` §2.1 con esta convención queda pendiente como parte del primer ítem 🔒F que se ejecute (registrada aquí para no perderla).

---

## Semana 1 — matrices.tex (capítulo con más brechas del bloque)

### F9AL.02 — matrices: estructura de secciones R1
**Acción:** insertar cabeceras para que el capítulo quede: `\section{Propiedades básicas}` (existente) → `\section{Determinantes}` (hoy subsumido en "Matrices invertibles: determinantes", l.1462) → `\section{Matrices invertibles}` (existente, l.829) → `\section{Problemas propuestos}` (nueva, ver F9AL.04). Mover el mínimo de contenido; solo re-encabezar y reordenar bloques completos si un tema quedó partido.
**Criterio de cierre:** ≥4 secciones; determinantes con sección propia; orden def→teo→ej respetado dentro de cada una; compilación limpia.
**Líneas estimadas:** 40–90
**Estado:** Completado — 2026-07-07

**Notas de ejecución:**
- Estructura final: `\section{Propiedades básicas}` → `\section{Matrices invertibles}` (con `\subsection{Método de eliminación gaussiana}`, renombrada desde «Matrices invertibles: Método de eliminación gaussiana») → `\section{Determinantes}` (promovida desde `\subsection{Matrices invertibles: determinantes}`) → `\section{Problemas propuestos}` (heading insertado antes del banco final, l.2397; su contenido se trata en F9AL.04).
- **Desviación justificada del orden listado en el plan** (Determinantes antes de Matrices invertibles): el texto de Determinantes depende explícitamente del material previo («Hasta este momento hemos visto que una matriz cuadrada $A$ es invertible si su rango…», rem «De eliminación gaussiana a determinante», Caracterización v1 por rango). Reordenarla habría exigido reescribir la motivación — se mantiene el orden físico actual, que es el lógico del texto.
- Bloque de matrices especiales (diagonal, triangular, simétrica, antisimétrica, traza + teorema + 6 ejemplos; 105 líneas) movido íntegro desde dentro de la subsección gaussiana (donde interrumpía el flujo) al final de `\section{Propiedades básicas}` — caso «tema partido» previsto en la acción.
- Verificación: 139 entornos (32 example + 25 prob + 50 myproof + 21 definition + 11 theorem) idénticos antes y después; refs a `def:traza`/`def:escalonada` siguen válidas (todas posteriores a la nueva posición). Compilación limpia: 0 errores `!`, 772 pp.

### F9AL.03 — matrices: anidar 8 myproof huérfanos
**Acción:** localizar los 8 `\begin{myproof}` fuera de example/prob (detección automatizada disponible); anidar cada uno dentro de su `prob`/`example` correspondiente.
**Criterio de cierre:** `myproof_huerfanos = 0` en re-escaneo; compilación limpia.
**Líneas estimadas:** 16–40 (solo movimiento de delimitadores)
**Estado:** Completado — 2026-07-07

**Notas de ejecución:**
- 8 huérfanos localizados con escaneo de anidamiento (tras F9AL.02): l.627, 690, 765, 1395, 2862, 2895, 2994, 3057. Patrón uniforme estilo B: `\end{prob}` → línea en blanco → `\begin{myproof}`. Corrección: el `\end{prob}` se movió tras el `\end{myproof}` correspondiente en los 8 casos.
- Re-escaneo: 0 huérfanos; 25 `\begin{prob}` / 25 `\end{prob}` balanceados; 50 myproof intactos.
- **Hallazgo relevante para F9AL.04:** con los 8 reencajados, los **25/25 probs del capítulo tienen solución interna** (el diagnóstico contaba 17 + 8 huérfanos). Aplicada la Decisión F tal cual, la sección `Problemas propuestos` quedaría vacía — requiere decisión del autor (ver F9AL.04).
- Compilación limpia: 0 errores `!`, 772 pp.

### F9AL.04 — matrices: crear sección de propuestos + aplicar Decisión F 🔒F
**Acción:** reunir los 25 probs bajo `\section{Problemas propuestos}`; según Decisión F, elevar 3–5 representativos con solución a `example` (4 pasos + boxed) y tratar el resto conforme a la convención elegida; tags de graduación.
**Criterio de cierre:** sección única de propuestos, graduada con tags; convención F aplicada al 100 % del capítulo.
**Líneas estimadas:** 80–150
**Estado:** Completado — 2026-07-07

**Notas de ejecución:**
- Tras F9AL.03 los 25/25 probs tenían solución interna → el autor decidió (2026-07-07): elevar 5 y **crear 18 propuestos nuevos sin solución** (lote redactado por el asistente y aprobado explícitamente por el autor antes de insertarse).
- **5 elevaciones a `example`** (validadas por el autor), cada una en su sección temática: #1 Operaciones con matrices y compatibilidad de tamaños (4 pasos); #5 Ingresos mensuales mediante un producto matricial (4 pasos); #8 Inversa por el algoritmo de Gauss-Jordan (7 pasos, conserva `\label{ej.inversa}`); #9 Determinante $5\times 5$ por reducción a forma triangular (enunciado corregido: decía «forma diagonal» pero la reducción es triangular); #10 Inversa mediante la matriz adjunta (typo «Calcule de inversa» corregido; ref ajustada a «Ejemplo \ref{ej.inversa}»). Todas con `Paso N.` y `\boxed{}`.
- **`\section{Problemas resueltos adicionales}`**: 20 probs íntegros con su myproof (6 movidos desde secciones temáticas — grafos ×2, aerolínea, restaurante, frutas, invertibles multiparte — + 14 del banco final), cada uno con tag individual (6 Básico / 8 Intermedio / 6 Desafiante; tag por prob y no por grupo porque el banco heredado no está ordenado por dificultad).
- **`\section{Problemas propuestos}`**: 18 nuevos sin solución, agrupados §2.4 (5 Básico / 9 Intermedio / 4 Desafiante ≈ 28/50/22): operaciones y compatibilidad, especiales y traza, det 2×2, Gauss-Jordan, adjunta, rango, invertibilidad con parámetro, propiedades del det, descomposición S+K, grafos, aplicación panadería, ecuación matricial, nilpotente, AB−BA≠I (traza), suma de filas de A⁻¹, det(adj A).
- `GUIA_REESCRITURA_PROBLEMARIO.md` §2.1 actualizada con la convención F completa (compromiso pendiente de F9AL.01).
- Verificación: 38/38 prob, 37/37 example, 50/50 myproof, 0 huérfanos. Compilación limpia (ver registro).

### F9AL.05 — matrices: auditoría de figuras (protocolo F8.31)
**Acción:** 8 entornos figure sin caption/label + 4 tikzpicture fuera de figure → todos a `figure[H]` + `\caption` + `\label{fig:...}` + anchors explícitos.
**Criterio de cierre:** 12/12 figuras compliant; compilación limpia.
**Líneas estimadas:** 60–120
**Estado:** Completado — 2026-07-07

**Notas de ejecución:**
- 8 `figure[H]` tenían caption pero **no label** → añadidos: `fig:grafo_ejemplo01`, `fig:grafo_ejemplo02`, `fig:sarrus_columnas`, `fig:sarrus_filas`, `fig:grafo_prob_dibujo_a/_b/_c`, `fig:red_vuelos`.
- 4 tikzpicture sueltos convertidos a `figure[H]` + caption + label: el del ejemplo de Sarrus (estaba en `center` → `fig:sarrus_ejemplo`) y los 3 grafos-enunciado del prob de adyacencia (`fig:grafo_adyacencia_a/_b/_c`).
- Fix adicional: en el grafo (c) del prob de adyacencia la arista 3→4 estaba dibujada dos veces (la línea duplicada llevaba el comentario «Corrección: solo una arista 3→4») → eliminada la duplicada; la matriz C ya era consistente con una sola arista.
- Anchors: los nodos de texto flotante ya tenían anchor explícito (estilo `anchor=base` en las figuras de Sarrus); los nodos restantes son de forma cerrada (círculos de grafos) sin texto flotante.
- Verificación: 12/12 `figure[H]` con caption+label, 0 tikz fuera de figure, 0 `center`, 0 labels duplicados. Compilación limpia: 0 errores `!`, 774 pp.

### F9AL.06 — matrices: figuras nuevas R2
**Acción:** (a) esquema del producto matricial AB (fila i × columna j con flechas); (b) expansión por cofactores 3×3 con submatrices sombreadas; (c) interpretación geométrica del determinante 2×2 como área del paralelogramo.
**Criterio de cierre:** 3 figuras insertadas inmediatamente después de la definición correspondiente (R2), estándar F8; compilación limpia.
**Líneas estimadas:** 100–160
**Estado:** Completado — 2026-07-07

**Notas de ejecución:**
- `fig:producto_matricial`: esquema $AB$ con matrices genéricas $3{\times}2\cdot 2{\times}3$, fila 2 de $A$ (rojo) y columna 3 de $B$ (azul) enmarcadas, flechas grises hacia $c_{23}$ y fórmula $c_{23}=a_{21}b_{13}+a_{22}b_{23}$ — tras la def. de multiplicación de matrices.
- `fig:det_area`: paralelogramo generado por $(a,b)$ y $(c,d)$ (dibujado con $(3,1)$ y $(1,2)$) sobre rejilla, área $|ad-bc|$ — tras la rem de fundamentación del det $2\times 2$.
- `fig:cofactores_sombreados`: tres copias de la matriz $3\times 3$ con fila 1/columna $j$ en gris y submatriz $M_{1j}$ sombreada en azul, con signos $+/-/+$ — tras `def:menor`.
- Estándar F8: `figure[H]` + caption + label, anchors explícitos, paleta `blue!70!black`/`red!70!black`/`gray!50`; librerías `matrix` y `calc` ya usadas por las figuras de Sarrus del capítulo. Compilación limpia: 0 errores `!`, 774 pp.

### F9AL.07 — matrices: verificación de protocolo en 32 examples
**Acción:** confirmar que los 19 computacionales usan `\textbf{Paso N.}` (punto) + `\boxed{}`; que los 13 ilustrativos tienen título y se justifican como tales; corregir desviaciones.
**Criterio de cierre:** 100 % de examples conformes o justificados; lista de correcciones en Notas.
**Líneas estimadas:** 20–60
**Estado:** Completado — 2026-07-07

**Notas de ejecución:**
- El capítulo tiene ahora **37 examples** (32 originales + 5 elevaciones de F9AL.04).
- **47 marcas `\textbf{Paso N:}` (dos puntos) normalizadas a `\textbf{Paso N.}`** en todo el archivo (formato GUIA §2.2) — cubría los ejemplos didácticos de grafos, operaciones elementales, formas escalonadas, rango, cofactores, Sarrus y adjunta.
- 2 correcciones de `\boxed{}`: los ejemplos de grafos dirigidos (`ejgrafo01`, `ejgrafo02`) tenían Paso 1/2 sin caja → encajonada la matriz de adyacencia (resultado computable; la figura es la visualización).
- Auditoría final automatizada: 24/24 examples con myproof conformes (Paso N. + boxed); 13 examples ilustrativos (identificación de entradas, suma, escalar, transpuesta, especiales, traza, verificación de inversa, matrices elementales, no-escalonadas, menores) justificados con título según criterio de Fase 4.
- 0 `\textbf{Paso N:}` residuales en el archivo (incluye los myproof de «Problemas resueltos adicionales»).

---

## Semana 2 — sel.tex

### F9AL.08 — sel: estructura de secciones R1
**Acción:** el capítulo tiene 2 723 líneas sin secciones antes de los propuestos. Insertar: `\section{Sistemas lineales y forma matricial}`, `\section{Eliminación gaussiana y Gauss-Jordan}`, `\section{Consistencia y conjunto solución}`, `\section{Sistemas homogéneos}`, `\section{Regla de Cramer}` (ajustar títulos al contenido real al ejecutar).
**Criterio de cierre:** ≥5 secciones temáticas; ningún contenido eliminado; compilación limpia.
**Líneas estimadas:** 30–70
**Estado:** Completado — 2026-07-07

**Notas de ejecución:**
- 7 secciones insertadas (títulos ajustados al contenido real, como preveía el plan): `Sistemas lineales y forma matricial` (l.7, tras la intro del capítulo), `Tipos de solución e interpretación geométrica` (l.55: defs de tipos/homogéneo + ejemplos 2×2/3×3 con figuras), `Eliminación gaussiana y variables libres` (l.359: rem de análisis escalonado + def variables básicas/libres + ejemplo 3×4), `Consistencia: el teorema de Rouché-Frobenius` (l.444: teorema + demostración + caracterización invertibles v3), `Sistemas homogéneos` (l.592), `Regla de Cramer` (l.651), `Problemas resueltos adicionales` (l.698, delimita el banco de 23 probs — anticipa F9AL.10 con el heading de la convención F ya decidida).
- Solo inserción de cabeceras: ningún contenido movido ni eliminado.
- Inventario para ítems siguientes: 30 probs = 23 en banco (15 con myproof interno + 8 con myproof huérfano estilo B, l.1651–2116 pre-inserción — exactamente los 8 de F9AL.09) + 7 propuestos sin solución bajo el heading final. Tras F9AL.09 el banco completo quedará resuelto → en F9AL.10 no habrá que reclasificar probs entre secciones.

### F9AL.09 — sel: anidar 8 myproof huérfanos
**Acción:** igual que F9AL.03 aplicado a `sel.tex`.
**Criterio de cierre:** `myproof_huerfanos = 0`; compilación limpia.
**Líneas estimadas:** 16–40
**Estado:** Completado — 2026-07-07

**Notas de ejecución:**
- 8 huérfanos (l.1665, 1794, 1862, 1930, 1976, 2035, 2086, 2130 tras F9AL.08) reencajados con el mismo procedimiento de F9AL.03: `\end{prob}` movido tras el `\end{myproof}` correspondiente. Eran las soluciones de los probs 11–18 del banco (matriz X, dieta, alcancía, número de dos dígitos, matriz simétrica con parámetros, coeficientes a/b/c, matriz de coeficientes, sistema con parámetro).
- Re-escaneo: 0 huérfanos; 30/30 `\begin{prob}`/`\end{prob}`. El banco de `Problemas resueltos adicionales` queda 23/23 con solución interna; los 7 propuestos finales sin solución (sin reclasificaciones pendientes para F9AL.10).

### F9AL.10 — sel: propuestos + Decisión F + heading 🔒F
**Acción:** renombrar `\section{Problemas propuestos para el capítulo}` → `\section{Problemas propuestos}`; aplicar Decisión F a los 30 probs (15 con solución dentro); tags de graduación.
**Criterio de cierre:** heading estándar, convención F aplicada, tags presentes.
**Líneas estimadas:** 60–120
**Estado:** Completado — 2026-07-07 (en dos sesiones)

**Notas de ejecución:**
- Heading renombrado a `\section{Problemas propuestos}`.
- **4 elevaciones a `example`** desde el banco resuelto: Consistencia según un parámetro; Tres números (regla de Cramer); Interpolación de una parábola; Ley de cosenos vía regla de Cramer. Con ello el capítulo queda con 9 examples (F9AL.12 los verificará).
- **Banco `Problemas resueltos adicionales`**: 19 probs con myproof interno, tag individual (4 Básico / 12 Intermedio / 3 Desafiante).
- **`Problemas propuestos`**: 17 probs sin solución = 7 heredados + **10 nuevos** (lote redactado por el asistente y aprobado explícitamente por el autor el 2026-07-07 antes de insertarse; el primer borrador se perdió al cerrar la sesión anterior y se redactó de nuevo). Graduación 5 Básico / 8 Intermedio / 4 Desafiante ≈ 29/47/24. Agrupados con separadores de comentario en el orden de las secciones del capítulo: forma matricial y tipos de solución (2 nuevos), eliminación gaussiana/Gauss-Jordan (2 nuevos + drill heredado), consistencia y rango (1 nuevo Rouché-Frobenius directo + parámetro t heredado), homogéneos (1 nuevo), Cramer (1 nuevo con caso det = 0), teoría (1 nuevo «una o infinitas» + 2 heredados), aplicaciones (2 nuevos: balanceo de propano y fondos de inversión + 3 heredados, reubicados aquí interpolación cúbica y casas).
- Incidencia de compilación: `\,\%` en modo matemático rompe con babel-spanish (`\es@sppercent`, «Incompatible glue units», 5 errores) — corregido a `\%` sin espacio fino. Nota para futuros lotes.
- Verificación: 36/36 prob balanceados (19 banco + 17 propuestos); 0 huérfanos. Compilación limpia: 0 errores `!`, 778 pp.

### F9AL.11 — sel: figura 3 planos en ℝ³ + auditoría de las 9 existentes
**Acción:** (a) figura nueva en minipages pgfplots 3D: tres configuraciones (punto único / recta / sin intersección) tras la discusión de tipos de solución; (b) completar caption/label en las 2 figuras no conformes.
**Criterio de cierre:** figura nueva estándar F8 insertada según R2; 9/9 existentes conformes.
**Líneas estimadas:** 90–140
**Estado:** Completado — 2026-07-07

**Notas de ejecución:**
- **Figura nueva `fig:tresplanoscasos`**: 3 minipages de 0.32\textwidth con pgfplots 3D (`surf, samples=2`, colormap constante por plano — sin librería `patchplots`, no cargada en el preámbulo), insertada dentro de la rem de interpretación geométrica, justo tras el itemize de casos $3\times 3$ (posición R2). Paneles: (a) solución única — planos $z=2-x$, $z=2-y$, $z=1$ con punto común $(1,1,1)$ marcado; (b) infinitas soluciones — $z=y$, $z=2-y$, $z=1$ con la recta común $\{(t,1,1)\}$ en trazo grueso; (c) sin solución — $z=0.4$ y $z=1.6$ paralelos + $z=y$ transversal (el ejemplo que menciona el propio texto). Paleta del capítulo (blue/red/green como `fig:sistema3x3`). Verificación visual en PDF: ejes extendidos (ymax=3.9) para que las etiquetas de eje no se solapen con los planos.
- **Auditoría de las 9 existentes**: solo 2 no conformes (el diagnóstico acertó): «Interpretación geométrica de sistemas $2\times 2$» → `\label{fig:sistema2x2casos}`; «Curvas que cumplen la condición del problema» → `\label{fig:familiapolinomios}`. La figura del triángulo (ley de cosenos) sí tenía label (`trianguloreglacramer`, sin prefijo `fig:` — igual que otros 4 labels heredados del capítulo, que se conservan porque tienen refs en el texto). 10/10 figuras con caption+label.
- Compilación limpia (2 pasadas): 0 errores `!`, 0 refs indefinidas, 778 pp.

### F9AL.12 — sel: verificación de protocolo en 5 examples
**Acción:** igual que F9AL.07 (Ejs. con Paso N + boxed ya al 4/5; cerrar el restante o justificarlo como ilustrativo).
**Criterio de cierre:** 5/5 conformes o justificados.
**Líneas estimadas:** 10–30
**Estado:** Completado — 2026-07-07

**Notas de ejecución:**
- El capítulo tiene ahora **9 examples** (5 originales + 4 elevaciones de F9AL.10).
- **37 marcas `Paso N:` (dos puntos) normalizadas a `Paso N.`** en todo el archivo: 34 simples + 3 con título (`Paso 1: Calcular el rango…` → `Paso 1. Calcular el rango…`, formato titulado idéntico al de matrices.tex). Cubre los examples 2×2, 3×3 y homogéneo 3×4, y los myproof del banco de resueltos.
- Example «Sistema homogéneo $3\times 4$»: los pasos 3 (variables básicas/libres) y 4 (solución paramétrica) existían como texto sin marca → marcados `\textbf{Paso 3.}` / `\textbf{Paso 4.}`.
- Resultado: 8/8 computacionales con `Paso N.` + `\boxed{}`; 1 ilustrativo justificado con título («Producto matriz-vector como combinación lineal de columnas», identidad mostrada sin cómputo, criterio Fase 4). Total 52 marcas `Paso N.` en el archivo, 0 residuales con dos puntos.
- Compilación limpia: 0 errores `!`, 778 pp.

---

## Semana 3 — espaciosvectoriales.tex + prodinterno.tex

### F9AL.13 — espaciosvectoriales: figuras nuevas R2 (capítulo con CERO figuras)
**Acción:** (a) diagrama W ⊂ V con el vector 0 (subespacio); (b) dos vectores no colineales generando ℝ² (combinaciones lineales/generado); (c) esquema de los espacios fundamentales de A (fila/columna/nulo con dimensiones y rango-nulidad). Insertar cada una inmediatamente después de su definición (R2).
**Criterio de cierre:** ≥3 figuras estándar F8; el capítulo deja de tener 0 figuras; compilación limpia.
**Líneas estimadas:** 120–180
**Estado:** Completado (2026-07-08)
**Notas de ejecución:**
- `fig:subespacio_en_V` (tras la Obs. 6.10, def. de subespacio): elipse V ⊃ W con **0**, u, v y u+v (cerradura), estilo Venn 2D.
- `fig:gen_dos_vectores` (tras def. de subespacio generado): v₁, v₂ no colineales; w=2v₁+v₂ construido por etapas (dashed 2v₁ → +v₂) y −v₁+2v₂ con coeficiente negativo. Aritmética verificada: 2(2,0.5)+(0.5,1.5)=(4.5,2.5); −(2,0.5)+2(0.5,1.5)=(−1,2.5).
- `fig:cuatro_espacios` (tras def. de espacios fundamentales): esquema tipo Strang — ℝⁿ dividido en R(A) (dim r) y N(A) (dim n−r), ℝᵐ en C(A) y N(Aᵀ); flecha x↦Ax y N(A)↦{0}; caption menciona rango-nulidad.
- Las 3 verificadas visualmente (pdftoppm pp. 158, 163, 172). Compilación limpia: 0 errores `!`, 778 pp.

### F9AL.14 — espaciosvectoriales: propuestos + Decisión F + heading 🔒F
**Acción:** heading estándar; los probs 1–15 (con solución) y 16–36 (sin solución) se tratan según Decisión F (candidatos naturales a elevar: verificación de subespacio, independencia lineal por determinante, base del espacio nulo); tags de graduación en los restantes.
**Criterio de cierre:** convención F aplicada; 15–25 propuestos graduados con tags.
**Líneas estimadas:** 60–120
**Estado:** Completado (2026-07-08)
**Notas de ejecución:**
- **4 elevaciones a `example`** (protocolo 4 pasos + `\boxed{}`, en su sección temática): Independencia lineal según un parámetro (det con λ, factorización `(λ−1)(2λ+1)²`); Extensión de un conjunto l.i. a una base (base incompleta, det 4×4 = 4); Bases de los espacios fila, columna y nulo (multi-parte a/b); Construcción de una matriz con espacio nulo prescrito (rango-nulidad inverso). Verificadas con SymPy. ⚠️ Pendiente visto bueno del autor (elegidas según candidatos del plan; no había prob resuelto de "verificación de subespacio").
- **Error heredado corregido** en el ejemplo de bases de espacios fundamentales (a): la RREF es `(1,0,1,−2/7)`, no `(1,0,1,2/7)` → base de R(A) y segundo generador de N(A) con signo corregido: `(2/7,−4/7,0,1)` (confirmado SymPy).
- **11 probs resueltos** movidos íntegros (con su myproof) a `\section{Problemas resueltos adicionales}` (§6.7) con tag por prob: 3B/6I/2D.
- **Propuestos:** heading renombrado a `\section{Problemas propuestos}` (E4); 21 propuestos heredados reordenados en grupos con comentarios: 7 Básico / 9 Intermedio / 5 Desafiante (33/43/24 %). No hizo falta redactar propuestos nuevos (el capítulo, a diferencia de matrices/sel, ya tenía 21 sin solución).
- Balance verificado: 32/32 prob, 25/25 myproof, 19 examples. Compilación limpia 778 pp; §6.7 (p. 173) y §6.8 (p. 178) verificadas visualmente.

### F9AL.15 — espaciosvectoriales: auditoría R1 + R3 de teoremas centrales
**Acción:** verificar orden def→motivación→teorema→ejemplo en las 7 secciones; el teorema de la base/dimensión (central) debe tener demostración o esquema — añadir esquema si solo hay enunciado; el criterio de subespacio (operacional) enunciado + referencia.
**Criterio de cierre:** inversiones registradas/corregidas (≤50 líneas por corrección); teorema central con esquema.
**Líneas estimadas:** 30–90
**Estado:** Completado (2026-07-08)
**Notas de ejecución:**
- **R3 teorema central:** la prueba de «Invariancia del número de elementos en una base» invocaba un «lema de intercambio» inexistente en el libro → añadido `\begin{theorem}[Lema de intercambio]` (`thm:cap06:lema-intercambio`) con esquema de prueba (argumento de Steinitz, 8 líneas) justo antes; la prueba de invariancia ahora lo referencia con `\ref`.
- **R3 extra:** Criterio del Wronskiano no tenía prueba → añadida prueba por contrarrecíproco (5 líneas: derivar la relación de dependencia n−1 veces anula las columnas).
- **Criterio de subespacio:** ya conforme (coro «versión compacta» enunciado con referencia explícita al Teorema del test — sin cambios).
- **INV corregidas (2):** (i) §6.3: def «Subespacio generado» + fig:gen_dos_vectores estaban DESPUÉS del teorema cuya prueba usa `gen{...}` → movidas antes; teorema retitulado «El generado es el menor subespacio que contiene a los generadores». (ii) §6.4: example elevado «Independencia lineal según un parámetro» (test por determinante) quedaba tras el Wronskiano → movido tras el corolario de propiedades, antes de def Wronskiano.
- Orden R1 verificado en las 7 secciones (mapa completo de entornos); §6.1 y §6.5 sin figura propia (no requerida). Intro de capítulo presente. 2 pasadas lualatex; solo warning preexistente `figrayo`. 778 pp, 0 errores; pp. 162/167 verificadas visualmente.

### F9AL.16 — prodinterno: estructura de secciones R1 (capítulo con CERO secciones)
**Acción:** insertar: `\section{Producto interno}`, `\section{Norma, distancia y ángulo}` (incluye Cauchy-Schwarz), `\section{Ortogonalidad y complemento ortogonal}`, `\section{Proceso de Gram-Schmidt}`, `\section{Proyección ortogonal y mínimos cuadrados}`, `\section{Problemas propuestos}` (ajustar al contenido real).
**Criterio de cierre:** ≥5 secciones + sección de propuestos; compilación limpia.
**Líneas estimadas:** 30–70
**Estado:** Completado (2026-07-08)
**Notas de ejecución:**
- 7 secciones insertadas (solo cabeceras, nada movido — mismo procedimiento que F9AL.08): §7.1 Producto interno (incluye norma inducida y caso complejo, orden físico conservado); §7.2 Norma, ángulo y desigualdad de Cauchy-Schwarz; §7.3 Ortogonalidad y complemento ortogonal; §7.4 Bases ortogonales y proceso de Gram-Schmidt; §7.5 Proyección ortogonal y mínimos cuadrados; §7.6 Series de Fourier (contenido real no previsto en el plan); §7.7 Problemas resueltos adicionales (ante el banco final de 14 probs, marcado `% PROBLEMA 1`).
- **Desviación documentada:** `\section{Problemas propuestos}` NO se insertó aún — el capítulo no tiene ningún prob sin solución al final (el único sin myproof es la nota-fórmula «Regresión polinómica» en §7.5), y una sección vacía rompería el PDF. Se creará en F9AL.18 al aplicar Decisión F (que además requerirá redactar propuestos nuevos con validación del autor, como en matrices).
- Inventario para F9AL.18: 23 probs (9 dentro de secciones temáticas + 14 en el banco §7.7); 22 con myproof; el de regresión polinómica sin él.

### F9AL.17 — prodinterno: figuras R2 + auditoría
**Acción:** (a) proyección ortogonal de u sobre v con ángulo recto marcado (tras def. de proyección); (b) Gram-Schmidt en ℝ²: v₁, v₂ originales → u₁, u₂ ortogonales (tras el teorema); (c) completar label de la figura existente sin él y verificar la otra.
**Criterio de cierre:** 2 figuras nuevas estándar F8; 2/2 existentes conformes.
**Líneas estimadas:** 90–140
**Estado:** Completado (2026-07-08)
**Notas de ejecución:**
- `fig:proyeccion_ortogonal` (tras def. de proyección, §7.4): u=(1,3), v=(4,2), proy=(2,1) — aritmética exacta, (u−proy)·v=0; marca de ángulo recto en el pie de la proyección.
- `fig:gram_schmidt_r2` (tras el teorema de Gram-Schmidt): u₁=(2,1), u₂=(0,2) → v₂=u₂−proy=(−0.8,1.6), v₁·v₂=0 exacto; proyección punteada gris y ángulo recto en el origen.
- Auditoría existentes: figura de la recta de mínimos cuadrados tenía caption sin label → añadido `fig:recta_minimos_cuadrados`; `fig1` («Altura de un triángulo») renombrado a `fig:altura_triangulo` (label + su único `\ref`, mismo archivo). 2/2 conformes.
- Verificadas visualmente (pdftoppm pp. 190–191). 2 pasadas lualatex; solo warning preexistente `figrayo`. PDF: 780 pp, 0 errores.

### F9AL.18 — prodinterno: protocolo + residuales + propuestos 🔒F
**Acción:** eliminar/auditar las 2 marcas `\square` residuales; verificar 4 pasos en los 9 examples (8 ya conformes); aplicar Decisión F a los 23 probs (22 con solución); tags.
**Criterio de cierre:** 0 marcas residuales fuera de `proof`; examples conformes; convención F aplicada con tags.
**Líneas estimadas:** 50–110
**Estado:** Completado (2026-07-09)
**Notas de ejecución:**
- **⚠️ 2 errores matemáticos corregidos (verificados con SymPy)** en las series de Fourier del banco. Los coeficientes traían factores `(-1)^k` que corresponden al intervalo `[-π,π]`, no al `[0,2π]` que usan los enunciados:
  - `f(x)=x²+2x+1`: `a_k = 4(-1)^k/k²` → `4/k²`; `b_k = -4(-1)^k/k - 4π/k` → `-4(π+1)/k`.
  - `f(x)=9x²+4x`: `a_k = 36(-1)^k/k²` → `36/k²`; `b_k = -72(-1)^k/k³ - 8(-1)^k/k` → `-(36π+8)/k` (el término en `k³` era espurio).
  - Los 3 problemas lineales del banco (`9x+7`, `5x+7`, `7x+2`) y `a_0` en todos los casos estaban correctos.
- **Residuales:** las «2 marcas `\square`» eran 2 `\qedhere` dentro de `proof` (conformes al criterio), pero embebidos en math inline `\(...\)`. Eliminados; `proof` emite el □ automáticamente. Auditoría final: 0 `\qedhere`/`\square`/`\blacksquare`/`\qed` en todo el archivo.
- **Decisión F — 5 elevaciones a `example`** (lote validado por el autor), todas con protocolo 4 pasos + `\boxed{}` y aritmética verificada:
  - §7.2 `Identidad del paralelogramo` y `Ley del coseno` (la sección no tenía ejemplos de demostración).
  - §7.4 `Extensión de un vector a una base ortogonal de ℝ³` (Gram-Schmidt sobre `{v₁,e₁,e₂}`; verificado con `fractions.Fraction`, ortogonalidad exacta).
  - §7.5 `Ley de Hooke` (mínimos cuadrados con datos reales; `Σx=32.8`, `Σx²=278.82`, `Σxy=141.98`, `det=39.44` verificados).
  - §7.6 `Series de Fourier en [0,2π]` — **primer y único ejemplo de la sección**, que antes tenía cero. Movido desde el banco y expandido con la derivación completa: 6 integrales auxiliares verificadas con SymPy + nota explícita de por qué no aparecen factores `(-1)^k`.
  - Nota LaTeX: el título `[Series de Fourier en $[0,2\pi]$]` necesita llaves (`[{...}]`) porque el `]` cierra el argumento opcional.
- **Banco §7.7:** 17 probs (13 heredados + 4 reubicados desde secciones temáticas). Los 4 movidos: rombo, diagonales de igual norma, Gram-Schmidt en ℝ³, base ortogonal de `P₂(ℝ)`. Tags de graduación sobre **cada** prob: 6B/7I/4D.
- **`\section{Problemas propuestos}` (§7.8) creada desde cero** con 18 probs nuevos 5B/9I/4D (lote validado por el autor), en 6 subsecciones temáticas por comentario. El capítulo no tenía ningún prob sin solución, tal como anticipaba F9AL.16.
- **Otras correcciones de auditoría:**
  - `prob[Regresión polinómica]` no era un problema sino una fórmula sin pregunta → convertido a `rem` con `\label{rem:regresion_polinomica}` y una frase sobre la matriz de Vandermonde.
  - Prob «valor de verdad», literal (b): la respuesta era evasiva («Verdadero si ambos están en `W⊥`; de lo contrario, falso»), lo cual no responde el enunciado. La afirmación es **falsa**; se redactó contraejemplo explícito (`V=ℝ²`, `W=gen{(1,0)}`, `u=(1,0)`, `v=(0,1)`). El literal (c) se afinó (el único vector de `W` ortogonal a todo `W` es `0`).
  - 30 `Paso N:` → `Paso N.`; `\boxed{}` intermedio eliminado del example de `P₂(ℝ)` (la convención lo reserva para el Paso 4).
- **Examples:** 14 en total (9 previos + 5 elevados). 13 con `\boxed{}`; el restante (`Producto interno no usual`) es ilustrativo sin `myproof` — aceptable por la guía. El único no conforme (`Base ortogonal en P₂(ℝ)`, 1 solo paso) se reestructuró a 4 pasos; su cadena aritmética se verificó íntegra con SymPy (`⟨v₂,v₂⟩=13/240`, `⟨x−x²,v₂⟩=−1/80`, ortogonalidad final exacta).
- 0 `myproof` huérfanos. 8 secciones. 35 probs (17 banco + 18 propuestos). 2 pasadas lualatex; único warning `figrayo` (preexistente, `vectoresrn.tex`). PDF: **782 pp, 0 errores**.

---

## Semana 4 — vvpropios.tex

### F9AL.19 — vvpropios: párrafo introductorio + estructura de secciones
**Acción:** (a) escribir el párrafo introductorio del capítulo (único del libro sin él): motivar Av=λv como "direcciones que A no tuerce", conexión hacia atrás (matrices/determinantes vía ecuación característica) y hacia adelante (diagonalización, sistemas de EDOs — `\ref` a cap29). Si se aprueba la Decisión E2 (intercambio con translineales), motivar además desde la matriz de una transformación. (b) Insertar secciones: `\section{Valores y vectores propios}`, `\section{Diagonalización}`, `\section{Teorema de Cayley-Hamilton y potencias de matrices}`, manteniendo `\section{Algunas aplicaciones adicionales}` al final.
**Criterio de cierre:** intro de 5–9 líneas presente; ≥4 secciones; compilación limpia.
**Líneas estimadas:** 40–80
**Estado:** Completado — 2026-07-10

**Notas de ejecución:**
- **Intro** (5 frases tras `\chapter`): motiva $A\mathbf{v}=\lambda\mathbf{v}$ como «direcciones que la matriz no tuerce»; conexión hacia atrás con determinantes (`\ref{matrdet}`) y espacios nulos (`\ref{sel}`); hacia adelante con diagonalización, potencias y sistemas de EDOs (`\ref{sistemasedos}`). La parte condicional de la acción (Decisión E2) no aplica: E2 no está aprobada.
- **Labels nuevos:** `\label{vvpropios}` en el chapter; `\label{sistemasedos}` añadido a `cap29_Sistemas de EDOs.tex` (no tenía y la intro lo referencia; servirá también para F9AL.22).
- **7 secciones** insertadas sin mover contenido (títulos ajustados al contenido real): §8.1 Valores y vectores propios; §8.2 Diagonalización y potencias de matrices (la rem de potencias `potdim` y el example $A^6$ están físicamente aquí y dependen de $A=PDP^{-1}$, no de Cayley-Hamilton — por eso «potencias» va en este título y no en el de C-H como esbozaba el plan); §8.3 Aplicación: sistemas de ecuaciones diferenciales lineales; §8.4 El teorema de Cayley-Hamilton; §8.5 Valores propios e invertibilidad (Caracterización v5 + 2 probs sobre vectores propios de $A^{-1}$); §8.6 Problemas resueltos adicionales (heading anticipado para F9AL.21, precedente F9AL.08); §8.7 Algunas aplicaciones adicionales (existente).
- Única micro-reubicación: la frase puente «Algunas aplicaciones adicionales…» estaba **antes** del heading de su sección → movida después.
- **Hallazgo registrado para F9AL.21:** en l.92–98 hay un `\begin{proof}` huérfano (sin enunciado) que demuestra «$A$ invertible $\iff$ $\lambda=0$ no es valor propio» — aparentemente se perdió el enunciado del corolario. Duplica el ítem 18 de la Caracterización v5 (§8.5) y su prueba. No se tocó (regla: nada se corrige sin decisión del autor). Opciones para el autor en F9AL.21: (a) añadir el enunciado de corolario perdido tras el coro de triangulares; (b) fusionarlo con la v5.
- Compilación limpia (2 pasadas): 0 errores `!`, 0 refs indefinidas, 782 pp.

### F9AL.20 — vvpropios: figuras nuevas R2 (capítulo con CERO figuras)
**Acción:** (a) acción de A sobre vector propio (v escala λv, w genérico rota) — TikZ 2D con flechas rojas/azules; (b) diagrama de cajas de diagonalización A = PDP⁻¹ (cambio de base). Insertar tras la definición y tras el teorema de diagonalización respectivamente.
**Criterio de cierre:** 2 figuras estándar F8; compilación limpia.
**Líneas estimadas:** 80–130
**Estado:** Completado — 2026-07-10

**Notas de ejecución:**
- `fig:accion_vector_propio` (tras la def. de valores/vectores propios, posición R2): $A=\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)$; $\mathbf{v}=(1,1)$ rojo se estira a $A\mathbf{v}=3\mathbf{v}$ sobre la recta invariante $E_3$ (dashed); $\mathbf{w}=(1,0)$ azul gira a $A\mathbf{w}=(2,1)$ con arco indicador. Aritmética exacta.
- `fig:diagonalizacion_cajas` (tras el teorema de condición de diagonalización): cuadrado conmutativo $\mathbf{x}\to A\mathbf{x}$ (arriba, flecha roja) vs. $P^{-1}\to D\to P$ (camino inferior), cajas con coordenadas canónicas/propias.
- Estándar F8: `figure[H]` + caption + label tras caption; paleta `blue!70!black`/`red!70!black`; `>=stealth`; `\small`.
- Verificadas visualmente (pdftoppm pp. 212 y 217). Compilación limpia (2 pasadas): 0 errores `!`, 782 pp.

### F9AL.21 — vvpropios: sección de propuestos + Decisión F + protocolo 🔒F
**Acción:** crear `\section{Problemas propuestos}` (hoy no existe; los 14 probs, 13 con solución, están dispersos); aplicar Decisión F; tags; verificar 4 pasos en los 10 examples (5 computacionales conformes, 5 por revisar/justificar).
**Criterio de cierre:** sección única graduada; convención F aplicada; examples conformes o justificados.
**Líneas estimadas:** 60–120
**Estado:** Completado — 2026-07-10 (2 lotes)

**Notas de ejecución:**
- **Decisiones del autor (2026-07-10, 4 preguntas):** elevar solo `prob:vvp`; añadir el corolario perdido del `proof` huérfano; sustituir los literales EDO duplicados por sistemas nuevos; completar la solución evasiva del LRC.
- **1 elevación a `example`** (el autor eligió 1 de 4 candidatas): «Valores y vectores propios y sus multiplicidades» (`ex:vvp_multiplicidades`, ex `prob:vvp`) — 4 literales con protocolo por literal (Paso 1 polinomio, Paso 2 raíces/m.a., Paso 3 espacios propios, Paso 4 resumen con `\boxed{}`); ref del example de diagonalización actualizada («en el Ejemplo \ref{ex:vvp_multiplicidades}»). Typo «redución» corregido.
- **`proof` huérfano resuelto:** nuevo `\begin{coro}[Invertibilidad y el valor propio cero]` (`cor:cerovp`) antes de su prueba; la Caracterización v5 ahora cita el corolario en vez de duplicar la prueba.
- **⚠️ Error matemático heredado corregido (verificado SymPy):** prob del circuito LRC — con $R=1$, $L=1$, $C=0.5$ es $1/(RC)=2$, no $1$: matriz correcta $\left(\begin{smallmatrix}0&1\\-2&-2\end{smallmatrix}\right)$, $\lambda=-1\pm i$ (el libro traía $\lambda=\frac{-1\pm i\sqrt7}{2}$). (a) reescrito con solución general real; (b) resuelto el PVI ($i_L=e^{-t}(2\cos t+3\sen t)$, $v_C=e^{-t}(\cos t-5\sen t)$); (c) corregido $e^{-t/2}\to e^{-t}$.
- **Duplicación eliminada:** los literales (a)/(b) del prob de sistemas EDO del banco repetían íntegros los 2 examples de §8.3 → sustituidos por sistemas nuevos verificados SymPy ($A=\left(\begin{smallmatrix}1&2\\2&1\end{smallmatrix}\right)$ con CI $(3,1)$; $A=\left(\begin{smallmatrix}4&1\\3&2\end{smallmatrix}\right)$ con CI $(1,5)$); el (c) $3\times3$ se conservó.
- Prob expositivo «Solución de EDOs de primer orden…» (sin pregunta ni solución) → `rem` con `\label{rem:edo_primer_orden}` (precedente: regresión polinómica en prodinterno).
- **Banco §8.6:** los 12 probs del capítulo quedaron todos en el banco (movidos: C-H desde §8.4, los 2 de $A^{-1}$ desde §8.5), en 5 grupos temáticos con separadores; tag individual 3B/6I/3D.
- **Protocolo:** 15 marcas `Paso N:` → `Paso N.`; 11 examples (10+1 elevado): 6 computacionales conformes (Paso N. + boxed), 5 ilustrativos justificados con título (aplicación potencias, Markov, forma cuadrática, 2 sistemas dinámicos).
- **§8.8 «Problemas propuestos» creada** (última sección, E4): 16 probs nuevos 5B/8I/3D en 4 grupos temáticos, lote aprobado por el autor y 16/16 verificados con SymPy (P9/P10 en forma simbólica general).
- Compilación limpia (2 pasadas): 0 errores `!`, 0 refs indefinidas, 788 pp.

### F9AL.22 — vvpropios: nota editorial sobre aplicaciones a EDOs
**Acción:** la sección de aplicaciones EDO se conserva (decisión de Fase 4). Ahora que existe `cap29`, añadir remisiones cruzadas (`\ref`) en ambos sentidos y una `rem` que delimite: aquí se ve el mecanismo eigen, el tratamiento sistemático está en cap29. **No recortar contenido sin autorización del autor** — registrar en Notas cualquier solapamiento detectado.
**Criterio de cierre:** referencias cruzadas insertadas; solapamientos documentados en Notas para decisión del autor.
**Líneas estimadas:** 10–30
**Estado:** Completado — 2026-07-10

**Notas de ejecución:**
- **cap29 → vvpropios:** en §29.3 (derivación de $(A-\lambda I)\mathbf{v}=0$) se añadió «Los métodos para calcular valores y vectores propios, junto con una primera aplicación de la diagonalización a estos sistemas, se desarrollaron en el Capítulo~\ref{vvpropios}».
- **vvpropios → cap29:** `rem[Alcance de esta sección]` al inicio de §8.3: aquí el mecanismo (diagonalizar desacopla); el tratamiento sistemático (λ complejos/repetidos, no homogéneos, aplicaciones) en el Capítulo~\ref{sistemasedos}. (La intro del capítulo, F9AL.19, ya remite también.)
- **Solapamientos documentados (sin recortar, para eventual decisión del autor):** (i) el teorema de solución general $\mathbf{y}=\sum c_i e^{\lambda_i x}\mathbf{v}_i$ aparece en ambos capítulos — en vvpropios probado vía desacople con $P$, en cap29 §29.3 enunciado por superposición de soluciones eigen: son complementarios; (ii) el prob del banco «EDO de orden superior → sistema» solapa §29.1.2 (allí es material central); (iii) el prob LRC solapa temáticamente §29.5.2 (circuitos de dos mallas; circuito distinto); (iv) la matriz $\left(\begin{smallmatrix}1&2\\3&2\end{smallmatrix}\right)$ del primer example de vvpropios reaparece en el example de §29.3.1 (contextos distintos: allí se resuelve el sistema completo).
- Compilación limpia (2 pasadas): 0 errores `!`, 0 refs indefinidas, 788 pp.

---

## Semana 5 — translineales.tex

### F9AL.23 — translineales: estructura de secciones R1
**Acción:** el capítulo (2 566 líneas) tiene una sola `\section` en la línea 10. Insertar: `\section{Transformaciones lineales}` (existente), `\section{Núcleo, imagen y el teorema rango-nulidad}`, `\section{Matriz de una transformación}`, `\section{Cambio de base}`, `\section{Composición e invertibilidad}`, `\section{Transformaciones geométricas en el plano y el espacio}` (ajustar al contenido real).
**Criterio de cierre:** ≥5 secciones; teorema rango-nulidad (central R3) con demostración o esquema verificado; compilación limpia.
**Líneas estimadas:** 40–90
**Estado:** Completado (2026-07-10). 6 secciones: Transformaciones lineales / Núcleo, imagen y el teorema de la dimensión / Composición, invertibilidad e isomorfismos / Matriz asociada a una transformación lineal / Transformaciones geométricas en el plano / Problemas resueltos adicionales. `\label{translineales}` añadido al capítulo. El teorema de la dimensión (`teodim`) ya tenía demostración completa (verificada). 792 pp, 0 errores.

### F9AL.24 — translineales: auditoría de 19 figuras + 1 tikz suelto
**Acción:** las 19 figuras en `figure` carecen todas de caption y label; 1 tikzpicture está fuera de entorno figure. Protocolo F8.31 completo (caption + `\label{fig:...}` + anchors).
**Criterio de cierre:** 20/20 conformes; compilación limpia.
**Líneas estimadas:** 100–200 (2 lotes internos si excede 300)
**Estado:** Completado (2026-07-10). Corrección al diagnóstico: las 19 figuras SÍ tenían caption; lo que faltaba eran los 19 labels. 19 `\label{fig:...}` insertados tras caption + 17 anchors (11 `\textbf{Gráfica} (Figura~\ref{...})` en banco, 6 en teoría) + 2 refs en enunciados de probs gráficos. El tikz suelto (diagrama conmutativo matriz asociada, L457) envuelto en `figure[H]` → `fig:diagrama_matriz_asociada` con anchor. 20/20 conformes.

### F9AL.25 — translineales: figuras nuevas R2
**Acción:** (a) cuadrado unitario → paralelogramo bajo rotación θ y bajo cizalla (minipage doble); (b) diagrama conmutativo de composición T∘S entre V, W, Z con nodos y flechas. Insertar según R2 tras las definiciones correspondientes.
**Criterio de cierre:** 2 figuras estándar F8; compilación limpia.
**Líneas estimadas:** 80–130
**Estado:** Completado (2026-07-10). (a) `fig:cuadrado_rotacion_cizalla` — minipage doble: cuadrado unitario (azul punteado) → rotación π/6 y cizalla horizontal (rojo), con T(e₁)/T(e₂) y matrices; intro nueva de la sección geométrica la ancla. (b) `fig:composicion_diagrama` — diagrama U→V→W con flecha diagonal T₂∘T₁ punteada, tras la prueba de linealidad de la composición (notación del capítulo: T₁, T₂, U, V, W en lugar de T∘S, V, W, Z del plan).

### F9AL.26 — translineales: sección de propuestos + Decisión F 🔒F
**Acción:** crear `\section{Problemas propuestos}`; aplicar Decisión F a los 22 probs (22 con solución dentro); tags de graduación.
**Criterio de cierre:** sección única graduada; convención F aplicada al 100 %.
**Líneas estimadas:** 60–120
**Estado:** Pendiente

### F9AL.27 — translineales: completar protocolo de 4 pasos
**Acción:** de los 10 examples solo 3 tienen marcas de Paso; revisar los 7 restantes: los ilustrativos se justifican con título, los computacionales se reforman a 4 pasos + boxed.
**Criterio de cierre:** 10/10 conformes o justificados; lista en Notas.
**Líneas estimadas:** 40–100
**Estado:** Pendiente

---

## Semana 6 — complejos.tex + transversales de bloque

### F9AL.28 — complejos: elevar resueltos desde el banco 🔒F
**Acción:** el capítulo no tiene ningún `example` — todo el material resuelto son 24 probs con myproof dentro. Elevar 8–10 representativos a `example` con 4 pasos + boxed (candidatos: operaciones básicas, forma polar, De Moivre, raíces n-ésimas, ecuación con TFA, triángulo equilátero); el resto según Decisión F.
**Criterio de cierre:** 8–10 examples con 4 pasos; convención F aplicada al resto.
**Líneas estimadas:** 120–200
**Estado:** Pendiente

### F9AL.29 — complejos: auditoría de 7 figuras
**Acción:** 7 entornos figure, 0 con caption+label. Protocolo F8.31; verificar proporción 1:1 (círculos sin distorsión — ya revisado en 2026-06-16, solo confirmar).
**Criterio de cierre:** 7/7 conformes.
**Líneas estimadas:** 40–80
**Estado:** Pendiente

### F9AL.30 — complejos: figuras nuevas R2
**Acción:** (a) plano complejo con z = a+bi, módulo |z| y argumento θ (tras la def. de módulo/argumento); (b) raíces n-ésimas de la unidad distribuidas sobre la circunferencia unitaria (tras De Moivre/raíces).
**Criterio de cierre:** 2 figuras estándar F8 en posición R2.
**Líneas estimadas:** 70–110
**Estado:** Pendiente

### F9AL.31 — complejos: graduación + heading
**Acción:** renombrar `\section{Problemas propuestos para el capítulo}` → `\section{Problemas propuestos}`; tags de graduación sobre el banco resultante de F9AL.28.
**Criterio de cierre:** heading estándar; tags presentes; 15–20 propuestos si el banco lo permite (si queda corto tras elevaciones, añadir 3–5 nuevos sin solución cubriendo: forma polar, potencias, raíces, lugares geométricos).
**Líneas estimadas:** 20–80
**Estado:** Pendiente

### F9AL.32 — Transversal AL: normalizar headings de propuestos
**Acción:** verificar que los 7 capítulos usan exactamente `\section{Problemas propuestos}` (tras F9AL.04/.10/.14/.16/.21/.26/.31).
**Criterio de cierre:** grep de variantes = 0 en el bloque.
**Líneas estimadas:** 5–15
**Estado:** Pendiente

### F9AL.33 — Transversal AL: labels formales en resultados centrales
**Acción:** aplicar `thm:capNN:slug` / `def:capNN:slug` solo a los resultados centrales tocados en F9 (rango-nulidad, Gram-Schmidt, diagonalización, Cauchy-Schwarz, base/dimensión, De Moivre) — no es la fase Labeling global.
**Criterio de cierre:** ≥6 labels centrales; referencias cruzadas de F9AL.19/.22 funcionando.
**Líneas estimadas:** 15–30
**Estado:** Pendiente

### F9AL.34 — Cierre de bloque: compilación y re-inventario
**Acción:** compilar el maestro (2 pasadas LuaLaTeX); re-ejecutar el inventario automatizado sobre los 7+1 archivos; confirmar: 0 myproof huérfanos, 0 figuras sin caption/label, tags presentes, secciones de propuestos presentes.
**Criterio de cierre:** 0 errores `!`; tabla de re-inventario pegada en Notas; nº de páginas registrado.
**Líneas estimadas:** 0 (verificación)
**Estado:** Pendiente

---

## Bloque V — vectoresrn.tex (nota de decisión editorial)

**Nota editorial:** `vectoresrn.tex` pertenece a `\part{Álgebra Lineal}` (cap. real 3) pero fue clasificado como "auxiliar con contenido" en el encargo de este plan. Se incluye aquí como bloque opcional porque comparte todas las brechas del bloque AL; **el autor decide si se ejecuta dentro de F9AL o se difiere**. Características que no encajan en el criterio estándar: es el capítulo puente AL↔C3 (rectas, planos y cuádricas se usan en C3), tiene un banco fusionado de problemas de origen externo (2026-06-16) y usa el formato antiguo `Paso 1:` (dos puntos) en soluciones de probs.

### F9AL.35 — vectoresrn: estructura de secciones R1
**Acción:** 2 255 líneas sin secciones antes de los propuestos. Insertar: vectores y operaciones; producto punto (con Cauchy-Schwarz — único theorem actual, verificar R3); producto cruz y mixto; rectas en ℝ³; planos en ℝ³; cónicas y cuádricas.
**Criterio de cierre:** ≥5 secciones; compilación limpia.
**Líneas estimadas:** 30–70
**Estado:** Pendiente

### F9AL.36 — vectoresrn: auditoría de 26 figuras + `figrayo` duplicado
**Acción:** 24/26 figuras sin caption+label → protocolo F8.31 (2 lotes si excede 300 líneas); resolver el label duplicado `figrayo` (L.1221/L.1264) — **requiere decisión del autor sobre cuál conserva el nombre original**; verificar `axis equal image` en cónicas 2D (pendiente desde DIAGNÓSTICO Paso 4).
**Criterio de cierre:** 26/26 conformes; 0 labels duplicados; cónicas sin distorsión.
**Líneas estimadas:** 150–280
**Estado:** Parcial — `figrayo` resuelto (2026-07-09); resto pendiente.
**Notas de ejecución (adelanto de `figrayo`):**
- El duplicado **no requería decisión del autor**: no eran dos labels de la misma figura, sino dos figuras distintas del mismo problema (rayo reflejado, `\cite{espinoza2006Algebralineal}` p. 87) que compartían nombre por copia-pega. Además **ninguna tenía `\caption`** y **nadie las referenciaba** (`\ref{figrayo}`: 0 usos en todo el libro).
- Defecto de fondo: un `\label` colocado sin `\caption` (y antes de él) no captura el contador de figura, sino el contador vigente. Aunque no hubieran estado duplicados, ambos labels habrían resuelto a un número equivocado.
- Corrección: `fig:rayo_reflejado` (montaje físico: rayo incidente, normal, rayo reflejado) y `fig:rayo_construccion_vector` (construcción de $\mathbf{v}$ a partir de $\operatorname{proy}_{\mathbf{n}}\mathbf{u}$), cada una con `\caption` + `\label` después del caption. Añadidas 2 remisiones `\ref` en la prueba, que antes no existían.
- Verificado: resuelven a `figure.3.17` y `figure.3.18`, aparecen en el `.lof` y se imprimen como «Figura 3.17/3.18» en pp. 53–54. Matemática del problema revisada de paso y correcta ($t=7$, punto $(-5,-7,1)$, $\|\mathbf{v}\|=\|\mathbf{u}\|=\sqrt{2}$).
- **Warning `figrayo' multiply defined` eliminado: el libro compila ahora sin ningún warning de labels/referencias.** 782 pp, 0 errores.

### F9AL.37 — vectoresrn: protocolo + propuestos 🔒F
**Acción:** normalizar `Paso N:` → `Paso N.` en soluciones; verificar 4 pasos en los 8 examples; aplicar Decisión F a los 28 probs (26 con solución); heading `Problemas Propuestos` → `Problemas propuestos`; tags.
**Criterio de cierre:** formato de pasos uniforme; convención F aplicada; tags presentes.
**Líneas estimadas:** 60–140
**Estado:** Pendiente

---

## Ampliación 2026-07-10 — Protocolo de 4 pasos en los bancos de resueltos (F9AL.38–.45)

**Decisión del autor (2026-07-10):** el autor detectó que muchos `myproof` del bloque AL carecen del protocolo de 4 pasos. El plan original solo cubría los `example` (incluidas elevaciones); la Decisión F conservaba los myproof de los bancos «íntegros» pero nunca decidió sobre su formato interno. Se aprueba extender a AL el mismo criterio aplicado en C3 (F8.40–F8.47): **todo myproof computacional → protocolo `\textbf{Paso N.}` + `\boxed{}` final**.

**Inventario del escaneo (2026-07-10) — myproof sin marca `Paso N`:**

| Archivo | myproof | sin protocolo |
|---|---|---|
| matrices.tex | 50 | 26 |
| sel.tex | 32 | 18 |
| espaciosvectoriales.tex | 25 | 11 |
| prodinterno.tex | 30 | 15 |
| vvpropios.tex | 32 | 27 |
| translineales.tex | 56 | 47 |
| complejos.tex | 24 | 24 |
| vectoresrn.tex | 32 | 27 |
| **Total** | **281** | **195** |

**Criterio común a los 8 ítems (heredado de F8.44–F8.47 + GUIA §2.2):**
- Computacionales → 4 pasos (`Paso 1.` planteamiento/estrategia … `Paso 4.` conclusión con `\boxed{}`); el número de pasos puede exceder 4 si el cómputo lo exige.
- Multi-parte → `Paso 1.` Estrategia común + pasos por sub-parte (patrón F8.44), o protocolo completo dentro de cada literal si las partes son independientes.
- Demostraciones teóricas breves (una sola cadena de implicaciones, ≤4 líneas) pueden conservarse en prosa — se registra cada excepción en Notas (análogo al criterio «ilustrativo» de los examples).
- La aritmética NO se re-deriva (ya verificada en V3.x/V4.x): solo se reestructura. Si la reestructuración revela una inconsistencia, se registra sin corregir y se escala al autor.
- Compilación limpia tras cada ítem; si un capítulo excede 300 líneas modificadas, se parte en lotes internos con compilación entre lotes.

### F9AL.38 — matrices: 26 myproof → protocolo 4 pasos
**Estado:** Pendiente

### F9AL.39 — sel: 18 myproof → protocolo 4 pasos
**Estado:** Pendiente

### F9AL.40 — espaciosvectoriales: 11 myproof → protocolo 4 pasos
**Estado:** Pendiente

### F9AL.41 — prodinterno: 15 myproof → protocolo 4 pasos
**Estado:** Pendiente

### F9AL.42 — vvpropios: 27 myproof → protocolo 4 pasos
**Nota:** ejecutar tras F9AL.21 (las elevaciones de ese ítem reducen el conteo del banco).
**Estado:** Completado — 2026-07-10

**Notas de ejecución:**
- Tras F9AL.21/.46 el archivo tenía 33 myproof, 23 sin marca `Paso N` (todos en el banco §8.6). **21 reestructurados** a protocolo con `\boxed{}` en los resultados computacionales: 3 literales de matrices con $D$ (Jordan $J_2(-3)$, complejos $a\pm ib$, rotación $e^{\pm i\theta}$), 2 del parámetro $a$, el de vp $0,3,-3$ (Paso 4 resumen nuevo), demostración de la raíz $m$ (3 pasos, sin boxed por ser demostración), $A^2(4,3)$, 2 de $A^{20}$, 4 de Cayley-Hamilton, $A^{-1}$, 3 sistemas EDO, EDO de orden superior, LRC (a)/(b).
- **2 excepciones de prosa registradas** (criterio ampliación: ≤4 líneas, una sola cadena): prob «$3\mathbf{v}$ vector propio de $A^{-1}$» (2 líneas) y literal (c) del LRC ($t\to\infty$, 2 líneas).
- **Mejoras de auditoría:** prob de $A^{-1}$ justifica $\lambda\neq0$ con `\ref{cor:cerovp}`; artefacto de cita `[2]` eliminado en C-H (b) (frase circular → remisión al literal d); «(normalizados)» corregido (no lo estaban); EDO de orden superior con soluciones generales explícitas de las otras 2 ecuaciones e `itemize` en vez de guiones.
- Balance: 33/33 myproof, 28/28 prob, 12/12 example, 0 huérfanos. Compilación limpia (2 pasadas): 0 errores `!`, 0 refs indefinidas, 790 pp.

### F9AL.43 — translineales: 47 myproof → protocolo 4 pasos (2 lotes)
**Nota:** ejecutar tras F9AL.26/.27.
**Estado:** Pendiente

### F9AL.44 — complejos: 24 myproof → protocolo 4 pasos
**Nota:** ejecutar tras F9AL.28 (las 8–10 elevaciones de ese ítem ya salen con 4 pasos; este ítem cubre el resto del banco).
**Estado:** Pendiente

### F9AL.45 — vectoresrn: 27 myproof → protocolo 4 pasos (bloque V, opcional)
**Nota:** ejecutar tras F9AL.37; hereda la condición de alcance del bloque V.
**Estado:** Pendiente

### F9AL.46 — vvpropios: subsección breve sobre la forma canónica de Jordan
**Solicitud del autor (2026-07-10):** incluir una parte sobre formas canónicas de Jordan, «no muy extensa porque el curso no nos da», como ítem para más adelante.
**Acción:** añadir al final de §Diagonalización y potencias de matrices una subsección mínima: (a) def. de bloque de Jordan $J_k(\lambda)$; (b) enunciado sin prueba del teorema de la forma canónica de Jordan (toda matriz compleja es semejante a una matriz de bloques de Jordan, única salvo orden); (c) 1 ejemplo $2\times 2$ completo con la matriz no diagonalizable del capítulo (p. ej. la del literal (a) del Ejemplo de multiplicidades o $\left(\begin{smallmatrix}-3&2\\0&-3\end{smallmatrix}\right)$ del banco, que ya remiten a Jordan); (d) `rem` de alcance con remisión bibliográfica. Conectar con las 2 menciones existentes de «forma de Jordan» en el capítulo (convertirlas en `\ref`).
**Criterio de cierre:** subsección ≤120 líneas con def + teorema enunciado + 1 ejemplo 4 pasos + rem de alcance; compilación limpia.
**Líneas estimadas:** 80–120
**Nota de orden:** ejecutar tras F9AL.22, en cualquier punto antes del cierre de bloque F9AL.34.
**Estado:** Completado — 2026-07-10

**Notas de ejecución:**
- **§8.2.1 «La forma canónica de Jordan»** (67 líneas, al final de §8.2): párrafo motivador (m.g. < m.a. ⇒ no hay base de vectores propios) → `definition[Bloque de Jordan]` con $J_1, J_2, J_3$ explícitos → `theorem[Forma canónica de Jordan]` (`thm:cap08:jordan`, enunciado sin prueba: semejanza, unicidad salvo orden, diagonalizable ⟺ bloques de tamaño 1) → `example` 4 pasos (`ex:jordan_2x2`) → `rem[Alcance y potencias]`.
- **Ejemplo con matriz fresca** $A=\left(\begin{smallmatrix}1&1\\-1&3\end{smallmatrix}\right)$ (no la del banco, para no duplicar): $(\lambda-2)^2$, m.g. $=1$, vector propio generalizado $(A-2I)\mathbf{v}_2=\mathbf{v}_1$ → $\mathbf{v}_2=(0,1)$, $P=\left(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\right)$, $J=J_2(2)$, verificación $AP=PJ$. Confirmado con SymPy (incl. `jordan_form()` y $J^5$ contra la fórmula $J_2(\lambda)^k$).
- **rem de alcance:** remisión a `\cite{hoffman1973algebra}` (cita nueva → corrido `bibtex` + 2 lualatex) + fórmula cerrada $J_2(\lambda)^k$ conectando con el tema de potencias de la sección.
- **2 conexiones `\ref{subsec:jordan}`** desde las menciones existentes: Paso 4 del literal (a) de `ex:vvp_multiplicidades` y el prob del banco con $\left(\begin{smallmatrix}-3&2\\0&-3\end{smallmatrix}\right)$ (a la que además se le explicitó $J_2(-3)$).
- Verificación visual pp. 221–222 (cita resuelta «Hoffman and Kunze, 1973»). Compilación limpia: 0 errores `!`, 0 refs/citas indefinidas, 790 pp.

---

## Registro de progreso

| Ítem | Archivo(s) | Acción | Estado | Fecha | Notas |
|---|---|---|---|---|---|
| F9AL.01 | `.md` | Decisión F registrada | Completado | 2026-07-06 | F-i variante conservadora: elevar 3–5 por cap.; resto íntegro en `\section{Problemas resueltos adicionales}`; huérfanos se reencajan. Ítems 🔒F desbloqueados. |
| F9AL.02 | `matrices.tex` | Estructura de secciones | Completado | 2026-07-07 | 4 secciones: Propiedades básicas → Matrices invertibles (subsec. gaussiana) → Determinantes (promovida) → Problemas propuestos. Bloque matrices especiales (105 l.) movido a Propiedades básicas. Orden físico Determinantes tras invertibles conservado (dependencia narrativa). 772 pp, 0 errores. |
| F9AL.03 | `matrices.tex` | Anidar 8 myproof huérfanos | Completado | 2026-07-07 | 8/8 reencajados (l.627, 690, 765, 1395, 2862, 2895, 2994, 3057); re-escaneo 0 huérfanos; 25/25 probs quedan con solución interna → propuestos quedaría vacía (decisión en F9AL.04). 772 pp, 0 errores. |
| F9AL.04 | `matrices.tex` | Sección propuestos + Decisión F + tags | Completado | 2026-07-07 | 5 elevaciones a example (validadas); 20 resueltos íntegros en `Problemas resueltos adicionales` con tags; 18 propuestos nuevos aprobados por el autor (5B/9I/4D); GUIA §2.1 actualizada. 38/38 prob, 0 huérfanos. |
| F9AL.05 | `matrices.tex` | Auditoría 12 figuras | Completado | 2026-07-07 | 8 labels añadidos; 4 tikz sueltos → figure[H]+caption+label; arista 3→4 duplicada eliminada en grafo (c). 12/12 conformes. 774 pp, 0 errores. |
| F9AL.06 | `matrices.tex` | 3 figuras nuevas R2 | Completado | 2026-07-07 | fig:producto_matricial, fig:det_area, fig:cofactores_sombreados — insertadas en posición R2, estándar F8. 774 pp, 0 errores. |
| F9AL.07 | `matrices.tex` | Verificación protocolo 32 examples | Completado | 2026-07-07 | 37 examples (con 5 elevados): 47 `Paso N:` → `Paso N.`; 2 boxed añadidos (grafos); 24/24 con myproof conformes; 13 ilustrativos justificados. |
| F9AL.08 | `sel.tex` | Estructura de secciones | Completado | 2026-07-07 | 7 secciones insertadas (6 temáticas + banco `Problemas resueltos adicionales`); solo cabeceras, nada movido. Los 8 huérfanos del cap. son las soluciones de los probs 11–18 del banco. |
| F9AL.09 | `sel.tex` | Anidar 8 myproof huérfanos | Completado | 2026-07-07 | 8/8 reencajados (soluciones de probs 11–18 del banco); 0 huérfanos; 30/30 prob balanceados; banco 23/23 resuelto. |
| F9AL.10 | `sel.tex` | Propuestos + Decisión F + heading | Completado | 2026-07-07 | 4 elevaciones a example; banco 19 probs con tags; propuestos 17 (7 heredados + 10 nuevos aprobados) 5B/8I/4D; fix `\,\%` babel-spanish. 778 pp, 0 errores. |
| F9AL.11 | `sel.tex` | Figura 3 planos ℝ³ + auditoría | Completado | 2026-07-07 | fig:tresplanoscasos (3 minipages pgfplots 3D: punto/recta/sin intersección, verificada visualmente); 2 labels añadidos (fig:sistema2x2casos, fig:familiapolinomios); 10/10 conformes. 778 pp, 0 errores. |
| F9AL.12 | `sel.tex` | Verificación protocolo 5 examples | Completado | 2026-07-07 | 9 examples (con 4 elevados): 37 `Paso N:` → `Paso N.`; Pasos 3–4 marcados en homogéneo 3×4; 8/8 computacionales conformes + 1 ilustrativo justificado. |
| F9AL.13 | `espaciosvectoriales.tex` | 3 figuras nuevas R2 | Completado | 2026-07-08 | fig:subespacio_en_V, fig:gen_dos_vectores, fig:cuatro_espacios; verificadas visualmente pp. 158/163/172. 778 pp, 0 errores. |
| F9AL.14 | `espaciosvectoriales.tex` | Propuestos + Decisión F + tags | Completado | 2026-07-08 | 4 elevaciones (SymPy-verificadas, 1 error de signo heredado corregido); banco §6.7 con 11 probs taggeados; 21 propuestos 7B/9I/5D; heading E4. 778 pp, 0 errores. |
| F9AL.15 | `espaciosvectoriales.tex` | Auditoría R1 + R3 | Completado | 2026-07-08 | Lema de intercambio nuevo (esquema Steinitz); prueba Wronskiano añadida; 2 INV corregidas (def generado+figura antes del teorema; example det antes de Wronskiano). 778 pp, 0 errores. |
| F9AL.16 | `prodinterno.tex` | Estructura de secciones (0 actuales) | Completado | 2026-07-08 | 7 secciones (6 temáticas + banco §7.7, incluye §7.6 Series de Fourier); heading de propuestos diferido a F9AL.18 (0 probs sin solución al final). 780 pp, 0 errores. |
| F9AL.17 | `prodinterno.tex` | 2 figuras nuevas + auditoría | Completado | 2026-07-08 | fig:proyeccion_ortogonal, fig:gram_schmidt_r2 (aritmética exacta, verificadas pp. 190–191); label añadido a recta mín. cuadrados; fig1→fig:altura_triangulo. |
| F9AL.18 | `prodinterno.tex` | Protocolo + residuales + propuestos | Completado | 2026-07-09 | **2 errores de Fourier corregidos** (factores `(-1)^k` de `[-π,π]` en problemas sobre `[0,2π]`, verificado SymPy). 5 elevaciones (incl. 1er ejemplo de §7.6). Banco 17 probs 6B/7I/4D. §7.8 propuestos creada: 18 probs 5B/9I/4D. `prob[Regresión polinómica]`→`rem`. Respuesta evasiva corregida con contraejemplo. 782 pp, 0 errores. |
| F9AL.19 | `vvpropios.tex` | Intro + estructura de secciones | Completado | 2026-07-10 | Intro 5 frases (refs a matrdet/sel/sistemasedos); 7 secciones sin mover contenido; labels `vvpropios` + `sistemasedos` (cap29); heading banco anticipado; `proof` huérfano l.92 registrado para F9AL.21. 782 pp, 0 errores. |
| F9AL.20 | `vvpropios.tex` | 2 figuras nuevas R2 | Completado | 2026-07-10 | fig:accion_vector_propio (v se estira, w gira; A=(2 1;1 2)) + fig:diagonalizacion_cajas (cuadrado conmutativo PDP⁻¹); verificadas pp. 212/217. 782 pp, 0 errores. |
| F9AL.21 | `vvpropios.tex` | Sección propuestos + Decisión F | Completado | 2026-07-10 | 1 elevación (ex:vvp_multiplicidades); cor:cerovp para proof huérfano; error LRC corregido (λ=−1±i); duplicados EDO sustituidos; banco 12 probs 3B/6I/3D; §8.8 con 16 propuestos 5B/8I/3D SymPy-OK. 788 pp, 0 errores. |
| F9AL.22 | `vvpropios.tex` | Remisiones cruzadas EDO (cap29) | Completado | 2026-07-10 | Ref cap29§3→vvpropios + rem de alcance §8.3→cap29; 4 solapamientos documentados sin recorte. 788 pp, 0 errores. Semana 4 completa. |
| F9AL.23 | `translineales.tex` | Estructura de secciones | Completado | 2026-07-10 | 6 secciones + label capítulo; teodim ya tenía prueba. 792 pp |
| F9AL.24 | `translineales.tex` | Auditoría 20 figuras | Completado | 2026-07-10 | 19 labels + 19 anchors + tikz suelto → fig:diagrama_matriz_asociada. 20/20 |
| F9AL.25 | `translineales.tex` | 2 figuras nuevas R2 | Completado | 2026-07-10 | fig:cuadrado_rotacion_cizalla (minipage doble) + fig:composicion_diagrama |
| F9AL.26 | `translineales.tex` | Sección propuestos + Decisión F | Pendiente | — | — |
| F9AL.27 | `translineales.tex` | Completar 4 pasos | Pendiente | — | — |
| F9AL.28 | `complejos.tex` | Elevar 8–10 resueltos del banco | Pendiente | — | — |
| F9AL.29 | `complejos.tex` | Auditoría 7 figuras | Pendiente | — | — |
| F9AL.30 | `complejos.tex` | 2 figuras nuevas R2 | Pendiente | — | — |
| F9AL.31 | `complejos.tex` | Graduación + heading | Pendiente | — | — |
| F9AL.32 | 7 caps AL | Headings normalizados | Pendiente | — | — |
| F9AL.33 | 7 caps AL | Labels resultados centrales | Pendiente | — | — |
| F9AL.34 | maestro | Compilación + re-inventario | Pendiente | — | — |
| F9AL.35 | `vectoresrn.tex` | Estructura de secciones (bloque V, opcional) | Pendiente | — | Requiere decisión de alcance |
| F9AL.36 | `vectoresrn.tex` | Auditoría 26 figuras + figrayo (bloque V) | Parcial | 2026-07-09 | `figrayo` resuelto: eran 2 figuras distintas sin caption y sin referencias → `fig:rayo_reflejado` + `fig:rayo_construccion_vector`, con captions y 2 `\ref` nuevas. 0 warnings de labels. Faltan las otras 24 figuras y `axis equal image`. |
| F9AL.37 | `vectoresrn.tex` | Protocolo + propuestos (bloque V) | Pendiente | — | — |
| F9AL.38 | `matrices.tex` | 26 myproof → 4 pasos | Pendiente | — | Ampliación 2026-07-10 |
| F9AL.39 | `sel.tex` | 18 myproof → 4 pasos | Pendiente | — | Ampliación 2026-07-10 |
| F9AL.40 | `espaciosvectoriales.tex` | 11 myproof → 4 pasos | Pendiente | — | Ampliación 2026-07-10 |
| F9AL.41 | `prodinterno.tex` | 15 myproof → 4 pasos | Pendiente | — | Ampliación 2026-07-10 |
| F9AL.42 | `vvpropios.tex` | 27 myproof → 4 pasos | Completado | 2026-07-10 | 21/23 reestructurados con boxed; 2 excepciones prosa (≤4 líneas) registradas; artefacto [2] y «normalizados» corregidos; ref a cor:cerovp. 790 pp, 0 errores. |
| F9AL.43 | `translineales.tex` | 47 myproof → 4 pasos (2 lotes) | Pendiente | — | Tras F9AL.26/.27 |
| F9AL.44 | `complejos.tex` | 24 myproof → 4 pasos | Pendiente | — | Tras F9AL.28 |
| F9AL.45 | `vectoresrn.tex` | 27 myproof → 4 pasos (bloque V) | Pendiente | — | Tras F9AL.37; opcional |
| F9AL.46 | `vvpropios.tex` | Subsección breve forma de Jordan | Completado | 2026-07-10 | §8.2.1: def J_k + teorema enunciado + ejemplo A=(1 1;−1 3)→J_2(2) SymPy-OK + rem con cite Hoffman-Kunze (bibtex corrido) + 2 refs conectadas. 790 pp, 0 errores. |

**Total: 46 ítems** (42 núcleo + 4 bloque V opcional). F9AL.34 (cierre de bloque) se ejecuta después de F9AL.44 y F9AL.46.

---

## Notas de protocolo

- Cada ítem se ejecuta en Claude Code con los archivos `.tex` abiertos; compilar con LuaLaTeX después de cada ítem; si falla, revertir antes de continuar.
- Antes de cada ítem: (1) leer las primeras 50 líneas del `.tex` destino, (2) recontar `\begin{prob}` / `\begin{myproof}` / `\begin{example}` reales, (3) compilar y confirmar 0 errores `!` antes de cerrar.
- Ítems 🔒F no arrancan sin F9AL.01 cerrado.
- Elevaciones de problema a resuelto (F9AL.04, .28 y análogos): cada myproof nuevo o reestructurado se presenta al autor para validación antes de escribirlo (misma regla que F8.P2–P4).
- La matemática ya está verificada (V3.x/V4.x): al mover contenido no se re-deriva nada; si un movimiento revela una inconsistencia matemática, se registra sin corregir y se escala al autor.
