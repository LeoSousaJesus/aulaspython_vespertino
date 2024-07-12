import os
import time

lista_cpf = ['123456789', '987654321', '333333333', '444444444']
lista_usuarios = ['gomes', 'oliveira', 'lucas', 'karython']


os.system
while True:
    print(30*'=', 'Bem-vindo ao sistema Python cadastros', 30*'=')
    print('1. Cadastrar usuário')
    print('2. Consultar usuário')
    print('3. Acessar Sistema')
    print('4. Remover usuário')
    print('5. Sair')

    opcao = input('Digite a opção desejada: ')

#Opção para cadastrar novo usuário
    if opcao == '1':
        os.system('cls')
        novo_nome = input('Digite o nome que será cadastrado: ')
        novo_cpf = input('Digite um CPF: ')

        if novo_cpf in lista_cpf:
            print('O cpf digitado já existe')
        else:
            lista_cpf.append(novo_cpf)
            lista_usuarios.append(novo_nome)
            print('Senha cadastrada com sucesso!')

    #Opção consultar usuários
    elif opcao == '2':
        
        for i in lista_usuarios:
            print(f'Usuários: {i}')

    #Opção para acesssar o sistema
    elif opcao == '3':
        os.system('cls')
        cpf_login = input('Digite um novo cpf: ')

        if cpf_login in lista_cpf:
            print('Acesso realizado com sucesso!')
        else:
            lista_cpf.append(novo_cpf)
            lista_usuarios.append(novo_nome)
            print('Usuário cadastrado com sucesso')

    elif opcao == '4':
        os.system('cls')
        cpf_remove = input('Digite o CPF a ser excluído: ')

        if cpf_remove in lista_cpf:
            indice = lista_cpf.index(cpf_remove)
            nome = lista_usuarios.pop(indice)
            lista_cpf.pop(indice)

            print(f'Usuário: {nome} com o cpf {cpf_remove} foi removido com sucesso!')

    elif opcao == '5':
        os.system('cls')
        print('Saindo do sistema')
        time.sleep(3)
        break

    else:
        print('Opção Inválida!')