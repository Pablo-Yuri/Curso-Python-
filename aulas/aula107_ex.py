
# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# =====================================================================

cidades =  ['Salvador', 'Ubatuba', 'Belo Horizonte', ]
estados =  ['BA', 'SP', 'MG', 'SP']

def zipper(a,b):
    menor = a if len(a) <= len(b) else b
    maior = b if a == menor else a

    for index in range(len(menor)):
        menor[index] = (menor[index], maior[index])
    print(menor)

zipper(cidades, estados)
print('=-' * 20, '\n')

# =====================================================================

def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    # print(intervalo)
    return [
        (l1[i], l2[i])
        for i in range(intervalo)
    ]

cidades =  ['Salvador', 'Ubatuba', 'Belo Horizonte', ]
estados =  ['BA', 'SP', 'MG', 'SP']

print(zipper(cidades, estados))
print('=-' * 20, '\n')

# =====================================================================

from itertools import zip_longest

cidades =  ['Salvador', 'Ubatuba', 'Belo Horizonte', ]
estados =  ['BA', 'SP', 'MG', 'SP']

print(list(zip(cidades, estados)))
print(list(zip_longest(cidades, estados, fillvalue="Sem cidade")))

# =====================================================================
