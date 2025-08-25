maior = "0"

for i in range(5):
  num = int(input("Digite um número: "))

  if maior == "0":
    maior = num

  if num > maior:
    maior = num

print(f"O maior é {maior}")