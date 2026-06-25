import numpy as np

# Prob 11: AX - XB = C
A = np.array([[3,1],[-1,2]], dtype=float)
B = np.array([[1,4],[2,0]], dtype=float)
C = np.array([[2,-2],[5,4]], dtype=float)

# Verify document's answer X_doc
X_doc = np.array([[5/7, 4/3],[-4/7, -22/7]], dtype=float)
residual = A @ X_doc - X_doc @ B - C
print("=== Verificación X del documento ===")
print("X_doc =\n", X_doc)
print("AX - XB (con X_doc):\n", A @ X_doc - X_doc @ B)
print("C:\n", C)
print("Residual AX-XB-C:\n", residual)
print("Solución correcta?", np.allclose(residual, 0))

# The equation AX - XB = C can be written as a linear system
# by vectorizing: vec(X) = [x11, x21, x12, x22] (column-major)
# or [x11, x12, x21, x22] (row-major)
# Using the identity: vec(AXB) = (B^T ⊗ A) vec(X)
# AX - XB = C => (I⊗A - B^T⊗I) vec(X) = vec(C)

n = 2
I = np.eye(n)
# Kronecker: A⊗B means we want (I⊗A - B^T⊗I) for vec(AX-XB)=vec(C)
# With column-major vectorization: vec(AXB) = (B^T ⊗ A) vec(X)
# AX = A X I => (I^T ⊗ A) vec(X) = (I ⊗ A) vec(X)
# XB = I X B => (B^T ⊗ I) vec(X)
# So: ((I⊗A) - (B^T⊗I)) vec(X) = vec(C)

M = np.kron(I, A) - np.kron(B.T, I)
vec_C = C.flatten(order='F')  # column-major vectorization

print("\n=== Sistema vectorizado (col-major) ===")
print("M =\n", M)
print("vec(C) =", vec_C)
vec_X = np.linalg.solve(M, vec_C)
print("vec(X) = [x11, x21, x12, x22] =", vec_X)
X_correct = vec_X.reshape(n, n, order='F')
print("X correcto =\n", X_correct)

# Verify correct solution
print("\n=== Verificación X correcto ===")
res2 = A @ X_correct - X_correct @ B - C
print("AX - XB =\n", A @ X_correct - X_correct @ B)
print("C =\n", C)
print("Residual =\n", res2)
print("Correcto?", np.allclose(res2, 0))

# Also show as fractions
from fractions import Fraction
print("\nX correcto como fracciones:")
for i in range(2):
    row = [str(Fraction(X_correct[i,j]).limit_denominator(100)) for j in range(2)]
    print(f"  {row}")

# Show correct system (4 equations)
print("\n=== Sistema correcto de 4 ecuaciones ===")
print("Correct XB[1,1] = x11 + 2*x12 (NO x11 + 2*x21)")
print("System:")
print("  2*x11 - 2*x12 + x21 = 2")
print(" -4*x11 + 3*x12 + x22 = -2")
print(" -x11 + x21 - 2*x22 = 5")
print(" -x12 - 4*x21 + 2*x22 = 4")
