# Exercício - Adiando execução de funções
def soma(x, y):
    return f"{x} + {y} = {x + y}"

def multiplica(x, y):
    return f"{x} * {y} = {x * y}"


def criar_funcao(funcao, *args):
    x = args[0]
    def execucao(y):
        return funcao(x,y)
    return execucao


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(9))
print(multiplica_por_dez(9))

print(soma_com_cinco(4))
print(multiplica_por_dez(3))




