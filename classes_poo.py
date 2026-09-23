"""
Conceito:
Classes definem novos tipos de objetos reunindo estado e comportamento. __init__
inicializa uma instância, self representa a própria instância e métodos de
instância operam sobre seus atributos.

Sintaxe Básica / Assinatura:
class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor

    def metodo(self):
        ...

Mapeamento de Módulos Nativo / Equivalência:
Classes são uma funcionalidade nativa do Python. Em Python, praticamente tudo é
objeto, inclusive funções, classes, listas e números.

Pontos de Atenção:
1. self deve ser o primeiro parâmetro dos métodos de instância por convenção.
2. Mantenha os atributos em um estado válido e concentre regras relacionadas na classe.
3. Não transforme toda estrutura de dados em classe; use classes quando houver ganho de modelagem.
"""


class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0) -> None:
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O depósito deve ser maior que zero.")

        self.saldo += valor

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O saque deve ser maior que zero.")

        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para o saque.")

        self.saldo -= valor

    def exibir_saldo(self) -> str:
        return f"{self.titular}: R$ {self.saldo:.2f}"


def exemplo_classes() -> None:
    conta = ContaBancaria("Ana", 100.0)

    conta.depositar(50.0)
    conta.sacar(30.0)

    print(conta.exibir_saldo())