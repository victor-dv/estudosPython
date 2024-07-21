nome = input("Nome do funcionário: ")
salarioA = int(input("Salario Atual: "))

salarioAumento = (salarioA * (25/100))
salarioF = salarioA + salarioAumento
print(f"Salário do funcionário(a) {nome} com aumento é igual à: ", salarioF)