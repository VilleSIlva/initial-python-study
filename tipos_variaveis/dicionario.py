"""
Exemplos de uso de dicionários em Python
Dicionários são estruturas de dados que armazenam pares chave-valor
"""

# Criando um dicionário
person = {
    "nome": "Ville Nunes",
    "age": 20,
    "sexo": "m",
    "date_nasc": "20/03/2006",  
    "cidade": "Umuarama"
}

# Exibindo o dicionário completo
print("Meu dicionário:", person)

# Acessando valores por chave usando colchetes
print("Nome:", person["nome"])

# Adicionando uma nova chave-valor ao dicionário
person['sobrenome'] = "Silva"
print("Idade:", person.get("age"))  # Usando get() para acessar de forma segura

# Atualizando um valor existente
person["age"] = 19
print("Dicionário atualizado:", person)

# Removendo dados do dicionário usando del
del person["sobrenome"]
print("Dicionário após remover sobrenome:", person)

# Métodos úteis: keys(), values(), items()

# Método keys() - retorna todas as chaves do dicionário
chaves = list(person.keys())
print(f"\nChaves do dicionário: {chaves}")
print(f"Primeira chave: {chaves[0]}")

# Método values() - retorna todos os valores do dicionário
values = list(person.values())
print(f"Valores do dicionário: {values}")

# Método items() - retorna pares (chave, valor) como tuplas
items = list(person.items())
print(f"Items do dicionário (tuplas): {items}")
print(f"Primeiro item (chave): {items[0][0]}")
print(f"Primeiro item (valor): {items[0][1]}")