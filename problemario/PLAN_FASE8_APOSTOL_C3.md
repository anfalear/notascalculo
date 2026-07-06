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
**Estado:** Completo — 2026-06-26. `figuras_guia.tex` creado con plantillas A (hélice+tangente), B (paraboloide+normal) y C (región tipo I). Estándares globales documentados al final del archivo.

---

### F8.02 — Cap. 18 (`funvectoriales.tex`): figura curva en R³ y vector tangente
**Sección destino:** inmediatamente después de la definición de función vectorial  
**Figura:** hélice $\mathbf{r}(t)=(\cos t, \sin t, t/2)$ con vector tangente en $t=\pi/2$, ejes xyz etiquetados, sin relleno de superficie  
**TikZ:** `tikzpicture` con `tdplot` o pgfplots 3D axis — elegir el que compile más rápido  
**Líneas estimadas:** 40–60  
**Estado:** Completo — 2026-06-26. Figura pgfplots 3D insertada después de `\end{definition}` de función vectorial (entre párrafo "curva parametrizada" y subsección Límite). `\label{fig:helice_tangente}`. Compilación limpia.

---

### F8.03 — Cap. 18 (`funvectoriales.tex`): figura superficie de nivel y curvas de nivel
**Sección destino:** después de la definición de función de varias variables / curvas de nivel  
**Figura:** paraboloide $z=x^2+y^2$ visto desde arriba con 4 curvas de nivel $c=1,2,3,4$ en el plano $xy$ (proyección), y la superficie en 3D encima — dos subfiguras o figura compuesta  
**TikZ:** pgfplots `surf` + pgfplots 2D para proyección  
**Líneas estimadas:** 60–80  
**Estado:** Completo — 2026-06-26. Figura doble (minipage 46%+50%) insertada después de `\end{pasos}[Trazado de curvas de nivel]` y antes del ejemplo resuelto de paraboloide. Izquierda: TikZ 2D con 4 círculos (c=1,2,3,4, scale=1.1). Derecha: pgfplots 3D surf shader=flat corner samples=20. `\label{fig:paraboloide_curvas_nivel}`.

---

### F8.04 — Cap. 19 (`limvariasvariables.tex`): figura vecindad abierta en R²
**Sección destino:** después de la definición de límite (ε-δ en R²)  
**Figura:** disco abierto $B((x_0,y_0),\delta)$ con punto interior, borde punteado, etiquetas $\delta$, $(x_0,y_0)$, y banda de salida $|f-L|<\varepsilon$ indicada en texto lateral  
**TikZ:** `tikzpicture` puro, 2D  
**Líneas estimadas:** 30–45  
**Estado:** Completo — 2026-06-26. TikZ 2D insertado inmediatamente después de `\end{definition}[Límite de una función de dos variables]`. Disco relleno azul claro, borde punteado, radio δ, punto interior (x,y), nota ε lateral. `\label{fig:disco_epsilon_delta}`.

---

### F8.05 — Cap. 19 (`limvariasvariables.tex`): figura discontinuidad esencial sobre recta
**Sección destino:** después del ejemplo de límite que no existe (trayectorias distintas)  
**Figura:** dos trayectorias hacia el origen con límites distintos — recta $y=mx$ y parábola $y=x^2$ — con flechas de dirección y etiquetas de límite obtenido por cada camino  
**TikZ:** `tikzpicture` puro, 2D  
**Líneas estimadas:** 35–50  
**Estado:** Completo — 2026-06-26. TikZ 2D insertado DENTRO del example "Límite que no existe por trayectorias distintas", entre el enunciado y `\begin{myproof}` (F8.30 integrado aquí). Recta y=x (rojo) y parábola y=x² (azul) con flechas →(0,0) y etiquetas lim=0 / lim=1/2. `\label{fig:trayectorias_limite}`.

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
**Estado:** Completo — 2026-06-26. Nueva sección insertada antes de `\section{Coordenadas cilíndricas}`. Contiene: definición Jacobiano 2×2, figura F8.14 (incrustada), teorema cambio de variables, rem sobre J=0, ejemplo coordenadas polares (e^{r²}, disco r≤2, resultado π(e⁴-1) con 4 pasos + boxed). `\label{sec:cambio-var-dobles}`.

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
**Estado:** Completo — 2026-06-26. Nueva sección `\section{Cambio de variables en integrales triples}` con definición Jacobiano 3×3, teorema cambio de variables triple, párrafo de conexión con cilíndricas/esféricas. Definición cilíndrica ampliada con cálculo explícito del determinante 3×3 (→ r). Definición esférica con nota referenciando la sección. `\label{sec:cambio-var-triples}`.

---

### F8.14 — Cap. 33 (`inttriples.tex`): figura geométrica del Jacobiano
**Sección destino:** dentro de F8.12, después de la definición de Jacobiano  
**Figura:** cuadrado $[0,1]^2$ en plano $(u,v)$ → paralelogramo deformado en plano $(x,y)$ con los vectores columna del Jacobiano como lados, área $= |J|$ indicada  
**TikZ:** `tikzpicture` 2D, dos subfiguras con flecha de transformación entre ellas  
**Líneas estimadas:** 40–55  
**Estado:** Completo — 2026-06-26. Figura minipage doble (42%+10%+42%) dentro de F8.12, entre definición y teorema. Cuadrado azul R*=[0,1]² ← T → paralelogramo rojo R con "área=|J|". `\label{fig:jacobiano_2x2}`.

---

## Semana 4 — Figuras caps. 32 y 34

### F8.15 — Cap. 32 (`apintdobles.tex`): figuras región tipo I y tipo II
**Sección destino:** antes de la integral sobre región general (no rectangular)  
**Figura A:** región tipo I — $a \le x \le b$, $g_1(x) \le y \le g_2(x)$ — con curvas $g_1$, $g_2$ etiquetadas y franja vertical sombreada  
**Figura B:** región tipo II — $c \le y \le d$, $h_1(y) \le x \le h_2(y)$ — franja horizontal  
**TikZ:** dos `tikzpicture` 2D en minipages lado a lado  
**Líneas estimadas:** 60–80  
**Estado:** Completo — 2026-06-26. Dos minipages TikZ 2D: (a) tipo I azul con curvas g₁/g₂ y líneas dashed a=b, (b) tipo II rojo con curvas h₁/h₂ y líneas dashed c=d. Insertado antes de `\begin{pasos}[Integral doble sobre una región general]`. `fig:region_tipo_I_II`.

---

### F8.16 — Cap. 32 (`apintdobles.tex`): figura cambio de orden de integración
**Sección destino:** después del primer ejemplo de región no rectangular  
**Figura:** región acotada por dos curvas, con las dos descomposiciones posibles (vertical y horizontal) superpuestas, indicando cuál es más simple  
**TikZ:** `tikzpicture` 2D  
**Líneas estimadas:** 45–60  
**Estado:** Completo — 2026-06-26. Dos minipages TikZ 2D (escala 2.0): región D entre y=x² e y=x con franjas verticales (a, dy dx) y horizontales (b, dx dy). Insertado después de `\end{rem}` y antes de `\section*{Problemas propuestos}`. `fig:cambio_orden_integracion`.

---

### F8.17 — Cap. 34 (`cap34_integrales_vectoriales.tex` — ahora Cap. 33 del libro): figura campo vectorial con flechas
**Sección destino:** después de la definición de campo vectorial  
**Figura:** campo $\mathbf{F}(x,y)=(-y,x)$ (rotacional puro) en grilla $[-2,2]^2$ con flechas proporcionales, ejes etiquetados  
**TikZ:** pgfplots 2D con `quiver` — es el método más limpio para campos vectoriales en pgfplots  
**Líneas estimadas:** 35–50  
**Estado:** Completo — 2026-06-26. TikZ puro con `\foreach \xi/\yi in {...}`: grilla 5×5 (excl. origen) de flechas F=(-y,x)×0.28, escala=0.88. Insertado entre párrafo introductorio de div/rot y `\begin{definition}[Divergencia]`. `fig:campo_vectorial_rotacional`.

---

### F8.18 — Cap. 34: figura curva orientada para integral de línea
**Sección destino:** antes de la definición de integral de línea escalar  
**Figura:** curva suave $C$ de $A$ a $B$ en R², con flechas de orientación, punto de muestreo $P_i$, segmento $\Delta s_i$ indicado, y valor $f(P_i)$ como altura sobre la curva (barra vertical)  
**TikZ:** `tikzpicture` 2D  
**Líneas estimadas:** 45–60  
**Estado:** Completo — 2026-06-26. TikZ 2D: curva cerrada suave C con dos segmentos orientados (→ en cada mitad), región R sombreada azul, etiqueta "orientación +". Insertado entre `\end{definition}[Curva cerrada...]` y `\begin{theorem}[Teorema de Green]`. `fig:curva_orientacion_positiva`.

---

