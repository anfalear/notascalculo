# Fase 9-T · Auditoría e integración de talleres de refuerzo — Cálculo III

**Fecha:** 2026-07-17 · **Responsable:** Fabián · **Ejecutor:** Claude Code
**Insumos:** 7 talleres de refuerzo (I–VI, VIII) + Examen Final Nov-2025 + 8 capítulos `.tex` de Cálculo III

---

## 1. Objetivo

Verificar que cada problema de los talleres de refuerzo 2026-1 tenga un equivalente
estructural en el problemario. Donde no lo haya: integrarlo como **problema resuelto**
(entorno `prob` + `myproof`) en la sección temática correspondiente, y/o como
**problema propuesto** en la sección final del capítulo. Esta fase NO edita los `.tex`
hasta cerrar la auditoría y las decisiones bloqueantes.

**Criterio de equivalencia estructural:** mismo tipo de técnica y dificultad comparable.
No se exige coincidencia textual ni de valores numéricos. Ejemplo: si el capítulo ya
tiene un límite por trayectorias + emparedado con función racional homogénea, T3.08
cuenta como CUBIERTO aunque la función sea otra.

---

## 2. Mapeo talleres → capítulos

| Taller | Tema | Archivo(s) destino | Secciones ancla |
|---|---|---|---|
| T1 | Superficies y secciones cónicas | `funvectoriales.tex` | §Superficies cuádricas, §Curvas y superficies de nivel |
| T2 | Funciones vectoriales | `funvectoriales.tex` | §Funciones vectoriales (todas las subsec.) |
| T3 | Dominio, límites y continuidad | `limvariasvariables.tex` (+dominios en `funvectoriales.tex` §Funciones de varias variables) | §Límite y continuidad, §Emparedado, §Continuidad |
| T4 | Derivadas parciales y regla de la cadena | `planostangentes.tex` + `gradientes.tex` | §Derivadas parciales, §Plano tangente, §Diferenciales / §Regla de la cadena, §Derivación implícita |
| T5 | Gradientes, direccionales y puntos críticos | `gradientes.tex` + `multiplicadoresintdobles.tex` | §Gradiente, §Derivada direccional, §Plano tangente-gradiente / §Criterio 2ª derivada |
| T6 | Optimización, Lagrange e integrales dobles | `multiplicadoresintdobles.tex` | §Lagrange, §Hessiano limitado, secciones de integrales dobles |
| T8 | Int. de línea, Green e int. triples | `cap33.tex` + `cap34.tex` + `inttriples.tex` | §Int. línea, §Campos conservativos / §Green / §Triples, §Cambio de variables |
| EX | Examen final Nov-2025 (transversal) | según ítem | según ítem |

**Ausente:** Taller VII (por numeración, probablemente integrales dobles en polares /
área de superficie / cambio de variables 2D). Verificar si existe y subirlo antes de
cerrar la auditoría de `multiplicadoresintdobles.tex` y `cap34.tex`.

---

## 3. Decisiones bloqueantes (responder ANTES de ejecutar Fase C)

- **D1 — Autoría/reformulación:** los talleres son material de la Escuela (posiblemente
  de varios profesores). ¿Se integran los enunciados (a) textuales, (b) reformulados con
  redacción propia y mismos valores, o (c) reformulados con valores nuevos (isomorfos)?
  Recomendación: (c) para el Examen Final; (b) mínimo para talleres.
- **D2 — Figuras:** los talleres usan capturas de GeoGebra; el libro exige TikZ/pgfplots
  (R2, `shader=flat`, `samples≤20`). ¿Cada problema importado con figura genera un
  ítem TikZ obligatorio, o se admite el estado intermedio "figura pendiente" con
  `%TODO-FIG`? Recomendación: ítem TikZ separado, para no bloquear el texto.
