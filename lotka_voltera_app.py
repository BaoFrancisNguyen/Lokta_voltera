import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from lotka_voltera_functions import load_csv_data, calculate_mse


# valeurs proportionnelles à la population de proies et de prédateurs
rabbit = [1]
fox = [2]
time =[0]
alpha = 2/3
beta = 4/3
gamma = 1
delta = 1
step = 0.01

# Charger les données réelles à partir du fichier CSV
csv_file_path = 'populations_lapins_renards.csv'  # Remplacez par le chemin correct si nécessaire
time_real, prey_real, predator_real = load_csv_data(csv_file_path)

### Comparer les données simulées aux données réelles
# Convertir les données simulées en numpy array
simulated_prey = np.array(rabbit) * 1000
simulated_predator = np.array(fox) * 1000  

#approximation of the differential equation
for _ in range(0, 100_000):
    new_time_value = time[-1]
    new_rabbit_value = (rabbit[-1] * (alpha - beta * fox[-1])) * step + rabbit[-1]
    new_fox_value = (fox[-1] * (delta * rabbit[-1] - gamma)) * step + fox[-1]

    rabbit.append(new_rabbit_value)
    fox.append(new_fox_value)
    time.append(new_time_value + step)

lapin = np.array(rabbit)
renard = np.array(fox)

lapin *= 1000
renard *= 1000


plt.figure(figsize=(15, 6))
plt.plot(time, rabbit, label='Rabbit', color='blue')
plt.plot(time, fox, label='Fox', color='red')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('Evolution of Population of Rabbit and Fox')
plt.show()