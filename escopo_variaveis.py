"""
Conceito:
Escopo determina onde um nome pode ser acessado. Python procura nomes seguindo,
de forma simplificada, a regra LEGB: Local, Enclosing, Global e Built-in.

Sintaxe Básica / Assinatura:
valor_global = 10

def funcao():
    valor_local = 20

Mapeamento de Módulos Nativo / Equivalência:
Escopo é parte do funcionamento nativo da linguagem. As palavras global e
nonlocal existem para reatribuir nomes de escopos externos, mas devem ser usadas
com moderação.

Pontos de Atenção:
1. Uma variável local existe apenas no escopo da função em que foi criada.
2. Evite modificar estado global desnecessariamente.
3. Objetos mutáveis globais podem ser modificados sem global, mas isso aumenta acoplamento.
"""


TAXA_PADRAO = 0.10


def calcular_preco_final(preco: float) -> float:
    desconto_local = 5.0
    return preco * (1 + TAXA_PADRAO) - desconto_local


def exemplo_escopo() -> None:
    print(calcular_preco_final(100.0))