- **D3 — Problema humidex (T3.01):** problema de tabla/datos con contexto Bucaramanga-IDEAM.
  Rompe el registro Apostol pero tiene valor didáctico local. ¿Se incluye como
  "problema contextualizado" (quizá en un entorno `example` o recuadro propio) o se excluye?
- **D4 — Taller VII:** ¿existe? Si sí, se añade al inventario antes de ejecutar.
- **D5 — Enunciados "use GeoGebra":** muchos ítems dicen "realice un bosquejo con
  GeoGebra". En el libro, ¿se conserva la instrucción (útil para el curso) o se
  reemplaza por la figura TikZ ya resuelta? Recomendación: figura TikZ en la solución,
  y en propuestos conservar "verifique con GeoGebra" como coletilla opcional.

---

## 4. Inventario atómico

Convención de IDs: `T<n>.<ítem>` y `EX.<ítem>`. Columnas **Veredicto** y **Ref** las
llena Claude Code en Fase A. Veredictos: `CUBIERTO` / `PARCIAL` / `FALTA`.
`Ref` = línea o `\label` del problema equivalente en el `.tex`.

### T1 — Superficies y cónicas → `funvectoriales.tex`

| ID | Descriptor | Técnica | Veredicto | Ref |
|---|---|---|---|---|
| T1.01 | Cónica 4x²−y²−8x+6y−4=0: elementos (hipérbola) | completar cuadrados, focos | FALTA | no hay cónicas planas con elementos (focos/vértices) en el cap. |
| T1.02 | Hiperboloide 4x²+y²−z²=1 ∩ plano z=3 → elipse | sustitución, canónica | PARCIAL | L1194; trazas sí, falta extraer elementos canónicos de la elipse resultante |
| T1.03 | Paraboloide −9x²+16y²=144z ∩ x=0 → parábola | traza, vértice/foco/directriz | FALTA | no aparece vértice/foco/directriz en ninguna traza |
| T1.04 | Elipsoide 4x²+3y²+z²−8x+12y−6z+13=0 (a–d) | canónica, semiejes, trazas 3 planos | PARCIAL | L1789 (propuesto h: esfera con términos lineales); falta elipsoide resuelto con completar cuadrados |
| T1.05 | Cono x²+2y²−z²=0 (a–e) | clasificar, trazas, vs paraboloide | CUBIERTO | L1150 (example cono, trazas) |
| T1.06 | Cilindro elíptico 9x²+4y²−18x+8y+1=0 (a–d) | canónica, secciones z=c | FALTA | el cap. no trata cilindros (0 menciones) |
| T1.07 | x²+2y²−4x+4y−z+6=0 → paraboloide elíptico | identificar, eje de apertura | PARCIAL | L1066; solo forma canónica, sin traslación/completar cuadrados |
| T1.08 | x²−y²+z²−4x−2z+4=0 → hiperboloide 1 hoja | canónica, trazas | PARCIAL | L1194; canónico eje z, sin traslación ni eje y |
| T1.09 | y²−x²−z²−2y+4z−7=0 → hiperboloide 2 hojas | orientación, trazas | PARCIAL | L1235; canónico eje z, falta reorientar + completar cuadrados |
| T1.10 | z=3x²−y²+12x+2y+10 → paraboloide hiperbólico | punto de silla | PARCIAL | L1107; canónico, sin términos lineales |
| T1.11 | f(t)=(4sinh t, 1+3cosh t) → hipérbola | identidad cosh²−sinh²=1 | FALTA | no hay funciones hiperbólicas en el cap. |

### T2 — Funciones vectoriales → `funvectoriales.tex`

