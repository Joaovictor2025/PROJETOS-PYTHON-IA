'''6- Calculadora de Média Escolar
Enunciado:
Desenvolva um programa que solicite o nome de um aluno e suas 3 notas. O programa deve calcular a média e informar se o aluno foi aprovado (média >= 7), está em recuperação (5 <= média < 7) ou foi reprovado (média < 5).'''

aluno = input("Digite o nome do Aluno: ")
nota01 = float(input("Digite a Primeira Nota "))
nota02 = float(input("Digite a Segunda Nota "))
nota03 = float(input("Digite a Terceira Nota "))

media = (nota01 + nota02 + nota03) / 3

print(f" A Media do {aluno} é {media:.2f} ")
if media >=7: 
    print(" Aprovado!")
elif media  >= 5 :
    print(" Recuperação!")
else:
    print("Reprovado!")
