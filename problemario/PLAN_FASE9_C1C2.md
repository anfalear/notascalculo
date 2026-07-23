# PLAN_FASE9_C1C2.md — Criterio Apostol para Cálculo I y II

**Inicio:** Pendiente (plan generado 2026-07-06)
**Objetivo:** Aplicar el criterio Apostol operativo (R1–R3) a los 11 capítulos de Cálculo I/II (`funciones`, `limites`, `derivadas`, `apderivadas`, `tecintegracion`, `intdefinida`, `apintegral`, `impropias`, `polares`, `sucesionesyseries`, `sucesionesyseriesfunciones`) + bloque auxiliar `preliminares` (§Semana 1, con nota).
**Compilador:** LuaLaTeX. Todas las figuras en TikZ puro o pgfplots — sin pstricks, sin Asymptote.
**Regla de tamaño:** cada ítem ≤ 300 líneas de código nuevo o modificado.
**Regla de contenido:** nada se elimina sin decisión explícita del autor.

---

## Criterio Apostol operativo — C1/C2

**R1-C1 — Orden canónico dentro de cada capítulo:**
párrafo introductorio → definición → figura geométrica → teorema → prueba/esquema → ejemplos (4 pasos + `\boxed{}`) → `\section{Problemas propuestos}`.

**Adaptación propia de C1/C2:** en Cálculo la motivación geométrica frecuentemente **precede** a la definición (secante→tangente antes de la derivada; rectángulos de Riemann antes de la integral; suma parcial antes de la serie). El orden `figura motivadora → definición → teorema` es una variante válida de R1 en este bloque y **no se registra como inversión**. Lo que sí es inversión: teoremas usados antes de enunciarse, o ejemplos que usan técnicas de secciones posteriores.

**R2-C1/C2 — Figura obligatoria (tipos apropiados):**
| Concepto | Figura |
|---|---|
| Límite ε-δ | Banda ε en y, entorno δ en x, punto excluido — TikZ 2D |
| Discontinuidades | Removible / salto / esencial (punto lleno-vacío, salto, oscilación) |
| Derivada | Secante → tangente (límite geométrico); zonas de crecimiento; concavidad; TVM secante ∥ tangente |
| Integral | Rectángulos de Riemann con partición; TFC como área acumulada A(x); regiones fillbetween |
| Técnicas | Triángulos de referencia para sustitución trigonométrica (3 casos) |
| Impropias | Región no acotada que "crece" hacia ∞ con límite de área |
| Paramétricas/polares | Curvas con `axis equal image` — sin excepción |
| Sucesiones/series | Puntos sobre la recta acercándose a L; rectángulos 1/2ⁿ de la geométrica; banda ε de convergencia uniforme; radio de convergencia sobre la recta |

**R3-C1/C2 — Nivel de demostración:**
| Tipo | Tratamiento |
|---|---|
| Centrales: ε-δ de límites básicos, sándwich, TVI, TVM, TFC1/TFC2, unicidad del límite, criterio de comparación y razón | Demostración completa o esquema con pasos clave (mayoría ya presentes — auditar, no reescribir) |
| Operacionales: reglas de derivación, L'Hôpital, criterios de convergencia avanzados (Raabe, integral), convergencia uniforme e intercambio de límites | Enunciado riguroso + esquema/ejemplo |
| Propiedades de cálculo: linealidad, monotonía, álgebra de límites | Enunciado + referencia |

**Criterio de problemas — C1/C2:**
Mínimo 15 propuestos por capítulo, máximo 40; graduación 25/50/25 con tags. En capítulos largos se admite la organización **por subsección temática** (patrón de `apderivadas`) con tags dentro de cada subsección — sujeto a Decisión E4. Déficits/excesos actuales: `tecintegracion` 4 (crítico), `limites` 50 y `sucesionesyseriesfunciones` 48 (exceso).

**Estado diagnóstico (inventario automatizado 2026-07-06):**

| Cap real | Archivo | Líneas | Sec/Sub | Ex (4 pasos) | Probs | myproof huérf. | Figuras `center` sin estándar | Figure envs (OK) | Tags |
|---|---|---|---|---|---|---|---|---|---|
| 10 | preliminares.tex | 797 | 2/6 | 6 (3+3 ilustr.) | 8 | 0 | 5 | 4 (4) | 0 |
| 11 | funciones.tex | 1 225 | 6/11 | 11 (6) | 17 | 0 | 3 | 15 (2) | 0 |
| 12 | limites.tex | 1 034 | 8/0 | 10 (10) | **50** | 2 | 0 | 3 (2) | 0 |
| 13 | derivadas.tex | 1 406 | 9/0 | 26 (26) | 37 | 3 | 3 | 3 (3) | 0 |
| 14 | apderivadas.tex | 2 831 | 9/9 | 21 (21) | 51 | 0 | **21** | 7 (2) | 0 |
| 15 | tecintegracion.tex | 1 288 | 7/19 | 25 (25) | **4** | 2 | 0 (0 figuras en total) | 0 | 0 |
| 16 | intdefinida.tex | 506 | 8/2 | 7 (7) | 15 | 0 | 5 | 0 | 0 |
| 17 | apintegral.tex | 2 267 | 7/6 | 24 (24) | 41 | 0 | **26** | 0 | 0 |
| 18 | impropias.tex | 951 | 4/0 | 7 (**myproof fuera ×7**) | 16 | **7** | 7 | 0 | 0 |
| 19 | polares.tex | 1 233 | 4/3 | 8 (8) | 12 | 0 | 12 | 0 | 0 |
| 20 | sucesionesyseries.tex | 1 344 | 2/8 | 14 (13) | 16 | 0 | 10 | 0 | 0 |
| 21 | sucesionesyseriesfunciones.tex | 1 711 | 4/4 | 12 (12) | **48** | 0 | 12 | 0 | 0 |

**Naturaleza del bloque vs C3:** el contenido y el protocolo de 4 pasos ya están al nivel C3 (Fases 1–3 los dejaron completos y verificados); la deuda dominante es (1) **el estándar de figuras** — ~98 tikz en `\begin{center}` sin caption/label frente al protocolo F8 —, (2) **figuras R2 nuevas** listadas en la GUIA §4–5 y nunca ejecutadas, (3) **graduación de bancos** (0 tags) con dos excesos y un déficit crítico, y (4) el bug estructural de `impropias`. No hay trabajo estructural de secciones (a diferencia de AL).

