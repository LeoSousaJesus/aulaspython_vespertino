# Crie um programa que realiza a contagem de 1 até 100, usando apenas números ímpares, 
# ao final do processo exiba em tela quantos números ímpares foram emcontrados nesse intervalo, assim como a soma dos mesmos:

cont = 0
somar = 0

for i in range(1, 101):
    if i % 2 == 1:
        
        somar += i
        cont += 1

print(f'Existe na lista {cont} números ímpares')
print(f'A soma dos números ímpares é: {somar}')