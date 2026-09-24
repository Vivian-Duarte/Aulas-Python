"""
Conceito:
Um heap mantém o menor elemento acessível com eficiência e pode implementar uma
fila de prioridade. Em Python, heapq trabalha diretamente sobre uma list e usa
por padrão a propriedade de min-heap.

Sintaxe Básica / Assinatura:
heapq.heappush(heap, item)
menor = heapq.heappop(heap)
heapq.heapify(lista)

Código de Exemplo:
O bloco de código logo abaixo demonstra o conceito com uma aplicação prática.

Mapeamento de Módulos Nativo / Equivalência:
Python não possui um tipo Heap nativo separado; o módulo heapq da biblioteca
padrão fornece as operações sobre uma list comum.

Pontos de Atenção:
1. heappush() e heappop() custam O(log n); consultar heap[0] custa O(1).
2. A lista interna não fica totalmente ordenada; apenas respeita a propriedade do heap.
3. Para prioridades compostas, tuplas como (prioridade, item) são uma solução comum.
"""


def exemplo_heap() -> None:
    tarefas: list[tuple[int, str]] = []

    # Quanto menor o número, maior a prioridade neste exemplo.
    heapq.heappush(tarefas, (2, "Responder e-mails"))
    heapq.heappush(tarefas, (1, "Corrigir falha crítica"))
    heapq.heappush(tarefas, (3, "Atualizar documentação"))

    while tarefas:
        prioridade, tarefa = heapq.heappop(tarefas)
        print(prioridade, tarefa)