

from aula127_a_ex_class import CAMINHO, os, json, Pessoa

CAMINHO = os.path.dirname(__file__)
CAMINHO = os.path.join(CAMINHO, "aula127_dados.json")

dados_json = None 
with open(CAMINHO, "r", encoding="utf8") as file:
    dados_json = json.load(file)

    p1 = Pessoa(**dados_json[0])
    p2 = Pessoa(**dados_json[1])
    p3 = Pessoa(**dados_json[2])

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)


# class Pessoa():
#     def __init__(self, nome, idade, nascimento):
#         self.nome = nome
#         self.idade = idade
#         self.nascimento = nascimento
    
#     def saudacao(self):
#         return f"{self.nome} tem {self.idade}, nasceu no ano de {self.nascimento}."

# # print(p1, p2)

# for pessoa in dados_json:
#     pessoa["nome"] = Pessoa(pessoa["nome"],pessoa["idade"],pessoa["nascimeto"])
#     print(pessoa["nome"].saudacao())


# print()
# p1, p2, *pResto = dados_json
# print(p1["nome"].saudacao())
# print(p2["nome"].saudacao())
# print(*pResto,sep="\n")
