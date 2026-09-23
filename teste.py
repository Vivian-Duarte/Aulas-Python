#palavra secreta

import os

palavra = 'cachoeira'
letra_acertada = ''
numero_tentativas = 0

print('Vamos jogar um jogo de adivinhacao! Adivinhe a plavra secreta a partir das letras.\n')
while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    if len(letra_digitada) > 1:
        print('Digite apenas 1 letra.')
        continue

    if letra_digitada in palavra:
        letra_acertada += letra_digitada

    palavra_formada = ''
    for letra in palavra:
        if letra in letra_acertada:
            palavra_formada += letra
        else: 
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra:
        os.system('cls') #limpa tudo antes desse comando
        print('Parabens! Voce acertou.')
        print('A palavra era: cachoeira.')
        print('Tentativas: ', numero_tentativas)
        letra_acertada = ''
        numero_tentativas = 0
