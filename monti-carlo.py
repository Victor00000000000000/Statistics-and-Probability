from random import random
import matplotlib.pyplot as plt

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

def gaussiana_creater(arrValues):
	gauss_dict = dict()
	for i in range(len(arrValues)):
		if arrValues[i] in gauss_dict.values():
			gauss_dict[i] += 1
		else:
			gauss_dict[i] = 1

	return gauss_dict

def monti_carlo_indiMed(G, arrVar, arrIncertezas, quantidade_experimentos):
	arrVarRandomicos = [0*len(arrVar)]
	arrResultadoRandomico = [0*quantidade_experimentos]
	for i in range(quantidade_experimentos):
		arrVarRandomicos[i] = random(arrVar[i]-arrIncertezas[i], arrVar[i]+arrIncertezas[i])
		arrResultadoRandomico[i] = G(*arrVarRandomicos)
	mergeSort(arrResultadoRandomico, 0, len(arrResultadoRandomico))
	gauss_distribut = gaussiana_creater(arrResultadoRandomico)
	return gauss_distribut

def G(a,b):
	return a*b

if __name__ == "__main__":
	
	arrVar=[25.3, 56.5]
	arrIncertezasPadrao=[0.6, 0.8]
	quantidade_experimentos=100
	gauss = monti_carlo_indiMed(arrVar, arrIncertezasPadrao, quantidade_experimentos)
	plt.figure(1,2)
	plt.plot(gauss.keys(), gauss.values())
    #plt.show()
    #plt.savefig("monti-carlo-result.png")
## RESPOSTA: (1429 +- 39)mm
