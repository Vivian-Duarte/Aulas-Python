"""
Conceito:
Funções agrupam instruções reutilizáveis sob um nome e ajudam a dividir um
problema grande em partes menores. Use def para declarar a função e return para
devolver um resultado ao código chamador.

Sintaxe Básica / Assinatura:
def nome_funcao(parametro):
    resultado = ...
    return resultado

Mapeamento de Módulos Nativo / Equivalência:
Funções são objetos de primeira classe e fazem parte do núcleo da linguagem;
não é necessário importar nenhum módulo para criá-las.

Pontos de Atenção:
1. Uma função sem return explícito retorna None.
2. Prefira funções pequenas, com uma responsabilidade clara.
3. Evite depender excessivamente de variáveis globais; passe dados por parâmetros.
"""


def somar(a: float, b: float) -> float:
    # Os type hints documentam os tipos esperados, mas não os impõem em execução.
    resultado = a + b
    return resultado


def dividir_com_resto(dividendo: int, divisor: int) -> tuple[int, int]:
    # Python pode retornar vários valores; na prática eles são empacotados em uma tupla.
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto


def exemplo_funcoes() -> None:
    total = somar(10, 5)
    print(total)

    quociente, resto = dividir_com_resto(17, 5)
    print(quociente, resto)