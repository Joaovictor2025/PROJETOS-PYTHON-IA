'''
2 - Crie um programa em Python que solicite um número do usuário e informe se ele é par ou ímpar.'''
# Solicitao usuario que divisivel por 2 ( resto é igual a zero)
numero = int(input("Digite um numero: "))

if numero % 2 ==0:
# Se o resto da divisão for zero será o numeropar
    print("O numero é par. ")
else:
 # Caso contrario será impar
    print("o numero é impar.")