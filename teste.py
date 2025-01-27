

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

