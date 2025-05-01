'''4 - Crie uma função em Python que receba um número como parâmetro e retorne o dobro desse número. Depois, chame essa função com um número fornecido pelo usuário.'''
# 'def' Define uma função chamada "dobro" e vai receber  um parametro chamado numero
def dobro(numero):
    # Retorna ovalor do número multiplicado por 2 
    return numero * 2
# Solicita ao usuario que digite um numero
valor = float(input("Digite um Numero para Calcular: "))
# Chama a Função dobro passando o valor digitado e armazena  o resultado
resultado = dobro(valor)
#Exibe o Resultado
print(" O Dobro do numero é:", resultado)