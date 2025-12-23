"""
Gerenciador de Lista de Tarefas
Sistema simples de gerenciamento de tarefas com interface no terminal
"""

# Lista global para armazenar todas as tarefas
tarefas = []


def adicionar_tarefas(tarefas, nome_tarefa):
    """
    Adiciona uma nova tarefa à lista
    
    Args:
        tarefas (list): Lista de tarefas
        nome_tarefa (str): Nome da tarefa a ser adicionada
    """
    nova_tarefa = {
        "nome": nome_tarefa,
        "concluida": False
    }
    
    tarefas.append(nova_tarefa)
    print(f"\nA tarefa '{nome_tarefa}' foi adicionada com sucesso!")


def ver_tarefas(tarefas):
    """
    Exibe todas as tarefas da lista com seus status
    
    Args:
        tarefas (list): Lista de tarefas
    """
    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada ainda.")
        return
    
    print("\n" + "="*50)
    print("Lista de Tarefas:")
    print("="*50)
    
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa['concluida'] else "⏳"
        nome_tarefa = tarefa['nome']
        print(f"{indice}. {status} {nome_tarefa}")


def editar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    """
    Edita o nome de uma tarefa existente
    
    Args:
        tarefas (list): Lista de tarefas
        indice_tarefa (int): Índice da tarefa (começando em 1)
        novo_nome_tarefa (str): Novo nome para a tarefa
    """
    indice_atualizado = indice_tarefa - 1
    
    if len(tarefas) <= 0:
        print("\nNenhuma tarefa para atualizar.")
    elif indice_atualizado >= 0 and indice_atualizado < len(tarefas):
        tarefas[indice_atualizado]['nome'] = novo_nome_tarefa
        print("\nTarefa atualizada com sucesso!")
    else:
        print("\nÍndice inválido. Tarefa não encontrada.")


def completar_tarefa(tarefas, indice_tarefa):
    """
    Marca uma tarefa como concluída
    
    Args:
        tarefas (list): Lista de tarefas
        indice_tarefa (int): Índice da tarefa (começando em 1)
    """
    indice_atualizado = indice_tarefa - 1
    
    if len(tarefas) <= 0:
        print("\nNenhuma tarefa para completar.")
    elif indice_atualizado >= 0 and indice_atualizado < len(tarefas):
        if tarefas[indice_atualizado]['concluida']:
            print("\nEsta tarefa já está concluída!")
        else:
            tarefas[indice_atualizado]['concluida'] = True
            print("\nTarefa concluída com sucesso!")
    else:
        print("\nÍndice inválido. Tarefa não encontrada.")


def deletar_tarefa_completadas(tarefas):
    """
    Remove todas as tarefas que estão marcadas como concluídas
    
    Args:
        tarefas (list): Lista de tarefas
    """
    if len(tarefas) <= 0:
        print("\nNenhuma tarefa para excluir.")
        return
    
    # Corrigido: usar list comprehension ou criar nova lista para evitar
    # problemas ao remover itens durante a iteração
    tarefas_antes = len(tarefas)
    tarefas[:] = [tarefa for tarefa in tarefas if not tarefa['concluida']]
    tarefas_removidas = tarefas_antes - len(tarefas)
    
    if tarefas_removidas > 0:
        print(f"\n{tarefas_removidas} tarefa(s) concluída(s) deletada(s) com sucesso!")
    else:
        print("\nNenhuma tarefa concluída encontrada para deletar.")


# Loop principal do programa
while True:
    print("\n" + "="*50)
    print("Menu do Gerenciador de Lista de Tarefas")
    print("="*50)
    print("\n1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas Concluídas")
    print("6. Sair")
    
    escolha = input("\nDigite a sua escolha: ").strip()
    
    if escolha == "1":
        nome_tarefa = input("\nQual o nome da tarefa: ").strip()
        if nome_tarefa:
            adicionar_tarefas(tarefas, nome_tarefa)
        else:
            print("\nNome da tarefa não pode estar vazio!")
            
    elif escolha == "2":
        ver_tarefas(tarefas)
        
    elif escolha == "3":
        ver_tarefas(tarefas)
        if len(tarefas) > 0:
            try:
                indice = int(input("\nQual o índice da tarefa que você quer atualizar: "))
                novo_nome = input("Qual o novo nome: ").strip()
                if novo_nome:
                    editar_nome_tarefa(tarefas, indice, novo_nome)
                else:
                    print("\nNome da tarefa não pode estar vazio!")
            except ValueError:
                print("\nErro: Digite um número válido!")
                
    elif escolha == "4":
        ver_tarefas(tarefas)
        if len(tarefas) > 0:
            try:
                indice = int(input("\nEscolha a tarefa para completar: "))
                completar_tarefa(tarefas, indice)
            except ValueError:
                print("\nErro: Digite um número válido!")
                
    elif escolha == "5":
        deletar_tarefa_completadas(tarefas)
        
    elif escolha == "6":
        print("\nSaindo do programa...")
        break
    else:
        print("\nOpção inválida! Escolha um número de 1 a 6.")


print("\nPrograma Finalizado!")