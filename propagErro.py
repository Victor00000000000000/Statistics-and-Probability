import sympy as smp
import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt

def prop_erro_MedIndireta(arrRB, arrU, G, arrVar):
    #In, I300, I150 = smp.symbols('In I300 I150')

    a = arrVar[0]
    b = arrVar[1]
    c = arrVar[2]

    ma = arrRB[0]
    mb = arrRB[1]
    mc = arrRB[2]

    # Declaração simbólica das funções
    G_lamb = smp.lambdify([a, b, c], G)

    # Declaração simbólica das derivadas
    G_a = smp.diff(G, a)
    G_b = smp.diff(G, b)
    G_c = smp.diff(G, c)

    # Declaração das Incertezas (Valores de hold ainda)
    U_a = arrU[0]
    U_b = arrU[1]
    U_c = arrU[2]

    # Declaração Produto (Derivada em relação a v) x (Incerteza Padrão de v)
    produtoGaxU_a = G_a*U_a
    produtoGbxU_b = G_b*U_b
    produtoGcxU_c = G_c*U_c

    # Declaração dos function object de cada função simbólica. É como se a partir de cada função simbólica, fosse criada uma função com o "def".
    produtoGaxU_a_lamb = smp.lambdify(produtoGaxU_a.free_symbols, produtoGaxU_a)
    produtoGbxU_b_lamb = smp.lambdify(produtoGbxU_b.free_symbols, produtoGbxU_b)
    produtoGcxU_c_lamb = smp.lambdify(produtoGcxU_c.free_symbols, produtoGcxU_c)

    incertezaExpandidaProp = sqrt(produtoGaxU_a_lamb(mb, mc)**2 + produtoGbxU_b_lamb(ma, mb, mc)**2 + produtoGcxU_c_lamb(ma, mb, mc)**2)

    RB = round(G_lamb(ma, mb, mc), 2)
    U = round(float(incertezaExpandidaProp), 3)

    return [RB, U]
