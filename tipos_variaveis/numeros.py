"""
Exemplos de tipos numéricos e operações matemáticas em Python
Demonstra inteiros, floats e operadores aritméticos
"""

# Tipo inteiro (int)
numero_inteiro = 20
print("Inteiro =", numero_inteiro)

# Tipo real com ponto flutuante (float)
numero_real = 3.14
print("Real com ponto flutuante =", numero_real)

# Função type() - retorna o tipo da variável
print("Tipo da variável inteiro =", type(numero_inteiro))
print("Tipo da variável real com ponto flutuante =", type(numero_real))

# Operações aritméticas básicas

# Soma (+)
soma = 1 + 1
print(f"\n1 + 1 = {soma}")

# Subtração (-)
subtracao = 1 - 1
print(f"1 - 1 = {subtracao}")

# Multiplicação (*)
multiplicacao = 2 * 5
print(f"2 x 5 = {multiplicacao}")

# Divisão (/) - sempre retorna float
divisao = 5 / 2
print(f"5 / 2 = {divisao}")
print(f"Tipo da variável do resultado da divisão: {type(divisao)}")

# Conversão de tipos

# int() - converte para inteiro (trunca a parte decimal)
print(f"\nValor em inteiro: {int(divisao)}")

# float() - converte para float
print(f"Valor em float: {float(soma)}")

# Módulo (%) - retorna o resto da divisão
modulo = 5 % 2
print(f"\nResto da divisão (5 % 2): {modulo}")

# Divisão inteira (//) - retorna apenas a parte inteira
divisao_inteira = 5 // 2
print(f"5 // 2 = {divisao_inteira}")
print(f"Tipo da variável do resultado da divisão inteira: {type(divisao_inteira)}")
