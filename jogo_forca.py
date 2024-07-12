import random

lista_palavras = ['python', 'programação', 'computador', 'notebook', 'software', 'openai', 'hardware']

palavra = random.choice(lista_palavras)# palavra secreta escolhida aleatoriamente
letras_corretas = []
letras_erradas = []
tentativas = 6

while True:
    palavra_escondida = ''
    for letra in palavra:
        if letra in letras_corretas:
            palavra_escondida += letra
        else:
            palavra_escondida += '-'

    print('Palavra:', palavra_escondida)
    print('Letras erradas:', letras_erradas)
    print('Tentativas restantes:', tentativas)

    if palavra_escondida == palavra:
        print('Você acertou')
        break
    elif tentativas == 0:
        print('Você perdeu! A palvra era: ', palavra)
        break
    
    letra_usuario = input('Digite uma letra: ').lower()

    # Verificando a letra digitada
    if letra_usuario in palavra:
        print('Letra correta!')
        letras_corretas.append(letra_usuario)
    else:
        print('Letra incorreta!')
        letras_erradas.append(letra_usuario)
        tentativas -= 1