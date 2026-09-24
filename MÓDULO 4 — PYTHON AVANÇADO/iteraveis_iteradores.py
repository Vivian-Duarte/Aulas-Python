"""
Conceito:
Um iterável é um objeto capaz de fornecer um iterador, como list, tuple, str,
dict e set. Um iterador mantém o estado da travessia e entrega o próximo valor
por meio de next() até gerar StopIteration.

Sintaxe Básica / Assinatura:
iterador = iter(iteravel)
valor = next(iterador)

Código de Exemplo:
O bloco de código logo abaixo demonstra o conceito com uma aplicação prática.

Mapeamento de Módulos Nativo / Equivalência:
iter() e next() são funções built-in. O protocolo de iteração usa os métodos
especiais __iter__() e __next__(), que também podem ser implementados em classes próprias.

Pontos de Atenção:
1. Todo iterador é iterável, mas nem todo iterável é o próprio iterador.
2. Um iterador normalmente é consumido: depois de esgotado, não reinicia sozinho.
3. O for chama iter() e next() internamente até receber StopIteration.
"""


class ContagemRegressiva:
    def __init__(self, inicio: int) -> None:
        self.atual = inicio

    def __iter__(self) -> ContagemRegressiva:
        return self

    def __next__(self) -> int:
        if self.atual <= 0:
            raise StopIteration

        valor = self.atual
        self.atual -= 1
        return valor


def exemplo_iteraveis_iteradores() -> None:
    numeros = [10, 20, 30]
    iterador = iter(numeros)

    print(next(iterador))
    print(next(iterador))
    print(next(iterador))

    for numero in ContagemRegressiva(3):
        print(numero)
