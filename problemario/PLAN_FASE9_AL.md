# PLAN_FASE9_AL.md — Criterio Apostol para Álgebra Lineal

**Inicio:** Pendiente (plan generado 2026-07-06)
**Objetivo:** Aplicar el criterio Apostol operativo (R1–R3) a los 7 capítulos de Álgebra Lineal (`matrices`, `sel`, `espaciosvectoriales`, `prodinterno`, `vvpropios`, `translineales`, `complejos`) + bloque adicional `vectoresrn` (nota editorial §Bloque V).
**Compilador:** LuaLaTeX. Todas las figuras en TikZ puro o pgfplots — sin pstricks, sin Asymptote.
**Regla de tamaño:** cada ítem ≤ 300 líneas de código nuevo o modificado.
**Regla de contenido:** nada se elimina sin decisión explícita del autor.
**Prerequisito bloqueante:** Decisión F (convención de soluciones en `prob`, ver `ARQUITECTURA_LIBRO.md` §3.1) — los ítems marcados 🔒F no pueden ejecutarse antes.

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
**Estado:** Pendiente

---

## Semana 1 — matrices.tex (capítulo con más brechas del bloque)

### F9AL.02 — matrices: estructura de secciones R1
**Acción:** insertar cabeceras para que el capítulo quede: `\section{Propiedades básicas}` (existente) → `\section{Determinantes}` (hoy subsumido en "Matrices invertibles: determinantes", l.1462) → `\section{Matrices invertibles}` (existente, l.829) → `\section{Problemas propuestos}` (nueva, ver F9AL.04). Mover el mínimo de contenido; solo re-encabezar y reordenar bloques completos si un tema quedó partido.
**Criterio de cierre:** ≥4 secciones; determinantes con sección propia; orden def→teo→ej respetado dentro de cada una; compilación limpia.
**Líneas estimadas:** 40–90
**Estado:** Pendiente

### F9AL.03 — matrices: anidar 8 myproof huérfanos
**Acción:** localizar los 8 `\begin{myproof}` fuera de example/prob (detección automatizada disponible); anidar cada uno dentro de su `prob`/`example` correspondiente.
**Criterio de cierre:** `myproof_huerfanos = 0` en re-escaneo; compilación limpia.
**Líneas estimadas:** 16–40 (solo movimiento de delimitadores)
**Estado:** Pendiente

### F9AL.04 — matrices: crear sección de propuestos + aplicar Decisión F 🔒F
**Acción:** reunir los 25 probs bajo `\section{Problemas propuestos}`; según Decisión F, elevar 3–5 representativos con solución a `example` (4 pasos + boxed) y tratar el resto conforme a la convención elegida; tags de graduación.
**Criterio de cierre:** sección única de propuestos, graduada con tags; convención F aplicada al 100 % del capítulo.
**Líneas estimadas:** 80–150
**Estado:** Pendiente

### F9AL.05 — matrices: auditoría de figuras (protocolo F8.31)
**Acción:** 8 entornos figure sin caption/label + 4 tikzpicture fuera de figure → todos a `figure[H]` + `\caption` + `\label{fig:...}` + anchors explícitos.
**Criterio de cierre:** 12/12 figuras compliant; compilación limpia.
**Líneas estimadas:** 60–120
**Estado:** Pendiente

### F9AL.06 — matrices: figuras nuevas R2
**Acción:** (a) esquema del producto matricial AB (fila i × columna j con flechas); (b) expansión por cofactores 3×3 con submatrices sombreadas; (c) interpretación geométrica del determinante 2×2 como área del paralelogramo.
**Criterio de cierre:** 3 figuras insertadas inmediatamente después de la definición correspondiente (R2), estándar F8; compilación limpia.
**Líneas estimadas:** 100–160
**Estado:** Pendiente

### F9AL.07 — matrices: verificación de protocolo en 32 examples
**Acción:** confirmar que los 19 computacionales usan `\textbf{Paso N.}` (punto) + `\boxed{}`; que los 13 ilustrativos tienen título y se justifican como tales; corregir desviaciones.
**Criterio de cierre:** 100 % de examples conformes o justificados; lista de correcciones en Notas.
**Líneas estimadas:** 20–60
**Estado:** Pendiente

---

## Semana 2 — sel.tex

### F9AL.08 — sel: estructura de secciones R1
**Acción:** el capítulo tiene 2 723 líneas sin secciones antes de los propuestos. Insertar: `\section{Sistemas lineales y forma matricial}`, `\section{Eliminación gaussiana y Gauss-Jordan}`, `\section{Consistencia y conjunto solución}`, `\section{Sistemas homogéneos}`, `\section{Regla de Cramer}` (ajustar títulos al contenido real al ejecutar).
**Criterio de cierre:** ≥5 secciones temáticas; ningún contenido eliminado; compilación limpia.
**Líneas estimadas:** 30–70
**Estado:** Pendiente

