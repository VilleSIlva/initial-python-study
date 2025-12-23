"""
Exemplos de uso de valores booleanos e operadores lógicos em Python
Demonstra True, False e os operadores and, or
"""

# Valores booleanos em Python
# Condição Falsa
False

# Condição Verdadeira
True

# Estruturas condicionais
# if = se condição
# else = se não

if True:
    print("Bloco IF vai ser executado")
else:
    print("Bloco ELSE não será executado")

# Operadores Lógicos: and (E) e or (OU)

# Operador AND (E) - retorna True apenas se ambas condições forem True
print("\nOperador AND:")
if True and True:
    print("Bloco será executado (True and True)")

if True and False:
    print("Bloco não será executado (True and False)")

if False and False:
    print("Bloco não será executado (False and False)")

# Operador OR (OU) - retorna True se pelo menos uma condição for True
print("\nOperador OR:")
if True or False:
    print("Bloco OR vai ser executado (True or False)")

if False or False:
    print("Bloco OR não vai ser executado (False or False)")

if True or True:
    print("Bloco OR vai ser executado (True or True)")
