"""
Ejemplo: plano tangente a z = x^2 y^3 en (1, 2)  (planostangentes.tex).

    manim -pql ejemplo_plano_tangente.py PlanoTangente      # borrador rápido
    manim -pqh ejemplo_plano_tangente.py PlanoTangente      # final 1080p
"""

from plantilla import *


class PlanoTangente(EscenaProblema):
    numero = "?"  # TODO: número del problema en el PDF
    tema = "Plano tangente"

    def construct(self):
        self.portada()
        self.enunciado(r"Calcule el plano tangente a la superficie $z = x^2y^3$ en el punto $(1,2)$.")

        _, (fx_fy,) = self.paso(
            "Paso 1. Derivadas parciales",
            r"f_x = 2xy^3,\qquad f_y = 3x^2y^2",
        )

        # En vertical, las líneas largas se parten en varias.
        if VERTICAL:
            valores = [r"f(1,2)=8", r"f_x(1,2)=16", r"f_y(1,2)=12"]
        else:
            valores = [r"f(1,2)=8,\quad f_x(1,2)=16,\quad f_y(1,2)=12"]
        _, lineas = self.paso("Paso 2. Evaluar en (1, 2)", *valores, run_time=0.8)
        self.resaltar(VGroup(*lineas))

        _, (plano,) = self.paso(
            "Paso 3. Ecuación del plano",
            r"z - 8 = 16(x-1) + 12(y-2)",
        )

        self.respuesta(r"z = 16x + 12y - 32")
        self.cierre()
