"""
escenas_campos.py -- Animaciones Manim para los videos de campos vectoriales
(Cálculo III, 2026-2). Una escena por cada \\manimframe de los decks:

  Video 1 (Green)
    V1aOrientacionBorde      Región y orientación del borde            (~26 s)
    V1bVerificacionDisco     Verificación de Green en un disco         (~24 s)
  Video 2 (superficies, flujo, divergencia)
    V2aNormalSuperficie      Vector normal sobre superficie param.     (~27 s)
    V2bParaboloideBase       Flujo: paraboloide cerrado con su base    (~27 s)
  Video 3 (Stokes)
    V3aSuperficiesBorde      La curva y las superficies que la tapan   (~25 s)

Paleta: la de estilo_presentaciones.tex (fondo lightbg, navy, tealx, brick, gold).

Render final (1080p, 30 fps), desde esta carpeta:
    python render_escenas.py            # todas
    python render_escenas.py V2aNormalSuperficie
Prueba rápida:
    manim -ql escenas_campos.py V1aOrientacionBorde
"""
import numpy as np
from manim import *

# ---------------- Paleta ----------------
NAVY = ManimColor("#1B2A4A")
TEAL = ManimColor("#1F7A6C")
BRICK = ManimColor("#A34A3E")
GOLD = ManimColor("#B8891C")
LIGHTBG = ManimColor("#F2F2EF")
GRAY60 = ManimColor("#8A8A85")

config.background_color = LIGHTBG
Text.set_default(color=NAVY, font="Segoe UI")
MathTex.set_default(color=NAVY)
Dot3D.set_default(resolution=(6, 6))
Tex.set_default(color=NAVY)


def flecha3d(a, b, color=NAVY, thickness=0.02):
    """Flecha 3D liviana: línea + cono de baja resolución.
    (Arrow3D trae ~1000 subobjetos y cuesta ~1 s por cuadro en Cairo.)"""
    a, b = np.array(a, float), np.array(b, float)
    d = b - a
    L = np.linalg.norm(d)
    u = d / L
    h = min(0.28, 0.35 * L)
    linea = Line(a, b - h * u, color=color, stroke_width=thickness * 220)
    punta = Cone(base_radius=max(0.07, 3.5 * thickness), height=h, direction=u,
                 resolution=(1, 10), fill_color=color, fill_opacity=1,
                 stroke_width=0, show_base=False).shift(b - h * u)
    return VGroup(linea, punta)


def titulo(texto):
    return Text(texto, font_size=34, weight=BOLD).to_edge(UP, buff=0.4)


# =====================================================================
# VIDEO 1
# =====================================================================
def blob(t, c=ORIGIN, k=1.0):
    r = 2.2 + 0.35 * np.sin(3 * t) + 0.2 * np.cos(2 * t + 0.5)
    return c + k * np.array([1.35 * r * np.cos(t), 0.95 * r * np.sin(t), 0])


def curva_cerrada(f, n=200, **kw):
    ts = np.linspace(0, TAU, n, endpoint=False)
    m = VMobject(**kw)
    m.set_points_smoothly([f(t) for t in ts] + [f(0)])
    return m


def flecha_en(f, s, sentido=1, largo=0.75, color=BRICK):
    """Flecha tangente a la curva f en el parámetro s."""
    p = f(s)
    d = (f(s + 1e-3) - f(s - 1e-3)) * sentido
    d = d / np.linalg.norm(d)
    return Arrow(p - 0.05 * d, p + largo * d, buff=0, color=color,
                 stroke_width=7, max_tip_length_to_length_ratio=0.45)


