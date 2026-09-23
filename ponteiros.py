"""
Conceito:
Python não expõe ponteiros para manipulação direta como C. Variáveis armazenam
referências para objetos, e múltiplas variáveis podem referenciar o mesmo objeto,
o que é especialmente importante para estruturas mutáveis.

Sintaxe Básica / Assinatura:
a = [1, 2]
b = a
b.append(3)
# a também passa a ser [1, 2, 3]

Mapeamento de Módulos Nativo / Equivalência:
A ideia equivalente a um ponteiro é uma referência gerenciada pelo Python. O
programador normalmente não aloca nem libera memória manualmente; a memória é
gerenciada pelo interpretador e pelo coletor de lixo.

Pontos de Atenção:
1. == compara valores; is verifica se duas referências apontam para o mesmo objeto.
2. Objetos mutáveis podem ser modificados através de qualquer referência compartilhada.
3. Evite usar is para comparar números ou strings; normalmente use == nesses casos.
"""


def exemplo_referencias() -> None:
    lista_a = [1, 2, 3]
    lista_b = lista_a

    lista_b.append(4)

    print(lista_a)  # [1, 2, 3, 4]
    print(lista_b)  # [1, 2, 3, 4]
    print(lista_a is lista_b)  # True: mesmo objeto.
    print(lista_a == lista_b)  # True: mesmos valores.
    print(id(lista_a), id(lista_b))
