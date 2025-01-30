produtos = {
    'nome1': 'Produto 5', 'preco': 10.00,
    'nome2': 'Produto 1', 'preco': 22.32,
    'nome3': 'Produto 3', 'preco': 10.11,
    'nome4': 'Produto 2', 'preco': 105.87,
    'nome5': 'Produto 4', 'preco': 69.90
}
novo = [["ajuste", "pablo"]]
produtos.update(novo)
print(produtos)


nome = "ajuste"
produto = produtos.get(nome) if produtos.get(nome) is not None else "produto não encontrado"
print(produto)