class V1aOrientacionBorde(Scene):
    def construct(self):
        t1 = titulo("Orientación positiva: la región queda a la izquierda")
        self.play(FadeIn(t1))

        c = DOWN * 0.4
        f = lambda t: blob(t, c, 0.95)
        borde = curva_cerrada(f, color=NAVY, stroke_width=4)
        region = borde.copy().set_fill(TEAL, 0.35).set_stroke(width=0)
        R = MathTex("R", font_size=60, color=TEAL).move_to(c)
        self.play(Create(borde), FadeIn(region), Write(R), run_time=2)

        s = ValueTracker(0)
        flecha = always_redraw(lambda: flecha_en(f, s.get_value()))
        # pequeña flecha hacia la izquierda del recorrido (hacia R)
        def izq():
            p = f(s.get_value())
            d = f(s.get_value() + 1e-3) - f(s.get_value() - 1e-3)
            d = d / np.linalg.norm(d)
            n = np.array([-d[1], d[0], 0])
            return Arrow(p, p + 0.7 * n, buff=0, color=TEAL, stroke_width=5,
                         max_tip_length_to_length_ratio=0.35)
        aizq = always_redraw(izq)
        rastro = always_redraw(lambda: ParametricFunction(
            f, t_range=[0, max(s.get_value(), 1e-3)], color=BRICK, stroke_width=6))
        self.add(rastro, flecha, aizq)
        self.play(s.animate.set_value(TAU), run_time=7, rate_func=linear)
        self.play(FadeOut(flecha), FadeOut(aizq), FadeOut(rastro))

        # --- región con agujero ---
        t2 = titulo("Con agujero: exterior antihorario, interior horario")
        g = lambda t: c + np.array([1.0 * np.cos(t) + 0.3, 0.75 * np.sin(t), 0])
        hueco_borde = curva_cerrada(g, color=NAVY, stroke_width=4)
        anillo = Cutout(borde.copy(), hueco_borde.copy()).set_fill(TEAL, 0.35).set_stroke(width=0)
        self.play(FadeTransform(t1, t2), R.animate.move_to(c + LEFT * 1.9 + DOWN * 0.2),
                  FadeOut(region), FadeIn(anillo), Create(hueco_borde), run_time=2)

        s.set_value(0)
        s2 = ValueTracker(0)
        fe = always_redraw(lambda: flecha_en(f, s.get_value()))
        re = always_redraw(lambda: ParametricFunction(
            f, t_range=[0, max(s.get_value(), 1e-3)], color=BRICK, stroke_width=6))
        # interior en sentido horario: parámetro decreciente
        gi = lambda t: g(-t)
        fi = always_redraw(lambda: flecha_en(gi, s2.get_value(), largo=0.6, color=GOLD))
        ri = always_redraw(lambda: ParametricFunction(
            gi, t_range=[0, max(s2.get_value(), 1e-3)], color=GOLD, stroke_width=6))
        self.add(re, fe, ri, fi)
        ext = Text("exterior: antihorario", font_size=26, color=BRICK).to_corner(DL, buff=0.5)
        inte = Text("interior: horario", font_size=26, color=GOLD).to_corner(DR, buff=0.5)
        self.play(FadeIn(ext), FadeIn(inte))
        self.play(s.animate.set_value(TAU), s2.animate.set_value(TAU),
                  run_time=8, rate_func=linear)
        self.wait(2)


