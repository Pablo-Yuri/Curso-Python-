

lista = ["Pablo", "Yuri", 'Ribeiro']

for num in range(len(lista)):
    print(num, lista[num])

lista.append("Souza")

for num, nome in enumerate(lista):
    print(num, nome)