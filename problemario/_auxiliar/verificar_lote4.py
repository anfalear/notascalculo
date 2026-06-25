import numpy as np

# Prob 23: A^2 = 3I + 2A, A^{-1} = (A-2I)/3
A = np.array([[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]], dtype=float)
I4 = np.eye(4)
A2 = A @ A
RHS = 3*I4 + 2*A
Ainv = (A - 2*I4) / 3

print('=== Prob 23 ===')
print('A^2 correcto:')
print(A2.astype(int))
print('3I+2A:')
print(RHS.astype(int))
print('A^2 == 3I+2A:', np.allclose(A2, RHS))
print('A * Ainv = I?', np.allclose(A @ Ainv, I4))
print('Ainv = (A-2I)/3:')
from fractions import Fraction
for row in Ainv:
    print(' ', [str(Fraction(x).limit_denominator(10)) for x in row])

# Prob 24: det(A) = ax^2 + bx - c
# Verificar con un ejemplo concreto: a=1, b=2, c=3, x=1
import sympy as sp
a, b, c, x = sp.symbols('a b c x')
A24 = sp.Matrix([
    [1, 0, c],
    [0, a, -b],
    [sp.Rational(1,1)/a, x, x**2]
])
det24 = A24.det()
print()
print('=== Prob 24 ===')
print('det(A) simbolico =', sp.expand(det24))
print('Esperado: a*x^2 + b*x - c')

# Prob 22: tr y det relacion
a, b, c, d = sp.symbols('a b c d')
A22 = sp.Matrix([[a, b],[c, d]])
A22sq = A22 * A22
tr_A = sp.trace(A22)
tr_A2 = sp.trace(A22sq)
det_A = A22.det()
formula = (tr_A**2 - tr_A2) / 2
print()
print('=== Prob 22 ===')
print('tr(A) =', tr_A)
print('tr(A^2) =', sp.expand(tr_A2))
print('(tr(A)^2 - tr(A^2))/2 =', sp.expand(formula))
print('det(A) =', det_A)
print('Coinciden:', sp.simplify(formula - det_A) == 0)