class V1bVerificacionDisco(Scene):
    def construct(self):
        plano = NumberPlane(x_range=[-3.5, 3.5, 1], y_range=[-3.5, 3.5, 1],
                            x_length=7, y_length=7,
                            background_line_style={"stroke_color": GRAY60,
                                                   "stroke_opacity": 0.35,
                                                   "stroke_width": 1},
                            axis_config={"stroke_color": GRAY60}).shift(LEFT * 3)
        campo = ArrowVectorField(lambda p: np.array([-(p[1]), p[0] + 3, 0]) * 0.32,
                                 x_range=[-6.5, 0.5, 1], y_range=[-3.5, 3.5, 1],
                                 colors=[GRAY60], stroke_width=3)
        # (el campo se evalúa en coordenadas de pantalla; el +3 corrige el shift)
        cab = MathTex(r"\mathbf F=\langle -y,\ x\rangle", font_size=48).move_to(RIGHT * 3.6 + UP * 2.8)
        self.play(Create(plano), run_time=1)
        self.play(Create(campo), Write(cab), run_time=2)

        O = plano.c2p(0, 0)
        circ = Circle(radius=2, color=NAVY, stroke_width=5).move_to(O)
        lab_c = MathTex(r"C:\ r=2", font_size=36).next_to(circ, DR, buff=-0.1)
        self.play(Create(circ), FadeIn(lab_c))

        t = ValueTracker(0)
        punto = lambda: O + 2 * np.array([np.cos(t.get_value()), np.sin(t.get_value()), 0])
        def vec():
            a = t.get_value()
            d = np.array([-np.sin(a), np.cos(a), 0])
            return Arrow(punto(), punto() + 1.1 * d, buff=0, color=BRICK, stroke_width=7,
                         max_tip_length_to_length_ratio=0.35)
        fl = always_redraw(vec)
        arco = always_redraw(lambda: Arc(radius=2, start_angle=0,
                                         angle=max(t.get_value(), 1e-3),
                                         arc_center=O, color=BRICK, stroke_width=8))
        integ = MathTex(r"\oint_C \mathbf F\cdot d\mathbf r =", font_size=44)
        num = DecimalNumber(0, num_decimal_places=2, font_size=44, color=BRICK)
        pi = MathTex(r"\pi", font_size=44, color=BRICK)
        fila = VGroup(integ, num, pi).arrange(RIGHT, buff=0.15).move_to(RIGHT * 3.6 + UP * 1.2)
        num.add_updater(lambda m: m.set_value(4 * t.get_value() / PI))
        pi.add_updater(lambda m: m.next_to(num, RIGHT, buff=0.1))
        nota = Text("tangente: siempre a favor", font_size=24, color=BRICK).next_to(fila, DOWN, buff=0.3)
        self.add(arco, fl)
        self.play(FadeIn(fila), FadeIn(nota))
        self.play(t.animate.set_value(TAU), run_time=7, rate_func=linear)
        num.clear_updaters(); pi.clear_updaters()
        ocho = MathTex(r"\oint_C \mathbf F\cdot d\mathbf r = 8\pi", font_size=44).move_to(fila)
        ocho[0][-2:].set_color(BRICK)
        self.play(FadeOut(fl), FadeOut(nota), ReplacementTransform(fila, ocho))

        # --- interior ---
        disco = Circle(radius=2).move_to(O).set_fill(TEAL, 0.4).set_stroke(width=0)
        rot = MathTex(r"N_x-M_y = 1-(-1) = 2", font_size=40, color=TEAL).move_to(RIGHT * 3.6 + DOWN * 0.2)
        doses = VGroup(*[MathTex("2", font_size=30, color=TEAL).move_to(O + np.array([x, y, 0]))
                         for x in np.arange(-1.5, 1.6, 0.75) for y in np.arange(-1.5, 1.6, 0.75)
                         if x * x + y * y < 3.3])
        self.play(campo.animate.set_opacity(0.15), FadeIn(disco), Write(rot), LaggedStart(*[FadeIn(d) for d in doses], lag_ratio=0.05),
                  run_time=3)
        area = MathTex(r"\iint_R 2\,dA = 2\cdot 4\pi = 8\pi", font_size=44).move_to(RIGHT * 3.6 + DOWN * 1.5)
        self.play(Write(area), run_time=2)
        caja = SurroundingRectangle(VGroup(ocho, area), color=GOLD, buff=0.25)
        igual = Text("los dos lados coinciden", font_size=26, color=GOLD).next_to(caja, DOWN, buff=0.25)
        self.play(Create(caja), FadeIn(igual))
        self.wait(2)


# =====================================================================
# VIDEO 2
# =====================================================================
def z_sup(u, v):
    return 0.7 * np.sin(0.9 * u) * np.cos(0.7 * v)


def r_sup(u, v):
    return np.array([u, v, z_sup(u, v)])


def ru_sup(u, v):
    return np.array([1, 0, 0.63 * np.cos(0.9 * u) * np.cos(0.7 * v)])


def rv_sup(u, v):
    return np.array([0, 1, -0.49 * np.sin(0.9 * u) * np.sin(0.7 * v)])


