Aulas Python

Repositório criado para organizar estudos, exemplos práticos e implementações em Python, com foco em fundamentos da linguagem, coleções nativas, estruturas de dados e conceitos de programação mais avançados.

O material está dividido em módulos para facilitar a consulta e a evolução dos estudos.

Versão recomendada: Python 3.10 ou superior.

Estrutura do repositório

aulas_Python2026/
│
├── MÓDULO 1 — FUNDAMENTOS E ESTRUTURAS DE CONTROLE/
│   ├── escopo_variaveis.py
│   ├── for.py
│   ├── funçao.py
│   ├── jogo_palavra_secreta.py
│   ├── operadores.py
│   ├── parametros.py
│   ├── tipos.py
│   └── while_else.py
│
├── MÓDULO 2 — COLEÇÕES NATIVAS/
│   ├── conjuntos.py
│   ├── dicionario.py
│   ├── lista.py
│   ├── string.py
│   └── tuplas.py
│
├── MÓDULO 3 — ESTRUTURAS DE DADOS/
│   ├── arvore_binaria.py
│   ├── atribuicao_e_copias.py
│   ├── collections.py
│   ├── fila.py
│   ├── grafo.py
│   ├── heap.py
│   ├── mutabilidade.py
│   ├── pilha.py
│   ├── ponteiros_referencias.py
│   └── structs_equivalentes.py
│
├── MÓDULO 4 — PYTHON AVANÇADO/
│   ├── classes_poo.py
│   ├── excessao.py
│   ├── generators.py
│   ├── iteraveis_iteradores.py
│   └── whit_open.py
│
├── configuracao_vscode.txt
└── README.md

Módulo 1 — Fundamentos e Estruturas de Controle

Este módulo reúne os conceitos fundamentais necessários para começar a programar em Python e entender como o fluxo de execução de um programa funciona.

Arquivos

Arquivo

Conteúdo

tipos.py

Tipos básicos de dados e exemplos de uso

operadores.py

Operadores aritméticos, relacionais, lógicos e outros operadores da linguagem

for.py

Estrutura de repetição for

while_else.py

Estrutura while e uso de else em laços

funçao.py

Criação e utilização de funções

parametros.py

Parâmetros de funções, argumentos e retornos

escopo_variaveis.py

Escopo local e global de variáveis

jogo_palavra_secreta.py

Exercício prático aplicando estruturas de controle e lógica

Exemplo

def saudacao(nome):
    return f"Olá, {nome}!"


for nome in ["Ana", "Carlos", "Maria"]:
    print(saudacao(nome))

Módulo 2 — Coleções Nativas

Este módulo apresenta as principais estruturas de dados já disponíveis na própria linguagem Python.

Arquivos

Arquivo

Conteúdo

lista.py

Listas, operações, métodos e manipulação de elementos

tuplas.py

Tuplas, imutabilidade e desempacotamento

dicionario.py

Estruturas chave-valor com dict

conjuntos.py

Conjuntos com set e operações entre conjuntos

string.py

Strings, indexação, métodos e manipulação de texto

Exemplo

aluno = {
    "nome": "Ana",
    "nota": 9.0
}

print(aluno["nome"])

Módulo 3 — Estruturas de Dados

Este módulo aborda estruturas clássicas da Ciência da Computação e mostra como elas podem ser implementadas ou representadas em Python.

Arquivos

Arquivo

Conteúdo

pilha.py

Pilha seguindo o princípio LIFO

fila.py

Fila seguindo o princípio FIFO

heap.py

Heap e fila de prioridade

arvore_binaria.py

Árvore binária e percursos

grafo.py

Representação e navegação em grafos

collections.py

Estruturas úteis do módulo collections

structs_equivalentes.py

Equivalentes Python para estruturas semelhantes a structs

ponteiros_referencias.py

Referências de objetos e comparação com o conceito de ponteiros

atribuicao_e_copias.py

Atribuição, cópia rasa e cópia profunda

mutabilidade.py

Objetos mutáveis e imutáveis

Pilha

Uma pilha utiliza o princípio:

LIFO — Last In, First Out

O último elemento inserido é o primeiro a ser removido.

pilha = []

pilha.append(10)
pilha.append(20)

