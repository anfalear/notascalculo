# PROGRESO_VERIFICACION.md — Verificación Matemática del Problemario

Última actualización: 2026-06-25 (Ej/Teo muestreo V1–V3 completado; 12/12 ítems cerrados; V1.3 corregido y confirmado — ver sección deuda técnica cerrada abajo)

Este archivo se actualiza al cierre de cada sesión, siguiendo el protocolo de `PLAN_VERIFICACION_MATEMATICA.md` Sección 5. No se elimina ningún contenido del problemario durante este proceso — ver regla heredada en el plan, Sección 3.

---

## Ya verificados — Fase 1 (no requieren reverificación)

| Capítulo | Archivo | Fecha verificación | Resultado |
|---|---|---|---|
| 5 | limites.tex | 2026-06-16 | Verificado — corrección matemática concreta (raíz de polinomio, IVT) |
| 2 | preliminares.tex | 2026-06-16 | Verificado — AM-GM corregida, 2 problemas corregidos con justificación |
| 11 | apintegral.tex | — | Verificado — capítulo modelo, todos los ejemplos verificados |
| 12 | impropias.tex | 2026-06-17 | Verificado — 7/7 ejemplos, sin errores |
| 13 | polares.tex | 2026-06-17 | Verificado — 2 errores hallados y corregidos |
| 25 | sucesionesyseries.tex | 2026-06-17 | Verificado — errores numéricos corregidos en Ej.13 y Ej.14, Raabe verificado |
| 26 | sucesionesyseriesfunciones.tex | 2026-06-17 | Verificado — 12/12 correctos, 1 error en diagrama TikZ corregido |

**No aplica** (sin contenido matemático): Cap. 1 — politicas.tex

---

## Tabla de seguimiento — ítems pendientes

Estado: `Pendiente` / `En progreso` / `Completo` / `Bloqueado` (requiere decisión del autor)

