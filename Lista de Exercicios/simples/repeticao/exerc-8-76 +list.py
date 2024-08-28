
#OBS.: Refaça o exercicio usando lista para armazenarmos valores digitados pelo usuario
#OBS2.: Faça com que o sistema sorteie 6 valores digitados pelo usuario logo apos exibir as mensagens
#Random.randrange command ( print(random.randrange(1, 51))

maior = 0
menor = 9999999
soma = 0
limite = 5

listValores = [] #[] representa um Array ou Lista

for x in range(1, limite + 1):
    valor = int(input(f"Qual o {x}º  valor? "))
    if(valor > maior):
        maior = valor
    if(valor < menor):
        menor = valor
    soma = soma + valor
    print("soma: ", soma)

    listValores.append(valor)

print("Media: ", soma/5)
print("Maior valor e: ", maior)
print("Menor valor e: ", menor)
print("valores: ", listValores)

for x in listValores:
    if(x % 2 == 0):
        print("Item: ", x)