| ID | Descriptor | Técnica | Veredicto | Ref |
|---|---|---|---|---|
| T2.01 | lím ⟨e^{−3t}, t²/sen²t, cos 2t⟩ | límite por componentes | CUBIERTO | L158 (prob 3 incisos) + example L129 |
| T2.02 | lím ⟨cos t, t² sen(1/t), t²⟩ | teorema de compresión | PARCIAL | L158; falta componente resuelta por emparedado (t²sen(1/t)) |
| T2.03 | Tangente a ⟨t³,2t,sen(t−1)⟩ en t=1 | derivada, punto de anclaje | PARCIAL | L325; hay derivada/velocidad pero nunca se escribe la ecuación de la recta tangente |
| T2.04 | T̂(0) de ⟨te^{−t}, 2arctan t, 2e^t⟩ | tangente unitario | FALTA | el vector tangente unitario no aparece en el cap. |
| T2.05 | Astroide ⟨cos³t, sen³t⟩: no-suavidad y longitud en [0,π/2] | r'(t)=0, longitud de arco | PARCIAL | L608; longitud sí, falta discusión de suavidad (r'(t)=0) |
| T2.06 | Longitud de ⟨e^t sen t, e^t cos t⟩, [0,π] | longitud de arco | CUBIERTO | L608 inciso c (idéntico) |
| T2.07 | ⟨arccos(2t²−1), arcsen t⟩ es segmento de recta | identidades inversas | FALTA | sin equivalente |
| T2.08 | a(t) constante: hallar r(t), tipo de curva, mínimo al origen | integración vectorial, optimización 1D | PARCIAL | L475; integral definida sí, falta PVI cinemático (a→v→r) con condiciones iniciales |
| T2.09 | Cilindro x²+y²=1 ∩ plano y+z=2: parametrizar, tangente en (0,1,1) | parametrización trigonométrica vs raíz | FALTA | no hay parametrización de intersección de superficies |
| T2.10 | Recta ⊥ al segmento entre centros de S1 y S2 (cuádricas) | completar cuadrados, vector director | FALTA | sin equivalente |
| T2.11 | Intersección de curvas r(t) y s(u) (cos/sen/cos2t) | igualación por componentes | FALTA | sin equivalente |
| T2.12 | Reparametrizar ⟨e^{2t}cos2t, 2, e^{2t}sen2t⟩ por longitud de arco | s(t), despeje t(s) | CUBIERTO | L723 (example) + propuesto L1667 |
| T2.13 | Cónica x²+y²−2xy−2(x+y)+1=0: parábola rotada, parametrización, tangentes h/v | discriminante b²−4ac, cambio u,v | FALTA | no hay rotación de ejes/cónicas rotadas en el libro de Cálc. III |

### T3 — Dominio, límites, continuidad → `limvariasvariables.tex` (dominios: también `funvectoriales.tex`)

| ID | Descriptor | Técnica | Veredicto | Ref |
|---|---|---|---|---|
| T3.01 | Humidex f(T,h) tabla (Bucaramanga/IDEAM): estimación y límite de cociente incremental | interpretación de datos | | ver D3 |
| T3.02 | Relacionar 4 funciones con superficies (ln(x²+y²−1), e^{−x²−y²}, cos(x²+y²), x²−y³) | curvas de nivel | | |
| T3.03 | Dominio √((x+y)ln(x−y)) | desigualdades por casos | | |
| T3.04 | Dominio ln(−x+2+y)/√((x−y+1)ln(x+y+1)) | casos combinados | | |
| T3.05 | Dominio √(sen x · sen y) | periodicidad, tablero | | |
| T3.06 | Dominio de ⟨ln(t²−1), √(sen t), cos(1/t)⟩ | intersección de dominios | | |
| T3.07 | Gráfica de contorno: comportamiento de lím [f(h,0)−f(0,0)]/h | lectura de curvas de nivel | | |
| T3.08 | lím (x³+4x²+2y²)/(2x²+y²) = 2 | trayectorias + emparedado | | |
| T3.09 | f=xy²/(x²+y⁴): discontinua en (0,0) pero lím 0 por rectas | trayectoria x=y² | | |
| T3.10 | Continuidad en (0,0) de la función de T3.08 con f(0,0)=2 | definición de continuidad | | |
| T3.11 | Discontinuidad removible (misma función, f(0,0)=0) | redefinición | | |
| T3.12 | f=(x³y−xy³)/(x²+y²): continuidad y f_x, f_y en (0,0) | compresión, parciales por definición | | |

