"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
valor =  input("Digite um valor inteiro: ")

if valor.isdigit():
    impar_ou_par = int(valor) % 2
    if impar_ou_par == 0:
        print(f"{valor} é um número PAR")
    else:
        print(f"{valor} é um número ÍMPAR")
else:
    print("O valor digitado não é um número inteiro")
    
