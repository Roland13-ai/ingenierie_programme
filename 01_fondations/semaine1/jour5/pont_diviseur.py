# --- Association série ---
class AssociationSerie:
    def __init__(self, R1, R2, Vin):
        self.R1 = R1
        self.R2 = R2
        self.Vin = Vin
    
    def calculer(self):
        self.Req = self.R1 + self.R2
        self.I = self.Vin / self.Req
        print(f"Req = {self.Req:.2f} Ω")
        print(f"I = {self.I:.4f} A")
    
    def tension_R1(self):
        VR1 = (self.Vin * self.R1) / (self.R1 + self.R2)
        print(f"VR1 = {VR1:.2f} V")
        return VR1
    
    def tension_R2(self):
        VR2 = (self.Vin * self.R2) / (self.R1 + self.R2)
        print(f"VR2 = {VR2:.2f} V")
        return VR2


# --- Association parallèle ---
class AssociationParallele:
    def __init__(self, R1, R2, I_total):
        self.R1 = R1
        self.R2 = R2
        self.I_total = I_total
    
    def calculer(self):
        self.Req = (self.R1 * self.R2) / (self.R1 + self.R2)
        self.V = self.Req * self.I_total
        print(f"Req = {self.Req:.2f} Ω")
        print(f"V = {self.V:.2f} V")
    
    def courant_R1(self):
        I1 = (self.I_total * self.R2) / (self.R1 + self.R2)
        print(f"I1 = {I1:.4f} A")
        return I1
    
    def courant_R2(self):
        I2 = (self.I_total * self.R1) / (self.R1 + self.R2)
        print(f"I2 = {I2:.4f} A")
        return I2


# --- Programme principal ---
print("=== Pont diviseur ===")
print("1 - Série")
print("2 - Parallèle")
choix = int(input("Votre choix : "))

R1 = float(input("R1 (Ω) : "))
R2 = float(input("R2 (Ω) : "))

if choix == 1:
    Vin = float(input("Vin (V) : "))
    circuit = AssociationSerie(R1, R2, Vin)
    circuit.calculer()
    
    option = int(input("\n1 - Tension R1 | 2 - Tension R2 : "))
    if option == 1:
        circuit.tension_R1()
    elif option == 2:
        circuit.tension_R2()

elif choix == 2:
    I_total = float(input("I total (A) : "))
    circuit = AssociationParallele(R1, R2, I_total)
    circuit.calculer()
    
    option = int(input("\n1 - Courant R1 | 2 - Courant R2 : "))
    if option == 1:
        circuit.courant_R1()
    elif option == 2:
        circuit.courant_R2()

else:
    print("Choix invalide.")
    