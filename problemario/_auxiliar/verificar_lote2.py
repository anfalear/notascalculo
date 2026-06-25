import numpy as np

# Prob 8 & 10: inversa de A via Gauss-Jordan y adjunta
A = np.array([[1,2,3],[2,5,3],[1,0,8]], dtype=float)
Ainv = np.linalg.inv(A)
print('=== Prob 8 & 10 ===')
print('A^-1 =', np.round(Ainv).astype(int))
print('det(A) =', round(np.linalg.det(A)))
print('AA^-1 =', np.round(A @ Ainv).astype(int))

# Prob 9: det 5x5
M = np.array([[2,3,0,1,0],[0,1,4,0,2],[1,0,3,0,0],[0,2,0,1,1],[3,0,0,2,0]], dtype=float)
print()
print('=== Prob 9 ===')
print('det(M) =', round(np.linalg.det(M)))

# Prob 13 (a)
A13a = np.array([[1,-1,1],[2,3,0],[0,2,-1]], dtype=float)
B13a = np.array([[2,-1,5,7,8],[4,0,-3,0,1],[3,5,-7,2,1]], dtype=float)
Ainv13a = np.linalg.inv(A13a)
X13a = Ainv13a @ B13a
print()
print('=== Prob 13 (a) ===')
print('det(A) =', round(np.linalg.det(A13a)))
print('A^-1 =', np.round(Ainv13a).astype(int))
print('X =', np.round(X13a).astype(int))

# Prob 13 (b)
A13b = np.array([[-2,0,1],[0,-1,-1],[1,1,-4]], dtype=float)
B13b = np.array([[4,3,2,1],[6,7,8,9],[1,3,7,9]], dtype=float)
Ainv13b = np.linalg.inv(A13b)
X13b = Ainv13b @ B13b
print()
print('=== Prob 13 (b) ===')
print('det(A) =', round(np.linalg.det(A13b)))
print('9*A^-1 =', np.round(9*Ainv13b).astype(int))
print('9*X (filas) =')
for row in 9*X13b:
    print('  ', [round(x, 4) for x in row])

# Prob 11 (ya verificado, confirmacion det)
A11 = np.array([[0,0,2,0],[1,0,0,1],[0,-1,3,0],[2,5,1,3]], dtype=float)
print()
print('=== Prob 11 (confirmacion det) ===')
print('det(A) =', round(np.linalg.det(A11)))
Ainv11 = np.linalg.inv(A11)
print('A^-1 =')
for row in Ainv11:
    print('  ', [round(x, 4) for x in row])
