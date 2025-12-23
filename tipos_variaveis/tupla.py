"""
Exemplos de uso de tuplas em Python
Tuplas são estruturas de dados ordenadas e imutáveis (não podem ser modificadas)
"""

# Criando uma tupla
minha_tupla = (1, 2, 3, 5, 5, 6, 7, 1)

# Acessando elementos da tupla por índice
print(f"Primeiro elemento (índice 0): {minha_tupla[0]}")

# count() - conta quantas vezes um valor aparece na tupla
print(f"Quantidade de vezes que o número 2 aparece: {minha_tupla.count(2)}")
print(f"Quantidade de vezes que o número 5 aparece: {minha_tupla.count(5)}")

# index() - retorna o índice da primeira ocorrência de um valor
print(f"Índice do primeiro número 3: {minha_tupla.index(3)}")
print(f"Índice do primeiro número 5: {minha_tupla.index(5)}")

# Nota: Tuplas são imutáveis, então não podemos modificar seus elementos
# minha_tupla[0] = 10  # Isso causaria um erro!