"""
montar_video.py -- Arma el video a partir de las diapositivas (PDF de beamer) y
las tomas de voz (una por bloque del guion) en ./audio/.

    python montar_video.py 1            # video 1 con las tomas que haya
    python montar_video.py 1 --hasta 4  # solo los bloques 1-4

Correspondencia: el bloque k del guion (k-ésimo \\narracion del .tex) es el
frame k del PDF (etiqueta de página k); sus páginas son los revelados (\\pause).
Toma de voz: audio/videoN_voz_<nombre>_k.m4a.

Cuándo se revela cada \\pause dentro de un bloque: en la frase de PISTAS (la
posición de esa frase en el texto, en proporción a las palabras, se ajusta a la
pausa de la voz más cercana). Sin pista: reparto en partes iguales.

Las páginas "▶ Animación Manim" se reemplazan por el mp4 de animaciones/ que
indique ANIMACIONES (ver abajo).

Salida: borradores/videoN_borrador.mp4 (1920x1080, 30 fps, H.264 + AAC).
"""
import argparse, re, sys
from fractions import Fraction
from pathlib import Path

import av
import fitz
import numpy as np

AQUI = Path(__file__).resolve().parent
VIDEOS = {1: ("video_1_green", "green"),
          2: ("video_2_superficie_flujo_divergencia", "superficie_flujo_divergencia"),
          3: ("video_3_stokes", "stokes")}

# (video, bloque) -> frase donde aparece cada revelado (desde el segundo)
PISTAS = {
    (1, 2): ["Green es exactamente", "Esta idea, frontera contra interior"],
    (1, 4): ["Por eso la forma vectorial"],
    (1, 5): ["Si dentro de la región hay un punto"],
    (1, 7): ["Sobre un cuadrito", "Al sumar todos los cuadritos"],
    (1, 9): ["En el interior, M es", "Ahora el borde", "Los dos lados coinciden"],
    (1, 10): ["Un campo que sirve", "Así obtenemos la fórmula", "Es el principio de un aparato"],
    (1, 11): ["Al formar x d y", "Integrando a b"],
    (1, 12): ["Como sabemos el borde"],
    (1, 13): ["Al formar x d y", "Queda x uno delta y", "Cada lado aporta"],
    (1, 14): ["La suma es tres mil"],
    (1, 15): ["da otra vez mil"],
    (1, 16): ["El segundo es el dominio"],
}

# (video, bloque) -> mp4 de animaciones/ que reemplaza la página "▶ Animación Manim".
# Arranca al entrar el bloque; si es más larga que la voz se alarga el silencio
# siguiente para no cortarla; si es más corta se congela su último cuadro.
ANIMACIONES = {
    (1, 6): "video1_A_orientacion_borde.mp4",
    (1, 8): "video1_B_verificacion_disco.mp4",
}

ANCHO, ALTO, FPS, SR = 1920, 1080, 30, 48000
INICIO, ENTRE, FINAL = 0.5, 0.6, 1.5   # silencios añadidos (s)


def narraciones(tex):
    """Textos de los \\narracion[...]{...}, en orden (llaves balanceadas)."""
    s = tex.read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r"\\narracion(\[[^\]]*\])?\{", s):
        i, prof = m.end(), 1
        while prof:
            prof += {"{": 1, "}": -1}.get(s[i], 0)
            i += 1
        out.append(s[m.end():i - 1])
    return out


def frames_pdf(pdf):
    """Lista de listas de índices de página, una por frame (por etiqueta)."""
    grupos, ultima = [], None
    for i, p in enumerate(pdf):
        lab = p.get_label()
        if lab.startswith("<FEFF"):
            lab = bytes.fromhex(lab[1:-1]).decode("utf-16-be")
        if lab != ultima:
            grupos.append([])
            ultima = lab
        grupos[-1].append(i)
    return grupos


