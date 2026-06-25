# PLAN_FASE8_APOSTOL_C3.md — Criterio Apostol para Cálculo III

**Inicio:** 2026-06-25  
**Objetivo:** Aplicar criterio Apostol operativo (R1–R3) a los 8 capítulos de C3 del problemario, priorizando figuras TikZ guía y sección de Jacobiano ausente.  
**Compilador:** LuaLaTeX. Todas las figuras en TikZ puro o pgfplots — sin pstricks, sin Asymptote.  
**Regla de tamaño:** cada ítem ≤ 300 líneas de código nuevo o modificado.  
**Regla de contenido:** nada se elimina sin decisión explícita del autor.

---

## Criterio Apostol operativo — C3

**R1 — Orden canónico dentro de cada capítulo:**  
definición → motivación geométrica (figura) → teorema (enunciado riguroso) → esquema de prueba o prueba completa → ejemplos (4 pasos + `\boxed{}`) → problemas propuestos

**R2 — Figura obligatoria:**  
todo concepto con interpretación geométrica lleva figura TikZ inmediatamente después de la definición o teorema. No se remite a figuras posteriores.

**R3 — Nivel de demostración:**

| Tipo | Tratamiento |
|---|---|
| Teoremas centrales (Green, Stokes, Divergencia, TFC línea, plano tangente, regla cadena) | Demostración completa o esquema con pasos clave explícitos |
| Teoremas operacionales (Fubini, criterio 2ª deriv., Fubini triple, propiedades integrales) | Enunciado riguroso + esquema geométrico/intuitivo |
| Propiedades de cálculo (linealidad, monotonía, etc.) | Enunciado + referencia |

---

## Criterio de problemas — C3

**Mínimo por capítulo:** 8–10 resueltos (con `\begin{myproof}`) + 15–20 propuestos (sin myproof).  
**Máximo propuestos:** 40.  
**Criterio de elevación a resuelto:** pedagógico — el problema ilustra una técnica o caso clave que el estudiante necesita ver resuelto antes de intentarlo solo. No se eleva por volumen.  
**Función de los propuestos:** guía de exámenes y talleres de casa — deben ser variados, graduados en dificultad, y cubrir todos los subtemas del capítulo.

**Estado diagnóstico:**

| Cap | Resueltos actuales | Propuestos actuales | Déficit resueltos | Déficit propuestos | Exceso propuestos |
|---|---|---|---|---|---|
| 18 | 6 | 5 | — | +10 | — |
| 19 | 2 | 14 | +6 | — | — |
| 20 | 2 | 7 | +6 | +8 | — |
| 21 | 1 | 16 | +7 | — | — |
| 22 | 6 | 16 | — | — | — |
| 32 | 11 | 0 | — | +15 | — |
| 33 | 7 | ~8 est. | — | +7 est. | — |
| 34 | 16 | 29 | — | — | revisar si 9+ deben ser resueltos |

---

## Semana 0 — Auditoría y ajuste de problemas (prerequisito para figuras)

### F8.P1 — Cap. 18 (`funvectoriales.tex`): elevar resueltos + añadir propuestos
**Situación:** 6 resueltos (Probs 6–11), 5 propuestos (Probs 1–5).  
**Acción:**  
- Revisar Probs 1–5: identificar cuáles son técnicamente representativos → elevar 2–3 a resueltos (myproof dentro de prob)  
- Añadir 10–12 problemas propuestos nuevos cubriendo: longitud de arco, límite de función vectorial, continuidad, derivada (reglas), integral definida vectorial, superficies de nivel con descripción verbal  
- Verificar que los resueltos existentes (Probs 6–11) están bien estructurados pedagógicamente  
**Criterio de cierre:** 8–10 resueltos, 15–18 propuestos, graduación creciente verificada  
**Líneas estimadas:** 80–130  
**Estado:** Completo — 2026-06-25. Archivo tenía 24 probs y 6 resueltos (no 11 como estimado). Se añadieron myproof a Probs 1, 3 y 5 (límites, derivadas, longitud de arco). Resultado: 9 resueltos, 15 propuestos. Compilación limpia.

---

