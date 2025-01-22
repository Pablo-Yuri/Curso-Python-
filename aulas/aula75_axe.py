

# def pegar_num(coisa_a_ser_feita):
#     def duplicar(num):
#         return f'{num} X 2 = {num * 2}'
    
#     def triplicar(num):
#         return f'{num} X 3 = {num * 3}'
    
#     def quadriplicar(num):
#         return f'{num} X 4 = {num * 4}'
    
#     if coisa_a_ser_feita == "duplicar":
#         return duplicar
#     elif coisa_a_ser_feita == "triplicar":
#         return triplicar
#     elif coisa_a_ser_feita == "quadriplicar":
#         return quadriplicar
#     else:
#         return "Parametro inválido"

# duplicar = pegar_num("duplicar")
# triplicar = pegar_num("triplicar")
# quadriplicar = pegar_num("quadriplicar")

# print(duplicar(20))
# print(triplicar(65))
# print(quadriplicar(2))
# print(quadriplicar(4))
# print(triplicar(87))

# print('=' * 20)

def mulplicar_por(quantas_vezes):
    def mult(numero):
        return f'{numero} X {quantas_vezes} = {numero * quantas_vezes}'
    return mult

duplicar_ = mulplicar_por(2)
triplicar_ = mulplicar_por(3)
quadriplicar_ = mulplicar_por(4)

print(duplicar_(2))
print(triplicar_(4))
print(quadriplicar_(2))



dados = {
    "nome": "pablo",
    "idade": 18
}

print(dados['idade'])
print(dados["nome"])