# DIAGNÓSTICO PROBLEMARIO — Andrés Fabián Leal Archila
**Fecha:** 2026-06-16  
**Versión:** 0.1 — lectura sin modificaciones

---

## PASO 1 — Inventario crudo

### Archivo maestro
`anfalearNotasCalculo.tex` (513 líneas). Incluye **dos partes** actuales:

| Parte actual | Archivos incluidos en orden |
|---|---|
| `\part{Álgebra Lineal}` | politicasal, complejos, vectoresrn, matrices, sel, espaciosvectoriales, prodinterno, vvpropios, translineales |
| `\part{Cálculo}` | politicas, preliminares, funciones, limites, derivadas, apderivadas, tecintegracion, intdefinida, apintegral, impropias, polares, sucesionesyseries, sucesionesyseriesfunciones, funvectoriales, limvariasvariables, planostangentes, gradientes, multiplicadoresintdobles, apintdobles, inttriples, camposconservativos, integraleslineacampos, intsuperficies |

No hay archivos `.cls` ni `.sty` personalizados; todo el preámbulo está en el maestro.

### Todos los archivos `.tex` (tamaño en líneas)

| Archivo | Líneas |
|---|---|
| matrices.tex | 3 167 |
| sel.tex | 2 922 |
| apderivadas.tex | 2 684 |
| translineales.tex | 2 529 |
| apintegral.tex | 2 266 |
| vectoresrn.tex | 2 258 |
| sucesionesyseriesfunciones.tex | 1 712 |
| prodinterno.tex | 1 455 |
| complejos.tex | 1 423 |
| vvpropios.tex | 1 395 |
| sucesionesyseries.tex | 1 343 |
| derivadas.tex | 1 321 |
| espaciosvectoriales.tex | 1 294 |
| polares.tex | 1 232 |
| funciones.tex | 1 207 |
| tecintegracion.tex | 1 202 |
| limvariasvariables.tex | 1 007 |
| limites.tex | 968 |
| impropias.tex | 967 |
| funvectoriales.tex | 913 |
| gradientes.tex | 869 |
| preliminares.tex | 797 |
| integraleslineacampos.tex | 706 |
| intsuperficies.tex | 695 |
| anfalearNotasCalculo.tex | 513 |
| camposconservativos.tex | 493 |
| multiplicadoresintdobles.tex | 463 |
| inttriples.tex | 382 |
| intdefinida.tex | 380 |
| apintdobles.tex | 377 |
| planostangentes.tex | 363 |
| politicas.tex | 137 |
| politicasal.tex | 117 |

### Observaciones sobre archivos sueltos / problemáticos

1. **`planostangentes.tex`** abre con `\section{...}` en lugar de `\chapter{...}`. Es un **huérfano estructural**: no puede funcionar como capítulo independiente. Actualmente se incluye en la parte de Cálculo directamente, lo que implica que su contenido aparece como sección sin numeración de capítulo propia.

2. **`politicas.tex` y `politicasal.tex`** son versiones paralelas de "Políticas del curso" para Cálculo y Álgebra Lineal respectivamente. El índice objetivo tiene un solo Cap. 1 "Políticas del curso".

3. **`multiplicadoresintdobles.tex`** mezcla Cap. 22 (Lagrange) con Cap. 32 (integrales dobles rectangulares) en el mismo archivo.

4. **`apintdobles.tex`** tiene encabezado `\chapter{Lección 2.3...}` y **`inttriples.tex`** tiene `\chapter{Lección 3.1...}`: denominación de "lección" inconsistente con la estructura de libro.

---

## PASO 2 — Mapeo contra el índice de 34 capítulos

**Convenciones de estado:**
- **Completo**: archivo(s) con cobertura temática sustancial y volumen razonable.
- **Parcial**: existe contenido pero hay subtemas faltantes, problemas estructurales o de estilo grave.
- **Ausente**: no existe nada identificable.

