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

**Taller VII:** confirmado que NO existe (D4 resuelta, 2026-07-18). El inventario
queda completo con los 7 talleres + examen.

---

## 3. Decisiones bloqueantes — RESUELTAS (coordinador, 2026-07-18)

- **D1 — RESUELTA: (c) isomorfos para TODO** (talleres y examen): misma estructura y
  técnica, valores nuevos, redacción propia del problemario.
- **D2 — RESUELTA: TikZ obligatorio.** Toda figura se crea en TikZ/pgfplots siguiendo
  `figuras_guia.tex` (shader=flat/flat corner, samples≤20, paleta blue!70!black /
  red!70!black, \node separados con anchor explícito, figure[H]+caption+label).
  No se admite el estado "figura pendiente".
- **D3 — RESUELTA: se incluye un ISOMORFO de humidex** (problema contextualizado de
  tabla de datos con estimación de parciales por cocientes incrementales, con contexto
  y valores nuevos). Ver F9T.20.
- **D4 — RESUELTA: el Taller VII NO existe.** Se elimina la advertencia del inventario;
  nada queda bloqueado por este motivo.
- **D5 — RESUELTA: figura TikZ siempre**, aunque el original sea captura de GeoGebra.
  En propuestos se puede conservar "verifique con GeoGebra" como coletilla opcional.

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
| T3.01 | Humidex f(T,h) tabla (Bucaramanga/IDEAM): estimación y límite de cociente incremental | interpretación de datos | FALTA | BLOQUEADO-D3; no hay problemas de interpretación de datos/tabla en el libro |
| T3.02 | Relacionar 4 funciones con superficies (ln(x²+y²−1), e^{−x²−y²}, cos(x²+y²), x²−y³) | curvas de nivel | PARCIAL | fv L1696–L1801 (curvas de nivel abundantes); falta ejercicio de emparejamiento función↔superficie |
| T3.03 | Dominio √((x+y)ln(x−y)) | desigualdades por casos | PARCIAL | fv L807 (√ y ln en cociente); falta producto dentro de la raíz con análisis de signos por casos |
| T3.04 | Dominio ln(−x+2+y)/√((x−y+1)ln(x+y+1)) | casos combinados | PARCIAL | fv L807; misma carencia que T3.03, con combinación más compleja |
| T3.05 | Dominio √(sen x · sen y) | periodicidad, tablero | FALTA | ningún dominio con estructura periódica/tablero |
| T3.06 | Dominio de ⟨ln(t²−1), √(sen t), cos(1/t)⟩ | intersección de dominios | FALTA | hay continuidad de r(t) (fv L1644) pero no dominio de función vectorial |
| T3.07 | Gráfica de contorno: comportamiento de lím [f(h,0)−f(0,0)]/h | lectura de curvas de nivel | FALTA | no hay problemas de lectura/estimación sobre mapa de contorno |
| T3.08 | lím (x³+4x²+2y²)/(2x²+y²) = 2 | trayectorias + emparedado | CUBIERTO | lv L254 (racional, límite no nulo) + emparedado lv L638 |
| T3.09 | f=xy²/(x²+y⁴): discontinua en (0,0) pero lím 0 por rectas | trayectoria x=y² | CUBIERTO | lv L377 (rectas 0, parábola ½); también example L148 |
| T3.10 | Continuidad en (0,0) de la función de T3.08 con f(0,0)=2 | definición de continuidad | CUBIERTO | lv L798 (example por partes) + L892 |
| T3.11 | Discontinuidad removible (misma función, f(0,0)=0) | redefinición | CUBIERTO | lv L717, L749, L768, L915 |
| T3.12 | f=(x³y−xy³)/(x²+y²): continuidad y f_x, f_y en (0,0) | compresión, parciales por definición | CUBIERTO | lv L798 (continuidad) + pt L434 (parciales por definición en (0,0)) |

### T4 — Parciales y regla de la cadena → `planostangentes.tex` / `gradientes.tex`

| ID | Descriptor | Destino | Veredicto | Ref |
|---|---|---|---|---|
| T4.01 | Bosquejo f(x,y)=cos x (cilindro) | funvectoriales o planostangentes | FALTA | fv no trata cilindros (cf. T1.06); pt no tiene bosquejos de superficie |
| T4.02 | Parciales de x²−x³y²+y⁴ | planostangentes | CUBIERTO | pt L951 (propuesto a) + example L158 |
| T4.03 | z_x, z_y de x/y² | planostangentes | CUBIERTO | pt L158 (example a, cociente x/y en exponente) + L951 |
| T4.04 | f_x(1,2) de x³y²−4xy⁴+5 | planostangentes | CUBIERTO | pt L655 (evalúa f_x(1,2), f_y(1,2) de x²y³) |
| T4.05 | f_z de ln(x²+y²+z²) | planostangentes | CUBIERTO | pt L962 (propuesto h, función idéntica) + example L376 |
| T4.06 | f_x de (x²+y²)^{2/3} incl. (0,0) por definición | planostangentes | CUBIERTO | pt L434 (parciales por definición en (0,0), función por partes) |
| T4.07 | Segundas parciales de sen(x−2y); f_xy=f_yx | planostangentes | CUBIERTO | pt L250 (example + Clairaut) + propuestos L967, L979 |
| T4.08 | Laplace: z=y/(x²+y²) | planostangentes | CUBIERTO | pt L495 (ln(x²+y²) satisface Laplace) + L1015 (armónica) |
| T4.09 | Laplace: u=e^x sen y | planostangentes | CUBIERTO | pt L495 + L967 b (segundas de e^x cos y) |
| T4.10 | f=∫_x^y √(1+t³)dt: parciales vía 1TFC | planostangentes | FALTA | no hay parciales vía Teorema Fundamental del Cálculo |
| T4.11 | Razón de cambio de V=xyz respecto al ancho | planostangentes | PARCIAL | gr L117 (tasas de caja, pero vía cadena); falta interpretar una parcial sola como razón de cambio |
| T4.12 | Vectores tangentes T_x, T_y a z=f(x,y) | planostangentes | PARCIAL | pt L60–L114 (interpretación geométrica + figura); falta problema que construya ⟨1,0,f_x⟩, ⟨0,1,f_y⟩ |
| T4.13 | Plano tangente al elipsoide: forma xx₀/a²+yy₀/b²+zz₀/c²=1 | planostangentes o gradientes | PARCIAL | pt L690, L1003 (elipsoides numéricos); falta la deducción simbólica general |
| T4.14 | Elipsoide x²+2y²+3z²=1: tangente ∥ 3x−y+3z=1 | gradientes | CUBIERTO | pt L711 + L736 (misma técnica: ∇ ∥ normal dado) |
| T4.15 | y=x²+z²: tangente ∥ x+2y+3z=1 | gradientes | CUBIERTO | pt L711 (problema idéntico) |
| T4.16 | ∂z/∂x implícita en x²+y²+z²=25 | gradientes (§implícita) | CUBIERTO | gr L335 + example L254 + propuestos L1023, L1046 |
| T4.17 | Tangente horizontal en z+x²+y²=6 | planostangentes | CUBIERTO | pt L711 (tangente ∥ plano dado; caso normal ⟨0,0,1⟩ es idéntico) |
| T4.18 | dz total de z=x²y⁵ | planostangentes (§Diferenciales) | CUBIERTO | pt L839 (definición) + L1041 (propuesto dw) |
| T4.19 | Linealizar x³yz en (1,2,3) | planostangentes (§Linealización) | PARCIAL | pt L775, L807 (linealización en 2 variables); falta linealizar f(x,y,z) de 3 variables |
| T4.20 | Aproximar √(3.02²+3.99²) por diferenciales | planostangentes | CUBIERTO | pt L775 (example casi idéntico: √(x²+y²) en (3,4)) |
| T4.21 | Placa circular: dA con r: 10→10.1 | planostangentes | CUBIERTO | pt L1029 (error máximo en área de rectángulo con diferenciales) |
| T4.22 | Diferenciable ⇒ continua (demostración) | planostangentes | PARCIAL | pt L904 (teorema con esbozo de 2 líneas); falta la demostración completa |
| T4.23 | dz/dt con z=x²+y², x=sen t, y=cos t | gradientes (§cadena) | CUBIERTO | gr L28 (example Caso 1) + propuesto L1005 |
| T4.24 | ∂z/∂s con z=e^{xy}, x=s/t, y=t²s | gradientes | CUBIERTO | gr L289 (z=e^{xy}, x=st, y=s+t, casi idéntico) + example L197 |
| T4.25 | ∂w/∂t, ∂w/∂s (w=xyz y w=x²+y²+z², 2 casos) | gradientes | CUBIERTO | gr L289 (Caso 2) + L117 (cadena con 3 variables intermedias) |
| T4.26 | dy/dx implícita: cos(x+y)=y sen x | gradientes | PARCIAL | gr L238–L363 (implícita solo para F(x,y,z)); falta el caso dy/dx=−F_x/F_y con F(x,y)=0 |
| T4.27 | w_rr con cadena de 2º orden | gradientes | FALTA | no hay regla de la cadena de segundo orden en el cap. |
| T4.28 | d²P/dt² de P=kT/V (contexto químico) | gradientes | FALTA | sin equivalente; requiere cadena de 2º orden (cf. T4.27) |

