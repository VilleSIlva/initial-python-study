"""
Gerenciador de Contatos
Sistema simples de gerenciamento de contatos com interface no terminal

Funcionalidades:
[x] - Mostrar uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
[x] - Implementar funcionalidade para adicionar um contato (Nome, Telefone, Email, Favorito)
[x] - Desenvolver visualização da lista de contatos cadastrados
[x] - Criar funcionalidade para editar um contato existente
[x] - Implementar opção para marcar/desmarcar um contato como favorito
[x] - Desenvolver visualização da lista de contatos favoritos
[x] - Criar funcionalidade para apagar um contato
"""

# Lista global para armazenar todos os contatos
lista_contatos = []


def adicionar_contato(lista_contatos, nome, telefone, email):
   
    novo_contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }

    lista_contatos.append(novo_contato)
    print("\nO contato {} foi adicionado à sua lista".format(nome))
    return


def listar_contatos_favoritos(lista_contatos):
    """
    Exibe todos os contatos marcados como favoritos
    
    Args:
        lista_contatos (list): Lista de contatos
    """
    print("\n----------------Lista de Contatos Favoritos----------------")
    encontrou = False
    
  
    for indice, contato in enumerate(lista_contatos, start=1):
        if contato['favorito']:
            encontrou = True
            print(f"\n[{indice}] Nome: {contato['nome']}; Email: {contato['email']}; Telefone: {contato['telefone']};")
    
    if not encontrou:
        print("\nNenhum contato em favoritos")

    print("\n-----------------------------------------------------------")
    return


def listar_contatos(lista_contatos):
    """
    Exibe todos os contatos cadastrados na lista
    
    Args:
        lista_contatos (list): Lista de contatos
    """
    print("\n----------------Lista de Contatos----------------")
    print("\nLista de contatos")

   
    if len(lista_contatos) <= 0:
        print("\nSua lista não possui nenhum contato")
        return

 
    for indice, contato in enumerate(lista_contatos, start=1):
        favorito = "[Em favoritos]" if contato["favorito"] else ""
        nome = contato['nome']
        telefone = contato['telefone']
        email = contato['email']

        print(f"\n[{indice}] Nome: {nome}; Email: {email}; Telefone: {telefone};  {favorito}")
        print("\n--------------------------------------------")
    return


def editar_contato(lista_contatos, indice_contato, nome, telefone, email):
   
    indice_atualizado = int(indice_contato) - 1

    
    if nome != "":
        lista_contatos[indice_atualizado]["nome"] = nome

    if email != "":
        lista_contatos[indice_atualizado]["email"] = email

    if telefone != "":
        lista_contatos[indice_atualizado]["telefone"] = telefone
    
    print("\nContato atualizado com sucesso")


def adicionar_remover_favorito(lista_contatos, indice_contato):
   
    indice_atualizado = int(indice_contato) - 1

   
    lista_contatos[indice_atualizado]["favorito"] = not lista_contatos[indice_atualizado]["favorito"]
    
    status = "adicionado aos" if lista_contatos[indice_atualizado]["favorito"] else "removido dos"
    print(f"\nContato {status} favoritos com sucesso!")


def deletar_contato(lista_contatos, indice_contato):
  
    indice_atualizado = int(indice_contato) - 1
    

    if indice_atualizado < 0 or indice_atualizado >= len(lista_contatos):
        print("\nÍndice inválido. Contato não encontrado.")
        return False
    
  
    nome_contato = lista_contatos[indice_atualizado]["nome"]
    

    contato_removido = lista_contatos.pop(indice_atualizado)
    print(f"\nContato '{nome_contato}' foi removido com sucesso!")
    return True



while True:
    print("\nBem-vindo ao gerenciador de contatos")

    # Exibe o menu de opções
    print("\n----------------Menu----------------")
    print("\n1. Adicionar um contato")
    print("2. Visualizar todos os contatos")
    print("3. Editar contato")
    print("4. Marcar/Desativar contato favorito")
    print("5. Ver todos os contatos favoritos")
    print("6. Deletar contato")
    print("7. Sair")
    print("\n------------------------------------")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
        print("\n----------------Iniciando o Cadastro----------------")

        nome = input("\n- Insira o nome do contato: ").strip()
        telefone = input("- Insira o número do telefone: ").strip()
        email = input("- Insira o email: ").strip()

    
        if nome and telefone and email:
            adicionar_contato(lista_contatos, nome, telefone, email)
        else:
            print("\nErro: Todos os campos são obrigatórios!")
        
        print("\n---------------------------------------------------")
    
   
    elif opcao == "2":
        listar_contatos(lista_contatos)
  
    elif opcao == "3":
        listar_contatos(lista_contatos)
        if len(lista_contatos) > 0:
            print("\n----------------Iniciando a Edição----------------")
            try:
                indice = int(input("\nDigite o índice do contato que você deseja editar: "))
                nome = input("Digite o novo nome do contato ou aperte enter para manter o mesmo nome: ").strip()
                telefone = input("Digite o novo telefone do contato ou aperte enter para manter o mesmo telefone: ").strip()
                email = input("Digite o novo email do contato ou aperte enter para manter o mesmo email: ").strip()
                editar_contato(lista_contatos, indice, nome, telefone, email)
                print("\n---------------------------------------------------")
            except ValueError:
                print("\nErro: Digite um número válido!")
            except IndexError:
                print("\nErro: Índice inválido. Contato não encontrado.")
            except Exception as e:
                print(f"\nErro: {e}")
    
 
    elif opcao == "4":
        listar_contatos(lista_contatos)
        if len(lista_contatos) > 0:
            try:
                indice = int(input("\nDigite o índice do contato para adicionar/remover dos favoritos: "))
                adicionar_remover_favorito(lista_contatos, indice)
            except ValueError:
                print("\nErro: Digite um número válido!")
            except IndexError:
                print("\nErro: Índice inválido. Contato não encontrado.")
            except Exception as e:
                print(f"\nErro: {e}")
    elif opcao == "5":
        listar_contatos_favoritos(lista_contatos)
    elif opcao == "6":
 
        listar_contatos(lista_contatos)
        if len(lista_contatos) > 0:
            try:
                indice = int(input("\nDigite o índice do contato que você deseja deletar: "))
                deletar_contato(lista_contatos, indice)
            except ValueError:
                print("\nErro: Digite um número válido!")
            except Exception as e:
                print(f"\nErro ao deletar contato: {e}")
    elif opcao == "7":
        print("\nSistema finalizado")
        break
    else:
        print("\nOpção inválida!!")