### T4 — Parciales y regla de la cadena → `planostangentes.tex` / `gradientes.tex`

| ID | Descriptor | Destino | Veredicto | Ref |
|---|---|---|---|---|
| T4.01 | Bosquejo f(x,y)=cos x (cilindro) | funvectoriales o planostangentes | | |
| T4.02 | Parciales de x²−x³y²+y⁴ | planostangentes | | |
| T4.03 | z_x, z_y de x/y² | planostangentes | | |
| T4.04 | f_x(1,2) de x³y²−4xy⁴+5 | planostangentes | | |
| T4.05 | f_z de ln(x²+y²+z²) | planostangentes | | |
| T4.06 | f_x de (x²+y²)^{2/3} incl. (0,0) por definición | planostangentes | | |
| T4.07 | Segundas parciales de sen(x−2y); f_xy=f_yx | planostangentes | | |
| T4.08 | Laplace: z=y/(x²+y²) | planostangentes | | |
| T4.09 | Laplace: u=e^x sen y | planostangentes | | |
| T4.10 | f=∫_x^y √(1+t³)dt: parciales vía 1TFC | planostangentes | | |
| T4.11 | Razón de cambio de V=xyz respecto al ancho | planostangentes | | |
| T4.12 | Vectores tangentes T_x, T_y a z=f(x,y) | planostangentes | | |
| T4.13 | Plano tangente al elipsoide: forma xx₀/a²+yy₀/b²+zz₀/c²=1 | planostangentes o gradientes | | |
| T4.14 | Elipsoide x²+2y²+3z²=1: tangente ∥ 3x−y+3z=1 | gradientes | | |
| T4.15 | y=x²+z²: tangente ∥ x+2y+3z=1 | gradientes | | |
| T4.16 | ∂z/∂x implícita en x²+y²+z²=25 | gradientes (§implícita) | | |
| T4.17 | Tangente horizontal en z+x²+y²=6 | planostangentes | | |
| T4.18 | dz total de z=x²y⁵ | planostangentes (§Diferenciales) | | |
| T4.19 | Linealizar x³yz en (1,2,3) | planostangentes (§Linealización) | | |
| T4.20 | Aproximar √(3.02²+3.99²) por diferenciales | planostangentes | | |
| T4.21 | Placa circular: dA con r: 10→10.1 | planostangentes | | |
| T4.22 | Diferenciable ⇒ continua (demostración) | planostangentes | | |
| T4.23 | dz/dt con z=x²+y², x=sen t, y=cos t | gradientes (§cadena) | | |
| T4.24 | ∂z/∂s con z=e^{xy}, x=s/t, y=t²s | gradientes | | |
| T4.25 | ∂w/∂t, ∂w/∂s (w=xyz y w=x²+y²+z², 2 casos) | gradientes | | |
| T4.26 | dy/dx implícita: cos(x+y)=y sen x | gradientes | | |
| T4.27 | w_rr con cadena de 2º orden | gradientes | | |
| T4.28 | d²P/dt² de P=kT/V (contexto químico) | gradientes | | |

### T5 — Gradientes, direccionales, críticos → `gradientes.tex` / `multiplicadoresintdobles.tex`

