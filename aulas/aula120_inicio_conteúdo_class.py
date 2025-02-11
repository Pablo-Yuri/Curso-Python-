# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa("Pablo", "Yuri")
p2 = Pessoa("Maria", "Joana")

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)

print(isinstance(p2, str))
print(isinstance(p2, Pessoa))
