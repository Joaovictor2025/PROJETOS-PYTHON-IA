senha_correta = "123456789"
tentativas = 0
while True:
    senha = input("Digite a sua senha: ")
    tentativas -= 1
    if senha == senha_correta:
        print(" Acesso Concedido")
        break
    else:
        print("Senha Incorreta! ")
    if tentativas == 3:
        print("Numero de tentativas excedido, ACESSO NEGADO!!")
        break