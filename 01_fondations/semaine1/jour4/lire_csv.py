import csv
import matplotlib.pyplot as plt
from pathlib import Path

# Chemin vers le dossier data/
data_dir = Path(__file__).parent / "data"
fichier_csv = data_dir / "reponse_freq_RC.csv"

# Listes pour stocker les données
freqs, modules, phases = [], [], []

# Lecture du CSV
with open(fichier_csv, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Ignore la ligne d'en-tête
    for row in reader:
        freqs.append(float(row[0]))
        modules.append(float(row[1]))
        phases.append(float(row[2]))

# Création du graphique
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.semilogx(freqs, modules)
ax1.set_ylabel("Module (Ω)")
ax1.set_title("Réponse en fréquence – Circuit RC série")
ax1.grid(True)

ax2.semilogx(freqs, phases)
ax2.set_xlabel("Fréquence (Hz)")
ax2.set_ylabel("Phase (°)")
ax2.grid(True)

plt.tight_layout()
plt.savefig(data_dir / "reponse_freq_RC.png")
plt.show()