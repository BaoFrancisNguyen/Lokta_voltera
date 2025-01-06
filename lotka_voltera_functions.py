import numpy as np
from itertools import product

# Fonction pour résoudre les équations de Lotka-Volterra avec l'algorithme d'Euler
def lotka_volterra(alpha, beta, gamma, delta, prey_init, predator_init, dt, t_max):

    #initialisation des variables
    time_steps = int(t_max / dt)
    prey = np.zeros(time_steps)
    predator = np.zeros(time_steps)
    prey[0], predator[0] = prey_init, predator_init
    #résolution des équations de Lotka-Volterra avec l'algorithme d'Euler


    for time in range(1, time_steps):
        
        prey[time] = prey[time-1] + dt * (alpha * prey[time-1] - beta * prey[time-1] * predator[time-1])
        predator[time] = predator[time-1] + dt * (delta * prey[time-1] * predator[time-1] - gamma * predator[time-1])
    
    return prey, predator

# Fonction pour calculer la MSE
def mse(observed_prey, observed_predator, simulated_prey, simulated_predator):

    return np.mean((observed_prey - simulated_prey)**2 + (observed_predator - simulated_predator)**2)