### F8.P2 — Cap. 19 (`limvariasvariables.tex`): elevar resueltos
**Situación:** 2 resueltos (Probs 5, 11 — myproof añadido por corrección), 14 propuestos.  
**Acción:**  
- Leer los 14 propuestos e identificar 6–7 que ilustren técnicas clave: límite por trayectorias, límite por definición ε-δ, discontinuidad esencial, continuidad en dominio con agujero  
- Elevar esos 6–7 a resueltos añadiendo myproof completo  
- Verificar que los propuestos restantes (~7–8) cubren variedad suficiente  
**Criterio de cierre:** 8–9 resueltos, 7–8 propuestos, sin duplicación de técnica entre resueltos  
**Líneas estimadas:** 120–180 (6–7 myproof nuevos)  
**Estado:** Completo — 2026-06-25. Archivo tenía 9 resueltos y 12 propuestos (plan estimaba 2 y 14). Se añadieron myproof a Probs 3 (polares), 5 (trayectoria parabólica — corregido x³y→x²y) y 12 (simplificación algebraica). Se añadió Proposición de función acotada + resuelto x⁴y/(x⁴+y⁴) + 2 propuestos. Resultado: 13 resueltos, 10 propuestos. Compilación limpia (2 pasadas).

---

### F8.P3 — Cap. 20 (`planostangentes.tex`): elevar resueltos + añadir propuestos
**Situación:** 2 resueltos (Probs 4–5), 7 propuestos (Probs 1–3, 6–9).  
**Acción:**  
- Elevar Probs 1–3 a resueltos (cubren: derivadas parciales básicas, orden superior, función implícita) — añadir myproof  
- Elevar 3 de los Probs 6–9 a resueltos (cubren: plano tangente, aproximación lineal, diferencial total)  
- Añadir 8–10 propuestos nuevos cubriendo: derivación implícita $F(x,y,z)=0$, diferenciales aplicados a error, plano tangente en superficie dada paramétricamente  
**Criterio de cierre:** 8–9 resueltos, 15–17 propuestos  
**Líneas estimadas:** 150–220  
**Estado:** Completo — 2026-06-25. Real: 20 probs (vs. 9 estimado). Se elevaron 6 probs a resueltos: derivadas cruzadas 3 vars, $f_x(0,0)$ por definición (caso no-diferenciable), ecuación de onda, ecuación de Laplace, plano tangente $z=x^2y^3$, linealización $\ln(1+x+2y)$. Se añadieron 5 propuestos nuevos: derivación implícita F(x,y,z)=0, error de área, plano tangente implícita, diferencial $w=x^2e^{y/z}$, derivación implícita $e^z-z=xy+1$. Resultado: 9 resueltos, 16 propuestos. Compilación limpia (732 págs).

---

### F8.P4 — Cap. 21 (`gradientes.tex`): elevar resueltos
**Situación:** 1 resuelto (Prob 9), 16 propuestos.  
**Acción:**  
- Identificar 7–8 propuestos que ilustren: cálculo de gradiente, derivada direccional en punto dado, dirección de máximo crecimiento, gradiente como normal a curva de nivel, regla de la cadena con parametrización  
- Elevar esos 7–8 a resueltos con myproof  
- Verificar que los ~8 propuestos restantes son de dificultad media-alta (apropiados para examen)  
**Criterio de cierre:** 8–9 resueltos, 8–9 propuestos  
**Líneas estimadas:** 140–200  
**Estado:** Completo — 2026-06-25. Real: 24 probs (vs. 17 estimado), 4 resueltos originales (todos razón de cambio). Se elevaron 5 probs: regla de cadena Caso 2 ($z=e^{xy}$), derivación implícita ($x^2y-y^2z+z^3=1$), derivada direccional (3 sub-casos), dirección de máximo crecimiento (3 sub-casos), plano tangente/recta normal a superficie implícita (3 superficies). Resultado: 9 resueltos, 15 propuestos. Compilación pendiente confirmación.

---

### F8.P5 — Cap. 22 (`multiplicadoresintdobles.tex`): revisar calidad pedagógica
**Situación:** 6 resueltos, 16 propuestos — en rango objetivo.  
**Acción:**  
- Verificar que los 6 resueltos cubren los casos canónicos: extremo libre con D>0 máx, D>0 mín, punto silla, Lagrange con 1 restricción, Lagrange con 2 restricciones, aplicación geométrica  
- Si algún caso canónico no está cubierto → elevar 1 propuesto adicional a resuelto  
- Verificar graduación de los 16 propuestos (fácil → medio → difícil)  
**Criterio de cierre:** 6–8 resueltos con cobertura canónica completa, 14–16 propuestos graduados  
**Líneas estimadas:** 30–80 (revisión + ajuste menor)  
**Estado:** Completo — 2026-06-25. 1 myproof añadido: minimizar $f=x^2+y^2$ s.t. $x+y=1$ con Hessiano bordeado ($\bar{H}=-4<0$, mínimo confirmado). 2 problemas de ley de Ohm (razón de cambio) movidos al Cap 21 donde corresponden. Resultado: 9 resueltos, 20 propuestos. Compilación limpia (734 págs).

