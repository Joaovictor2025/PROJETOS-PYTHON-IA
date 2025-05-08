'''5- Verificador de Número Primo
Enunciado:
Crie um programa que solicite um número inteiro positivo ao usuário e verifique se ele é um número primo. Um número primo só é divisível por 1 e por ele mesmo.'''

numero = int(input("Digite um NUmero positivo: "))
if numero < 2:
    print(f"O numero{numero} não é primo")
else:
    e_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            e_primo = False
            break
    if e_primo:
        print(f"O numero:{numero} é primo.")
    else:
        print(f"o numero: {numero} não é primo")
