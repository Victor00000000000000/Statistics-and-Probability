from random import random
from numpy.random import normal
import matplotlib.pyplot as plt
import numpy as np
from math import trunc, ceil

def return_gaussiana(G, arrVar, arrIncertezas, quantidade_experimentos):
    generatedG= monti_carlo_indiMed(G, arrVar, arrIncertezas, quantidade_experimentos)
     
    media = np.mean(generatedG)
    desvio_padrao = np.std(generatedG)
    #xmed = (max(generatedG) + min(generatedG))/2
     
    fig = plt.figure(figsize=(6,5))
    plt.hist(generatedG, bins=400)
     
    plt.axvline(media, 0, color="red", linestyle="-")
    plt.axvline(media + desvio_padrao, 0, color="red", linestyle="-")
    plt.axvline(media - desvio_padrao, 0, color="red", linestyle="-")
    plt.axvline(media + 2*desvio_padrao, 0, color="red", linestyle="-")
    plt.axvline(media - 2*desvio_padrao, 0, color="red", linestyle="-")
 
    print("Média:", round(media, 2))
    print("Desvio Padrão:", round(desvio_padrao, 2))
    print(f"Medida: ({round(media, 2)} +- {round(desvio_padrao, 2)})") # Como são muitos experimentos t é aproximadamente 2.
    print(f"Intervalo: [{round(media - desvio_padrao, 2)}, {round(media + desvio_padrao, 2)}]")
    plt.show()

def monti_carlo_indiMed(G, arrVar, arrIncertezas, quantidade_experimentos):

    # Criação de arrays para os valores gerados
    arrVarRandomicos = [0]*len(arrVar)
    arrResultadoRandomico = [0]*quantidade_experimentos

    for j in range(quantidade_experimentos):
        for i in range(len(arrVar)):
            arrVarRandomicos[i] = normal(arrVar[i], arrIncertezas[i])
        arrResultadoRandomico[j] = G(*arrVarRandomicos)
    return arrResultadoRandomico

def G(a,b):
	return a*b

if __name__ == "__main__":
    arrVar=[25.3, 56.5]
    arrIncertezasPadrao=[0.6, 0.8]
    quantidade_experimentos=1000000
    return_gaussiana(G, arrVar, arrIncertezasPadrao, quantidade_experimentos)

    plt.show()
        #plt.savefig("monti-carlo-result.png")
        ## RESPOSTA: (1429 +- 39)mm
