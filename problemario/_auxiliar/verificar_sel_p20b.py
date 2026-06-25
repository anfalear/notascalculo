import numpy as np
from fractions import Fraction

# Datos exactos
x = np.array([1.0, 2.0, 4.0, 8.0, 16.0, 32.0])
y = np.array([0.0, 3.12, 15.86, 33.7, 81.5, 123.0])

# Vandermonde V[i,j] = x[i]^(5-j)
n = 6
V = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        V[i, j] = x[i] ** (5 - j)

# Condition number
cond = np.linalg.cond(V)
print(f"Numero de condicion de la matriz de Vandermonde: {cond:.3e}")

# Solve
coef = np.linalg.solve(V, y)
print("\nCoeficientes correctos [a5, a4, a3, a2, a1, a0]:")
labels = ['a5', 'a4', 'a3', 'a2', 'a1', 'a0']
for i, (lbl, c) in enumerate(zip(labels, coef)):
    print(f"  {lbl} = {c:.8f}")

# Verify at data points
print("\nVerificacion en los 6 puntos de datos:")
all_ok = True
for xi, yi in zip(x, y):
    p = sum(coef[j] * xi**(5-j) for j in range(6))
    ok = abs(p - yi) < 0.001
    if not ok:
        all_ok = False
    print(f"  P({int(xi)}) = {p:.6f}  (esperado: {yi})  {'OK' if ok else 'ERROR'}")
print(f"Todos correctos: {all_ok}")

# P(20) computation
x_eval = 20.0
p20 = sum(coef[j] * x_eval**(5-j) for j in range(6))
print(f"\nP(20) correcto = {p20:.4f}  [{p20*100:.1f} lb]")

# Show step by step
print(f"\nCalculando P(20) paso a paso:")
for i, (lbl, c) in enumerate(zip(labels, coef)):
    power = 5 - i
    val = c * x_eval**power
    print(f"  {c:.6f} * 20^{power} = {c:.6f} * {x_eval**power:.0f} = {val:.4f}")
print(f"  Suma = {p20:.4f}")

# Rounded coefficients (4 sig figs)
print("\n=== Tabla RREF para el documento (4 cifras sig.) ===")
for i, (lbl, c) in enumerate(zip(labels, coef)):
    print(f"  {lbl} ≈ {c:.4f}")
