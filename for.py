"""
Exemplos de uso do loop for em Python
Demonstra diferentes formas de iterar sobre listas, dicionários e ranges
"""

# Lista de números
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Iterando sobre uma lista diretamente
print("Iterando sobre lista:")
for i in lista:
    print(i)

# Dicionário com informações pessoais
dicionario = {
    "name": "Ville Nunes da Silva",
    "age": 30,
    "city": "Umuarama"
}

# Iterando sobre as chaves do dicionário
print("\nIterando sobre chaves do dicionário:")
for chave in dicionario.keys():
    print(chave)

# Iterando sobre os valores do dicionário
print("\nIterando sobre valores do dicionário:")
for value in dicionario.values():
    print(value)  # Corrigido: estava usando 'chave' mas deveria ser 'value'

# Iterando sobre chaves e valores simultaneamente
print("\nIterando sobre chaves e valores:")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

# Criando uma lista com range
print(f"\nLista criada com range(0, 10): {list(range(0, 10))}")

# Iterando com range (gera números de 0 a 4)
print("\nIterando com range(5):")
for numero in range(5):
    print("Número:", numero)

# Iterando usando índices da lista
print("\nIterando usando índices:")
for i in range(0, len(lista)):
    print(f"Índice {i}: {lista[i]}")

# Usando enumerate para obter índice e valor simultaneamente
lista_enumerate = ["A", "B", "C", "D"]
print("\nUsando enumerate:")
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")