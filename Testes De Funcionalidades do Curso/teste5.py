import os
import json, copy

BASE_DIR = os.path.dirname(__file__)
caminho = os.path.join(BASE_DIR, "caminho_json.json")


with open(caminho, 'a+') as file:
    file.seek(0.0)
    # dados = (file.read())
    dados = json.load(file)

dados_mod = copy.deepcopy(dados)
print(*dados_mod,sep="\n")

print("="*40)
dados_mod.append({'nome': 'Produto 8', 'preco': 75.0})
print(*dados_mod,sep="\n")