| # | Título objetivo | Estado | Archivo(s) fuente | Notas |
|---|---|---|---|---|
| 1 | Políticas del curso | **Parcial** | `politicas.tex` + `politicasal.tex` | Hay DOS archivos separados (Cálculo y AL); el objetivo tiene uno solo |
| 2 | Preliminares | **Completo** | `preliminares.tex` | Cubre axiomas de R, valor absoluto, intervalos, vecindades, sup/ínf |
| 3 | Números complejos | **Completo** | `complejos.tex` | Representaciones, Euler, De Moivre, TFA; 1 bug estructural menor |
| 4 | Funciones | **Completo** | `funciones.tex` | Catálogo completo; ejemplos sin formato 4 pasos |
| 5 | Límites y Continuidad | **Parcial** | `limites.tex` | 1 error matemático confirmado (ver Paso 5); ejemplos sin 4 pasos |
| 6 | La Derivada | **Parcial** | `derivadas.tex` | Buena cobertura temática; 0/26 ejemplos con formato 4 pasos; 0 `\boxed` |
| 7 | Aplicaciones de la Derivada | **Parcial** | `apderivadas.tex` | Falta "diferenciales y aproximaciones" del programa; 12/19 ejemplos con 4 pasos; solo 2 `\boxed` |
| 8 | Espacio euclídeo n-dimensional | **Completo** | `vectoresrn.tex` | Vectores, producto punto/cruz, rectas, planos |
| 9 | Integrales indefinidas y técnicas | **Parcial** | `tecintegracion.tex` | 25 ejemplos sin formato 4 pasos; 0 `\boxed`; solo 4 problemas propuestos |
| 10 | La Integral Definida | **Parcial** | `intdefinida.tex` | **0 problemas propuestos** (prob=0); 0 formato 4 pasos; 0 `\boxed`; capítulo teoría pura sin ejercicios |
| 11 | Aplicaciones de la integral | **Completo** | `apintegral.tex` | Mejor capítulo: 24/24 ejemplos con 4 pasos y `\boxed`; TikZ fillbetween correcto |
| 12 | Integrales Impropias | **Completo** | `impropias.tex` | 7/7 ejemplos con 4 pasos; TikZ correcto |
| 13 | Curvas Paramétricas y Coordenadas Polares | **Completo** | `polares.tex` | 8 ejemplos con 4 pasos; 7 instancias `axis equal` apropiadas |
| 14 | Matrices y determinantes | **Parcial** | `matrices.tex` | Contenido rico (3 167 líneas); solo 5/32 ejemplos con formato 4 pasos; muchas soluciones fuera de myproof |
| 15 | Sistemas de ecuaciones lineales | **Parcial** | `sel.tex` | Grande (2 922 líneas); 8 instancias de Paso 1 en 5 ejemplos (inconsistente); estilo mixto |
| 16 | Espacios vectoriales | **Parcial** | `espaciosvectoriales.tex` | 15 ejemplos con 0/15 formato 4 pasos; 0 `\boxed` |
| 17 | Espacios vectoriales con producto interno | **Parcial** | `prodinterno.tex` | 4/11 ejemplos con Paso 1; Gram-Schmidt presente |
| 18 | Funciones de varias variables y vectoriales | **Parcial** | `funvectoriales.tex` | 4/7 ejemplos con Paso 1; cubre curvas en R³ y superficies |
| 19 | Límites y continuidad en Rn | **Parcial** | `limvariasvariables.tex` | **PROBLEMA ESTRUCTURAL**: §2 (líneas 460–864) contiene derivadas parciales → pertenece al Cap. 20 |
| 20 | Diferenciación parcial, gradiente y diferenciabilidad | **Parcial** | `limvariasvariables.tex` (§2) + `planostangentes.tex` + `gradientes.tex` (§1) | **PROBLEMA ESTRUCTURAL GRAVE**: contenido fragmentado en 3 archivos; planostangentes.tex no tiene `\chapter` |
| 21 | Regla de la cadena y derivadas direccionales | **Parcial** | `planostangentes.tex` + `gradientes.tex` (§1) | Mismo problema estructural que Cap. 20 |
| 22 | Optimización: extremos y multiplicadores de Lagrange | **Parcial** | `gradientes.tex` (§2) + `multiplicadoresintdobles.tex` (§1) | **PROBLEMA ESTRUCTURAL**: multiplicadoresintdobles.tex también contiene integrales dobles (Cap. 32) |
| 23 | Valores y vectores propios | **Parcial** | `vvpropios.tex` | 0/10 ejemplos con formato 4 pasos; incluye aplicaciones EDO que sobrepasan el alcance del cap. |
| 24 | Transformaciones lineales | **Parcial** | `translineales.tex` | 0/10 ejemplos con 4 pasos; **0 `\boxed`** en todo el archivo; myproof=56 (inconsistencia alta) |
| 25 | Sucesiones y Series de Números Reales | **Completo** | `sucesionesyseries.tex` | 13/14 ejemplos con 4 pasos; sólido |
| 26 | Sucesiones y series de funciones | **Completo** | `sucesionesyseriesfunciones.tex` | 12/12 ejemplos con Paso 1; 48 problemas (muchos sin solución) |
| 27 | EDOs de primer orden | **Ausente** | — | — |
| 28 | EDOs lineales de orden superior | **Ausente** | — | — |
| 29 | Sistemas lineales de EDOs | **Ausente** | — | — |
| 30 | Soluciones en series de potencias para EDOs | **Ausente** | — | — |
| 31 | Transformada de Laplace | **Ausente** | — | — |
| 32 | Integrales múltiples | **Parcial** | `multiplicadoresintdobles.tex` (§2–3) + `apintdobles.tex` + `inttriples.tex` | Contenido fragmentado en 3 archivos; falta coordenadas cilíndricas y esféricas |
| 33 | Integrales de línea y de superficie | **Parcial** | `camposconservativos.tex` + `integraleslineacampos.tex` + `intsuperficies.tex` | Tres archivos; contenido existe pero sin delimitación clara |
| 34 | Teoremas integrales (Green, Stokes, Divergencia) | **Parcial** | `integraleslineacampos.tex` (§3–4) + `intsuperficies.tex` (§4–5) | Green en un archivo, Stokes y Gauss en otro; no existe cap. autónomo |

