import sympy as sp

# -------------------------------
# 1. Définir des symboles
# -------------------------------
# On déclare des variables qui ne contiennent PAS des nombres,
# mais des lettres (comme en maths).
R, C, L, omega = sp.symbols('R C L omega', positive=True)

# -------------------------------
# 2. Impédance d'un condensateur
# -------------------------------
# En électricité : Zc = 1 / (j*C*omega)
# sp.I représente le nombre imaginaire j
Zc = 1 / (sp.I * C * omega)
print("Impédance du condensateur :")
print("Zc =", Zc)

# -------------------------------
# 3. Impédance d'une inductance
# -------------------------------
Zl = sp.I * L * omega
print("\nImpédance de l'inductance :")
print("Zl =", Zl)

# -------------------------------
# 4. Circuit RC série
# -------------------------------
Z_R = R
Z_eq = Z_R + Zc
print("\nImpédance équivalente RC série :")
print("Z_eq =", Z_eq)

# -------------------------------
# 5. Module de l'impédance
# -------------------------------
# Le module d'un complexe a+bj est sqrt(a² + b²)
module_carre = sp.re(Z_eq)**2 + sp.im(Z_eq)**2
module = sp.sqrt(sp.simplify(module_carre))
print("\nModule de Z_eq :")
print("|Z| =", module)

# -------------------------------
# 6. Résoudre une équation
# -------------------------------
# Question : pour quelle pulsation ω le module vaut-il R/2 ?
# On crée une équation : |Z| = R/2
equation = sp.Eq(module, R/2)
solution = sp.solve(equation, omega)
print("\nPulsation pour laquelle |Z| = R/2 :")
print("ω =", solution)

# Exercice : impédance d'un circuit RL parallèle
Z_RL_parallele = (R * Zl) / (R + Zl)
sp.simpli(Z_RL_parallele)
print("\nImpédance RL parallèle :")
sp.pprint(Z_RL_parallele)   # Affiche la formule 
