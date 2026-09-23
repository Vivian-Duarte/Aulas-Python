print('a' + 'b') #concatena

a_dez_vezes = 'A' * 10
print(a_dez_vezes)

a = 'VNKK'
b = 1.2
string = 'a={0} b={1:.2f} a={0} a={0}' #o 0 e 1 sao os indices que indicam a ordem de a e de b
formato = string.format(a, b)
print(formato)

#outro modo de formatar
variavel = 'AB'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <2}')
print(f'{variavel: >8}')
print(f'{variavel: ^10}')

print(f'{7238.344: >+.2f}')


#fatiamento de strings
variavel = 'chocolate com pimenta'
print(variavel[4:11]) #comeca do indice 4 e vai ate o 11

#conta o tamanho da string
variavel = 'chocolate com pimenta'
print(len(variavel))

#comeca do indice 0, vai ate o final e pula de 6 em 6 caracteres
variavel = 'chocolate com pimenta'
print(variavel[0:len(variavel):6])


#inverso
nome=input('Seu nome e: ')
print(nome)
print('Ó inverso de %s e: %s ' % (nome, nome[::-1]))
print('Seu nome tem: ', len(nome))
print('Á primeira letra do nome e: ', nome[0])
print('Á primeira letra do nome e: ', nome[-1])

#conta quandas vezes o caratere aparece
frase = 'Abobora com quiabo e frango.'
print(frase.count('a'))



 

