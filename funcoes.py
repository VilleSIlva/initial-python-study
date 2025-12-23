"""
Exemplos de funções em Python
Demonstra diferentes tipos de funções: sem retorno, com retorno e com múltiplos parâmetros
"""

# Exemplo 1: Função sem retorno (apenas executa uma ação)
def saudacao(nome):
    """
    Imprime uma mensagem de saudação
    
    Args:
        nome (str): Nome da pessoa a ser saudada
    """
    print("Olá %s" % nome)

# Chamando a função
saudacao("Ville")

# Exemplo 2: Função com retorno
def quadrado(numero):
    """
    Calcula o quadrado de um número
    
    Args:
        numero (int/float): Número a ser elevado ao quadrado
    
    Returns:
        int/float: Resultado do número elevado ao quadrado
    """
    resultado = numero ** 2
    return resultado

# Chamando a função e exibindo o resultado
print(f"Quadrado de 20: {quadrado(20)}")

# Exemplo 3: Função com múltiplos parâmetros
def soma(numero1, numero2):
    """
    Soma dois números
    
    Args:
        numero1 (int/float): Primeiro número
        numero2 (int/float): Segundo número
    
    Returns:
        int/float: Resultado da soma
    """
    resultado = numero1 + numero2
    return resultado

# Chamando a função e exibindo o resultado
print(f"Soma de 2 + 3: {soma(2, 3)}")