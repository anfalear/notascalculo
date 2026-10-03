# Videos de soluciones con Manim

Idea: tomar problemas del problemario que ya tienen solución, animarlos con
Manim y subirlos a YouTube en dos formatos:

| Formato | Duración | Contenido |
|---|---|---|
| Video normal (horizontal 16:9) | 5–12 min | El problema completo, de principio a fin |
| Short / Reel (vertical 9:16) | 30–90 s | Solo el momento más visual de la solución, remitiendo al video largo |

Por cada problema: **un video largo + un short** sacado de su escena más visual.

## Archivos

- `plantilla.py`: configuración común (formato, colores, macros LaTeX, zona segura) y la clase `EscenaProblema`.
- `ejemplo_plano_tangente.py`: escena de prueba (plano tangente a z = x²y³ en (1,2), `planostangentes.tex`).
- `media/horizontal/`, `media/vertical/`: renders (no van al repo).

## Cómo renderizar

Desde `videos/`, en PowerShell:

```powershell
# borrador rápido (480p)
manim -pql ejemplo_plano_tangente.py PlanoTangente

# final horizontal (1080p)
manim -pqh ejemplo_plano_tangente.py PlanoTangente

# final vertical (1080x1920)
$env:FORMATO="vertical"; manim -pqh ejemplo_plano_tangente.py PlanoTangente; Remove-Item Env:FORMATO
```

- La orientación sale de la variable `FORMATO`; la calidad, de `-ql/-qm/-qh/-qk`.
- No usar `-r`: la plantilla lo sobrescribe.
- Marco lógico: 16×9 unidades en horizontal, 9×16 en vertical.
- La carpeta de salida lleva la altura en píxeles: en vertical `-ql` sale en `media/vertical/videos/.../854p30/`.
- Para revisar el encuadre sin ver todo el video: `manim -ql -s ...` guarda solo el último cuadro como PNG.
- Probado con Manim 0.21.0 + MiKTeX (latex + dvisvgm). En esta máquina Manim **no** está instalado en el Python global: `pip install manim` (o en un venv).

## Cómo hacer un video nuevo

```python
from plantilla import *

class MiProblema(EscenaProblema):
    numero = "19.23"
    tema = "Derivada direccional"

    def construct(self):
        self.portada()
        self.enunciado(r"Texto con $matemáticas$ ...")
        _, (linea,) = self.paso("Paso 1. ...", r"f_x = ...")
        self.resaltar(linea)          # o una parte: linea[0][3:7]
        self.paso("Paso 2. ...", r"...", r"...")   # varias líneas
        self.respuesta(r"\text{resultado}")
        self.cierre()
```

Métodos de `EscenaProblema`:

| Método | Qué hace |
|---|---|
| `portada()` | "Problema N" + tema |
| `enunciado(tex)` | Caja fija arriba (Tex: texto con `$...$`); corta líneas solo |
| `paso(titulo, *mathtex)` | Bloque nuevo debajo; si no cabe, los pasos viejos se van y el resto sube |
| `resaltar(mob)` | Recuadro amarillo momentáneo |
| `respuesta(mathtex)` | Resultado enmarcado en verde |
| `limpiar_pasos()` | Borra los pasos y deja el enunciado |
| `cierre()` | Remite al problemario y al canal |

Funciones sueltas: `parrafo(tex, ancho)` (Tex con corte de línea) y
`ajustar_ancho(mob)` (encoge si no cabe). La constante `VERTICAL` permite
adaptar una escena al formato, p. ej. partir una ecuación larga en varias
líneas solo en vertical (ver el Paso 2 del ejemplo).

Para gráficas o 3D se puede mezclar libremente: la escena es una `Scene`
normal (para 3D habrá que hacer una variante sobre `ThreeDScene`, pendiente).

## Convenciones de estilo

- Colores: fondo `#14161c`, acento azul (títulos de paso), amarillo (lo que se explica), verde (respuesta).
- Macros LaTeX iguales a las del libro: `\R \N \Z \Q \abs \norm`. Si un problema usa otro macro, agregarlo a `PLANTILLA_TEX`.
- Estructura fija: enunciado → idea clave → desarrollo → respuesta.
- Título y descripción de YouTube con el número del problema ("Problema 19.23").

**Vertical:**
- Componer hacia abajo, ecuaciones largas en varias líneas.
- La plantilla ya deja libre ~15 % abajo y ~12 % a la derecha (interfaz de YouTube/Instagram).
- Letra grande: la plantilla sube los tamaños automáticamente.

## Pendientes antes de publicar

- [ ] **Atribución (F10.02):** verificar que los enunciados elegidos no vengan de libros publicados, o reformularlos.
- [ ] Poner el nombre del canal en `CANAL` (`plantilla.py`).
- [ ] Poner el número real del problema de ejemplo (`numero = "?"`).
- [ ] Elegir 10–15 candidatos. Prioridad: geometría 3D (planos tangentes, regiones de integración, cambios de coordenadas), campos vectoriales (flujo, Green, Stokes), álgebra lineal (transformaciones, vectores propios), gradiente con curvas de nivel. Evitar los de pura manipulación algebraica.
- [ ] Variante 3D de `EscenaProblema` (`ThreeDScene`), para el plano tangente con la superficie.
- [ ] Hacer el primer video completo (horizontal + short) antes de planear la serie entera.

## Bitácora

- 2026-10-02: plantilla y ejemplo creados. Renderizados y revisados cuadro a cuadro en ambos formatos (encuadre, corte del enunciado, scroll de pasos con 7 pasos). Nada commiteado todavía.
