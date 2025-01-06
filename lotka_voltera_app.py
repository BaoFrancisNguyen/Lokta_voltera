import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

# valeurs proportionnelles à la population de proies et de prédateurs
rabbit = [1]
fox = [2]
time =[0]
alpha = 2/3
beta = 4/3
gamma = 1
delta = 1
step = 0.01

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