| ID | Descriptor | Destino | Veredicto | Ref |
|---|---|---|---|---|
| T5.01 | ∇ de x²−x³y²+y⁴ | gradientes | | |
| T5.02 | ∇ de xy²/z³ | gradientes | | |
| T5.03 | ∇ de e^{x²y}+ln(x+y) en (1,1) | gradientes | | |
| T5.04 | Química s=ln(zy)/x: dirección máx + D_u en ⟨0,1,2⟩ | gradientes | | |
| T5.05 | UGV en colina: dirección de máxima pendiente (suroeste) | gradientes | | |
| T5.06 | D_u de xy²z³ en (1,1,1), v=⟨2,1,−2⟩ | gradientes | | |
| T5.07 | D_u de e^x sen y en (0,π/4), v=i−j | gradientes | | |
| T5.08 | Máx D_u de √(x²+y²) en (3,4) | gradientes | | |
| T5.09 | ∇f=0 para x²+y²−4x+6y | gradientes | | |
| T5.10 | Ángulo entre ∇f y ∇g en (1,1) | gradientes | | |
| T5.11 | Críticos de x²+2y²−4x+8y | multiplicadores | | |
| T5.12 | Críticos de x²+y²−4x+6y+10 | multiplicadores | | |
| T5.13 | Máx crecimiento de √(x²+y²+z²) en (3,4,12) | gradientes | | |
| T5.14 | D_u de arctan(y/x) hacia el origen | gradientes | | |
| T5.15 | Críticos de x³+y³−3xy+5 (silla + mínimo) | multiplicadores | | |
| T5.16 | Plano tangente a x²+2y²+3z²=23/3 vía ∇ | gradientes | | |
| T5.17 | Insecto en caja: T=xyz(1−x)(2−y)(3−z), enfriarse máx | gradientes | | |
| T5.18 | Montañeros T=ln(3xy+2x²−y): 3 incisos (dirección, D_u, nivel) | gradientes | | |
| T5.19 | Reacción T=−x³+4x²y−3y²: 3 incisos | gradientes | | |
| T5.20 | Potencial V=x²+y²+xy+5 en región y=(x−1)²−1, y=x | multiplicadores (extremos en región) | | |
| T5.21 | Críticos de 4x²−16x+4y²−4y+20 en región (frontera 3 tramos) | multiplicadores | | |
| T5.22 | Hallar a,b: D_u máx = 3√2 en bisectriz, f=e^{ax+by}cos(x+y) | gradientes | | |
| T5.23 | ¿∃ u con D_u f=√2? (respuesta: no existe) | gradientes | | |
| T5.24 | Extremos absolutos de x²+xy+y² en disco cerrado | multiplicadores | | |
| T5.25 | ∇f(1,2) a partir de dos direccionales dadas | gradientes | | |
| T5.26 | Críticos de (x²+y²)e^{−(x²+y²)}: mín absoluto + máx en circunferencia | multiplicadores | | |
| T5.27 | Paralelepípedo inscrito en 16x²+4y²+9z²=144 | multiplicadores | | |
| T5.28 | Vector normal a z=4x²+9y² en (1,1,13) | gradientes | | |
| T5.29 | Plano tangente a xyz=1 en (1,1,1) | gradientes | | |
| T5.30 | Recta normal a z=x²y en (2,1,4) (ecs. simétricas) | gradientes | | |
| T5.31 | Toda normal a la esfera pasa por el origen | gradientes | | |
| T5.32 | Ortogonalidad esfera x²+y²+z²=25 y cono x²+y²−z²=0 | gradientes | | |

### T6 — Optimización, Lagrange, int. dobles → `multiplicadoresintdobles.tex`

