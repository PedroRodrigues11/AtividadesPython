palavra = input("Digite a palavra a ser analisada: ").lower()
vogais = 0

for letra in palavra:
  if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    vogais += 1

print(f"A quantidade de vogais nessa palavra é {vogais}")