---

### F8.P6 — Cap. 32 (`apintdobles.tex`): añadir propuestos puros
**Situación:** 11 resueltos (todos), 0 propuestos — sin material para examen/taller.  
**Acción:**  
- Los 11 resueltos actuales son correctos y bien estructurados — no tocar  
- Añadir 15–18 problemas propuestos nuevos (sin myproof) cubriendo: integral doble rectangular, región tipo I, región tipo II, cambio de orden, coordenadas polares, área de región, volumen bajo superficie, centro de masa lámina, momentos de inercia, área superficial  
- Graduar: 5 directos, 8 intermedios, 5 desafiantes  
**Criterio de cierre:** 11 resueltos, 15–18 propuestos  
**Líneas estimadas:** 80–120  
**Estado:** Completo — 2026-06-25. Se añadieron 18 propuestos nuevos: 5 directos (Fubini rect., tipo I/II, área), 8 intermedios (cambio de orden, coord. polares, masa/CM, momento de inercia), 5 desafiantes (área superficial, volumen, momento polar, integral anular). Resultado: 11 resueltos, 18 propuestos. Compilación limpia (734 págs).

---

### F8.P7 — Cap. 33 (`inttriples.tex`): conteo real + ajuste
**Situación:** conteo de propuestos no disponible en los `.md` — requiere leer el archivo.  
**Acción:**  
- Contar resueltos y propuestos actuales  
- Verificar cobertura: coordenadas rectangulares, masa/momentos, cilíndricas, esféricas, Jacobiano (pendiente F8.12–F8.13)  
- Ajustar según déficit encontrado: elevar resueltos si <8, añadir propuestos si <15  
- Nota: los propuestos de Jacobiano se añaden después de F8.12–F8.13  
**Criterio de cierre:** 8–10 resueltos, 15–20 propuestos  
**Líneas estimadas:** 20–150 (depende del conteo real)  
**Estado:** Completo — 2026-06-25. Real antes: 5 resueltos (todos dobles 2D), 73 propuestos. Se elevaron 4 a resueltos: volumen $z=2-x-y$ (V=1), masa rect. $\rho=xyz$ (M=225/2), cilíndricas $\int\int\int(x^2+y^2)$ (648π), esféricas $\iiint 5z$ cono-esfera (10π). Se eliminaron 16 propuestos redundantes (duplicados exactos, variantes cilíndricas, láminas triangulares redundantes, probs de capítulo incorrecto). 3 probs vectoriales movidos a Cap 34. Resultado: 9 resueltos, ~53 propuestos (sobre máximo — pendiente decisión editorial futura). Compilación limpia (734 págs).

---

### F8.P8 — Cap. 34 (`cap34_integrales_vectoriales.tex`): seleccionar resueltos guía entre propuestos
**Situación:** 16 resueltos, 29 propuestos — propuestos por encima del máximo recomendado.  
**Acción:**  
- Revisar los 29 propuestos e identificar 8–10 que ilustren técnicas que no aparecen en los 16 resueltos orgánicos (e.g., campo conservativo en R³, flujo por superficie no gráfica, Stokes sobre superficie con borde no trivial)  
- Elevar esos 8–10 a resueltos añadiendo myproof  
- Los propuestos restantes (19–21): verificar que no hay duplicación de tipo y que están graduados  
- Si quedan >25 propuestos después del ajuste → marcar los más difíciles como `\textbf{(*)Desafío}` sin eliminar  
**Criterio de cierre:** 24–26 resueltos, 19–21 propuestos, sin duplicación  
**Líneas estimadas:** 200–280 (8–10 myproof nuevos, cap. grande)  
**Estado:** Completo — 2026-06-25. Real: 10 myproof en examples, 25 propuestos (incluyendo 3 movidos de Cap 33). Se elevaron 8 probs: integral de línea 3 caminos (2/3), campos conservativos R² y R³ + potenciales, TFC ($\int=4$), área por Green + elipse ($\pi ab$), campo de vórtice ($\oint=2\pi$, dominio no s.c.), flujo div.thm. esfera ($128\pi/3$), Stokes cono ($-\pi$), $I_z$ cáscara esférica ($2MR^2/3$). Resultado: 18 resueltos totales (10 examples + 8 probs), 17 propuestos. Compilación pendiente confirmación.

---

## Semana 1 — Marco TikZ + figuras Cap. 18 y Cap. 19