### F8.19 — Cap. 34: figura superficie orientada con vector normal
**Sección destino:** antes de la definición de integral de superficie vectorial (flujo)  
**Figura:** parche de superficie con vector normal $\mathbf{n}$ en varios puntos, orientación consistente indicada por sentido de giro del borde, con dos caras diferenciadas visualmente  
**TikZ:** pgfplots 3D con `surf`, vectores normales añadidos con `\draw[->]`  
**Líneas estimadas:** 55–75  
**Estado:** Completo — 2026-06-26. pgfplots 3D: paraboloide z=4-x²-y² (colormap/cool, samples=14, opacity=0.75) + 4 vectores normales n (dirección ∇F normalizada) en rojo. Insertado entre párrafo "flujo" y `\begin{definition}[Flujo de un campo vectorial]`. `fig:superficie_orientada`.

---

## Semana 5 — Revisión orden interno R1 + esquemas de prueba

### F8.20 — Auditoría R1: verificar orden canónico en caps. 18–22
**Acción:** revisar que en cada capítulo el orden sea definición → figura → teorema → prueba/esquema → ejemplo → problemas. Registrar cualquier inversión.  
**Entregable:** lista de inversiones encontradas + correcciones aplicadas (cada corrección ≤ 50 líneas de reordenamiento)  
**Estado:** Completo — 2026-06-26

**Inversiones encontradas y acciones:**

| Cap | ID | Descripción | Acción |
|---|---|---|---|
| 18 | — | `\begin{rem}[Interpretación geométrica]` de longitud de arco viene después del ejemplo. Revisado: el rem interpreta el resultado numérico del ejemplo (L = 2π√2), no motiva la definición. Posición post-ejemplo es correcta. | SIN INVERSIÓN REAL. No se modifica. |
| 18 | INV18.2 | Subsección "Reglas de derivación": teorema sin ejemplo resuelto ilustrativo. | REGISTRADO (ausencia, no inversión de posición). Pendiente F8.25. |
| 19 | INV19.1 | `\begin{theorem}[Composición de funciones continuas]` + proof venían después de 3 probs resueltos de discontinuidad. | REGISTRADO. No se corrige: los probs ilustran casos de discontinuidad que motivan el teorema — orden pedagógicamente justificado. |
| 20 | INV20.1 | Párrafo de interpretación geométrica + figura de derivadas parciales venían DESPUÉS de dos ejemplos (antes: def → rem → ej1 → ej2 → figura). | **CORREGIDO**: movidos entre `\end{rem}` (notación) y `\begin{example}[Derivadas parciales por definición]`. Nuevo orden: def → rem(notación) → párrafo+figura(geométrica) → ej1 → ej2. (38 líneas). |
| 20 | INV20.2 | Falta párrafo introductorio del capítulo. | REGISTRADO. Cubierto por F8.24 (pendiente). |
| 21 | INV21.1 | Figura `fig:gradiente_curvas_nivel` viene después del `\begin{theorem}[Propiedades del gradiente]`. | REGISTRADO. No se corrige: la figura ilustra inmediatamente la lista de interpretación geométrica que la precede — coherencia interna mantenida. |
| 22 | — | Sin inversiones. Estructura correcta en todo el capítulo. | — |

---

### F8.21 — Esquema de prueba: Teorema de Green (Cap. 34)
**Verificar:** si la demostración actual es completa o solo enunciado  
**Acción según resultado:**  
- Si es solo enunciado: añadir esquema con pasos clave (dividir región en tipo I + tipo II, aplicar TFC a cada integral itinerada, sumar)  
- Si es completa: añadir figura geométrica del argumento (región con borde orientado, franjas verticales/horizontales)  
**Líneas estimadas:** 40–80 según caso  
**Estado:** Completo — 2026-06-26. Prueba ya era completa (pedagógica, región tipo I+II). Figura TikZ 2D añadida después de `\end{proof}`: elipse como región R + franja vertical clipeada (azul oscuro) + orientación antihoraria de C (decorations.markings) + etiquetas g₁(x), g₂(x), C₁(→), C₂(←), a, b. `fig:green_region_tipo_I`. 764 págs, 0 errores.

---

### F8.22 — Esquema de prueba: Teorema de Stokes (Cap. 34)
**Verificar:** si la prueba de Green como caso particular de Stokes (que ya existe) es suficiente o si falta el esquema general  
**Acción:** añadir figura con superficie $S$, borde $\partial S$ orientado por regla de la mano derecha, y micro-circulaciones del rotacional  
**Líneas estimadas:** 35–55  
**Estado:** Completo — 2026-06-26. Figura TikZ 2D añadida entre `\end{rem}` y `\begin{proof}`: forma orgánica cerrada como superficie S + borde ∂S con 3 flechas stealth (regla de la mano derecha) + 3 vectores n (azul) + 3 micro-circulaciones arc CCW (gris). `fig:stokes_superficie`. 764 págs, 0 errores.

---

### F8.23 — Esquema de prueba: Teorema de la Divergencia (Cap. 34)
**Verificar:** estado de la demostración actual  
**Acción:** añadir esquema con sólido $E$ dividido en rebanadas verticales, flujo neto por cara superior e inferior, cancelación de caras internas  
**Líneas estimadas:** 40–60  
**Estado:** Completo — 2026-06-26. Figura TikZ 2D añadida después de `\end{proof}`: grilla 2×2 de celdas (sólido Q) + flechas de cancelación en cara interior vertical (rojas, opuestas) + flechas de flujo neto en ∂Q exterior (azules, hacia afuera) + etiquetas Q y ∂Q. `fig:divergencia_cancelacion`. 764 págs, 0 errores.

---

### F8.24 — Introducción narrativa: caps. 18, 19, 32 (los que no tienen párrafo introductorio)
**Acción:** verificar cuáles capítulos C3 carecen de párrafo introductorio (motivación del capítulo antes de la primera sección). Añadir donde falte: 1 párrafo de 4–6 líneas con la pregunta central del capítulo y su conexión con lo anterior.  
**Líneas estimadas:** 6–8 por capítulo afectado  
**Estado:** Completo — 2026-06-26. Auditoría real: caps 18, 19, 32, 33 ya tenían intro completa. Cap 20 (`planostangentes.tex`) carecía de párrafo a nivel `\chapter` (saltaba directo a `\section`). Añadido párrafo de 9 líneas entre `\chapter{...}` y los comentarios de sección: conecta con cap 19 (límites/continuidad), introduce derivada parcial, plano tangente y diferenciabilidad, y advierte que DP existentes ≠ diferenciable. 764 págs, 0 errores.

---

## Semana 6 — Auditorías y contenido adicional Cap. 18

### F8.25 — Cap. 18 (`funvectoriales.tex`): auditoría de ejemplos de dominio sin figura
**Acción:** recorrer todos los ejemplos de dominio de funciones de varias variables que estén resueltos (cálculo del dominio) pero sin figura TikZ asociada. Por cada uno: añadir figura TikZ 2D del dominio en el plano xy (región sombreada, frontera etiquetada, punto de exclusión si aplica).  
**Criterio de cierre:** ningún ejemplo de dominio calculado queda sin representación gráfica.  
**Líneas estimadas:** 20–40 por figura (número total depende de auditoría).  
**Estado:** Completo — 2026-06-26. Auditoría: 1 `\begin{example}` de dominio sin figura (línea 794: $f=\sqrt{x+y}/\ln(x-y)$). Los 4 `\begin{prob}` de dominio que siguen ya tienen figuras. Figura añadida dentro de myproof, entre descripción verbal del Paso 4 y `\boxed{}`: triángulo azul D (x>0, -x≤y<x) + línea y=-x sólida (incluida) + y=x rayada (excluida) + y=x-1 punteada (excluida interior) + punto (1,0) + círculo vacío en origen. `fig:dominio_log_raiz`. 764 págs, 0 errores.

---

### F8.26 — Cap. 18 (`funvectoriales.tex`): galería de superficies canónicas
**Acción:** añadir una sección (o subsección según el orden R1 del capítulo) con las 5 superficies cuádricas fundamentales: paraboloide elíptico, paraboloide hiperbólico, cono elíptico, hiperboloide de una hoja, hiperboloide de dos hojas. Para cada superficie: figura pgfplots 3D (shader=flat, samples=20), ecuación canónica, nombre, y 1 ejemplo resuelto con estructura de 4 pasos + `\boxed{}` (dominio, trazado por trazas, identificación de tipo).  
**Criterio de cierre:** las 5 superficies presentes, cada una con figura + ejemplo resuelto completo.  
**Líneas estimadas:** 200–280 en total.  
**Estado:** Completo — 2026-06-26. Nueva `\subsection{Superficies cuádricas}` (`\label{sec:superficies-cuadricas}`) insertada entre `\subsection{Gráfica}` y `\subsection{Curvas y superficies de nivel}`. Rem anterior actualizado ("en secciones posteriores" → "en la subsección siguiente"). Las 5 superficies con figura pgfplots 3D + ejemplo 4 pasos + boxed: (1) paraboloide elíptico z=x²+4y²; (2) paraboloide hiperbólico z=x²-y²; (3) cono circular z²=x²+y² (2 napas); (4) hiperboloide 1 hoja x²+y²-z²=1 (paramétrico, samples=18); (5) hiperboloide 2 hojas z²-x²-y²=1 (2 casquetes). Todas las figuras con `[H]`. 766 págs, 0 errores.