| ID | Descriptor | Técnica | Veredicto | Ref |
|---|---|---|---|---|
| T6.01 | Críticos de x²+y²−2x−4y | Hessiano | | |
| T6.02 | Críticos de x³−3xy² (Hessiano nulo → trayectorias) | criterio inconcluso | | |
| T6.03 | Lagrange: x+y en x²+y²=1 | 1 restricción | | |
| T6.04 | Lagrange: xy en x²+4y²=4 | 1 restricción | | |
| T6.05 | Lagrange: xyz en esfera unitaria | simetría | | |
| T6.06 | Lata cilíndrica, costo tapa=2×lateral | Lagrange aplicado | | |
| T6.07 | Caja con diagonal L: volumen máximo | sustitución + críticos | | |
| T6.08 | Acme: min Σ distancias² a 3 puntos | críticos libres | | |
| T6.09 | Paralelepípedo en elipsoide x²/a²+y²/b²+z²/c²=1 | implícita | | |
| T6.10 | Tanque 256 pies³ sin tapa: min área | sustitución | | |
| T6.11 | Caja en 9x²+36y²+4z²=36 | Lagrange | | |
| T6.12 | Caja: área 1500, aristas 200 (máx y mín) | Lagrange 2 restricciones | | |
| T6.13 | Curva intersección de 2 superficies más cercana al origen | Lagrange 2 restricciones | | |
| T6.14 | Plano ∩ cono: punto más alto y más bajo de la elipse | Lagrange 2 restricciones | | |
| T6.15 | ∬_{[0,1]²}(x+y) dA | doble directa | | |
| T6.16 | ∬ e^{x²}: inversión del orden | Fubini | | |
| T6.17 | ∬ x sobre 0≤y≤x≤2 | región tipo I | | |
| T6.18 | ∬ (x+y) sobre triángulo (0,0),(1,0),(1,1) | región tipo I | | |
| T6.19 | Volumen: x=4−y², z=0, z=x | doble como volumen | | |
| T6.20 | Volumen: z=x²+4y² sobre región entre y²=x y x²=y | región entre parábolas | | |
| T6.21 | Volumen en polares: z=10−3x²−3y² y z=4 | polares | | |

### T8 — Línea, Green, triples → `cap33.tex` / `cap34.tex` / `inttriples.tex`

| ID | Descriptor | Destino | Veredicto | Ref |
|---|---|---|---|---|
| T8.01 | Verificar Green: F=(2x³−y³, x³+y³) en anillo 1≤x²+y²≤4 | cap34 §Green | | |
| T8.02 | Green con curva abierta (t,sen t): cerrar con segmento, orientación | cap34 §Green | | |
| T8.03 | Identidad div(F×G)=G·rotF−F·rotG (ojo: verificar signo) | cap34 §Div y rot | | |
| T8.04 | f(x,y,z)=∫_C F con C segmento al punto: hallar f y probar ∇f=F | cap33 §Conservativos | | |
| T8.05 | ∫ de línea escalar: x+cos²z sobre hélice | cap33 §Línea escalar | | |
| T8.06 | Campo conservativo → potencial → TFC de línea | cap33 §Conservativos | | |
| T8.07 | ∭(x²+y²): paraboloide x²+y²=2z y plano z=2 (cilíndricas + Jacobiano) | inttriples | | |
| T8.08 | Volumen: cono z²=x²+y² ∩ esfera x²+y²+z²=4 (esféricas) | inttriples | | |
| T8.09 | Volumen: z=x²+3y² y z=12−x²/3 | inttriples o multiplicadores | | |
| T8.10 | Volumen: z=√x, z=0, y∈[0,3], x+z=2 | inttriples | | |
| T8.11 | Tetraedro (0,0,0),(⅓,0,0),(0,1,0),(0,0,1): volumen | inttriples | | |
| T8.12 | Centro de masa del cubo unitario, ρ=x²+y²+z² | inttriples §Masa | | |
| T8.13 | Centro de masa: y=x², y=3, z=0, z=6−⅔y², ρ=x | inttriples §Masa | | |

### EX — Examen Final Nov-2025 (Tema 2)

