import numpy as np
import pandas as pd
from itertools import product


#fonction pour charger les données réelles depuis un fichier CSV
def load_csv_data(file_path):
    try:
        data = pd.read_csv(file_path)
        
        #vérification des colonnes
        if 'date' in data.columns and 'lapin' in data.columns and 'renard' in data.columns:
            return data['date'].values, data['lapin'].values, data['renard'].values
        else:
            raise ValueError("Le fichier CSV doit contenir les colonnes 'date', 'lapin', et 'renard'.")
    except Exception as e:
        raise IOError(f"Erreur lors du chargement du fichier CSV : {e}")

#fonction pour calculer la MSE
def calculate_mse(real_lapin, real_renard, simulated_lapin, simulated_renard):

    #Mean Squared Error (Erreur Quadratique Moyenne)

    #But : Mesurer l'écart entre les données réelles et celles simulées
    #Comment : On calcule la Moyenne des Carrés des Écarts (MSE) pour les lapins et les renards
    #Pourquoi : Plus la MSE est basse, plus la simulation est proche de la réalité

    #Pour chaque point de données, on calcule la différence entre la valeur réelle et la valeur simulée.
    #Exemple pour les lapins : erreur = real_lapin - simulated_lapin
    #On élève cette différence au carré pour éviter les annulations positives et négatives (erreur au carré)
    # pour chaque temps, on calcule la moyenne des erreurs au carré pour obtenir la MSE
    # exemple T0: erreur = (real_lapin[0] - simulated_lapin[0]) ** 2
    # exemple T1: erreur = (real_lapin[1] - simulated_lapin[1]) ** 2
    # MSE = (erreur_T0 + erreur_T1 + ... + erreur_Tn) / n
    #
    # On fait la même chose pour les renards

    try:
        mse_lapin = np.mean((real_lapin - simulated_lapin) ** 2)
        mse_renard = np.mean((real_renard - simulated_renard) ** 2)
        return mse_lapin, mse_renard
    except Exception as e:
        raise ValueError(f"Erreur dans le calcul du MSE : {e}")
    
#fonction de simulation de lotka volterra
def simulate_lotka_volterra(alpha, beta, gamma, delta, step=0.01, iterations=100_000):

    #But : Simuler l'évolution des populations de lapins et de renards
    #Comment : Utilisation des équations de Lotka-Volterra avec des paramètres alpha, beta, gamma et delta
    #Pourquoi : Pour comprendre les interactions entre les deux populations

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
    #But : Trouver les meilleurs paramètres qui minimisent l'erreur
    #Comment :
        #On teste plusieurs combinaisons de paramètres grâce à product
        #Pour chaque combinaison, on simule les populations et on calcule la MSE
        #On garde les paramètres qui donnent la plus petite MSE
        #Pourquoi : Pour obtenir des résultats plus proches des données réelles
    best_params = None
    best_mse = float('inf')
    
    for alpha, beta, gamma, delta in product(alpha_range, beta_range, gamma_range, delta_range):
        _, simulated_prey, simulated_predator = simulate_lotka_volterra(alpha, beta, gamma, delta)
        
        #ajustement de la taille des données simulées
        min_length = min(len(real_prey), len(simulated_prey))
        mse_prey = np.mean((real_prey[:min_length] - simulated_prey[:min_length]) ** 2)
        mse_predator = np.mean((real_predator[:min_length] - simulated_predator[:min_length]) ** 2)
        total_mse = mse_prey + mse_predator
        #mise à jour des meilleurs paramètres
        if total_mse < best_mse:
            best_mse = total_mse
            best_params = {
                'alpha': alpha,
                'beta': beta,
                'gamma': gamma,
                'delta': delta
            }
    
    return best_params, best_mse
    