### T5 — Gradientes, direccionales, críticos → `gradientes.tex` / `multiplicadoresintdobles.tex`

| ID | Descriptor | Destino | Veredicto | Ref |
|---|---|---|---|---|
| T5.01 | ∇ de x²−x³y²+y⁴ | gradientes | CUBIERTO | gr L407 (example) + propuesto L1014 |
| T5.02 | ∇ de xy²/z³ | gradientes | CUBIERTO | gr L1014 (propuestos c, d en 3 variables) |
| T5.03 | ∇ de e^{x²y}+ln(x+y) en (1,1) | gradientes | CUBIERTO | gr L779 (∇ evaluado en punto) + L818 |
| T5.04 | Química s=ln(zy)/x: dirección máx + D_u en ⟨0,1,2⟩ | gradientes | CUBIERTO | gr L691 (D_u) + L818 (dir. máx) + propuestos contextualizados L1037ss |
| T5.05 | UGV en colina: dirección de máxima pendiente (suroeste) | gradientes | CUBIERTO | gr L1050 (montaña) + L1037 (insecto colina) |
| T5.06 | D_u de xy²z³ en (1,1,1), v=⟨2,1,−2⟩ | gradientes | PARCIAL | gr L691 (D_u solo en 2 var) + L818c (∇ 3 var); falta D_u con vector dado en 3 variables |
| T5.07 | D_u de e^x sen y en (0,π/4), v=i−j | gradientes | CUBIERTO | gr L645 (example idéntico salvo v) + L691b (e^x cos y, v=⟨1,−1⟩) |
| T5.08 | Máx D_u de √(x²+y²) en (3,4) | gradientes | CUBIERTO | gr L818 (dirección y tasa máxima, 3 incisos) |
| T5.09 | ∇f=0 para x²+y²−4x+6y | gradientes | CUBIERTO | mi L909a + L920 (críticos de cuadráticas) |
| T5.10 | Ángulo entre ∇f y ∇g en (1,1) | gradientes | FALTA | no hay problema de ángulo entre dos gradientes |
| T5.11 | Críticos de x²+2y²−4x+8y | multiplicadores | CUBIERTO | mi L224 (example) + propuesto L920 |
| T5.12 | Críticos de x²+y²−4x+6y+10 | multiplicadores | CUBIERTO | mi L224 + L920 |
| T5.13 | Máx crecimiento de √(x²+y²+z²) en (3,4,12) | gradientes | CUBIERTO | gr L818c (dir. y tasa máx en 3 variables) |
| T5.14 | D_u de arctan(y/x) hacia el origen | gradientes | CUBIERTO | gr L779a (D_u en dirección de P a Q) |
| T5.15 | Críticos de x³+y³−3xy+5 (silla + mínimo) | multiplicadores | CUBIERTO | mi L920 item 3 (x³+y³−3xy, idéntico salvo constante) |
| T5.16 | Plano tangente a x²+2y²+3z²=23/3 vía ∇ | gradientes | CUBIERTO | gr L964 (prob a-b-c) + example L916 |
| T5.17 | Insecto en caja: T=xyz(1−x)(2−y)(3−z), enfriarse máx | gradientes | CUBIERTO | gr L1059, L1073 (insecto enfriarse) + L1037 (3 var) |
| T5.18 | Montañeros T=ln(3xy+2x²−y): 3 incisos (dirección, D_u, nivel) | gradientes | PARCIAL | gr L1037/L691 cubren 2 incisos; falta inciso "dirección sin cambio de T" (tangente a curva de nivel) |
| T5.19 | Reacción T=−x³+4x²y−3y²: 3 incisos | gradientes | PARCIAL | misma carencia que T5.18 |
| T5.20 | Potencial V=x²+y²+xy+5 en región y=(x−1)²−1, y=x | multiplicadores (extremos en región) | CUBIERTO | mi L572 (placa circular resuelta) + L909 (rect./círculo/triángulo) |
| T5.21 | Críticos de 4x²−16x+4y²−4y+20 en región (frontera 3 tramos) | multiplicadores | CUBIERTO | mi L909c (triángulo, 3 tramos) + example L572 |
| T5.22 | Hallar a,b: D_u máx = 3√2 en bisectriz, f=e^{ax+by}cos(x+y) | gradientes | FALTA | sin equivalente (problema inverso de parámetros) |
| T5.23 | ¿∃ u con D_u f=√2? (respuesta: no existe) | gradientes | FALTA | no hay problema sobre el rango \|D_u f\|≤‖∇f‖ |
| T5.24 | Extremos absolutos de x²+xy+y² en disco cerrado | multiplicadores | CUBIERTO | mi L909b (xy en disco) + example L572 |
| T5.25 | ∇f(1,2) a partir de dos direccionales dadas | gradientes | FALTA | sin equivalente (reconstruir ∇f desde dos D_u, sistema lineal) |
| T5.26 | Críticos de (x²+y²)e^{−(x²+y²)}: mín absoluto + máx en circunferencia | multiplicadores | PARCIAL | mi L224/L920 (críticos libres); falta función radial con máximos en toda una circunferencia |
| T5.27 | Paralelepípedo inscrito en 16x²+4y²+9z²=144 | multiplicadores | PARCIAL | mi L982 (caja máx con restricción de área vía Lagrange); falta caja inscrita en elipsoide (cf. T6.09) |
| T5.28 | Vector normal a z=4x²+9y² en (1,1,13) | gradientes | CUBIERTO | gr L916 (example) + L964 |
| T5.29 | Plano tangente a xyz=1 en (1,1,1) | gradientes | CUBIERTO | gr L964c + pt L1036 (x²y+y²z+z²x=3 en (1,1,1)) |
| T5.30 | Recta normal a z=x²y en (2,1,4) (ecs. simétricas) | gradientes | CUBIERTO | gr L964 (rectas normales en forma simétrica) |
| T5.31 | Toda normal a la esfera pasa por el origen | gradientes | FALTA | sin equivalente (propiedad general demostrativa) |
| T5.32 | Ortogonalidad esfera x²+y²+z²=25 y cono x²+y²−z²=0 | gradientes | FALTA | no hay problemas de superficies ortogonales (∇F⊥∇G en la intersección) |

