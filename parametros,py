"""
Conceito:
Parâmetros recebem os dados usados por uma função. *args captura uma quantidade
variável de argumentos posicionais em uma tupla, enquanto **kwargs captura
argumentos nomeados em um dicionário.

Sintaxe Básica / Assinatura:
def funcao(obrigatorio, padrao=0, *args, **kwargs):
    ...

Mapeamento de Módulos Nativo / Equivalência:
*args e **kwargs fazem parte da sintaxe nativa do Python. Os nomes args e kwargs
são convenções; os símbolos * e ** são o que realmente produz o comportamento.

Pontos de Atenção:
1. Não use *args/**kwargs quando uma assinatura explícita deixar a função mais clara.
2. Parâmetros com valores padrão mutáveis, como [], podem compartilhar estado entre chamadas.
3. **kwargs aceita nomes de argumento; internamente esses valores chegam como dict.
"""


def calcular_media(*valores: float) -> float:
    if not valores:
        return 0.0

    return sum(valores) / len(valores)


def criar_usuario(nome: str, **dados_extras: object) -> dict[str, object]:
    usuario: dict[str, object] = {"nome": nome}
    usuario.update(dados_extras)
    return usuario


def adicionar_item(item: str, itens: list[str] | None = None) -> list[str]:
    # Em vez de usar itens=[] como padrão, usamos None para evitar estado compartilhado.
    if itens is None:
        itens = []

    itens.append(item)
    return itens


def exemplo_parametros() -> None:
    print(calcular_media(7.5, 8.0, 9.5))

    usuario = criar_usuario(
        "Nicholas",
        idade=22,
        cidade="João Monlevade",
        ativo=True,
    )
    print(usuario)

    print(adicionar_item("Python"))