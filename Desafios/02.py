from itertools import groupby

# alunoss = ["a","a","a","a","b","b","c","c","a"]
# grupo2 = groupby(sorted(alunoss))
# for chave, valor in grupo2:
#     print(chave)
#     print(list(valor))

alunos = [{"nome": "Alice", "escola": "Escola A", "nota": 85},
        {"nome": "Bruno", "escola": "Escola B", "nota": 90},
        {"nome": "Carlos", "escola": "Escola C", "nota": 78},
        {"nome": "Diana", "escola": "Escola B", "nota": 92},
        {"nome": "Eduardo", "escola": "Escola A", "nota": 88},
        {"nome": "Fernanda", "escola": "Escola C", "nota": 95},
        {"nome": "Gabriel", "escola": "Escola A", "nota": 80},
        {"nome": "Helena", "escola": "Escola B", "nota": 89},
        {"nome": "Igor", "escola": "Escola C", "nota": 76},
        {"nome": "Júlia", "escola": "Escola D", "nota": 91}
]

def ordena(aluno):
    return aluno["escola"]

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

# alunos_agrupados = sorted(alunos, key=lambda a: a["escola"])
# grupos = groupby(alunos_agrupados, key=lambda a: a["escola"])

for chave, valor in grupos:
    print(chave)
    # print(list(valor))
    for i in valor:
        print(i)