### F9AL.09 — sel: anidar 8 myproof huérfanos
**Acción:** igual que F9AL.03 aplicado a `sel.tex`.
**Criterio de cierre:** `myproof_huerfanos = 0`; compilación limpia.
**Líneas estimadas:** 16–40
**Estado:** Pendiente

### F9AL.10 — sel: propuestos + Decisión F + heading 🔒F
**Acción:** renombrar `\section{Problemas propuestos para el capítulo}` → `\section{Problemas propuestos}`; aplicar Decisión F a los 30 probs (15 con solución dentro); tags de graduación.
**Criterio de cierre:** heading estándar, convención F aplicada, tags presentes.
**Líneas estimadas:** 60–120
**Estado:** Pendiente

### F9AL.11 — sel: figura 3 planos en ℝ³ + auditoría de las 9 existentes
**Acción:** (a) figura nueva en minipages pgfplots 3D: tres configuraciones (punto único / recta / sin intersección) tras la discusión de tipos de solución; (b) completar caption/label en las 2 figuras no conformes.
**Criterio de cierre:** figura nueva estándar F8 insertada según R2; 9/9 existentes conformes.
**Líneas estimadas:** 90–140
**Estado:** Pendiente

### F9AL.12 — sel: verificación de protocolo en 5 examples
**Acción:** igual que F9AL.07 (Ejs. con Paso N + boxed ya al 4/5; cerrar el restante o justificarlo como ilustrativo).
**Criterio de cierre:** 5/5 conformes o justificados.
**Líneas estimadas:** 10–30
**Estado:** Pendiente

---

## Semana 3 — espaciosvectoriales.tex + prodinterno.tex

### F9AL.13 — espaciosvectoriales: figuras nuevas R2 (capítulo con CERO figuras)
**Acción:** (a) diagrama W ⊂ V con el vector 0 (subespacio); (b) dos vectores no colineales generando ℝ² (combinaciones lineales/generado); (c) esquema de los espacios fundamentales de A (fila/columna/nulo con dimensiones y rango-nulidad). Insertar cada una inmediatamente después de su definición (R2).
**Criterio de cierre:** ≥3 figuras estándar F8; el capítulo deja de tener 0 figuras; compilación limpia.
**Líneas estimadas:** 120–180
**Estado:** Pendiente

### F9AL.14 — espaciosvectoriales: propuestos + Decisión F + heading 🔒F
**Acción:** heading estándar; los probs 1–15 (con solución) y 16–36 (sin solución) se tratan según Decisión F (candidatos naturales a elevar: verificación de subespacio, independencia lineal por determinante, base del espacio nulo); tags de graduación en los restantes.
**Criterio de cierre:** convención F aplicada; 15–25 propuestos graduados con tags.
**Líneas estimadas:** 60–120
**Estado:** Pendiente

### F9AL.15 — espaciosvectoriales: auditoría R1 + R3 de teoremas centrales
**Acción:** verificar orden def→motivación→teorema→ejemplo en las 7 secciones; el teorema de la base/dimensión (central) debe tener demostración o esquema — añadir esquema si solo hay enunciado; el criterio de subespacio (operacional) enunciado + referencia.
**Criterio de cierre:** inversiones registradas/corregidas (≤50 líneas por corrección); teorema central con esquema.
**Líneas estimadas:** 30–90
**Estado:** Pendiente

### F9AL.16 — prodinterno: estructura de secciones R1 (capítulo con CERO secciones)
**Acción:** insertar: `\section{Producto interno}`, `\section{Norma, distancia y ángulo}` (incluye Cauchy-Schwarz), `\section{Ortogonalidad y complemento ortogonal}`, `\section{Proceso de Gram-Schmidt}`, `\section{Proyección ortogonal y mínimos cuadrados}`, `\section{Problemas propuestos}` (ajustar al contenido real).
**Criterio de cierre:** ≥5 secciones + sección de propuestos; compilación limpia.
**Líneas estimadas:** 30–70
**Estado:** Pendiente

### F9AL.17 — prodinterno: figuras R2 + auditoría
**Acción:** (a) proyección ortogonal de u sobre v con ángulo recto marcado (tras def. de proyección); (b) Gram-Schmidt en ℝ²: v₁, v₂ originales → u₁, u₂ ortogonales (tras el teorema); (c) completar label de la figura existente sin él y verificar la otra.
**Criterio de cierre:** 2 figuras nuevas estándar F8; 2/2 existentes conformes.
**Líneas estimadas:** 90–140
**Estado:** Pendiente

