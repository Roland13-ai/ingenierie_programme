
import numpy as np
import sympy as sp  
import matplotlib.pyplot as plt
import csv

# Étape 1 : Saisie des paramètres
R = float(input("Résistance R (Ω) : "))
L = float(input("Inductance L (H) : "))
C = float(input("Capacité C (F) : "))
fmin = float(input("Fréquence minimale (Hz) : "))
fmax = float(input("Fréquence maximale (Hz) : "))
N = int(input("Nombre de points : "))

import numpy as np

# Étape 2 : Calculs avec NumPy
f = np.logspace(np.log10(fmin), np.log10(fmax), N)
omega = 2 * np.pi * f

Z_R = R
Z_L = 1j * L * omega
Z_C = 1 / (1j * C * omega)
Z = Z_R + Z_L + Z_C

module = np.abs(Z)
phase = np.angle(Z, deg=True)

# Fréquence de résonance (module minimal)
idx_min = np.argmin(module)
f_res = f[idx_min]
mod_res = module[idx_min]

print(f"\nFréquence de résonance : {f_res:.2f} Hz")
print(f"Module à la résonance : {mod_res:.2f} Ω")
