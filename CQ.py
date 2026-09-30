import matplotlib.pyplot as plt

# Tabela 1 - Peças de 1ª linha
# Valores: quantidade em unidades; limites em mm
pecas_primeira_linha = {
    "Quantidade de Peças Requisitadas pelo Cliente": 200,
    "Limite Superior de Tolerância do Cliente": 7.51,
    "Limite Inferior de Tolerância do Cliente": 7.49,
}

# Tabela de Valores (em R$)
tabela_valores = {
    "Peça Boa Vendida": 750.95,
    "Peça Boa Refugada": -80.32,
    "Peça Ruim Refugada": -80.32,
    "Peça Ruim Vendida": -5950.78,
    "Multa por Peça Faltante": -500.00,
}

# Tabela 2 - Características das Prensas
# Valores: [Desvio Padrão (mm), Custo Diário (R$)]
prensas = {
    "Prensa 1": [0.005, 63000.00],
    "Prensa 2": [0.006, 50300.00],
    "Prensa 3": [0.009, 33800.00],
    "Prensa 4": [0.027, 20900.00],
    "Prensa 5": [0.049, 16300.00],
    "Prensa 6": [0.056, 12500.00],
    "Prensa 7": [0.070, 4300.00],
    "Prensa 8": [0.090, 2100.00],
    "Prensa 9": [0.150, 900.00],
}

# Tabela 3 - Características dos Sistemas de Medição
# Valores: [Custo Diário (R$), Correção (mm), Repetibilidade (mm)]
sistemas_medicao = {
    "SM 1": [25000.00, 0, 0.002],
    "SM 2": [20000.00, 0, 0.005],
    "SM 3": [9000.00, 0, 0.015],
    "SM 4": [8000.00, 0, 0.08],
    "SM 5": [7500.00, 0, 0.2],
}
lista = list(prensas.values())
listaSM = list(sistemas_medicao.values())

arrCustoPrensa = [lista[i][1] for i in range(len(lista))]
arrToleranciaPrensa = [lista[i][0] for i in range(len(lista))]
arrCustoSM = [listaSM[i][0] for i in range(len(listaSM))]

arrToleranciaSM = [listaSM[i][2] for i in range(len(listaSM))]
arrToleranciaSM2 = [0.015] + arrToleranciaSM
arrToleranciaPrensa2 = [0.015] + arrToleranciaPrensa

arrRotulosPrensas = list(prensas.keys())
arrRotulosPrensas2 = ["Cliente"] + arrRotulosPrensas

arrRotulosSM = list(sistemas_medicao.keys())
arrRotulosSM2 = ["Cliente"] + arrRotulosSM

zeros1 = [0]*len(arrRotulosPrensas2)
zeros2 = [0]*len(arrRotulosSM2)

print(arrToleranciaSM2)
print(zeros2)

print(len(arrRotulosSM2))
print(len(zeros2))

fig = plt.figure(figsize=(24, 20))

axs1 = fig.add_subplot(511)
axs2 = fig.add_subplot(512)
axs3 = fig.add_subplot(513)
axs4 = fig.add_subplot(514)
axs5 = fig.add_subplot(515)

axs1.bar(arrRotulosPrensas, arrCustoPrensa, color="skyblue", label="Custo por Prensa")
axs2.plot(arrRotulosPrensas, arrToleranciaPrensa, color="red", label="Tolerância por Prensa")
axs3.errorbar(arrRotulosPrensas2, zeros1, arrToleranciaPrensa2, label="Erro por Prensa")
axs4.errorbar(arrRotulosSM2, zeros2, arrToleranciaSM2, label="Erro por Sistema de Medida")
axs5.bar(arrRotulosSM, arrCustoSM, color="skyblue", label="Custo por Sistema de Medição")

plt.show()