**Observaciones de naturaleza por capítulo (qué lo hace distinto):**
- `preliminares` es fundacional (axiomas, sup/inf): pocas figuras posibles; R2 se satisface con recta numérica y diagramas de vecindad. Es auxiliar en el encargo — su inclusión aquí es decisión de alcance del autor.
- `funciones` es un catálogo: 5 de sus examples son galerías de figuras sin cálculo (aceptadas sin 4 pasos); su deuda es de auditoría de figuras, no de contenido.
- `limites` mezcla banco enorme (50) con teoría rigurosa; el exceso se resuelve con Decisión (§F9C1.02).
- `apintegral` es el **capítulo modelo en contenido** (24/24 con 4 pasos, fillbetween verificado) pero el peor en estándar de figuras (26 en center) — la intervención es solo de formato, riesgo bajo pero volumen alto.
- `impropias` está marcado "Alto" desde Fase 1 pero **nunca recibió la corrección de anidamiento**: sus 7 myproof están fuera del example (verificado línea a línea). El contenido interno (4 pasos, boxed) está bien.
- `polares` exige `axis equal image` en cada conversión center→figure (ya lo usa; verificar que no se pierda).
- `sucesionesyseries` y `sucesionesyseriesfunciones` organizan propuestos por subsección (2 y 4 respectivamente) — patrón a conservar con tags internos (Decisión E4).
- `tecintegracion` tiene una dependencia adelantada: §"Sustitución en integrales definidas" (l.221) usa la integral definida un capítulo antes de definirse — **nota de decisión editorial**, ver F9C1.20.

---

## Semana 0 — Decisiones bloqueantes

### F9C1.01 — Registrar Decisión E4 (organización de propuestos)
**Archivo:** este `.md` + `GUIA_REESCRITURA_PROBLEMARIO.md`
**Acción:** confirmar con el autor: sección única `\section{Problemas propuestos}` como estándar, con subsecciones temáticas permitidas en capítulos largos (apderivadas, sucesiones×2); tags de graduación dentro de cada subsección.
**Criterio de cierre:** decisión registrada en ambos `.md`.
**Líneas estimadas:** 5–15 (Markdown)
**Estado:** Completado — 2026-07-06

**Decisión del autor (E4):**
- Heading único: `\section{Problemas propuestos}` (minúscula en "propuestos"), siempre **última sección del capítulo** (precedida por `\section{Problemas resueltos adicionales}` cuando exista, según Decisión F).
- En capítulos largos se permiten subsecciones temáticas internas (patrón apderivadas), con tags de graduación dentro de cada subsección.
- Las 4 variantes actuales de heading se renombran cuando cada capítulo sea intervenido en su ítem correspondiente (no de forma masiva anticipada).
- Nota de ejecución: la actualización de `GUIA_REESCRITURA_PROBLEMARIO.md` §2.4 con esta convención queda pendiente como parte del primer ítem de graduación que se ejecute (registrada aquí para no perderla).

### F9C1.02 — Decisión de exceso de propuestos (limites 50, sucesionesyseriesfunciones 48)
**Acción:** presentar al autor las opciones por capítulo: (a) consolidar duplicados de técnica hasta ≤40, (b) marcar los excedentes como `\textbf{(*) Desafío}` sin eliminar, (c) mantener con justificación (banco de examen). **Nada se elimina sin autorización.**
**Criterio de cierre:** decisión registrada por capítulo; aplicación queda en F9C1.10 y F9C1.37.
**Líneas estimadas:** 5–15 (Markdown)
**Estado:** Completado — 2026-07-06

**Decisión del autor:**
- **No se elimina ningún problema.** Los bancos que excedan 40 se reorganizan por subsección temática (amparado en E4); los problemas que superen la cuota se marcan con el comentario `% Banco extendido` y cuentan fuera del mínimo/máximo.
- La aplicación queda en F9C1.10 (limites, 50) y F9C1.37 (sucesionesyseriesfunciones, 48).

---

## Semana 1 — preliminares.tex (auxiliar, ver nota) + funciones.tex

**Nota de alcance:** `preliminares.tex` fue clasificado como auxiliar en el encargo; se incluye porque es el arranque pedagógico de C1. El autor decide si estos 2 ítems se ejecutan o se difieren.

### F9C1.03 — preliminares: figuras R2 nuevas
**Acción:** (a) recta numérica con intervalo (a,b) y vecindad V_ε(x₀); (b) diagrama de supremo (conjunto acotado, s y franja s−ε con un punto del conjunto dentro). Convertir además las 5 figuras en `center` a `figure[H]` + caption + label + anchors.
**Criterio de cierre:** 2 figuras nuevas estándar F8 en posición R2; 0 tikz fuera de figure.
**Líneas estimadas:** 90–150
**Estado:** Completado — 2026-07-17

**Notas de ejecución (2026-07-17):**
- El diagnóstico estaba parcialmente desactualizado: `fig:vecindad` y `fig:supremo` **ya existían** con caption+label. R2(a) queda cubierto por `fig:vecindad` (ya conforme, se le añadió ancla) + la conversión de `fig:intervalo_abierto`; R2(b) se resolvió **ampliando** `fig:supremo` con la franja $(\alpha-\varepsilon,\alpha]$ + punto $x\in S$ + caption descriptivo + párrafo-ancla.
- 4 tikz `center`→`figure[H]`+caption+label: `fig:valabs_ecuacion`, `fig:valabs_desigualdad`, `fig:intervalo_abierto`, `fig:supremo_sucesion`. El 5.º `center` del diagnóstico es la tabla de intervalos (tabular, no figura) — se conserva.
- Anclas nuevas: `fig:rectanumerica`, `fig:vecindad`. Resultado: 10/10 figuras del cap. conformes, todas con ancla.
- **Trampa babel-spanish descubierta:** `\inf` en `\caption` rompe el `.lof` (operador con tilde «ínf» vía `\es@a`, frágil en args móviles). Documentada en GUIA §2.3. `\sup` es seguro.

