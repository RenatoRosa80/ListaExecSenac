#74) Faça um algoritmo que conte de 1 a 100 e a cada multiplo de 10 emita uma mensagem: "multiplo de 10".
# O usuario deve entrar com o valor do multiplo que deve ser mostrado na lista.

multiplo = int(input("Qual seria o multiplo? "))
valorInicial = int(input("Qual o valor incial? "))
valorFinal = int(input("Qual seria o valor final? "))

if(valorFinal < valorInicial):
    for i in range(valorInicial, valorFinal+1):
        if(i % multiplo == 0):
        print(i, "multiplo ", multiplo)
        else:
            print(i)
else:
    print("Valor de entrada invalido!")
