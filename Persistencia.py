def ScoreRankear(nome, pontuacao):
    # Carregue o ranking existente do arquivo
    ranking = []
    try:
        with open('ranking.txt', 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split()
                ranking.append((partes[1], int(partes[2])))
    except FileNotFoundError:
        pass  # Se o arquivo não existir ainda, apenas continue com uma lista vazia

    # Adicione o novo registro ao ranking
    ranking.append((nome, pontuacao))

    # Classifique o ranking por pontuação (ordem crescente)
    ranking.sort(key=lambda x: x[1])

    # Salve o ranking atualizado de volta no arquivo
    with open('ranking.txt', 'w') as arquivo:
        for i, (nome, pontuacao) in enumerate(ranking, start=1):
            arquivo.write(f"{i} {nome:<10} {pontuacao}\n")

def exibirRanking():
    # Carregue o ranking do arquivo e exiba na tela
    ranking = []
    try:
        with open('ranking.txt', 'r') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split()
                ranking.append((int(partes[0]), partes[1], int(partes[2])))
    except FileNotFoundError:
        ranking = []

    if ranking:
        print("=== Melhor Pontuação ===")
        print("Nome         #Jogadas")
        for posicao, nome, pontuacao in ranking:
            print(f"{posicao} {nome:<10} {pontuacao}")
    else:
        print("Ainda não há pontuações no ranking.")