print(pilha.pop())

Fila

Uma fila utiliza o princípio:

FIFO — First In, First Out

O primeiro elemento inserido é o primeiro a ser removido.

from collections import deque

fila = deque()

fila.append("A")
fila.append("B")

print(fila.popleft())

Heap / Fila de prioridade

Python disponibiliza o módulo heapq para trabalhar com heaps.

import heapq

fila = []

heapq.heappush(fila, 30)
heapq.heappush(fila, 10)
heapq.heappush(fila, 20)

print(heapq.heappop(fila))

Árvore binária

Uma árvore binária organiza dados de forma hierárquica.

        raiz
       /    \
 esquerda  direita

O material inclui estudos de percursos como:

pré-ordem;

em ordem;

pós-ordem.

Grafos

Grafos representam relações entre vértices.

grafo = {
    "A": {"B", "C"},
    "B": {"A", "D"},
    "C": {"A"},
    "D": {"B"}
}

Eles podem ser percorridos utilizando estratégias como BFS e DFS.

Referências, atribuição e cópias

Em Python, variáveis normalmente mantêm referências para objetos.

lista_a = [1, 2, 3]
lista_b = lista_a

lista_b.append(4)

print(lista_a)

Nesse exemplo, as duas variáveis referenciam o mesmo objeto.

Para criar cópias independentes, podem ser utilizados recursos do módulo copy.

import copy

copia_rasa = copy.copy(lista_a)
copia_profunda = copy.deepcopy(lista_a)

Módulo 4 — Python Avançado

Este módulo reúne recursos que ajudam a compreender melhor o funcionamento da linguagem e a desenvolver programas mais organizados.

Arquivos

Arquivo

Conteúdo

classes_poo.py

Classes, objetos, atributos e métodos

excessao.py

Tratamento de exceções

generators.py

Generators e uso de yield

iteraveis_iteradores.py

Iteráveis, iteradores, iter() e next()

whit_open.py

Manipulação de arquivos com gerenciadores de contexto

Programação Orientada a Objetos

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        return f"Olá! Meu nome é {self.nome}."


pessoa = Pessoa("Ana")

print(pessoa.apresentar())

Tratamento de exceções

try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Valor inválido.")
else:
    print(f"Número informado: {numero}")
finally:
    print("Fim da execução.")

Iteráveis e iteradores

numeros = [10, 20, 30]

iterador = iter(numeros)

print(next(iterador))
print(next(iterador))

Generators

Generators produzem valores sob demanda e podem ajudar a reduzir o consumo de memória.

def contador():
    yield 1
    yield 2
    yield 3


for numero in contador():
    print(numero)

Manipulação de arquivos

O gerenciador de contexto with ajuda a garantir que o arquivo seja fechado corretamente após o uso.

with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)

Organização dos exemplos

Sempre que possível, os conteúdos seguem uma estrutura didática semelhante a:

Conceito
Sintaxe Básica / Assinatura
Código de Exemplo
Mapeamento Nativo / Equivalência
Pontos de Atenção

A proposta é que cada arquivo possa funcionar tanto como exemplo executável quanto como material de revisão.

Como executar os códigos

Verifique a versão instalada:

python --version

Execute um arquivo com:

python nome_do_arquivo.py

Exemplo:

python "MÓDULO 3 — ESTRUTURAS DE DADOS/pilha.py"

No Windows, também pode ser usado:

py "MÓDULO 3 — ESTRUTURAS DE DADOS/pilha.py"

Clonando o repositório

git clone https://github.com/Vivian-Duarte/Aulas-Python.git

Depois:

cd Aulas-Python

Atualizando o GitHub

Depois de modificar ou adicionar arquivos:

git status

Adicionar as alterações:

git add .

Criar o commit:

git commit -m "Atualiza materiais de Python"

Enviar para o GitHub:

git push

Tecnologias utilizadas

Python 3.10+

Git

GitHub

Visual Studio Code

Status

O repositório está em desenvolvimento.

Novos exemplos, exercícios e conceitos serão adicionados conforme o avanço dos estudos.

Autora

Vivian Duarte

Material desenvolvido para estudo e prática de Python, Estruturas de Dados e conceitos de Engenharia de Software.