import os

print("=" * 50)
print("Mandar e trazer dados de arquivos txt\n")

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, "caminho.txt")

with open(SAVE_TO, "w+") as arquivo:
    arquivo.write("Pablo Yuri\n")
    

with open(SAVE_TO, "a+") as arquivo:
    arquivo.write("Yuri\n")
    arquivo.seek(0.0)
    print(arquivo.read())
# os.rename(SAVE_TO, 'teste4.txt')


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# for produto in produtos:
#     print(produto)
print("=" * 50)
print("Mandar dados para arquivos json\n")
import json

SAVE_TO2 = os.path.join(BASE_DIR, "caminho_json.json")

with open (SAVE_TO2, "w+") as file:
    json.dump(produtos, file, indent=2)    


dados = json.dumps(produtos, indent=2)  # => Formata em json no proprio codigo, salva em uma va riavel 
print(dados)


print("=" * 50)
print("Trazer dados de arquivos json\n")

JSON_FILE = os.path.join(BASE_DIR, "caminho_json.json") # => trazer arquivos

with open(JSON_FILE, "r") as file:
    dados = json.load(file)
    print(*dados, sep="\n")
