import matplotlib.pyplot as plt
import numpy as np
from itertools import product 
from lotka_voltera_functions import load_csv_data, calculate_mse, simulate_lotka_volterra, grid_search_lotka

# Paramètres initiaux du modèle Lotka-Volterra
alpha = 2/3
beta = 4/3
gamma = 1
delta = 1
step = 0.01
iterations = 100_000

# Chargement des données réelles
csv_file_path = 'populations_lapins_renards.csv'
time_real, rabbit_real, fox_real = load_csv_data(csv_file_path)

# Simulation avec les paramètres initiaux
time, rabbit, fox = simulate_lotka_volterra(alpha, beta, gamma, delta, step, iterations)

# Redimensionner les données simulées pour correspondre aux données réelles
simulated_rabbit = np.array(rabbit[:len(rabbit_real)])
simulated_fox = np.array(fox[:len(fox_real)])

# Calcul de l'erreur MSE
mse_rabbit, mse_fox = calculate_mse(rabbit_real, fox_real, simulated_rabbit, simulated_fox)
print(f"MSE Lapins : {mse_rabbit:.2f}")
print(f"MSE Renards : {mse_fox:.2f}")

# Optimisation des paramètres avec Grid Search
alpha_range = np.linspace(0.1, 1.0, 5)
beta_range = np.linspace(0.1, 1.0, 5)
gamma_range = np.linspace(0.1, 1.0, 5)
delta_range = np.linspace(0.1, 1.0, 5)

best_params, best_mse = grid_search_lotka(rabbit_real, fox_real, alpha_range, beta_range, gamma_range, delta_range)
print(f"Meilleurs paramètres : {best_params} avec MSE : {best_mse:.2f}")

# Simulation avec les meilleurs paramètres optimisés
time_opt, rabbit_opt, fox_opt = simulate_lotka_volterra(best_params['alpha'], best_params['beta'], best_params['gamma'], best_params['delta'], step, iterations)

# Visualisation des résultats
plt.figure(figsize=(15, 6))
plt.plot(time_opt, rabbit_opt, label='Lapins (Optimisés)', color='blue')
plt.plot(time_opt, fox_opt, label='Renards (Optimisés)', color='red')
plt.scatter(time_real, rabbit_real, label='Lapins (Réels)', color='cyan', s=10)
plt.scatter(time_real, fox_real, label='Renards (Réels)', color='orange', s=10)
plt.xlabel('Temps')
plt.ylabel('Population')
plt.legend()
plt.title('Évolution des populations de lapins et de renards (Optimisées vs Réelles)')
plt.show()

#observation: les résultats données simulées et les données réelles ne sont pas à la même échelle



