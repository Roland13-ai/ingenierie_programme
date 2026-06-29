from circuits import (impedance_resistance, impedance_condensateur, impedance_inductance, impedance_serie, impedance_parallele)
import numpy as np
r = 1000
c = 1e-6
f = 50
z_r = impedance_resistance(r)
z_c = impedance_condensateur(c, f)
z_rc = impedance_serie(z_r, z_c)

print(f"R= {z_r:.2f} ohm")
print(f"Zc a {f} Hz = {z_c :.2f} ohm")
print(f" équivalent série = {z_rc :.2f} ohm")
print(f"Module= {abs(z_rc):.2f} ohm")
print(f"Phase = {np.angle(z_rc, deg=True):.2f}°")