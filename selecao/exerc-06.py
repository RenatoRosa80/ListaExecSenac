#6) Reescreva o programa do exercício anterior considerando o zero como neutro, ou seja, se fordigitado o valor zero, escrever a palavra zero.

#entradas
valor = int(input("Escreva um valor: "))

#processamento
resposta = ""
if valor == 0:
    resposta = "Zero"
elif valor > 0:
    #saidas
    #print("Positivo")
    resposta = "Positivo"
else:
    #saidas
    #print("Negativo")
    resposta = "Negativo"

#saida
print("O valor é: ", resposta)