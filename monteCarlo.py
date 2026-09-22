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
    print(f"Medida: ({round(media, 2)} +- {round(t_student(quantidade_experimentos-1)*desvio_padrao, 2)})") # Como são muitos experimentos t é aproximadamente 2.
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

def t_student(graus_liberdade):
    t_student_95_45 = {
    1: 13.968, 2: 4.527, 3: 3.307, 4: 2.869, 5: 2.649,
    6: 2.517, 7: 2.429, 8: 2.366, 9: 2.320, 10: 2.284,
    11: 2.255, 12: 2.231, 13: 2.212, 14: 2.195, 15: 2.181,
    16: 2.169, 17: 2.158, 18: 2.149, 19: 2.140, 20: 2.133,
    25: 2.105, 30: 2.087
    }
    if graus_liberdade in t_student_95_45.keys():
        return t_student_95_45[graus_liberdade]
    else:
         if graus_liberdade > 30:
              return 2
         elif 20 < graus_liberdade < 30:
              raise IndexError

def G(a,b):
	return a*b

'''
if __name__ == "__main__":
    arrVar=[25.3, 56.5]
    arrIncertezasPadrao=[0.6, 0.8]
    quantidade_experimentos=1000000
    return_gaussiana(G, arrVar, arrIncertezasPadrao, quantidade_experimentos)

    plt.show()
        #plt.savefig("monti-carlo-result.png")
        ## RESPOSTA: (1429 +- 39)mm
'''