### F9C1.04 — preliminares: elevar resueltos + graduación
**Acción:** elevar 2–3 de los 8 propuestos a resueltos (inducción, desigualdad por casos, cálculo de sup/inf — recomendación GUIA §4); tags de graduación en los restantes; si el banco queda <8, añadir 3–4 propuestos nuevos.
**Criterio de cierre:** ≥2 resueltos nuevos con 4 pasos validados por el autor; banco graduado con tags.
**Líneas estimadas:** 60–110
**Estado:** Completado — 2026-07-17

**Notas de ejecución (2026-07-17):**
- 3 elevaciones aprobadas por el autor, insertadas con protocolo de 4 pasos + boxed: (1) desigualdad AM-GM en §Axiomas de campo y orden (la subsección no tenía examples); (2) $|x-2|+|x+1|=5$ por 3 casos + `fig:valabs_suma` en §Valor absoluto (técnica sin ejemplo previo); (3) $\sup/\inf$ de $\{(-1)^n/n\}$ + `fig:supremo_alternante` en §Conjuntos acotados (extremos alcanzados — contraste con el ejemplo $\frac{n}{n+1}$).
- Literales elevados retirados del banco (Probs. antiguos 1.3, 4.6, 6.1).
- Banco reordenado B→I→D con marcadores de grupo (aprobado por el autor): Básico 1 prob (15 literales), Intermedio 4 probs (21 literales), Desafiante 3 probs (15 literales) — 8 probs, 51 literales. Párrafo introductorio actualizado (niveles en vez de bloques temáticos).
- La actualización pendiente de GUIA §2.4 con la convención E4 (registrada en F9C1.01) se ejecutó aquí.

### F9C1.05 — funciones: auditoría de figuras (15 figure envs, 2 OK; 3 center)
**Acción:** protocolo F8.31 sobre las 13 figuras sin caption/label (incluye las galerías de catálogo pgfplots) y los 3 tikz en center. Lotes de ≤300 líneas si excede.
**Criterio de cierre:** 18/18 conformes; galerías con captions descriptivos.
**Líneas estimadas:** 120–250
**Estado:** Completado — 2026-07-17

**Notas de ejecución (2026-07-17):**
- Diagnóstico corregido: las 15 figure envs tenían **caption pero solo 2 label**; los «3 center» eran 2 tabulares (tablas trig/inversas, no figuras) + 1 `center` interno de `fig:caja-3d` (ya conforme) — **0 tikz sueltos reales**.
- 13 labels nuevos: fig:costo_contenedor, fig:recta_vertical, fig:tramos_salto, fig:potencias_enteras, fig:potencias_racionales, fig:exponenciales, fig:logaritmicas, fig:seno_coseno, fig:tangente, fig:traslaciones_parabola, fig:amplitud_fase, fig:trig_inversas, fig:ventana_normanda (todos **después** del caption, regla F8b).
- Anclas `\ref` añadidas para las 15 (incl. fig:caja y fig:caja-3d que tenían label sin ancla). 2 captions enriquecidos (tramos_salto, ventana_normanda).

### F9C1.06 — funciones: figuras R2 nuevas
**Acción:** (a) gráfica genérica con dominio y rango proyectados con flechas a los ejes; (b) función por tramos con punto lleno/vacío en la discontinuidad; (c) reflexión sobre y=x para la inversa (f y f⁻¹).
**Criterio de cierre:** 3 figuras estándar F8 tras las definiciones correspondientes (R2).
**Líneas estimadas:** 90–150
**Estado:** Completado — 2026-07-17

**Notas de ejecución (2026-07-17):**
- (a) `fig:dominio_rango` tras la Definición de función: curva sinusoidal con extremos marcados, D_f proyectado al eje x (rojo), R_f al eje y (verde), proyecciones punteadas desde máximo interior y mínimo de borde.
- (b) **pre-satisfecha** por `fig:tramos_salto` (ya existía como ejemplo con círculo abierto/punto sólido; conformada en F9C1.05) — no se duplicó.
- (c) `fig:inversa_reflexion` tras el algoritmo de inversión: $e^x$ y $\ln x$ con $y=x$ punteada, par simétrico $(1,e)$–$(e,1)$ conectado, `axis equal image`.

### F9C1.07 — funciones: graduación + elevaciones
**Acción:** tags en los 17 propuestos; elevar 2–3 a resueltos si cubren técnica sin ejemplo previo (composición con dominio, inversa con restricción); heading ya estándar (verificar).
**Criterio de cierre:** banco graduado; elevaciones validadas por el autor.
**Líneas estimadas:** 40–90
**Estado:** Completado — 2026-07-17

**Notas de ejecución (2026-07-17):**
- El banco real tenía 16 probs (no 17). 3 elevaciones aprobadas por el autor con protocolo de 4 pasos: (1) inversa sin fórmula explícita ($f=x^5+x^3+x$: $f^{-1}(3)=1$, $f(f^{-1}(2))=2$, $g^{-1}(4)=0$) en §Funciones inversas; (2) $f=\sqrt{1-x^2}$ en $[0,1]$ autoinversa (cuarto de circunferencia, conecta con fig:inversa_reflexion); (3) mareas bahía de Fundy $D(t)=7+5\cos[\frac{\pi}{6}(t-6.75)]$ — primer resuelto de §Transformaciones.
- Banco reordenado B→I→D con marcadores de grupo: **3B** (dominios, paridad, cocientes incrementales) / **7I** (familias ×2, transformaciones $e^x$, tramos, transformaciones trig, operaciones, ecuaciones exp/log) / **3D** (cúbica por interpolación, descomposición de compuestas, modelado 12 literales). Heading ya estándar (verificado).

---

## Semana 2 — limites.tex + derivadas.tex

### F9C1.08 — limites: figuras R2 nuevas
**Acción:** (a) diagrama ε-δ (banda ε, entorno δ, punto excluido — análogo a `fig:disco_epsilon_delta` de C3 pero en 1 variable); (b) tres discontinuidades (removible/salto/esencial) en minipages; (c) asíntota horizontal + vertical en una misma gráfica pgfplots.
**Criterio de cierre:** 3 figuras estándar F8 en posición R2 (la ε-δ inmediatamente tras la definición formal, §l.74).
**Líneas estimadas:** 110–170
**Estado:** Completado — 2026-07-17

