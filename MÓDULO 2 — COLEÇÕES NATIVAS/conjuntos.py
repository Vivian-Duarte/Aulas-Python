"""
Conceito:
Sets armazenam elementos únicos e não fornecem acesso por índice. São úteis para
remover duplicatas, testar pertinência e executar operações matemáticas de
conjuntos, como união, interseção e diferença.

Sintaxe Básica / Assinatura:
conjunto = {1, 2, 3}
conjunto.add(4)

Mapeamento de Módulos Nativo / Equivalência:
set é um tipo nativo do Python. O conjunto vazio deve ser criado com set(), pois
{} cria um dicionário vazio.

Pontos de Atenção:
1. Testes de pertinência com in são O(1) em média.
2. A ordem de um set não deve ser usada como regra de negócio.
3. Os elementos precisam ser hashable; uma list não pode ser item de um set.
"""


def exemplo_sets() -> None:
    grupo_a = {1, 2, 3, 4}
    grupo_b = {3, 4, 5, 6}

    uniao = grupo_a | grupo_b
    intersecao = grupo_a & grupo_b
    diferenca = grupo_a - grupo_b
    diferenca_simetrica = grupo_a ^ grupo_b

    grupo_a.add(10)
    grupo_a.discard(999)  # Não gera erro se o valor não existir.

    print(uniao)
    print(intersecao)
    print(diferenca)
    print(diferenca_simetrica)
    print(3 in grupo_a)
