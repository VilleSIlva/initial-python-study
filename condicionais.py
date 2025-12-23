"""
Exemplos de estruturas condicionais em Python
Demonstra o uso de if, else e expressões condicionais (operador ternário)
"""

# Exemplo 1: Estrutura condicional básica (if/else)
idade = int(input("Quantos anos você tem? "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# Exemplo 2: Expressão condicional (operador ternário)
# Forma compacta de escrever if/else em uma única linha
mensagem = "Pode tirar a CNH" if idade >= 18 else "Você não pode tirar a CNH"
print(mensagem)
