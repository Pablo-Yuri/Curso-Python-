# Entrada: l1 = [2,4,3], l2 = [5,6,4]
#  Saída: [7,0,8]
#  Explicação: 342 + 465 = 807.


# l1 = [2,4,3]
# l2 = [5,6,4]
# l1  = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]


# maior = l1.copy() if len(l1) > len(l2) else l2.copy()
# menor = l1.copy() if len(l1) < len(l2) else l2.copy() 


# print("maior",maior, "menor",menor)

# while len(menor) != len(maior):
#     menor.append(0)

#print(maior, menor)

def addTwoNumbers(l1 , l2):
    # maior = l1.copy() if len(l1) >= len(l2) else l2.copy()
    # menor = l2.copy() if len(l1) <= len(l2) else l1.copy() 

    if l1 >= l2:
        maior = l1
        menor = l2
    else:
        maior = l2
        menor = l1

    print(maior, menor)    

    while len(menor) != len(maior):
        menor.append(0)

    lista_soma = []
    sobra = 0

    for index, num in enumerate(maior):
        #print(num, l2[index])
        # print(f"soma = {num} {menor[index]} = {num + menor[index]}")
        soma = num + menor[index] + sobra
        if sobra > 0: sobra -= 1
        # print("soma =",soma)
        # print(lista_soma)
        # soma.append(num + menor[index])
        if soma >= 10:
            # print("soma for =",soma - 10)
            #print(">=10")
            lista_soma.append(soma-10)
            sobra += 1
        else:
            lista_soma.append(soma)

        if index == len(maior) - 1 and sobra > 0:
            lista_soma.append(sobra)

    return lista_soma


l1  = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
l1 = [2,4,3]
l2 = [5,6,4]
# l1 = [0]

print(addTwoNumbers(l1,l2))


# Entrada: l1  = [9,9,9,9,9,9,9], 
#            l2 = [9,9,9,9]
#             [8,9,9,9,0,0,0,1]
 
#  l1 = [243], l2 = [564]
#  Saída



class Solution:
    def addTwoNumbers(self, l1: list[int], l2: list[int]):
        if l1 >= l2:
            maior = l1
            menor = l2
        else:
            maior = l2
            menor = l1

        print(maior, menor)    

        while len(menor) != len(maior):
            menor.append(0)

        lista_soma = []
        sobra = 0

        for index, num in enumerate(maior):
            soma = num + menor[index] + sobra

            if sobra > 0: sobra -= 1

            if soma >= 10:
                lista_soma.append(soma-10)
                sobra += 1

            else:
                lista_soma.append(soma)

            if index == len(maior) - 1 and sobra > 0:
                lista_soma.append(sobra)

        return lista_soma

l1  = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
l1 = [2,4,3]
l2 = [5,6,4]
l1 = [0]
l2 = [0]

print(addTwoNumbers(self='',l1=l1,l2=l1))

