"""
Conceito:
Generators são iteradores produzidos por funções com yield ou por generator
expressions. Eles calculam valores sob demanda, preservando o estado entre as
iterações sem precisar armazenar todos os resultados de uma vez.

Sintaxe Básica / Assinatura:
def gerador():
    yield valor

gerador_por_expressao = (expressao for item in iteravel)

Código de Exemplo:
O bloco de código logo abaixo demonstra o conceito com uma aplicação prática.

Mapeamento de Módulos Nativo / Equivalência:
yield e generator expressions são recursos nativos do Python. Um generator
implementa automaticamente o protocolo de iterator, incluindo __iter__ e __next__.

Pontos de Atenção:
1. Generators são consumidos durante a iteração e não podem ser reiniciados automaticamente.
2. Eles economizam memória em sequências grandes porque geram um valor por vez.
3. Se precisar reutilizar todos os resultados várias vezes, uma list pode ser mais apropriada.
"""


def gerar_pares(limite: int):
    numero = 0

    while numero <= limite:
        if numero % 2 == 0:
            yield numero
        numero += 1


def exemplo_generators() -> None:
    pares = gerar_pares(10)

    # Cada chamada de next() continua do ponto em que o generator parou.
    print(next(pares))
    print(next(pares))

    # Generator expression: não cria uma lista de quadrados antecipadamente.
    quadrados = (numero**2 for numero in range(5))
    for quadrado in quadrados:
        print(quadrado)