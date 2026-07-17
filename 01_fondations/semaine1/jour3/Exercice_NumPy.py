import numpy as np

# Tableau de 10 tensions différentes
Vin = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
R1 = 100
R2 = 200

# Calcul vectoriel : tout d'un coup
Req = R1 + R2
I = Vin / Req
VR1 = R1 * I
VR2 = R2 * I

print("-" * 40)
for i in range(len(Vin)):
    print(f" {Req} | {Vin[i]:6.0f}  | {I[i]:.1f} | {VR1[i]:6.2f} | {VR2[i]:.2f}")
print("-" * 40)