### T6 — Optimización, Lagrange, int. dobles → `multiplicadoresintdobles.tex`

| ID | Descriptor | Técnica | Veredicto | Ref |
|---|---|---|---|---|
| T6.01 | Críticos de x²+y²−2x−4y | Hessiano | CUBIERTO | mi L224 (example) + L909a (misma función) + L920 |
| T6.02 | Críticos de x³−3xy² (Hessiano nulo → trayectorias) | criterio inconcluso | CUBIERTO | mi L937 (función idéntica, 3 incisos) + L948 (x²y², D=0) |
| T6.03 | Lagrange: x+y en x²+y²=1 | 1 restricción | CUBIERTO | mi L869 (problema dual x²+y² s.a. x+y=1) + L967 |
| T6.04 | Lagrange: xy en x²+4y²=4 | 1 restricción | CUBIERTO | mi L731 (example xy en circunferencia) + L967-1 |
| T6.05 | Lagrange: xyz en esfera unitaria | simetría | CUBIERTO | mi L967 item 2 (idéntico) |
| T6.06 | Lata cilíndrica, costo tapa=2×lateral | Lagrange aplicado | CUBIERTO | mi L425 (caja con costos ponderados 1.5×, resuelto) + L1006 (lata propuesta) |
| T6.07 | Caja con diagonal L: volumen máximo | sustitución + críticos | CUBIERTO | mi L448 (caja vértice en plano) + L982 (caja con área dada); misma técnica |
| T6.08 | Acme: min Σ distancias² a 3 puntos | críticos libres | PARCIAL | mi L309 (mín. distancia a plano, críticos libres); falta suma de distancias² a varios puntos |
| T6.09 | Paralelepípedo en elipsoide x²/a²+y²/b²+z²/c²=1 | implícita | FALTA | no hay caja inscrita en elipsoide (cf. T5.27) |
| T6.10 | Tanque 256 pies³ sin tapa: min área | sustitución | CUBIERTO | mi L494 (acuario, técnica idéntica) + L1024 (caja sin tapa) |
| T6.11 | Caja en 9x²+36y²+4z²=36 | Lagrange | FALTA | cf. T6.09 (mismo vacío) |
| T6.12 | Caja: área 1500, aristas 200 (máx y mín) | Lagrange 2 restricciones | FALTA | no hay Lagrange con 2 restricciones en el cap. |
| T6.13 | Curva intersección de 2 superficies más cercana al origen | Lagrange 2 restricciones | FALTA | cf. T6.12 |
| T6.14 | Plano ∩ cono: punto más alto y más bajo de la elipse | Lagrange 2 restricciones | FALTA | cf. T6.12 |
| T6.15 | ∬_{[0,1]²}(x+y) dA | doble directa | CUBIERTO | ai L49 (example) + L294 (prob rectángulos) |
| T6.16 | ∬ e^{x²}: inversión del orden | Fubini | CUBIERTO | ai L411 (cambio de orden resuelto) + propuestos L1525 (sen y²), L1530 (e^{x³}) |
| T6.17 | ∬ x sobre 0≤y≤x≤2 | región tipo I | CUBIERTO | ai L336-2 (∬x entre parábolas) + L1519 (tipo II con x) |
| T6.18 | ∬ (x+y) sobre triángulo (0,0),(1,0),(1,1) | región tipo I | CUBIERTO | ai L336-1 (x+y región general) + example L574 (triángulo) |
| T6.19 | Volumen: x=4−y², z=0, z=x | doble como volumen | CUBIERTO | ai L1406 (tetraedro) + L1572 (volumen bajo z=3+x); misma técnica |
| T6.20 | Volumen: z=x²+4y² sobre región entre y²=x y x²=y | región entre parábolas | CUBIERTO | ai L521 (example volumen) + L336-2 y L1512 (región entre parábolas) |
| T6.21 | Volumen en polares: z=10−3x²−3y² y z=4 | polares | PARCIAL | ai L1536 (paraboloide hasta z=0 en polares); falta volumen entre paraboloide y plano z=c>0 (hallar la proyección) |

### T8 — Línea, Green, triples → `cap33.tex` / `cap34.tex` / `inttriples.tex`

| ID | Descriptor | Destino | Veredicto | Ref |
|---|---|---|---|---|
| T8.01 | Verificar Green: F=(2x³−y³, x³+y³) en anillo 1≤x²+y²≤4 | cap34 §Green | PARCIAL | c34 L168 (verificación en disco) + L1391 (rectángulo); falta Green en anillo (región múltiplemente conexa, cf. c33 L920) |
| T8.02 | Green con curva abierta (t,sen t): cerrar con segmento, orientación | cap34 §Green | FALTA | no hay Green cerrando una curva abierta con un segmento auxiliar |
| T8.03 | Identidad div(F×G)=G·rotF−F·rotG (ojo: verificar signo) | cap34 §Div y rot | PARCIAL | c34 L1418 (identidad div(rot F)=0 propuesta); falta div(F×G)=G·(∇×F)−F·(∇×G) — al insertarla, corregir signo respecto al taller |
| T8.04 | f(x,y,z)=∫_C F con C segmento al punto: hallar f y probar ∇f=F | cap33 §Conservativos | PARCIAL | c33 L728, L841 (potencial por integración parcial + TFC); falta construir f como integral de línea sobre segmento |
| T8.05 | ∫ de línea escalar: x+cos²z sobre hélice | cap33 §Línea escalar | CUBIERTO | c33 L375 (example hélice) + L861 (masa de alambre helicoidal) + c34 L1372 |
| T8.06 | Campo conservativo → potencial → TFC de línea | cap33 §Conservativos | CUBIERTO | c33 L728 (example con el flujo completo) + L812, L841; c34 L414 |
| T8.07 | ∭(x²+y²): paraboloide x²+y²=2z y plano z=2 (cilíndricas + Jacobiano) | inttriples | CUBIERTO | it L538 (cilíndricas, integrando x²+y²) + example L514 (paraboloide) |
| T8.08 | Volumen: cono z²=x²+y² ∩ esfera x²+y²+z²=4 (esféricas) | inttriples | CUBIERTO | it L672 (misma región esfera∩cono en esféricas) + L754 |
| T8.09 | Volumen: z=x²+3y² y z=12−x²/3 | inttriples o multiplicadores | PARCIAL | it L802, L811 (paraboloide-plano); falta volumen entre dos paraboloides (proyección por igualación) |
| T8.10 | Volumen: z=√x, z=0, y∈[0,3], x+z=2 | inttriples | PARCIAL | it L69, L321 (volúmenes rectangulares con planos); falta sólido con techo mixto (z=√x y plano) que exige partir la región |
| T8.11 | Tetraedro (0,0,0),(⅓,0,0),(0,1,0),(0,0,1): volumen | inttriples | CUBIERTO | it L69 (example tetraedro) + propuestos L797, L807 |
| T8.12 | Centro de masa del cubo unitario, ρ=x²+y²+z² | inttriples §Masa | CUBIERTO | it L711 (∭(x²+y²+z²) sobre el cubo = masa) + L222, L724 (centro de masa) |
| T8.13 | Centro de masa: y=x², y=3, z=0, z=6−⅔y², ρ=x | inttriples §Masa | PARCIAL | it L222 (centro de masa con ρ constante) + L775 (ρ variable solo planteado/CAS); falta centro de masa 3D con ρ variable resuelto a mano |

