valor = float(input("Digite o valor recebido por hora: "))
horas = int(input("Digite a quantidade de horas trabalhadas: "))

salario = valor * horas

print("Salário bruto: R$ {:.2f}".format(salario))
print("IR (11%): R$ {:.2f}".format(salario * 0.11))
print("INSS (8%): R$ {:.2f}".format(salario * 0.08))
print("Sindicato(5%): R$ {:.2f}".format(salario * 0.05))
print("Salário líquido: R$ {:.2f}".format(salario * 0.76))