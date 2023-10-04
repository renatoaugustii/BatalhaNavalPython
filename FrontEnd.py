import os
import Tabuleiro, Persistencia

#Escopo de variáveis globais
Run = 0


# Função para habilitar o menu principal
def menuPrincipal():
    print('⚓⚓⚓  Batalha Naval ⚓⚓⚓')
    print()
    print('1 - Jogar')
    print('2 - Ver Melhores Pontuações')
    print('3 - Sair')
    #Recebe o resultado das opcoes acima, sera tratado o erro caso seja uma opção inválida.
    escolha = input('Escolha uma opção:')
    print('\n')

    # Utilização de um Dicionário para  mapeamento das opções para as funções correspondentes
    opcoes = {
        '1': jogar,
        '2': verMelhoresPontuacoes,
        '3': sair
    }
    
    # Chamada da função correspondente à escolha do usuário
    funcao = opcoes.get(escolha)

    if funcao:
        funcao()
    else:
        #Caso a opção digitada no menu seja inválida o programa retorna ao menu principal e aguarda que seja digitado uma tecla válida.
        menuPrincipal()


def validar_posicao(posicao):
    #verifica se a posição tem dois caracteres inicialmente
    if len(posicao) != 2:
        return False
    #Verifica se o primeiro caracter pertence ao conjunto 'ABCDEF'
    if posicao[0].upper() not in 'ABCDEF':
        return False
    #Verifica se o segundo caracter pertence ao conjunto '123456'
    if posicao[1] not in '123456':
        return False
    #Se for válido a função retorna valor verdadeiro
    return True



def jogar():
    # PREPARAÇÃO DO TABULEIRO PARA O INÍCIO DO JOGO
    Navios = Tabuleiro.criarPosicaoNavios()
    Submarinos = Tabuleiro.criarPosicaoSubmarinos()
    Tabuleiro.reinicializarTabuleiro()
    
    jogadas = 0
    navios_afundados = 0
    submarinos_afundados = 0
    posicoes_jogadas = []  # Lista para rastrear as posições já jogadas

    os.system('pause')
    while True:
        #os.system('cls')
        Tabuleiro.imprimirTabuleiro()
        print(' ')
        print(f'Jogadas até agora: {jogadas}')
        print(f'Afundados até agora = Navios {navios_afundados} de 5 | Submarinos {submarinos_afundados} de 3')
        print('Digite a posição para tentar (formato linha coluna)')
        posicao = input(' Se quiser desistir digite -1: ').upper()
        print('')
        
        if posicao == '-1':
            print('Você desistiu!')
            break

        if validar_posicao(posicao):
            # Verifique se a posição já foi jogada
            if posicao in posicoes_jogadas:
                print('Essa posição já foi jogada. Tente outra.')
                continue  # Vai para a próxima iteração do loop

            posicoes_jogadas.append(posicao)  # Adicione a posição à lista de posições jogadas

            jogadas += 1

            afundamento_submarino = Tabuleiro.verificarAfundamentoSubmarino(posicao, Submarinos)
            
            if Tabuleiro.verificarAfundamentoNavios(posicao, Navios):
                print(f'A posição {posicao} atingiu um navio!')
                Tabuleiro.atualizarNavio(posicao)
                navios_afundados += 1
            elif afundamento_submarino == 2:
                print(f'A posição {posicao} atingiu um Submarino completamente!')
                Tabuleiro.atualizarSubmarino(posicao)
                submarinos_afundados += 1
            elif afundamento_submarino == 1:
                print(f'A posição {posicao} atingiu um Submarino parcialmente!')
                Tabuleiro.atualizarSubmarino(posicao)
            else:
                Tabuleiro.atualizarAgua(posicao)
        
        # Verifique a vitória após cada jogada
        if navios_afundados == 5 and submarinos_afundados == 3:
            print('✨✨✨ VOCÊ GANHOU!!! ✨✨✨')
            nome = input('Qual seu nome?')
            Persistencia.ScoreRankear(nome, jogadas)
            break
        print('')



# Função para a opção "Ver Melhores Pontuações"
def verMelhoresPontuacoes():
    Persistencia.exibirRanking()
    print(' ')
    menuPrincipal()
    # Coloque aqui o código para exibir as melhores pontuações

# Função para a opção "Sair"
def sair():
    global Run
    Run = -1
    #Limpa a tela antes de mostrar a mensagem que o jogador saiu.
    os.system('cls')
    print('Você saiu do jogo!')
    
#Variável Run será utilizada como flag de indicaçao que o game deverá estar rodando. Caso seja digitado o valor de -1, o programa será encerrado.
menuPrincipal()

#Continuar, Verificar porque os submarinos estao contando como acerto mesmo quando acerta apenas 1 parte dele.