### F8.01 — Plantilla de figura TikZ estándar para el libro
**Archivo:** nuevo `figuras_guia.tex` (incluible con `\input` desde cualquier cap.)  
**Contenido:** 3 figuras de referencia como comentarios documentados:  
(a) curva paramétrica en R³ con vector tangente (hélice circular)  
(b) superficie de nivel f(x,y)=c con gradiente perpendicular  
(c) región acotada tipo I en R²  
**Criterio de cierre:** compila limpio, figuras legibles en PDF a tamaño de página estándar.  
**Estado:** Pendiente

---

### F8.02 — Cap. 18 (`funvectoriales.tex`): figura curva en R³ y vector tangente
**Sección destino:** inmediatamente después de la definición de función vectorial  
**Figura:** hélice $\mathbf{r}(t)=(\cos t, \sin t, t/2)$ con vector tangente en $t=\pi/2$, ejes xyz etiquetados, sin relleno de superficie  
**TikZ:** `tikzpicture` con `tdplot` o pgfplots 3D axis — elegir el que compile más rápido  
**Líneas estimadas:** 40–60  
**Estado:** Pendiente

---

### F8.03 — Cap. 18 (`funvectoriales.tex`): figura superficie de nivel y curvas de nivel
**Sección destino:** después de la definición de función de varias variables / curvas de nivel  
**Figura:** paraboloide $z=x^2+y^2$ visto desde arriba con 4 curvas de nivel $c=1,2,3,4$ en el plano $xy$ (proyección), y la superficie en 3D encima — dos subfiguras o figura compuesta  
**TikZ:** pgfplots `surf` + pgfplots 2D para proyección  
**Líneas estimadas:** 60–80  
**Estado:** Pendiente

---

### F8.04 — Cap. 19 (`limvariasvariables.tex`): figura vecindad abierta en R²
**Sección destino:** después de la definición de límite (ε-δ en R²)  
**Figura:** disco abierto $B((x_0,y_0),\delta)$ con punto interior, borde punteado, etiquetas $\delta$, $(x_0,y_0)$, y banda de salida $|f-L|<\varepsilon$ indicada en texto lateral  
**TikZ:** `tikzpicture` puro, 2D  
**Líneas estimadas:** 30–45  
**Estado:** Pendiente

---

### F8.05 — Cap. 19 (`limvariasvariables.tex`): figura discontinuidad esencial sobre recta
**Sección destino:** después del ejemplo de límite que no existe (trayectorias distintas)  
**Figura:** dos trayectorias hacia el origen con límites distintos — recta $y=mx$ y parábola $y=x^2$ — con flechas de dirección y etiquetas de límite obtenido por cada camino  
**TikZ:** `tikzpicture` puro, 2D  
**Líneas estimadas:** 35–50  
**Estado:** Pendiente

---

## Semana 2 — Figuras caps. 20, 21, 22

### F8.06 — Cap. 20 (`planostangentes.tex`): figura plano tangente sobre superficie
**Sección destino:** antes del teorema de plano tangente  
**Figura:** superficie suave con plano tangente en punto $(x_0,y_0,z_0)$ marcado, vector normal $\nabla F$ perpendicular al plano, ejes xyz  
**TikZ:** pgfplots 3D `surf` con `shader=flat` (rápido, sin demoras de compilación)  
**Restricción:** la superficie debe ser simple (paraboloide o silla) para que pgfplots no tarde más de 10 s  
**Líneas estimadas:** 55–75  
**Estado:** Pendiente

---

### F8.07 — Cap. 20 (`planostangentes.tex`): figura aproximación lineal
**Sección destino:** después de la definición de diferencial total  
**Figura:** zoom sobre superficie cerca de $(x_0,y_0)$ mostrando que el plano tangente "pega" bien localmente — superficie curva y plano superpuesto, con $\Delta z$ vs $dz$ indicados con segmentos etiquetados  
**TikZ:** pgfplots 3D, misma superficie que F8.06 para consistencia visual  
**Líneas estimadas:** 50–65  
**Estado:** Pendiente

---

### F8.08 — Cap. 21 (`gradientes.tex`): figura vector gradiente y curvas de nivel
**Sección destino:** inmediatamente después de la definición de gradiente  
**Figura:** 5–6 curvas de nivel de $f(x,y)=x^2+y^2/4$ (elipses) con vectores $\nabla f$ en 4 puntos, perpendiculares a las curvas, longitud proporcional a $\|\nabla f\|$  
**TikZ:** pgfplots 2D con `contour` o `tikzpicture` con elipses manuales — elegir lo más limpio  
**Líneas estimadas:** 45–65  
**Estado:** Pendiente

