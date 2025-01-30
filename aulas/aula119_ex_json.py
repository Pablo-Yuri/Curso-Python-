import os
import json

CAMINHO = os.path.dirname(__file__)
CAMINHO = os.path.join(CAMINHO, "aula119.json")

lista_tarefas = []
tarefas_refazer = []


def lista_json():
    try:
        with open(CAMINHO, "r") as file:
            # dados = json.dumps(file)
            dados = json.load(file)
            # print(dados, sep="\n")
            return dados
    except FileNotFoundError:
        adicionar_json(lista_tarefas)
    

def listar(lista):
    print()
    for tarefa in lista:
        print(tarefa)
    print()

    return True

def adicionar_tarefa(tarefa, lista_tarefas):
    if tarefa not in lista_tarefas:
        lista_tarefas.append(tarefa)
        print()
        adicionar_json(lista_tarefas)
        return
    
    return print(f"{tarefa= } já está na lista")


def adicionar_json(lista):
    with open(CAMINHO, "w", encoding="utf8") as arquivo:
        json.dump(lista, arquivo, indent=2)
        
def desfazer(tarefa):
    if not lista_tarefas:
        return print("\nNenhuma tarefa para desfazer\n")
    
    tarefa = lista_tarefas.pop()
    tarefas_refazer.append(tarefa)
    adicionar_json(lista_tarefas)
    
        
lista_tarefas.extend(lista_json())
# print("lista", lista_tarefas)
    
def refazer(tarefa):
    if not tarefas_refazer:
        return print("\nNenhuma tarefa para ser refeita")
    
    tarefa = tarefas_refazer.pop()
    lista_tarefas.append(tarefa)
    adicionar_json(lista_tarefas)
    
    
while True:
    print('Comandos: listar')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        "listar": lambda: listar(lista_tarefas),
        "adicionar_tarefa": lambda: adicionar_tarefa(tarefa, lista_tarefas),
        "refazer": lambda: refazer(tarefa),
        "desfazer": lambda: desfazer(tarefa)
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos["adicionar_tarefa"]
    comando()
    # adicionar_json(lista_tarefas)
