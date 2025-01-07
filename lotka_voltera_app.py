import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from lotka_voltera_functions import load_csv_data, calculate_mse

# Valeurs proportionnelles à la population de proies et de prédateurs
rabbit = [1]
fox = [1]
time = [0]
alpha = 2/3
beta = 4/3
gamma = 1
delta = 1
step = 0.01

# Charger les données réelles à partir du fichier CSV
csv_file_path = 'populations_lapins_renards.csv'
time_real, rabbit_real, fox_real = load_csv_data(csv_file_path)

# Simulation avec l'équation différentielle
for _ in range(0, 100_000):
    new_time_value = time[-1] + step
    new_rabbit_value = rabbit[-1] + step * (rabbit[-1] * (alpha - beta * fox[-1]))
    new_fox_value = fox[-1] + step * (fox[-1] * (delta * rabbit[-1] - gamma))

    rabbit.append(new_rabbit_value)
    fox.append(new_fox_value)
    time.append(new_time_value)

# Convertir les données simulées en numpy array
simulated_rabbit = np.array(rabbit) * 1000
simulated_fox = np.array(fox) * 1000

# Ajuster les données simulées pour qu'elles aient la même taille que les données réelles
if len(simulated_rabbit) > len(rabbit_real):
    step_ratio = len(simulated_rabbit) // len(rabbit_real)  # Ratio entre les tailles des données
    simulated_rabbit_resized = simulated_rabbit[::step_ratio][:len(rabbit_real)]
    simulated_fox_resized = simulated_fox[::step_ratio][:len(fox_real)]
else:
    simulated_rabbit_resized = simulated_rabbit[:len(rabbit_real)]
    simulated_fox_resized = simulated_fox[:len(fox_real)]

# Calculer la MSE
mse_lapin, mse_renard = calculate_mse(rabbit_real, fox_real, simulated_rabbit_resized, simulated_fox_resized)

# Afficher les résultats de la MSE
print(f"Erreur quadratique moyenne (MSE) pour les lapins : {mse_lapin:.2f}")
print(f"Erreur quadratique moyenne (MSE) pour les renards : {mse_renard:.2f}")

# Visualisation
plt.figure(figsize=(15, 6))
plt.plot(time, simulated_rabbit, label='Lapins (Simulés)', color='blue')
plt.plot(time, simulated_fox, label='Renards (Simulés)', color='red')
plt.scatter(time_real, rabbit_real, label='Lapins (Réels)', color='cyan', s=10)
plt.scatter(time_real, fox_real, label='Renards (Réels)', color='orange', s=10)
plt.xlabel('Temps')
plt.ylabel('Population')
plt.legend()
plt.title('Évolution des populations de lapins et de renards (Simulées vs Réelles)')
plt.show()

