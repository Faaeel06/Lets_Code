import random
import matplotlib.pyplot as plt
import math


def confere_interior(dentro):
    x, y = random.random(), random.random()
    raio = 0.5

    if ((x - raio) ** 2) + ((y - raio) ** 2) <= raio ** 2:
        dentro += 1

    return dentro


def cal_aprox_Pi(N, step=10):
    dentro = 0

    pi_aproxs = {}

    for i in range(N):
        dentro = confere_interior(dentro)

        if i % step == 0 and i != 0:
            pi_aproxs[i] = 4 * dentro / i

    return pi_aproxs


pi_aproxs = cal_aprox_Pi(100000)

plt.figure(figsize=(12, 5))

plt.plot(list(pi_aproxs.keys()), list(pi_aproxs.values()), label="proxy de $\pi$")

plt.axhline(y=math.pi, color="red", label="$\pi$ real")

plt.legend()
plt.show()
