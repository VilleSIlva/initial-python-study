"""
Exemplos de manipulação de strings em Python
Demonstra diferentes formas de declarar, formatar e manipular strings
"""

# Declaração de strings

# String simples
nome_completo = "Ville Nunes Figueiredo Da Silva"

# String com múltiplas linhas usando aspas triplas
nome_completo_aspas_duplas = """
    Ville Nunes
"""

# String com quebra de linha usando barra invertida
nome_completo_quebra = "Ville Nunes \
da Silva"

nome = "Ville"
sobrenome = "Nunes Figueiredo Da Silva"

# Formatação de strings - diferentes formas

print("Nome completo (1ª forma - vírgula):", nome_completo)
print("Nome completo (2ª forma - concatenação): " + nome_completo)
print("Nome completo (3ª forma - concatenação): " + nome + " " + sobrenome)
print("Nome completo (4ª forma - múltiplos argumentos):", nome, sobrenome)
print("Nome completo (5ª forma - aspas triplas):", nome_completo_aspas_duplas)
print("Nome completo (6ª forma - quebra de linha):", nome_completo_quebra)
print("Nome completo (7ª forma - %): %s" % nome_completo_quebra)
print("Nome completo (8ª forma - % múltiplos): %s %s" % (nome, sobrenome))
print(f"Nome completo (9ª forma - f-string): {nome} {sobrenome}")
print("Nome completo (10ª forma - format): {} {}".format(nome, sobrenome))

# Métodos úteis de strings

print("\n" + "="*50)
print("Métodos de String:")
print("="*50)

# find() - retorna o índice da primeira ocorrência
print(f"nome.find('i'): {nome.find('i')}")

# count() - conta quantas vezes um caractere aparece
print(f"nome.count('i'): {nome.count('i')}")

# lower() - converte para minúsculas
print(f"nome.lower(): {nome.lower()}")

# upper() - converte para maiúsculas
print(f"nome.upper(): {nome.upper()}")

# encode() - codifica a string em bytes
print(f"nome.encode(): {nome.encode()}")

# decode() - decodifica bytes para string
print(f"nome.encode().decode(): {nome.encode().decode()}")

# replace() - substitui caracteres
print(f"nome.replace('i', 'a'): {nome.replace('i', 'a')}")

# join() - junta elementos de uma sequência com um separador
print(f"'-'.join(nome): {'-'.join(nome)}")

# split() - divide a string em uma lista
print(f"nome.split(''): {nome.split('')}")  # Nota: split('') pode não funcionar como esperado
print(f"'Ville Nunes'.split(' '): {'Ville Nunes'.split(' ')}")  # Exemplo melhor

# strip() - remove caracteres do início e fim da string
texto_com_espacos = "  Ville  "
print(f"'{texto_com_espacos}'.strip(): '{texto_com_espacos.strip()}'")

# startswith() - verifica se a string começa com determinado texto
print(f"nome.startswith('Vi'): {nome.startswith('Vi')}")

# Operador in - verifica se um texto está contido na string
print(f"'Vi' in nome: {'Vi' in nome}")
print(f"'Vi' not in nome: {'Vi' not in nome}")
