# Calculadora simples SEM função

print("=== Calculadora Simples ===")

# Lendo os números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Escolhendo a operação
print("Escolha a operação:")

print("1 - Soma (+)")
print("2 - Subtraçaõ (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

opera = input("Digite a operação: ")

# Realizando o cálculo
if opera == "1":
  resultado = num1 + num2
elif opera == "2":
  resultado = num1 - num2
elif opera == "3":
  resultado = num1 * num2
elif opera == "4":
  resultado = num1 / num2
else:
  resultado = "Inválido!"

print("Resultado:", resultado)