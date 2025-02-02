# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import os
import json

CAMINHO = os.path.dirname(__file__)
CAMINHO = os.path.join(CAMINHO, "aula127_dados.json")


class Pessoa():
    # list_for_json = [{
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # self.nascimeto = None
    
    # def get_ano_nascimento(self):
    #     ano_nascimento = 2024 - self.idade
    #     self.nascimeto = ano_nascimento

    def salvar_json(self):
        # self.get_ano_nascimento()
        dados = vars(self)
        list_for_json.append(dados)
        # print(list_for_json)
        with open(CAMINHO, "w", encoding="utf8",) as file:
            json.dump(list_for_json, file, indent=2)



list_for_json = []
pablo = Pessoa("Pablo", 18)
yuri = Pessoa("Yuri", 17)
p3 = Pessoa("Maria", 54)
p4 = Pessoa("João", 44)

pablo.salvar_json()
yuri.salvar_json()
p3.salvar_json()
p4.salvar_json()

# print(pablo.nome)
# print(pablo.idade)
# pablo.get_ano_nascimento()
# pablo.salvar_json()

print()

# print(yuri.nome)
# print(yuri.idade)
# yuri.get_ano_nascimento()
# yuri.salvar_json()

# p3.get_ano_nascimento()
# p3.salvar_json()