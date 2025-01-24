import copy

from dados.produtos_modulos import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10% /
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

# print(*produtos,sep="\n")

# print("Produtos originais",*produtos,sep="\n", end="\n\n")


# Aumente os preços dos produtos a seguir em 10% /
# Gere novos_produtos por deep copy (cópia profunda)
nova_lista = copy.deepcopy(produtos)
# preco_alterado.append({'nome': 'Produto 6', 'preco': 100})

def alteracao_preco(produtos):
    for produto in produtos:
        produto["preco"] = round(produto["preco"] * 1.1, 2)
    
alteracao_preco(nova_lista)
# print("Produtos com aleração no preço 10% a mais",*nova_lista,sep="\n", end="\n\n")


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome_decrescente = sorted(
    copy.deepcopy(produtos),
    key=lambda posicao: posicao["nome"],
    reverse=True

)
# print("Produtos ordenados por nome decrescente",*produtos_ordenados_por_nome_decrescente, sep="\n", end="\n\n")


# Ordene os produtos por preco crescente (do menor para maior)
produtos_ordenados_por_preco_crescente = sorted(
    produtos,
    key=lambda posicao: posicao["preco"],
)
# print("produtos_ordenados_por_preco_crescente",*produtos_ordenados_por_preco_crescente,sep="\n", end="\n\n")

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
# Gere_produtos_ordenados_por_preco = sorted(
#     copy.deepcopy(produtos),
#     key=lambda posicao: posicao["preco"],
# )
# print("Gere produtos_ordenados_por_preco",*Gere_produtos_ordenados_por_preco,sep="\n", end="\n\n")

# print("Produtos originais",*produtos,sep="\n", end="\n\n")


# >>>>> Final

print("Produtos originais",*produtos,sep="\n", end="\n\n")

print("Produtos com aleração no preço 10% a mais",*nova_lista,sep="\n", end="\n\n")

print("Produtos ordenados por nome decrescente",*produtos_ordenados_por_nome_decrescente, sep="\n", end="\n\n")

print("produtos_ordenados_por_preco_crescente",*produtos_ordenados_por_preco_crescente,sep="\n", end="\n\n")

print("Produtos originais",*produtos,sep="\n", end="\n\n")
