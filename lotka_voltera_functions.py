import numpy as np
import pandas as pd
from lotka_voltera_app import time, rabbit, fox


# Fonction pour charger les données réelles depuis un fichier CSV
def load_csv_data(file_path):
    data = pd.read_csv(file_path)
    return data['Time'], data['Prey'], data['Predator']

# Fonction pour calculer la MSE
# on utilise le carré de la différence entre les valeurs réelles et les valeurs simulées pour obtenir une valeur positive

def calculate_mse(real_prey, real_predator, simulated_prey, simulated_predator):
    # on calcule la moyenne des carrés des différences
    mse_prey = np.mean((real_prey - simulated_prey) ** 2)
    mse_predator = np.mean((real_predator - simulated_predator) ** 2)
    
    return mse_prey, mse_predator

# Charger un fichier CSV
csv_file_path = input("populations_lapins_renards.csv")
time_real, prey_real, predator_real = load_csv_data(csv_file_path)