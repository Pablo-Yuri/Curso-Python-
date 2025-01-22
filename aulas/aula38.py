qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_colunas:
    coluna = 1
    print(linha, end=" - ")
    while coluna <= qtd_colunas:
        print(f"{coluna=}", end=' ')
        coluna += 1
    print('')
    linha += 1