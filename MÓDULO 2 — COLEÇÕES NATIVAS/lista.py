
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

"""
Conceito:
Uma lista ligada é formada por nós em que cada nó guarda um valor e uma
referência para o próximo nó. Ela é útil didaticamente para entender referências
e pode oferecer inserção/remoção O(1) no início quando o nó é conhecido.

Sintaxe Básica / Assinatura:
no.valor
no.proximo

Código de Exemplo:
O bloco de código logo abaixo demonstra o conceito com uma aplicação prática.

Mapeamento de Módulos Nativo / Equivalência:
Python não possui uma linked list simples como tipo nativo. Em aplicações reais,
list ou collections.deque normalmente são preferidos, mas a estrutura pode ser
implementada com classes e referências de objetos.

Pontos de Atenção:
1. Acesso ao elemento de índice n custa O(n), pois é necessário percorrer os nós.
2. Inserção no início pode ser O(1); busca continua O(n).
3. Em Python, não há necessidade de liberar manualmente a memória dos nós desconectados.
"""


@dataclass
class NoLista:
    valor: object
    proximo: NoLista | None = None


class ListaLigada:
    def __init__(self) -> None:
        self.cabeca: NoLista | None = None

    def inserir_inicio(self, valor: object) -> None:
        self.cabeca = NoLista(valor, self.cabeca)

    def inserir_fim(self, valor: object) -> None:
        novo_no = NoLista(valor)

        if self.cabeca is None:
            self.cabeca = novo_no
            return

        atual = self.cabeca
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novo_no

    def remover_inicio(self) -> object:
        if self.cabeca is None:
            raise IndexError("A lista ligada está vazia.")

        valor = self.cabeca.valor
        self.cabeca = self.cabeca.proximo
        return valor

    def para_lista(self) -> list[object]:
        valores: list[object] = []
        atual = self.cabeca

        while atual is not None:
            valores.append(atual.valor)
            atual = atual.proximo

        return valores


def exemplo_lista_ligada() -> None:
    lista = ListaLigada()
    lista.inserir_inicio(20)
    lista.inserir_inicio(10)
    lista.inserir_fim(30)

    print(lista.para_lista())
    print(lista.remover_inicio())
    print(lista.para_lista())