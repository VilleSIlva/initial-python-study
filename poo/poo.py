from abc import ABC,abstractmethod

#POO

#Class Exemplo
class Pessoas:
    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        print(f"Olá tudo bem, meu nome é {self.nome}")

#Objetos
pessoa1 = Pessoas("Ville",20)
pessoa1.saudacao()


class Animal:
    def __init__(self,nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"\nO animal {self.nome} andou")

    def emitir_som():
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print("Au Au")

class Gato(Animal):
    def emitir_som(self):
        print("Miau")

cachorro = Cachorro("Dog")
cachorro.andar()
cachorro.emitir_som()

gato = Gato("Cat")
gato.emitir_som()
gato.andar()

class ContaBancaria:
    def __init__(self,saldo) -> None:
        self.__saldo = saldo

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self,valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        print(f"Seu saldo é {self.__saldo}")

conta = ContaBancaria(1000)
conta.depositar(200)
conta.consultar_saldo()
conta.sacar(500)
conta.consultar_saldo()

class Veiculo(ABC):
    
    @abstractmethod
    def ligar_veiculo():
        pass

    @abstractmethod
    def desligar_veiculo():
        pass


class Moto(Veiculo):
    def ligar_veiculo(self):
        print("Veiculo Ligando")

    def desligar_veiculo(self):
        print("Veiculo Desligando")

newMoto = Moto()
newMoto.ligar_veiculo()