---

## PASO 3 — Calidad y consistencia de estilo

### Tabla de entornos y cobertura de 4 pasos

| Archivo / Cap. | def | thm | rem | ex | prob | myproof | ex con 4 pasos | prob con sol. | boxed | Consist. estilo |
|---|---|---|---|---|---|---|---|---|---|---|
| preliminares (C2) | — | 5 | 5 | 5 | 7 | 5 | 4/5 | 0 | 5 | Alto |
| complejos (C3) | ~10 | ~10 | ~8 | — | ~15 | ~15 | n/a | ≈14 | ~15 | Alto |
| funciones (C4) | ~10 | 5 | 5 | ~8 | ~12 | ~8 | 0/8 | 0 | — | Medio |
| limites (C5) | 5 | 10 | 8 | ~12 | ~30 | ~12 | 0 | 0 | — | Medio |
| derivadas (C6) | 2 | 8 | 14 | 26 | 37 | 29 | **0/26** | ~3 | **0** | **Bajo** |
| apderivadas (C7) | 4 | 8 | 9 | 19 | 50 | 19 | 12/19 | 0 | 2 | Medio |
| vectoresrn (C8) | 11 | 1 | 1 | 8 | 23 | 29 | 5/8 | ≈20 | 21 | Medio |
| tecintegracion (C9) | 2 | 9 | 10 | 25 | 4 | 27 | **0/25** | ≈2 | **0** | **Bajo** |
| intdefinida (C10) | 4 | 10 | 8 | 7 | **0** | 7 | **0/7** | n/a | **0** | **Bajo** |
| apintegral (C11) | 8 | 7 | 13 | 24 | 41 | 24 | **24/24** | 0 | **24** | **Alto** |
| impropias (C12) | 3 | 3 | 5 | 7 | 17 | 7 | **7/7** | 0 | 7 | **Alto** |
| polares (C13) | 2 | 4 | 6 | 8 | 12 | 8 | 8/8 | ≈4 | 12 | **Alto** |
| matrices (C14) | 21 | 11 | 6 | 32 | 25 | 49 | 5/32 | ~25 | 53 | Medio |
| sel (C15) | 5 | 4 | 4 | 5 | 30 | 32 | ~8 mezcl. | ≈30 | 5 | Medio |
| espaciosvect. (C16) | 12 | 17 | 5 | 15 | 36 | 25 | **0/15** | ≈20 | 2 | **Bajo** |
| prodinterno (C17) | 10 | 15 | 1 | 11 | 23 | 31 | 4/11 | ≈20 | 21 | Medio |
| funvectoriales (C18) | 10 | 5 | 10 | 7 | 13 | 7 | 4/7 | 0 | 7 | Medio |
| limvariasvariables (C19) | 6 | 3 | 13 | 13 | 14 | 12 | 7/13 | ≈10 | 15 | Medio |
| planostangentes (C20/21) | 2 | 5 | 4 | 6 | 5 | 6 | 0/6 | ≈5 | 7 | Bajo |
| gradientes (C20/21/22) | 6 | 6 | 12 | 5 | 10 | 5 | 3/5 | ≈5 | 4 | Medio |
| multiplicadoresintdobles (C22/32) | 6 | 6 | 2 | 7 | 6 | 3 | **0/7** | ≈3 | **0** | **Bajo** |
| apintdobles (C32) | **0** | **0** | 3 | 7 | 8 | 7 | 0/7 | ≈7 | 7 | **Bajo** |
| inttriples (C32) | 1 | 1 | 4 | 7 | 10 | 7 | 0/7 | ≈7 | 6 | **Bajo** |
| vvpropios (C23) | 7 | 10 | 3 | 10 | 14 | 33 | **0/10** | ≈14 | 4 | **Bajo** |
| translineales (C24) | 10 | 9 | 2 | 10 | 22 | 56 | **0/10** | ≈22 | **0** | **Bajo** |
| sucesionesyseries (C25) | 7 | 16 | 12 | 14 | 16 | 13 | 13/14 | ≈12 | 12 | **Alto** |
| sucesionesyseriesfunc. (C26) | 4 | 13 | 16 | 12 | 48 | 12 | 12/12 | 0 | 14 | **Alto** |
| camposconservativos (C33) | 1 | 2 | 7 | 4 | 7 | 4 | 3/4 | ≈4 | 4 | Medio |
| integraleslineacampos (C33/34) | 5 | 3 | 9 | 3 | 12 | 3 | 3/3 | ≈3 | 3 | Medio |
| intsuperficies (C33/34) | 4 | 2 | 6 | 9 | 10 | 9 | 8/9 | ≈9 | 9 | Medio |

### Desviaciones de estilo más frecuentes

