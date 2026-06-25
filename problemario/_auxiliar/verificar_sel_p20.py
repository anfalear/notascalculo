import numpy as np

# Prob 20: polinomio de grado 5 interpolando datos de alas
# x en unidades de 100 ft/s, y en unidades de 100 lb
x = np.array([1, 2, 4, 8, 16, 32], dtype=float)
y = np.array([0, 3.12, 15.86, 33.7, 81.5, 123.0], dtype=float)

# Vandermonde system: coeficientes [a5, a4, a3, a2, a1, a0]
# V[i,j] = x[i]^(5-j)
n = 6
V = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        V[i, j] = x[i] ** (5 - j)

# Solve V * coef = y
coef = np.linalg.solve(V, y)
print("Coeficientes [a5, a4, a3, a2, a1, a0]:")
for i, c in enumerate(coef):
    print(f"  a{5-i} = {c:.6g}")

# Document's coefficients
doc_coef = np.array([0.000245, -0.0234, 0.891, -16.85, 153.2, -137.4])
print("\nCoeficientes del documento [a5, a4, a3, a2, a1, a0]:")
for i, c in enumerate(doc_coef):
    print(f"  a{5-i} = {c}")

# Verify document's polynomial at data points
print("\nVerificacion del polinomio del documento en los 6 puntos:")
for xi, yi in zip(x, y):
    p = sum(doc_coef[j] * xi**(5-j) for j in range(6))
    print(f"  P({int(xi)}) = {p:.4f}  (esperado: {yi})")

# Compute P(20) correctly using document's coefficients
x_eval = 20
print(f"\nCalculo correcto de P(20) con coeficientes del documento:")
print(f"  0.000245 * 20^5 = 0.000245 * {20**5} = {0.000245 * 20**5}")
print(f"  0.0234  * 20^4 = 0.0234  * {20**4} = {0.0234 * 20**4}")
print(f"  0.891   * 20^3 = 0.891   * {20**3} = {0.891 * 20**3}")
print(f"  16.85   * 20^2 = 16.85   * {20**2} = {16.85 * 20**2}")
print(f"  153.2   * 20   = {153.2 * 20}")
print(f"  -137.4")
p20_doc = sum(doc_coef[j] * x_eval**(5-j) for j in range(6))
print(f"  P(20) (docum. coef.) = {p20_doc:.4f}  [x100 lb = {p20_doc*100:.1f} lb]")

# Document's claimed computation:
print(f"\nComputo del documento (INCORRECTO):")
print(f"  0.000245*20^5 -> documento pone: 78.4  (correcto: {0.000245 * 20**5})")
print(f"  0.0234*20^4  -> documento pone: 374.4  (correcto: {0.0234 * 20**4})")
doc_p20_wrong = 78.4 - 374.4 + 7128 - 6740 + 3064 - 137.4
print(f"  Suma con errores: {doc_p20_wrong}")

# Correct polynomial at x=20
p20_correct = sum(coef[j] * x_eval**(5-j) for j in range(6))
print(f"\nPolinomio correcto (NumPy) en x=20: P(20) = {p20_correct:.4f}  [{p20_correct*100:.1f} lb]")