### EX — Examen Final Nov-2025 (Tema 2)

| ID | Descriptor | Destino | Veredicto | Ref |
|---|---|---|---|---|
| EX.01 | V/F Clairaut: ¿∃f con f_x=2x+xy², f_y=2xy? | planostangentes | CUBIERTO | c33 L829 (¿campo conservativo? = misma técnica) + pt L979, L987 (V/F Clairaut) |
| EX.02 | Esféricas ρsen²φ=cosφ → identificar superficie cartesiana | inttriples §Cambio de variables | FALTA | no hay identificación de superficie cartesiana desde ecuación esférica |
| EX.03 | Partícula sale por la tangente en t=1: posición en t=2 | funvectoriales | PARCIAL | fv L325 (velocidad/derivada); falta recta tangente + movimiento sobre ella (cf. T2.03) |
| EX.04 | ∫₀¹∫_{x²}^x f dydx a polares (opción múltiple) | apintdobles (ver H1) | PARCIAL | ai L1162 (cambio a polares, región circular); falta conversión de región NO circular (r=f(θ) de parábola/recta) |
| EX.05 | V/F continuidad de √(xy)/(x²+y²−25) en \|x\|+\|y\|<1 | limvariasvariables | PARCIAL | lv L798, L892 (continuidad en regiones); falta V/F que combine el dominio (xy≥0) con la región dada |
| EX.06 | Depósito cilíndrico cerrado V=12: r y h óptimos | multiplicadores | CUBIERTO | mi L1006 (lata cilíndrica 2 L, idéntico) |
| EX.07 | Direcciones con D_u T = 0, T=100xy² en (3,−4) | gradientes | FALTA | no hay problema de direcciones con derivada direccional nula (cf. T5.18/T5.19) |
| EX.08 | Extremos de y² con 5x⁴−y³+3y⁶=0 | multiplicadores | CUBIERTO | mi L731 (Lagrange) + L770/L797 (casos degenerados ∇g=0 y candidato falso) |
| EX.09 | ∭: dentro de ρ=1, fuera de ρ=cosφ, sobre plano xy (esféricas) | inttriples | PARCIAL | it L672 (esféricas esfera∩cono) + L775 (entre esferas, solo planteo/CAS); falta límite interior ρ=cosφ (esfera desplazada) |
| EX.10 | Área de superficie de f=1−x²+y sobre triángulo | apintdobles §Área de superficie (ver H1) | CUBIERTO | ai L1562 (plano sobre triángulo) + L942 (example paraboloide) + it L816 |

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

## 6. Resumen de auditoría (Fase A completa, 2026-07-18)

### Totales por veredicto

| Bloque | CUBIERTO | PARCIAL | FALTA | Total |
|---|---|---|---|---|
| T1 | 1 | 6 | 4 | 11 |
| T2 | 3 | 4 | 6 | 13 |
| T3 | 5 | 3 | 4 | 12 |
| T4 | 18 | 6 | 4 | 28 |
| T5 | 21 | 5 | 6 | 32 |
| T6 | 14 | 2 | 5 | 21 |
| T8 | 6 | 6 | 1 | 13 |
| EX | 4 | 4 | 2 | 10 |
| **Total** | **72** | **36** | **32** | **140** |

### Estado por capítulo destino

- `funvectoriales.tex` — el más débil: concentra los FALTA/PARCIAL de T1 (cónicas con
  elementos, cilindros, completar cuadrados en cuádricas) y T2 (T̂ unitario, recta
  tangente, intersección de superficies, cónicas rotadas), más los dominios de T3.02–06.
- `limvariasvariables.tex` — bien cubierto (T3 núcleo de límites/continuidad completo);
  vacíos solo en interpretación de datos (T3.01, bloqueado D3), contorno (T3.07) y EX.05.
- `planostangentes.tex` — muy bien cubierto (18/28 de T4); vacíos puntuales: parciales
  vía 1TFC (T4.10), vectores tangentes T_x/T_y, linealización en 3 variables.
- `gradientes.tex` — bien cubierto en lo básico; vacíos: cadena de 2º orden (T4.27–28),
  D_u nula (T5.18/19, EX.07), problemas inversos de ∇ (T5.22/23/25), ángulo entre
  gradientes (T5.10), normales de esfera/superficies ortogonales (T5.31/32).
- `multiplicadoresintdobles.tex` — optimización libre y Lagrange 1 restricción muy
  cubiertos; vacío estructural: Lagrange con 2 restricciones (T6.12–14) y caja inscrita
  en elipsoide (T5.27, T6.09, T6.11 — tres ítems del mismo vacío).
- `apintdobles.tex` — muy bien cubierto; solo falta conversión a polares de regiones no
  circulares (EX.04).
- `inttriples.tex` — bien cubierto en cilíndricas/esféricas básicas; vacíos: superficie
  desde ecuación esférica (EX.02), esfera desplazada ρ=cosφ (EX.09), volumen entre dos
  paraboloides (T8.09), centro de masa 3D con ρ variable resuelto (T8.13).
- `cap33.tex` / `cap34.tex` — línea/conservativos/Green bien cubiertos; vacíos: Green
  cerrando curva abierta (T8.02), Green en anillo (T8.01), identidad div(F×G) (T8.03),
  potencial como integral de línea (T8.04).

### Los 5 vacíos más graves (técnicas del examen pesan doble)

1. **EX.07 + T5.18/T5.19 — direcciones con D_u = 0** (tangente a la curva de nivel):
   técnica del examen final sin ningún equivalente; además cierra los incisos "nivel" de
   dos problemas contextualizados de taller.
2. **EX.02 — identificar superficie cartesiana desde ecuación esférica**: técnica del
   examen sin cobertura; encaja natural en `inttriples.tex` §Coordenadas esféricas.
3. **Lagrange con 2 restricciones (T6.12, T6.13, T6.14)**: tres ítems FALTA por un
   único vacío estructural del capítulo de optimización; el teorema ni se enuncia.
4. **Bloque T2 de funciones vectoriales (6 FALTA)**: en particular T̂ unitario (T2.04),
   recta tangente a una curva (T2.03→EX.03, enlaza con el examen) y parametrización de
   la intersección de superficies (T2.09, clásico de examen).
5. **Regla de la cadena de 2º orden (T4.27, T4.28)**: técnica estándar de evaluación
   (w_rr, d²P/dt²) ausente de `gradientes.tex`.

---

## 7. Plan de inserción (Fase B, 2026-07-18)

Ítems ordenados por prioridad: (1º) técnicas del examen sin cobertura o parciales,
(2º) FALTA de talleres, (3º) PARCIAL. Ítems que comparten un mismo vacío se fusionan
en un solo F9T.NN (se listan todos los orígenes). Convenciones: Tipo = prob resuelto |
propuesto | ambos; Estimación S (<30 min) / M (30–90) / L (>90). Por D1 resuelta:
**TODOS los enunciados se insertan como isomorfos** (estructura y técnica idénticas,
valores y redacción nuevos). Por D2/D5: toda figura es TikZ según `figuras_guia.tex`.

### Prioridad 1 — Examen final

