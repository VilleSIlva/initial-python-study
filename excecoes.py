"""
Exemplo de tratamento de exceções em Python
Este código demonstra como capturar e tratar diferentes tipos de erros
"""

print("Exemplo de captura de exceções:")

while True:
    try:
        # Tenta converter a entrada do usuário para inteiro
        numero = int(input("Digite um número inteiro: "))
        
        # Tenta dividir 10 pelo número digitado
        resultado = 10 / numero
        
    except ValueError as e:
        # Captura erro quando o usuário digita algo que não é um número
        print(f"Erro de validação: {e}")
        print("Erro: valor inválido (não é um número inteiro)")
        # Não relança a exceção para continuar o loop
        
    except ZeroDivisionError as e:
        # Captura erro quando tenta dividir por zero
        print(f"Erro: {e}")
        print("Não é possível dividir por zero!")
        
    except Exception as e:
        # Captura qualquer outro tipo de erro
        print(f"Erro inesperado: {e}")
        
    else:
        # Executado apenas se não houver exceções
        print(f"Resultado: {resultado}")
        break  # Sai do loop se a operação foi bem-sucedida
        
    finally:
        # Sempre executado, independente de ter ocorrido erro ou não
        print("Operação finalizada\n")