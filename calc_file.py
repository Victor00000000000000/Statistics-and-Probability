from numpy.random import normal
import matplotlib.pyplot as plt

def production_pieces(n_pecas, prensa_tolerancia, valor_central):
    arrPecas = [0]*n_pecas
    for i in range(n_pecas):
        arrPecas[i] = normal(valor_central, prensa_tolerancia)

    return arrPecas

def MedindoPecas(arr_pecas, SM_tolerancia, prensa_tolerancia, valor_central):
    pass


def calc_lucros():
    pass


if __name__ == "__main__":
    pecas = production_pieces(1000, 0.015, 7.505)
    plt.hist(pecas, bins=20)
    plt.show()
