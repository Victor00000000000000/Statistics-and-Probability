import sympy as smp
import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt

In, I300, I150 = smp.symbols('In I300 I150')

# Declaração simbólica das funções
Mp = (I300 - I150)/150
Mg = ((I300 + I150) - 450*Mp)/2
N = (In - Mg)/Mp

# Declaração simbólica das derivadas
N_In = smp.diff(N, In)
N_I300 = smp.diff(N, I300)
N_I150 = smp.diff(N, I150)

# Declaração das Incertezas (Valores de hold ainda)
u_In = 1
u_I300 = 2
u_I150 = 3 

# Declaração Produto (Derivada em relação a v) x (Incerteza Padrão de v)
produtoNu_In = N_In*u_In
produtoNu_I300 = N_I300*u_I300
produtoNu_I150 = N_I150*u_I150

# Declaração dos function object de cada função simbólica. É como se a partir de cada função simbólica, fosse criada uma função com o "def".
produtoNu_In_lamb = smp.lambdify([I150, I300], produtoNu_In)
produtoNu_I300_lamb = smp.lambdify([I150, I300, In], produtoNu_I300)
produtoNu_I150_lamb = smp.lambdify([I150, I300, In], produtoNu_I150)


print(produtoNu_In)
print(produtoNu_I300)
print(produtoNu_I150)

print(produtoNu_In_lamb(1, 2))
print(produtoNu_I300_lamb(1, 2, 1))
print(produtoNu_I150_lamb(1, 2, 1))
