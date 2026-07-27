# Fase 10 — Preparación editorial

Frente de trabajo posterior al cierre del contenido (Fases 1–9). Reúne lo que
separa un **manuscrito completo** de un **texto publicable**. Se abre como
registro ahora, pero su ejecución se recomienda **después de congelar el
contenido** (cierre de F9-EDOs), porque varios ítems (señaladamente el índice
analítico) siembran marcas por todo el libro y rehacerlas tras mover secciones
es trabajo perdido.

## Alcance de la publicación (decisión pendiente del autor)

El alcance condiciona qué ítems son obligatorios:

- **Apuntes / PDF para estudiantes:** F10.01 (índice analítico) + una pasada de
  erratas. Lo demás es opcional.
- **Libro formal con ISBN a la venta:** además, F10.02 (atribución/derechos —
  bloqueante y no resoluble solo compilando), F10.03 (revisión externa) y
  F10.04 (producción).

---

## Ítems

### F10.01 — Índice analítico (de términos)
**Resoluble por nosotros: SÍ.** No depende de terceros ni de permisos.
**Acción:**
1. Activar `imakeidx` en el preámbulo (`\usepackage{imakeidx}` +
   `\makeindex[intoc]`); añadir `\printindex` al final del maestro.
2. Sembrar `\index{término}` en los puntos de *definición* de cada concepto
   central (no en cada aparición): definiciones, teoremas con nombre, métodos.
   Estrategia por lotes, un bloque temático por sesión (AL, cálculo 1 var.,
   varias var., series, EDOs), reutilizando los `\begin{definition}` y
   `\begin{theorem}[...]` ya existentes como anclas naturales.
3. Subentradas donde aplique (`\index{límite!de una sucesión}`).
4. Compilar con la secuencia `lualatex → makeindex → lualatex`.
**Criterio de cierre:** índice alfabético al final del libro con las entradas
de todos los conceptos centrales; sin entradas duplicadas por variante
ortográfica; compilación limpia.
**Momento recomendado:** tras cerrar F9-EDOs (contenido congelado).
**Estado:** COMPLETO (2026-07-27). Ejecutado en 8 lotes.

**Ejecución por lotes:**

| # | Lote | Archivos | Entradas |
|---|------|----------|----------|
| 1 | Álgebra lineal | matrices, sel, espaciosvectoriales, prodinterno, vvpropios, translineales, complejos | 123 |
| 2 | Cálculo 1 var. — diferencial | preliminares, funciones, limites, derivadas, apderivadas | 63 |
| 3 | Cálculo 1 var. — integral | tecintegracion, intdefinida, apintegral, impropias, polares | 53 |
| 4 | Sucesiones y series | sucesionesyseries, sucesionesyseriesfunciones | 41 |
| 5 | Cálculo en varias variables | vectoresrn, limvariasvariables, planostangentes, gradientes, multiplicadoresintdobles, funvectoriales | 64 |
| 6 | EDOs | cap27, cap28, cap29, cap30, cap31 | 37 |
| 7 | Integrales avanzadas | apintdobles, inttriples, cap33, cap34 | 40 |
| 8 | Cierre y auditoría | — | +3 |

**Total: 424 entradas `\index{}` en 34 archivos, 197 cabeceras de primer nivel.**

**Convenciones fijadas:**
- El `\index{}` va pegado al constructo de apertura del entorno, tras el
  argumento opcional y el `\label` si lo hay:
  `\begin{theorem}[Teorema de Green]\index{Green, teorema de}`.
- Solo en el punto de *definición* del concepto (definiciones, teoremas con
  nombre, métodos), nunca en cada aparición.