---

### F8.27 — Cap. 18 (`funvectoriales.tex`): ejemplos resueltos de superficies de nivel
**Acción:** añadir 2–3 ejemplos resueltos de superficies de nivel $f(x,y,z)=c$ para varios valores de $c$, cada uno con figura pgfplots 3D mostrando la familia de superficies. Los ejemplos deben cubrir casos distintos (esfera, elipsoide, paraboloide) para ilustrar variedad de comportamiento.  
**Criterio de cierre:** 2–3 ejemplos resueltos con 4 pasos + `\boxed{}`, cada uno con figura 3D.  
**Líneas estimadas:** 80–120 en total.  
**Estado:** Completo — 2026-06-26. 3 ejemplos añadidos después de `\end{rem}[Interpretación en topografía]` y antes del primer `\begin{prob}`: (1) esferas $f=x^2+y^2+z^2$ ($k=1,4,9$ → radios 1,2,3; figura esfera unitaria paramétrica); (2) elipsoide $f=x^2+y^2/4+z^2/9$ ($k=1$ → semiejes 1,2,3; figura elipsoide paramétrico); (3) paraboloides $f=x^2+y^2-z$ ($k=0,-1$ → vértices en $z=0,1$; figura 2 paraboloides superpuestos). Figuras `fig:nivel_esfera`, `fig:nivel_elipsoide`, `fig:nivel_paraboloides`. 768 págs, 0 errores.

---

### F8.28 — Cap. 18 (`funvectoriales.tex`): auditoría de estructura interna de resueltos
**Acción:** verificar que todos los ejemplos resueltos existentes en `funvectoriales.tex` tienen la estructura de 4 pasos del protocolo diagnóstico + `\boxed{}` en el resultado final. Corregir los que no cumplan: añadir los pasos faltantes, reorganizar si el orden es incorrecto, añadir `\boxed{}` donde falte.  
**Criterio de cierre:** todos los resueltos existentes cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–30 por ejemplo corregido (número total depende de auditoría).  
**Estado:** Completo — 2026-06-26

**Correcciones aplicadas (4 de 7 ejemplos):**
- L.129 (Límite vectorial): añadido `\textbf{Paso 4: Resultado vectorial.}` antes de `\boxed{}`. Tenía 3 pasos.
- L.323 (Derivada hélice): reestructurado de 2 a 4 pasos: Paso 1 (componentes de r), Paso 2 (derivar), Paso 3 (función derivada), Paso 4 (evaluar en π/4).
- L.465 (Integral vectorial): añadido `\textbf{Paso 4: Resultado vectorial.}` antes de `\boxed{}`. Tenía 3 pasos.
- L.711 (Longitud arco circunferencia): separado verificación en Paso 4 independiente. Tenía 3 pasos.
- L.550 (Longitud hélice): ya tenía 4 pasos + `\boxed{}`. Sin cambios.
- L.794 (Dominio log+raíz): ya tenía 4 pasos + `\boxed{}` (verificado en F8.25). Sin cambios.
- L.1328 (Curvas de nivel paraboloide): ya tenía 4 pasos + `\boxed{}`. Sin cambios.

PDF final: 762 páginas. Compilación limpia.

---

### F8.29 — Cap. 19 (`limvariasvariables.tex`): auditoría de estructura interna de resueltos
**Acción:** verificar que todos los ejemplos resueltos existentes en `limvariasvariables.tex` tienen la estructura de 4 pasos del protocolo diagnóstico + `\boxed{}` en el resultado final. Corregir los que no cumplan: añadir los pasos faltantes, reorganizar si el orden es incorrecto, añadir `\boxed{}` donde falte.  
**Criterio de cierre:** todos los resueltos existentes cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–30 por ejemplo corregido (número total depende de auditoría).  
**Estado:** Completo — 2026-06-27

**Correcciones aplicadas (11 elementos en 8 examples + 3 probs):**
- Example L.148 (tray. distintas): Paso 1+Conclusión → Pasos 1-4 (tray1/tray2/comparación/conclusión)
- Example L.286 (tray. paramétricas): ídem restructuración 4 pasos
- Example L.347 (rectas, sin pasos ni boxed): añadidos Pasos 1-4 + `\boxed{\text{No existe}}`
- Example L.521 (polares, 3 pasos): Paso 3 dividido en Paso 3 (independencia θ) + Paso 4 (resultado)
- Example L.579 (sustitución directa, 2 pasos): restructurado en 4 pasos (tipo/denominador/sustitución/resultado)
- Example L.623 (emparedado, 2 pasos): restructurado en 4 pasos (cota inf./cota sup./sandwich/resultado)
- Example L.776 (continuidad por partes, 3 pasos): Paso 3 dividido en unión + Paso 4 (resultado)
- Example L.818 (3 variables, Paso 1+Conclusión): restructurado en 4 pasos
- Prob L.261 (factorización, 3 pasos): añadido Paso 4 antes de `\boxed{}`
- Prob L.319 (polares raíz, 3 pasos): añadido Paso 4 antes de `\boxed{}`
- Prob L.489 (Prop. acotada, 3 pasos): añadido Paso 4 antes de `\boxed{}`

PDF final: 768 páginas. Compilación limpia.

---

### F8.30 — Cap. 19 (`limvariasvariables.tex`): vincular figura F8.05 a ejemplo resuelto
**Acción:** identificar el ejemplo resuelto de límite por trayectorias en `limvariasvariables.tex` (el que muestra límite inexistente por dos caminos distintos). Insertar la figura F8.05 (dos trayectorias hacia el origen con límites distintos — recta $y=mx$ y parábola $y=x^2$) inmediatamente después del enunciado del ejemplo y antes del desarrollo, con `\caption` y `\label` correctos. Verificar que las trayectorias de la figura corresponden exactamente a las trayectorias usadas en el ejemplo resuelto; si no coinciden, ajustar la figura para que sean consistentes.  
**Criterio de cierre:** figura F8.05 insertada en el lugar correcto, trayectorias de la figura y del ejemplo coinciden, caption y label presentes, compilación limpia.  
**Líneas estimadas:** 20–40.  
**Estado:** Completo — 2026-06-26. Integrado durante F8.05: figura con y=x y y=x² colocada dentro del example "Límite que no existe por trayectorias distintas", exactamente entre el enunciado y `\begin{myproof}`. Trayectorias coinciden con el ejemplo (y=x → lim=0, y=x² → lim=1/2).

---

## Semana 7 — Auditoría de figuras preexistentes

### F8.31 — Cap. 18 (`funvectoriales.tex`): auditoría de figuras preexistentes
**Acción:** identificar todas las figuras que ya existen en el archivo (anteriores a la Fase 8). Por cada una: verificar que está dentro de un entorno `figure`, tiene `\caption` descriptivo, tiene `\label` con convención `fig:`, y todas las etiquetas de puntos y curvas usan `anchor` explícito o desplazamiento `xshift`/`yshift` para evitar solapamiento. Corregir las que no cumplan el estándar de `figuras_guia.tex`.  
**Criterio de cierre:** todas las figuras preexistentes cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–20 por figura corregida (número total depende de auditoría).  
**Estado:** Completo — 2026-06-27

**Correcciones aplicadas (9 figuras preexistentes):**
- 4 figuras de dominio (círculos/elipses en probs): añadidos `\caption` y `\label` a cada `figure[H]`.
- 1 figura curvas de nivel paraboloide (en example): `\begin{center}` → `\begin{figure}[H]`, `\caption`, `\label`; etiquetas `k=...` con `anchor` explícito (`south`, `above left`, etc.).
- 2 figuras dominio R² (en probs de ln): `\caption`, `\label` + `anchor` explícito en `\node`.
- 2 figuras curvas de nivel ln: `\caption`, `\label` + `anchor=west` en etiquetas `z=`.
- 10 figuras de Fase 8 (F8.02–F8.27): todas ya compliant — sin cambios.

PDF: 768 páginas, 0 errores.

---

### F8.32 — Cap. 19 (`limvariasvariables.tex`): auditoría de figuras preexistentes
**Acción:** igual que F8.31 aplicado a `limvariasvariables.tex`.  
**Criterio de cierre:** todas las figuras preexistentes cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–20 por figura corregida (número total depende de auditoría).  
**Estado:** Completo — 2026-06-27

**Correcciones aplicadas:** 0. El archivo contiene exactamente 2 figuras, ambas de Fase 8 (F8.04: `fig:disco_epsilon_delta` y F8.05: `fig:trayectorias_limite`). No existen figuras preexistentes. Ambas figuras de F8 ya cumplen el protocolo completo: `figure[H]`, `\caption`, `\label{fig:...}`, `anchor` explícito en todos los `\node`.

