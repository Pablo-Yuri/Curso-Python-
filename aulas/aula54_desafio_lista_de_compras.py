"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista_produtos = []

while True:
    opcao = input("Escolha uma das opções abaixo\n[i]nseir, [a]pagar ou [l]istar: ").lower()
    opcao = opcao[0]
    opcoes_validas = 'ial'

    if opcao in opcoes_validas:
        # 
        if opcao == "i":
            produto = input("Digite o nome do produto: ")
            lista_produtos.append(produto)
        elif opcao == "a":
            try:
                produto = input("Digite o id do produto que deseja apagar: ")
                lista_produtos.pop(int(produto))
            except ValueError:
                print("Digite um número inteiro")
            except IndexError:
                print("Digite um id válido")
            except Exception:
                print("Erro desconhecido")
        elif opcao == "l":
            os.system('cls')
            print("=" * 15)
            for id, produto in enumerate(lista_produtos):
                print(id, produto)
            print("=" * 15)
    else:
        print("Opção inválida")    
    