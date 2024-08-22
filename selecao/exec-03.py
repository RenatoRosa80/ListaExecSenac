#3) Escreva um programa para ler as notas das duas avaliações de um aluno no semestre, calcular e
#escrever a média semestral e a seguinte mensagem: PARABÉNS! Você foi aprovado! somente se oaluno foi aprovado (considere 6.0 a média mínima para aprovação

#entrada
aluno = str(input("Aluno: "))
nota1 = float(input("Valor da Nota 01: "))
nota2 = float(input("Valor da Nota 02: "))
media = ()


#processamento
media = (nota1 + nota2) / 2
if media >= 6:
    print("Parabens! Você foi Aprovado")
else:
    print("Você foi REPROVADO! Estude mais..")