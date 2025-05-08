'''8 - Crie um programa que armazene nomes de países e suas capitais em um dicionário. O usuário digita o nome do país e o programa mostra a capital correspondente.'''

capitais = {
    "Brasil": "brasilia" ,
    "Argentina" : "Bueno Aires",
    "França": "Paris",
    "Japão" : "Tóquio",
    "Canadá": "Ottawa",
    "Alemanha": "Berlim",
    "Argentina": "Buenos Aires",
    "Estados Unidos": "Washington, D.C.",
    "Itália": "Roma",
    "Portugal": "Lisboa",
    "Reino Unido": "Londres"
}
pais = input("Digite o nome de um país: ")
if pais in capitais:
    print("A Capital de", pais, "é:", capitais[pais] )
else: 
    print("País não encontrado.")