"""
Conceito:
Python não possui struct como C. namedtuple permite criar registros leves,
imutáveis e acessíveis por nomes de campos, sendo útil para pequenos grupos de
dados que não precisam de comportamento complexo.

Sintaxe Básica / Assinatura:
from collections import namedtuple
Pessoa = namedtuple("Pessoa", ["nome", "idade"])
pessoa = Pessoa("Ana", 20)

Mapeamento de Módulos Nativo / Equivalência:
namedtuple, do módulo collections, é uma das equivalências de struct. Outra
opção moderna e mais flexível é dataclasses.dataclass.

Pontos de Atenção:
1. Instâncias de namedtuple são imutáveis.
2. Campos nomeados melhoram a legibilidade em relação a tuplas comuns.
3. Para validações, métodos e muitos valores padrão, dataclass costuma ser melhor.
"""


PessoaNT = namedtuple("PessoaNT", ["nome", "idade"])


def exemplo_namedtuple() -> None:
    pessoa = PessoaNT("Ana", 21)

    print(pessoa.nome)
    print(pessoa.idade)

    # _replace cria uma NOVA instância porque namedtuple é imutável.
    pessoa_atualizada = pessoa._replace(idade=22)
    print(pessoa_atualizada)

"""
Conceito:
@dataclass reduz o código repetitivo necessário para classes cujo objetivo
principal é armazenar dados. Automaticamente pode gerar __init__, __repr__,
__eq__ e outros métodos especiais.

Sintaxe Básica / Assinatura:
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

Mapeamento de Módulos Nativo / Equivalência:
dataclass pertence ao módulo padrão dataclasses e é a equivalência moderna mais
comum para muitos usos de struct em Python.

Pontos de Atenção:
1. Dataclasses são mutáveis por padrão; use @dataclass(frozen=True) para imutabilidade.
2. Use default_factory para campos mutáveis, como listas.
3. Type hints documentam tipos, mas validação automática não é feita pela dataclass.
"""


@dataclass(slots=True)
class Produto:
    nome: str
    preco: float
    estoque: int = 0

    def valor_em_estoque(self) -> float:
        return self.preco * self.estoque


def exemplo_dataclass() -> None:
    produto = Produto(nome="Teclado", preco=250.0, estoque=3)

    print(produto)
    print(produto.valor_em_estoque())

    produto.estoque += 2
    print(produto.estoque)
