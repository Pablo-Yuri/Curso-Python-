from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, nome):
        self._nome = nome
        # self.nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Foo(AbstractFoo):
    def __init__(self, nome):
        super().__init__(nome)

foo = Foo("bar")
print(foo.nome)
foo = Foo("Pablo")
print(foo.nome)