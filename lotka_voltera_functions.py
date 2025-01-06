import numpy as np
from itertools import product

# Fonction pour résoudre les équations de Lotka-Volterra avec l'algorithme d'Euler
def lotka_volterra(alpha, beta, gamma, delta, prey_init, predator_init, dt, t_max):
    time_steps = int(t_max / dt)
    prey = np.zeros(time_steps)
    predator = np.zeros(time_steps)
    prey[0], predator[0] = prey_init, predator_init

    for time in range(1, time_steps):
        prey[time] = prey[time-1] + dt * (alpha * prey[time-1] - beta * prey[time-1] * predator[time-1])
        predator[time] = predator[time-1] + dt * (delta * prey[time-1] * predator[time-1] - gamma * predator[time-1])
    
    return prey, predator