# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

# print(perguntas[0]['Opções'][0])
Acertos = 0
Erros = 0
Respostas_invalidas = 0

for dados_perguntas in perguntas:
    print(f"Pergunta: {dados_perguntas['Pergunta']}")
    
    for index, opcao in enumerate(dados_perguntas['Opções']):
        print(f"{index}) {opcao}")
    resposta_user =  input("Escolha uma opção: ")

    try:
        resposta_user = int(resposta_user)
        resposta_user = dados_perguntas['Opções'][resposta_user]
        
        if resposta_user == dados_perguntas['Resposta']:
            print("Acertou")
            Acertos += 1
        else:
            print("Errou")
            Erros += 1
    
    except ValueError:
        print("Digite Apenas números")
        Respostas_invalidas += 1
    
    except IndexError:
        print("Opção inexistente")
        Respostas_invalidas += 1

print(f'{'='*25}\n{Acertos = }\n{Erros = }\n{Respostas_invalidas = }')

