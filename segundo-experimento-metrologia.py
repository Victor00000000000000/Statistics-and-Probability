import monteCarlo as mC
quantidade_experimentos = 10000000

In = 1654.667
I300 = 293.800
I150 = 198.200

UIn = 2.900
UI300 = 1.785
UI150 = 1.701

def N(In, I300, I150):
    Mp = (I300 - I150)/150
    Mg = ((I300 + I150) - 450*Mp)/2
    N = (In - Mg)/Mp
    return N

arrVar = [In, I300, I150]
arrIncertezasExpandida = [UIn, UI300, UI150]

mC.return_gaussiana(N, arrVar, arrIncertezasExpandida, quantidade_experimentos)

'''
Média: 2436.73
Desvio Padrão: 57.37
Medida: (2436.73 +- 114.74)
Intervalo: [2379.36, 2494.1]
'''

'''
Média: 2436.72
Desvio Padrão: 57.46
Medida: (2436.72 +- 114.92)
Intervalo: [2379.26, 2494.19]
'''