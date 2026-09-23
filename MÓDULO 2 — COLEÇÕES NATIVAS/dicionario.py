"""
Conceito:
Dicionários armazenam pares chave-valor e permitem localizar informações por uma
chave em vez de por posição. São muito usados para representar registros,
configurações, índices e mapeamentos.

Sintaxe Básica / Assinatura:
dados = {"chave": valor}
dados["chave"]
dados.get("chave")

Mapeamento de Módulos Nativo / Equivalência:
dict é um tipo nativo do Python. Em Python moderno, mantém a ordem de inserção.

Pontos de Atenção:
1. Busca, inserção e remoção por chave são O(1) em média.
2. dados["x"] gera KeyError se a chave não existir; get retorna None ou um padrão.
3. Chaves precisam ser hashable, como str, int e tuplas adequadamente imutáveis.
"""


def exemplo_dicionarios() -> None:
    aluno = {
        "nome": "Ana",
        "nota": 8.5,
        "aprovado": True,
    }

    # Inserção de nova chave.
    aluno["curso"] = "Sistemas de Informação"

    # Atualização de uma chave existente.
    aluno["nota"] = 9.0

    # Busca segura: se telefone não existir, devolve o texto informado.
    telefone = aluno.get("telefone", "Não informado")

    # setdefault cria a chave apenas se ela ainda não existir.
    aluno.setdefault("faltas", 0)

    # Percorre chave e valor.
    for chave, valor in aluno.items():
        print(chave, valor)

    # Remove a chave e devolve seu valor.
    curso = aluno.pop("curso")

    print(telefone)
    print(curso)
    print(aluno)
