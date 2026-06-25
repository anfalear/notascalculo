import numpy as np

# Prob 22: (tr(A)^2 - tr(A^2))/2 == det(A) para varios ejemplos
print('=== Prob 22 ===')
tests = [
    [[1,2],[3,4]],
    [[5,-1],[2,3]],
    [[0,7],[-3,2]],
    [[-1,4],[6,0]],
]
for A in tests:
    Am = np.array(A, dtype=float)
    trA = np.trace(Am)
    trA2 = np.trace(Am @ Am)
    formula = (trA**2 - trA2) / 2
    detA = np.linalg.det(Am)
    ok = np.isclose(formula, detA)
    print(f'A={A}  (tr^2 - tr(A^2))/2={formula:.4f}  det={detA:.4f}  OK={ok}')

# Prob 24: det(A) = ax^2 + bx - c, verificar numericamente
print()
print('=== Prob 24 ===')
# usar a=2, b=3, c=5, x=1 → det esperado = 2*1+3*1-5 = 0
a_v, b_v, c_v, x_v = 2, 3, 5, 1
A24 = np.array([
    [1,      0,   c_v],
    [0,      a_v, -b_v],
    [1/a_v,  x_v, x_v**2]
], dtype=float)
det_num = np.linalg.det(A24)
det_formula = a_v*x_v**2 + b_v*x_v - c_v
print(f'a={a_v}, b={b_v}, c={c_v}, x={x_v}: det(A)={det_num:.6f}, formula={det_formula} -> OK={np.isclose(det_num, det_formula)}')

# segundo caso: a=1, b=0, c=1, x=2 → det = 1*4+0-1 = 3
a_v, b_v, c_v, x_v = 1, 0, 1, 2
A24b = np.array([
    [1,      0,   c_v],
    [0,      a_v, -b_v],
    [1/a_v,  x_v, x_v**2]
], dtype=float)
det_num = np.linalg.det(A24b)
det_formula = a_v*x_v**2 + b_v*x_v - c_v
print(f'a={a_v}, b={b_v}, c={c_v}, x={x_v}: det(A)={det_num:.6f}, formula={det_formula} -> OK={np.isclose(det_num, det_formula)}')

# tercer caso con numeros fraccionarios: a=3, b=-1, c=2, x=0.5
a_v, b_v, c_v, x_v = 3, -1, 2, 0.5
A24c = np.array([
    [1,      0,   c_v],
    [0,      a_v, -b_v],
    [1/a_v,  x_v, x_v**2]
], dtype=float)
det_num = np.linalg.det(A24c)
det_formula = a_v*x_v**2 + b_v*x_v - c_v
print(f'a={a_v}, b={b_v}, c={c_v}, x={x_v}: det(A)={det_num:.6f}, formula={det_formula:.6f} -> OK={np.isclose(det_num, det_formula)}')
