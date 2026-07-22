import numpy as np

# Circuit : Vin = 10V, R1 = 100Ω, R2 = 200Ω
# Trouver Vout (tension aux bornes de R2)

Vin = 10
R1 = 100
R2 = 200

# Loi des nœuds : I = Vin / (R1 + R2)
I = Vin / (R1 + R2)

# Tension aux bornes de R2
Vout = R2 * I

print(f"Courant I = {I:.3f} A")
print(f"Tension Vout = {Vout:.2f} V")
print(f"Vérification : Vout/Vin = R2/(R1+R2) = {R2/(R1+R2):.3f}")

# Circuit deux mailles
# Maille 1 : R1*I1 + R2*(I1 - I2) = V1
# Maille 2 : R2*(I2 - I1) + R3*I2 = -V2

R1, R2, R3 = 10, 20, 30
V1, V2 = 12, 6

# Matrice A et vecteur B
A = np.array([[R1 + R2, -R2],
              [-R2, R2 + R3]])
B = np.array([V1, -V2])

# Résolution
I = np.linalg.solve(A, B)
I1, I2 = I[0], I[1]

print(f"\nI1 = {I1:.3f} A")
print(f"I2 = {I2:.3f} A")
print(f"Vérification A·I = {A @ I}")