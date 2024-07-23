#Gratificação de 10%
#15% de descontos do salario apos a gratificação
salarioBruto = int(input("Salário: "))
salarioGratificacao = (salarioBruto * 10/100) + salarioBruto
salarioDescontos = salarioGratificacao - (salarioGratificacao * 15/100) 

print("Salário Bruto: ", salarioBruto, "\n"
      "Salario após gratificação: ", salarioGratificacao, "\n"
      "Salario após descontos: ", salarioDescontos)
