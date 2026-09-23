"""
Conceito:
Tuplas são sequências ordenadas e imutáveis. São úteis para representar grupos
de valores que não devem ter sua estrutura modificada e para empacotamento e
desempacotamento de dados.

Sintaxe Básica / Assinatura:
tupla = (1, 2, 3)
a, b, c = tupla

Mapeamento de Módulos Nativo / Equivalência:
tuple é um tipo nativo do Python.

Pontos de Atenção:
1. Uma tupla com um único elemento precisa de vírgula: (10,).
2. A tupla é imutável, mas pode conter objetos internos mutáveis, como listas.
3. Desempacotamento exige quantidade compatível, salvo quando *resto é utilizado.
"""


def exemplo_tuplas() -> None:
    coordenada = (10, 25)
    x, y = coordenada

    nomes = ("Ana", "Bruno", "Carlos", "Daniel")
    primeiro, *meio, ultimo = nomes

    tupla_um_item = (42,)

    print(x, y)
    print(primeiro, meio, ultimo)
    print(tupla_um_item)