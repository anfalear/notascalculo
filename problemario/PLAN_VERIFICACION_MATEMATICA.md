# PLAN DE VERIFICACIÓN MATEMÁTICA — Problemario de Cálculo y Álgebra Lineal

Documento complementario a `PROMPT_CLAUDE_CODE.md` y `PROGRESO.md`. Este plan no reformatea ni reorganiza: su único objetivo es dejar verificado matemáticamente todo el contenido que la auditoría del 2026-06-19 identificó como no verificado o parcialmente verificado.

---

## 1. Objetivo

Llevar los 37 ítems del problemario al estado "matemáticamente revisado y verificado", entendiendo por esto el criterio operacional de la Sección 2. Al cierre de este plan, ningún problema del documento debe quedar sin al menos uno de los siguientes: (a) verificación explícita documentada, o (b) reporte explícito de por qué no se verificó (bloqueado, requiere decisión del autor, etc.).

## 2. Criterio operacional de "verificado"

Un problema se considera matemáticamente verificado cuando se cumplen las cinco condiciones:

1. El enunciado es autocontenido y resoluble sin ambigüedad (datos suficientes, notación clara, sin dependencias rotas a otros problemas).
2. La solución fue **re-derivada de forma independiente** — no solo leída y aceptada visualmente. Si ya existe una solución en el documento, se reproduce el cálculo desde cero y se compara contra lo escrito.
3. Si el problema no tenía solución previa (caso típico de los bancos fusionados con solo enunciado), se resuelve desde cero y se documenta.
4. Cualquier error encontrado se corrige con **justificación matemática explícita** en el reporte de la sesión (no "se ajustó", sino qué estaba mal y por qué la corrección es correcta).
5. El problema permanece en el documento. Aplica la regla de no eliminación ya establecida: si un problema parece redundante, repetido entre capítulos, o fuera de lugar, se reporta para que tú decidas — nunca se descarta unilateralmente durante la verificación.

No cuenta como verificación: confirmar que el entorno LaTeX compila, confirmar que el problema "se ve bien", o que el banco "parece sólido". Eso ya se hizo en las fases de reformateo y es exactamente lo que esta verificación tiene que ir más allá de.

## 3. Regla heredada de no eliminación

Se mantiene sin cambios el recordatorio permanente fijado el 2026-06-19: ningún ejemplo, problema, observación o definición existente puede eliminarse. Mover, fusionar o reordenar sí está permitido. Esto aplica también durante la verificación: si un problema resulta tener un error irreparable o es un duplicado exacto, se reporta — no se borra sin tu visto bueno.

## 4. Fases y orden de ejecución

El orden sigue el riesgo real detectado en la auditoría, no el orden de capítulos del libro.

### Fase V1 — Bancos con "sin verificar" explícito en el código (riesgo alto)
Estos son los únicos casos donde el propio archivo admite, en un comentario, que el contenido no fue revisado. Es el riesgo más concreto porque ya está señalizado y nadie lo cerró.

| Ítem | Archivo | Capítulo | Alcance |
|---|---|---|---|
| V1.1 | funvectoriales.tex | 18 | Resolver primero la duplicación estructural (dos `\section{Problemas propuestos}`) y luego verificar los 11 problemas del banco |
| V1.2 | gradientes.tex | 21 | 17 problemas del banco |
| V1.3a | multiplicadoresintdobles.tex | 22 | Primeros 11 problemas del banco |
| V1.3b | multiplicadoresintdobles.tex | 22 | Últimos 11 problemas del banco |
| V1.4 | limvariasvariables.tex | 19 | 16 problemas del banco |
| V1.5 | planostangentes.tex | 20 | 9 problemas del banco |

### Fase V2 — Contenido nuevo sin verificación independiente
Contenido que no viene de un banco preexistente sino que se creó durante el reformateo. Nadie lo ha verificado todavía bajo ningún criterio.

| Ítem | Archivo | Capítulo | Alcance |
|---|---|---|---|
| V2.1 | intdefinida.tex | 10 | 15 problemas creados desde cero |
| V2.2 | apderivadas.tex | 7 | 7 ejemplos con pasos nuevos + 12 ejemplos preexistentes (ninguno de los 19 tiene verificación documentada) |
| V2.3 | inttriples.tex | 33 | Sección "Coordenadas esféricas", 2 ejemplos nuevos |

### Fase V3 — Bancos fusionados pendientes de Fase 1
Bancos que entraron a capítulos ya tocados en Fase 1 pero sin verificación completa, o capítulos donde la fusión no dejó comentarios de trazabilidad.