**Notas de ejecución (2026-07-17):**
- (a) `fig:limite_epsilon_delta`: genérica (curva sinusoidal por $(c,L)$ excluido, banda azul $L\pm\epsilon$, entorno rojo $c\pm\delta$), inmediatamente tras el párrafo que sigue a la definición formal.
- (b) `fig:tipos_discontinuidad`: 3 minipages (removible / de salto / infinita — la «esencial» del plan se materializó como infinita, acorde con la clasificación del capítulo que separa infinita y oscilante).
- (c) `fig:asintotas`: $f(x)=1/(x-2)$ (la misma función que discute la rem ancla), AV $x=2$ roja + AH $y=0$, dos ramas con `restrict y to domain`.

### F9C1.09 — limites: anidar 2 myproof huérfanos + auditoría de 3 figuras
**Acción:** anidar los 2 myproof fuera de entorno; completar caption/label en la figura no conforme (1 de 3).
**Criterio de cierre:** 0 huérfanos; 3/3 figuras conformes.
**Líneas estimadas:** 15–40
**Estado:** Completado — 2026-07-17

**Notas de ejecución (2026-07-17):**
- Los 2 myproof huérfanos eran demostraciones de **teoremas** (Unicidad del límite y $\sin x/x$), no de examples. Precedente verificado en los 6 caps AL cerrados: las pruebas de teoremas usan `proof` (0 casos de theorem+myproof). Se convirtieron a `\begin{proof}` en vez de anidarse.
- Figura del encaje: `fig:encaje_areas` (caption ya existía) + ancla «véase la figura» → `\ref`.
- `fig:epsilon_delta_demo`: tenía label sin ancla → ancla en Paso 2 y caption enriquecido (era «Interpretación geométrica del límite»).
- 3/3 + 3 nuevas de .08 = 6/6 figuras conformes con ancla.

### F9C1.10 — limites: banco de 50 propuestos — graduación + Decisión F9C1.02 + elevaciones
**Acción:** aplicar la decisión de exceso; graduar con tags; elevar 4–5 a resueltos cubriendo técnicas sin ejemplo: ε-δ de límite lineal, 0/0 por factorización, trigonométrico, continuidad en un punto, aplicación del TVI (recomendación GUIA §4).
**Criterio de cierre:** banco ≤40 o excedentes marcados según decisión; tags completos; 4–5 resueltos nuevos validados.
**Líneas estimadas:** 120–200
**Estado:** Completado — 2026-07-17

**Notas de ejecución (2026-07-17):**
- Las técnicas recomendadas por la GUIA ya tenían resuelto (ε-δ, 0/0, TVI ×2, laterales ×2, equivalentes ×4); las elevaciones se eligieron por técnicas realmente sin cubrir. **5 elevaciones aprobadas por el autor y SymPy-verificadas:** racionalización $(\sqrt x-1)/(x-1)=1/2$; infinito racional $5x^2/(3x^2-5)=5/3$ (primer resuelto de §Límites infinitos); asíntotas de $x^2/(16-x^2)$ (AV $\pm4$ con signos, AH $-1$; **fusiona 2 probs del banco**); tipo $1^\infty$ $(1+x^2)^{\cot^2x}=e$; continuidad con parámetros $m=1,n=3$ (primer resuelto de §Continuidad; literal a del prob m/n).
- **Errata heredada corregida (aprobada por el autor):** $\lim_{x\to 1}\frac{\sin x-\cos x}{\cos 2x}$ → $x\to\pi/4$ (con 1 era sustitución directa ≈−0.72; con π/4 es el 0/0 clásico $=-\sqrt2/2$, SymPy-OK).
- Banco reorganizado en **6 subsecciones** (algebraicos y racionalización / trigonométricos y equivalentes / infinito y $1^\infty$ / asíntotas / continuidad / TVI y teóricos) con tags B/I/D por subsección: 9B/17I/14D = 40 contados + **4 `% Banco extendido`** (duplicado del ejemplo $\frac{x^2-1}{x-1}$ + 3 sustituciones directas triviales). Nada eliminado; el prob comentado del sándwich se conservó comentado. Heading → `Problemas propuestos`.

### F9C1.11 — derivadas: figuras R2 nuevas
**Acción:** (a) secante → tangente (dos secantes con h decreciente y la tangente límite, punto (x₀,f(x₀))); (b) árbol de dependencias de la regla de la cadena (nodos y ramas con derivadas parciales del caso y=f(u), u=g(x)).
**Criterio de cierre:** 2 figuras estándar F8; la secante-tangente inmediatamente antes/después de la definición de derivada (R1-C1 permite figura antes).
**Líneas estimadas:** 80–130
**Estado:** Pendiente

### F9C1.12 — derivadas: huérfanos + center + residuales
**Acción:** anidar 3 myproof huérfanos; convertir 3 tikz en center a figure[H]+caption+label; auditar las 3 marcas `\square`/`\qedhere` (eliminar si están en example/myproof, conservar si son `proof` legítimos).
**Criterio de cierre:** 0 huérfanos; 0 tikz fuera de figure; residuales auditados con lista en Notas.
**Líneas estimadas:** 30–70
**Estado:** Pendiente

### F9C1.13 — derivadas: graduación + elevaciones
**Acción:** tags en los 37 propuestos; elevar 3–4 a resueltos (derivada por definición de no-polinomial, cadena anidada, implícita, derivada de inversa — GUIA §4); heading `Problemas Propuestos` → `Problemas propuestos`.
**Criterio de cierre:** banco graduado; elevaciones validadas; heading estándar.
**Líneas estimadas:** 90–160
**Estado:** Pendiente

---

## Semana 3 — apderivadas.tex

### F9C1.14 — apderivadas: conversión de figuras center — lote 1 (razones de cambio + extremos)
**Acción:** de los 21 tikz en `center`, convertir los de las secciones Razones de Cambio y Valores Extremos (~10) a figure[H]+caption+label+anchors.
**Criterio de cierre:** lote conforme; compilación limpia.
**Líneas estimadas:** 100–200
**Estado:** Pendiente