def leer_audio(f):
    c = av.open(str(f))
    r = av.AudioResampler(format="fltp", layout="stereo", rate=SR)
    partes = [o.to_ndarray() for fr in c.decode(c.streams.audio[0]) for o in r.resample(fr)]
    partes += [o.to_ndarray() for o in r.resample(None)]
    c.close()
    return np.concatenate(partes, axis=1).astype(np.float32)


def silencios(x, min_s=0.3):
    """Centros (s) de los silencios de al menos min_s."""
    mono = x.mean(axis=0)
    w = SR // 100
    rms = np.sqrt(np.mean(mono[: len(mono) // w * w].reshape(-1, w) ** 2, axis=1))
    db = 20 * np.log10(rms + 1e-9)
    sil = db < np.percentile(db, 95) - 30
    centros, i = [], 0
    while i < len(sil):
        if sil[i]:
            j = i
            while j < len(sil) and sil[j]:
                j += 1
            if j - i >= min_s * 100:
                centros.append((i + j) / 200)
            i = j
        else:
            i += 1
    return centros


def tiempos_revelado(texto, pistas, n, dur, sils):
    """Instantes (s, relativos a la toma) en que aparecen los revelados 2..n."""
    if n <= 1:
        return []
    palabras = texto.split()
    if pistas and len(pistas) == n - 1:
        fr = []
        for p in pistas:
            k = texto.find(p)
            if k < 0:
                sys.exit(f"Pista no encontrada en el guion: {p!r}")
            fr.append(len(texto[:k].split()) / len(palabras))
    else:
        fr = [k / n for k in range(1, n)]
    out = []
    for f in fr:
        t = f * dur
        cerca = [s for s in sils if abs(s - t) <= 3.0]
        out.append(min(cerca, key=lambda s: abs(s - t)) if cerca else t)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video", type=int, choices=VIDEOS)
    ap.add_argument("--hasta", type=int, default=None)
    a = ap.parse_args()

    base, nombre = VIDEOS[a.video]
    textos = narraciones(AQUI / f"{base}.tex")
    pdf = fitz.open(AQUI / f"{base}.pdf")
    frames = frames_pdf(pdf)
    if len(frames) != len(textos):
        sys.exit(f"El PDF tiene {len(frames)} frames y el .tex {len(textos)} narraciones")

    tomas = {}
    for f in (AQUI / "audio").glob(f"video{a.video}_voz_{nombre}_*.m4a"):
        tomas[int(f.stem.rsplit("_", 1)[1])] = f
    ultimo = a.hasta or len(textos)
    faltan = [k for k in range(1, ultimo + 1) if k not in tomas]
    if faltan:
        sys.exit(f"Faltan las tomas de los bloques {faltan}")

    # Línea de tiempo: audio total + lista (inicio_s, página)
    pistas_audio, cambios, t = [np.zeros((2, int(INICIO * SR)), np.float32)], [], INICIO
    for k in range(1, ultimo + 1):
        x = leer_audio(tomas[k])
        dur = x.shape[1] / SR
        pags = frames[k - 1]
        rev = tiempos_revelado(textos[k - 1], PISTAS.get((a.video, k)), len(pags), dur, silencios(x))
        inicio_pag = (t - (INICIO if k == 1 else ENTRE / 2)) if k > 1 else 0.0
        anim = ANIMACIONES.get((a.video, k))
        if anim:
            anim = AQUI / "animaciones" / anim
            if not anim.exists():
                sys.exit(f"Falta la animación {anim.name}")
        cambios.append((inicio_pag, pags[0], anim))
        for r, p in zip(rev, pags[1:]):
            cambios.append((t + r, p, None))
        print(f"bloque {k:2d}  {t:6.1f}s  dur {dur:5.1f}s  páginas {[p + 1 for p in pags]}"
              f"  revelados en {[round(t + r, 1) for r in rev]}"
              + (f"  animación {anim.name}" if anim else ""))
        pistas_audio.append(x)
        t += dur
        sep = ENTRE if k < ultimo else FINAL
        if anim:
            c = av.open(str(anim))
            d_anim = c.duration / 1e6
            c.close()
            fin_pag = t + sep - (ENTRE / 2 if k < ultimo else 0)
            falta = inicio_pag + d_anim + 0.3 - fin_pag
            if falta > 0:
                sep += falta
                print(f"          animación {d_anim:.1f}s: +{falta:.1f}s de silencio")
        pistas_audio.append(np.zeros((2, int(sep * SR)), np.float32))
        t += sep
    audio = np.concatenate(pistas_audio, axis=1)
    total = audio.shape[1] / SR

    # Imágenes de las páginas usadas
    zoom = ANCHO / pdf[0].rect.width
    imgs = {}
    for _, p, an in cambios:
        if p not in imgs and not an:
            pm = pdf[p].get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
            arr = np.frombuffer(pm.samples, np.uint8).reshape(pm.height, pm.width, 3)
            lienzo = np.zeros((ALTO, ANCHO, 3), np.uint8)
            h, w = min(ALTO, arr.shape[0]), min(ANCHO, arr.shape[1])
            lienzo[:h, :w] = arr[:h, :w]
            imgs[p] = lienzo

    salida = AQUI / "borradores" / (f"video{a.video}_borrador"
                                    + (f"_bloques1-{ultimo}" if a.hasta else "") + ".mp4")
    salida.parent.mkdir(exist_ok=True)
    out = av.open(str(salida), "w")
    vs = out.add_stream("libx264", rate=FPS)
    vs.width, vs.height, vs.pix_fmt = ANCHO, ALTO, "yuv420p"
    vs.options = {"crf": "20", "preset": "medium", "tune": "stillimage"}
    as_ = out.add_stream("aac", rate=SR)
    as_.layout = "stereo"

    nfr = int(np.ceil(total * FPS))
    j, cache = 0, {}
    seg, cont, it, leidos, cuadro = None, None, None, 0, None
    for i in range(nfr):
        ti = i / FPS
        while j + 1 < len(cambios) and cambios[j + 1][0] <= ti:
            j += 1
        t0, p, an = cambios[j]
        if an:
            if seg != j:                      # entra a una animación
                if cont:
                    cont.close()
                cont = av.open(str(an))
                it, leidos, cuadro, seg = cont.decode(video=0), 0, None, j
            objetivo = int(round((ti - t0) * FPS))
            while leidos <= objetivo:
                try:
                    fr = next(it)
                except StopIteration:
                    break                     # se congela el último cuadro
                cuadro = fr.to_ndarray(format="rgb24")
                leidos += 1
            if cuadro.shape[:2] != (ALTO, ANCHO):
                sys.exit(f"{an.name} no es {ANCHO}x{ALTO}")
            vf = av.VideoFrame.from_ndarray(cuadro, format="rgb24")
        else:
            if p not in cache:
                cache = {p: av.VideoFrame.from_ndarray(imgs[p], format="rgb24")}
            vf = cache[p]
        vf.pts = i
        vf.time_base = Fraction(1, FPS)
        for pk in vs.encode(vf):
            out.mux(pk)
    for pk in vs.encode():
        out.mux(pk)
    if cont:
        cont.close()

    paso = 1024
    for i in range(0, audio.shape[1], paso):
        trozo = np.ascontiguousarray(audio[:, i:i + paso])
        af = av.AudioFrame.from_ndarray(trozo, format="fltp", layout="stereo")
        af.sample_rate = SR
        af.pts = i
        af.time_base = Fraction(1, SR)
        for pk in as_.encode(af):
            out.mux(pk)
    for pk in as_.encode():
        out.mux(pk)
    out.close()
    print(f"-> {salida.relative_to(AQUI)}  ({int(total // 60)}:{total % 60:04.1f})")


if __name__ == "__main__":
    main()
