
"""
Conceito:
Listas armazenam uma sequência ordenada e mutável de objetos. São úteis quando
os elementos precisam ser adicionados, removidos, alterados ou percorridos.

Sintaxe Básica / Assinatura:
lista = [valor1, valor2, valor3]
lista.append(valor)
lista[index]

Mapeamento de Módulos Nativo / Equivalência:
list é um tipo nativo do Python e não exige importação.

Pontos de Atenção:
1. append no final é O(1) amortizado, mas inserir/remover no início tende a ser O(n).
2. A atribuição lista_b = lista_a cria um alias; as duas variáveis apontam para a mesma lista.
3. Índices negativos acessam a lista de trás para frente, por exemplo lista[-1].
"""

string = 'ADVB'
lista = [123, True, 'Vivian', 1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))

#        0   1  2   3
lista = [12, 3, 56, 77]
lista.append(43) #adiciona o numero 43 ao final da lista
lista.append(3455)
ultimo_valor = lista.pop() #remove o ultimo item da lista
lista.append(1)
lista.pop(2) #remove o indice 2
print(lista, 'Removido,', ultimo_valor)
del lista [-1] #deleta o ultimo item da lista
print(lista)
lista.insert(0, 'v') #adiciona no indice 0 a string v
print(lista)
print(lista [4]) #imprime o valor do indice 4
lista.clear() #limpa a lista
print(lista)


lista_a = [1, 2, 4]
lista_b = [5, 78, 55]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) #estende a lista
print(lista_c)

#a lista_b aponta para o mesmo endereco de memoria que a lista_a
lista_a = ['abaobora', 3, 566]
lista_b = lista_a
print(lista_b)

lista_a = ['abaobora', 3, 566]
lista_b = lista_a.copy() #copia a lista_a para dentro da lista_b
print(lista_b)


#mostra os indices com seus valores e tipos
lista = ['maria', 'ana', 'o', 9] 
lista.append('joao')
indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

nome1, nome2, nome3 = ['maria', 'noah', 'miguel']
print(nome2)

nome1, *_ = ['maria', 'noah', 'miguel'] #*_ significa resto da variavel
print(nome2, _)


 #enumera intens de uma lista
lista = ['maria', 'noah', 'miguel']
lista.append('ana')
lista_enumerada = list(enumerate(lista)) 
print(lista_enumerada)
#enumera intens de uma lista
lista = ['maria', 'noah', 'miguel']
lista.append('ana')
for indice, nome in enumerate(lista):
    print(indice, nome)

"""
Conceito:
List comprehensions são uma forma compacta de criar listas a partir de outros
iteráveis. São apropriadas para transformações ou filtros simples e legíveis.

Sintaxe Básica / Assinatura:
resultado = [expressao for item in iteravel]
resultado = [expressao for item in iteravel if condicao]

Mapeamento de Módulos Nativo / Equivalência:
É uma construção sintática nativa do Python.

Pontos de Atenção:
1. Evite comprehensions muito complexas; um for comum pode ser mais legível.
2. A list comprehension cria a lista inteira em memória.
3. Para grandes volumes processados sob demanda, considere uma expressão geradora.
"""


def exemplo_list_comprehension() -> None:
    numeros = [1, 2, 3, 4, 5, 6]

    quadrados = [numero**2 for numero in numeros]
    pares = [numero for numero in numeros if numero % 2 == 0]
    quadrados_dos_pares = [numero**2 for numero in numeros if numero % 2 == 0]

    print(quadrados)
    print(pares)
    print(quadrados_dos_pares)