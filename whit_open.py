"""
Conceito:
Arquivos permitem persistir informações fora da memória do programa. O comando
with open(...) usa um gerenciador de contexto que fecha o arquivo automaticamente,
mesmo quando ocorre uma exceção dentro do bloco.

Sintaxe Básica / Assinatura:
with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

Mapeamento de Módulos Nativo / Equivalência:
open é uma função built-in. O protocolo de gerenciador de contexto usado por
with é nativo da linguagem.

Pontos de Atenção:
1. Informe encoding="utf-8" explicitamente para arquivos de texto quando possível.
2. Modos comuns: r leitura, w sobrescrita, a acréscimo e b modo binário.
3. Evite read() em arquivos enormes; prefira percorrer linha por linha.
"""


def exemplo_arquivos() -> None:
    caminho = "exemplo_guia_python.txt"

    # "w" cria o arquivo ou sobrescreve seu conteúdo anterior.
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write("Primeira linha\n")
        arquivo.write("Segunda linha\n")

    # "a" acrescenta conteúdo ao final.
    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write("Terceira linha\n")

    # "r" abre para leitura.
    with open(caminho, "r", encoding="utf-8") as arquivo:
        for numero_linha, linha in enumerate(arquivo, start=1):
            print(numero_linha, linha.rstrip())

    # Limpeza do arquivo criado exclusivamente para esta demonstração.
    os.remove(caminho)