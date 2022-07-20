import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.integrate import quad
from math import factorial

X = [1, 2, 3, 4]

P = [0.3, 0.4, 0.2, 0.1]

esp = np.dot(X, P)

print("Valor esperado:", np.round(esp, 2))

var = np.round(np.dot(np.power(X, 2), P) - np.power(esp, 2), 2)

print("Variância:     ", var)


def f1(x):
    return x / (x * x) / 3


esp, err1 = quad(f1, -1, 2)

print("Valor esperado: ", esp)
print("Erro da Integral: ", err1)


def f2(x):
    return (x * x) * (x * x) / 3


esp_2, err2 = quad(f2, -1, 2)

var = esp_2 - esp * esp

print("Variância: ", var)
print("Erro da Integral: ", err2)

print('=' * 50)

print(pd.Series(np.random.binomial(1, 0.8, 100000)).value_counts(normalize=True))
print('-' * 15)
print(pd.Series(np.random.binomial(3, 0.8, 100000)).value_counts(normalize=True))

print('=' * 50)


def binomial(n, p, k):
    c = (factorial(n) / (factorial(n - k) * factorial(k)))
    return c * np.power(p, k) * np.power(1 - p, n - k)


n = 5

k = 2

p = 8 / 12

print("A probabilidade será: ", np.round(binomial(n, p, k), 4))

print('-' * 15)

n = 5

p = 4 / 12

prop = 0

for k in range(3, 6):
    prop += binomial(n, p, k)

print("A probabilidade será:", np.round(prop, 4))
