#Calculando media ponderada
#Criei 3 notas e 3 pesos para receberem seus valores atraves do usuario, ja armazenando nas variaveis
peso1 = (int(input("Peso 1 =")))
nota1 = (int(input("Nota 1 =")))
peso2 = (int(input("Peso 2 =")))
nota2 = (int(input("Nota 2 =")))
peso3 = (int(input("Peso 3 =")))
nota3 = (int(input("Nota 3 =")))

#aqui criei um algorotimo para calcular a media ponderada
#me perdi no decorrer dos códigos por conta dos parenteses
#armazenei o calculo a uma variavel
mediaP = ((peso1 * nota1) + (peso2 * nota2) + (peso3 * nota3)) / (peso1 + peso2 + peso3)

#mostrando o algoritmo 
print(mediaP)
