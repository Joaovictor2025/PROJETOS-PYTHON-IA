'''Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.'''


import random # importando o modulo random
import string # importando o modulo de caracteries prontos
tamanho = int (input(" Informe o tamanho de aracteres para gerar uma senha: "))
'''bloco para definir caracteries que seraousados.
ascii - trazendo letras minusculas e maiusculas
digits - trazendo numeros de 0 a 9.
punctuantion - trazendo caracteries especiais.'''
caracteries_possiveis = string.ascii_letters + string.digits + string.punctuation
'''blocos de gerador de senha 
random.choses - escolhe tamanho dos elementos da lista'''
senha_lista = random.choices(caracteries_possiveis, k=tamanho)
senha = " ".join(senha_lista)   #Aqui esta unido os caracteries.
print("Senha Gerada: ", senha)