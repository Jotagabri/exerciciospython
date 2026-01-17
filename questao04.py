1. Calculadora Simples (+, -, , /)

print("=== Calculadora ===")

num1 = float(input("Digite o primeiro número: "))
oper = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if oper == "+":
    print("Resultado:", num1 + num2)
elif oper == "-":
    print("Resultado:", num1 - num2)
elif oper == "*":
    print("Resultado:", num1 * num2)
elif oper == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Erro: divisão por zero!")
else:
    print("Operação inválida!")

2. Registrar notas e calcular média da turma

print("=== Média da Turma ===")

quantidade = int(input("Quantos alunos têm na turma? "))

soma_notas = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma_notas += nota

media = soma_notas / quantidade
print(f"Média da turma: {media:.2f}")

3. Verificar segurança de senha

print("=== Verificador de Senha ===")

senha = input("Digite uma senha: ")

tem_tamanho = len(senha) >= 8
tem_numero = any(char.isdigit() for char in senha)

if tem_tamanho and tem_numero:
    print("Senha válida e segura!")
else:
    print("Senha insegura! Verifique os critérios:")
    if not tem_tamanho:
        print("- Deve ter pelo menos 8 caracteres")
    if not tem_numero:
        print("- Deve conter pelo menos um número")

4. Verificar números pares e ímpares e contar

print("=== Analisador de Números ===")

pares = 0
impares = 0

while True:
    numero = input("Digite um número (ou 'sair' para encerrar): ")

    if numero.lower() == "sair":
        break

    if not numero.isdigit():
        print("Por favor, digite apenas números.")
        continue

    numero = int(numero)

    if numero % 2 == 0:
        pares += 1
        print("Número par.")
    else:
        impares += 1
        print("Número ímpar.")

print("\nResumo:")
print(f"Pares digitados: {pares}")
print(f"Ímpares digitados: {impares}")

