import sympy as smp
import propagErro as pE

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

RM = pE.prop_erro_MedIndireta(arrRB, arrIncertezasExpandida, N, arrVar)

print(RM)