### F9C1.15 — apderivadas: conversión de figuras center — lote 2 (resto) + auditoría de 7 figure envs
**Acción:** convertir los ~11 tikz restantes; completar caption/label en los 5 figure envs no conformes.
**Criterio de cierre:** 0 tikz fuera de figure en el archivo; 7/7 figure envs conformes.
**Líneas estimadas:** 100–200
**Estado:** Pendiente

### F9C1.16 — apderivadas: figuras R2 nuevas
**Acción:** (a) zonas de crecimiento/decrecimiento sombreadas con signo de f′; (b) concavidad con tangentes girando (cóncava arriba/abajo, punto de inflexión); (c) TVM: curva entre A y B con secante y tangente paralela en c.
**Criterio de cierre:** 3 figuras estándar F8 en posición R2 (TVM junto a su demostración ya existente — central R3).
**Líneas estimadas:** 100–160
**Estado:** Pendiente

### F9C1.17 — apderivadas: graduación por subsecciones + elevaciones
**Acción:** el banco de 51 está organizado en 6 subsecciones temáticas (patrón a conservar, Decisión E4): tags 25/50/25 dentro de cada subsección; elevar 2–3 en subsecciones cuya técnica no tenga resuelto directo; heading ya estándar en sección madre (verificar mayúscula).
**Criterio de cierre:** tags en las 6 subsecciones; elevaciones validadas.
**Líneas estimadas:** 60–130
**Estado:** Pendiente

---

## Semana 4 — tecintegracion.tex + intdefinida.tex

### F9C1.18 — tecintegracion: expansión del banco (déficit crítico: 4 propuestos)
**Acción:** añadir 12–16 propuestos nuevos graduados: ~5 Básico (sustitución simple, potencia), ~7 Intermedio (partes, fracciones parciales, potencias trigonométricas), ~4 Desafiante (sustitución trig, combinadas, cíclicas); tags; cubrir todos los subtemas del capítulo.
**Criterio de cierre:** 15–20 propuestos totales graduados con tags; cobertura completa de subtemas.
**Líneas estimadas:** 80–140
**Estado:** Pendiente

### F9C1.19 — tecintegracion: figuras R2 (capítulo con CERO figuras)
**Acción:** (a) triángulos rectángulos de referencia de la sustitución trigonométrica — minipage triple, un triángulo por caso (√(a²−u²), √(a²+u²), √(u²−a²)), insertados en la subsección "Idea geométrica y fundamento" (l.791); (b) figura de antiderivada como familia de curvas F(x)+C (curvas paralelas verticales).
**Criterio de cierre:** ≥2 figuras (4 tikz) estándar F8; el capítulo deja de tener 0 figuras.
**Líneas estimadas:** 110–170
**Estado:** Pendiente

### F9C1.20 — tecintegracion: heading + huérfanos + residuales + nota de dependencia
**Acción:** renombrar `\section{Ejercicios propuestos}` → `\section{Problemas propuestos}`; anidar 2 myproof huérfanos; auditar 2 marcas residuales; **nota de decisión editorial:** la subsección "Sustitución en integrales definidas" (l.221) usa la integral definida antes del cap. 16 — opciones: (i) moverla a `intdefinida.tex`, (ii) precederla de una rem con remisión hacia adelante, (iii) mantener. Registrar decisión del autor sin ejecutar movimiento en este ítem.
**Criterio de cierre:** heading estándar; 0 huérfanos; residuales auditados; decisión de dependencia registrada.
**Líneas estimadas:** 20–50
**Estado:** Pendiente

### F9C1.21 — intdefinida: figuras R2 + conversión de 5 center
**Acción:** (a) suma de Riemann: rectángulos bajo la curva con partición etiquetada (fillbetween); (b) TFC geométrico: área acumulada A(x) con x móvil; convertir los 5 tikz en center al estándar F8.
**Criterio de cierre:** 2 figuras nuevas en posición R2 (Riemann en §l.44, TFC en §l.223); 0 tikz fuera de figure.
**Líneas estimadas:** 120–180
**Estado:** Pendiente

### F9C1.22 — intdefinida: graduación + heading
**Acción:** tags en los 15 propuestos (creados en Fase 3, verificados V2.1); heading `Problemas Propuestos` → `Problemas propuestos`.
**Criterio de cierre:** banco graduado; heading estándar.
**Líneas estimadas:** 15–35
**Estado:** Pendiente

---

## Semana 5 — apintegral.tex + impropias.tex

### F9C1.23 — apintegral: conversión de figuras center — lote 1 (áreas + volúmenes)
**Acción:** de los 26 tikz en `center`, convertir los de §Áreas y §Volúmenes (~13) a figure[H]+caption+label+anchors, preservando intactos los fillbetween verificados en Fase 1.
**Criterio de cierre:** lote conforme; fillbetween sin regresiones; compilación limpia.
**Líneas estimadas:** 130–250
**Estado:** Pendiente

### F9C1.24 — apintegral: conversión de figuras center — lote 2 (longitud, superficies, física)
**Acción:** convertir los ~13 restantes (longitud de arco, superficies de revolución, trabajo, centroide, inercia, hidrostática).
**Criterio de cierre:** 0 tikz fuera de figure en el archivo.
**Líneas estimadas:** 130–250
**Estado:** Pendiente

### F9C1.25 — apintegral: auditoría de 17 marcas residuales
**Acción:** el archivo contiene 17 marcas `\qquad\square`/`$\square$`/`\qedhere` (detección automatizada): clasificar cuáles están dentro de `proof` legítimos (se conservan) y cuáles en example/myproof (se eliminan, regla GUIA §2.2).
**Criterio de cierre:** 0 marcas en example/myproof; lista clasificada en Notas.
**Líneas estimadas:** 17–40
**Estado:** Pendiente

### F9C1.26 — apintegral: graduación del banco
**Acción:** tags 25/50/25 en los 41 propuestos (límite 40: si el conteo real confirma 41, marcar 1 como Desafío extra o consolidar con autorización); heading ya estándar (verificar).
**Criterio de cierre:** banco graduado ≤40 o excedente marcado.
**Líneas estimadas:** 40–70
**Estado:** Pendiente

