import sympy as smp
import propagErro as pE
'''
In_m = 1654.667
I300_m = 293.800
I150_m = 198.200

UIn = 2.878
UI300 = 1.735
UI150 = 1.647

arrRB = [In_m, I300_m, I150_m]
arrIncertezasExpandida = [UIn, UI300, UI150]

In, I300, I150 = smp.symbols('In I300 I150')
N = (In - (((I300 + I150) - 450*((I300 - I150)/150))/2))/((I300 - I150)/150)

arrVar = [In, I300, I150]
'''

Iepsilon = 31.5
IE = 205000
Ib = 31.945
Ih = 3.1115
Ig = 9.80665
IL = 165.04
Ix = 5.646

Uepsilon = 1.69864681536019
UE = 5000
Ub = 0.242525304659122
Uh = 0.44587062168526
Ug = 0.001
UL = 0.977297948439992
Ux = 0.210620681226543

arrRB = [Iepsilon, IE, Ib, Ih, Ig, IL, Ix]
arrIncertezasExpandida = [Uepsilon, UE, Ub, Uh, Ug, UL, Ux]

epsilon, E, b, h, g, L, x = smp.symbols('epsilon E b h g L x')
m = (epsilon*E*b*(h**2))/(6*g*(L-x)*1000)
arrVar = [epsilon, E, b, h, g, L, x]

RM = pE.prop_erro_MedIndireta(arrRB, arrIncertezasExpandida, m, arrVar)

print(RM)