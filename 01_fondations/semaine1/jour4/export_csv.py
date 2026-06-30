import csv
import numpy as np 
from pathlib import Path
import sys


# Ajoute le dossier jour3 au chemin pour importer circuits
sys.path.insert(0, str(Path(__file__).parent.parent / "jour3"))
from circuits import impedance_resistance, impedance_condensateur, impedance_serie, module_et_phase

# Paramètres du circuit
R = 1000         # 1 kΩ
C = 1e-6         # 1 µF
frequences = np.logspace(0, 5, 50)  # 50 fréquences de 1 Hz à 100 kHz

# Crée le dossier data/ s'il n'existe pas
data_dir = Path(__file__).parent / "data"
data_dir.mkdir(exist_ok=True)

# Fichier CSV de sortie
fichier_csv = data_dir / "reponse_freq_RC.csv"

# Écriture du fichier CSV
with open(fichier_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Frequence (Hz)", "Module (Ohm)", "Phase (deg)"])  # En-tête
    for f_req in frequences:
        z_r = impedance_resistance(R)
        z_c = impedance_condensateur(C, f_req)
        z_eq = impedance_serie(z_r, z_c)
        module, phase = module_et_phase(z_eq)
        writer.writerow([f"{f_req:.2f}", f"{module:.2f}", f"{phase:.2f}"])

print(f"Fichier créé : {fichier_csv}")
print(f"Nombre de lignes : {len(frequences)}")