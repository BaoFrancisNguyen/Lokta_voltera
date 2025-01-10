import numpy as np
import pandas as pd
from itertools import product


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
    
# Fonction de simulation du modèle de Lotka-Volterra
def simulate_lotka_volterra(alpha, beta, gamma, delta, step=0.01, iterations=100_000):
    rabbit = [1]
    fox = [2]
    time = [0]
    
    for _ in range(iterations):
        new_rabbit = (rabbit[-1] * (alpha - beta * fox[-1])) * step + rabbit[-1]
        new_fox = (fox[-1] * (delta * rabbit[-1] - gamma)) * step + fox[-1]
        
        rabbit.append(new_rabbit)
        fox.append(new_fox)
        time.append(time[-1] + step)
    
    return np.array(time), np.array(rabbit), np.array(fox)

def grid_search_lotka(real_prey, real_predator, alpha_range, beta_range, gamma_range, delta_range):
    best_params = None
    best_mse = float('inf')
    
    for alpha, beta, gamma, delta in product(alpha_range, beta_range, gamma_range, delta_range):
        _, simulated_prey, simulated_predator = simulate_lotka_volterra(alpha, beta, gamma, delta)
        
        # Ajuster la taille des données simulées
        min_length = min(len(real_prey), len(simulated_prey))
        mse_prey = np.mean((real_prey[:min_length] - simulated_prey[:min_length]) ** 2)
        mse_predator = np.mean((real_predator[:min_length] - simulated_predator[:min_length]) ** 2)
        total_mse = mse_prey + mse_predator
        
        if total_mse < best_mse:
            best_mse = total_mse
            best_params = {
                'alpha': alpha,
                'beta': beta,
                'gamma': gamma,
                'delta': delta
            }
    
    return best_params, best_mse
    
