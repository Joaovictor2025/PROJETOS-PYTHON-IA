
quantidade_pares = 0
quantidade_impares = 0

while  True:
    entrada = input(" Digite um numero inteiro (ou 'fim' para encerrar):")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("O numero é PAR.")
            quantidade_pares += 1
        else:
            print(" O numero é IMPAR.")
            quantidade_impares += 1 
    except ValueError:
        print("Erro: Voce deve Digitar um Numero Inteiro ou 'FIM'.")

print(f"Quantidade de numeros PARES: {quantidade_pares}")
print(f"Quantidade de numeros IMPARES: {quantidade_impares}")