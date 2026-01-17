1. Classificador de Idade

idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    categoria = "Criança"
elif 13 <= idade <= 17:
    categoria = "Adolescente"
elif 18 <= idade <= 59:
    categoria = "Adulto"
elif idade >= 60:
    categoria = "Idoso"
else:
    categoria = "Idade inválida"

print("Classificação:", categoria)


2. Calculadora de IMC

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"Seu IMC é {imc:.2f} - {classificacao}")

3. Conversor de Temperatura

valor = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Converter para (C/F/K): ").upper()

resultado = None

# Converter a Celsius primeiro
if origem == "C":
    temp_c = valor
elif origem == "F":
    temp_c = (valor - 32) * 5/9
elif origem == "K":
    temp_c = valor - 273.15
else:
    print("Unidade de origem inválida!")
    exit()

# Converter Celsius para destino
if destino == "C":
    resultado = temp_c
elif destino == "F":
    resultado = (temp_c * 9/5) + 32
elif destino == "K":
    resultado = temp_c + 273.15
else:
    print("Unidade de destino inválida!")
    exit()

print(f"{valor}°{origem} = {resultado:.2f}°{destino}")

4. Verificador de Ano Bissexto

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "NÃO é um ano bissexto.")
