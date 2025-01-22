"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import random
import sys

#sys.exit()
#print("cpf gerado =", cpf_random)

for qtd in range(100):
    lista = random.sample(range(0,10),9)
    #print(lista)
    cpf_random = ''
    for n in range(len(lista)):
        cpf_random += str(lista[n])
    cpf_user = cpf_random
    cpf_somente_num = cpf_user.replace(".",'').replace('-','').replace(' ','')
    nove_digitos = cpf_somente_num[:9]
    digito_1 = 0
    digito_2 = 0
    cpf_final = cpf_somente_num
    # print(cpf_final)
    passagem = 1
    while passagem <= 2:
        nove_ou_dez_digitos = cpf_final[:9]
        soma_das_multiplicacoes = 0

        cont = 10
        if passagem > 1:
                nove_ou_dez_digitos = cpf_final + str(digito_1)
                cont = 11
        # print("cpf", nove_ou_dez_digitos)
        for valor in nove_ou_dez_digitos:
            soma_das_multiplicacoes += int(valor) * cont
            cont -= 1

        multiplicacao_final = (soma_das_multiplicacoes * 10) % 11

        if passagem < 2:
            digito_1 = multiplicacao_final if multiplicacao_final <= 9 else 0
        else:
            digito_2 = multiplicacao_final if multiplicacao_final <= 9 else 0

        passagem += 1

    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
    print(f"{qtd+1} = {cpf_gerado=}")
    # print(cpf_user)

# if cpf_somente_num == cpf_gerado:
#      print("CPF válido")
# else:
#      print("CPF inválido")
# print(cpf_final)

# print(f"{digito_1 = }")
# print(f"{digito_2 = }")
# print(cpf_gerado)