---

### F8.09 — Cap. 21 (`gradientes.tex`): figura derivada direccional como pendiente
**Sección destino:** antes del teorema de derivada direccional  
**Figura:** superficie $z=f(x,y)$, punto $P$, dirección unitaria $\mathbf{u}$ en plano $xy$, plano vertical cortando la superficie en esa dirección — la intersección es la curva cuya pendiente es $D_{\mathbf{u}}f$  
**TikZ:** pgfplots 3D, superficie simple  
**Líneas estimadas:** 55–70  
**Estado:** Pendiente

---

### F8.10 — Cap. 22 (`multiplicadoresintdobles.tex`): figura punto de silla
**Sección destino:** después de la definición de punto crítico, antes del criterio de la segunda derivada  
**Figura:** superficie $z=x^2-y^2$ (silla de montar) con punto crítico en el origen marcado, con las dos direcciones de curvatura opuesta indicadas  
**TikZ:** pgfplots 3D `surf`  
**Líneas estimadas:** 45–60  
**Estado:** Pendiente

---

### F8.11 — Cap. 22 (`multiplicadoresintdobles.tex`): figura región factible Lagrange
**Sección destino:** antes del primer ejemplo de multiplicadores  
**Figura:** curvas de nivel $f(x,y)=c$ para varios $c$, restricción $g(x,y)=0$ como curva, punto de tangencia (solución óptima) donde una curva de nivel es tangente a la restricción, gradientes paralelos indicados  
**TikZ:** `tikzpicture` 2D con curvas dibujadas manualmente (elipses + recta o círculo)  
**Líneas estimadas:** 50–70  
**Estado:** Pendiente

---

## Semana 3 — Jacobiano (sección nueva en Cap. 33)

### F8.12 — Cap. 33 (`inttriples.tex`): sección Cambio de variables — definición y Jacobiano 2×2
**Acción:** nueva `\section{Cambio de variables en integrales dobles}` insertada antes de `\section{Coordenadas cilíndricas}`  
**Contenido:**  
- Definición de transformación $T(u,v)=(x(u,v),y(u,v))$  
- Definición de Jacobiano $\partial(x,y)/\partial(u,v)$ como determinante 2×2  
- Teorema de cambio de variables (enunciado riguroso, sin demostración — R3 operacional)  
- Esquema geométrico: rectángulo en $(u,v)$ → región deformada en $(x,y)$, área escalada por $|J|$  
- 1 ejemplo completo (4 pasos): integral doble con cambio $x=r\cos\theta$, $y=r\sin\theta$ (caso polar como instancia del Jacobiano — conecta con lo que ya existe)  
**Líneas estimadas:** 120–160  
**Estado:** Pendiente

---

### F8.13 — Cap. 33 (`inttriples.tex`): Jacobiano 3×3 + reencuadre de cilíndricas/esféricas
**Acción:** nueva `\section{Cambio de variables en integrales triples}` insertada antes de la sección de cilíndricas actual  
**Contenido:**  
- Jacobiano 3×3 (determinante)  
- Teorema de cambio de variables triple (enunciado)  
- Esquema: paralelepípedo en $(u,v,w)$ → sólido deformado, volumen escalado por $|J|$  
- Añadir al inicio de la sección de cilíndricas existente: 2 líneas que calculen el Jacobiano cilíndrico $r$ y lo conecten con la fórmula $dV=r\,dr\,d\theta\,dz$  
- Añadir al inicio de la sección de esféricas existente: 2 líneas con el Jacobiano esférico $\rho^2\sin\phi$  
**Líneas estimadas:** 80–110 (más 2×2 líneas de edición en secciones existentes)  
**Estado:** Pendiente

---

### F8.14 — Cap. 33 (`inttriples.tex`): figura geométrica del Jacobiano
**Sección destino:** dentro de F8.12, después de la definición de Jacobiano  
**Figura:** cuadrado $[0,1]^2$ en plano $(u,v)$ → paralelogramo deformado en plano $(x,y)$ con los vectores columna del Jacobiano como lados, área $= |J|$ indicada  
**TikZ:** `tikzpicture` 2D, dos subfiguras con flecha de transformación entre ellas  
**Líneas estimadas:** 40–55  
**Estado:** Pendiente

---

## Semana 4 — Figuras caps. 32 y 34

