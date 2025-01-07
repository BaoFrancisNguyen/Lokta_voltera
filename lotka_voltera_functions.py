import numpy as np
import pandas as pd



import numpy as np
import pandas as pd

# Fonction pour charger les données réelles depuis un fichier CSV
def load_csv_data(file_path):
    try:
        data = pd.read_csv(file_path)
        
        # Vérifie que les colonnes nécessaires sont présentes
        if 'date' in data.columns and 'lapin' in data.columns and 'renard' in data.columns:
            return data['date'].values, data['lapin'].values, data['renard'].values
        else:
            raise ValueError("Le fichier CSV doit contenir les colonnes 'date', 'lapin', et 'renard'.")
    except Exception as e:
        raise IOError(f"Erreur lors du chargement du fichier CSV : {e}")

# Fonction pour calculer la MSE
def calculate_mse(real_lapin, real_renard, simulated_lapin, simulated_renard):
    try:
        mse_lapin = np.mean((real_lapin - simulated_lapin) ** 2)
        mse_renard = np.mean((real_renard - simulated_renard) ** 2)
        return mse_lapin, mse_renard
    except Exception as e:
        raise ValueError(f"Erreur dans le calcul du MSE : {e}")

