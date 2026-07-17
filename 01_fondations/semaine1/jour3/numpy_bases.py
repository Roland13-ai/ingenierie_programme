import numpy as np

# 1. Créer un tableau de tensions (10 valeurs de 0 à 5 V)
tensions = np.linspace(0, 5, 10)
print("Tensions (V) :", tensions)

# 2. Loi d'Ohm : I = U / R
R = 1000  # ohms
courants = tensions / R
print("Courants (A) :", courants)

# 3. Puissance : P = U * I
puissances = tensions * courants5
print("Puissances (W) :", puissances)

# 4. Extraire les valeurs > 2.5 V
tensions_elevees = tensions[tensions > 2.5]
print("Tensions > 2.5 V :", tensions_elevees)