| Ítem | Archivo | Capítulo | Alcance |
|---|---|---|---|
| V3.1 | complejos.tex | 3 | 24 problemas del banco |
| V3.2 | vectoresrn.tex | 8 | 23 problemas orgánicos (los 5 del banco ya se verificaron en Fase 1) |
| V3.3 | prodinterno.tex | 17 | 7 problemas computacionales |
| V3.4 | apintdobles.tex | 32 | 11 problemas (sin marcadores de trazabilidad — se verifican todos) |
| V3.5 | cap31_Transformada de Laplace.tex | 31 | 21 problemas, excluyendo el ya corregido (parámetro b duplicado) |

### Fase V4 — Capítulos solo reformateados (contenido del documento original): MUESTREO, no verificación completa

Riesgo bajo: el contenido matemático es el del documento original, no se tocó en el reformateo. Por volumen (289 de 486 problemas, 59.5% del total) y bajo riesgo, esta fase usa **muestreo sistemático** en vez del protocolo de verificación completa de las Fases V1-V3.

**Regla de tamaño de muestra:** si el archivo tiene 5 problemas o menos, se verifican todos. Si tiene más de 5, la muestra es `max(5, ceil(0.25 × n))`.

**Regla de selección:** sistemática, no al azar y no los primeros N. Se divide el archivo en tantos segmentos iguales como el tamaño de la muestra y se toma un problema de cada segmento (posición `round(n/muestra × k)` para `k = 1...muestra`). Esto evita el sesgo de que los primeros problemas de un capítulo suelen ser los más simples.

**Regla de escalación:** si el muestreo de un archivo encuentra al menos un error matemático, ese archivo escala a verificación completa (100%, protocolo de Sección 5) en la siguiente sesión. Se reclasifica de Tipo `Muestreo` a Tipo `Completo` en `PROGRESO_VERIFICACION.md`.

| Ítem | Archivo | Capítulo | # problemas | Muestra |
|---|---|---|---|---|
| V4.1 | derivadas.tex | 6 | 37 | 10 |
| V4.2 | tecintegracion.tex | 9 | 4 | 4 (100%, archivo pequeño) |
| V4.3 | funciones.tex | 4 | 17 | 5 |
| V4.4 | matrices.tex | 14 | 25 | 7 |
| V4.5 | sel.tex | 15 | 30 | 8 |
| V4.6 | espaciosvectoriales.tex | 16 | 36 | 9 |
| V4.7 | vvpropios.tex | 23 | 14 | 5 |
| V4.8 | translineales.tex | 24 | 22 | 6 |
| V4.9 | cap34_integrales_vectoriales.tex | 34 | 29 | 8 |
| V4.10a | cap27_EDOs primer orden.tex | 27 | 19 | 5 |
| V4.10b | cap28_EDOs orden n.tex | 28 | 20 | 5 |
| V4.10c | cap29_Sistemas de EDOs.tex | 29 | 20 | 5 |
| V4.10d | cap30_Sol EDOs Series Potencias.tex | 30 | 16 | 5 |

**Subtotal Fase V4: 82 de 289 problemas verificados directamente (28.4%), con escalación automática a 100% por archivo si aparece un error.**

**Nota sobre el alcance final del plan:** con este cambio, el problemario no terminará con "486 de 486 verificados". Terminará con 197 problemas (Fases V1-V3) verificados al 100%, más 82 problemas de V4 verificados como validación muestral. La forma correcta de describir el resultado final es "verificación completa en bancos fusionados y contenido nuevo; muestreo sin errores en contenido heredado del documento original" — no "100% del problemario verificado". Si esa distinción no es aceptable para el uso que le vas a dar al problemario (por ejemplo, si necesitas poder afirmar verificación completa sin matices), avísalo antes de ejecutar V4 y se revierte a verificación completa de los 289.

## 5. Protocolo de trabajo por ítem (una sesión = un ítem)

1. Abrir el archivo, contar problemas con grep (`\begin{prob}...\end{prob}`) y confirmar contra la tabla de este plan.
2. Para cada problema: re-derivar la solución de forma independiente, sin mirar la solución existente primero si la hay — luego comparar.
3. Si hay discrepancia: documentar qué estaba mal, por qué, y la corrección con justificación matemática explícita.
4. Si el problema no tenía solución: resolverlo y agregarlo en el formato `myproof` que usa el resto del capítulo.
5. Si un problema parece redundante o fuera de lugar: NO eliminar. Anotar en la fila de `PROGRESO_VERIFICACION.md` bajo "Notas" para que decidas después.
6. Cerrar el ítem actualizando `PROGRESO_VERIFICACION.md`: estado, fecha, # verificados, errores encontrados/corregidos, notas.
7. Un ítem no se marca "Completo" si quedó algún problema sin re-derivar — se marca "En progreso" y se retoma en la siguiente sesión desde el punto exacto donde quedó (anotar el número de problema en "Notas").