### F9C1.27 — impropias: anidar los 7 myproof huérfanos (bug estructural en TODOS los ejemplos)
**Acción:** los 7 examples siguen el patrón `\end{example}` → `\begin{myproof}` (verificado: l.77/81, 149/153, 254/261, 352/362, 490/493, 543/547, 641/645). Mover cada `\end{example}` para encapsular su myproof. El contenido interno (4 pasos + boxed) ya es correcto — no tocar.
**Criterio de cierre:** 7/7 examples con myproof dentro; `myproof_huerfanos = 0`; compilación limpia.
**Líneas estimadas:** 14–30 (solo delimitadores)
**Estado:** Pendiente

### F9C1.28 — impropias: figuras — conversión de 7 center + figura R2 nueva
**Acción:** convertir los 7 tikz en center al estándar F8 (fillbetween verificados — no alterar trayectorias); añadir figura de integral impropia como límite de área creciente (región [a,t] con t→∞).
**Criterio de cierre:** 0 tikz fuera de figure; figura nueva en posición R2 (tras la def. de 1er tipo).
**Líneas estimadas:** 90–160
**Estado:** Pendiente

### F9C1.29 — impropias: graduación + heading
**Acción:** tags en los 16 propuestos; heading `Problemas Propuestos` → `Problemas propuestos`.
**Criterio de cierre:** banco graduado; heading estándar.
**Líneas estimadas:** 15–35
**Estado:** Pendiente

---

## Semana 6 — polares.tex + sucesionesyseries.tex

### F9C1.30 — polares: conversión de 12 figuras center
**Acción:** convertir los 12 tikz/pgfplots en center al estándar F8 **verificando que cada curva polar/cónica conserva `axis equal image`** (el archivo ya lo usa 7×; ninguna conversión debe perderlo).
**Criterio de cierre:** 0 tikz fuera de figure; `axis equal image` presente en todas las curvas polares.
**Líneas estimadas:** 100–200
**Estado:** Pendiente

### F9C1.31 — polares: graduación + elevaciones
**Acción:** tags en los 12 propuestos; si tras graduar quedan subtemas sin propuesto (longitud de arco polar, área entre dos curvas polares), añadir 3–4 nuevos; heading ya estándar (verificar).
**Criterio de cierre:** banco graduado con cobertura completa de subtemas; 12–16 propuestos.
**Líneas estimadas:** 40–90
**Estado:** Pendiente

### F9C1.32 — sucesionesyseries: conversión de 10 figuras center
**Acción:** convertir los 10 tikz en center al estándar F8.
**Criterio de cierre:** 0 tikz fuera de figure; compilación limpia.
**Líneas estimadas:** 80–160
**Estado:** Pendiente

### F9C1.33 — sucesionesyseries: figuras R2 nuevas
**Acción:** (a) sucesión convergente: puntos aₙ sobre la recta numérica acercándose a L con banda (L−ε, L+ε); (b) serie geométrica: rectángulos de área 1/2ⁿ llenando el cuadrado unitario (demostración visual de Σ1/2ⁿ=1).
**Criterio de cierre:** 2 figuras estándar F8 en posición R2 (tras def. de límite de sucesión y tras la serie geométrica).
**Líneas estimadas:** 70–120
**Estado:** Pendiente

### F9C1.34 — sucesionesyseries: graduación en subsecciones de propuestos
**Acción:** el capítulo tiene 2 subsecciones de propuestos (Sucesiones l.671, Series l.1233 — patrón conservado por Decisión E4): tags dentro de cada una sobre los 16 probs.
**Criterio de cierre:** tags en ambas subsecciones.
**Líneas estimadas:** 15–35
**Estado:** Pendiente

---

## Semana 7 — sucesionesyseriesfunciones.tex + transversales y cierre

### F9C1.35 — sucesionesyseriesfunciones: conversión de 12 figuras center
**Acción:** convertir los 12 tikz en center al estándar F8 (incluye el diagrama de radios corregido en Fase 1 — preservar la corrección R=∞).
**Criterio de cierre:** 0 tikz fuera de figure.
**Líneas estimadas:** 100–180
**Estado:** Pendiente

### F9C1.36 — sucesionesyseriesfunciones: figuras R2 nuevas
**Acción:** (a) banda de convergencia uniforme: f ± ε con las fₙ encerradas; (b) radio de convergencia sobre la recta: centro a, extremos a±R con estado de convergencia en cada zona.
**Criterio de cierre:** 2 figuras estándar F8 en posición R2 (tras def. de convergencia uniforme y tras el teorema del radio).
**Líneas estimadas:** 70–120
**Estado:** Pendiente

### F9C1.37 — sucesionesyseriesfunciones: banco de 48 — aplicar Decisión F9C1.02 + tags
**Acción:** aplicar la decisión de exceso sobre las 4 subsecciones de propuestos (l.452, 902, 1420, 1673 — patrón conservado); tags dentro de cada una.
**Criterio de cierre:** banco conforme a la decisión; tags en las 4 subsecciones.
**Líneas estimadas:** 40–90
**Estado:** Pendiente

### F9C1.38 — Transversal C1/C2: normalizar headings de propuestos
**Acción:** unificar a `\section{Problemas propuestos}` (o subsecciones según E4) en los 12 archivos: corrige `Problemas Propuestos` (limites, derivadas, apderivadas, intdefinida, impropias, vectoresrn-si-aplica) y el ya tratado de tecintegracion.
**Criterio de cierre:** grep de variantes = 0 en el bloque.
**Líneas estimadas:** 6–15
**Estado:** Pendiente

### F9C1.39 — Transversal C1/C2: auditoría R3 de teoremas centrales
**Acción:** verificar que cada central tiene demostración o esquema: unicidad del límite, sándwich, TVI (esquema mínimo), TVM (ya demostrado F3), TFC1/TFC2 (ya demostrados), criterios de comparación y razón; completar esquema donde solo haya enunciado; registrar el estado por teorema.
**Criterio de cierre:** tabla teorema→tratamiento en Notas; esquemas añadidos donde faltaban (≤80 líneas c/u).
**Líneas estimadas:** 40–160 (según hallazgos)
**Estado:** Pendiente

