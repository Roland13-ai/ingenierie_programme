
🎯 Projet – Analyse d’un circuit RLC série
Objectif : Partir des valeurs de 
R
R, 
L
L, 
C
C et produire un rapport complet (calculs, graphiques, fichier CSV).

Déroulé en 5 étapes
Saisie des paramètres
L’utilisateur entre 
R
R (Ω), 
L
L (H), 
C
C (F), la plage de fréquences (fmin, fmax) et le nombre de points.

Calculs numériques (NumPy)

Vecteur de fréquences 
f
f

Pulsation 
ω
=
2
π
f
ω=2πf

Impédance 
Z
=
R
+
j
(
L
ω
−
1
C
ω
)
Z=R+j(Lω− 
Cω
1
​
 )

Module 
∣
Z
∣
∣Z∣ et phase 
φ
φ

Fréquence de résonance 
f
0
=
1
2
π
L
C
f 
0
​
 = 
2π 
LC
​
 
1
​
  (calculée avec NumPy)

Calcul symbolique (SymPy)

Déclarer 
R
,
L
,
C
,
ω
R,L,C,ω comme symboles

Écrire la formule de l’impédance 
Z
Z

Dériver l’expression pour retrouver la fréquence de résonance

Vérifier que le résultat correspond à 
f
0
=
1
/
(
2
π
L
C
)
f 
0
​
 =1/(2π 
LC
​
 )

Tracé du diagramme de Bode (Matplotlib)

Figure avec deux sous‑graphiques (module et phase)

Échelle semi‑log pour l’axe des fréquences

Marqueur vertical à la fréquence de résonance

Export CSV

Sauvegarder 
f
f, 
∣
Z
∣
∣Z∣ et 
φ
φ dans un fichier rlc_analyse.csv