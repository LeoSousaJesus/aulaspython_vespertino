import os

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))

salas = [{'sala': 1, 'filme':'Vingadores Guerra Infinita', 'classificacao': 12},
          {'sala': 2, 'filme':'Piratas do Caribe', 'classificacao': 14},
          {'sala': 3, 'filme':'Barbie', 'classificacao': 'Livre'},
          {'sala': 4, 'filme':'Bruxa de Blair', 'classificacao': 16},
          {'sala': 5, 'filme':'Deadpool & Wolverine', 'classificacao': 18}]

print("Salas Disponíveis:")
for sala in salas:        
    print(f"Sala: {sala['sala']} - Filme: {sala['filme']} - Classificação Indicativa: {sala['classificacao']}")

while True:
    escolha = int(input("Selecione a Sala: "))
    
    sala_encontrada = next((sala for sala in salas if sala['sala'] == escolha), None)
        
    if sala_encontrada:
        sala_encontrada['classificacao'] = 0 if sala_encontrada['classificacao'] == "Livre" else sala_encontrada['classificacao']
        if idade >= sala_encontrada['classificacao']:
            print(f"{nome}, você foi alocado na sala {escolha} e está apto para assistir ao filme {sala_encontrada['filme']}.")
            break
        else:
                print(f"{nome}, você não tem idade suficiente para assistir ao filme {sala_encontrada['filme']}.")
    else:
        print("Sala não encontrada! Por favor selecione uma sala disponível.")