| ID | Descriptor | Destino | Veredicto | Ref |
|---|---|---|---|---|
| EX.01 | V/F Clairaut: ¿∃f con f_x=2x+xy², f_y=2xy? | planostangentes | | |
| EX.02 | Esféricas ρsen²φ=cosφ → identificar superficie cartesiana | inttriples §Cambio de variables | | |
| EX.03 | Partícula sale por la tangente en t=1: posición en t=2 | funvectoriales | | |
| EX.04 | ∫₀¹∫_{x²}^x f dydx a polares (opción múltiple) | multiplicadoresintdobles | | |
| EX.05 | V/F continuidad de √(xy)/(x²+y²−25) en |x|+|y|<1 | limvariasvariables | | |
| EX.06 | Depósito cilíndrico cerrado V=12: r y h óptimos | multiplicadores | | |
| EX.07 | Direcciones con D_u T = 0, T=100xy² en (3,−4) | gradientes | | |
| EX.08 | Extremos de y² con 5x⁴−y³+3y⁶=0 | multiplicadores | | |
| EX.09 | ∭: dentro de ρ=1, fuera de ρ=cosφ, sobre plano xy (esféricas) | inttriples | | |
| EX.10 | Área de superficie de f=1−x²+y sobre triángulo | cap34 o inttriples (según dónde viva área de superficie) | | |

---

## 5. PROMPT PARA CLAUDE CODE

> Copiar desde aquí hasta el final de la sección. Requiere este mismo archivo
> (`F9T_talleres_auditoria.md`) en la raíz del repo, junto a los 8 `.tex`.