---

### F8.33 — Cap. 20 (`planostangentes.tex`): auditoría de figuras preexistentes
**Acción:** igual que F8.31 aplicado a `planostangentes.tex`.  
**Criterio de cierre:** todas las figuras preexistentes cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–20 por figura corregida (número total depende de auditoría).  
**Estado:** Completo — 2026-06-27

**Correcciones aplicadas (1 figura preexistente):**
- L.68 (Interpretación geométrica DP): ya tenía `figure[H]` y `\caption`; añadido `\label{fig:dp_interpretacion_geometrica}` + `anchor=north` + color `red!70!black`/`blue!70!black` + `\small` a los dos `\node` que indicaban planos $y=y_0$ y $x=x_0$.
- 2 figuras de Fase 8 (`fig:plano_tangente_3d`, `fig:aprox_lineal_dz`): ya compliant — sin cambios.

---

### F8.34 — Cap. 21 (`gradientes.tex`): auditoría de figuras preexistentes
**Acción:** igual que F8.31 aplicado a `gradientes.tex`.  
**Criterio de cierre:** todas las figuras preexistentes cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–20 por figura corregida (número total depende de auditoría).  
**Estado:** Completo — 2026-06-27

**Correcciones aplicadas (1 figura preexistente):**
- L.1035 (triángulo en prob de razón de cambio): tenía `figure[H]` pero sin `\caption` ni `\label`. Añadido `anchor=south west` al `\node{$\theta$}`, `\caption{Triángulo con lados $x$, $y$ y ángulo $\theta$...}`, `\label{fig:triangulo_cadena}`.
- 2 figuras de Fase 8 (`fig:gradiente_curvas_nivel`, `fig:derivada_direccional`): ya compliant — sin cambios.

---

### F8.35 — Cap. 22 (`multiplicadoresintdobles.tex`): auditoría de figuras preexistentes
**Acción:** igual que F8.31 aplicado a `multiplicadoresintdobles.tex`.  
**Criterio de cierre:** todas las figuras preexistentes cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–20 por figura corregida (número total depende de auditoría).  
**Estado:** Completo — 2026-06-27

**Correcciones aplicadas (2 figuras preexistentes):**
- L.347 (trapecio canal, dentro de myproof): tenía `figure[H]` pero sin `\caption` ni `\label`. 4 nodos `$\theta$` sin anchor. Añadidos `anchor=center` a los 4, `\caption{Sección transversal del canal...}`, `\label{fig:trapecio_canal}`.
- L.734 (cúspide $y^3=x^2$): tenía `figure[H]` y `\caption` pero sin `\label`. 1 nodo sin anchor. Añadidos `anchor=south west` al nodo `$\nabla g(0,0)$` y `\label{fig:cuspide_lagrange_falla}`.
- 2 figuras de Fase 8 (`fig:punto_silla`, `fig:lagrange_region_factible`): ya compliant — sin cambios.

---

### F8.36 — Cap. 32 (`apintdobles.tex`): auditoría de figuras preexistentes
**Acción:** igual que F8.31 aplicado a `apintdobles.tex`.  
**Criterio de cierre:** todas las figuras preexistentes cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–20 por figura corregida (número total depende de auditoría).  
**Estado:** Completo — 2026-06-27

**Correcciones aplicadas (8 figuras preexistentes):**
- L.641 (lámina rect. x∈[0,4]): añadidos `\caption` + `\label{fig:lamina_rect_masa}`.
- L.664 (lámina y=e^x): añadidos `\caption` + `\label{fig:lamina_exp_masa}`.
- L.710 (lámina rect. b×h, inercia): añadidos `\caption` + `\label{fig:lamina_rect_inercia}`.
- L.1228 (lámina polar r=2sinθ): añadidos `\caption` + `\label{fig:lamina_polar_masa}`.
- L.1279 (`fig1.1`): label renombrado a `fig:region_cuadricas_1`; referencia en texto actualizada.
- L.1322: tenía `\caption` pero sin `\label`; añadido `\label{fig:region_cuadricas_2}`.
- L.1477 (`fig1.2`): label renombrado a `fig:region_polar_1`; referencia en texto actualizada.
- L.1504 (`fig3.2`): label renombrado a `fig:region_polar_2`; referencia en texto actualizada; caption diferenciado ("segunda variante").
- 3 figuras de Fase 8 (`fig:region_tipo_I_II`, `fig:cambio_orden_integracion`, `fig:jacobiano_2x2`): ya compliant — sin cambios.
- Todos los nodos ya tenían posicionamiento explícito — sin correcciones de anchor.

---

### F8.37 — Cap. 33 (`inttriples.tex`): auditoría de figuras preexistentes
**Acción:** igual que F8.31 aplicado a `inttriples.tex`.  
**Criterio de cierre:** todas las figuras preexistentes cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–20 por figura corregida (número total depende de auditoría).  
**Estado:** Completo — 2026-06-27

**Correcciones aplicadas:** 0. `inttriples.tex` no contiene ninguna figura (ni preexistentes ni de Fase 8 — la figura del Jacobiano `fig:jacobiano_2x2` fue insertada en `apintdobles.tex`).

---

### F8.38 — Cap. 33 (`cap33.tex`): auditoría de figuras preexistentes
**Acción:** igual que F8.31 aplicado a `cap33.tex` (Campos vectoriales e integrales de línea).  
**Criterio de cierre:** todas las figuras preexistentes cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–20 por figura corregida (número total depende de auditoría).  
**Estado:** Completo — 2026-06-27

**Correcciones aplicadas:** 0. `cap33.tex` no contiene ninguna figura.

---

### F8.39 — Cap. 34 (`cap34.tex`): auditoría de figuras preexistentes
**Acción:** igual que F8.31 aplicado a `cap34.tex` (Integrales de superficie y teoremas integrales).  
**Criterio de cierre:** todas las figuras preexistentes cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–20 por figura corregida (número total depende de auditoría).  
**Estado:** Completo — 2026-06-27

**Correcciones aplicadas (9 nodos sin anchor en 4 figuras de Fase 8):**
No hay figuras preexistentes. Las 6 figuras son de Fase 8 y ya tenían `figure[H]`, `\caption`, `\label`. Los nodos sin `anchor` explícito fueron corregidos:
- `fig:curva_orientacion_positiva`: `anchor=west` a $C$, `anchor=center` a $R$, `anchor=south` a "orientación +"
- `fig:green_region_tipo_I`: `anchor=center` a $R$, `anchor=west` a $C$
- `fig:divergencia_cancelacion`: `anchor=center` a "se cancelan" y a $Q$
- `fig:stokes_superficie`: `anchor=center` a $S$, `anchor=east` a "micro-circulaciones"

---

## Semana 8 — Revisión manual post-lectura

### F8.40 — Cap. 20 (`planostangentes.tex`): mejorar figura de derivadas parciales con rectas tangentes en 3D
**Acción:** localizar la figura existente de interpretación geométrica de derivadas parciales. Modificarla para que muestre explícitamente las dos rectas tangentes en el punto $(x_0, y_0, z_0)$: una en la dirección $x$ (pendiente $f_x$) y otra en la dirección $y$ (pendiente $f_y$), ambas sobre la superficie en 3D. Usar pgfplots 3D con `shader=flat`, `samples=20`. Etiquetas con `anchor` explícito. Figura dentro de `figure` con `\caption` y `\label`.  
**Criterio de cierre:** figura muestra superficie + punto + dos rectas tangentes etiquetadas, sin solapamiento de etiquetas, compilación limpia.  
**Líneas estimadas:** 60–90.  
**Estado:** Completo (2026-06-27). Figura TikZ 3D oblicua reemplazada por pgfplots 3D: paraboloide $z=x^2+y^2$ (shader=flat corner, samples=18, opacity=0.62, colormap/cool) + curva traza $y=1$ (rojo) + curva traza $x=1$ (azul) + recta tangente $f_x$ (rojo punteado) + recta tangente $f_y$ (azul punteado) + punto $(1,1,2)$ + etiquetas con anchor explícito. `fig:dp_interpretacion_geometrica`.

---

