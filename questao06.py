1 - Gerador de senha aleatória

import random
import string

print("=== GERADOR DE SENHAS ===")

tamanho = int(input("Digite o tamanho da senha: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

senha = "".join(random.choice(caracteres) for _ in range(tamanho))

print(f"Senha gerada: {senha}")


2 - Buscar usuário fictício em API (Random User API)

import requests

url = "https://randomuser.me/api/"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()

    dados = resposta.json()
    usuario = dados["results"][0]

    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("=== Usuário Aleatório ===")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")

except Exception:
    print("Falha ao acessar a API ou conexão com erro.")

3 - Consultar informações de CEP (ViaCEP)

import requests

cep = input("Digite o CEP (somente números): ")

url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()

    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print("=== Dados do CEP ===")
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")

except Exception:
    print("Falha na conexão ou erro ao consultar o CEP.")

4 - Consulta de moedas em relação ao Real (BRL)

import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, BTC): ").upper()

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()

    dados = resposta.json()

    chave = f"{moeda}BRL"

    if chave not in dados:
        print("Moeda não encontrada ou código inválido.")
    else:
        info = dados[chave]

        print("=== Cotação Atual ===")
        print(f"Moeda: {moeda}")
        print(f"Atual: R$ {info['bid']}")
        print(f"Máxima: R$ {info['high']}")
        print(f"Mínima: R$ {info['low']}")
        print(f"Última atualização: {info['create_date']}")

except Exception:
    print("Erro na conexão ou na consulta da moeda.")
