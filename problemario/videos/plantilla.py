"""
Plantilla común para los videos de soluciones del problemario.

Uso (desde la carpeta videos/):

    # horizontal (por defecto)
    manim -pqh ejemplo_plano_tangente.py PlanoTangente

    # vertical (Shorts / Reels), en PowerShell:
    $env:FORMATO="vertical"; manim -pqh ejemplo_plano_tangente.py PlanoTangente; Remove-Item Env:FORMATO

El formato se lee de la variable de entorno FORMATO al importar este
módulo. La calidad (-ql, -qh, ...) se respeta; solo se gira la
orientación. No usar `-r`: este módulo lo sobrescribe.
"""

import os

from manim import *

# ---------------------------------------------------------------------------
# Formato
# ---------------------------------------------------------------------------

FORMATO = os.environ.get("FORMATO", "horizontal").lower()
VERTICAL = FORMATO == "vertical"

# Se respeta la calidad pedida con -ql / -qm / -qh / -qk y solo se gira
# la orientación de los píxeles.
_lado_mayor = max(config.pixel_width, config.pixel_height)
_lado_menor = min(config.pixel_width, config.pixel_height)
if VERTICAL:
    config.pixel_width, config.pixel_height = _lado_menor, _lado_mayor
    config.frame_width, config.frame_height = 9, 16
else:
    config.pixel_width, config.pixel_height = _lado_mayor, _lado_menor
    config.frame_width, config.frame_height = 16, 9

config.frame_rate = 30
# Separar los renders por formato para que uno no pise al otro.
config.media_dir = os.path.join("media", FORMATO)

# ---------------------------------------------------------------------------
# Estilo
# ---------------------------------------------------------------------------

CANAL = "@tu_canal"  # TODO: poner el nombre del canal

COLOR_FONDO = "#14161c"
COLOR_TEXTO = "#e8e6e3"
COLOR_TENUE = "#8a8f98"
ACENTO = "#5fb3f9"      # títulos de paso, elementos principales
DESTACADO = "#f5c451"   # lo que se está explicando en este momento
RESPUESTA = "#7ee08a"   # resultado final

config.background_color = COLOR_FONDO

TAM_TITULO = 56 if VERTICAL else 52
TAM_TEXTO = 40 if VERTICAL else 36
TAM_MATE = 46 if VERTICAL else 42

# Zona segura: lo que no tapa la interfaz de YouTube / Instagram.
# En vertical se reserva ~15 % abajo (título, botones) y ~12 % a la
# derecha (likes, comentarios).
_W, _H = config.frame_width, config.frame_height
if VERTICAL:
    MARGEN_SUP, MARGEN_INF = 1.4, 0.15 * _H
    MARGEN_IZQ, MARGEN_DER = 0.45, 0.12 * _W
else:
    MARGEN_SUP, MARGEN_INF = 0.5, 0.5
    MARGEN_IZQ, MARGEN_DER = 0.7, 0.7

ZONA_SUP = _H / 2 - MARGEN_SUP
ZONA_INF = -_H / 2 + MARGEN_INF
ZONA_IZQ = -_W / 2 + MARGEN_IZQ
ZONA_DER = _W / 2 - MARGEN_DER
ZONA_ANCHO = ZONA_DER - ZONA_IZQ
ZONA_CENTRO_X = (ZONA_IZQ + ZONA_DER) / 2
SANGRIA = 0.3 if VERTICAL else 0.5  # sangría de las ecuaciones bajo cada paso

# ---------------------------------------------------------------------------
# LaTeX: mismos macros que el problemario
# ---------------------------------------------------------------------------

PLANTILLA_TEX = TexTemplate()
PLANTILLA_TEX.add_to_preamble(r"""
\usepackage{amsmath,amssymb}
\newcommand{\N}{{\mathbb N}}
\newcommand{\Z}{{\mathbb Z}}
\newcommand{\Q}{{\mathbb Q}}
\newcommand{\R}{{\mathbb R}}
\newcommand{\abs}[1]{\left\vert#1\right\vert}
\newcommand{\norm}[1]{\left\Vert#1\right\Vert}
""")

Tex.set_default(tex_template=PLANTILLA_TEX, color=COLOR_TEXTO, font_size=TAM_TEXTO)
MathTex.set_default(tex_template=PLANTILLA_TEX, color=COLOR_TEXTO, font_size=TAM_MATE)
Text.set_default(color=COLOR_TEXTO)


_PT_POR_TAM = {}


def _unidades_por_pt(font_size):
    """Cuántas unidades de Manim mide 1 pt de LaTeX a este tamaño de letra."""
    if font_size not in _PT_POR_TAM:
        regla = Tex(r"\rule{100pt}{1pt}", font_size=font_size)
        _PT_POR_TAM[font_size] = regla.width / 100
    return _PT_POR_TAM[font_size]


def parrafo(tex, ancho=None, font_size=None, **kwargs):
    """Tex con cortes de línea automáticos para que quepa en `ancho`."""
    ancho = ancho or ZONA_ANCHO
    font_size = font_size or TAM_TEXTO
    pts = ancho / _unidades_por_pt(font_size)
    return Tex(
        rf"\begin{{minipage}}{{{pts:.1f}pt}}\raggedright {tex}\end{{minipage}}",
        font_size=font_size, **kwargs,
    )


def ajustar_ancho(mob, ancho=None):
    """Reduce `mob` si no cabe en el ancho de la zona segura."""
    ancho = ancho or ZONA_ANCHO
    if mob.width > ancho:
        mob.scale_to_fit_width(ancho)
    return mob


# ---------------------------------------------------------------------------
# Escena base
# ---------------------------------------------------------------------------

