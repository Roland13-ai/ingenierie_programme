"""
Projet : Analyse complète d'un circuit RLC série
Auteur : Roland13-ai
Date   : 2026
Objectif : Utiliser NumPy, SymPy, Matplotlib et CSV pour étudier
           un circuit RLC série à partir des paramètres saisis par l'utilisateur.
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import csv

# ============================================================
# ÉTAPE 1 – Saisie des paramètres
# ============================================================
print("=== ANALYSE D'UN CIRCUIT RLC SÉRIE ===\n")
R = float(input("Résistance R (Ω)     : "))
L = float(input("Inductance L (H)      : "))
C = float(input("Capacité C (F)        : "))
fmin = float(input("Fréquence minimale (Hz) : "))
fmax = float(input("Fréquence maximale (Hz) : "))
N = int(input("Nombre de points       : "))

# ============================================================
# ÉTAPE 2 – Calculs numériques avec NumPy
# ============================================================
# Vecteur de fréquences en échelle logarithmique
f = np.logspace(np.log10(fmin), np.log10(fmax), N)
omega = 2 * np.pi * f

# Impédances élémentaires
Z_R = R                          # résistance (réelle)
Z_L = 1j * L * omega             # inductance (imaginaire positive)
Z_C = 1 / (1j * C * omega)       # condensateur (imaginaire négative)
Z = Z_R + Z_L + Z_C              # impédance totale (complexe)

# Module et phase
module = np.abs(Z)                # module en Ω
phase = np.angle(Z, deg=True)     # phase en degrés

# Fréquence de résonance (module minimal)
idx_min = np.argmin(module)       # indice du minimum
f_res = f[idx_min]                # fréquence de résonance (Hz)
mod_res = module[idx_min]         # module à la résonance (Ω)

print("\n--- RÉSULTATS NUMÉRIQUES ---")
print(f"Fréquence de résonance : {f_res:.2f} Hz")
print(f"Module à la résonance : {mod_res:.2f} Ω")

# ============================================================
# ÉTAPE 3 – Calcul symbolique avec SymPy
# ============================================================
# Déclaration des symboles
R_s, L_s, C_s, omega_s = sp.symbols('R_s L_s C_s omega_s', positive=True)

# Impédance symbolique
Z_s = R_s + sp.I * L_s * omega_s + 1 / (sp.I * C_s * omega_s)
module_s = sp.sqrt(sp.re(Z_s)**2 + sp.im(Z_s)**2)

# Dérivée du module par rapport à omega
derivee = sp.diff(module_s, omega_s)
freq_res_s = sp.solve(sp.Eq(derivee, 0), omega_s)

print("\n--- RÉSULTATS SYMBOLIQUES ---")
print("Impédance totale :")
sp.pprint(Z_s)
print("Fréquence(s) de résonance (ω₀) :")
sp.pprint(freq_res_s)

# Vérification avec la formule classique
f0_classique = 1 / (2 * np.pi * np.sqrt(L * C))
print(f"F₀ classique = {f0_classique:.2f} Hz")

# ============================================================
# ÉTAPE 4 – Tracé du diagramme de Bode (Matplotlib)
# ============================================================
plt.figure(figsize=(10, 8))

# Module
plt.subplot(2, 1, 1)
plt.semilogx(f, module, 'b', linewidth=2)
plt.axvline(f_res, color='r', linestyle='--', label=f'Résonance ({f_res:.2f} Hz)')
plt.ylabel('Module (Ω)')
plt.title('Diagramme de Bode – Circuit RLC série')
plt.legend()
plt.grid(True)

# Phase
plt.subplot(2, 1, 2)
plt.semilogx(f, phase, 'r', linewidth=2)
plt.axvline(f_res, color='b', linestyle='--', label=f'Résonance ({f_res:.2f} Hz)')
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Phase (°)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('03_projets/bode_RLC.png')
plt.close()
print("\nGraphique sauvegardé : 03_projets/bode_RLC.png")

# ============================================================
# ÉTAPE 5 – Export des données (CSV)
# ============================================================
with open('03_projets/rlc_analyse.csv', 'w', newline='', encoding='utf-8') as fichier:
    writer = csv.writer(fichier)
    writer.writerow(['Frequence (Hz)', 'Module (Ohm)', 'Phase (deg)'])
    for i in range(N):
        writer.writerow([f"{f[i]:.2f}", f"{module[i]:.2f}", f"{phase[i]:.2f}"])

print("Données exportées : 03_projets/rlc_analyse.csv")
print("\n=== ANALYSE TERMINÉE ===")