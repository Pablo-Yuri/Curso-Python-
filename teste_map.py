produtos = [
    {'nome': 'Pablo', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# print(*list(map(
#     lambda x: x,
#     produtos
#     )), sep="\n")

def alteracao(produto):
    return {
            **produto,
            "preco": round(produto["preco"] * 1.1, 2)
    }


# produtos = [1,2,43,4,5,6]
modificacao1 = list(map(
    alteracao, 
    produtos))


print(*modificacao1, sep="\n")




def alterar_nome(produto):
    return {
        **produto,
        "nome": produto["nome"]}

modificacao2 = list(map(
    alterar_nome,
    produtos
))


print()
print(*modificacao2, sep="\n")

