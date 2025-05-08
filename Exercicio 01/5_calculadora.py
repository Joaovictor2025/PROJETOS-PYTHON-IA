'''5 - Crie um programa em Python que peça dois números e uma operação matemática (+, -, * ou /), e mostre o resultado de acordo com a operação escolhida.'''

#solicita que o usuario digite o primeiro numero
num01 = float(input("Digite o primeiro numero"))
#solicita que o usuario digite o segundo numero
num02 = float(input("Digite o primeiro numero"))
#solicita que o usuario digite a operação
operacao = input(" Digite a Operação (+, -, * ou /): ")
#verifica a operação que o usuario digitou
if operacao == "+":
    #Soma os numeros
    resultado = num01 + num02
    print("O resultado da Soma é: ", resultado)

elif operacao == "-":
    #Subtrai o numero
    resultado = num01 - num02
    print("O resultado da Subitração é: ", resultado)

elif operacao == "*":
    #Multiplica o numero 
    resultado = num01 * num02
    print("O resultado da Multiplicação é: ", resultado)

elif operacao == "/":
    #verifica se o segundo numero é diferente de zero
    if num02 != 0:
        resultado = num01 / num02
        print("O resultado da Divisão é: ", resultado)
    else:
        print("Erro: Divisão por ZERO não é permitido")
else:
    print("Operação invalida!")