"""
Conceito:
Uma árvore binária é uma estrutura hierárquica em que cada nó possui no máximo
dois filhos: esquerdo e direito. Percursos definem a ordem de visita aos nós e
são fundamentais para processamento de expressões, árvores de busca e hierarquias.

Sintaxe Básica / Assinatura:
pre_ordem: raiz -> esquerda -> direita
em_ordem:  esquerda -> raiz -> direita
pos_ordem: esquerda -> direita -> raiz

Código de Exemplo:
O bloco de código logo abaixo demonstra o conceito com uma aplicação prática.

Mapeamento de Módulos Nativo / Equivalência:
Python não oferece uma classe de árvore binária na biblioteca built-in. Uma
implementação simples usa classes/dataclasses cujos atributos referenciam outros nós.

Pontos de Atenção:
1. Em uma árvore de busca binária válida, o percurso em ordem produz valores ordenados.
2. Os percursos abaixo custam O(n), pois visitam cada nó uma vez.
3. Árvores muito profundas podem atingir o limite de recursão do Python.
"""


@dataclass
class NoArvore:
    valor: int
    esquerda: NoArvore | None = None
    direita: NoArvore | None = None


def percurso_pre_ordem(no: NoArvore | None) -> list[int]:
    if no is None:
        return []

    # Visita primeiro a raiz, depois esquerda e direita.
    return [no.valor] + percurso_pre_ordem(no.esquerda) + percurso_pre_ordem(no.direita)


def percurso_em_ordem(no: NoArvore | None) -> list[int]:
    if no is None:
        return []

    # Visita esquerda, raiz e direita.
    return percurso_em_ordem(no.esquerda) + [no.valor] + percurso_em_ordem(no.direita)


def percurso_pos_ordem(no: NoArvore | None) -> list[int]:
    if no is None:
        return []

    # Visita esquerda e direita antes da raiz.
    return percurso_pos_ordem(no.esquerda) + percurso_pos_ordem(no.direita) + [no.valor]


def exemplo_arvore_binaria() -> None:
    #              8
    #            /   \
    #           4     12
    #          / \    / \
    #         2   6  10 14
    raiz = NoArvore(
        8,
        esquerda=NoArvore(4, NoArvore(2), NoArvore(6)),
        direita=NoArvore(12, NoArvore(10), NoArvore(14)),
    )

    print("Pré-ordem:", percurso_pre_ordem(raiz))
    print("Em ordem:", percurso_em_ordem(raiz))
    print("Pós-ordem:", percurso_pos_ordem(raiz))
