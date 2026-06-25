import numpy as np

# Prob 19: propiedades det dado det(M)=-8
# Verificar det(C) del inciso (b)
C = np.array([[1,2,0],[0,1,3],[4,0,1]], dtype=float)
print('=== Prob 19 (b) ===')
print('det(C) =', round(np.linalg.det(C)))
print('det(C)*(-8) =', round(np.linalg.det(C)) * (-8))

# Verificar con una M concreta que det(B)=25*det(M)
M = np.array([[1,0,0],[0,2,0],[0,0,3]], dtype=float)  # det=6
B = C @ M
print('Prueba con M diagonal (1,2,3): det(M)=', round(np.linalg.det(M)))
print('det(CM)=', round(np.linalg.det(B)), ' debe ser 25*6=', 25*6)

# Prob 20: operaciones elementales y det
B20 = np.array([[-1,5,8],[0,-8,6],[0,0,-8]], dtype=float)
detB = np.linalg.det(B20)
print()
print('=== Prob 20 ===')
print('det(B) (triangular) =', round(detB))
factor = (-4) * 1 * (-1) * (-1/4)
print('Factor total de operaciones:', factor)
print('det(A) = det(B)/factor =', round(detB / factor))

# Prob 23: A^2 = 3I + 2A para la matriz específica
A23 = np.array([[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]], dtype=float)
A23sq = A23 @ A23
I4 = np.eye(4)
RHS = 3*I4 + 2*A23
print()
print('=== Prob 23 (previa lectura) ===')
print('A^2 =')
print(A23sq.astype(int))
print('3I+2A =')
print(RHS.astype(int))
print('A^2 == 3I+2A:', np.allclose(A23sq, RHS))
# Derivar A^{-1} de A^2 = 3I+2A
# A*A = 3I + 2A => A*A - 2A = 3I => A(A-2I) = 3I => A^{-1} = (A-2I)/3
Ainv23 = (A23 - 2*I4) / 3
print('A^{-1} = (A-2I)/3 =')
print(np.round(Ainv23, 4))
print('A * A^{-1} =')
print(np.round(A23 @ Ainv23, 4))
