class Animal:
    def __init__(self,nome) -> None:
        self.nome = nome
    
    def emitir_som():
        pass

class Mamifero(Animal):
    def amamentar(self):
        print(f"O animal está amamentando")

class Ave(Animal):
    def voar(self):
        print(f"O animal está voando")


class Morcego(Ave,Mamifero):
    def emitir_som(self):
        print(f"O {self.nome} está fazendo barulho")

batman = Morcego(nome="Batman")

batman.emitir_som()
batman.voar()