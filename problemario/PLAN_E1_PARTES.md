# PLAN_E1_PARTES.md — Prosas introductorias de las 9 partes

**Inicio:** 2026-07-16 — **COMPLETADO el mismo día** (el autor aprobó los 9 borradores e instruyó la inserción inmediata, dispensando el prerequisito)
**Prerequisito:** F9AL.40 y F9AL.41 completados (cierre de F9 Álgebra Lineal) — *dispensado por el autor el 2026-07-16*
**Objetivo:** insertar una prosa introductoria de 4–6 líneas después de cada `\part{}` en `anfalearNotasCalculo.tex`, antes del primer `\input` de cada parte.
**Compilador:** LuaLaTeX.
**Regla:** cada ítem ≤ 10 líneas. El contenido de cada prosa lo redacta el autor externamente y se entrega como texto listo para insertar.

---

## Ítems

### E1.PR1 — Parte I: Fundamentos y Cálculo diferencial de una variable
- Archivo destino: `anfalearNotasCalculo.tex`
- Inserción: bloque `\begin{quote}...\end{quote}` tras el `\part{}` correspondiente
- Líneas estimadas: 6–8
- Estado: Pendiente
- Fecha: —
- Notas: —

### E1.PR2 — Parte II: Vectores y geometría analítica
- Archivo destino: `anfalearNotasCalculo.tex`
- Inserción: bloque `\begin{quote}...\end{quote}` tras el `\part{}` correspondiente
- Líneas estimadas: 6–8
- Estado: Pendiente
- Fecha: —
- Notas: —

### E1.PR3 — Parte III: Cálculo integral de una variable
- Archivo destino: `anfalearNotasCalculo.tex`
- Inserción: bloque `\begin{quote}...\end{quote}` tras el `\part{}` correspondiente
- Líneas estimadas: 6–8
- Estado: Pendiente
- Fecha: —
- Notas: —

### E1.PR4 — Parte IV: Álgebra Lineal matricial
- Archivo destino: `anfalearNotasCalculo.tex`
- Inserción: bloque `\begin{quote}...\end{quote}` tras el `\part{}` correspondiente
- Líneas estimadas: 6–8
- Estado: Pendiente
- Fecha: —
- Notas: —

### E1.PR5 — Parte V: Cálculo diferencial en varias variables
- Archivo destino: `anfalearNotasCalculo.tex`
- Inserción: bloque `\begin{quote}...\end{quote}` tras el `\part{}` correspondiente
- Líneas estimadas: 6–8
- Estado: Pendiente
- Fecha: —
- Notas: —

### E1.PR6 — Parte VI: Álgebra Lineal avanzada
- Archivo destino: `anfalearNotasCalculo.tex`
- Inserción: bloque `\begin{quote}...\end{quote}` tras el `\part{}` correspondiente
- Líneas estimadas: 6–8
- Estado: Pendiente
- Fecha: —
- Notas: —

### E1.PR7 — Parte VII: Sucesiones y Series
- Archivo destino: `anfalearNotasCalculo.tex`
- Inserción: bloque `\begin{quote}...\end{quote}` tras el `\part{}` correspondiente
- Líneas estimadas: 6–8
- Estado: Pendiente
- Fecha: —
- Notas: —

### E1.PR8 — Parte VIII: Ecuaciones Diferenciales Ordinarias
- Archivo destino: `anfalearNotasCalculo.tex`
- Inserción: bloque `\begin{quote}...\end{quote}` tras el `\part{}` correspondiente
- Líneas estimadas: 6–8
- Estado: Pendiente
- Fecha: —
- Notas: —

### E1.PR9 — Parte IX: Cálculo integral en varias variables
- Archivo destino: `anfalearNotasCalculo.tex`
- Inserción: bloque `\begin{quote}...\end{quote}` tras el `\part{}` correspondiente
- Líneas estimadas: 6–8
- Estado: Pendiente
- Fecha: —
- Notas: —

---

## Registro de progreso

| Ítem | Parte | Intervención | Estado | Fecha | Notas |
|---|---|---|---|---|---|
| E1.PR1 | I — Fundamentos y Cálculo diferencial de una variable | Prosa introductoria tras `\part` | Completo | 2026-07-16 | Borrador aprobado por el autor sin cambios |
| E1.PR2 | II — Vectores y geometría analítica | Prosa introductoria tras `\part` | Completo | 2026-07-16 | Borrador aprobado por el autor sin cambios |
| E1.PR3 | III — Cálculo integral de una variable | Prosa introductoria tras `\part` | Completo | 2026-07-16 | Borrador aprobado por el autor sin cambios |
| E1.PR4 | IV — Álgebra Lineal matricial | Prosa introductoria tras `\part` | Completo | 2026-07-16 | Borrador aprobado por el autor sin cambios |
| E1.PR5 | V — Cálculo diferencial en varias variables | Prosa introductoria tras `\part` | Completo | 2026-07-16 | Borrador aprobado por el autor sin cambios |
| E1.PR6 | VI — Álgebra Lineal avanzada | Prosa introductoria tras `\part` | Completo | 2026-07-16 | Borrador aprobado por el autor sin cambios |
| E1.PR7 | VII — Sucesiones y Series | Prosa introductoria tras `\part` | Completo | 2026-07-16 | Borrador aprobado por el autor sin cambios |
| E1.PR8 | VIII — Ecuaciones Diferenciales Ordinarias | Prosa introductoria tras `\part` | Completo | 2026-07-16 | Borrador aprobado; rayas escritas `---` |
| E1.PR9 | IX — Cálculo integral en varias variables | Prosa introductoria tras `\part` | Completo | 2026-07-16 | Borrador aprobado; rayas escritas `---` |

**Notas de ejecución (2026-07-16):**
- Formato insertado: `\noindent{\itshape ...}\bigskip` (el formato de los borradores aprobados), no `\begin{quote}...\end{quote}` — la inconsistencia entre ambas especificaciones se resolvió a favor del texto aprobado.
- Compilación: 2 pasadas LuaLaTeX, 0 errores. PDF: **802 páginas** (+18 respecto a 784).
- **Comportamiento de página (resuelto 2026-07-16):** inicialmente la clase `book` expulsaba página tras el título de `\part` y cada prosa quedaba sola en la página siguiente (+18 pp, PDF 802). El autor eligió la opción (ii): se añadió `\titleclass{\part}{top}` + `\titlespacing*{\part}{0pt}{0pt}{25pt}` al preámbulo (tras el `\titleformat` de part), con lo que **la prosa comparte página con el título de la parte**. PDF final: **784 pp, 0 errores** (verificado visualmente en Parte VI, p. 477).

---

## Notas de protocolo

- El contenido de cada prosa lo entrega el autor antes de ejecutar el ítem.
- Compilar con LuaLaTeX después de cada ítem y confirmar 0 errores.
- Nada se genera automáticamente — esperar texto del autor.
