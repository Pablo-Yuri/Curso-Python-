lista = """10012560, Caio Vitor Martins Souza, 15.000, 75.649, 52.974, 5.233, 80.135, 3/ 10016449,
Daniel Ricardo de Araujo Seguro, 22.000, 78.158, 45.815, 6.929, 85.290, 2/ 10017342,
Davi Silva Rendeiro, 12.333, 44.499, 24.633, 4.633, -83.150, 17/ 10005200, Davi Sousa
de Farias, 10.000, 73.983, 29.999, 5.121, -6.935, 10, 1/ 10017444, Diego Larrosa
Chimpliganond, 8.000, 69.825, 29.656, 6.100, -12.280, 11/ 10007831, Eduardo Garcia
Pires Goncalves, 12.333, 63.166, 35.632, 6.833, 6.080, 9/ 10002397, Eduardo Ramos
Diniz, 23.000, 68.000, 63.990, 7.534, 129.360, 1/ 10010412, Felipe Couto Duque, 8.333,
62.833, 37.982, 6.833, 6.430, 8/ 10005876, Fernanda Vasconcelos Reis, 12.333, 52.666,
30.965, 5.914, -36.125, 12/ 10020334, Grazielle Montinegro dos Santos, 4.333, 51.824,
17.972, 6.367, -89.955, 18, 2/ 10020604, Joao Vitor Fonseca Santos Bittencourt, 12.000,
59.824, 45.966, 4.293, 13.000, 7/ 10003990, Lucas Gabriel Ferreira de Souza, 11.333,
45.491, 34.307, 4.700, -50.615, 13/ 10020832, Lucas Kaczan Freitas de Gouvea, 18.000,
79.158, 36.306, 7.389, 53.675, 5/ 10018138, Marina Monteiro Mota, 13.000, 79.008,
31.315, 6.672, 23.865, 6/ 10003861, Matheus Kempa Severino, 21.000, 65.825, 13.331,
5.417, -56.735, 14/ 10012797, Natallia Maria Maltha Mascarenhas, 0.333, 32.824,
16.298, 4.500, -154.305, 20/ 10011749, Rafael Vasconcelos Viana, 3.000, 48.491, 28.299,
6.033, -68.030, 15/ 10016834, Talita Riane Castro da Silva, 1.000, 39.674, 25.332, 5.833,
-100.405, 19/ 10012854, Victor Goncalves Fernandes, 10.333, 52.499, 18.631, 5.500, -
82.590, 16/ 10006360, Yuri Villa Chan Rodrigues de Castro, 4.333, 73.158, 54.632, 5.967,
67.700, 4"""

lista = lista.split('/')
# print(*lista, sep="\n")
lista2 = []
cont = 10
for num, i in enumerate(lista):
    i = i.split(",")
    i.pop(0)
    print(i)
    if int(i[-1]) is cont:
        print(">>",i[-1])
    # lista2.append(" ".join(i))
    # print(i)

# print(*lista2, sep="\n")

# cont = 1
# while True:
#     for num, i in enumerate(lista):
#         i = i.split(",")
#         i.pop(0)
#         print(i[-1])
#         if int(i[-1]) == cont:
#             print(i[-1])
#             lista2.append(i)
#             cont += 1
#     if cont == 20:
#         break

# print(lista2)