### F9T.01 — HECHO (2026-07-18) — [origen: EX.07, T5.18, T5.19] [destino: gradientes.tex, §Derivada direccional, tras L850]
- Tipo: ambos
- Enunciado: la temperatura de una placa es T(x,y)=kxy² (valores isomorfos). En un punto dado, halle TODAS las direcciones u con D_u T=0 e interprete: son las tangentes a la curva de nivel. Propuestos: incisos "dirección sin cambio" estilo T5.18/T5.19.
- Solución: ∇T en el punto → D_u T=∇T·u=0 → sistema con ‖u‖=1 → dos direcciones opuestas ⊥ ∇T → interpretación geométrica.
- Figura: SÍ → F9T.01f: curva de nivel por el punto, ∇T y las dos direcciones tangentes (TikZ 2D).
- Estimación: M

### F9T.02 — [origen: EX.02] [destino: inttriples.tex, §Coordenadas esféricas, tras la definición L566]
- Tipo: ambos
- Enunciado: identifique la superficie cartesiana dada por la ecuación esférica ρ sen²φ = c·cosφ (isomorfo; resultado: paraboloide). Propuestos: ρ=c·cosφ (esfera desplazada), φ=c (cono).
- Solución: multiplicar por ρ → ρ²sen²φ=ρcosφ·c → x²+y²=cz → identificar.
- Figura: NO
- Estimación: S

### F9T.03 — [origen: EX.03, T2.03] [destino: funvectoriales.tex, §Funciones vectoriales (derivada), tras L325]
- Tipo: ambos
- Enunciado: (i) recta tangente a r(t) en t=t₀ (cierra T2.03); (ii) una partícula abandona la trayectoria en t=t₀ y sigue por la tangente a velocidad constante: posición en t=t₁ (isomorfo de EX.03).
- Solución: r'(t₀) → recta L(s)=r(t₀)+s·r'(t₀) → posición = r(t₀)+(t₁−t₀)r'(t₀).
- Figura: SÍ → F9T.03f: curva, punto de salida y rayo tangente (TikZ 2D o pgfplots 3D según curva elegida).
- Estimación: M

### F9T.04 — [origen: EX.04] [destino: apintdobles.tex, §Integrales dobles en polares, tras L1184]
- Tipo: ambos
- Enunciado: convierta ∫₀¹∫_{x²}^{x} f dy dx a coordenadas polares (isomorfo): región entre recta y parábola → límites r desde 0 hasta r=tanθ·secθ y θ∈[0,π/4].
- Solución: describir región → recta y=x: θ=π/4; parábola y=x²: r sinθ=r²cos²θ → r=tanθ secθ → armar la integral.
- Figura: SÍ → F9T.04f: región entre y=x², y=x con rayo genérico θ (TikZ 2D).
- Estimación: M

### F9T.05 — [origen: EX.05] [destino: limvariasvariables.tex, §Continuidad, tras los ejemplos de clasificación]
- Tipo: ambos
- Enunciado: V/F (isomorfo): "g(x,y)=√(xy)/(x²+y²−c) es continua en la región |x|+|y|<r". Analizar dominio (xy≥0 falla en cuadrantes II/IV) y el denominador.
- Solución: dominio de √(xy) → la región dada contiene puntos fuera del dominio → falsa (o ajustar región para variante verdadera); verificación de denominador ≠0.
- Figura: NO
- Estimación: S

### F9T.06 — [origen: EX.09] [destino: inttriples.tex, §Coordenadas esféricas, tras el prob L672]
- Tipo: prob resuelto
- Enunciado: volumen (o ∭ f) de la región dentro de ρ=a, fuera de ρ=a·cosφ, sobre el plano xy (isomorfo de EX.09).
- Solución: región: φ∈[0,π/2], ρ∈[a cosφ, a] → ∭ρ²senφ → integrar en ρ, luego φ, luego θ.
- Figura: SÍ → F9T.06f: corte en el plano xz mostrando ambas esferas y la región (TikZ 2D).
- Estimación: M

### Prioridad 2 — FALTA de talleres

### F9T.07 — [origen: T1.01] [destino: funvectoriales.tex, antes de §Superficies cuádricas]
- Tipo: ambos
- Enunciado: dada una cónica Ax²+By²+Cx+Dy+E=0 (hipérbola, valores tipo taller), obtener forma canónica por completar cuadrados y extraer centro, vértices, focos y asíntotas.
- Solución: completar cuadrados → canónica → elementos → bosquejo.
- Figura: SÍ → F9T.07f: hipérbola con asíntotas y focos (TikZ 2D).
- Estimación: M

### F9T.08 — [origen: T1.03] [destino: funvectoriales.tex, §Cuádricas (trazas), junto a paraboloides]
- Tipo: propuesto
- Enunciado: para el paraboloide −a x²+b y²=c z, halle la traza con x=0 e identifique vértice, foco y directriz de la parábola resultante.
- Solución: sustituir → parábola canónica → 4p → elementos.
- Figura: NO
- Estimación: S

### F9T.09 — [origen: T1.06] [destino: funvectoriales.tex, §Cuádricas, nueva subsec. breve "Cilindros"]
- Tipo: ambos
- Enunciado: mini-teoría (definición de cilindro: ecuación sin una variable) + prob: cilindro elíptico ax²+by²+cx+dy+e=0 → canónica, secciones z=c, bosquejo.
- Solución: completar cuadrados → elipse trasladada → generatrices paralelas al eje z.
- Figura: SÍ → F9T.09f: cilindro elíptico en 3D (pgfplots, shader=flat, samples≤20).
- Estimación: M

### F9T.10 — [origen: T1.11] [destino: funvectoriales.tex, §Funciones vectoriales (curvas), propuestos]
- Tipo: propuesto
- Enunciado: muestre que f(t)=(a·sinh t, b+c·cosh t) recorre una rama de hipérbola (identidad cosh²−sinh²=1) e indique cuál rama.
- Solución: despejar sinh/cosh → identidad → hipérbola; cosh t≥1 selecciona la rama.
- Figura: NO
- Estimación: S

### F9T.11 — [origen: T2.04] [destino: funvectoriales.tex, §Derivada de funciones vectoriales, tras la derivada]
- Tipo: ambos
- Enunciado: definición de vector tangente unitario T̂(t)=r'(t)/‖r'(t)‖ (rem breve) + prob: T̂(t₀) para una r(t) con componentes mixtas (isomorfo de T2.04).
- Solución: r'(t) → evaluar → normalizar.
- Figura: NO
- Estimación: M

### F9T.12 — [origen: T2.09] [destino: funvectoriales.tex, §Funciones vectoriales, tras curvas en el espacio]
- Tipo: prob resuelto
- Enunciado: parametrice la curva intersección del cilindro x²+y²=a² con el plano y+z=b y halle la recta tangente en un punto dado (isomorfo de T2.09).
- Solución: x=a cos t, y=a sen t, z=b−a sen t → t₀ del punto → r'(t₀) → recta tangente. Comentar la alternativa con raíz (dos cartas).
- Figura: SÍ → F9T.12f: cilindro + plano + curva intersección (pgfplots 3D, shader=flat).
- Estimación: M

### F9T.13 — [origen: T2.11] [destino: funvectoriales.tex, propuestos]
- Tipo: propuesto
- Enunciado: determine si las curvas r(t) y s(u) (componentes trigonométricas tipo taller) se intersectan y halle los puntos de intersección (parámetros independientes).
- Solución: igualar componente a componente con parámetros distintos → resolver el sistema → verificar en la tercera componente.
- Figura: NO
- Estimación: S

