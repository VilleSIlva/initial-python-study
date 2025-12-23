class MinhaClasse:
    variavel = 20

    @classmethod
    def classMethod(cls):
        print("Class Method")

    @staticmethod
    def clasStatic():
        print("Class Estatica")

print(MinhaClasse.variavel)
MinhaClasse.classMethod()
MinhaClasse.clasStatic()