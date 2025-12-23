"""
Exemplo de uso do loop while em Python
Demonstra um loop infinito controlado com break
"""

print("Exemplo de while:")

# Inicializando o contador
contador = 0

# Loop infinito que será interrompido quando contador for 4
while True:
    print(f"Contagem: {contador}")
    contador += 1  # Incrementa o contador
    
    # Condição para sair do loop
    if contador == 4:
        break  # Interrompe o loop

print("Programa finalizado")