### F9T.14 — [origen: T2.10] [destino: funvectoriales.tex, propuestos]
- Tipo: propuesto
- Enunciado: dadas dos cuádricas S1, S2 con términos lineales (esferas/elipsoides), halle la recta perpendicular al plano dado que pasa por el punto medio del segmento entre sus centros (reformulación tipo taller).
- Solución: completar cuadrados en ambas → centros → vector director → ecuación de la recta.
- Figura: NO
- Estimación: M

### F9T.15 — [origen: T2.07] [destino: funvectoriales.tex, propuestos]
- Tipo: propuesto
- Enunciado: demuestre que r(t)=⟨arccos(2t²−1), arcsen t⟩, t∈[0,1], describe un segmento de recta (identidades de funciones inversas).
- Solución: con t=sen θ: arccos(2sen²θ−1)=π−2θ y arcsen(sen θ)=θ → x+2y=π → segmento.
- Figura: NO
- Estimación: S

### F9T.16 — [origen: T2.13] [destino: funvectoriales.tex, propuestos (o remitir a Álgebra Lineal)]
- Tipo: propuesto
- Enunciado: para la cónica x²+y²−2xy−2(x+y)+1=0: (i) discriminante B²−4AC=0 → parábola rotada; (ii) parametrización con el cambio u=x+y, v=x−y; (iii) puntos de tangente horizontal/vertical.
- Solución: discriminante → rotación 45° → canónica en (u,v) → parametrizar → derivar.
- Figura: SÍ → F9T.16f: parábola rotada con ejes u,v (TikZ 2D).
- Estimación: L

### F9T.17 — [origen: T3.05] [destino: funvectoriales.tex, §Funciones de varias variables (dominios), tras L807]
- Tipo: prob resuelto
- Enunciado: halle y grafique el dominio de f(x,y)=√(sen x · sen y): estructura de tablero por periodicidad.
- Solución: sen x·sen y≥0 → ambos ≥0 o ambos ≤0 → cuadrícula [kπ,(k+1)π]×[mπ,(m+1)π] con k+m par.
- Figura: SÍ → F9T.17f: tablero sombreado en [−2π,2π]² (TikZ 2D).
- Estimación: M

### F9T.18 — [origen: T3.06] [destino: funvectoriales.tex, §Funciones vectoriales (dominio/continuidad), junto a L1644]
- Tipo: ambos
- Enunciado: dominio de r(t)=⟨ln(t²−1), √(sen t), cos(1/t)⟩: intersección de los tres dominios componentes.
- Solución: |t|>1 ∩ sen t≥0 ∩ t≠0 → intersección de intervalos → respuesta en notación de intervalos.
- Figura: NO
- Estimación: S

### F9T.19 — [origen: T3.07] [destino: limvariasvariables.tex, §Límite (motivación) o §Continuidad, como prob con figura]
- Tipo: prob resuelto
- Enunciado: dada la gráfica de contorno de f (curvas de nivel con valores), estime el signo y comportamiento de lím_{h→0} [f(h,0)−f(0,0)]/h.
- Solución: leer valores de nivel sobre el eje x → cociente incremental por lados → conclusión (existe/no existe, signo).
- Figura: SÍ → F9T.19f: mapa de contorno sintético con niveles etiquetados (TikZ 2D).
- Estimación: M

### F9T.20 — [origen: T3.01] [destino: planostangentes.tex, §Derivadas parciales, tras el example L158] — DESBLOQUEADO (D3)
- Tipo: prob resuelto
- Enunciado: isomorfo de humidex — tabla de sensación térmica S(T,v) (temperatura del
  aire vs. velocidad del viento, valores nuevos, contexto genérico de estación
  meteorológica). Estimar ∂S/∂T y ∂S/∂v en un punto de la tabla mediante cocientes
  incrementales (promedio de diferencias adelante/atrás) e interpretar unidades y signo.
- Solución: leer valores vecinos de la tabla → cocientes [S(T+ΔT,v)−S(T,v)]/ΔT por
  ambos lados → promediar → interpretación física; conectar con la definición de
  parcial como límite del cociente incremental.
- Figura: NO (la tabla se compone con `tabular`, no requiere TikZ).
- Estimación: M

### F9T.21 — [origen: T4.01] [destino: funvectoriales.tex, junto a F9T.09 (cilindros)]
- Tipo: propuesto
- Enunciado: bosqueje la gráfica de f(x,y)=cos x en R³ e identifíquela como cilindro (generatrices paralelas al eje y).
- Solución: la ecuación no depende de y → trasladar la curva z=cos x.
- Figura: SÍ → F9T.21f: superficie z=cos x (pgfplots 3D, shader=flat, samples≤20).
- Estimación: S

### F9T.22 — [origen: T4.10] [destino: planostangentes.tex, §Derivadas parciales, propuestos]
- Tipo: propuesto
- Enunciado: para f(x,y)=∫_x^y √(1+t³) dt, calcule f_x y f_y usando el 1er Teorema Fundamental del Cálculo.
- Solución: f_y=√(1+y³); f_x=−√(1+x³) (límite inferior).
- Figura: NO
- Estimación: S

### F9T.23 — [origen: T4.27, T4.28] [destino: gradientes.tex, §Regla de la cadena, tras el Caso 2 (L230)]
- Tipo: ambos
- Enunciado: rem breve (la parcial de una parcial vuelve a usar la cadena) + prob resuelto: w_rr para w=f(x,y), x=r cosθ, y=r senθ (o análogo polinomial). Propuesto: d²P/dt² para P=kT/V con T(t), V(t) dadas (contexto químico, isomorfo T4.28).
- Solución: w_r por cadena → derivar w_r respecto a r reaplicando cadena a f_x y f_y → agrupar (f_xx, f_xy, f_yy).
- Figura: NO
- Estimación: L

### F9T.24 — [origen: T5.10] [destino: gradientes.tex, §Gradiente, propuestos]
- Tipo: propuesto
- Enunciado: calcule el ángulo entre ∇f y ∇g en el punto dado (funciones tipo taller).
- Solución: ambos gradientes → cosθ = (∇f·∇g)/(‖∇f‖‖∇g‖).
- Figura: NO
- Estimación: S

### F9T.25 — [origen: T5.23, T5.25] [destino: gradientes.tex, §Derivada direccional, tras el teorema del máximo (L752)]
- Tipo: ambos
- Enunciado: (i) sabiendo D_u f y D_v f en un punto para dos direcciones dadas, reconstruya ∇f (sistema lineal 2×2); (ii) decida si existe u con D_u f=c cuando c>‖∇f‖ (no existe: |D_u f|≤‖∇f‖).
- Solución: plantear ∇f·u=α, ∇f·v=β → resolver; para (ii) usar la cota |∇f·u|≤‖∇f‖.
- Figura: NO
- Estimación: M

### F9T.26 — [origen: T5.22] [destino: gradientes.tex, propuestos (desafiante)]
- Tipo: propuesto
- Enunciado: halle a,b tales que la derivada direccional máxima de f=e^{ax+by}cos(x+y) en el origen valga c√2 y ocurra en la dirección de la bisectriz (isomorfo).
- Solución: ∇f(0,0)=(a,b) → condiciones de dirección (a=b) y magnitud → resolver.
- Figura: NO
- Estimación: M

