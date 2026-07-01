import numpy as np

# Circuit : E = 10 V, R1 = 100 Ω, R2 = 200 Ω
# Équations :
#  I1*R1 + (I1 - I2)*R2 = E
#  (I2 - I1)*R2 + I2*R1 = 0   (maille 2 avec une charge R1)

# Sous forme matricielle : A * I = B
A = np.array([[300, -200],
              [-200, 300]])
B = np.array([10, 0])

# Résolution
courants = np.linalg.solve(A, B)
print("Courants :", courants)

# Vérification
print("A * I =", A @ courants)