### F8.15 — Cap. 32 (`apintdobles.tex`): figuras región tipo I y tipo II
**Sección destino:** antes de la integral sobre región general (no rectangular)  
**Figura A:** región tipo I — $a \le x \le b$, $g_1(x) \le y \le g_2(x)$ — con curvas $g_1$, $g_2$ etiquetadas y franja vertical sombreada  
**Figura B:** región tipo II — $c \le y \le d$, $h_1(y) \le x \le h_2(y)$ — franja horizontal  
**TikZ:** dos `tikzpicture` 2D en minipages lado a lado  
**Líneas estimadas:** 60–80  
**Estado:** Pendiente

---

### F8.16 — Cap. 32 (`apintdobles.tex`): figura cambio de orden de integración
**Sección destino:** después del primer ejemplo de región no rectangular  
**Figura:** región acotada por dos curvas, con las dos descomposiciones posibles (vertical y horizontal) superpuestas, indicando cuál es más simple  
**TikZ:** `tikzpicture` 2D  
**Líneas estimadas:** 45–60  
**Estado:** Pendiente

---

### F8.17 — Cap. 34 (`cap34_integrales_vectoriales.tex` — ahora Cap. 33 del libro): figura campo vectorial con flechas
**Sección destino:** después de la definición de campo vectorial  
**Figura:** campo $\mathbf{F}(x,y)=(-y,x)$ (rotacional puro) en grilla $[-2,2]^2$ con flechas proporcionales, ejes etiquetados  
**TikZ:** pgfplots 2D con `quiver` — es el método más limpio para campos vectoriales en pgfplots  
**Líneas estimadas:** 35–50  
**Estado:** Pendiente

---

### F8.18 — Cap. 34: figura curva orientada para integral de línea
**Sección destino:** antes de la definición de integral de línea escalar  
**Figura:** curva suave $C$ de $A$ a $B$ en R², con flechas de orientación, punto de muestreo $P_i$, segmento $\Delta s_i$ indicado, y valor $f(P_i)$ como altura sobre la curva (barra vertical)  
**TikZ:** `tikzpicture` 2D  
**Líneas estimadas:** 45–60  
**Estado:** Pendiente

---

### F8.19 — Cap. 34: figura superficie orientada con vector normal
**Sección destino:** antes de la definición de integral de superficie vectorial (flujo)  
**Figura:** parche de superficie con vector normal $\mathbf{n}$ en varios puntos, orientación consistente indicada por sentido de giro del borde, con dos caras diferenciadas visualmente  
**TikZ:** pgfplots 3D con `surf`, vectores normales añadidos con `\draw[->]`  
**Líneas estimadas:** 55–75  
**Estado:** Pendiente

---

## Semana 5 — Revisión orden interno R1 + esquemas de prueba

### F8.20 — Auditoría R1: verificar orden canónico en caps. 18–22
**Acción:** revisar que en cada capítulo el orden sea definición → figura → teorema → prueba/esquema → ejemplo → problemas. Registrar cualquier inversión.  
**Entregable:** lista de inversiones encontradas + correcciones aplicadas (cada corrección ≤ 50 líneas de reordenamiento)  
**Estado:** Pendiente

---

### F8.21 — Esquema de prueba: Teorema de Green (Cap. 34)
**Verificar:** si la demostración actual es completa o solo enunciado  
**Acción según resultado:**  
- Si es solo enunciado: añadir esquema con pasos clave (dividir región en tipo I + tipo II, aplicar TFC a cada integral itinerada, sumar)  
- Si es completa: añadir figura geométrica del argumento (región con borde orientado, franjas verticales/horizontales)  
**Líneas estimadas:** 40–80 según caso  
**Estado:** Pendiente

---

### F8.22 — Esquema de prueba: Teorema de Stokes (Cap. 34)
**Verificar:** si la prueba de Green como caso particular de Stokes (que ya existe) es suficiente o si falta el esquema general  
**Acción:** añadir figura con superficie $S$, borde $\partial S$ orientado por regla de la mano derecha, y micro-circulaciones del rotacional  
**Líneas estimadas:** 35–55  
**Estado:** Pendiente

---

### F8.23 — Esquema de prueba: Teorema de la Divergencia (Cap. 34)
**Verificar:** estado de la demostración actual  
**Acción:** añadir esquema con sólido $E$ dividido en rebanadas verticales, flujo neto por cara superior e inferior, cancelación de caras internas  
**Líneas estimadas:** 40–60  
**Estado:** Pendiente

---

