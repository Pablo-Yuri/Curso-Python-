

# Considerando duas listas de inteiros ou floats (lista A e lista B)
# Some os valores nas listas retornando uma nova lista com os valores somados:
# Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
# menor.
# Exemplo:
# lista_a     = [1, 2, 3, 4, 5, 6, 7]
# lista_b     = [1, 2, 3, 4]

def somar_listas(l1,l2):
    intervalo = min(len(l1), len(l2))
    soma = [
        # (f"({l1[i]} + {l2[i]} = {l1[i] + l2[i]})")
        l1[i] + l2[i]
        for i in range(intervalo)
    ]
    return soma

lista_1     = [1, 2, 3, 4, 5, 6, 7]
lista_2     = [1, 2, 3, 4]
print(somar_listas(lista_1, lista_2), end="\n\n")

# =====================================================================
from itertools import zip_longest

lista_1     = [1, 2, 3, 4, 5, 6, 7]
lista_2     = [1, 2, 3, 4]

print(list(zip_longest(lista_1, lista_2, 
                       fillvalue="Sem dupla para a soma")), end='\n\n')

# montar_lista_soma = zip(lista_1, lista_2)
# print(montar_lista_soma)

def somar_listas(l1, l2):
    montar_lista_soma = zip(lista_1, lista_2)
    print(montar_lista_soma)
    soma = []
    for valores in montar_lista_soma:
        # print(valores)
        soma.append(valores[0] + valores[1])
    return soma

print(somar_listas(lista_1, lista_2))
