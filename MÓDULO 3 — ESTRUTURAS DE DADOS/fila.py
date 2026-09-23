"""
Conceito:
Uma fila segue a regra FIFO: First In, First Out, ou seja, o primeiro elemento a
entrar é o primeiro a sair. deque é a opção padrão eficiente para uma fila
simples em um único fluxo de execução.

Sintaxe Básica / Assinatura:
from collections import deque
fila = deque()
fila.append(valor)
valor = fila.popleft()

Mapeamento de Módulos Nativo / Equivalência:
Python não possui um tipo literal FIFO na sintaxe. collections.deque fornece a
implementação eficiente mais comum para filas simples.

Pontos de Atenção:
1. append() e popleft() são O(1).
2. Evite list.pop(0), pois remover o primeiro elemento de list custa O(n).
3. Para comunicação segura entre threads, prefira queue.Queue.
"""


def exemplo_fila_deque() -> None:
    fila: deque[str] = deque()

    fila.append("Cliente 1")
    fila.append("Cliente 2")
    fila.append("Cliente 3")

    while fila:
        proximo = fila.popleft()
        print("Atendendo:", proximo)

"""
Conceito:
queue.Queue implementa uma fila FIFO sincronizada, adequada para comunicação
entre threads. Ela possui operações como put, get, task_done e join.

Sintaxe Básica / Assinatura:
from queue import Queue
fila = Queue()
fila.put(valor)
valor = fila.get()
fila.task_done()

Mapeamento de Módulos Nativo / Equivalência:
Queue pertence ao módulo padrão queue e é uma estrutura de nível mais alto do
que deque para cenários concorrentes com threads.

Pontos de Atenção:
1. get() pode bloquear esperando um item; use timeout quando necessário.
2. Chame task_done() uma vez para cada item obtido por get() quando usar join().
3. Para código assíncrono baseado em asyncio, existe asyncio.Queue.
"""


def exemplo_queue() -> None:
    fila: Queue[str] = Queue()

    fila.put("Tarefa A")
    fila.put("Tarefa B")

    while not fila.empty():
        try:
            tarefa = fila.get_nowait()
        except Empty:
            break
        else:
            print("Processando:", tarefa)
            fila.task_done()
