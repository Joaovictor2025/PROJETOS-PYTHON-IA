'''7- Verificador de Palíndromo
Enunciado:
Crie um programa que solicite uma palavra e verifique se ela é um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente).'''

palavra = input(" Insira uma palavra ou uma frase: ")
palavra_formatada = palavra.replace("", "").lower()
palavra_invertida = palavra_formatada[:: -1]
if palavra_formatada == palavra_invertida:
    print(f"A Palavra / frase {palavra} é um Palidromo.")
else:
    print(f"A Palavra / frase {palavra} não é um Palidromo.")

