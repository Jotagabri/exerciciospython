1 - Função para calcular gorjeta

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


# Testando
valor = 100.00
porcentagem = 10
print(f"Gorjeta: R$ {calcular_gorjeta(valor, porcentagem):.2f}")

2 - Função para verificar palíndromo

def eh_palindromo(texto):
    texto_limpo = "".join(char.lower() for char in texto if char.isalnum())
    return texto_limpo == texto_limpo[::-1]


# Testando
palavra = "Ame a ema"
resultado = eh_palindromo(palavra)

print("Sim" if resultado else "Não")

3 - Programa para calcular desconto e preço final

def calcular_desconto(preco, porcentagem):
    return preco * (porcentagem / 100)


def calcular_preco_final(preco, porcentagem):
    desconto = calcular_desconto(preco, porcentagem)
    return preco - desconto


print("=== Cálculo de Desconto ===")

preco = float(input("Digite o preço do produto: R$ "))
porcentagem = float(input("Digite a porcentagem de desconto: "))

desconto = calcular_desconto(preco, porcentagem)
preco_final = calcular_preco_final(preco, porcentagem)

print(f"\nDesconto: R$ {desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")

4 - Programa que calcula quantos dias uma pessoa está viva

from datetime import datetime

print("=== Calculadora de Dias de Vida ===")

data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")

data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
data_atual = datetime.now()

diferenca = data_atual - data_nascimento

print(f"Você está vivo há {diferenca.days} dias!")

