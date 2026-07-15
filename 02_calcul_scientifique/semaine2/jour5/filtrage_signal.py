import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Créer un signal bruité
t = np.linspace(0, 1, 1000)
signal_pur = np.sin(2 * np.pi * 5 * t)    # Signal 5 Hz
bruit = 0.5 * np.random.randn(len(t))      # Bruit aléatoire
signal_bruite = signal_pur + bruit

# Filtre passe-bas Butterworth
fc = 10               # Fréquence de coupure 10 Hz
fs = 1000              # Fréquence d'échantillonnage
ordre = 4
b, a = signal.butter(ordre, fc / (fs/2), btype='low')
signal_filtre = signal.filtfilt(b, a, signal_bruite)

# Tracé
plt.figure(figsize=(10, 6))
plt.plot(t, signal_bruite, alpha=0.5, label='Bruité')
plt.plot(t, signal_pur, 'k--', linewidth=2, label='Pur')
plt.plot(t, signal_filtre, 'r', linewidth=2, label='Filtré')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.title('Filtrage passe-bas (Butterworth)')
plt.legend()
plt.grid(True)
plt.savefig('02_calcul_scientifique/semaine2/jour5/filtrage.png')
plt.close()