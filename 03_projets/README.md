Crée un fichier README.md dans 03_projets/ :

markdown
# Projet : Analyse d'un circuit RLC série

## 📝 Description

Ce projet réalise l'analyse complète d'un circuit RLC série à partir des paramètres saisis par l'utilisateur (R, L, C, plage de fréquences).

Il combine **4 frameworks Python** :
- **NumPy** : calculs vectoriels (impédance, module, phase, fréquence de résonance)
- **SymPy** : calcul symbolique (formule exacte de l'impédance, dérivation pour trouver la résonance)
- **Matplotlib** : tracé du diagramme de Bode (module et phase)
- **CSV** : export des données pour analyse externe (Excel, etc.)

## 🚀 Utilisation

```bash
python projet_RLC.py
Puis saisir les valeurs demandées :

Résistance R (Ω)

Inductance L (H)

Capacité C (F)

Fréquence minimale (Hz)

Fréquence maximale (Hz)

Nombre de points

📊 Résultats générés
Affichage de la fréquence de résonance et du module minimal

Formule symbolique de l'impédance et dérivée

Diagramme de Bode (module + phase) sauvegardé en PNG

Export CSV des données (fréquence, module, phase)

🧰 Technologies utilisées
Outil	                                      Rôle
NumPy                                     	Calculs numériques vectorisés
SymPy                                      	Calcul symbolique (formules exactes)
Matplotlib	                                Visualisation graphique
CSV	                                         Export de données tabulaires

📁 Fichiers
text
03_projets/
├── projet_RLC.py          # Script principal
├── bode_RLC.png           # Diagramme de Bode généré
├── rlc_analyse.csv        # Données exportées
└── README.md              # Documentation (ce fichier)