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

R_s, L_s, C_s, omega_s= sp.symbols('R_s, L_s, C_s, omega_s',  positive= True)
Z_s = R_s + (sp.I * L_s * omega_s + 1/(sp.I * C_s * omega_s))
Z_simp= sp.simplify( Z_s)
sp.pprint(Z_simp)

Mod_Zs= sp.sqrt((Z_s)**2+sp.im(Z_s)**2)
sp.pprint(Mod_Zs)

# Résolution : partie imaginaire = 0 → L_s*omega_s - 1/(C_s*omega_s) = 0
equation = sp.Eq(L_s * omega_s, 1/(C_s * omega_s))
solution = sp.solve(equation, omega_s)
print("\nPulsation(s) de résonance :")
sp.pprint(solution)

#Créer une figure de taille 10×8
plt.figure(figsize=(10,8))
#Tracer le module en fonction de la fréquence dans le sous-graphique du haut (échelle semi-log)
pltsubplot(2,1,1)
plt.plot(Mod_Zs, f)
plt.xlog("f")
plt.ylog("Module")
#Tracer la phase en fonction de la fréquence dans le sous-graphique du bas (échelle semi-log)
pltsubplot(2,1,2)
plt.plot(phase, f)
plt.xlog("phase")
plt.ylog("f")
#jouter une ligne verticale à la fréquence de résonance sur chaque graphique
plt.plot(f_res)
#Ajouter les étiquettes, titres et grilles
plt.title("RLC graphics")
#Sauvegarder l'image bode_RLC.png dans 03_projets/
plt.savefig("03_projets")
#Fermer la figure
plt.show()