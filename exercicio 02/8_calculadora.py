'''8- Calculadora Simples
Enunciado:
Crie um programa que simule uma calculadora simples. O usuário deve informar dois números e a operação desejada (+, -, *, /) e o programa deve exibir o resultado da operação.'''
numero1 = float(input("Digite o Primeiro  numero: "))
numero2 = float(input("Digite o Segundo  numero: "))

operacao = input("Digite a Operação a ser realizada (+,-,*,/):")

if operacao == "+":
    resultado = numero1 + numero2
    print(f"O resultado do {numero1} + {numero2} é: {resultado} ")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"O resultado do {numero1} - {numero2} é: {resultado} ")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"O resultado do {numero1} * {numero2} é: {resultado} ")
elif operacao == "/":
    if numero2!= 0:
        resultado = numero1 / numero2
        print(f"O resultado do {numero1} / {numero2} é: {resultado} ")
    else:
        print("Erro!!! Divisão por zero é permitido")
