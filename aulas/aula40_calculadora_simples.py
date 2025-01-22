# resultado = 0
# while True:
#     sair = input("Para finalizar Digite [s]air: ").lower()
#     if sair.startswith("s"):
#         print("Finalizado")
#         break

#     valor_1 = input("\nValor 1: ")
#     valor_2 = input("Valor 2: ")
#     operador = input("Operadores +, -, *, ou / : ")
#     try:
#         valor_1 = float(valor_1)
#         valor_2 = float(valor_2)
#         if operador == "+":
#             resultado = valor_1 + valor_2
#         elif operador == "-":
#             resultado = valor_1 - valor_2
#         elif operador == "*":
#             resultado = valor_1 * valor_2
#         elif operador == "/":
#             resultado = valor_1 / valor_2
#         else:
#             print("Operador inválido")
#         print(f"{resultado = }")
#     except:
#         print("Operação inválida")


""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == "+":
        resultado = num_1_float + num_2_float
    elif operador == "-":
        resultado = num_1_float - num_2_float
    elif operador == "*":
        resultado = num_1_float * num_2_float
    elif operador == "/":
        resultado = num_1_float / num_2_float
    else:
        print("ERRO")

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break