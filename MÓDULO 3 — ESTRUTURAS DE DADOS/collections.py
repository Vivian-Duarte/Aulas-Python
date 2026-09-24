"""
Conceito:
collections reúne estruturas especializadas para problemas comuns envolvendo
coleções. Entre as mais usadas estão deque, Counter, defaultdict e namedtuple,
que complementam list, dict, tuple e set.

Sintaxe Básica / Assinatura:
from collections import Counter, defaultdict, deque, namedtuple

Código de Exemplo:
O bloco de código logo abaixo demonstra o conceito com uma aplicação prática.

Mapeamento de Módulos Nativo / Equivalência:
collections pertence à biblioteca padrão do Python; não é necessário instalar
pacotes externos. Cada estrutura atende a um padrão de uso específico.

Pontos de Atenção:
1. Não use uma estrutura especializada quando o tipo nativo já representa bem o problema.
2. deque é ideal para operações nas duas extremidades; Counter para frequências.
3. Consulte a semântica da estrutura antes de escolher apenas por conveniência.
"""


def exemplo_collections() -> None:
    fila = deque(["A", "B"])
    fila.append("C")
    print(fila.popleft())

    frequencias = Counter("banana")
    print(frequencias)

    grupos = defaultdict(list)
    grupos["python"].append("Ana")
    print(dict(grupos))

"""
Conceito:
Counter é um dicionário especializado em contagem de elementos hashable. É útil
para frequências de palavras, votos, caracteres, categorias e outros problemas
de contagem.

Sintaxe Básica / Assinatura:
contador = Counter(iteravel)
contador[elemento]
contador.most_common(n)

Código de Exemplo:
O bloco de código logo abaixo demonstra o conceito com uma aplicação prática.

Mapeamento de Módulos Nativo / Equivalência:
Counter vem de collections e funciona de maneira semelhante a dict[elemento] = quantidade,
mas automatiza a inicialização e oferece operações próprias para contadores.

Pontos de Atenção:
1. Consultar uma chave ausente retorna 0 em vez de KeyError.
2. most_common() facilita recuperar os itens mais frequentes.
3. Counter mantém contagens e pode conter valores zero ou negativos após operações manuais.
"""


def exemplo_counter() -> None:
    linguagens = ["Python", "C", "Python", "Java", "Python", "C"]
    contador = Counter(linguagens)

    print(contador["Python"])
    print(contador["Rust"])  # Chave ausente: 0.
    print(contador.most_common(2))

"""
Conceito:
defaultdict é uma especialização de dict que cria automaticamente um valor
padrão para chaves ainda inexistentes. É muito útil para agrupamentos, contagens
e construção de estruturas aninhadas simples.

Sintaxe Básica / Assinatura:
dicionario = defaultdict(fabrica_padrao)

Código de Exemplo:
O bloco de código logo abaixo demonstra o conceito com uma aplicação prática.

Mapeamento de Módulos Nativo / Equivalência:
defaultdict vem de collections. Um padrão semelhante com dict seria usar
setdefault() ou verificar manualmente se a chave já existe.

Pontos de Atenção:
1. A fábrica padrão deve ser uma função ou callable, como list, int ou set.
2. Acessar uma chave ausente com [] cria essa chave automaticamente.
3. Se não quiser criar a chave durante consulta, use get() conscientemente.
"""


def exemplo_defaultdict() -> None:
    alunos_por_turma: defaultdict[str, list[str]] = defaultdict(list)

    alunos_por_turma["A"].append("Ana")
    alunos_por_turma["A"].append("Bruno")
    alunos_por_turma["B"].append("Carlos")

    print(dict(alunos_por_turma))

    contagem: defaultdict[str, int] = defaultdict(int)
    for letra in "banana":
        contagem[letra] += 1
    print(dict(contagem))