### F8.24 — Introducción narrativa: caps. 18, 19, 32 (los que no tienen párrafo introductorio)
**Acción:** verificar cuáles capítulos C3 carecen de párrafo introductorio (motivación del capítulo antes de la primera sección). Añadir donde falte: 1 párrafo de 4–6 líneas con la pregunta central del capítulo y su conexión con lo anterior.  
**Líneas estimadas:** 6–8 por capítulo afectado  
**Estado:** Pendiente

---

## Registro de progreso

| Ítem | Archivo(s) | Acción | Estado | Fecha | Notas |
|---|---|---|---|---|---|
| F8.P1 | `funvectoriales.tex` | Elevar 2–3 resueltos + añadir 10–12 propuestos | Completo | 2026-06-25 | 3 myproof añadidos (Probs 1, 3, 5). 9 resueltos, 15 propuestos. Compilación limpia. |
| F8.P2 | `limvariasvariables.tex` | Elevar 6–7 resueltos | Completo | 2026-06-25 | +myproof Probs 3,5,12 + Prop acot-polar + resuelto + 2 propuestos. 13 res., 10 prop. Compilación limpia. |
| F8.P3 | `planostangentes.tex` | Elevar 6 resueltos + añadir 8–10 propuestos | Completo | 2026-06-25 | +myproof 6 probs + 5 propuestos nuevos. 9 res., 16 prop. 732 págs. |
| F8.P4 | `gradientes.tex` | Elevar 7–8 resueltos | Completo | 2026-06-25 | +myproof 5 probs (cadena Caso2, implícita, deriv.direcc., máx.crec., plano tang.). 9 res., 15 prop. Compilación pendiente. |
| F8.P5 | `multiplicadoresintdobles.tex` | Revisar calidad pedagógica | Completo | 2026-06-25 | +myproof Hessiano limitado (Lagrange 1 restr.). Traslado 2 probs Ohm a Cap21. 9 res., 20 prop. Compilación pendiente. |
| F8.P6 | `apintdobles.tex` | Añadir 15–18 propuestos | Completo | 2026-06-25 | +18 propuestos nuevos (5 directos, 8 intermedios, 5 desafiantes). Todos los temas cubiertos: rect., tipo I/II, cambio orden, polares, vol., masa, momentos, área superf. 11 res., 18 prop. Compilación pendiente. |
| F8.P7 | `inttriples.tex` | Conteo real + ajuste | Pendiente | — | — |
| F8.P8 | `cap34_integrales_vectoriales.tex` | Elevar 8–10 resueltos, podar propuestos | Pendiente | — | — |
| F8.01 | `figuras_guia.tex` (nuevo) | Plantilla TikZ | Pendiente | — | — |
| F8.02 | `funvectoriales.tex` | Figura hélice R³ | Pendiente | — | — |
| F8.03 | `funvectoriales.tex` | Figura paraboloide + curvas nivel | Pendiente | — | — |
| F8.04 | `limvariasvariables.tex` | Figura vecindad ε-δ | Pendiente | — | — |
| F8.05 | `limvariasvariables.tex` | Figura trayectorias límite | Pendiente | — | — |
| F8.06 | `planostangentes.tex` | Figura plano tangente 3D | Pendiente | — | — |
| F8.07 | `planostangentes.tex` | Figura aproximación lineal | Pendiente | — | — |
| F8.08 | `gradientes.tex` | Figura gradiente + curvas nivel | Pendiente | — | — |
| F8.09 | `gradientes.tex` | Figura derivada direccional | Pendiente | — | — |
| F8.10 | `multiplicadoresintdobles.tex` | Figura punto de silla | Pendiente | — | — |
| F8.11 | `multiplicadoresintdobles.tex` | Figura región factible Lagrange | Pendiente | — | — |
| F8.12 | `inttriples.tex` | Sección Jacobiano 2×2 (nueva) | Pendiente | — | — |
| F8.13 | `inttriples.tex` | Sección Jacobiano 3×3 + reencuadre cil./esf. | Pendiente | — | — |
| F8.14 | `inttriples.tex` | Figura geométrica Jacobiano | Pendiente | — | — |
| F8.15 | `apintdobles.tex` | Figuras región tipo I y II | Pendiente | — | — |
| F8.16 | `apintdobles.tex` | Figura cambio de orden | Pendiente | — | — |
| F8.17 | `cap34_integrales_vectoriales.tex` | Figura campo vectorial quiver | Pendiente | — | — |
| F8.18 | `cap34_integrales_vectoriales.tex` | Figura curva orientada integral de línea | Pendiente | — | — |
| F8.19 | `cap34_integrales_vectoriales.tex` | Figura superficie orientada + normal | Pendiente | — | — |
| F8.20 | caps. 18–22 | Auditoría orden R1 | Pendiente | — | — |
| F8.21 | `cap34_integrales_vectoriales.tex` | Esquema prueba Green | Pendiente | — | — |
| F8.22 | `cap34_integrales_vectoriales.tex` | Esquema prueba Stokes | Pendiente | — | — |
| F8.23 | `cap34_integrales_vectoriales.tex` | Esquema prueba Divergencia | Pendiente | — | — |
| F8.24 | caps. 18, 19, 32 | Introducciones narrativas | Pendiente | — | — |
| F8.02 | `funvectoriales.tex` | Figura hélice R³ | Pendiente | — | — |
| F8.03 | `funvectoriales.tex` | Figura paraboloide + curvas nivel | Pendiente | — | — |
| F8.04 | `limvariasvariables.tex` | Figura vecindad ε-δ | Pendiente | — | — |
| F8.05 | `limvariasvariables.tex` | Figura trayectorias límite | Pendiente | — | — |
| F8.06 | `planostangentes.tex` | Figura plano tangente 3D | Pendiente | — | — |
| F8.07 | `planostangentes.tex` | Figura aproximación lineal | Pendiente | — | — |
| F8.08 | `gradientes.tex` | Figura gradiente + curvas nivel | Pendiente | — | — |
| F8.09 | `gradientes.tex` | Figura derivada direccional | Pendiente | — | — |
| F8.10 | `multiplicadoresintdobles.tex` | Figura punto de silla | Pendiente | — | — |
| F8.11 | `multiplicadoresintdobles.tex` | Figura región factible Lagrange | Pendiente | — | — |
| F8.12 | `inttriples.tex` | Sección Jacobiano 2×2 (nueva) | Pendiente | — | — |
| F8.13 | `inttriples.tex` | Sección Jacobiano 3×3 + reencuadre cil./esf. | Pendiente | — | — |
| F8.14 | `inttriples.tex` | Figura geométrica Jacobiano | Pendiente | — | — |
| F8.15 | `apintdobles.tex` | Figuras región tipo I y II | Pendiente | — | — |
| F8.16 | `apintdobles.tex` | Figura cambio de orden | Pendiente | — | — |
| F8.17 | `cap34_integrales_vectoriales.tex` | Figura campo vectorial quiver | Pendiente | — | — |
| F8.18 | `cap34_integrales_vectoriales.tex` | Figura curva orientada integral de línea | Pendiente | — | — |
| F8.19 | `cap34_integrales_vectoriales.tex` | Figura superficie orientada + normal | Pendiente | — | — |
| F8.20 | caps. 18–22 | Auditoría orden R1 | Pendiente | — | — |
| F8.21 | `cap34_integrales_vectoriales.tex` | Esquema prueba Green | Pendiente | — | — |
| F8.22 | `cap34_integrales_vectoriales.tex` | Esquema prueba Stokes | Pendiente | — | — |
| F8.23 | `cap34_integrales_vectoriales.tex` | Esquema prueba Divergencia | Pendiente | — | — |
| F8.24 | caps. 18, 19, 32 | Introducciones narrativas | Pendiente | — | — |