### F9T.27 — [origen: T5.31, T5.32] [destino: gradientes.tex, §Plano tangente y gradiente, tras L997]
- Tipo: ambos
- Enunciado: (i) demuestre que toda recta normal a la esfera x²+y²+z²=R² pasa por el origen; (ii) demuestre que la esfera x²+y²+z²=R² y el cono x²+y²−z²=0 son ortogonales en su intersección (∇F·∇G=0).
- Solución: (i) recta normal p+t∇F(p)=p(1+2t) → pasa por 0; (ii) producto punto de gradientes sobre la curva intersección usando x²+y²=z².
- Figura: NO
- Estimación: M

### F9T.28 — [origen: T6.12, T6.13, T6.14] [destino: multiplicadoresintdobles.tex, nueva subsec. "Lagrange con dos restricciones" tras L903]
- Tipo: ambos
- Enunciado: teorema ∇f=λ∇g+μ∇h (enunciado sin prueba) + example resuelto (punto de la curva intersección de dos superficies más cercano al origen, isomorfo T6.13) + propuestos: caja con área y suma de aristas dadas (T6.12) y punto más alto/bajo de la elipse plano∩cono (T6.14).
- Solución: sistema de 5 ecuaciones (3 de gradientes + 2 restricciones) → resolver por eliminación → comparar candidatos.
- Figura: NO
- Estimación: L

### F9T.29 — [origen: T6.09, T6.11, T5.27] [destino: multiplicadoresintdobles.tex, §Lagrange, tras el example L731]
- Tipo: ambos
- Enunciado: paralelepípedo de volumen máximo inscrito en el elipsoide x²/a²+y²/b²+z²/c²=1 (resuelto en simbólico); propuesto isomorfo con valores numéricos (tipo T6.11/T5.27).
- Solución: V=8xyz, Lagrange con g=x²/a²+y²/b²+z²/c²−1 → simetría → x=a/√3, etc.
- Figura: NO
- Estimación: M

### F9T.30 — [origen: T8.02] [destino: cap34.tex, §Teorema de Green, tras el example L168]
- Tipo: prob resuelto
- Enunciado: evalúe ∫_C F·dr donde C es el arco (t, sen t), t∈[0,π] (curva abierta): cierre C con el segmento de regreso sobre el eje x, aplique Green y despeje la integral pedida; cuidado con la orientación.
- Solución: C∪S cerrada → Green sobre la región → ∫_C = ∮ − ∫_S → calcular la doble y la del segmento.
- Figura: SÍ → F9T.30f: arco de seno + segmento de cierre con flechas de orientación (TikZ 2D).
- Estimación: M

### Prioridad 3 — PARCIAL

### F9T.31 — [origen: T1.02] [destino: funvectoriales.tex, §Cuádricas (trazas), junto a L1194]
- Tipo: propuesto
- Enunciado: para el hiperboloide ax²+by²−z²=1 y el plano z=c, muestre que la traza es una elipse y halle sus semiejes, vértices y focos.
- Solución: sustituir z=c → dividir → semiejes → elementos.
- Figura: NO
- Estimación: S

### F9T.32 — [origen: T1.04, T1.07, T1.08, T1.09, T1.10] [destino: funvectoriales.tex, §Cuádricas, tras los examples canónicos]
- Tipo: ambos
- Enunciado: prob resuelto: clasificar el elipsoide con términos lineales (completar cuadrados en las 3 variables, centro, semiejes, trazas por 3 planos — isomorfo T1.04). Propuestos: batería isomorfa de T1.07–T1.10 (paraboloide elíptico, hiperboloides de 1 y 2 hojas reorientados, paraboloide hiperbólico con términos lineales).
- Solución: agrupar por variable → completar cuadrados → canónica trasladada → clasificación y elementos.
- Figura: SÍ → F9T.32f: elipsoide trasladado con sus trazas (pgfplots 3D, shader=flat).
- Estimación: L

### F9T.33 — [origen: T2.02] [destino: funvectoriales.tex, §Límites de funciones vectoriales, tras L158]
- Tipo: propuesto
- Enunciado: lím_{t→0} ⟨cos t, t² sen(1/t), t²⟩ — la componente central por teorema de compresión.
- Solución: 0≤|t²sen(1/t)|≤t² → emparedado → límite ⟨1,0,0⟩.
- Figura: NO
- Estimación: S

### F9T.34 — [origen: T2.05] [destino: funvectoriales.tex, §Longitud de arco, junto a L608]
- Tipo: propuesto
- Enunciado: para el astroide r(t)=⟨cos³t, sen³t⟩: (i) muestre que r'(t)=0 en los múltiplos de π/2 (la curva no es suave allí); (ii) longitud en [0,π/2].
- Solución: r'(t) → factorizar → ceros; ‖r'‖=3|sen t cos t| → integrar.
- Figura: NO
- Estimación: S

### F9T.35 — [origen: T2.08] [destino: funvectoriales.tex, §Integrales de funciones vectoriales, tras L475]
- Tipo: prob resuelto
- Enunciado: PVI cinemático: dadas a(t) constante, v(0) y r(0), halle v(t) y r(t); identifique el tipo de curva y el instante de distancia mínima al origen.
- Solución: integrar a → v (constante de v(0)) → integrar v → r (constante de r(0)) → ‖r(t)‖² minimizar en 1 variable.
- Figura: NO
- Estimación: M

### F9T.36 — [origen: T3.02] [destino: funvectoriales.tex, §Curvas y superficies de nivel, tras L1696]
- Tipo: prob resuelto
- Enunciado: relacione cada función (ln(x²+y²−1), e^{−x²−y²}, cos(x²+y²), x²−y³ — o isomorfas) con su mapa de curvas de nivel, justificando por dominio, simetría radial y crecimiento.
- Solución: análisis de dominio/anillos/periodicidad radial → emparejamiento razonado.
- Figura: SÍ → F9T.36f: 4 minipaneles de curvas de nivel (TikZ 2D, contour manual con circunferencias/curvas).
- Estimación: L

### F9T.37 — [origen: T3.03, T3.04] [destino: funvectoriales.tex, §Funciones de varias variables (dominios), tras L807]
- Tipo: ambos
- Enunciado: prob resuelto: dominio de √((x+y)·ln(x−y)) por análisis de signos por casos (producto ≥0). Propuesto: dominio de ln(−x+2+y)/√((x−y+1)ln(x+y+1)) (isomorfo T3.04).
- Solución: casos (ambos factores ≥0) ∪ (ambos ≤0) → intersecar con x−y>0 → describir región.
- Figura: SÍ → F9T.37f: región del dominio sombreada con rectas frontera (TikZ 2D).
- Estimación: M

### F9T.38 — [origen: T4.11] [destino: planostangentes.tex, §Derivadas parciales, propuestos]
- Tipo: propuesto
- Enunciado: V=xyz (caja). Interprete ∂V/∂y como razón de cambio del volumen respecto al ancho con las demás dimensiones fijas; evalúe en un punto y explique unidades.
- Solución: ∂V/∂y=xz → evaluar → interpretación.
- Figura: NO
- Estimación: S

### F9T.39 — [origen: T4.12] [destino: planostangentes.tex, §Plano tangente, antes del protocolo L610]
- Tipo: propuesto
- Enunciado: muestre que T_x=⟨1,0,f_x⟩ y T_y=⟨0,1,f_y⟩ son tangentes a z=f(x,y) y que su producto cruz da el normal ⟨−f_x,−f_y,1⟩ del plano tangente.
- Solución: curvas coordenadas → derivar → producto cruz → comparar con la fórmula del plano.
- Figura: NO
- Estimación: S