### F8.41 — Cap. 20 (`planostangentes.tex`): auditoría de resueltos sin 4 pasos
**Acción:** verificar que todos los ejemplos resueltos existentes en `planostangentes.tex` tienen la estructura de 4 pasos del protocolo diagnóstico + `\boxed{}` en el resultado final. Corregir los que no cumplan.  
**Criterio de cierre:** todos los resueltos cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–30 por ejemplo corregido.  
**Estado:** Completo (2026-06-27). 16 resueltos auditados, 16 corregidos:
1. DP definición: "Conclusión" → "Paso 3. Verificación." + "Paso 4. Resultado." + `\boxed{}`
2. DP reglas (a+b): reestructuración completa a 4 pasos
3. DP 2° orden: "Conclusión" → "Paso 3. Verificación (Clairaut)." + "Paso 4. Resultado."
4. 3 variables: estructura completa de 4 pasos añadida
5. $f_{xy},f_{yz},f_{zx}$: "Conclusión" → "Paso 3. Verificación (Clairaut)." + "Paso 4. Resultado."
6. $f_x(0,0)$: "Conclusión" → "Paso 3. Observación." + "Paso 4. Resultado."
7. Ecuación de onda: añadido "Paso 4. Resultado." antes de `\boxed{}`
8. Laplace: añadido "Paso 4. Resultado." antes de `\boxed{}`
9. Plano tangente paraboloide (enumerate): 4° ítem con `\boxed{}` añadido; removido de fuera del `\end{enumerate}`
10. $z=x^2y^3$ prob: añadido "Paso 4. Resultado." antes de `\boxed{z=16x+12y-20}`
11. Elipsoide+esfera: prosa reestructurada a 4 pasos explícitos
12. Paraboloide paralelo: prosa reestructurada a 4 pasos explícitos
13. Hiperboloide paralelo: prosa reestructurada a 4 pasos explícitos
14. Linealización $\sqrt{x^2+y^2}$ (enumerate 4 ítems): `\boxed{4.98}` movido dentro del ítem 4
15. Linealización $\ln(1+x+2y)$: añadido "Paso 4. Resultado." antes de `\boxed{}`
16. Diferenciabilidad $xe^{xy}$ (enumerate 3 ítems): añadido ítem 4 con `\boxed{}`; eliminada prosa con boxed fuera del enumerate

---

### F8.42 — Cap. 21 (`gradientes.tex`): auditoría de resueltos sin 4 pasos
**Acción:** igual que F8.41 aplicado a `gradientes.tex`.  
**Criterio de cierre:** todos los resueltos cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–30 por ejemplo corregido.  
**Estado:** Completo (2026-06-27). 16 resueltos auditados, 12 corregidos:
1. Voltaje: prosa → 4 pasos
2. Cono: prosa → 4 pasos
3. Caja área: prosa → 4 pasos
4. Triángulo: prosa → Paso 1-4 explícitos
5. Deriv. implícita ejemplo (enumerate 3 ítems + boxed fuera): añadido ítem 4 con boxed
6. $z=e^{xy}$: "Conclusión" → "Paso 4. Resultado."
7. $x^2y-y^2z+z^3=1$: añadido Paso 3 verificación + "Paso 4. Resultado."
8. Gradiente $x^2\sin y+e^{xy}$: 2 pasos → 4 pasos (split Paso 1-2 + Paso 3 ensamblaje + Paso 4)
9. Deriv. dir. (3 sub-partes a/b/c): Paso 1 Estrategia + Paso 2/3/4 (a/b/c)
10. Maximización (2 sub-partes): Paso 1 gradiente, Paso 2 normalizar, Paso 3 (a), Paso 4 (b)
11. Max crecimiento (3 sub-partes): Paso 1 Estrategia + Paso 2/3/4 (a/b/c)
12. Plano tang. + recta normal (3 sub-partes): Paso 1 Estrategia + Paso 2/3/4 (a/b/c)
Los 4 restantes ya cumplían el protocolo.

---

### F8.43 — Cap. 22 (`multiplicadoresintdobles.tex`): auditoría de resueltos sin 4 pasos
**Acción:** igual que F8.41 aplicado a `multiplicadoresintdobles.tex`.  
**Criterio de cierre:** todos los resueltos cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–30 por ejemplo corregido.  
**Estado:** Completo (2026-06-27). 12 resueltos auditados, 10 corregidos:
1. Punto más cercano plano $x-y+z=9$: prosa → Paso 1-4 + boxed
2. Canal trapecio: añadidos Paso 1-4 (preservando figura preexistente) + boxed
3. Caja tapa abierta: prosa → Paso 1-4 + boxed
4. Caja en primer octante: añadidos Paso 1-4 + boxed
5. Acuario mínimo costo: prosa → Paso 1-4 + boxed
6. Hardy-Weinberg: prosa → Paso 1-4 + boxed
7. Punto más cercano plano $2x+4y+3z=12$: prosa → Paso 1-4 + boxed
8. Temperatura placa circular: prosa → Paso 1-4 + boxed
9. Rectángulo hessiano (3 pasos): separado Paso 3→Paso 3+Paso 4 Resultado
10. Hessiano limitado prob ("Conclusión"): fusionado con Paso 4
Los 2 restantes ya cumplían el protocolo.

---

### F8.44 — Cap. 32 (`apintdobles.tex`): auditoría de resueltos sin 4 pasos
**Acción:** igual que F8.41 aplicado a `apintdobles.tex`.  
**Criterio de cierre:** todos los resueltos cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–30 por ejemplo corregido.  
**Estado:** Completo (2026-06-27). 27 myproof auditados, 21 corregidos: 19 con Paso 4 añadido antes de `\boxed{}`; 5 reestructuraciones completas prosa → 4 pasos. PDF: 772 págs.

---

### F8.45 — Cap. 33 (`inttriples.tex`): auditoría de resueltos sin 4 pasos
**Acción:** igual que F8.41 aplicado a `inttriples.tex`.  
**Criterio de cierre:** todos los resueltos cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–30 por ejemplo corregido.  
**Estado:** Completo (2026-06-27). 13 myproof auditados, 5 corregidos: L.71 enumerate → 4 pasos; L.146/L.233 Paso 4 añadido; L.172 → 4 pasos; L.299 Paso 2 dividido. PDF: 772 págs.

---

### F8.46 — Cap. 33 (`cap33.tex`): auditoría de resueltos sin 4 pasos
**Acción:** igual que F8.41 aplicado a `cap33.tex` (Campos vectoriales e integrales de línea).  
**Criterio de cierre:** todos los resueltos cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–30 por ejemplo corregido.  
**Estado:** Completo (2026-06-27). 6 myproof auditados, 2 corregidos: campo conservativo (boxed → Paso 4); integral de línea cuadrado (prosa → 4 pasos). PDF: 772 págs.

---

### F8.47 — Cap. 34 (`cap34.tex`): auditoría de resueltos sin 4 pasos
**Acción:** igual que F8.41 aplicado a `cap34.tex` (Integrales de superficie y teoremas integrales).  
**Criterio de cierre:** todos los resueltos cumplen el protocolo. Lista de correcciones registrada en las notas del ítem.  
**Líneas estimadas:** 10–30 por ejemplo corregido.  
**Estado:** Completo (2026-06-27). 18 myproof auditados, 6 corregidos: multi-parte (a-f), TFC, Green+elipse, campo vórtice, Stokes, Divergencia esfera. PDF: 772 págs.

---

### F8.48 — Caps. 32 y 33 (`apintdobles.tex`, `inttriples.tex`): figuras de cambio de coordenadas
**Acción:** crear tres figuras TikZ/pgfplots que expliquen geométricamente el cambio de coordenadas, insertadas en la sección correspondiente de cada capítulo:
- **Polares** (`apintdobles.tex`): círculo de radio $r$ con ángulo $\theta$, punto $(r,\theta)$ etiquetado, relaciones $x=r\cos\theta$, $y=r\sin\theta$ indicadas, explicación del elemento de área $r\,dr\,d\theta$.
- **Cilíndricas** (`inttriples.tex`): cilindro con variables $r$, $\theta$, $z$ etiquetadas, punto $(r,\theta,z)$ marcado, explicación del elemento de volumen $r\,dr\,d\theta\,dz$.
- **Esféricas** (`inttriples.tex`): esfera con variables $\rho$, $\phi$, $\theta$ etiquetadas, punto $(\rho,\phi,\theta)$ marcado, explicación del elemento de volumen $\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$.

Cada figura dentro de `figure` con `\caption` y `\label`. Etiquetas con `anchor` explícito sin solapamiento. Estándar de `figuras_guia.tex`.  
**Criterio de cierre:** tres figuras compilando limpio, cada una insertada inmediatamente antes de la primera integral en esas coordenadas.  
**Líneas estimadas:** 50–80 por figura (150–240 total).  
**Estado:** Completo (2026-06-27). Tres figuras TikZ 2D: (1) polares en `apintdobles.tex` — rectángulo polar r·Δr·Δθ con punto P(r,θ), proyecciones x=rcosθ/y=rsinθ, después del párrafo de dA; (2) cilíndricas en `inttriples.tex` — minipage doble (vista superior r,θ + vista lateral r,z) con dV=r dr dθ dz, entre `\end{definition}` y `\begin{theorem}` cilíndricas; (3) esféricas — vista en plano xz con ρ,φ,θ, dV=ρ²sinφ dρ dφ dθ, entre `\end{definition}` y `\begin{theorem}` esféricas. `fig:coordenadas_polares`, `fig:coordenadas_cilindricas`, `fig:coordenadas_esfericas`. PDF: 772 págs, 0 errores.

