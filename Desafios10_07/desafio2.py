import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    tarefa = ['acordar', 'banhar', 'escovar os dentes', 'tomar café', 'trabalhar', 'almoçar']
    
    print("Lista de Tarefas")
    print("1. Adiciona nova Tarefa")
    print("2. Visualizar Tarefas")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefa.append(nova_tarefa)

    elif opcao == '2':
        if len(tarefa) == 0:
            print("Nenhuma tarefa adicionada até o momento")
        else:
            print("Tarefas:")
            for i, tarefa in enumerate(tarefa, start=1):
                print(f"{i}. {tarefa}")
        input("Pressione Enter para continuar ")

    elif opcao == '3':
        print("O Programa será encerrado ")
        break
    else:
        print("Opção inválida. Tente novamente.")
        input("Pressione Enter para continuar...")
