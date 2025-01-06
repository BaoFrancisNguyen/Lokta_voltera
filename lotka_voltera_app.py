import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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