# Decoradores 

def meu_decorador(func):
    def wrapper():
        print("Executou antes")
        func()
        print("Executou Depois")
    return wrapper

@meu_decorador
def teste_decorador():
    print("Executou no meio")

teste_decorador()


class ClassDecorador:
    def __init__(self,func) -> None:
        self.func = func
    
    def __call__(self) -> None:
        print("Executou antes")
        self.func()
        print("Executou Depois")

@ClassDecorador
def teste_decorador2():
    print("Executou no meio")

teste_decorador2()