- **Claves de ordenación `sinacentos@conacentos` en toda clave con tilde.**
  `makeindex` ordena por bytes UTF-8, así que sin ellas los acentos rompen el
  alfabeto: `ángulo` y `área` caían **después de `wronskiano`**, `límite`
  después de `longitud de arco`, y `mínimos cuadrados` después de
  `multiplicadores de Lagrange`. Detectado en la verificación visual, no por
  la compilación (makeindex no avisa).
  **Regla crítica:** la clave de orden debe aplicarse *uniformemente* — si una
  misma cabecera aparece con clave en un archivo y sin ella en otro, el índice
  la parte en dos entradas distintas. Se aplican por script sobre todos los
  `.tex` a la vez y se verifican con `check_sortkeys.py`.
- Subentradas con `!` (hasta 3 niveles, p. ej. `matriz!invertible!caracterización`).
- Los cruces entre capítulos fusionan página bajo la misma clave (p. ej.
  «Euler, fórmula de» combina `prodinterno` y `complejos`; «Weierstrass»
  combina apderivadas, multiplicadoresintdobles y ssfunciones).

**Auditoría de cierre (lote 8) — unificaciones aplicadas:**
- `Wronskiano` → `wronskiano` (espaciosvectoriales), para fusionar con cap28.
- `extremos absolutos` / `extremos locales` (+ sus dos criterios) → subentradas
  de una única cabecera `extremos`, junto con las de varias variables.
- `Weierstrass, teorema del valor extremo de` → `Weierstrass!teorema del valor
  extremo`, que fusiona el caso de una y varias variables.
- `teorema del valor medio` → `teorema del valor medio!de Lagrange`, para
  convivir con las dos subentradas de integrales.
- `plano tangente`: la noción se introduce en prosa (no hay entorno), así que
  el `\index{}` va anclado al `\textbf{plano tangente}` de `planostangentes`.
- `integral de superficie!de un campo vectorial` añadido junto a `flujo`.
- `infinitesimales equivalentes` → `infinitesimales!equivalentes` (limites y
  sucesionesyseries), para no dejar dos cabeceras contiguas casi idénticas.
- Resultado: **0 variantes ortográficas**, 0 cabeceras partidas, 0 llaves
  desbalanceadas, 0 claves con caracteres especiales de makeindex sin escapar.

**Fragmentaciones NO corregidas (decisión deliberada):** pares como
`serie` / `serie de Taylor`, `derivada` / `derivada parcial`,
`divergencia` / `divergencia, teorema de la`, `función` / `función vectorial`
son conceptos distintos y alfabetizan contiguos; separarlos es práctica
estándar de indización y facilita la búsqueda.

**Secuencia de compilación:** `lualatex` ×2 → `makeindex anfalearNotasCalculo.idx`
→ `lualatex`. `imakeidx` está sin `-shell-escape`, así que **no** ejecuta
makeindex automáticamente: hay que invocarlo a mano.

**Scripts** (scratchpad): `seed_index.py` (siembra por archivo+línea),
`audit_index.py` (variantes, duplicados, cabeceras huérfanas),
`fix_index.py` (unificaciones del cierre).

### F10.02 — Atribución y derechos de problemas de terceros
**Resoluble por nosotros: PARCIAL (requiere decisión y posiblemente permisos).**
Hay problemas tomados de Spivak, Apostol, Larson, Putnam y Andreescu
(detectados en `apintegral`, `limites`, `intdefinida`, `limvariasvariables`,
`tecintegracion`). Para publicación formal: reescribirlos como originales, o
citar y gestionar permisos. Para uso educativo interno con cita, es defendible.
**Estado:** Registrado (bloqueante para venta con ISBN).

### F10.03 — Corrección de erratas y revisión externa
Lectura de prueba completa del libro (830+ pp). La matemática está muy
verificada (SymPy), pero a esta escala siempre quedan erratas de redacción,
signo y referencias cruzadas. Idealmente con revisor externo.
**Estado:** Registrado.

### F10.04 — Producción
Corrección de estilo del español, diseño de cubierta, revisión tipográfica
profesional, ISBN.
**Estado:** Registrado.

---

**Total: 4 frentes.** F10.01 **cerrado el 2026-07-27**. Los tres restantes
(F10.02 atribución, F10.03 erratas, F10.04 producción) dependen de decisiones
del autor o de terceros, no de compilar.
