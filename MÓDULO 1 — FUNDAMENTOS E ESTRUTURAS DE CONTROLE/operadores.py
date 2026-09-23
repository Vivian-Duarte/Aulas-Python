#and, or e not são operadores lógicos que verificam condicoes em expressoes. 

#and significa “e”: só é True quando todas as condições são verdadeiras.
idade = 18
tem_carteira = True

if idade >= 18 and tem_carteira: #and significa “e”: só é True quando todas as condições são verdadeiras.
    print("Pode dirigir")


#or significa “ou”: é True quando pelo menos uma das condições é verdadeira.
chovendo = False
frio = True

if chovendo or frio:
    print("Leve uma blusa") 

#not significa negação: ele inverte o valor lógico.
tem_tarefa = False

if not tem_tarefa: 
    print("Pode brincar")


#in, not in sao operadores de associacao. Verifica se um valor esta presente ou nao dentro de: string, listas, tuplas, dicionarios


#Retorna True se o valor existe na sequência.
nome = "Nicholas"

if "N" in nome: 
    print("Existe a letra N")


numeros = [1, 2, 3, 4]

if 3 in numeros:
    print("Número encontrado")


#Retorna True se o valor não existe na sequência.

nome = "Nicholas"

if "z" not in nome: 
    print("Não existe a letra z")


numeros = [1, 2, 3, 4]

if 5 not in numeros:
    print("Número não encontrado")


#interpolacao
nome = 'Luiz'
preco = 123.44
variavel = '%s, preco e R$%.2f' % (nome, preco)
print(variavel)


#hexadecimal = %X
print('O haxadecimal de %d e %02X' % (11, 11))

#is verifica se duas variáveis apontam para o mesmo objeto na memória.
a = [1, 2, 3]
b = a

print(a is b)  # True (mesmo objeto)

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # False (objetos diferentes)
print(a == b)  # True (valores iguais)

#not = não é o mesmo objeto
a = [1, 2, 3]
b = [1, 2, 3]

print(a is not b)  # True

# None = nenhum valor ou vazio.
valor = None

if valor is None:
    print("Não tem valor")