1. **Ausencia total del formato 4 pasos en ejemplos** (ficheros C6, C9, C10, C16, C23, C24, C22, C32): los ejemplos resueltos son `myproof` directos sin "Paso 1: Análisis gráfico…" etc.  
2. **Ausencia de `\boxed{}`** en respuestas finales (derivadas, tecintegracion, intdefinida, translineales, multiplicadoresintdobles): el lector no puede identificar visualmente el resultado.  
3. **`myproof` fuera de `prob`** (complejos.tex ≈ línea 311–399): la solución del triángulo equilátero está en un `\begin{myproof}` que aparece *después* de `\end{prob}`.  
4. **Uso de entornos no esperados** en varios archivos de Álgebra Lineal: se usa `\begin{pasos}` (construcción/protocolo) donde se esperarían los 4 pasos dentro de `\begin{example}`. No es incorrecto, pero es inconsistente.  
5. **Prosa genérica** (sin "el hilo conductor") en C6, C9, C14, C15, C16, C23, C24: la narrativa no conecta geometría/física con el formalismo de manera explícita.  
6. **`\begin{rem}` con ítems de lista separados por texto** (especialmente en limvariasvariables y gradientes): viola la convención de no poner dos `itemize` separadas por texto dentro de un `rem`.  
7. **intdefinida.tex** es el único capítulo sin ningún `\begin{prob}` — es teoría pura sin sección de ejercicios.  
8. **translineales.tex** tiene myproof=56 con prob=22 y example=10 → hay ~24 soluciones "huérfanas" o sub-partes sin estructura clara.

---

## PASO 4 — Verificación técnica de TikZ (muestreo)

### apintegral.tex (19 instancias fillbetween)
✅ Todas las verificadas (5 muestras) usan correctamente trayectorias nombradas (`name path=`) dentro del mismo dominio paramétrico antes de llamar `fill between[of=A and B]`. El patrón de corrección está documentado en comentarios del propio archivo. **Sin errores detectados.**

### impropias.tex (9 instancias fillbetween)
✅ Muestreo de 3 instancias: trayectorias nombradas, mismo espacio paramétrico. **Sin errores detectados.**

### polares.tex (7 instancias `axis equal`, 3 fillbetween)
✅ El uso de `axis equal` sin `image` es aceptable en pgfplots (no recorta la región); las figuras de coordenadas polares lo requieren y está bien aplicado.  
⚠️ Algunas curvas polares usan `domain=0:2*pi` con variable estándar `x`; pgfplots acepta esto, pero puede generar advertencias de rango. No es un error funcional pero sí ruido en el log.

### apderivadas.tex (figuras TikZ de tasas de cambio)
✅ Los cuerpos cónicos y geométricos en tasas de cambio relacionadas usan coordenadas absolutas sin fillbetween; sin errores detectados.

### Ausencia de `axis equal image`
⚠️ En figuras de cónicas, círculos y elipses distribuidas en `vectoresrn.tex` y `complejos.tex`, se omite `axis equal` o `axis equal image` en algunos subplots. Esto distorsiona la proporción visual (círculos se ven como elipses). No es un error de compilación sino de presentación.

---

## PASO 5 — Verificación matemática (muestras)

### Cap. 2 — Preliminares
- ✅ Ejemplo `|2x-3|=5` → `x=4, x=-1` correcto.  
- ✅ Ejemplo `sup{n/(n+1)}=1` — demostración por arquímedianidad correcta.  
- ✅ Desigualdad triangular: demostración por casos correcta.

### Cap. 3 — Números complejos
- ✅ `z1z2z3 = (1+2i)(-2+3i)(1-i) = -15+i` — verificado paso a paso.  
- ✅ `z = (-1+√3i)/(3+√3i)` (problema de `it`) — análisis correcto; conclusión "Ninguna" es matemáticamente apropiada.  
- ✅ Argumento de z con arg ∈ (π, 3π/2) para `2z⁴+2z²+1=0` → `11π/8` correcto.
- ✅ Triángulo equilátero z₁=1+i, z₂=-1-i: |z₃|=√6, arg=3π/4 → z₃=-√3+i√3 correcto.

### Cap. 5 — Límites y Continuidad
- ✅ `lim_{x→0} ln(1+3x)/sin(2x) = 3/2` por equivalentes — correcto.  
- ✅ Demostración de `lim sin(x)/x = 1` por sándwich — rigurosa y correcta.  
- **❌ ERROR CONFIRMADO (línea 921):** `p(x) = x^{11}+x-x+2 = x^{11}+2`. Este polinomio es siempre positivo en (0,1) (`p(0)=2>0`, `p(1)=3>0`), por lo que el problema "¿Tiene raíces en (0,1)?" tiene respuesta **no** y contradice la consigna implícita de aplicar TVI. Es casi certero un error tipográfico (probablemente falta un término, e.g., `x^{11}+x^4-x-2` o similar).

### Cap. 6 — La Derivada
- ✅ `f'(x)=2x` para `f(x)=x²` por definición — correcto.  
- ✅ `f'(x)=1/(2√x)` para `f(x)=√x` — correcto (muestreo de los 3 primeros ejemplos).

