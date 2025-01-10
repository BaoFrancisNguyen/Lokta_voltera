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


    #Mean Squared Error (Erreur Quadratique Moyenne)

    #But : Mesurer l'écart entre les données réelles et celles simulées
    #Comment : On calcule la Moyenne des Carrés des Écarts (MSE) pour les lapins et les renards
    #Pourquoi : Plus la MSE est basse, plus la simulation est proche de la réalité

    #Pour chaque point de données, on calcule la différence entre la valeur réelle et la valeur simulée.
    #Exemple pour les lapins : erreur = real_lapin - simulated_lapin
    #On élève cette différence au carré pour éviter les annulations positives et négatives (erreur au carré)
    # pour chaque temps, on calcule la moyenne des erreurs au carré pour obtenir la MSE
    # exemple T0: erreur = (real_lapin[0] - simulated_lapin[0]) ** 244
    # exemple T1: erreur = (real_lapin[1] - simulated_lapin[1]) ** 2
    # MSE = (erreur_T0 + erreur_T1 + ... + erreur_Tn) / n
    #
    # On fait la même chose pour les renards
    #simulated_lapin = np.array(simulated_lapin)*1000
    #simulated_renard = np.array(simulated_renard)*1000
    #print(real_lapin)
    #print(simulated_lapin)
    #print(real_renard)
    #print(simulated_renard)
    
    # Fonction pour calculer la MSE avec mise à l'échelle automatique
def calculate_mse(real_lapin, real_renard, simulated_lapin, simulated_renard):
    try:
        # Calcul du facteur de mise à l'échelle
        scale_factor_lapin = np.max(real_lapin) / np.max(simulated_lapin)
        scale_factor_renard = np.max(real_renard) / np.max(simulated_renard)
        
        # Mise à l'échelle des données simulées
        simulated_lapin_scaled = simulated_lapin * scale_factor_lapin
        simulated_renard_scaled = simulated_renard * scale_factor_renard
        
        # Calcul de la MSE
        mse_lapin = np.mean((real_lapin - simulated_lapin_scaled) ** 2)
        mse_renard = np.mean((real_renard - simulated_renard_scaled) ** 2)
        
        return mse_lapin, mse_renard
    except Exception as e:
        raise ValueError(f"Erreur dans le calcul du MSE : {e}")
    
#fonction de simulation de lotka volterra
def simulate_lotka_volterra(alpha, beta, gamma, delta, step=0.01, iterations=100_000):

    #But : Simuler l'évolution des populations de lapins et de renards
    #Comment : Utilisation des équations de Lotka-Volterra avec des paramètres alpha, beta, gamma et delta
    #Pourquoi : Pour comprendre les interactions entre les deux populations

    # on pose les conditions de cauchy
    rabbit = [1]
    fox = [2]
    time = [0]
    
    for _ in range(iterations):

        # fonctions analytiques transformées en équations discrètes / méthode d'Euler
        new_rabbit = (rabbit[-1] * (alpha - beta * fox[-1])) * step + rabbit[-1]
        new_fox = (fox[-1] * (delta * rabbit[-1] - gamma)) * step + fox[-1]
        
        rabbit.append(new_rabbit)
        fox.append(new_fox)
        time.append(time[-1] + step)
    
    return np.array(time), np.array(rabbit), np.array(fox)

def grid_search_lotka(real_prey, real_predator, alpha_range, beta_range, gamma_range, delta_range):

    #Le Grid Search est une méthode de recherche systématique qui permet de trouver les meilleurs paramètres pour un modèle.

    #Dans le cadre du modèle Lotka-Volterra, le Grid Search permet de trouver les meilleures valeurs pour les paramètres suivants :

    #alpha : Taux de croissance des lapins (proies)
    #beta : Taux de prédation des lapins par les renards
    #gamma: Taux de mortalité naturelle des renards
    #delta : Taux de croissance des renards grâce à la chasse des lapins

    #But : Trouver les meilleurs paramètres qui minimisent l'erreur
    #Avantage : Teste toutes les combinaisons sans oublier aucune possibilité
    #Limite : Peut être lent si les plages de valeurs sont très larges

    #Comment :
        #On teste plusieurs combinaisons de paramètres grâce à product
        #Pour chaque combinaison, on simule les populations et on calcule la MSE
        #On garde les paramètres qui donnent la plus petite MSE
        #Pourquoi : Pour obtenir des résultats plus proches des données réelles

# def grid_search_lotka():
    #alphas = numpy.linspace(0, 1, 100)
    #betas = numpy.linspace(0, 1, 100)
    #gammas = numpy.linspace(0, 1, 100)
    #deltas = numpy.linspace(0, 1, 100)

    #best_alpha, best_beta, best_gamma, best_delta = None, None, None, None
    #best_rmse = float('inf') # initialisation de la RMSE à l'infini

    #for alpha, beta, gamma, delta in intertools.product(alphas, betas, gammas, deltas):
     #time, rabbit, fox = simulate_lotka_volterra(alpha, beta, gamma, delta)
        #rmse_rabbit = rmse(rabbit, real_rabbit)
        #rmse_fox = rmse(fox, real_fox)
        #total_rmse = rmse_rabbit + rmse_fox
        #if total_rmse < best_rmse:
            #best_rmse = total_rmse
            #best_alpha, best_beta, best_gamma, best_delta = alpha, beta, gamma, delta

    #return best_alpha, best_beta, best_gamma, best_delta, best_rmse


    best_params = None
    best_mse = float('inf')

    #La fonction product() génère toutes les combinaisons possibles des paramètres
    
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



# rmse = np.sqrt(mse)
# rmse_rabbit = np.sqrt(mse_rabbit)
# rmse_fox = np.sqrt(mse_fox)

# print(f"RMSE Lapins : {rmse_rabbit:.2f}")
# print(f"RMSE Renards : {rmse_fox:.2f}")