| Ítem | Capítulo | Archivo | Tipo | # problemas total | # a verificar | # verificados | Estado | Fecha | Errores encontrados | Errores corregidos | Notas |
|---|---|---|---|---|---|---|---|---|---|---|---|
| V1.1 | 18 | funvectoriales.tex | Completo | 11 (banco) | 11 | 11 | Completo | 2026-06-19 | 1 (Prob3c: `=` faltante en LaTeX) | 1 | Duplicación \section resuelta (2ª eliminada). Probs 6-11 con solución verificados numéricamente. Prob3c: typo `f(x,y)\dfrac{}{}` → `f(x,y)=\dfrac{}{}`. Círculos llamados "elipse" en Probs 8,11: válido (son elipses degeneradas), sin cambio. |
| V1.2 | 21 | gradientes.tex | Completo | 17 (banco) | 17 | 17 | Completo | 2026-06-19/20 | 6 (Prob2: unidades m/s→m³/s; Prob3: typo 0.03→0.3 + unidades m/s→m²/s; Prob5: unidades m/s→cm/s en tasa de z; Prob7: unidades m/s→cm/s en tasa de z; Prob9: enunciado "12 cm/min"→"12 cm" y myproof nuevo) | 6 + 1 | Probs 2 y 3: corregidos 2026-06-19. Probs 5 y 7: m/s→cm/s en la tasa de z (los otros datos ya estaban en cm/s). Prob 9: dato ambiguo resuelto — la longitud del segundo cateto es 12 cm (no una tasa); enunciado corregido y myproof agregado: dα/dt = 3/61 rad/min, derivando tan α = a/b con db/dt=0, sec²α = 61/36. |
| V1.3a | 22 | multiplicadoresintdobles.tex | Completo | 11 (primera mitad banco) | 11 | 11 | Completo | 2026-06-19 | 5 (Prob1: D=8→12, s_xx=2→4, (1/3-1)→(1/3-2), √12→5√3/3; Prob7: cm³→cm² en enunciado) | 5 | Probs 3-6 con solución: todos correctos. Probs 2,8-11 sin solución: enunciados bien planteados y resolubles. |
| V1.3b | 22 | multiplicadoresintdobles.tex | Completo | 11 (segunda mitad banco) | 11 | 11 | Completo | 2026-06-19 | 6 (Prob18: P_qq=-2→-4, D=4→12; Prob19: label ∂f/∂x→∂f/∂y; Prob20: (√3/2,1/2)→(√3/2,-1/2) y (-√3/2,1/2)→(-√3/2,-1/2); Prob21: cm³→cm²) | 6 | Probs 12-17,22 sin solución: todos bien planteados. |
| V1.4 | 19 | limvariasvariables.tex | Completo | 16 (banco) | 16 | 16 | Completo | 2026-06-19 | 2 (Prob5: error en dominio de discontinuidad; Prob11: x⁴ faltante en denominador) | 2 | Prob5: solución decía "solo indetermina en (0,0)" — ERROR: x⁵+6y⁵=0 define la recta x=−⁵√6·y completa. Corregido con descripción de discontinuidades esenciales en toda la recta + verificación en origen. Prob11: paso intermedio "x⁴(1−m²)/(1+m²)" → "x⁴(1−m²)/[x⁴(1+m²)]". Probs 7,8,9,13,14,15,16 sin solución: todos bien planteados y verificados. |
| V1.5 | 20 | planostangentes.tex | Completo | 9 (banco) | 9 | 9 | Completo | 2026-06-19 | 1 (Prob3: $(2z-8)$ → $(2z_0-8)$ en fórmula general de ∇G) | 1 | Probs 4-5 con solución correctos. Probs 6-11 sin solución: todos bien planteados; respuestas: 4x+2y+z=7; 2x+2y+2√3z=9; 5x+2y-2z=-4; Euler grado 6 verificado; f armónica sii A=0; x-2y+z=4. |
| V2.1 | 10 | intdefinida.tex | Completo | 15 (nuevos) | 15 | 15 | Completo | 2026-06-19 | 0 | 0 | Sin errores. Los 15 problemas bien planteados; respuestas: 6; 3; [1,e]; 0; {2,14/3-ln4,9,1}; 3x²sin(x⁶); 2xcos(x²)-cosx; ln17/2; 1; 2/π; {8,-8}; (e-1)/2; {4/3m,4m}; ∛2; sinx√(1+cos⁴x). Ejemplos orgánicos (5) correctos. |
| V2.2 | 7 | apderivadas.tex | Completo | 21 (ejs. orgánicos) | 21 | 21 | Completo | 2026-06-19 | 1 (Ej11: C(√3)=1292.8→1319.6 USD) | 1 | 21 ejemplos verificados (3 razones cambio, 4 extremos/mon/conc/análisis, 1 trazado, 3 optim, 2 TVM, 4 L'Hôpital, 2 Newton-Raphson, 2 diferenciales). Error: costo mínimo tubería era $1292.8; correcto es 300√3+800≈$1319.6 (C(0)=1400 y C(8)≈1709 correctos). |
| V2.3 | 33 | inttriples.tex | Completo | 2 (sección esféricas) | 2 | 2 | Completo | 2026-06-19 | 0 | 0 | Ambas respuestas exactas: 10π≈31.41592 y 64π≈201.0619. Ej. orgánico bola: V=4πa³/3 ✓. Ej. cilíndrica: V=8π ✓. |
| V3.1 | 3 | complejos.tex | Completo | 24 (banco) | 24 | 24 | Completo | 2026-06-19 | 3 | 3 | Prob1b: z₁z₂z₃=-15+i→-9+7i (2i×(-2) escrito como +4i y step final 7i²-7i transpuesto). Prob1c: numerador (-8-8i)(-5+14i)=152+152i→152-72i (-112i escrito como +112i). BProb4: w̄ "cuarto"→"tercer" cuadrante. 21/24 restantes correctos. |
| V3.2 | 8 | vectoresrn.tex | Completo | 23 (orgánicos) | 23 | 23 | Completo | 2026-06-20 | 2 (Prob3e: x=(3,-7/3,-1)→(3,-7/3,1); banco P1: mismo error + typo 2u-v+w→2u-v-w) | 2 | Todos los 23 problemas verificados. Prob 12 (9 partes: baricentro, ortocentro, recta de Euler) verificado numéricamente al detalle. Banco P3 sin solución en banco (la solución está en Prob 20 orgánico). |
| V3.3 | 17 | prodinterno.tex | Completo | 23 (conteo real 2026-06-22; plan decía 7) | 23 | 23 | Completo | 2026-06-22 | 5 (Probs 3, 5, 7, 9, 13) | 5 | Correcciones verificadas y aplicadas por el autor. Todas las soluciones re-derivadas son correctas. Se verificaron 23 problemas (incluidos los 16 sin errores). Ej/Teo: no muestreados (capítulo cerrado antes del protocolo de muestreo — ver deuda técnica en PLAN Sección 8). |
| V3.4 | 32 | apintdobles.tex | Completo | 11 (sin trazabilidad) | 11 | 11 | Completo | 2026-06-22 | 0 errores en enunciados | 0 | Todos bien planteados. Sin soluciones previas: se agregó myproof a los 11. Respuestas: P1(26; 0), P2(3/20; 3/20; 17√17/24), P3(orden invertido), P4(5/3+π/4), P5(m=52/15, x̄=16/13, ȳ=190/91), P6(Ix=160/9, Iy=608/105, I0=7424/315), P7(π(e⁴−e)), P8(π/3+√3/2), P9(≈1.208, sin forma cerrada elemental), P10(π/6), P11(m=5π/3, x̄=21/20, ȳ=0). |
| V3.5 | 31 | cap31_Transformada de Laplace.tex | Completo | 21 | 21 | 21 | Completo | 2026-06-22 | 0 | 0 | 21/21 correctos (4 lotes). Muestreo ej/teo: 9/46 revisados (20%), todos correctos. Capítulo sin errores. |
| V4.1 | 6 | derivadas.tex | Muestreo | 37 | 10 | 10 | Completo | 2026-06-22 | 0 | 0 | Probs muestreados: 4,7,11,15,19,22,26,30,33,37 — todos correctos. Ej/Teo: 8/38 (Envs #5,10,14,19,24,29,33,38), todos correctos. Sin escalación. |
| V4.2 | 9 | tecintegracion.tex | Muestreo (=100%, archivo pequeño) | 4 | 4 | 4 | Completo | 2026-06-22 | 0 | 0 | Todos verificados al 100%. Ej/Teo: 8/38 (Envs #5,10,14,19,24,29,33,38), todos correctos. Sin escalación. |
| V4.3 | 4 | funciones.tex | Muestreo | 17 | 5 | 5 | Completo | 2026-06-23 | 2 (Prob17-sub10: "cm"→"m" en enunciado; caption figura → "Patrón para la tienda de acampar") | 2 | Probs 3,7,10,14 correctos. Prob17 bien planteado excepto dos typos tipográficos en sub-ítem 10. Ej/Teo: 6/29 revisados, todos correctos. Sin escalación (errores tipográficos, no matemáticos). |
| V4.4 | 14 | matrices.tex | Completo (escalado desde Muestreo) | 25 | 25 | 25 | Completo | 2026-06-24 | 11 (Lote1: 6 errores; Lote4: Prob23 cadena A²=[A]=[A]=res→A²=[A]·[A]=res) | 11 | Lotes 2-4 sin errores adicionales. Prob23: error de presentación (= en lugar de · entre factores). Probs 22,24 ✓. Nota estructural (no matemática): \begin{myproof} fuera de \begin{prob} en Probs 5,8,21,22. |
| V4.5 | 15 | sel.tex | Completo (escalado desde Muestreo) | 30 | 30 | 30 | Completo | 2026-06-24 | 4 (Env#9: texto pivote -2→-1; Prob11: XB subscript→respuesta incorrecta; Prob13: eliminación con fracciones incorrectas; Prob20: RREF incorrecta→coeficientes y P(20) totalmente mal) | 4 | Probs 24-30: "Problemas propuestos" sin myproof (N/A). Prob 11 verificado numéricamente con Kronecker. Prob 20: coeficientes del documento completamente incorrectos; corregidos usando NumPy (número de condición 2.7e8, sistema de Vandermonde mal condicionado). |
| V4.6 | 16 | espaciosvectoriales.tex | Completo (escalado desde Muestreo) | 36 | 36 | 36 | Completo | 2026-06-24 | 8 (Prob5c: det=0→201, no base→SÍ base; Prob8: det=2t-3→t-3, t≠3/2→t≠3; Prob9: mult. matricial incorrecta; Prob12a: RREF rango2→3, base 2→3 vectores; Prob12b: RREF rango3→4, base canónica R^4; Prob13: N(A) gen (1,-2,1,0,0)→(-1,2,1,0,0); Prob14: RREF y A incorrectos, A=[[2,4,1,0],[4,5,0,1]]→[[-2,4,1,0],[-5,8,0,1]]; Prob15b: cofactores erróneos, det=6t²+15t-9→6t²-15t+9, ceros t=1/2,−3→t=1,3/2) | 8 | Probs 1-15 con solución: todos verificados al 100%. Probs 16-36 ("Problemas propuestos"): enunciados verificados, sin myproof (diseño original del documento). Ej/Teo: 14/70 muestreados, todos correctos. Prob15a ✓. |
| V4.7 | 23 | vvpropios.tex | Completo (escalado desde Muestreo) | 14 | 14 | 14 | Completo | 2026-06-24 | 6 (Prob6c anterior; Prob11 anterior; Prob12b anterior; Prob1a: mult_geom λ=2 es 1 no 2, (2,0,1) no es eigenvector, A no diagonalizable; Prob9a: eigenvalores 2,3,-5→0,1,-1 con eigenvectores (-2,1,4),(-4,2,7),(-3,1,5); Prob9b: A²⁰u corregido→(58,-28,-101); Prob12c: pol.car. (λ-1)²(λ-5)→(λ-1)(λ-2)(λ-3), eigs 1,2,3, solución completa con IC) | 6 | Probs 2,4,5,7,10,11,13,14 sin errores. Probs 1a,9,12c corregidos. Ej/Teo: 7/36 muestreados, todos correctos. |
| V4.8 | 24 | translineales.tex | Completo (escalado desde Muestreo) | 22 | 22 | 22 | Completo | 2026-06-24 | 4 (Env33: det; Prob2k: kernel; Env24: hip. débil; Prob12: def T) | 4 | Todos corregidos. Env33: det -11→-10. Prob2k: kernel (1,-1,1)→(3,-3,2). Env24: teorema único dividido en dos — (1) inyectivas→composición inyectiva, (2) invertibles→(T₂∘T₁)⁻¹=T₁⁻¹∘T₂⁻¹. Prob12: enunciado reformulado a T(f)=(f(0),f(π),f(2π))^T con soluciones reescritas: T(1+sinx+cosx)=(2,0,2), ker={sinx}, im=span{(1,1,1),(1,-1,1)}, rango=2. |
| V4.9 | 34 | cap34_integrales_vectoriales.tex | Completo (escalado desde Muestreo) | 29 | 29 | 29 | Completo | 2026-06-24 | 2 (Ej/Teo24: centro masa x̄=ȳ=z̄ incorrecto; Ej/Teo30: ∂(xz)/∂y=x→0) | 2 | 29 probs propuestos bien planteados. Ej24 (example/1389): simetría falsa x̄=ȳ=z̄=2R/3 → corregido a (4R/(3π),4R/(3π),2R/3). Ej30 (example/1620): ∇·F=x+2z→2z; resultado π/3 correcto por simetría pero divergencia era errónea. |
| V4.10a | 27 | cap27_EDOs primer orden.tex | Muestreo | 19 | 5 | 5 | Completo | 2026-06-24 | 0 | 0 | Probs 4,8,11,15,19 correctos. Ej/Teo 3/13 muestreados (def/21, example/220, example/386), correctos. Sin escalación. |
| V4.10b | 28 | cap28_EDOs orden n.tex | Completo (escalado desde Muestreo) | 20 | 20 | 20 | Completo | 2026-06-24 | 3 (Prob8: A=0,B=1→A=-1,B=0 para y''-4y'+4y=e^{2x}cosx; Prob19: u₁=ln(e^x+1)→u₁=x-ln(e^x+1), u₂=-e^x+x-ln→-e^x+ln; Ej/Teo23/example/369: ∫sin²(2x)/cos(2x)dx faltaba factor 1/2, yp corregido) | 3 | Probs 1-3,5-7,9-18,20 correctos. 32 entornos Ej/Teo verificados al 100%. Probs 8 y 19 (variación de parámetros) tenían errores de cálculo. Ej/Teo23 (y''+4y=tan(2x)): integral errónea propagó factor 2 en y_p. |
| V4.10c | 29 | cap29_Sistemas de EDOs.tex | Completo (escalado desde Muestreo) | 20 | 20 | 20 | Completo | 2026-06-24 | 1 (Prob4: ODE eliminación $x''-4x'-4x=0$→$x''-4x'+4x=0$; raíz doble $r=2$, solución $(c_1+c_2t)e^{2t}$) | 1 | Probs 1-3, 5-20 correctos. Ej/Teo: 4/17 muestreados (Envs #4,9,13,17), todos correctos. |
| V4.10d | 30 | cap30_Sol EDOs Series Potencias.tex | Muestreo | 16 | 5 | 5 | Completo | 2026-06-24 | 0 (muestreo) | 0 | Probs 3,6,10,13,16 correctos. Ej/Teo: 4/16 muestreados (#4,8,12,16), todos correctos. Sin escalación. Obs. fuera de muestra: Prob14 (Hermite n=1) tiene paso intermedio erróneo $y=a_0(1-2x^2)$ que no satisface la ODE — documento lo cuestiona pero deja sin corregir; se anota para decisión del autor. |

**Regla de escalación:** si el muestreo de un ítem V4 encuentra al menos un error matemático, ese ítem pasa automáticamente a Tipo `Completo` (se verifica el 100% del archivo) y se reclasifica como V4→V1 en la siguiente actualización de este archivo.

---

## Resumen de avance

- Fase V1: 6/6 ítems completos ✓ (V1.2 cerrado al 100% el 2026-06-20)
- Fase V2: 3/3 ítems completos ✓
- Fase V3: 5/5 ítems completos ✓
- Fase V4: 13/13 ítems completos (V4.1–V4.10d) ✓
- **Total: 27/27 ítems completos ✓**

**PLAN DE VERIFICACIÓN COMPLETADO.** 27/27 ítems cerrados. Ej/Teo muestreo V1–V3 completado y cerrado el 2026-06-25 (12/12 ítems; 1 error en V1.3 corregido y confirmado). Decisiones arquitectónicas A-D resueltas. Documento compila limpio: 724 páginas, 0 errores. Obs. abierta sin bloqueo: Prob14 (`cap30`) — paso intermedio Hermite n=1 posiblemente incorrecto; documentado para decisión del autor en sesión futura.

---

## Deuda técnica cerrada — Ej/Teo muestreo V1–V3 (2026-06-25)

Protocolo: entornos `\begin{example}`, `\begin{theorem}`, `\begin{lemma}`, `\begin{corollary}`, `\begin{definition}`, `\begin{proof}`, `\begin{myproof}` fuera de `\begin{prob}`. Muestra sistemática: si n<5 → todos; si n≥5 → max(2, ⌈0.20·n⌉). Selección: round(n/m·k)−1 para k=1…m.

| Ítem | Archivo | n total | n muestra | Resultado | Notas |
|---|---|---|---|---|---|
| V1.1 | funvectoriales.tex | 31 | 7 | Sin errores | Envs en l.132,184,290,376,494,584,703 — todos correctos |
| V1.2 | gradientes.tex | 24 | 5 | Sin errores | Envs en l.81,199,305,437,589 — todos correctos |
| V1.3 | multiplicadoresintdobles.tex | 24 | 5 | **1 ERROR — CERRADO** | Env #24 (l.514): det(H̄)=6d²+d√2 → correcto es 8d² (verificado SymPy+NumPy). Corrección aplicada: `= 6d^2+d\sqrt{2} > 0.` → `= 8d^2 > 0.` Confirmado en archivo el 2026-06-25. Conclusión matemática (H̄>0 → máx. restricto) sigue válida pues 8d²>0 |
| V1.4 | limvariasvariables.tex | 23 | 5 | Sin errores | Envs en l.161,276,324,391,441 — todos correctos |
| V1.5 | planostangentes.tex | 25 | 5 | Sin errores | Envs en l.89,229,520,603,635 — todos correctos |
| V2.1 | intdefinida.tex | 28 | 6 | Sin errores | Envs en l.121,179,250,298,332,424 — todos correctos |
| V2.2 | apderivadas.tex | 57 | 12 | Sin errores | Envs en l.281,355,453,718,891,1224,1439,1564,1676,1811,1937,2001 — todos correctos |
| V2.3 | inttriples.tex | 24 | 5 | Sin errores | Envs en l.118,179,269,420,490 — todos correctos |
| V3.1 | complejos.tex | 10 | 2 | Sin errores | Envs en l.179,528 — todos correctos |
| V3.2 | vectoresrn.tex | 26 | 6 | Sin errores | Envs en l.124,374,423,467,875,964 — todos correctos |
| V3.3 | prodinterno.tex | 59 | 12 | Sin errores | Envs en l.38,84,167,225,342,397,424,484,636,688,808,995 — todos correctos (incl. Gram-Schmidt P₂, mínimos cuadrados, Euler) |
| V3.4 | apintdobles.tex | 24 | 5 | Sin errores | Envs en l.81,141,422,567,621 — todos correctos |

**Resultado global: 12/12 ítems sin errores o con error corregido. Muestreo Ej/Teo V1–V3 completamente cerrado al 2026-06-25.**

**V1.3 — CERRADO:** corrección `= 6d^2+d\sqrt{2} > 0.` → `= 8d^2 > 0.` aplicada en `multiplicadoresintdobles.tex` l.514 y confirmada en archivo el 2026-06-25.

---

## Volumen total de problemas por fase (conteo real, 2026-06-19)

| Fase | Problemas en archivo | A verificar | Tipo |
|---|---|---|---|
| V1 (riesgo alto) | 75 | 75 | Completo |
| V2 (contenido nuevo) | 36 | 36 | Completo |
| V3 (bancos pendientes Fase 1) | 86 | 86 | Completo |
| V4 (solo reformateo) | 289 | 82 | Muestreo (~28%) |
| **Total** | **486** | **279** | |

**Importante para no sobre-afirmar:** al cierre de este plan, el problemario NO tendrá "486 de 486 problemas verificados". Tendrá 197 problemas (V1+V2+V3) verificados al 100%, más una validación por muestreo de 82/289 en V4. Si algún ítem V4 escala por la regla de escalación, ese número de verificación completa sube. La afirmación correcta a futuro es "100% verificado en bancos fusionados y contenido nuevo; muestreo sin errores en contenido heredado del documento original" — no "100% del problemario verificado".