class EscenaProblema(Scene):
    """
    Escena base: portada -> enunciado -> pasos -> respuesta -> cierre.

    Subclases definen `numero`, `tema` y escriben `construct` usando
    los métodos de abajo. Los pasos se apilan hacia abajo; cuando ya no
    caben, los más viejos se desvanecen y el resto sube.
    """

    numero = "?"
    tema = ""
    separacion = 0.45  # espacio vertical entre bloques

    def setup(self):
        self._enunciado = None
        self._pasos = []

    # -- piezas ------------------------------------------------------------

    def portada(self, espera=1.5):
        num = Text(f"Problema {self.numero}", font_size=TAM_TITULO, weight=BOLD, color=ACENTO)
        tema = Text(self.tema, font_size=TAM_TEXTO, color=COLOR_TENUE)
        grupo = VGroup(num, tema).arrange(DOWN, buff=0.35)
        ajustar_ancho(grupo).move_to([ZONA_CENTRO_X, 0, 0])
        self.play(FadeIn(num, shift=UP * 0.3), run_time=0.8)
        self.play(FadeIn(tema), run_time=0.6)
        self.wait(espera)
        self.play(FadeOut(grupo), run_time=0.5)

    def enunciado(self, tex, espera=2.0):
        """Muestra el enunciado arriba, en una caja; queda fijo."""
        texto = parrafo(tex, ZONA_ANCHO - 0.6)
        caja = SurroundingRectangle(texto, color=COLOR_TENUE, buff=0.25, corner_radius=0.1)
        grupo = VGroup(caja, texto)
        grupo.move_to([ZONA_CENTRO_X, 0, 0]).to_edge(UP, buff=MARGEN_SUP)
        self.play(Create(caja), Write(texto), run_time=1.5)
        self.wait(espera)
        self._enunciado = grupo
        return grupo

    def paso(self, titulo, *expresiones, espera=1.0, run_time=1.2):
        """
        Agrega un paso: un título corto y una o más líneas de MathTex.
        Devuelve (titulo, [lineas]) para poder resaltar partes después.
        """
        cab = Text(titulo, font_size=TAM_TEXTO, color=ACENTO, weight=BOLD)
        lineas = [ajustar_ancho(MathTex(e), ZONA_ANCHO - SANGRIA) for e in expresiones]
        bloque = VGroup(cab, *lineas).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        for l in lineas:
            l.shift(RIGHT * SANGRIA)
        self._colocar(bloque)

        self.play(FadeIn(cab, shift=RIGHT * 0.2), run_time=0.5)
        for l in lineas:
            self.play(Write(l), run_time=run_time)
        self.wait(espera)
        self._pasos.append(bloque)
        return cab, lineas

    def respuesta(self, expresion, espera=2.5):
        """Resultado final, enmarcado en el color de respuesta."""
        mat = ajustar_ancho(MathTex(expresion, color=RESPUESTA, font_size=TAM_MATE * 1.15), ZONA_ANCHO - 0.6)
        caja = SurroundingRectangle(mat, color=RESPUESTA, buff=0.25, corner_radius=0.1)
        bloque = VGroup(caja, mat)
        self._colocar(bloque)
        self.play(Write(mat), run_time=1.2)
        self.play(Create(caja), run_time=0.6)
        self.wait(espera)
        self._pasos.append(bloque)
        return bloque

    def cierre(self, espera=2.5):
        """Limpia la pantalla y remite al problemario y al canal."""
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
        linea1 = Text("Solución completa en el problemario", font_size=TAM_TEXTO)
        linea2 = Text(f"Problema {self.numero}", font_size=TAM_TEXTO, color=ACENTO)
        linea3 = Text(CANAL, font_size=TAM_TEXTO * 0.8, color=COLOR_TENUE)
        grupo = VGroup(linea1, linea2, linea3).arrange(DOWN, buff=0.35)
        ajustar_ancho(grupo).move_to([ZONA_CENTRO_X, 0, 0])
        self.play(FadeIn(grupo, shift=UP * 0.2))
        self.wait(espera)

    def resaltar(self, mob, color=DESTACADO):
        """Encierra `mob` (una línea o una parte de ella) un momento."""
        caja = SurroundingRectangle(mob, color=color, buff=0.08)
        self.play(Create(caja), run_time=0.5)
        self.wait(0.6)
        self.play(FadeOut(caja), run_time=0.4)

    def limpiar_pasos(self):
        """Borra todos los pasos (deja el enunciado)."""
        if self._pasos:
            self.play(*[FadeOut(p) for p in self._pasos], run_time=0.6)
        self._pasos = []

    # -- colocación --------------------------------------------------------

    def _tope(self):
        """Altura desde la que empiezan los pasos."""
        if self._enunciado is not None:
            return self._enunciado.get_bottom()[1] - self.separacion
        return ZONA_SUP

    def _apilar(self, mobs):
        """Centros de `mobs` apilados hacia abajo desde el tope, a la izquierda."""
        y = self._tope()
        centros = []
        for m in mobs:
            centros.append(np.array([ZONA_IZQ + m.width / 2, y - m.height / 2, 0]))
            y -= m.height + self.separacion
        return centros

    def _colocar(self, bloque):
        """Pone `bloque` debajo del último paso; si no cabe, hace scroll."""
        pila = self._pasos + [bloque]
        salen = []
        centros = self._apilar(pila)
        while len(pila) > 1 and centros[-1][1] - bloque.height / 2 < ZONA_INF:
            salen.append(pila.pop(0))
            centros = self._apilar(pila)

        bloque.move_to(centros[-1])
        self._pasos = pila[:-1]
        if salen:
            self.play(
                *[FadeOut(m) for m in salen],
                *[m.animate.move_to(c) for m, c in zip(pila[:-1], centros[:-1])],
                run_time=0.7,
            )
