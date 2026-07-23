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
**Estado:** Planificado (2026-07-23).

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

**Total: 4 frentes.** F10.01 es el único ejecutable de inmediato por nosotros;
se ejecuta al congelar el contenido.
