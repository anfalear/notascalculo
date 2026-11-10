"""
render_escenas.py -- Render final (1920x1080, 30 fps) de escenas_campos.py.
Deja los .mp4 con nombre claro en ./animaciones/ para llevarlos al editor.

    python render_escenas.py                 # las 5
    python render_escenas.py V2aNormalSuperficie V3aSuperficiesBorde
"""
import shutil, subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ESCENAS = {
    "V1aOrientacionBorde": "video1_A_orientacion_borde.mp4",
    "V1bVerificacionDisco": "video1_B_verificacion_disco.mp4",
    "V2aNormalSuperficie": "video2_A_normal_superficie.mp4",
    "V2bParaboloideBase": "video2_B_paraboloide_base.mp4",
    "V3aSuperficiesBorde": "video3_A_superficies_borde.mp4",
}

pedidas = sys.argv[1:] or list(ESCENAS)
dest = AQUI / "animaciones"
dest.mkdir(exist_ok=True)
for esc in pedidas:
    print(f"== {esc}", flush=True)
    subprocess.run(["manim", "--resolution", "1920,1080", "--frame_rate", "30",
                    "--disable_caching", "escenas_campos.py", esc], cwd=AQUI, check=True)
    mp4 = AQUI / "media" / "videos" / "escenas_campos" / "1080p30" / f"{esc}.mp4"
    shutil.copy2(mp4, dest / ESCENAS[esc])
    print(f"   -> animaciones/{ESCENAS[esc]}", flush=True)
