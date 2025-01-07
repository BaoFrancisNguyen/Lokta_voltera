import numpy as np
import pandas as pd
from lotka_voltera_app import time, rabbit, fox


# Fonction pour charger les données réelles depuis un fichier CSV
def load_csv_data(file_path):
    try:
        data = pd.read_csv(file_path)
        # Vérifie que les colonnes nécessaires sont présentes
        if 'Time' in data.columns and 'Prey' in data.columns and 'Predator' in data.columns:
            return data['Time'].values, data['Prey'].values, data['Predator'].values
        else:
            raise ValueError("Le fichier CSV doit contenir les colonnes 'Time', 'Prey', et 'Predator'.")
    except Exception as e:
        raise IOError(f"Erreur lors du chargement du fichier CSV : {e}")

# Fonction pour calculer la MSE
# on utilise le carré de la différence entre les valeurs réelles et les valeurs simulées pour obtenir une valeur positive

# Fonction pour calculer la MSE
def calculate_mse(real_prey, real_predator, simulated_prey, simulated_predator):
    try:
        mse_prey = np.mean((real_prey - simulated_prey) ** 2)
        mse_predator = np.mean((real_predator - simulated_predator) ** 2)
        return mse_prey, mse_predator
    except Exception as e:
        raise ValueError(f"Erreur dans le calcul du MSE : {e}")
