import monteCarlo as mC
import sympy as smp

quantidade_experimentos = 100000

'''
In = 1654.667
I300 = 293.800
I150 = 198.200

UIn = 2.878
UI300 = 1.735
UI150 = 1.647

def N(In, I300, I150):
    Mp = (I300 - I150)/150
    Mg = ((I300 + I150) - 450*Mp)/2
    N = (In - Mg)/Mp
    return N

arrVar = [In, I300, I150]
arrIncertezasExpandida = [UIn, UI300, UI150]
'''

epsilon = 31.5
E = 205000
b = 31.945
h = 3.1115
g = 9.80665
L = 165.04
x = 5.646

Uepsilon = 1.69864681536019
UE = 5000
Ub = 0.242525304659122
Uh = 0.44587062168526
Ug = 0.001
UL = 0.977297948439992
Ux = 0.210620681226543

def m(epsilon, E, b, h, g, L, x):

    m = (epsilon*E*b*(h**2))/(6*g*(L-x)*1000)

    return m

arrVar = [epsilon, E, b, h, g, L, x]
arrIncertezasExpandida = [Uepsilon, UE, Ub, Uh, Ug, UL, Ux]

mC.return_gaussiana(m, arrVar, arrIncertezasExpandida, quantidade_experimentos)

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