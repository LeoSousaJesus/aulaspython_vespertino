lista_nomes = ['Leo', 'Edu', 'Ste', 'Edite', 'Jose', 'Maria', 'João']

# Lista original
for i in range(len(lista_nomes)):
    print(f'{i + 1}° nome da lista é: {lista_nomes[i]}')
    
novo_nome = input('Digite o novo nome que será adicionado na lista: ')

posicao = input('Digite a posição que deseja colocar esse nome: ')
posicao = int(posicao)

#Corrigindo a posição
posicao -= 1

if posicao >= 0 and posicao <= len(lista_nomes):
    lista_nomes.insert(posicao, novo_nome)
else:
    print('Posicao inválida!')    

# exiba a lista atualizada
print()
print(30*'=', 'Lista Atualizada', 30*'=')

for i in range(len(lista_nomes)):
    print(f'{i + 1}° nome da lista é: {lista_nomes[i]}')

