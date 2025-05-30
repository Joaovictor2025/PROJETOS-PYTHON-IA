
while True:
    try:
        numero1 = float(input("Digite o Primeiro Numero"))
        numero2 = float(input("Digite o Segundo Numero"))
        operacao = input(" Digite a Operação (+,-,*,/): ")
        if  operacao == "+":
            resultado = numero1 + numero2
        elif  operacao == "-":
            resultado = numero1 - numero2
        elif  operacao == "*":
            resultado = numero1 * numero2
        elif  operacao == "/":
            resultado = numero1 / numero2
            if numero2 == 0:
                print(" Erro: divisão por ZERO não permitido.")
                continue
            resultado = numero1 / numero2
        else:
            print("Erro: Operação Invalida. Use (+, -, *, /). ")
            continue
        print(f"Resultado: {resultado:2f}")
        break
    except ValueError:
        print(" Erro: Digite Apenas Numeros.")
    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")