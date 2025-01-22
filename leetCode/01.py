# def two_sum(num):
#     def soma(*algo):
#         valores = algo
#         resultado = num
#         for valor in valores:
#                 for n in valores:
#                     if valor != n:
#                         print(valor, n, end="\n")
#                         if valor + n == num:
#                             print(f"{valor} + {n} = {resultado}")
#         return valores
#     return soma

# chegar_a = two_sum(8)

# print(chegar_a(5,4,10,9, 4))

def two_sum(*nums, alvo):
    nums = nums[0]
    #print(*nums, alvo, len(nums[0]))
    for valor2 in enumerate(nums):
        for valor1 in enumerate(nums):
            if valor1 != valor2:
                # print(valor1[1], valor2[1]) 
                soma = valor1[1] + valor2[1]
                # print(f"soma = {alvo}")             
                if soma == alvo:
                    # print(f"{valor1[1]} + {valor2[1]} = {alvo}")             
                    return valor2[0], valor1[0]
    else:
        return f"Não é possivel somar dois números da lista {nums} e obter {alvo}"                

nums = [5,3,4,3]
nums = [3,2,4]
# nums = [6,2,5,4]
print(two_sum(nums, alvo=6))

nums = [3,2,4]

# for valor1 in enumerate(nums):
#      for valor2 in enumerate(nums):
#         if valor1 != valor2:
#             print(valor1, valor2)
#             if valor1[1] + valor2[1] == 7:
#                 print(f"{valor1[1]} + {valor2[1]}")
#             else:
#                 print(f"Não é possivel somar dois números da lista  e obter {alvo}")

