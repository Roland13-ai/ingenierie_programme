import numpy as np
import matplotlib.pyplot as plt

R = 1000
C = 1e-6
f = np.logspace(0, 5, 200)

Z_R = R
Z_C = 1 / (1j * 2 * np.pi * f * C)
Z_eq = Z_R + Z_C
module = np.abs(Z_eq)
phase = np.angle(Z_eq, deg=True)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.semilogx(f, module, 'b', linewidth=1.5)
ax1.set_ylabel('Module (Ohm)')
ax1.set_title('Réponse en fréquence - Circuit RC série')
ax1.grid(True)

ax2.semilogx(f, phase, 'r', linewidth=1.5)
ax2.set_xlabel('Fréquence (Hz)')
ax2.set_ylabel('Phase (deg)')
ax2.grid(True)

plt.tight_layout()
plt.savefig('02_calcul_scientifique/semaine2/jour10/reponse_RC.png')
plt.show()
print("Graphique sauvegardé avec succès.")