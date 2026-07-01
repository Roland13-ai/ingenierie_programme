import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path 
data_dir = Path(__file__).parent / "data"
data_dir.mkdir(exist_ok=True)
# Ajoute le chemin vers circuits.py