## 5b. Protocolo atómico y muestreo de ejemplos/teoremas (vigente desde 2026-06-22)

A partir del ítem V3.5 y todos los ítems V4, se aplican las siguientes reglas adicionales al protocolo de la Sección 5:

**Protocolo atómico:** nunca reescribir un archivo completo. Verificar en **lotes de 5 problemas** máximo por iteración. Si hay errores: entregar solo el bloque `\begin{myproof}…\end{myproof}` corregido (o el `\begin{example}…\end{example}` corregido), con instrucciones exactas de búsqueda y reemplazo. Prohibido entregar el archivo entero.

**Muestreo de ejemplos/teoremas por ítem:** en cada ítem que se verifique (V3.5, V4.1…V4.10d), además de los `\begin{prob}`, se muestrean sistemáticamente los entornos `\begin{example}`, `\begin{theorem}`, `\begin{lemma}`, `\begin{corollary}`, `\begin{definition}`, `\begin{proof}` y `\begin{myproof}` (cuando no estén dentro de un `prob`).

- Si el archivo tiene menos de 5 entornos de estos tipos → se verifican **todos**.
- Si tiene 5 o más → muestra del **20%** (mínimo 2), seleccionada con `round(n/muestra × k)` para k=1…muestra.
- Veredicto: `✅ correcto` o `❌ error: …` + parche si procede.
- El muestreo se realiza **una sola vez por ítem** (al inicio del primer lote), no se repite en lotes posteriores.
- En el resumen de cada ítem se indica: "Ej/Teo muestreados: X/Y revisados, Z correctos."

## 5c. Protocolo de lectura de archivos .tex (vigente desde 2026-06-24)

Lección aprendida en V4.4 (`matrices.tex`): leer un archivo largo de una sola vez consume todo el contexto disponible y obliga a procesar más de 3 000 líneas antes de poder verificar un solo problema. Regla vinculante a partir de V4.5:

**Regla de lectura:** leer el archivo en bloques de **máximo 400 líneas** por llamada a Read. Nunca leer el archivo completo de una vez.

**Flujo obligatorio al iniciar cualquier ítem V4 (o cualquier ítem futuro):**

1. **Grep de `\begin{prob}`** en el archivo → obtener la lista de números de línea donde empieza cada problema. Esto cuesta solo una llamada y da el mapa completo del archivo.
2. **Calcular los números de problema de la muestra** (según la regla de selección de la Sección 4) e identificar los rangos de líneas correspondientes.
3. **Leer solo los rangos necesarios**: para cada lote de 5 problemas, hacer llamadas Read con `offset` y `limit` apuntando a las zonas de interés (típicamente 80–150 líneas por problema). No leer zonas de teoría entre problemas salvo que el muestreo de Ej/Teo lo requiera.
4. **Muestreo de Ej/Teo** (Sección 5b): calcular las posiciones de los entornos no-prob con un segundo grep (`\begin{example}`, `\begin{theorem}`, etc.) y leer solo esos bloques puntuales. No releer el archivo completo para este paso.
5. **Scripts de verificación**: siempre escribir un archivo `.py` con Write y ejecutarlo con PowerShell. Nunca usar `python -c "..."` (límite de ~965 bytes en PowerShell).

**Tamaño de lote:** máximo 5 problemas por iteración (sin cambio respecto a 5b). Con la regla de lectura de 400 líneas, esto equivale a leer entre 1 y 3 bloques de Read por lote, dependiendo de la densidad del archivo.

**Correcciones atómicas:** si un lote produce errores, entregar solo el bloque corregido con instrucciones exactas de búsqueda y reemplazo. No reescribir el archivo completo (sin cambio respecto a 5b).

## 6. Orden de continuación (actualizado 2026-06-22)

Estado al cierre de esta actualización: 11/28 ítems completos (V1 y V2 cerradas al 100%, V3.1 y V3.2 cerradas). Continuar estrictamente en este orden, sin saltar pasos:

1. **Aplicar las dos correcciones decididas en V1.2** (`gradientes.tex`) — ver `PROGRESO_VERIFICACION.md`, sección "Decisiones del autor — resueltas, pendientes de aplicar en el .tex". Esto cierra V1.2 al 100% sin asteriscos.
2. **V3.3** — prodinterno.tex (7 problemas)
3. **V3.4** — apintdobles.tex (11 problemas)
4. **V3.5** — cap31_Transformada de Laplace.tex (21 problemas)
5. **V4.1 a V4.10d** — los 13 ítems de muestreo (82 problemas), en el orden de la tabla de la Fase V4
6. **Cierre de este plan**: actualizar el resumen final de `PROGRESO_VERIFICACION.md` con el conteo total real (197 completos + 82 muestreo, más cualquier escalación V4→V1 que haya ocurrido)
7. **Recién ahí**, retomar `DIAGNOSTICO_PROBLEMARIO.md`: Decisiones de arquitectura A-D (Cap. 1 unificado, reasignación Caps. 19-22, frontera Caps. 32-34, EDOs). Decisión expresa del autor (2026-06-20): no se tocan antes de cerrar V4.
8. Diseñar y ejecutar la reorganización según los parámetros de Apostol, con base en las decisiones A-D ya tomadas.
9. Diseñar la tabla de progreso y ejecutar la Fase de labeling (Sección 7) — solo tiene sentido después de que la estructura de capítulos esté fija, para no etiquetar `capNN` que luego se mueve o se fusiona.

**Estado al 2026-06-22:** V3.3 cerrado (correcciones del autor). V3.5 en progreso (5/21 probs + muestreo ej/teo completado). Continuar: lotes 2–5 de V3.5, luego V4.1…V4.10d.

**Estado al 2026-06-24 (actualización 1):** V4.1–V4.7 cerrados. V4.4 escaló (matrices.tex, 11 errores). V4.5 escaló (sel.tex, 4 errores). V4.6 escaló (espaciosvectoriales.tex, 8 errores). V4.7 escaló (vvpropios.tex, 6 errores — Probs 6c, 11, 12b en muestreo anterior + Prob1a mult.geom., Prob9 eigenvalores completos, Prob12c pol.car.). Continuar V4.8 (translineales.tex, muestreo, 22 probs).

**Estado al 2026-06-24 (actualización 2):** V4.8 cerrado — translineales.tex escaló (3 errores: det Env33 -11→-10 corregido; kernel Prob2k (1,-1,1)→(3,-3,2) corregido; Env24 hipótesis teorema débil + Prob12 def T constante → 2 decisiones pendientes autor). 22/22 probs y 38 entornos Ej/Teo verificados al 100%. Continuar V4.9 (cap34_integrales_vectoriales.tex, muestreo, 29 probs, muestra 8).

**Estado al 2026-06-24 (actualización 3):** V4.9 cerrado — cap34_integrales_vectoriales.tex escaló (muestreo halló error en Ej/Teo 24). 2 errores corregidos: (1) example/1389 centro de masa primer octante, esfera con ρ=z: simetría falsa x̄=ȳ=z̄=2R/3 → corregido a (4R/(3π), 4R/(3π), 2R/3), añadido cálculo M_yz; (2) example/1620 aplicación tma. divergencia, F=(y,xz,z²): ∂(xz)/∂y=x era erróneo→0, ∇·F=x+2z→2z (respuesta π/3 coincidía por simetría). 29/29 probs propuestos verificados. 33/33 entornos Ej/Teo verificados. Continuar V4.10a (cap27_EDOs primer orden.tex).

**Estado al 2026-06-24 (actualización 4):** V4.10c cerrado — cap29_Sistemas de EDOs.tex escaló (1 error, Prob4: método de eliminación x'' - 4x' - 4x = 0 → x'' - 4x' + 4x = 0; la matriz tiene eigenvalor doble λ=2 verificado por det(A-λI)=(λ-2)², raíz doble da x=(c₁+c₂t)e^{2t} y no exponenciales con 2±2√2). 20/20 probs y 4/17 Ej/Teo muestreados, todos los demás correctos. Continuar V4.10d (cap30_Sol EDOs Series Potencias.tex, muestreo, 16 probs, muestra 5).

