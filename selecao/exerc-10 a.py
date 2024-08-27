#10) Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e
#escrevê-los em ordem crescente

#Entrada
valores = []
valores.append(int(input("Digite o primeiro valor? ")))
valores.append(int(input("Digite o segundo valor? ")))
valores.append(int(input("Digite o terceiro valor? ")))


for x in valores:
    print(x)

if(valores[0] > valores[1]):
    valorTemp = valor[0]
    valores[0] = valores[1]
    valores[1] = valorTemp

if(valores[0] > valores[2]):
    valorTemp = valor[0]
    valores[0] = valores[2]
    valores[2] = valorTemp

if(valores[1] > valores[1]):
    valorTemp = valor[0]
    valores[1] = valores[2]
    valores[2] = valorTemp

print(valores)