### F9C1.40 — Cierre de bloque: compilación y re-inventario
**Acción:** compilar el maestro (2 pasadas LuaLaTeX); re-ejecutar inventario sobre los 12 archivos; confirmar: 0 huérfanos, 0 tikz fuera de figure, 0 figuras sin caption/label, tags completos, headings unificados.
**Criterio de cierre:** 0 errores `!`; tabla de re-inventario en Notas; páginas registradas.
**Líneas estimadas:** 0 (verificación)
**Estado:** Pendiente

---

## Registro de progreso

| Ítem | Archivo(s) | Acción | Estado | Fecha | Notas |
|---|---|---|---|---|---|
| F9C1.01 | `.md` | Decisión E4 organización propuestos | Completado | 2026-07-06 | Heading único `Problemas propuestos`, última sección (tras `Problemas resueltos adicionales` si existe); subsecciones temáticas permitidas con tags internos; renombres al intervenir cada capítulo. |
| F9C1.02 | `.md` | Decisión exceso (limites 50 / sucfun 48) | Completado | 2026-07-06 | Nada se elimina: reorganizar por subsección (E4) y marcar excedentes con `% Banco extendido` (fuera de la cuota). Aplicación en F9C1.10 y F9C1.37. |
| F9C1.03 | `preliminares.tex` | 2 figuras R2 + 5 center | Completado | 2026-07-17 | Autor aprobó ejecutar (cap. abre el libro tras retiro de politicas). 4 center→figure[H]; fig:supremo ampliada con franja ε; fig:vecindad ya existía. 10/10 figs conformes. Trampa `\inf` en caption → GUIA §2.3 |
| F9C1.04 | `preliminares.tex` | Elevar 2–3 resueltos + tags | Completado | 2026-07-17 | 3 elevaciones aprobadas (AM-GM, valor absoluto por casos, sup/inf alternante); banco 8 probs reordenado B→I→D con marcadores de grupo; GUIA §2.4 actualizada con E4 |
| F9C1.05 | `funciones.tex` | Auditoría 18 figuras | Completado | 2026-07-17 | 13 labels + 15 anclas; los «3 center» eran 2 tabulares + 1 interno conforme; 17/17 figs conformes (con las 2 de F9C1.06) |
| F9C1.06 | `funciones.tex` | 3 figuras R2 nuevas | Completado | 2026-07-17 | fig:dominio_rango + fig:inversa_reflexion; (b) pre-satisfecha por fig:tramos_salto |
| F9C1.07 | `funciones.tex` | Graduación + elevaciones | Completado | 2026-07-17 | 3 elevaciones aprobadas (inversa sin fórmula, autoinversa, mareas Fundy); banco 13 probs 3B/7I/3D con marcadores de grupo |
| F9C1.08 | `limites.tex` | 3 figuras R2 nuevas | Completado | 2026-07-17 | fig:limite_epsilon_delta, fig:tipos_discontinuidad (3 minipages), fig:asintotas |
| F9C1.09 | `limites.tex` | 2 huérfanos + auditoría figuras | Completado | 2026-07-17 | Huérfanos eran pruebas de teoremas → `proof` (precedente AL); fig:encaje_areas + ancla; 6/6 conformes |
| F9C1.10 | `limites.tex` | Banco 50: decisión + tags + elevar 4–5 | Completado | 2026-07-17 | 5 elevaciones SymPy-OK; 6 subsecciones E4; 40 contados + 4 `% Banco extendido`; errata x→1→π/4 corregida; heading estándar |
| F9C1.11 | `derivadas.tex` | 2 figuras R2 nuevas | Completado | 2026-07-22 | fig:secante_tangente (2 secantes→tangente) + fig:arbol_cadena (árbol y→u→x). Verificadas visualmente pp. 90/94 |
| F9C1.12 | `derivadas.tex` | 3 huérfanos + 3 center + residuales | Completado | 2026-07-22 | 3 huérfanos (continuidad, prod., cadena) eran pruebas de teoremas → `proof` + `\qquad\square` retirado (qed auto). **Hallazgo: los 3 `center` son tablas (tabular), no tikz → sin conversión.** Extra: 3 figuras de propuestos con `\label` antes de `\caption` corregidas (circder/trider/lamparader) |
| F9C1.13 | `derivadas.tex` | Tags + elevar 3–4 + heading | Completado | 2026-07-22 | Heading→minúscula; 37 propuestos reagrupados 10B/19I/8D con marcadores (script preserva bloques íntegros). **Elevaciones OMITIDAS (decisión del autor): cobertura de ejemplos ya completa** |
| F9C1.14 | `apderivadas.tex` | Center lote 1 (~10) | Completado | 2026-07-22 | **Hallazgo: de los 21 `center`, solo 9 son tikz; 12 son tablas.** Convertidos a figure[H]+caption+label: caja_abierta_recorte, lata_cilindrica, tuberia_rio (cuerpo) |
| F9C1.15 | `apderivadas.tex` | Center lote 2 (~11) + 5 figure envs | Completado | 2026-07-22 | 6 tikz-center de propuestos→figure (cuadrado_inscrito, nino_globo, trote_nado, cine_angulo, astas_cable, grafica_fprima). 5 figure envs no conformes completados: tanque_conico, escalera_pared, monotonia_x3, bosquejo_racional (+label), concavidad_x4 (label antes de caption). Bloque figura comentado L~2469 dejado como dead-code |
| F9C1.16 | `apderivadas.tex` | 3 figuras R2 nuevas | Completado | 2026-07-22 | **Hallazgo: (a) crecimiento/decrec. y (b) concavidad YA existían (figs monotonia_x3/concavidad_x4).** Solo faltaba (c) TVM → fig:tvm_secante_tangente (secante+tangente paralela en c). Verificada p.124 |
| F9C1.17 | `apderivadas.tex` | Tags por subsección + elevaciones | Completado | 2026-07-22 | Marcadores de grupo B/I/D en las 6 subsecciones temáticas (patrón limites.tex). §1 Razones 4B/7I/4D (4 bloques de texto reubicados; 3 figuras grandes intactas); §2 2B/4I/1D; §3 3B/4I/3D; §4 1B/4I/2D; §5 1B/2I/1D; §6 1B/2I/1D. Heading `Propuestos`→`propuestos`; limpieza `\subsection{ Regla}`→`{Regla}`. **Sin elevaciones:** las 6 técnicas ya tienen resuelto directo en el cuerpo. V/F de repaso al inicio se deja sin marcador. 818 pp, 0 errores. |
| F9C1.18 | `tecintegracion.tex` | Banco 4 → 15–20 graduado | Completado | 2026-07-23 | **Hallazgo: los «4 propuestos» eran 4 entornos `prob` con 67 integrales.** Reordenados en B/I/D con marcador de grupo (bloque 1: 28→7B/12I/9D; bloque 2 potencias trig: 15→5B/6I/4D; bloque 3 sust. trig: 15→4B/7I/4D; bloque 4 Spivak/Larson: 8 marcado Desafiante completo). De las 16 aprobadas por el autor, **10 duplicaban integrales ya presentes** → insertadas solo las 6 que abrían un peldaño ausente (∫ln x/x, ∫xeˣ, ∫x²ln x, ∫(3x+5)/((x−1)(x²+1)), ∫dx/(x²+4x+13), ∫₀^{π/2}sen⁴x). Las 16 SymPy-OK. |
| F9C1.19 | `tecintegracion.tex` | Triángulos sust. trig + familia F(x)+C | Completado | 2026-07-23 | (b) `fig:familia_antiderivadas` nueva (pgfplots, familia x³/3+C con tangentes paralelas en x=1, verificada p.174). (a) **Hallazgo: los 3 triángulos de referencia YA existían** como `center` en las subsecciones Caso 1/2/3 → promovidos a figure[H]+caption+label (`fig:triangulo_caso1/2/3`) en vez de duplicar. |
| F9C1.20 | `tecintegracion.tex` | Heading + huérfanos + nota dependencia | Completado | 2026-07-23 | Heading `Ejercicios`→`Problemas propuestos`; 2 myproof huérfanos (linealidad, potencia generalizada) → `proof` (son pruebas de teoremas, precedente F9C1.09); labels `cap:tecintegracion`/`cap:intdefinida` añadidos. **Decisión del autor: mover** «Sustitución en integrales definidas» a `intdefinida.tex` (§TFC, `thm:sustitucion-definida`); en tecintegracion queda una `rem` con remisión hacia adelante. |
| F9C1.21 | `intdefinida.tex` | Riemann + TFC + 5 center | Completado | 2026-07-23 | 5 center→figure[H]+caption+label (`fig:exhaucion_circulo`, `fig:suma_riemann`, `fig:area_neta`, `fig:funcion_acumulacion`, `fig:tvm_integrales`) + ancla en prosa. **Hallazgo: las 2 «figuras R2 nuevas» (Riemann y acumulación) YA existían** — solo faltaba encapsularlas. |
| F9C1.22 | `intdefinida.tex` | Tags + heading | Completado | 2026-07-23 | Heading `Propuestos`→`propuestos`; 15 prob reordenados 5B/8I/2D con marcador de grupo. |
| F9C1.23–.24 | `apintegral.tex` | Center 26 (áreas/vol + long/sup/física) | Completado | 2026-07-23 | Los 26 tikz en `center` → figure[H]+caption+label+ancla (script `conv_centers.py`; captions redactados por contexto). fillbetween intactos. |
| F9C1.25 | `apintegral.tex` | Auditoría 17 residuales | Completado | 2026-07-23 | 4 `\qedhere` en `proof` conservados (L187/516/996/1146); 13 en `myproof` eliminados (GUIA §2.2). |
| F9C1.26 | `apintegral.tex` | Tags banco 41 | Completado | 2026-07-23 | 7 subsecciones temáticas E4 + marcador B/I/D (7B/22I/12D); el Putnam (#38) marcado `% Banco extendido` (excedente sobre 40). |
| F9C1.27 | `impropias.tex` | Anidar 7 myproof (bug estructural total) | Completado | 2026-07-23 | Los 7 `\end{example}` reencapsulan su `myproof` (script `fix_huerfanos.py`); contenido interno intacto. huérfanos 7→0. |
| F9C1.28 | `impropias.tex` | 7 center + figura R2 nueva | Pendiente | — | — |
| F9C1.29 | `impropias.tex` | Tags + heading | Pendiente | — | — |
| F9C1.30 | `polares.tex` | 12 center (preservar axis equal image) | Pendiente | — | — |
| F9C1.31 | `polares.tex` | Tags + cobertura de subtemas | Pendiente | — | — |
| F9C1.32 | `sucesionesyseries.tex` | 10 center | Pendiente | — | — |
| F9C1.33 | `sucesionesyseries.tex` | 2 figuras R2 nuevas | Pendiente | — | — |
| F9C1.34 | `sucesionesyseries.tex` | Tags en 2 subsecciones | Pendiente | — | — |
| F9C1.35 | `sucesionesyseriesfunciones.tex` | 12 center | Pendiente | — | — |
| F9C1.36 | `sucesionesyseriesfunciones.tex` | 2 figuras R2 nuevas | Pendiente | — | — |
| F9C1.37 | `sucesionesyseriesfunciones.tex` | Banco 48: decisión + tags ×4 subsecciones | Pendiente | — | — |
| F9C1.38 | 12 archivos | Headings unificados | Pendiente | — | — |
| F9C1.39 | bloque C1/C2 | Auditoría R3 centrales | Pendiente | — | — |
| F9C1.40 | maestro | Compilación + re-inventario | Pendiente | — | — |

**Total: 40 ítems** (38 núcleo + 2 de preliminares sujetos a decisión de alcance).

---

## Notas de protocolo

- Cada ítem se ejecuta en Claude Code; compilar con LuaLaTeX tras cada ítem; si falla, revertir.
- Antes de cada ítem: leer las primeras 50 líneas del `.tex`, recontar entornos, compilar tras cerrar.
- Conversión center→figure: **nunca** alterar el contenido del tikzpicture (los fillbetween de apintegral/impropias están verificados); solo envolver, añadir caption/label y anchors faltantes.
- Cada resuelto nuevo (elevaciones) se presenta al autor antes de escribirlo al archivo.
- Los excesos de banco (limites, sucfun) no se recortan sin la decisión F9C1.02 cerrada.
- La matemática está verificada (Fases 1–5, V1–V4): este plan no re-deriva resultados; cualquier inconsistencia detectada se registra y escala.
