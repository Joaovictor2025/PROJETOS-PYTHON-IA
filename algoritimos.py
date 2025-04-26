#Algoritimo de Busca
def busca (lista, nome_procurado):
    for i in range(len(lista)):
        if lista[i] == nome_procurado:
            return i + 1  # retorna para a posição
    return -1   #nao encontrou
nomes = [ "maria","Jose", "João", "Peddo","Ana"]
nome_procurado = input('Qual nome você quer procurar? ')
posicao = busca(nomes, "Ana")
if posicao != -1:
    print('O nome está na posição', posicao)
else:
    print('O nome não está na lista')

#Algoritimo de busca - Binario
def binaria (lista, valor_procurado):
    inicio = 0
    fim= len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor_procurado:
            return meio
        elif lista[meio] < valor_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1 
    return -1
numeros = [1,3,5,7,9,11,13,15,17]    
posicao = binaria(numeros, 15)
print("Número encontrado na Posição:", posicao)

    