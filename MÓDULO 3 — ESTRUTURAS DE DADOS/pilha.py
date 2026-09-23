"""
Conceito:
Uma pilha segue a regra LIFO: Last In, First Out, isto é, o último elemento a
entrar é o primeiro a sair. Em Python, uma list funciona muito bem como pilha
quando append e pop são usados no final.

Sintaxe Básica / Assinatura:
pilha = []
pilha.append(valor)
valor = pilha.pop()

Mapeamento de Módulos Nativo / Equivalência:
Python não possui um tipo nativo chamado Stack. list é a equivalência mais
simples e collections.deque também pode ser usado.

Pontos de Atenção:
1. append() e pop() no final da list são O(1) amortizado.
2. pop() em uma pilha vazia gera IndexError.
3. Não use insert(0, ...) para simular uma pilha; isso desloca elementos e custa O(n).
"""


def exemplo_pilha_list() -> None:
    pilha: list[str] = []

    pilha.append("página 1")
    pilha.append("página 2")
    pilha.append("página 3")

    topo = pilha[-1]
    removido = pilha.pop()

    print(topo)
    print(removido)
    print(pilha)

"""
Conceito:
collections.deque é uma fila de duas pontas que permite inserir e remover com
eficiência tanto no início quanto no final. Para uma pilha, use append e pop.

Sintaxe Básica / Assinatura:
from collections import deque
pilha = deque()
pilha.append(valor)
valor = pilha.pop()

Mapeamento de Módulos Nativo / Equivalência:
deque pertence ao módulo padrão collections; nenhuma biblioteca externa é necessária.

Pontos de Atenção:
1. append e pop nas extremidades são O(1).
2. Para uma pilha simples, list costuma ser suficiente e muito legível.
3. deque não é otimizado para acesso aleatório por índice no meio da estrutura.
"""


def exemplo_pilha_deque() -> None:
    pilha: deque[str] = deque()

    pilha.append("A")
    pilha.append("B")
    pilha.append("C")

    while pilha:
        print(pilha.pop())
