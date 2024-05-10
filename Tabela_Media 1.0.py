import pandas as pd
from tabulate import tabulate 
import matplotlib.pyplot as plt 
import numpy as np

S1= "Sudeste/Centro-Oeste"
S2= 'Sul'
S3= 'Norte'
S4= 'Nordeste'
E1= 'Verão'
E2= 'Outono'
E3= 'Inverno'
E4= 'Primavera'
A1= '2021'
A2= '2022'
A3= '2023'


# Dados para as colunas
dados = {
    'Subsistema': [S1,S1,S1,S1,S1,S1,S1,S1,S1,S1,S1,S1,
                   S2,S2,S2,S2,S2,S2,S2,S2,S2,S2,S2,S2,
                    S3,S3,S3,S3,S3,S3,S3,S3,S3,S3,S3,S3,
                     S4,S4,S4,S4,S4,S4,S4,S4,S4,S4,S4,S4 ],
                   
    'Estação do Ano': [E1,E2,E3,E4,E1,E2,E3,E4,E1,E2,E3,E4,
                       E1,E2,E3,E4,E1,E2,E3,E4,E1,E2,E3,E4,
                       E1,E2,E3,E4,E1,E2,E3,E4,E1,E2,E3,E4,
                       E1,E2,E3,E4,E1,E2,E3,E4,E1,E2,E3,E4],

    'Ano': [A1,A1,A1,A1,A2,A2,A2,A2,A3,A3,A3,A3,
            A1,A1,A1,A1,A2,A2,A2,A2,A3,A3,A3,A3,
            A1,A1,A1,A1,A2,A2,A2,A2,A3,A3,A3,A3,
            A1,A1,A1,A1,A2,A2,A2,A2,A3,A3,A3,A3,],

    'Média de Consumo':[42562.756545833334, 39872.74110215053, 38848.84931557018,   40452.09789999999,
                        43510.91444322917,  40616.385525985665,39137.430765789475,  40750.74446041667,
                        43385.4671140625,   40852.60497244623, 40463.71259188597,   45880.1984175926,

                        13227.983521354168, 11955.562921729392, 11763.972808530702, 12561.988056087963,
                        14171.260561979167, 11925.154492741936, 11781.199804495614, 12436.693787430557,
                        14219.718285156248, 12478.04931953405,  12204.117812894736, 13477.83875534722,

                        5735.831407395834,  6022.635406070788,  6178.913368026316,  6225.505194837963,
                        5871.4342468489585, 6002.494247871864,  6601.526118574561,  6831.937123379629,
                        6599.032256067708,  6995.523277710574,  7421.11336502193,   7660.687379027778,

                        11845.920904687498, 11193.942317652329, 11414.872815899123,  12260.237599421296,
                        11846.732041927084, 11303.300609543012, 11065.134667280701,  11985.366333333333,
                        12292.090574218751, 11786.054534386201, 11907.132225986841,  13482.080915162036,
                        ]
}


# Criar DataFrame
total = pd.DataFrame(dados)

# Encontrar o índice do maior valor na coluna
indice_maior_consumo = total['Média de Consumo'].idxmax()
indice_menor_consumo = total['Média de Consumo'].idxmin()

# Obter a linha completa com o maior valor
linha_maior_consumo = total.loc[indice_maior_consumo]
linha_menor_consumo = total.loc[indice_menor_consumo]

# Criar um novo DataFrame com a linha do maior valor
novo_dfmax = pd.DataFrame([linha_maior_consumo], columns=total.columns)
novo_dfmin = pd.DataFrame([linha_menor_consumo], columns=total.columns)

table = tabulate(total, headers='keys', tablefmt='fancy_grid')

# Exibir a linha completa
print("Maior Média de Consumo:")
print(novo_dfmax) 
print()
print("Menor Média de Consumo:")
print(novo_dfmin)



# Configurar a figura matplotlib
plt.figure(figsize=(12, 6.5))
plt.text(0.21, -2.50, table, {'fontsize': 9}, fontfamily='monospace')
plt.axis('off')


# Mostrar a figura
plt.show()


total.to_excel('Tabela_Consumo_Energia.xlsx', index=False)

