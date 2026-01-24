1 – Escrever dados de pessoas em um arquivo CSV

import csv

# Lista de listas com dados fictícios
pessoas = [
    ["Ana", 25, "São Paulo"],
    ["Carlos", 30, "Rio de Janeiro"],
    ["Mariana", 22, "Belo Horizonte"]
]

nome_arquivo = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ")

try:
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        # Cabeçalho
        escritor.writerow(["Nome", "Idade", "Cidade"])

        # Dados
        escritor.writerows(pessoas)

    print(f"Arquivo '{nome_arquivo}' gravado com sucesso!")

except Exception as erro:
    print("Erro ao escrever o arquivo CSV.")
    print("Detalhes:", erro)


2 – Ler dados de um arquivo CSV e imprimir na tela

import csv

nome_arquivo = input("Digite o nome do arquivo CSV a ser lido: ")

try:
    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            print(linha)

except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except Exception as erro:
    print("Erro ao ler o arquivo CSV.")
    print("Detalhes:", erro)

3 – Salvar e ler dados de uma pessoa em arquivo JSON

import json

# Dicionário com dados da pessoa
pessoa = {
    "nome": "João",
    "idade": 28,
    "cidade": "Curitiba"
}

nome_arquivo = input("Digite o nome do arquivo JSON (ex: pessoa.json): ")

try:
    # Escrita no arquivo JSON
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(pessoa, arquivo, indent=4, ensure_ascii=False)

    print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")

    # Leitura do arquivo JSON
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados_lidos = json.load(arquivo)

    print("Dados lidos do arquivo:")
    print(dados_lidos)

except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except Exception as erro:
    print("Erro ao manipular o arquivo JSON.")
    print("Detalhes:", erro)
