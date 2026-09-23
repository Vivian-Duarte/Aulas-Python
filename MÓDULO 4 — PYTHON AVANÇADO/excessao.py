"""
Conceito:
Exceções representam situações anormais que interrompem o fluxo normal de um
programa. try/except permite capturar erros esperados; else executa se não
ocorrer erro e finally executa independentemente do resultado.

Sintaxe Básica / Assinatura:
try:
    ...
except TipoDeErro:
    ...
else:
    ...
finally:
    ...

Mapeamento de Módulos Nativo / Equivalência:
O mecanismo de exceções é nativo do Python. As exceções padrão, como ValueError,
TypeError e KeyError, derivam de BaseException por meio de Exception.

Pontos de Atenção:
1. Capture exceções específicas em vez de usar except: sem tipo.
2. Não use exceções para esconder erros de programação inesperados.
3. finally é útil para limpeza, mas recursos como arquivos devem preferir with.
"""

"""
try :
    ...
    except:
        ...
"""
#tratamento de excassao (erro caso eu digite algo que nao e um numero)
numero_str = input('Vou dobrar o numero que voce digitar: ')
try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} e {numero_float * 2}')
except:
    print('Isso nao e um numero')

"""
Conceito:
Exceções customizadas permitem representar erros específicos do domínio da
aplicação. Elas normalmente herdam de Exception e são lançadas explicitamente
com raise quando uma regra inválida é detectada.

Sintaxe Básica / Assinatura:
class MinhaExcecao(Exception):
    pass

raise MinhaExcecao("mensagem")

Mapeamento de Módulos Nativo / Equivalência:
Classes de exceção são classes Python comuns que herdam de Exception.

Pontos de Atenção:
1. Use nomes terminados em Error para manter a convenção do Python.
2. Crie exceções customizadas quando o erro tiver significado real no domínio.
3. Preserve a causa original com raise NovaExcecao(...) from erro quando necessário.
"""


class SaldoInsuficienteError(Exception):
    """Erro lançado quando uma operação exige saldo maior que o disponível."""


def sacar(saldo: float, valor: float) -> float:
    if valor <= 0:
        raise ValueError("O valor do saque deve ser maior que zero.")

    if valor > saldo:
        raise SaldoInsuficienteError(
            f"Saldo insuficiente: saldo={saldo:.2f}, saque={valor:.2f}."
        )

    return saldo - valor


def exemplo_excecao_customizada() -> None:
    try:
        novo_saldo = sacar(100.0, 150.0)
    except SaldoInsuficienteError as erro:
        print("Operação negada:", erro)
    else:
        print("Novo saldo:", novo_saldo)
