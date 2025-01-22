"""
Iterando strings com while
"""
#       012345678910
#nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


nome = input("Digite algo: ")
qtd_letra = len(nome)
novo_nome = ''

contador = 0
while contador < qtd_letra:
    #print(f"_{nome[contador]}_", end=' ')
    letra = f"_{nome[contador]}"
    novo_nome = novo_nome + letra
    contador += 1

novo_nome = novo_nome + "_"
print(novo_nome)