```
Eres el ejecutor de la Fase 9-T del problemario de Cálculo III. Tu insumo maestro es
el archivo F9T_talleres_auditoria.md (este repo). El inventario de la sección 4
contiene los ~140 problemas de los talleres de refuerzo YA EXTRAÍDOS Y VERIFICADOS:
no necesitas leer los PDFs; trabaja exclusivamente contra ese inventario.

CONTEXTO DEL LIBRO
- Compilación: LuaLaTeX exclusivamente. El libro completo compila hoy con 0 errores;
  esa condición es invariante.
- Entornos: `prob` (problema resuelto) + `myproof` (solución), `rem`, `example`,
  `pasos`, `theorem`, `definition`. Los problemas propuestos van en la sección
  final "Problemas propuestos" de cada capítulo, en `enumerate`.
- Notación: usar `\sen` (no `\sin`) según la convención de unificación del proyecto.
  Verifica primero con grep qué usa cada archivo hoy y repórtalo; no mezcles.
- Figuras: solo pgfplots/TikZ con `shader=flat` y `samples<=20`. Prohibido insertar
  imágenes rasterizadas de GeoGebra.
- Reglas editoriales F8: R1 orden canónico (teoría → ejemplos → problemas resueltos
  de dificultad creciente → propuestos), R2 figura TikZ obligatoria donde el
  enunciado la pida o la solución la necesite, R3 profundidad de prueba escalonada.
- Archivos grandes: usa protocolo de ventana deslizante; nunca cargues un .tex
  completo si supera tu ventana cómoda de edición.

FASE A — AUDITORÍA (solo lectura, sin tocar los .tex)
Para cada ítem del inventario (T1.01 … EX.10):
1. Abre el/los archivo(s) destino indicados en la columna correspondiente y busca
   un problema estructuralmente equivalente: misma técnica central y dificultad
   comparable. La coincidencia de valores numéricos NO es requisito.
2. Asigna veredicto:
   - CUBIERTO: existe equivalente claro. Registra Ref (número de línea del \begin{prob}
     o \label si existe).
   - PARCIAL: existe algo del mismo tema pero falta la técnica específica del ítem
     (p. ej. hay Lagrange con 1 restricción pero no con 2). Registra Ref del más
     cercano y una nota de un renglón sobre qué falta.
   - FALTA: no hay nada comparable.
3. Escribe los resultados EN ESTE MISMO ARCHIVO, llenando las columnas Veredicto y
   Ref de las tablas de la sección 4. Un commit al cerrar cada taller:
   "F9T-A: auditoría T<n> (<x> cubiertos / <y> parciales / <z> faltantes)".
4. Al terminar los 8 bloques, agrega al final del archivo una sección
   "## 6. Resumen de auditoría" con: totales por veredicto y por capítulo, y los
   5 vacíos más graves a tu juicio (técnicas del examen final sin cobertura pesan doble).
Advertencia específica: en T8.03 la identidad correcta es
div(F×G) = G·(∇×F) − F·(∇×G); el taller original tiene los términos con signo
intercambiado. Si el problemario ya la tiene, verifica el signo; si la vas a
proponer como ítem nuevo, márcala "corregir signo respecto al taller".

FASE B — PLAN DE INSERCIÓN (solo escritura en este .md, aún sin tocar los .tex)
Para cada FALTA y cada PARCIAL, crea en una nueva sección "## 7. Plan de inserción"
un ítem atómico con este formato:

  ### F9T.<NN> — [origen: T5.22] [destino: gradientes.tex, §Derivada direccional, tras línea ~L]
  - Tipo: prob resuelto | propuesto | ambos
  - Enunciado: reformulado (según D1) — borrador de 1-3 líneas
  - Solución: esqueleto de pasos (no el desarrollo completo)
  - Figura: NO | SÍ → ítem TikZ separado F9T.<NN>f con descripción de la figura
  - Estimación: S (<30 min) / M (30-90) / L (>90)

Criterios de colocación:
- Problema con técnica nueva para el capítulo → prob resuelto en la sección temática,
  en el lugar que respete la progresión de dificultad (R1).
- Problema de práctica de una técnica ya ejemplificada → propuesto al final.
- Ítems del Examen Final (EX.*) → SIEMPRE reformular valores (isomorfo), nunca textual.
- T3.01 (humidex) queda en estado BLOQUEADO-D3: créale el ítem pero no lo planifiques
  hasta decisión del coordinador.
- No planifiques nada que dependa del Taller VII ausente (BLOQUEADO-D4).
Ordena los ítems F9T.NN por prioridad: (1º) técnicas del examen sin cobertura,
(2º) FALTA de talleres, (3º) PARCIAL. Commit: "F9T-B: plan de inserción (<n> ítems)".

FASE C — EJECUCIÓN (bloqueada)
NO ejecutes la Fase C en esta sesión. La Fase C se hará ítem por ítem, en sesiones
posteriores, cada una con este contrato: (a) un solo ítem F9T.NN por vez, (b) editar
solo el archivo destino, (c) compilar el capítulo (o el libro si hay tiempo) con
LuaLaTeX y verificar 0 errores antes del commit, (d) commit
"F9T-C: F9T.NN <descriptor corto>", (e) marcar el ítem como HECHO en este .md.
Si un ítem revela un problema estructural del capítulo (numeración, secciones,
notación), NO lo arregles de paso: regístralo en "## 8. Hallazgos" y sigue.

REGLAS GENERALES
- Nunca borres ni reordenes contenido existente de los .tex en las fases A y B.
- Si el inventario y el .tex se contradicen (p. ej. una sección no existe), gana el
  .tex; anota la discrepancia en "## 8. Hallazgos".
- Reporta al final de la sesión: fases completadas, commits, bloqueos abiertos.
```

---

## Anexo — Estado actual de los capítulos (2026-07-17)

| Archivo | Capítulo | Líneas | Entornos de problema (aprox.) |
|---|---|---|---|
| `funvectoriales.tex` | Funciones vectoriales y de varias variables | 1804 | alto |
| `limvariasvariables.tex` | Límites y continuidad en Rⁿ | 958 | 40 `prob` |
| `planostangentes.tex` | Dif. parcial, plano tangente y diferenciabilidad | 1050 | medio |
| `gradientes.tex` | Regla de la cadena, direccional y gradientes | 1097 | medio |
| `multiplicadoresintdobles.tex` | Optimización: libres y con restricciones | 1026 | medio |
| `inttriples.tex` | Integrales triples | 845 | medio |
| `cap33.tex` | Campos vectoriales e integrales de línea | 939 | medio |
| `cap34.tex` | Int. de superficie y teoremas integrales | 1432 | alto |