### F9T.40 — [origen: T4.13] [destino: planostangentes.tex o gradientes.tex, propuestos]
- Tipo: propuesto
- Enunciado: deduzca que el plano tangente al elipsoide x²/a²+y²/b²+z²/c²=1 en (x₀,y₀,z₀) es xx₀/a²+yy₀/b²+zz₀/c²=1.
- Solución: ∇F=⟨2x₀/a²,…⟩ → plano → simplificar usando que el punto satisface la ecuación.
- Figura: NO
- Estimación: S

### F9T.41 — [origen: T4.19] [destino: planostangentes.tex, §Aproximación lineal, tras L835]
- Tipo: propuesto
- Enunciado: linealice f(x,y,z)=x³yz (isomorfo) en un punto dado y aproxime f en un punto cercano.
- Solución: L=f(p)+f_x·Δx+f_y·Δy+f_z·Δz → evaluar.
- Figura: NO
- Estimación: S

### F9T.42 — [origen: T4.22] [destino: planostangentes.tex, §Diferenciales, reemplazar el esbozo de prueba L907]
- Tipo: prob resuelto (o elevar la prueba del teorema)
- Enunciado: demuestre con detalle que si f es diferenciable en (x₀,y₀) entonces es continua allí.
- Solución: Δz=f_xΔx+f_yΔy+ε₁Δx+ε₂Δy con ε→0 → Δz→0 → continuidad.
- Figura: NO
- Estimación: M

### F9T.43 — [origen: T4.26] [destino: gradientes.tex, §Derivación implícita, tras el teorema L238]
- Tipo: ambos
- Enunciado: rem: caso F(x,y)=0 → dy/dx=−F_x/F_y + prob: dy/dx para cos(x+y)=y·sen x (isomorfo).
- Solución: definir F → F_x, F_y → cociente; comparar con derivación implícita clásica.
- Figura: NO
- Estimación: S

### F9T.44 — [origen: T5.06] [destino: gradientes.tex, §Derivada direccional, ampliar prob L691 o propuesto]
- Tipo: propuesto
- Enunciado: D_u f para f(x,y,z)=xy²z³ en un punto, con v=⟨2,1,−2⟩ (isomorfo, 3 variables).
- Solución: ∇f → evaluar → normalizar v → producto punto.
- Figura: NO
- Estimación: S

### F9T.45 — [origen: T5.26] [destino: multiplicadoresintdobles.tex, tras el example L224]
- Tipo: prob resuelto
- Enunciado: críticos de f=(x²+y²)e^{−(x²+y²)}: mínimo absoluto en el origen y una circunferencia completa de máximos (r²=1); el criterio D falla sobre la circunferencia → análisis radial g(r)=re^{−r}.
- Solución: sustitución radial u=x²+y² → g(u)=ue^{−u} → g'=0 → u=1 → interpretar como conjunto de máximos.
- Figura: NO
- Estimación: M

### F9T.46 — [origen: T6.08] [destino: multiplicadoresintdobles.tex, propuestos]
- Tipo: propuesto
- Enunciado: halle el punto que minimiza la suma de los cuadrados de las distancias a tres puntos dados (isomorfo Acme; respuesta: el centroide).
- Solución: f=Σ‖p−p_i‖² → ∇f=0 → p=(p₁+p₂+p₃)/3 → D>0 confirma mínimo.
- Figura: NO
- Estimación: S

### F9T.47 — [origen: T6.21] [destino: apintdobles.tex, propuestos (polares)]
- Tipo: propuesto
- Enunciado: volumen del sólido entre z=c y el paraboloide z=a−b(x²+y²), con a>c (isomorfo T6.21): hallar la proyección igualando superficies.
- Solución: a−br²=c → r₀=√((a−c)/b) → V=∫∫(a−br²−c) r dr dθ.
- Figura: NO
- Estimación: S

### F9T.48 — [origen: T8.01] [destino: cap34.tex, §Green, tras el example L168]
- Tipo: prob resuelto
- Enunciado: verifique el teorema de Green para F=(2x³−y³, x³+y³) (isomorfo) en el anillo 1≤x²+y²≤4: dos fronteras con orientaciones opuestas.
- Solución: ∮ exterior − ∮ interior (parametrizar ambas) vs. ∬(N_x−M_y) dA en polares sobre el anillo.
- Figura: SÍ → F9T.48f: anillo con orientaciones de las dos fronteras (TikZ 2D).
- Estimación: M

### F9T.49 — [origen: T8.03] [destino: cap34.tex, §Divergencia y rotacional, propuestos]
- Tipo: propuesto
- Enunciado: demuestre la identidad div(F×G)=G·(∇×F)−F·(∇×G). **Nota: el taller original tiene los términos con signo intercambiado; se inserta con el signo correcto.**
- Solución: expandir F×G por componentes → derivar → reagrupar en los dos productos punto.
- Figura: NO
- Estimación: S

### F9T.50 — [origen: T8.04] [destino: cap33.tex, §Independencia de la trayectoria, tras el example L728]
- Tipo: prob resuelto
- Enunciado: para F conservativo dado, defina f(x,y,z)=∫_C F·dr con C el segmento de (0,0,0) a (x,y,z); calcule f explícitamente y verifique ∇f=F.
- Solución: r(t)=t⟨x,y,z⟩, t∈[0,1] → integrar en t → f cerrada → gradiente y comparación.
- Figura: NO
- Estimación: M

### F9T.51 — [origen: T8.09] [destino: inttriples.tex, propuestos (o apintdobles)]
- Tipo: propuesto
- Enunciado: volumen del sólido entre los paraboloides z=x²+3y² y z=c−x²−3y² (isomorfo): proyección por igualación (elipse).
- Solución: igualar → región elíptica → V=∬(techo−piso) dA, con cambio x=ar cosθ, y=br senθ (jacobiano abr).
- Figura: NO
- Estimación: S

### F9T.52 — [origen: T8.10] [destino: inttriples.tex, tras el prob L321]
- Tipo: prob resuelto
- Enunciado: volumen del sólido acotado por z=√x, z=0, los planos y=0, y=b y x+z=2 (isomorfo T8.10): el techo cambia de superficie → partir la región en x.
- Solución: intersección √x=2−x → x=1 → V=b[∫₀¹√x dx+∫₁²(2−x)dx].
- Figura: SÍ → F9T.52f: corte en el plano xz mostrando √x y 2−x (TikZ 2D).
- Estimación: M

### F9T.53 — [origen: T8.13] [destino: inttriples.tex, §Masa y centro de masa, tras el example L254]
- Tipo: prob resuelto
- Enunciado: centro de masa de un sólido con ρ variable resuelto a mano (isomorfo T8.12/T8.13: cubo o caja con ρ=x²+y²+z² o ρ=x).
- Solución: M, M_yz, M_xz, M_xy como triples iteradas → cocientes.
- Figura: NO
- Estimación: M

---

## 8. Hallazgos

- **H1 (T6, 2026-07-18):** el mapeo de la sección 2 asigna las integrales dobles de T6
  a `multiplicadoresintdobles.tex`, pero ese archivo contiene SOLO optimización
  (críticos, Lagrange, hessiano limitado). Las integrales dobles (Fubini, regiones,
  polares, masa/centro de masa, jacobiano) viven en `apintdobles.tex` (1700 líneas).
  Gana el `.tex`: T6.15–T6.21 se auditaron contra `apintdobles.tex` (abreviado `ai`).
  Lo mismo aplicará a EX.04 y EX.10 (área de superficie está en `apintdobles.tex` §Área
  de una superficie, L933).

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
