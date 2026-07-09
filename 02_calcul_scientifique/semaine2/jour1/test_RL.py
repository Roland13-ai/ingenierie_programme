import sympy as sp

# Symboles de base
R, C, L, omega = sp.symbols('R C L omega', positive=True)

# Les trois impédances
Z_R = R                              # Résistance : Z = R
Z_C = 1 / (sp.I * C * omega)         # Condensateur : Z = -j/(Cω)
Z_L = sp.I * L * omega               # Inductance : Z = jLω
"""
print("Impédance résistance :")
sp.pprint(Z_R)

print("\nImpédance condensateur :")
sp.pprint(Z_C)

print("\nImpédance inductance :")
sp.pprint(Z_L)"""
def association_serie(Z_R, Z_C):
    # Série : on additionne
    return Z_R + Z_C

def association_parallele(Z_R, Z_C): 
    # Parallèle : (Z1*Z2) / (Z1+Z2)
    return (Z_R * Z_C) / (Z_R + Z_C)
  
def module_impedance(Z):
    """Retourne le module symbolique d'une impédance complexe."""
    return sp.sqrt(sp.re(Z)**2 + sp.im(Z)**2)

# Test 
Z_C_num = Z_C.subs({C: 40, omega: 314})
Z_R_num= Z_R.subs(R, 200)

Z_par= association_parallele(Z_R_num, Z_C_num)
Z_ser= association_serie(Z_R_num, Z_C_num)
Z_C_mod= module_impedance(Z_R_num)
Z_R_mod= module_impedance(Z_C_num)

print(f"Zeq_Serie= {Z_ser}")
print(f"Zeq_parallele= {Z_par}") 
print(f"Module_ZC= {Z_C_mod}")
print(f"Module_ZR= {Z_R_mod}")