### F9AL.18 — prodinterno: protocolo + residuales + propuestos 🔒F
**Acción:** eliminar/auditar las 2 marcas `\square` residuales; verificar 4 pasos en los 9 examples (8 ya conformes); aplicar Decisión F a los 23 probs (22 con solución); tags.
**Criterio de cierre:** 0 marcas residuales fuera de `proof`; examples conformes; convención F aplicada con tags.
**Líneas estimadas:** 50–110
**Estado:** Pendiente

---

## Semana 4 — vvpropios.tex

### F9AL.19 — vvpropios: párrafo introductorio + estructura de secciones
**Acción:** (a) escribir el párrafo introductorio del capítulo (único del libro sin él): motivar Av=λv como "direcciones que A no tuerce", conexión hacia atrás (matrices/determinantes vía ecuación característica) y hacia adelante (diagonalización, sistemas de EDOs — `\ref` a cap29). Si se aprueba la Decisión E2 (intercambio con translineales), motivar además desde la matriz de una transformación. (b) Insertar secciones: `\section{Valores y vectores propios}`, `\section{Diagonalización}`, `\section{Teorema de Cayley-Hamilton y potencias de matrices}`, manteniendo `\section{Algunas aplicaciones adicionales}` al final.
**Criterio de cierre:** intro de 5–9 líneas presente; ≥4 secciones; compilación limpia.
**Líneas estimadas:** 40–80
**Estado:** Pendiente

### F9AL.20 — vvpropios: figuras nuevas R2 (capítulo con CERO figuras)
**Acción:** (a) acción de A sobre vector propio (v escala λv, w genérico rota) — TikZ 2D con flechas rojas/azules; (b) diagrama de cajas de diagonalización A = PDP⁻¹ (cambio de base). Insertar tras la definición y tras el teorema de diagonalización respectivamente.
**Criterio de cierre:** 2 figuras estándar F8; compilación limpia.
**Líneas estimadas:** 80–130
**Estado:** Pendiente

### F9AL.21 — vvpropios: sección de propuestos + Decisión F + protocolo 🔒F
**Acción:** crear `\section{Problemas propuestos}` (hoy no existe; los 14 probs, 13 con solución, están dispersos); aplicar Decisión F; tags; verificar 4 pasos en los 10 examples (5 computacionales conformes, 5 por revisar/justificar).
**Criterio de cierre:** sección única graduada; convención F aplicada; examples conformes o justificados.
**Líneas estimadas:** 60–120
**Estado:** Pendiente

### F9AL.22 — vvpropios: nota editorial sobre aplicaciones a EDOs
**Acción:** la sección de aplicaciones EDO se conserva (decisión de Fase 4). Ahora que existe `cap29`, añadir remisiones cruzadas (`\ref`) en ambos sentidos y una `rem` que delimite: aquí se ve el mecanismo eigen, el tratamiento sistemático está en cap29. **No recortar contenido sin autorización del autor** — registrar en Notas cualquier solapamiento detectado.
**Criterio de cierre:** referencias cruzadas insertadas; solapamientos documentados en Notas para decisión del autor.
**Líneas estimadas:** 10–30
**Estado:** Pendiente

---

## Semana 5 — translineales.tex

### F9AL.23 — translineales: estructura de secciones R1
**Acción:** el capítulo (2 566 líneas) tiene una sola `\section` en la línea 10. Insertar: `\section{Transformaciones lineales}` (existente), `\section{Núcleo, imagen y el teorema rango-nulidad}`, `\section{Matriz de una transformación}`, `\section{Cambio de base}`, `\section{Composición e invertibilidad}`, `\section{Transformaciones geométricas en el plano y el espacio}` (ajustar al contenido real).
**Criterio de cierre:** ≥5 secciones; teorema rango-nulidad (central R3) con demostración o esquema verificado; compilación limpia.
**Líneas estimadas:** 40–90
**Estado:** Pendiente

### F9AL.24 — translineales: auditoría de 19 figuras + 1 tikz suelto
**Acción:** las 19 figuras en `figure` carecen todas de caption y label; 1 tikzpicture está fuera de entorno figure. Protocolo F8.31 completo (caption + `\label{fig:...}` + anchors).
**Criterio de cierre:** 20/20 conformes; compilación limpia.
**Líneas estimadas:** 100–200 (2 lotes internos si excede 300)
**Estado:** Pendiente

### F9AL.25 — translineales: figuras nuevas R2
**Acción:** (a) cuadrado unitario → paralelogramo bajo rotación θ y bajo cizalla (minipage doble); (b) diagrama conmutativo de composición T∘S entre V, W, Z con nodos y flechas. Insertar según R2 tras las definiciones correspondientes.
**Criterio de cierre:** 2 figuras estándar F8; compilación limpia.
**Líneas estimadas:** 80–130
**Estado:** Pendiente

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
**Estado:** Pendiente

