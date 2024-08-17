#7) Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) eescrever o maior deles.

#entrada
valor1 = float(input("Qual o primeiro valor? "))
valor2 = float(input("Qual o segundo valor? "))

#processamento
resposta = 0
if valor1 > valor2:
    resposta = valor1
else:
    resposta = valor2

#saida
print("O maior deles é: ", resposta)