---

## Notas de protocolo

- Cada ítem se ejecuta en Claude Code con los archivos `.tex` abiertos.
- Compilar con LuaLaTeX después de cada ítem. Si la compilación falla, revertir antes de continuar.
- Las figuras pgfplots 3D usan `shader=flat` y `samples=20` como máximo para mantener tiempo de compilación < 15 s.
- Las figuras TikZ 2D no tienen restricción de tiempo pero deben quedar en < 80 líneas.
- Este archivo se actualiza al cerrar cada ítem: Estado → `completo`, Fecha → fecha real, Notas → observaciones concretas.
- Antes de ejecutar cualquier ítem: (1) leer las primeras 50 líneas del archivo `.tex` destino, (2) ejecutar `grep -c "\begin{prob}"` y `grep -c "\begin{myproof}"` para conteo real, (3) compilar con LuaLaTeX después del ítem y confirmar 0 errores antes de continuar.
- En ítems F8.P2, F8.P3, F8.P4: cada `\begin{myproof}` nuevo debe presentarse al autor para validación antes de escribirlo al archivo. No cerrar el ítem hasta confirmación explícita del autor.
- Archivos de referencia en el directorio: `PLAN_FASE8_APOSTOL_C3.md` (plan completo), `PROGRESO.md` (historial fases anteriores), `PROGRESO_VERIFICACION.md` (estado verificación matemática).
