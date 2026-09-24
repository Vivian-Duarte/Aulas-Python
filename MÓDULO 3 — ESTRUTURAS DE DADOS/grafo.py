"""
Conceito:
Um grafo representa vértices conectados por arestas e é usado em redes, mapas,
relacionamentos, dependências e rotas. Uma representação simples em Python usa
um dicionário de conjuntos como lista de adjacência.

Sintaxe Básica / Assinatura:
grafo = {
    vertice: {vizinho_1, vizinho_2}
}

Código de Exemplo:
O bloco de código logo abaixo demonstra o conceito com uma aplicação prática.

Mapeamento de Módulos Nativo / Equivalência:
Não existe um tipo grafo built-in. dict + set implementam uma lista de adjacência;
para projetos especializados existem bibliotecas externas, mas não são necessárias
aqui para compreender a estrutura fundamental.

Pontos de Atenção:
1. Em grafos não direcionados, uma aresta A-B deve ser registrada nos dois sentidos.
2. BFS usa naturalmente uma fila; DFS pode usar pilha ou recursão.
3. Use um conjunto de visitados para evitar ciclos infinitos durante a busca.
"""


class Grafo:
    def __init__(self) -> None:
        self.adjacencias: dict[str, set[str]] = {}

    def adicionar_vertice(self, vertice: str) -> None:
        self.adjacencias.setdefault(vertice, set())

    def adicionar_aresta(self, origem: str, destino: str) -> None:
        # Este exemplo representa um grafo não direcionado.
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.adjacencias[origem].add(destino)
        self.adjacencias[destino].add(origem)

    def bfs(self, inicio: str) -> list[str]:
        if inicio not in self.adjacencias:
            return []

        visitados = {inicio}
        fila = deque([inicio])
        ordem: list[str] = []

        while fila:
            atual = fila.popleft()
            ordem.append(atual)

            for vizinho in sorted(self.adjacencias[atual]):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

        return ordem

    def dfs(self, inicio: str) -> list[str]:
        if inicio not in self.adjacencias:
            return []

        visitados: set[str] = set()
        ordem: list[str] = []

        def visitar(vertice: str) -> None:
            visitados.add(vertice)
            ordem.append(vertice)

            for vizinho in sorted(self.adjacencias[vertice]):
                if vizinho not in visitados:
                    visitar(vizinho)

        visitar(inicio)
        return ordem


def exemplo_grafos() -> None:
    grafo = Grafo()
    grafo.adicionar_aresta("A", "B")
    grafo.adicionar_aresta("A", "C")
    grafo.adicionar_aresta("B", "D")
    grafo.adicionar_aresta("C", "D")

    print("BFS:", grafo.bfs("A"))
    print("DFS:", grafo.dfs("A"))