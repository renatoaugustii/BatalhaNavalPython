import random

# 0 = '\u25A0' => Não explorado
# 1 = '_'      => Água
# 2 = 'x'      => Afundado
# 3 = '\u2316'  => Parcial

#Incia o tabuleiro com 0 em todas as posições
tabuleiro = {
                'A1': '0', 'A2': '0', 'A3': '0', 'A4': '0', 'A5': '0', 'A6': '0',
                'B1': '0', 'B2': '0', 'B3': '0', 'B4': '0', 'B5': '0', 'B6': '0',
                'C1': '0', 'C2': '0', 'C3': '0', 'C4': '0', 'C5': '0', 'C6': '0',
                'D1': '0', 'D2': '0', 'D3': '0', 'D4': '0', 'D5': '0', 'D6': '0',
                'E1': '0', 'E2': '0', 'E3': '0', 'E4': '0', 'E5': '0', 'E6': '0',
                'F1': '0', 'F2': '0', 'F3': '0', 'F4': '0', 'F5': '0', 'F6': '0',
            }


def criarPosicaoNavios():
    listaNavios = []
    navios_colocados = 0
    while navios_colocados < 5:
        linha = random.choice('ABCDEF')
        coluna = str(random.randint(1,6))
        posicao = linha+coluna
        #Verifica se a posição ja esta ocupada
        if tabuleiro[posicao] == '0':
            tabuleiro[posicao] = '1'
            listaNavios.append(posicao) #Adiciona a posicao que foi escolhida aleatoriamente na ultima posicao da lista
            navios_colocados += 1
    return listaNavios

def criarPosicaoSubmarinos():
    listaSubmarinos = []
    submarinos_colocados = 0
    while submarinos_colocados < 3:  # Posicionar 3 submarinos
        # Escolha aleatoriamente a orientação (horizontal ou vertical)
        orientacao = random.choice(['horizontal', 'vertical'])
        
        if orientacao == 'horizontal':
            # Escolha aleatoriamente uma linha e uma coluna inicial
            linha = random.choice('ABCDEF')
            coluna = random.randint(1, 5)  # Certifique-se de que haja espaço suficiente para o submarino
            
            # Verifique se as posições adjacentes estão livres
            posicao1 = linha + str(coluna)
            posicao2 = linha + str(coluna + 1)
            if tabuleiro[posicao1] == '0' and tabuleiro[posicao2] == '0':
                # Marque as posições como ocupadas e adicione à lista de submarinos
                tabuleiro[posicao1] = '1'
                tabuleiro[posicao2] = '1'
                submarino = [posicao1, posicao2]
                listaSubmarinos.append(submarino)
                submarinos_colocados += 1
        else:
            # Escolha aleatoriamente uma linha inicial e uma coluna
            linha = random.choice('ABCDE')
            coluna = random.randint(1, 6)
            
            # Verifique se as posições adjacentes estão livres
            posicao1 = linha + str(coluna)
            posicao2 = chr(ord(linha) + 1) + str(coluna)
            if tabuleiro[posicao1] == '0' and tabuleiro[posicao2] == '0':
                # Marque as posições como ocupadas e adicione à lista de submarinos
                tabuleiro[posicao1] = '1'
                tabuleiro[posicao2] = '1'
                submarino = [posicao1, posicao2]
                listaSubmarinos.append(submarino)
                submarinos_colocados += 1
    return listaSubmarinos


def atualizarNavio(posicao):
     # Atualize a posição no tabuleiro para indicar que foi atingida
    tabuleiro[posicao] = '2' 

def atualizarSubmarino(posicao):
    # Esta função atualiza o tabuleiro quando um submarino é atingido parcialmente
    if posicao in tabuleiro:
        # Verifique se a outra parte do submarino já foi atingida
        outras_posicoes = [p for p in tabuleiro if tabuleiro[p] == '3']
        for outra_posicao in outras_posicoes:
            if abs(ord(outra_posicao[0]) - ord(posicao[0])) + abs(int(outra_posicao[1]) - int(posicao[1])) == 1:
                # A outra parte do submarino foi atingida, atualize as duas posições para '2'
                tabuleiro[outra_posicao] = '2'
                tabuleiro[posicao] = '2'
                return
        # Se não, atualize apenas a posição atual para indicar que foi atingida parcialmente
        tabuleiro[posicao] = '3'  # Use o Unicode '\u2316' para indicar um submarino atingido parcialmente


def atualizarAgua(posicao):
     # Atualize a posição no tabuleiro para indicar que não foi
    tabuleiro[posicao] = '1'  

def imprimirTabuleiro():
    #Cabeçalho numérico alinhado conforme as demais colunas
    print('    1 2 3 4 5 6')
    #For Incrementa as letras correspondentes para as linhas, valores são usados os que foram declarados no tabuleiro
    for L in 'ABCDEF':
        print(L,'|', end=' ')
        for C in range(1, 7):
            posicao = L + str(C)

            #Verifica qual simbolo deve utilizar para imprimir o tabuleiro
            if tabuleiro[posicao] == '0':
                print('\u25A0',end=' ')
            elif tabuleiro[posicao] == '1':
                print('_',end=' ')
            elif tabuleiro[posicao] == '2':
                print('x',end=' ')
            elif tabuleiro[posicao] == '3':
               print('\u2316',end=' ')
        print()

# Função para reinicializar o tabuleiro com todos os valores igual a '0'
def reinicializarTabuleiro():
    for posicao in tabuleiro:
        tabuleiro[posicao] = '0'


def verificarAfundamentoNavios(posicao, listaNavios):
    if posicao in listaNavios:
        listaNavios.remove(posicao)  # Remove a posição da lista de navios afundados
        return True
    return False


def verificarAfundamentoSubmarino(posicao, listaSubmarinos):
    for submarino in listaSubmarinos:
        if posicao in submarino:
            submarino.remove(posicao)  # Remove a posição da lista do submarino
            if len(submarino) == 0:
                listaSubmarinos.remove(submarino)  # Remove o submarino da lista se estiver completamente afundado
                return 2  # Retorna True para indicar que um submarino foi completamente afundado
            return 1  # Retorna True para indicar que um submarino foi atingido parcialmente
    return False  # Retorna False para indicar que nenhum submarino foi atingido nesta posição






    




        