class V2aNormalSuperficie(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=52 * DEGREES, theta=-55 * DEGREES, zoom=1.15)
        tit = titulo("Normal a una superficie parametrizada")
        self.add_fixed_in_frame_mobjects(tit); self.remove(tit)
        self.play(FadeIn(tit))

        sup = Surface(lambda u, v: r_sup(u, v), u_range=[-2.5, 2.5], v_range=[-2.5, 2.5],
                      resolution=(30, 30), fill_color=TEAL, fill_opacity=0.35,
                      stroke_width=0, checkerboard_colors=False)
        self.play(FadeIn(sup), run_time=1.5)

        lin_u = VGroup(*[ParametricFunction(lambda v, u=u: r_sup(u, v), t_range=[-2.5, 2.5],
                                            color=NAVY, stroke_width=2)
                         for u in np.linspace(-2.5, 2.5, 9)])
        lin_v = VGroup(*[ParametricFunction(lambda u, v=v: r_sup(u, v), t_range=[-2.5, 2.5],
                                            color=GOLD, stroke_width=2)
                         for v in np.linspace(-2.5, 2.5, 9)])
        ley_u = Text("u = cte", font_size=26, color=NAVY)
        ley_v = Text("v = cte", font_size=26, color=GOLD)
        ley = VGroup(ley_u, ley_v).arrange(DOWN, aligned_edge=LEFT).to_corner(UL, buff=0.5).shift(DOWN * 0.8)
        self.add_fixed_in_frame_mobjects(ley); self.remove(ley)
        self.play(Create(lin_u), FadeIn(ley_u), run_time=2)
        self.play(Create(lin_v), FadeIn(ley_v), run_time=2)

        u0 = ValueTracker(-0.6); v0 = ValueTracker(-0.4)
        k = 1.5
        P = lambda: r_sup(u0.get_value(), v0.get_value())
        RU = lambda: k * ru_sup(u0.get_value(), v0.get_value())
        RV = lambda: k * rv_sup(u0.get_value(), v0.get_value())
        def N():
            n = np.cross(RU(), RV())
            return 1.5 * n / np.linalg.norm(n)

        punto = always_redraw(lambda: Dot3D(P(), radius=0.07, color=NAVY))
        a_u = always_redraw(lambda: flecha3d(P(), P() + RU(), color=BRICK, thickness=0.03))
        a_v = always_redraw(lambda: flecha3d(P(), P() + RV(), color=BLUE_E, thickness=0.03))
        par = always_redraw(lambda: Polygon(P(), P() + RU(), P() + RU() + RV(), P() + RV(),
                                            stroke_color=GOLD, stroke_width=2,
                                            fill_color=GOLD, fill_opacity=0.4))
        a_n = always_redraw(lambda: flecha3d(P(), P() + N(), color=NAVY, thickness=0.025))

        l_ru = MathTex(r"\mathbf r_u", color=BRICK, font_size=40)
        l_rv = MathTex(r"\mathbf r_v", color=BLUE_E, font_size=40)
        l_n = MathTex(r"\mathbf r_u\times\mathbf r_v", color=NAVY, font_size=40)
        leyv = VGroup(l_ru, l_rv, l_n).arrange(DOWN, aligned_edge=LEFT).to_corner(UR, buff=0.5).shift(DOWN * 0.8)
        self.add_fixed_in_frame_mobjects(leyv); self.remove(leyv)

        self.play(FadeIn(punto))
        self.play(FadeIn(a_u), FadeIn(l_ru), run_time=1.2)
        self.play(FadeIn(a_v), FadeIn(l_rv), run_time=1.2)
        self.play(FadeIn(par), run_time=1.2)
        self.play(FadeIn(a_n), FadeIn(l_n), run_time=1.5)
        self.wait(1)

        # el punto se desliza y el normal lo acompaña
        self.begin_ambient_camera_rotation(rate=0.06)
        self.play(u0.animate.set_value(1.3), v0.animate.set_value(0.9), run_time=4, rate_func=smooth)
        self.play(u0.animate.set_value(-1.4), v0.animate.set_value(1.2), run_time=4, rate_func=smooth)
        self.play(u0.animate.set_value(0.2), v0.animate.set_value(-1.3), run_time=4, rate_func=smooth)
        self.stop_ambient_camera_rotation()
        self.wait(1.5)


