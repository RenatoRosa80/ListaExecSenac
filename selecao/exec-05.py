#5) Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.

#entradas
valor = int(input("Escreva um valor: "))

#processamento
resposta = ""
if valor >= 0:
    #saidas
    #print("Positivo")
    resposta = "Positivo"
else:
    #saidas
    #print("Negativo")
    resposta = "Negativo"

#saida
print("O valor é: ", resposta)