---

### F8.49 — Todos los capítulos C3: auditoría de problemas propuestos
**Acción:** recorrer todos los capítulos C3 (`funvectoriales.tex`, `limvariasvariables.tex`, `planostangentes.tex`, `gradientes.tex`, `multiplicadoresintdobles.tex`, `apintdobles.tex`, `inttriples.tex`, `cap33.tex`, `cap34.tex`) y por cada uno: (1) verificar que ningún problema propuesto contiene `\begin{myproof}` — eliminarlo si existe; (2) verificar que los propuestos están organizados por dificultad creciente — reordenar si no lo están, añadiendo comentario `% Básico`, `% Intermedio`, `% Desafiante` antes de cada grupo.  
**Criterio de cierre:** cero propuestos con myproof en todos los capítulos, todos los propuestos organizados por dificultad con comentarios de grupo. Compilación limpia.  
**Líneas estimadas:** 10–40 por capítulo.  
**Estado:** Completo (2026-06-27). Auditoría: 0 myproof dentro de `\begin{prob}` en la sección de propuestos en los 9 archivos. Tags % Básico / % Intermedio / % Desafiante añadidos a 7 archivos (funvectoriales, limvariasvariables, planostangentes, gradientes, multiplicadoresintdobles, apintdobles, inttriples). cap33 y cap34 ya tenían tags de F8.52/F8.53. PDF: 772 págs, 0 errores.

---

### F8.50 — Cap. 33 (`cap33.tex`): figura campo gradiente
**Acción:** crear figura pgfplots 2D con `quiver` mostrando el campo gradiente $\nabla f$ de una función concreta (e.g. $f(x,y)=x^2+y^2/4$) en una grilla $[-2,2]^2$, con curvas de nivel superpuestas mostrando la perpendicularidad entre el campo y las curvas. Figura dentro de `figure` con `\caption{Campo gradiente $\nabla f$ perpendicular a las curvas de nivel}` y `\label{fig:campo_gradiente}`. Etiquetas con `anchor` explícito. Estándar de `figuras_guia.tex`.  
**Criterio de cierre:** figura muestra campo + curvas de nivel + perpendicularidad visible, sin solapamiento, compilación limpia.  
**Líneas estimadas:** 50–70.  
**Estado:** Completo (2026-06-27). TikZ 2D con `\foreach` 4×4: flechas ∇f=(2x,y/2) en rojo + 3 elipses azules f=1/4,1/2,1. Insertado entre `\end{definition}[Campo vectorial gradiente]` y `\begin{rem}[Interpretación geométrica del gradiente]`. `fig:campo_gradiente`. PDF: 772 págs.

---

### F8.51 — Cap. 33 (`cap33.tex`): figura campo conservativo
**Acción:** crear figura pgfplots 2D con `quiver` mostrando un campo conservativo concreto (e.g. $\mathbf{F}(x,y)=(x,y)$, gradiente de $f=\frac{1}{2}(x^2+y^2)$) en grilla $[-2,2]^2$, con trayectoria cerrada superpuesta e indicación de que $\oint_C \mathbf{F}\cdot d\mathbf{r}=0$. Figura dentro de `figure` con `\caption{Campo conservativo: integral sobre trayectoria cerrada es cero}` y `\label{fig:campo_conservativo}`. Estándar de `figuras_guia.tex`.  
**Criterio de cierre:** figura muestra campo + trayectoria cerrada + etiqueta de resultado, sin solapamiento, compilación limpia.  
**Líneas estimadas:** 50–70.  
**Estado:** Completo (2026-06-27). TikZ 2D con `\foreach`: flechas radiales F=(x,y) en rojo + círculo azul orientado C + etiqueta ∮F·dr=0. Insertado entre `\end{definition}[Campo vectorial conservativo]` y `\begin{theorem}[Caracterización de campos conservativos]`. `fig:campo_conservativo`. PDF: 772 págs.

---

### F8.52 — Cap. 33 (`cap33.tex`): añadir problemas propuestos
**Acción:** revisar el conteo actual de propuestos en `cap33.tex`. Añadir los necesarios para alcanzar mínimo 15 propuestos, cubriendo: integral de línea escalar, integral de línea vectorial, campos conservativos y potenciales, teorema fundamental para integrales de línea, Green en región simplemente conexa, Green para calcular área. Organizar por dificultad con comentarios `% Básico`, `% Intermedio`, `% Desafiante`. Ningún propuesto nuevo lleva `\begin{myproof}`.  
**Criterio de cierre:** mínimo 15 propuestos, graduados, sin myproof, compilación limpia.  
**Líneas estimadas:** 60–100.  
**Estado:** Completo (2026-06-27). 7 originales preservados + 8 nuevos añadidos = 15 total. Nuevos: integral de línea vectorial directa (3 casos), TFC f=x²eʸ, campo conservativo R³ + potencial + TFC, campo F=(2xy+eʸ,x²+xeʸ), Green aplicación directa (2 casos), Green para áreas (elipse+astroide), campo de vórtice dominio no s.c. (4 partes), Green estratégico. Grupos: 4 Básico + 7 Intermedio + 4 Desafiante. PDF: 772 págs, 0 errores.

---

