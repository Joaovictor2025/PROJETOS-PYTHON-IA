'''Crie um programa que faça uma contagem regressiva a partir de um número informado pelo usuário até 0. O programa deve mostrar cada número da contagem e, ao final, exibir "FIM!".'''

numero = int(input("Digite o numero para contagem regressiva: "))
while numero >= 0:
    print(numero)
    numero -= 1
print("FIM")