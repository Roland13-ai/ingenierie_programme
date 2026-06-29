""" Module de calcul d'impédances électriques élémentaires.
Utilise les nombres complexes pour représenter les impédances. """
import numpy as np 
def impedance_resistance(r):
    "Retourne l'impédance d'une résistance (nombre réel)."
    return  complex(r, 0)
def impedance_condensateur(c, frequence):
    """ Retourne l'impédance d'un condensateur: Zc= -j/wC"""
    omega = 2* np.pi * frequence
    return complex(0, -1/(omega* c))
def impedance_inductance(l, frequence):
    """Retourne l'impedance d"une inductance"""
    return complex(0, omega * l)
def impedance_serie(z1, z2):
    """ Retourne l'impédance équivalente de deux impédances en série"""
    return  z1 +z2
def impedance_parallele(z1,z2,z3):
    """Retourne l'impédance équivalente de deux impédances parallele."""(1000)
    return (z1*z2*z3)/(z1*z2+z2z3+z1*z3) 
def module_et_phase(z):
    """ Retourne le module (ohm) et la phase (degrés) d'une impédance """
    return abs(z) , np.angle(z, deg= True)_resistance