### F9AL.37 — vectoresrn: protocolo + propuestos 🔒F
**Acción:** normalizar `Paso N:` → `Paso N.` en soluciones; verificar 4 pasos en los 8 examples; aplicar Decisión F a los 28 probs (26 con solución); heading `Problemas Propuestos` → `Problemas propuestos`; tags.
**Criterio de cierre:** formato de pasos uniforme; convención F aplicada; tags presentes.
**Líneas estimadas:** 60–140
**Estado:** Pendiente

---

## Registro de progreso

| Ítem | Archivo(s) | Acción | Estado | Fecha | Notas |
|---|---|---|---|---|---|
| F9AL.01 | `.md` | Decisión F registrada | Pendiente | — | — |
| F9AL.02 | `matrices.tex` | Estructura de secciones | Pendiente | — | — |
| F9AL.03 | `matrices.tex` | Anidar 8 myproof huérfanos | Pendiente | — | — |
| F9AL.04 | `matrices.tex` | Sección propuestos + Decisión F + tags | Pendiente | — | — |
| F9AL.05 | `matrices.tex` | Auditoría 12 figuras | Pendiente | — | — |
| F9AL.06 | `matrices.tex` | 3 figuras nuevas R2 | Pendiente | — | — |
| F9AL.07 | `matrices.tex` | Verificación protocolo 32 examples | Pendiente | — | — |
| F9AL.08 | `sel.tex` | Estructura de secciones | Pendiente | — | — |
| F9AL.09 | `sel.tex` | Anidar 8 myproof huérfanos | Pendiente | — | — |
| F9AL.10 | `sel.tex` | Propuestos + Decisión F + heading | Pendiente | — | — |
| F9AL.11 | `sel.tex` | Figura 3 planos ℝ³ + auditoría | Pendiente | — | — |
| F9AL.12 | `sel.tex` | Verificación protocolo 5 examples | Pendiente | — | — |
| F9AL.13 | `espaciosvectoriales.tex` | 3 figuras nuevas R2 | Pendiente | — | — |
| F9AL.14 | `espaciosvectoriales.tex` | Propuestos + Decisión F + tags | Pendiente | — | — |
| F9AL.15 | `espaciosvectoriales.tex` | Auditoría R1 + R3 | Pendiente | — | — |
| F9AL.16 | `prodinterno.tex` | Estructura de secciones (0 actuales) | Pendiente | — | — |
| F9AL.17 | `prodinterno.tex` | 2 figuras nuevas + auditoría | Pendiente | — | — |
| F9AL.18 | `prodinterno.tex` | Protocolo + residuales + propuestos | Pendiente | — | — |
| F9AL.19 | `vvpropios.tex` | Intro + estructura de secciones | Pendiente | — | — |
| F9AL.20 | `vvpropios.tex` | 2 figuras nuevas R2 | Pendiente | — | — |
| F9AL.21 | `vvpropios.tex` | Sección propuestos + Decisión F | Pendiente | — | — |
| F9AL.22 | `vvpropios.tex` | Remisiones cruzadas EDO (cap29) | Pendiente | — | — |
| F9AL.23 | `translineales.tex` | Estructura de secciones | Pendiente | — | — |
| F9AL.24 | `translineales.tex` | Auditoría 20 figuras | Pendiente | — | — |
| F9AL.25 | `translineales.tex` | 2 figuras nuevas R2 | Pendiente | — | — |
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
| F9AL.36 | `vectoresrn.tex` | Auditoría 26 figuras + figrayo (bloque V) | Pendiente | — | Requiere decisión autor (figrayo) |
| F9AL.37 | `vectoresrn.tex` | Protocolo + propuestos (bloque V) | Pendiente | — | — |

**Total: 37 ítems** (34 núcleo + 3 bloque V opcional).

---

## Notas de protocolo

- Cada ítem se ejecuta en Claude Code con los archivos `.tex` abiertos; compilar con LuaLaTeX después de cada ítem; si falla, revertir antes de continuar.
- Antes de cada ítem: (1) leer las primeras 50 líneas del `.tex` destino, (2) recontar `\begin{prob}` / `\begin{myproof}` / `\begin{example}` reales, (3) compilar y confirmar 0 errores `!` antes de cerrar.
- Ítems 🔒F no arrancan sin F9AL.01 cerrado.
- Elevaciones de problema a resuelto (F9AL.04, .28 y análogos): cada myproof nuevo o reestructurado se presenta al autor para validación antes de escribirlo (misma regla que F8.P2–P4).
- La matemática ya está verificada (V3.x/V4.x): al mover contenido no se re-deriva nada; si un movimiento revela una inconsistencia matemática, se registra sin corregir y se escala al autor.
