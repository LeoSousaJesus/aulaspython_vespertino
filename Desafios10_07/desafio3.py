def primo(numero):
    if numero <= 1:
        return False, 0
    
    divisor = 0
    for i in range(2, numero):
        if numero % i == 0:
            divisor += 1

    if divisor == 0:
        return True, 0
    else:
        return False, divisor

numero = int(input("Digite um número: "))


primo, divisor = primo(numero)

if primo:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo e é divisível {divisor} vezes.")
