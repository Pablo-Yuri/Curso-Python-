# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json, os

CAMINHO_ARQUIVO = os.path.dirname(__file__)
CAMINHO_ARQUIVO = os.path.join(CAMINHO_ARQUIVO, 'aula127versao_professor.json')

# CAMINHO_ARQUIVO = 'aula127versao_professor.json'
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]
def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()

    # versao_professor