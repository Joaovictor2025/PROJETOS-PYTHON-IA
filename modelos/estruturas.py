#Estrutura Sequencial 
nome = input("digitw seu nome: ")
idade = int(input("Digitw sua Idade: "))
cidade = input("Cidade onde Mora: ")
print("Olá", nome)
print("Você tem", idade, "anos")
print("E mora em", cidade)

#estrutura de repetição
for i in range(5):
    print("Conta",i)

contar = 0
while contar  <5:
    print("Executar", contar)
    contar += 1

#estrutura condicional
idade = 16
if idade > 18:
    print(" Maior de Idade!")
elif idade <18:
    print("Menor de Idade,Vá Dormir")
else:
    print(" Sei lá o que voce é")

ida = int(input("Qual  sua Idade?"))
if ida >=18:
    print("Manior de Idade")
else:
    print("Maior de Idade")