### Cap. 7 — Aplicaciones de la Derivada
- ✅ Tanque cónico: relación `h/r = 12/6 = 2` usada correctamente para derivación implícita.  
- ✅ Estructura lógica de razones de cambio relacionadas — matemáticamente correcta.

### Cap. 11 — Aplicaciones de la integral
- ✅ Área entre `y=x²` e `y=x+2`: intersecciones en `x=-1, x=2`; área = 9/2 — correcto.  
- ✅ Área de `y=x³-x` en `[-1,1]`: 1/4 + 1/4 = 1/2 — correcto.  
- ✅ Integral doble `∫∫_R (x²y+y²)dA` sobre `[0,1]×[0,2]` = 10/3 — correcto.

### Cap. 22/32 — multiplicadoresintdobles.tex
- ✅ Fubini sobre rectángulo — correcto.  
- ✅ Lagrange: muestra verificada — correcta.

### Cap. 25 — Sucesiones y Series
- ✅ Muestras de criterios de convergencia (razón, raíz) — correctamente enunciados y aplicados.

---

## PASO 6 — DIAGNÓSTICO FINAL: Tabla maestra de 34 capítulos

| # | Título | Estado | Archivo(s) | Ex. 4-pasos completos | Prob. con sol. | Errores mat. | Errores TikZ | Estilo |
|---|---|---|---|---|---|---|---|---|
| 1 | Políticas del curso | Parcial | `politicas.tex` + `politicasal.tex` | n/a | n/a | — | — | Medio (duplicado) |
| 2 | Preliminares | **Completo** | `preliminares.tex` | 4/5 | 0/7 | — | — | Alto |
| 3 | Números complejos | **Completo** | `complejos.tex` | n/a | ≈14/15 | — (1 bug struct.) | — | Alto |
| 4 | Funciones | **Completo** | `funciones.tex` | 0/8 | 0/12 | — | — | Medio |
| 5 | Límites y Continuidad | Parcial | `limites.tex` | 0/12 | 0/30 | 1 (polinomio l.921) | — | Medio |
| 6 | La Derivada | Parcial | `derivadas.tex` | **0/26** | 3/37 | — | — | **Bajo** |
| 7 | Aplicaciones Derivada | Parcial | `apderivadas.tex` | 12/19 | 0/50 | — | — | Medio |
| 8 | Espacio euclídeo Rⁿ | **Completo** | `vectoresrn.tex` | 5/8 | ≈20/23 | — | — | Medio |
| 9 | Integrales indefinidas / técnicas | Parcial | `tecintegracion.tex` | **0/25** | 2/4 | — | — | **Bajo** |
| 10 | La Integral Definida | Parcial | `intdefinida.tex` | **0/7** | — /**0 prob** | — | — | **Bajo** |
| 11 | Aplicaciones de la integral | **Completo** | `apintegral.tex` | **24/24** | 0/41 | — | — | **Alto** |
| 12 | Integrales Impropias | **Completo** | `impropias.tex` | **7/7** | 0/17 | — | — | **Alto** |
| 13 | Curvas Paramétricas / Polares | **Completo** | `polares.tex` | 8/8 | ≈4/12 | — | — | **Alto** |
| 14 | Matrices y determinantes | Parcial | `matrices.tex` | 5/32 | ≈25/25 | — | — | Medio |
| 15 | Sistemas de ecuaciones lineales | Parcial | `sel.tex` | parcial | ≈30/30 | — | — | Medio |
| 16 | Espacios vectoriales | Parcial | `espaciosvectoriales.tex` | **0/15** | ≈20/36 | — | — | **Bajo** |
| 17 | EV con producto interno | Parcial | `prodinterno.tex` | 4/11 | ≈20/23 | — | — | Medio |
| 18 | Fun. vect. y varias variables | Parcial | `funvectoriales.tex` | 4/7 | 0/13 | — | — | Medio |
| 19 | Límites y continuidad en Rⁿ | Parcial | `limvariasvariables.tex` §1 | 7/13* | ≈10/14 | — | — | Medio |
| 20 | Diferenciación parcial / gradiente | Parcial | `limvariasvariables.tex` §2 + `planostangentes.tex` + `gradientes.tex` §1 | 0–3/varios | varios | — | — | **Bajo** |
| 21 | Regla cadena / deriv. direccionales | Parcial | `planostangentes.tex` + `gradientes.tex` §1 | 0–3/varios | varios | — | — | **Bajo** |
| 22 | Optimización / Lagrange | Parcial | `gradientes.tex` §2 + `multiplicadoresintdobles.tex` §1 | 0/varios | ≈3 | — | — | **Bajo** |
| 23 | Valores y vectores propios | Parcial | `vvpropios.tex` | **0/10** | ≈14/14 | — | — | **Bajo** |
| 24 | Transformaciones lineales | Parcial | `translineales.tex` | **0/10** | ≈22/22 | — | **0 boxed** | **Bajo** |
| 25 | Sucesiones y Series Reales | **Completo** | `sucesionesyseries.tex` | 13/14 | ≈12/16 | — | — | **Alto** |
| 26 | Sucesiones y series de funciones | **Completo** | `sucesionesyseriesfunciones.tex` | 12/12 | 0/48 | — | — | **Alto** |
| 27 | EDOs de primer orden | **Ausente** | — | — | — | — | — | — |
| 28 | EDOs lineales ord. superior | **Ausente** | — | — | — | — | — | — |
| 29 | Sistemas lineales de EDOs | **Ausente** | — | — | — | — | — | — |
| 30 | Series de potencias para EDOs | **Ausente** | — | — | — | — | — | — |
| 31 | Transformada de Laplace | **Ausente** | — | — | — | — | — | — |
| 32 | Integrales múltiples | Parcial | `multiplicadoresintdobles.tex` §2–3 + `apintdobles.tex` + `inttriples.tex` | 0/varios | ≈17 | — | — | **Bajo** |
| 33 | Integrales de línea y superficie | Parcial | `camposconservativos.tex` + `integraleslineacampos.tex` + `intsuperficies.tex` | 14/16 | ≈16 | — | — | Medio |
| 34 | Teoremas integrales | Parcial | `integraleslineacampos.tex` §3–4 + `intsuperficies.tex` §4–5 | 11/12 | ≈12 | — | — | Medio |

*El §1 de `limvariasvariables.tex` cubre límites/continuidad (Cap.19); el §2 cubre derivadas parciales (Cap.20).

---

## RESUMEN EJECUTIVO

| Estado | Cantidad | Capítulos |
|---|---|---|
| **Completo** | **8** | 2, 3, 8, 11, 12, 13, 25, 26 |
| **Parcial** | **21** | 1, 4, 5, 6, 7, 9, 10, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 32, 33, 34 |
| **Ausente** | **5** | 27, 28, 29, 30, 31 (toda la Parte VIII — EDOs) |

**Gravedad general:** Alta. Los problemas son de tres tipos distintos:
1. **Estructural** (Caps. 19–22, 32–34): el contenido existe pero está partido en archivos sin correspondencia 1:1 con capítulos; varias decisiones de redistribución deben tomarse antes de editar.
2. **Estilo** (Caps. 6, 9, 10, 16, 23, 24 y toda la rama de Álgebra Lineal): falta el formato canónico de 4 pasos y `\boxed{}` en la mayoría de los capítulos de Álgebra Lineal y en derivadas/técnicas de integración.
3. **Contenido ausente** (Caps. 27–31): la Parte VIII completa no existe.

---

## LISTA PRIORIZADA DE HALLAZGOS

### Prioridad 1 — Error matemático
1. **`limites.tex`, línea 921**: `p(x)=x^{11}+x-x+2` simplifica a `x^{11}+2`, que es siempre positivo. El problema afirma implícitamente que tiene raíz en (0,1). Es un error tipográfico que vuelve el problema matemáticamente falso; hay que reconstruir el polinomio correcto.

### Prioridad 2 — Problemas estructurales que bloquean la reorganización
2. **`planostangentes.tex` no tiene `\chapter`**: comienza con `\section`. Antes de re-numerar, debe añadirse la cabecera de capítulo o fusionarse con otro archivo.
3. **`multiplicadoresintdobles.tex` mezcla Cap. 22 (Lagrange) y Cap. 32 (integral doble)**: hay que decidir si se divide en dos archivos o se reorganiza el contenido antes de cualquier edición.
4. **Caps. 19–22 fragmentados en 4 archivos** (`limvariasvariables`, `planostangentes`, `gradientes`, `multiplicadoresintdobles`): el §2 de limvariasvariables pertenece al Cap. 20, no al 19. Planostangentes cubre tanto Cap. 20 como Cap. 21. Gradientes cubre Cap. 20, 21 y 22.
5. **Caps. 32–34 fragmentados en 5 archivos**: hay que decidir la frontera entre Cap. 32 (integrales múltiples), Cap. 33 (línea/superficie) y Cap. 34 (teoremas), actualmente mezclados.
6. **`politicas.tex` vs `politicasal.tex`**: dos capítulos donde el índice tiene uno. ¿Libro unificado = un Cap. 1 único? Decisión de autoría.

### Prioridad 3 — Déficit de contenido
7. **Cap. 10 (`intdefinida.tex`)**: cero problemas propuestos. Requiere toda una sección de ejercicios.  
8. **Parte VIII (Caps. 27–31)**: 5 capítulos completamente inexistentes. Son ≈ 5 capítulos a crear desde cero.
9. **Cap. 32 (`inttriples.tex`, 382 líneas)**: faltan coordenadas cilíndricas y esféricas (1 definición + 1 teorema es mínimo).
10. **Cap. 7 (`apderivadas.tex`)**: falta la subsección "diferenciales y aproximaciones" listada en el programa del curso.

### Prioridad 4 — Estilo sistemático
11. **Formato 4 pasos ausente** en derivadas, tecintegracion, intdefinida, espaciosvectoriales, vvpropios, translineales, multiplicadoresintdobles, apintdobles, inttriples (9 archivos, ≈ 130+ ejemplos afectados).
12. **`\boxed{}` ausente** en derivadas (37 problemas), tecintegracion (25 ejemplos), translineales (10+22 items). Las respuestas finales son ilegibles visualmente.
13. **`\begin{myproof}` fuera de `\begin{prob}`** en `complejos.tex` ≈ línea 311: el entorno de solución del triángulo equilátero está estructuralmente desanclado.
14. **Consistencia de títulos de "lección"**: `apintdobles.tex` y `inttriples.tex` tienen `\chapter{Lección X.Y: ...}`. Deben renombrarse al patrón de libro.
15. **`axis equal` faltante** en algunas figuras de circunferencias y cónicas en `vectoresrn.tex` y `complejos.tex`.

---

## RECOMENDACIÓN DE CÓMO PROCEDER

### Decisiones de arquitectura (ANTES de editar cualquier archivo)

**Debes resolverlas tú porque involucran contenido editorial:**

**Decisión A — Cap. 1 (Políticas):** ¿Un solo capítulo unificado de políticas para Cálculo + AL, o dos capítulos separados (uno por secuencia de cursos)? Si es libro único con 9 partes, un solo Cap. 1 tiene sentido; el contenido sería la intersección y el material específico de cada curso iría en apéndice.

**Decisión B — Caps. 19–22 (multivariable):** Propongo este esquema de reasignación:
- `limvariasvariables.tex` §1 → Cap. 19  
- `limvariasvariables.tex` §2 + `planostangentes.tex` → fusionados en Cap. 20  
- `gradientes.tex` §1 → Cap. 21  
- `gradientes.tex` §2 + `multiplicadoresintdobles.tex` §1 → Cap. 22  
- `multiplicadoresintdobles.tex` §2–3 → se mueve al Cap. 32  
¿Estás de acuerdo con este reagrupamiento?

**Decisión C — Caps. 32–34:** ¿La separación entre Cap. 33 (integrales de línea/superficie) y Cap. 34 (teoremas integrales) es: ¿Green = Cap. 34? Actualmente Green está en `integraleslineacampos.tex` §3 y Stokes/Gauss en `intsuperficies.tex` §4–5. Propongo mover todo Green + Stokes + Gauss a un Cap. 34 autónomo.

**Decisión D — Part VIII (EDOs):** ¿Escribir los 5 capítulos nuevos desde cero (alto esfuerzo), o priorizarlos como trabajo futuro y marcar la parte como "en construcción" en esta edición?

### Orden de trabajo sugerido (una vez resueltas las decisiones)

1. **Corrección crítica inmediata**: reparar el error del polinomio en `limites.tex` línea 921 y mover el `\begin{myproof}` en `complejos.tex` dentro del `\begin{prob}` correspondiente.

2. **Restructuración de archivos** (Caps. 19–22, 32–34): renombrar, dividir y fusionar según las Decisiones B y C. Esto es prerequisito para todo el trabajo posterior.

3. **Completar Cap. 10** (`intdefinida.tex`): añadir sección de problemas propuestos (objetivo: ≥ 20 problemas).

4. **Reformatear estilo** (por orden de urgencia en el libro):
   - Primero: `derivadas.tex` y `tecintegracion.tex` (Caps. 6 y 9 — columna vertebral del Cálculo I)
   - Luego: toda la rama de Álgebra Lineal matricial (Caps. 14–17)
   - Finalmente: la rama avanzada (Caps. 23–24)

5. **Crear Parte VIII (Caps. 27–31)**: capítulos de EDOs, desde cero.

6. **Completar Cap. 32**: añadir coordenadas cilíndricas y esféricas.

7. **Revisión final de TikZ** (no urgente): verificar `axis equal image` en figuras de circunferencias y revisar dominios de curvas polares.

### Qué atacar primero

**Si el objetivo inmediato es tener los caps. 6, 9 y 10 listos** (Cálculo I completo): concentrar esfuerzo en reformatear 130+ ejemplos de derivadas + tecintegracion + añadir problemas a intdefinida. Es trabajo mecánico de reformateo, estimado en alto volumen pero baja complejidad.

**Si el objetivo inmediato es tener la estructura de 9 partes legible**: resolver las Decisiones A–D y hacer la restructuración de archivos. Es trabajo de reorganización pura, sin crear contenido nuevo, pero debe hacerse antes de editar.

**Si el objetivo es máximo impacto visible por esfuerzo invertido**: Cap. 11 (apintegral) ya es el modelo perfecto. Replicar ese nivel de calidad exactamente en Caps. 9, 10 y 6 produce la Parte III completa en estilo coherente — 3 capítulos contiguos de alto valor pedagógico.

---

*Diagnóstico generado en sesión de lectura: ningún archivo .tex fue modificado.*

---

## ACTUALIZACIÓN POSTERIOR — fusión manual de banco de ejercicios antiguo

Después de este diagnóstico, se depuró un banco de ejercicios antiguo (225 problemas) y se fusionó manualmente, fuera de esta sesión de diagnóstico, dentro de los archivos de los Caps. 8 (`vectoresrn.tex`), 18 (`funvectoriales.tex`), 19-22 (`limvariasvariables.tex`, `gradientes.tex`, `multiplicadoresintdobles.tex`) y 32 (`apintdobles.tex`, `inttriples.tex`, `multiplicadoresintdobles.tex`).

**Queda desactualizado por esto:** los conteos de `prob` y `myproof` en las tablas de Paso 3 y Paso 6 para esos siete capítulos — hay más problemas de los que reportan las tablas. Algunos de los problemas fusionados tienen figura en pstricks, todavía sin convertir a TikZ, embebida dentro de esos mismos archivos.

**Sigue vigente sin cambios:** el inventario de archivos (Paso 1), el mapeo de archivos a capítulos (Paso 2), los conteos de `ex`/`def`/`thm`/`rem` y la cobertura de formato de 4 pasos — columna "ex con 4 pasos" de Paso 3 (la fusión agregó `prob`, no `ex`), la verificación de TikZ y matemática por muestreo (Pasos 4 y 5 — ningún ejemplo verificado ahí fue tocado por la fusión), y toda la lista priorizada de hallazgos, incluyendo la fragmentación estructural y el error matemático.

No se repitió el diagnóstico completo: la fusión solo agregó problemas a archivos ya identificados, sin cambiar la estructura de capítulos ni introducir los problemas estructurales que este diagnóstico ya había mapeado.

---

## ACTUALIZACIÓN — 2026-06-25: Resolución de decisiones arquitectónicas y limpieza de directorio

### Estado de las Decisiones A–D

| Decisión | Estado | Detalle |
|---|---|---|
| A — Cap. 1 Políticas | ✅ Resuelta (ya estaba hecha) | `politicas.tex` ya tenía §Contenido AL + §Contenido Cálculo + §Políticas clase. `politicasal.tex` movido a `_auxiliar/`. Maestro: un solo `\input{politicas}` en `\part{Álgebra Lineal}`. |
| B — Caps. 19–22 | ✅ Resuelta (ya estaba hecha) | Los 4 archivos ya tienen `\chapter` propio y contenido correcto: limvariasvariables→Cap.19, planostangentes→Cap.20, gradientes→Cap.21, multiplicadoresintdobles→Cap.22. Sin fragmentación. |
| C — Caps. 32–34 | ✅ Resuelta | `cap34_integrales_vectoriales.tex` partido en `cap33.tex` (797L, campos vectoriales e integrales de línea) y `cap34.tex` (1064L, integrales de superficie + Green + Divergencia + Stokes). Maestro actualizado con `\input{cap33}` + `\input{cap34}`. Original movido a `_auxiliar/`. |
| D — EDOs Caps. 27–31 | ✅ Resuelta | 5 capítulos creados e incorporados al maestro (sesión anterior). |

### Error de `limites.tex` (Prioridad 1 del diagnóstico)
- **Estado:** ✅ Ya corregido (sesión 2026-06-16). Polinomio actual: `p(x)=x^{11}+x-1` — correcto: p(0)=-1<0, p(1)=1>0 → IVT garantiza raíz en (0,1).

### Limpieza del directorio (2026-06-25)
Se creó la carpeta `_auxiliar/` con 43 archivos de trabajo ya no necesarios en raíz:
- 31 scripts Python de verificación/reformateo
- 5 backups `*_ORIGINAL.tex`
- `politicasal.tex`, `donde quedamos.txt`
- 3 borradores vectoriales: `camposconservativos.tex`, `integraleslineacampos.tex`, `intsuperficies.tex`
- 4 archivos Markdown de seguimiento (devueltos a raíz para consulta)

**Raíz limpia:** 34 archivos `.tex` fuente + maestro + `.bib` + imagen + artefactos compilación.

### Muestreo Ej/Teo V1–V3 completado (2026-06-25)
12 archivos muestreados (totalez 331 entornos, 70 revisados). 1 error encontrado y corregido:
- `multiplicadoresintdobles.tex` ~l.514: det(Hessiano orlado) = 6d²+d√2 → **corregido a 8d²** (verificado SymPy + NumPy).

### Corrección V1.3 confirmada (2026-06-25)
`multiplicadoresintdobles.tex` l.514: `= 6d^2+d\sqrt{2} > 0.` → `= 8d^2 > 0.` aplicada y verificada en archivo.

### Estado final
Todas las decisiones arquitectónicas A–D están resueltas. Muestreo Ej/Teo V1–V3 cerrado sin pendientes. Estructura de 34 capítulos completa y limpia. El documento compila con 724 páginas, 0 errores (estado al 2026-06-25). No hay tareas editoriales ni estructurales pendientes.