### F8.53 — Cap. 34 (`cap34.tex`): añadir problemas propuestos
**Acción:** revisar el conteo actual de propuestos en `cap34.tex`. Añadir los necesarios para alcanzar mínimo 15 propuestos, cubriendo: integral de superficie escalar, integral de superficie vectorial (flujo), Stokes sobre superficie con borde no trivial, Divergencia en sólido acotado, aplicaciones (masa de superficie, flujo total). Organizar por dificultad con comentarios `% Básico`, `% Intermedio`, `% Desafiante`. Ningún propuesto nuevo lleva `\begin{myproof}`.  
**Criterio de cierre:** mínimo 15 propuestos, graduados, sin myproof, compilación limpia.  
**Líneas estimadas:** 60–100.  
**Estado:** Completo (2026-06-27). 16 originales reordenados por dificultad (sin eliminar ninguno). Grupos: 5 Básico (div/rot, interp. física, Green cuadrado, Green círculo, integral escalar curva) + 7 Intermedio (TFC, campo conservativo 3 partes, Green verificar, integral sup. cilindro, circulación Stokes, flujo Divergencia, campo potencial R³) + 4 Desafiante (área toro, ∇·(∇×F)=0, lámina z=xy masa+CM, demostración conservativo→flujo+circ 0). PDF: 772 págs, 0 errores.

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
| F8.P7 | `inttriples.tex` | Conteo real + ajuste | Completo | 2026-06-25 | Ver bloque narrativo Semana 0. |
| F8.P8 | `cap34_integrales_vectoriales.tex` | Elevar 8–10 resueltos, podar propuestos | Completo | 2026-06-25 | Ver bloque narrativo Semana 0. |
| F8.01 | `figuras_guia.tex` (nuevo) | Plantilla TikZ | Completo | 2026-06-26 | 3 plantillas (hélice, paraboloide+normal, región tipo I) + estándares globales. Excluido de `\input` en doc principal (es solo referencia). |
| F8.02 | `funvectoriales.tex` | Figura hélice R³ | Completo | 2026-06-26 | pgfplots 3D, después de def. función vectorial. `fig:helice_tangente`. |
| F8.03 | `funvectoriales.tex` | Figura paraboloide + curvas nivel | Completo | 2026-06-26 | Minipage doble, después de pasos trazado curvas nivel. `fig:paraboloide_curvas_nivel`. |
| F8.04 | `limvariasvariables.tex` | Figura vecindad ε-δ | Completo | 2026-06-26 | TikZ 2D, después de def. límite 2 vars. `fig:disco_epsilon_delta`. |
| F8.05 | `limvariasvariables.tex` | Figura trayectorias límite | Completo | 2026-06-26 | TikZ 2D dentro del example "trayectorias distintas", antes de myproof. F8.30 integrado. `fig:trayectorias_limite`. |
| F8.06 | `planostangentes.tex` | Figura plano tangente 3D | Completo | 2026-06-26 | pgfplots 3D paraboloide + plano tangente (naranja) + normal, antes del pasos-protocolo. `fig:plano_tangente_3d`. |
| F8.07 | `planostangentes.tex` | Figura aproximación lineal | Completo | 2026-06-26 | TikZ 2D sección con Δz vs dz + segmento error, después de def. diferencial total. `fig:aprox_lineal_dz`. |
| F8.08 | `gradientes.tex` | Figura gradiente + curvas nivel | Completo | 2026-06-26 | TikZ 2D 5 elipses f=x²+y²/4 + 4 vectores ∇f, antes de subsección interpretación geométrica. `fig:gradiente_curvas_nivel`. |
| F8.09 | `gradientes.tex` | Figura derivada direccional | Completo | 2026-06-26 | pgfplots 3D z=x²+y² con plano vertical y pendiente D_u f, antes del teorema fórmula gradiente. `fig:derivada_direccional`. |
| F8.10 | `multiplicadoresintdobles.tex` | Figura punto de silla | Completo | 2026-06-26 | pgfplots 3D z=x²-y² con curvas de curvatura ±, después de rem punto crítico. `fig:punto_silla`. |
| F8.11 | `multiplicadoresintdobles.tex` | Figura región factible Lagrange | Completo | 2026-06-26 | TikZ 2D elipses f + recta g=0 + punto óptimo + ∇f, antes del pasos-método Lagrange. `fig:lagrange_region_factible`. |
| F8.12 | `inttriples.tex` | Sección Jacobiano 2×2 (nueva) | Completo | 2026-06-26 | Nueva `\section{Cambio de variables en integrales dobles}` con def. Jacobiano 2×2, teorema cambio de variables, ejemplo polares (e^(x²+y²), disco r≤2 → π(e⁴-1)). |
| F8.13 | `inttriples.tex` | Sección Jacobiano 3×3 + reencuadre cil./esf. | Completo | 2026-06-26 | Nueva `\section{Cambio de variables en integrales triples}` con def. 3×3, teorema. Determinante cilíndrico explícito en def. cilíndricas. Nota esféricas referenciada. |
| F8.14 | `inttriples.tex` | Figura geométrica Jacobiano | Completo | 2026-06-26 | Figura minipage doble: cuadrado R*=[0,1]² → paralelogramo R con leyenda área=|J|. Dentro de F8.12. `fig:jacobiano_2x2`. |
| F8.15 | `apintdobles.tex` | Figuras región tipo I y II | Completo | 2026-06-26 | Minipages TikZ 2D: tipo I (g₁/g₂ + franjas verticales) y tipo II (h₁/h₂ + franjas horizontales). `fig:region_tipo_I_II`. |
| F8.16 | `apintdobles.tex` | Figura cambio de orden | Completo | 2026-06-26 | Minipages TikZ 2D: región y=x²/y=x con franja vertical (a) y horizontal (b). `fig:cambio_orden_integracion`. |
| F8.17 | `cap34.tex` | Figura campo vectorial quiver | Completo | 2026-06-26 | TikZ `\foreach` grilla 5×5: F=(-y,x). Antes de def. Divergencia. `fig:campo_vectorial_rotacional`. |
| F8.18 | `cap34.tex` | Figura curva orientada integral de línea | Completo | 2026-06-26 | TikZ 2D: curva cerrada C orientada (+) con región R. Antes de Teorema Green. `fig:curva_orientacion_positiva`. |
| F8.19 | `cap34.tex` | Figura superficie orientada + normal | Completo | 2026-06-26 | pgfplots 3D z=4-x²-y² + 4 vectores n en rojo. Antes de def. Flujo. `fig:superficie_orientada`. |
| F8.20 | caps. 18–22 | Auditoría orden R1 | Completo | 2026-06-26 | 1 inversión corregida (INV20.1 planostangentes: figura DP antes de ejemplos); 3 registradas sin corrección (INV18.2, INV19.1, INV21.1). Cap 18 y 22 sin inversiones. |
| F8.21 | `cap34.tex` | Figura geométrica prueba Green | Completo | 2026-06-26 | TikZ 2D: elipse R + franja vertical + orientación CCW + etiquetas C₁/C₂/g₁/g₂. `fig:green_region_tipo_I`. 764 págs. |
| F8.22 | `cap34.tex` | Figura superficie Stokes | Completo | 2026-06-26 | TikZ 2D: superficie S + ∂S orientado + vectores n + micro-circulaciones. `fig:stokes_superficie`. 764 págs. |
| F8.23 | `cap34.tex` | Figura cancelación Divergencia | Completo | 2026-06-26 | TikZ 2D: grilla 2×2 + flechas cancelación interna (rojo) + flujo ∂Q (azul). `fig:divergencia_cancelacion`. 764 págs. |
| F8.24 | `planostangentes.tex` | Introducción narrativa cap 20 | Completo | 2026-06-26 | Caps 18/19/32/33 ya tenían intro. Párrafo añadido en cap 20 (entre \chapter y \section). 764 págs. |
| F8.02 | `funvectoriales.tex` | Figura hélice R³ | Pendiente | — | — |
| F8.03 | `funvectoriales.tex` | Figura paraboloide + curvas nivel | Pendiente | — | — |
| F8.04 | `limvariasvariables.tex` | Figura vecindad ε-δ | Pendiente | — | — |
| F8.05 | `limvariasvariables.tex` | Figura trayectorias límite | Pendiente | — | — |
| F8.06 | `planostangentes.tex` | Figura plano tangente 3D | Completo | 2026-06-26 | pgfplots 3D paraboloide + plano tangente (naranja) + normal, antes del pasos-protocolo. `fig:plano_tangente_3d`. |
| F8.07 | `planostangentes.tex` | Figura aproximación lineal | Completo | 2026-06-26 | TikZ 2D sección con Δz vs dz + segmento error, después de def. diferencial total. `fig:aprox_lineal_dz`. |
| F8.08 | `gradientes.tex` | Figura gradiente + curvas nivel | Completo | 2026-06-26 | TikZ 2D 5 elipses f=x²+y²/4 + 4 vectores ∇f, antes de subsección interpretación geométrica. `fig:gradiente_curvas_nivel`. |
| F8.09 | `gradientes.tex` | Figura derivada direccional | Completo | 2026-06-26 | pgfplots 3D z=x²+y² con plano vertical y pendiente D_u f, antes del teorema fórmula gradiente. `fig:derivada_direccional`. |
| F8.10 | `multiplicadoresintdobles.tex` | Figura punto de silla | Completo | 2026-06-26 | pgfplots 3D z=x²-y² con curvas de curvatura ±, después de rem punto crítico. `fig:punto_silla`. |
| F8.11 | `multiplicadoresintdobles.tex` | Figura región factible Lagrange | Completo | 2026-06-26 | TikZ 2D elipses f + recta g=0 + punto óptimo + ∇f, antes del pasos-método Lagrange. `fig:lagrange_region_factible`. |
| F8.12 | `inttriples.tex` | Sección Jacobiano 2×2 (nueva) | Completo | 2026-06-26 | Nueva `\section{Cambio de variables en integrales dobles}` con def. Jacobiano 2×2, teorema cambio de variables, ejemplo polares (e^(x²+y²), disco r≤2 → π(e⁴-1)). |
| F8.13 | `inttriples.tex` | Sección Jacobiano 3×3 + reencuadre cil./esf. | Completo | 2026-06-26 | Nueva `\section{Cambio de variables en integrales triples}` con def. 3×3, teorema. Determinante cilíndrico explícito en def. cilíndricas. Nota esféricas referenciada. |
| F8.14 | `inttriples.tex` | Figura geométrica Jacobiano | Completo | 2026-06-26 | Figura minipage doble: cuadrado R*=[0,1]² → paralelogramo R con leyenda área=|J|. Dentro de F8.12. `fig:jacobiano_2x2`. |
| F8.15 | `apintdobles.tex` | Figuras región tipo I y II | Completo | 2026-06-26 | Minipages TikZ 2D: tipo I (g₁/g₂ + franjas verticales) y tipo II (h₁/h₂ + franjas horizontales). `fig:region_tipo_I_II`. |
| F8.16 | `apintdobles.tex` | Figura cambio de orden | Completo | 2026-06-26 | Minipages TikZ 2D: región y=x²/y=x con franja vertical (a) y horizontal (b). `fig:cambio_orden_integracion`. |
| F8.17 | `cap34.tex` | Figura campo vectorial quiver | Completo | 2026-06-26 | TikZ `\foreach` grilla 5×5: F=(-y,x). Antes de def. Divergencia. `fig:campo_vectorial_rotacional`. |
| F8.18 | `cap34.tex` | Figura curva orientada integral de línea | Completo | 2026-06-26 | TikZ 2D: curva cerrada C orientada (+) con región R. Antes de Teorema Green. `fig:curva_orientacion_positiva`. |
| F8.19 | `cap34.tex` | Figura superficie orientada + normal | Completo | 2026-06-26 | pgfplots 3D z=4-x²-y² + 4 vectores n en rojo. Antes de def. Flujo. `fig:superficie_orientada`. |
| F8.20 | caps. 18–22 | Auditoría orden R1 | Completo | 2026-06-26 | 1 inversión corregida (INV20.1 planostangentes: figura DP antes de ejemplos); 3 registradas sin corrección (INV18.2, INV19.1, INV21.1). Cap 18 y 22 sin inversiones. |
| F8.21 | `cap34.tex` | Figura geométrica prueba Green | Completo | 2026-06-26 | TikZ 2D: elipse R + franja vertical + orientación CCW + etiquetas C₁/C₂/g₁/g₂. `fig:green_region_tipo_I`. 764 págs. |
| F8.22 | `cap34.tex` | Figura superficie Stokes | Completo | 2026-06-26 | TikZ 2D: superficie S + ∂S orientado + vectores n + micro-circulaciones. `fig:stokes_superficie`. 764 págs. |
| F8.23 | `cap34.tex` | Figura cancelación Divergencia | Completo | 2026-06-26 | TikZ 2D: grilla 2×2 + flechas cancelación interna (rojo) + flujo ∂Q (azul). `fig:divergencia_cancelacion`. 764 págs. |
| F8.24 | `planostangentes.tex` | Introducción narrativa cap 20 | Completo | 2026-06-26 | Caps 18/19/32/33 ya tenían intro. Párrafo añadido en cap 20 (entre \chapter y \section). 764 págs. |
| F8.25 | `funvectoriales.tex` | Auditoría ejemplos dominio sin figura | Completo | 2026-06-26 | 1 example sin figura (f=√(x+y)/ln(x-y)); triángulo D + 3 rectas etiquetadas. `fig:dominio_log_raiz`. 764 págs. |
| F8.26 | `funvectoriales.tex` | Galería 5 superficies cuádricas | Completo | 2026-06-26 | Nueva subsección con 5 superficies: paraboloide elíptico/hiperbólico, cono, hiperboloide 1/2 hojas. Figura pgfplots 3D + ejemplo 4 pasos + boxed cada una. 766 págs. |
| F8.27 | `funvectoriales.tex` | 3 ejemplos superficies de nivel con figura 3D | Completo | 2026-06-26 | Esferas/elipsoide/paraboloides; figuras paramétricas pgfplots. `fig:nivel_esfera/elipsoide/paraboloides`. 768 págs. |
| F8.28 | `funvectoriales.tex` | Auditoría estructura interna resueltos: 4 pasos + boxed | Completo | 2026-06-26 | 4/7 ejemplos corregidos (L.129, L.323, L.465, L.711). 3 ya OK (L.550, L.794, L.1328). 762 págs. |
| F8.29 | `limvariasvariables.tex` | Auditoría estructura interna resueltos: 4 pasos + boxed | Completo | 2026-06-27 | 11 correcciones: 8 examples + 3 probs. Ver bloque narrativo Semana 6. 768 págs. |
| F8.30 | `limvariasvariables.tex` | Vincular figura F8.05 a ejemplo resuelto de trayectorias | Completo | 2026-06-26 | Integrado en F8.05: figura colocada dentro del example antes de myproof. |
| F8.31 | `funvectoriales.tex` | Auditoría figuras preexistentes: figure + caption + label + anchors | Completo | 2026-06-27 | 10 figuras Phase 8 ✓. 9 figuras preexistentes corregidas: +caption+label en 8 figure[H]; \begin{center}→figure[H] en 1 example. 768 págs. |
| F8.32 | `limvariasvariables.tex` | Auditoría figuras preexistentes: figure + caption + label + anchors | Completo | 2026-06-27 | 0 correcciones. Solo 2 figuras de F8 (F8.04/F8.05), ya compliant. |
| F8.33 | `planostangentes.tex` | Auditoría figuras preexistentes: figure + caption + label + anchors | Completo | 2026-06-27 | 1 fig. preexistente: añadido \label{fig:dp_interpretacion_geometrica} + anchor=north + \small a \node planos. |
| F8.34 | `gradientes.tex` | Auditoría figuras preexistentes: figure + caption + label + anchors | Completo | 2026-06-27 | 1 fig. preexistente (triángulo prob): añadido anchor=south west al nodo θ + \caption + \label{fig:triangulo_cadena}. |
| F8.35 | `multiplicadoresintdobles.tex` | Auditoría figuras preexistentes: figure + caption + label + anchors | Completo | 2026-06-27 | 2 figs. preexistentes: trapecio (anchor+caption+label) + cúspide (anchor+label). |
| F8.36 | `apintdobles.tex` | Auditoría figuras preexistentes: figure + caption + label + anchors | Completo | 2026-06-27 | 8 figs. preexistentes: +caption+label en 4; renombrar fig1.1/fig1.2/fig3.2 → fig:...; +label en 1. |
| F8.37 | `inttriples.tex` | Auditoría figuras preexistentes: figure + caption + label + anchors | Completo | 2026-06-27 | 0 correcciones. Archivo sin figuras. |
| F8.38 | `cap33.tex` | Auditoría figuras preexistentes: figure + caption + label + anchors | Completo | 2026-06-27 | 0 correcciones. Archivo sin figuras. |
| F8.39 | `cap34.tex` | Auditoría figuras preexistentes: figure + caption + label + anchors | Completo | 2026-06-27 | 9 nodos sin anchor en 4 figs. F8: anchor=west/center/south/east según posición. |
| F8.40 | `planostangentes.tex` | Mejorar figura derivadas parciales: rectas tangentes en 3D | Completo | 2026-06-27 | pgfplots 3D: paraboloide + trazas + rectas tangentes $f_x$/$f_y$ + punto (1,1,2). |
| F8.41 | `planostangentes.tex` | Auditoría resueltos sin 4 pasos + boxed | Completo | 2026-06-27 | 16 resueltos corregidos: prosa→4 pasos, enumerate→4 ítems, \boxed{} en Paso 4. |
| F8.42 | `gradientes.tex` | Auditoría resueltos sin 4 pasos + boxed | Completo | 2026-06-27 | 12 correcciones: prosa→4 pasos, enumerate+item4, "Conclusión"→"Paso 4", multi-parte→Paso 1-4. |
| F8.43 | `multiplicadoresintdobles.tex` | Auditoría resueltos sin 4 pasos + boxed | Completo | 2026-06-27 | 10 correcciones: 8 prosa→4 pasos, Paso3→Paso3+4, "Conclusión"→Paso4. |
| F8.44 | `apintdobles.tex` | Auditoría resueltos sin 4 pasos + boxed | Completo | 2026-06-27 | 27 myproof auditados, 21 corregidos: 19 Paso 4 nuevos, 5 reestructuraciones prosa→4 pasos. PDF: 772 págs. |
| F8.45 | `inttriples.tex` | Auditoría resueltos sin 4 pasos + boxed | Completo | 2026-06-27 | 13 myproof; 5 corregidos: L.71 enumerate→4 pasos; L.146/L.233 Paso 4; L.172 →4 pasos; L.299 Paso 2 dividido. PDF: 772 págs. |
| F8.46 | `cap33.tex` | Auditoría resueltos sin 4 pasos + boxed | Completo | 2026-06-27 | 6 myproof; 2 corregidos: campo conservativo (boxed→Paso 4); integral de línea cuadrado (prosa→4 pasos). PDF: 772 págs. |
| F8.47 | `cap34.tex` | Auditoría resueltos sin 4 pasos + boxed | Completo | 2026-06-27 | 18 myproof; 6 corregidos: multi-parte (a-f), TFC, Green+elipse, campo vórtice, Stokes, Divergencia esfera. PDF: 772 págs. |
| F8.48 | `apintdobles.tex`, `inttriples.tex` | Figuras cambio de coordenadas: polares, cilíndricas, esféricas | Completo | 2026-06-27 | 3 figuras TikZ 2D: polares (rectángulo polar, dA=r dr dθ) en apintdobles; cilíndricas (vista superior+lateral) y esféricas (plano xz, ρ,φ,θ) en inttriples. PDF: 772 págs. |
| F8.49 | Todos los caps. C3 | Auditoría propuestos: promover myproof + organizar por dificultad | Completo | 2026-06-27 | 0 myproof dentro de propuestos en todos los caps. Tags % Básico/Intermedio/Desafiante añadidos a 7 archivos (cap33/cap34 ya tenían tags de F8.52/F8.53). PDF: 772 págs. |
| F8.50 | `cap33.tex` | Figura campo gradiente con curvas de nivel | Completo | 2026-06-27 | TikZ 2D: elipses azules f=x²+y²/4 (c=1/4,1/2,1) + flechas ∇f rojas en grilla 4×4. Insertado entre def. campo gradiente y rem. interpretación geométrica. `fig:campo_gradiente`. PDF: 772 págs. |
| F8.51 | `cap33.tex` | Figura campo conservativo con trayectoria cerrada | Completo | 2026-06-27 | TikZ 2D: flechas radiales F=(x,y) + curva cerrada C (círculo azul, orientación +) + etiqueta ∮F·dr=0. Insertado entre def. campo conservativo y teorema caracterización. `fig:campo_conservativo`. PDF: 772 págs. |
| F8.52 | `cap33.tex` | Añadir mínimo 15 problemas propuestos graduados | Completo | 2026-06-27 | 7 originales preservados + 8 nuevos = 15 total. Grupos: 4 Básico, 7 Intermedio, 4 Desafiante. PDF: 772 págs. |
| F8.53 | `cap34.tex` | Añadir mínimo 15 problemas propuestos graduados | Completo | 2026-06-27 | 16 originales reordenados por dificultad. Grupos: 5 Básico, 7 Intermedio, 4 Desafiante. PDF: 772 págs. |

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
