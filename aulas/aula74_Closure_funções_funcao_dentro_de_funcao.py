"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_boa_noite("pablo"))

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))





def mulplicar_por(mulplicar_por):
    def multiplica(numero):
        return f"{numero} X {mulplicar_por} {mulplicar_por * numero}"
    return multiplica

num1 = mulplicar_por(10)
num2 = mulplicar_por(5)

print(num1(4))
# print(num1(40))
# print(num1(32))
# print(num1(45))

# print()
# print(num2(4))
# print(num2(40))
# print(num2(32))
# print(num2(45))


# soma = '1' + "1"
# print("soma = ", soma)

