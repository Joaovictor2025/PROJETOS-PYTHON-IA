def cadastrar_alunos():
    alunos = {}
    
    while True:
        nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
        if nome.lower() == "fim":
            break

        notas = []
        for i in range(3):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i+1} de {nome}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Erro: A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Erro: Digite um número válido.")
        
        alunos[nome] = notas

    return alunos

def calcular_medias(alunos):
    medias = {nome: sum(notas) / len(notas) for nome, notas in alunos.items()}
    return medias

def exibir_resultados(alunos, medias):
    print("\nLista de alunos e suas médias:")
    for nome, media in medias.items():
        print(f"{nome}: {media:.2f}")
    
    melhor_aluno = max(medias, key=medias.get)
    print(f"\nAluno com a maior média: {melhor_aluno} ({medias[melhor_aluno]:.2f})")

# Executando o sistema
alunos = cadastrar_alunos()
medias = calcular_medias(alunos)
exibir_resultados(alunos, medias)