class V2bParaboloideBase(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=68 * DEGREES, theta=-50 * DEGREES, zoom=0.82)
        ejes = ThreeDAxes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-1.5, 5, 1],
                          x_length=6, y_length=6, z_length=6.5,
                          axis_config={"color": GRAY60, "include_ticks": False}).shift(IN * 1.5)
        c = ejes.c2p
        tit = titulo("Problema 38: el domo con su base")
        cab = MathTex(r"\mathbf F=\langle x,y,z\rangle", font_size=40).to_corner(UL, buff=0.5).shift(DOWN * 0.8)
        self.add_fixed_in_frame_mobjects(tit, cab); self.remove(tit, cab)
        self.play(FadeIn(tit), Create(ejes))

        domo = Surface(lambda r, th: c(r * np.cos(th), r * np.sin(th), 4 - r * r),
                       u_range=[0, 2], v_range=[0, TAU], resolution=(10, 24),
                       fill_color=TEAL, fill_opacity=0.35, stroke_color=TEAL,
                       stroke_width=0.5, checkerboard_colors=False)
        base = Surface(lambda r, th: c(r * np.cos(th), r * np.sin(th), 0),
                       u_range=[0, 2], v_range=[0, TAU], resolution=(3, 24),
                       fill_color=GOLD, fill_opacity=0.35, stroke_color=GOLD,
                       stroke_width=0.5, checkerboard_colors=False)
        l_domo = MathTex(r"z=4-x^2-y^2", font_size=36, color=TEAL)
        l_base = MathTex(r"x^2+y^2\le 4,\ z=0", font_size=36, color=GOLD)
        lab = VGroup(l_domo, l_base).arrange(DOWN, aligned_edge=LEFT).next_to(cab, DOWN, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(lab); self.remove(lab)
        self.play(FadeIn(domo), FadeIn(l_domo), run_time=1.5)
        self.play(FadeIn(base), FadeIn(l_base), FadeIn(cab), run_time=1.5)

        def flecha(p, v, color, esc=0.33):
            return flecha3d(c(*p), c(*(np.array(p) + esc * np.array(v))), color=color, thickness=0.015)

        # campo en el domo: sale
        pts_d = [(0, 0, 4)] + [(r * np.cos(t), r * np.sin(t), 4 - r * r)
                                for r in (1.0, 1.75) for t in np.linspace(0, TAU, 6, endpoint=False) + (0.5 if r > 1.5 else 0)]
        f_domo = VGroup(*[flecha(p, p, NAVY) for p in pts_d])
        txt1 = Text("por el domo, el campo sale", font_size=26, color=NAVY).to_corner(DR, buff=0.5)
        self.add_fixed_in_frame_mobjects(txt1); self.remove(txt1)
        self.begin_ambient_camera_rotation(rate=0.08)
        self.play(LaggedStart(*[FadeIn(a) for a in f_domo], lag_ratio=0.05), FadeIn(txt1), run_time=3)
        self.wait(1.5)

        # campo en la base: horizontal
        pts_b = [(r * np.cos(t), r * np.sin(t), 0) for r in (0.8, 1.6)
                 for t in np.linspace(0, TAU, 6, endpoint=False) + (0.5 if r > 1 else 0)]
        f_base = VGroup(*[flecha(p, p, BRICK, esc=0.5) for p in pts_b])
        txt2 = Text("en la base, horizontal: no la cruza", font_size=26, color=BRICK).to_corner(DR, buff=0.5)
        self.add_fixed_in_frame_mobjects(txt2); self.remove(txt2)
        self.play(LaggedStart(*[FadeIn(a) for a in f_base], lag_ratio=0.05),
                  FadeOut(txt1), FadeIn(txt2), run_time=3)
        self.wait(1.5)

        # normales exteriores
        self.play(*[FadeOut(a) for a in [*f_domo, *f_base]], run_time=0.8)
        nd = []
        for (x, y, z) in [(0, 0, 4), (1.2, 0, 4 - 1.44), (-0.6, 1.0, 4 - 1.36), (0.3, -1.4, 4 - 2.05)]:
            n = np.array([2 * x, 2 * y, 1.0]); n /= np.linalg.norm(n)
            nd.append(flecha((x, y, z), n, GOLD, esc=1.0))
        nb = [flecha((x, y, 0), (0, 0, -1), GOLD, esc=1.0) for (x, y) in [(0, 0), (1.1, 0.4), (-0.8, -0.9)]]
        txt3 = Text("normales exteriores: arriba en el domo, abajo en la base",
                    font_size=26, color=GOLD).to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(txt3); self.remove(txt3)
        self.play(FadeOut(txt2), FadeIn(txt3),
                  LaggedStart(*[FadeIn(a) for a in nd + nb], lag_ratio=0.15), run_time=3)
        self.wait(6)
        self.stop_ambient_camera_rotation()


# =====================================================================
# VIDEO 3
# =====================================================================
A_TW = 0.7


def curva_C(t):
    return np.array([2 * np.cos(t), 2 * np.sin(t), A_TW * np.sin(2 * t)])


def sup_tapa(h):
    return lambda s, t: np.array([2 * s * np.cos(t), 2 * s * np.sin(t),
                                  A_TW * s * s * np.sin(2 * t) + h * (1 - s * s)])


def normal_num(f, s, t, e=1e-4):
    rs = (f(s + e, t) - f(s - e, t)) / (2 * e)
    rt = (f(s, t + e) - f(s, t - e)) / (2 * e)
    n = np.cross(rs, rt)
    return n / np.linalg.norm(n)


class V3aSuperficiesBorde(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=64 * DEGREES, theta=-50 * DEGREES, zoom=1.35)
        tit = titulo("Muchas superficies, un mismo borde")
        self.add_fixed_in_frame_mobjects(tit); self.remove(tit)
        self.play(FadeIn(tit))

        C = ParametricFunction(curva_C, t_range=[0, TAU], color=BRICK, stroke_width=6)
        self.play(Create(C), run_time=2)
        s = ValueTracker(0)
        def fl():
            a = s.get_value()
            p = curva_C(a)
            d = curva_C(a + 1e-3) - curva_C(a - 1e-3); d /= np.linalg.norm(d)
            return flecha3d(p, p + 0.8 * d, color=BRICK, thickness=0.03)
        f = always_redraw(fl)
        lC = MathTex("C", color=BRICK, font_size=48).to_corner(UL, buff=0.5).shift(DOWN * 0.8)
        self.add_fixed_in_frame_mobjects(lC); self.remove(lC)
        self.add(f)
        self.play(FadeIn(lC), s.animate.set_value(TAU), run_time=4, rate_func=linear)
        self.remove(f)
        # dejar una flecha fija de orientación
        self.add(flecha3d(curva_C(0.6), curva_C(0.6) + 0.8 * np.array([-np.sin(.6), np.cos(.6), 0.5]),
                         color=BRICK, thickness=0.03))

        formula = MathTex(r"\iint_S (\nabla\times\mathbf F)\cdot\mathbf n\,dS", r"=",
                          r"\oint_C \mathbf F\cdot d\mathbf r", font_size=38).to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(formula); self.remove(formula)
        self.play(FadeIn(formula))

        nombres = ["disco deformado", "casquete", "bolsa"]
        alturas = [0.0, 1.8, -1.8]
        colores = [TEAL, GOLD, BLUE_E]
        sup_prev = norm_prev = nom_prev = None
        self.begin_ambient_camera_rotation(rate=0.07)
        for nombre, h, col in zip(nombres, alturas, colores):
            g = sup_tapa(h)
            sup = Surface(g, u_range=[0, 1], v_range=[0, TAU], resolution=(14, 40),
                          fill_color=col, fill_opacity=0.4, stroke_color=col,
                          stroke_width=0.4, checkerboard_colors=False)
            normales = VGroup(*[flecha3d(g(ss, tt), g(ss, tt) + 1.0 * normal_num(g, ss, tt),
                                        color=NAVY, thickness=0.02)
                                for ss, tt in [(1e-3, 0.0), (0.6, 0.8), (0.6, 3.3), (0.6, 4.9)]])
            nom = Text(nombre, font_size=30, color=col).to_corner(UR, buff=0.5).shift(DOWN * 0.8)
            self.add_fixed_in_frame_mobjects(nom); self.remove(nom)
            if sup_prev is None:
                self.play(FadeIn(sup), FadeIn(nom), run_time=1.5)
            else:
                self.play(FadeOut(norm_prev), FadeOut(nom_prev), run_time=0.6)
                self.play(ReplacementTransform(sup_prev, sup), FadeIn(nom), run_time=1.6)
            self.play(LaggedStart(*[FadeIn(n) for n in normales], lag_ratio=0.2), run_time=1.5)
            self.wait(1.5)
            sup_prev, norm_prev, nom_prev = sup, normales, nom

        mismo = Text("mismo valor para todas", font_size=30, color=NAVY)
        self.add_fixed_in_frame_mobjects(mismo); self.remove(mismo)
        self.play(formula.animate.shift(LEFT * 1.6), run_time=0.8)
        mismo.next_to(formula, RIGHT, buff=0.6)
        caja = SurroundingRectangle(formula, color=GOLD, buff=0.15)
        self.add_fixed_in_frame_mobjects(caja); self.remove(caja)
        self.play(FadeIn(mismo), Create(caja))
        self.wait(3)
        self.stop_ambient_camera_rotation()