**Estado al 2026-06-24 (CIERRE DEL PLAN):** V4.10d cerrado — cap30_Sol EDOs Series Potencias.tex sin errores en muestreo (probs 3,6,10,13,16 correctos; Ej/Teo #4,8,12,16 correctos). Sin escalación. Observación fuera de muestra: Prob14 (Hermite n=1) — paso intermedio $y=a_0(1-2x^2)$ incorrecto (no satisface la ODE); documento se autointerroga pero deja sin resolver. Pendiente decisión del autor. **27/27 ítems del plan completados.** Resumen: 197 probs (V1+V2+V3) verificados al 100%; 82 probs (V4) por muestreo sistemático. 5 ítems V4 escalaron a Completo por error (V4.4 matrices, V4.5 sel, V4.6 espaciosvectoriales, V4.7 vvpropios, V4.8 translineales, V4.9 cap34, V4.10b cap28, V4.10c cap29).

**Estado al 2026-06-25 (CIERRE TOTAL):** Decisiones arquitectónicas A–D resueltas (ver DIAGNOSTICO_PROBLEMARIO.md § ACTUALIZACIÓN 2026-06-25). Muestreo Ej/Teo V1–V3 completado y cerrado: 12/12 ítems, 1 error (V1.3) corregido y confirmado en archivo. Corrección V1.3: `multiplicadoresintdobles.tex` l.514 `= 6d^2+d\sqrt{2} > 0.` → `= 8d^2 > 0.` Documento compila limpio: 724 páginas, 0 errores. **No hay pendientes de verificación ni arquitectónicos.** Obs. abierta sin bloqueo: Prob14 cap30 (Hermite n=1) — para decisión del autor en sesión futura.

**Resuelto, sin acción pendiente:** el `.bbl` roto (36 "Citation undefined") ya fue corregido por el autor recompilando BibTeX — no es parte de este plan.

## 7. Fase de labeling y reorganización Apostol (no iniciada — prerequisito: Sección 6, pasos 7-8 completos)

**Cambio de secuencia (2026-06-20):** originalmente esta fase se planeaba justo después del cierre de verificación (Fases V1-V4). Decisión del autor: primero se resuelven las decisiones de arquitectura de `DIAGNOSTICO_PROBLEMARIO.md` (A-D) y se ejecuta la reorganización según Apostol — recién con la estructura de capítulos ya estable se etiqueta. Etiquetar antes sería trabajo desechable si un capítulo se fusiona o se parte después.

**Alcance:** `\label` en todos los entornos de resultado matemático — teoremas, definiciones, proposiciones, lemas, corolarios — para poder citarlos con `\ref` entre capítulos.

**Convención de nombres aprobada:**
```
tipo:capNN:slug-corto
```
- `tipo` ∈ `{thm, def, prop, lem, cor}`
- `capNN` — número de capítulo a dos dígitos, basado en la numeración **final** post-reorganización
- `slug-corto` — 2 a 4 palabras kebab-case, sin tildes ni ñ (á→a, é→e, í→i, ó→o, ú→u, ñ→n)

Ejemplos: `thm:cap08:reflexion-rayo`, `def:cap02:valor-absoluto`, `prop:cap16:subespacio-vectorial`, `lem:cap25:criterio-raabe`, `cor:cap13:area-polar`.

**Regla de colisión:** sufijo numérico si dos resultados del mismo capítulo generan el mismo slug (`-2`, `-3`...).

**Primer paso al iniciar esta fase (no hacer antes):** grep de `\begin{` en los capítulos ya reorganizados para confirmar los nombres reales de los entornos (`theorem`, `definition`, `proposition`, o custom como `mydef`/`teo`) antes de tocar cualquier archivo. No se asume que coinciden con los nombres genéricos usados arriba.

Esta fase no tiene ítems ni tabla de progreso todavía — se diseña cuando la reorganización Apostol esté cerrada.

## 8. Qué no cubre este plan

- No vuelve a tocar formato (`Paso N`, `\boxed{}`, títulos) — eso ya está cerrado según PROGRESO.md.
- No resuelve por sí mismo la decisión de qué hacer con contenido redundante detectado — eso queda para ti.
- No incluye los 7 ítems ya verificados en Fase 1 (ver lista en PROGRESO_VERIFICACION.md), salvo las excepciones parciales explícitas (V3.2 y V3.5).
- No incluye las decisiones de arquitectura A-D ni la reorganización Apostol — eso vive en `DIAGNOSTICO_PROBLEMARIO.md` y se retoma según el orden de la Sección 6.
- **Pendiente: verificación muestral de ejemplos/teoremas en capítulos ya cerrados (V1, V2, V3.1, V3.2, V3.3, V3.4).** Estos capítulos se verificaron solo en sus problemas (`\begin{prob}`) antes de que se estableciera el protocolo de muestreo de ejemplos/teoremas (Sección 5b, vigente desde 2026-06-22). Si al final del plan sobra tiempo/tokens, se revisarán; en caso contrario, quedan documentados como **verificación parcial**: problemas al 100%, entornos no-problema sin revisar.
