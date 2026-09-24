"""
Conceito:
Python passa referências de objetos para funções por atribuição. Se a função
recebe um objeto mutável e o modifica internamente, o chamador pode observar a
mudança; reatribuir apenas o nome local não substitui o objeto do chamador.

Sintaxe Básica / Assinatura:
def alterar(lista):
    lista.append(1)

Mapeamento de Módulos Nativo / Equivalência:
Esse comportamento deriva do modelo de objetos e referências do Python; não é
passagem por ponteiro explícito como em C nem uma cópia automática do argumento.

Pontos de Atenção:
1. list, dict e set são mutáveis; str, int, float e tuple são essencialmente imutáveis.
2. Documente quando uma função modifica o objeto recebido.
3. Quando não quiser efeitos colaterais, crie e devolva um novo objeto.
"""


def adicionar_sem_copiar(valores: list[int], numero: int) -> None:
    valores.append(numero)


def adicionar_com_nova_lista(valores: list[int], numero: int) -> list[int]:
    return [*valores, numero]


def exemplo_mutabilidade() -> None:
    numeros = [1, 2]

    adicionar_sem_copiar(numeros, 3)
    print(numeros)  # A lista original foi alterada.

    nova_lista = adicionar_com_nova_lista(numeros, 4)
    print(numeros)  # Continua [1, 2, 3].
    print(nova_lista)  # Nova lista: [1, 2, 3, 4].
