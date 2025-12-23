"""
Exemplos de uso de listas em Python
Listas são estruturas de dados ordenadas e mutáveis que podem armazenar diferentes tipos de elementos
"""

# Declaração de uma lista
minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Exibindo a lista completa
print("Minha lista de exemplo:", minha_lista)

# Acessando elementos individuais e slices (fatias)
print(f"\nElemento no índice 2: {minha_lista[2]}")
print(f"Slice [1:4]: {minha_lista[1:4]}")  # Elementos do índice 1 ao 3
print(f"Slice [:7]: {minha_lista[:7]}")   # Elementos do início ao índice 6

# Modificando um elemento da lista
minha_lista[0] = "Python"
print(f"\nLista após modificar índice 0: {minha_lista}")

# Métodos de lista

# append() - adiciona um elemento ao final da lista
minha_lista.append("Final")
print(f"Após append('Final'): {minha_lista}")

# index() - retorna o índice do primeiro elemento encontrado
print(f"Índice de 'Final': {minha_lista.index('Final')}")

# insert() - insere um elemento em uma posição específica
minha_lista.insert(2, "Indice 2")
print(f"Após insert(2, 'Indice 2'): {minha_lista}")

# pop() - remove e retorna o elemento no índice especificado
elemento_removido = minha_lista.pop(3)
print(f"Elemento removido com pop(3): {elemento_removido}")
print(f"Lista após pop(3): {minha_lista}")

# remove() - remove a primeira ocorrência do valor especificado
minha_lista.remove("Python")
print(f"Após remove('Python'): {minha_lista}")

# sort() - ordena a lista in-place (modifica a lista original)
# Nota: só funciona se todos os elementos forem do mesmo tipo comparável
# Como temos strings e números misturados, isso pode causar erro
# Vamos criar uma nova lista apenas com números para demonstrar
lista_numeros = [3, 1, 4, 1, 5, 9, 2, 6]
lista_numeros.sort()
print(f"\nLista de números ordenada: {lista_numeros}")
