"""
Conceito:
Atribuição apenas cria outra referência para o mesmo objeto. A cópia rasa cria
um novo contêiner, mas reaproveita referências para objetos internos; a cópia
profunda copia recursivamente também os objetos internos.

Sintaxe Básica / Assinatura:
b = a
b = a.copy()
b = copy.copy(a)
b = copy.deepcopy(a)

Mapeamento de Módulos Nativo / Equivalência:
list.copy() e dict.copy() fornecem cópias rasas. O módulo padrão copy fornece
copy.copy para cópia rasa e copy.deepcopy para cópia profunda.

Pontos de Atenção:
1. Uma cópia rasa não isola objetos aninhados mutáveis.
2. deepcopy pode consumir mais memória e tempo e nem sempre é necessário.
3. Antes de copiar, pergunte se imutabilidade ou um novo modelo de dados seria melhor.
"""


def exemplo_copias() -> None:
    original = [[1, 2], [3, 4]]

    alias = original
    copia_rasa = copy.copy(original)
    copia_profunda = copy.deepcopy(original)

    # Modifica uma lista interna compartilhada por original, alias e copia_rasa.
    original[0].append(99)

    print("original:", original)
    print("alias:", alias)
    print("cópia rasa:", copia_rasa)
    print("cópia profunda:", copia_profunda)

    print(alias is original)  # True.
    print(copia_rasa is original)  # False.
    print(copia_rasa[0] is original[0])  # True: objeto interno compartilhado.
    print(copia_profunda[0] is original[0])  # False.
