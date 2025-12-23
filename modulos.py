"""
Exemplo de importação de módulos em Python
Este arquivo demonstra como importar e usar módulos padrão e personalizados
"""

# Importando função específica do módulo math
from math import sqrt

# Importando funções de um módulo personalizado
from modulo_personalizado import somar, saudacao

# Importando módulo externo (requer instalação: pip install requests)
import requests

print("Exemplo de importação de um módulo padrão:")

# Calculando a raiz quadrada usando a função sqrt do módulo math
raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é {raiz_quadrada}")

print("\nUtilização de módulos personalizados:")

# Usando função do módulo personalizado
resultado = somar(1, 2)
print(f"Resultado da soma: {resultado}")

# Fazendo uma requisição HTTP usando o módulo requests
response = requests.get("https://www.youtube.com.br")
print(f"Resposta status code: {response.status_code}")