import os
from Tabuleiro import startTabuleiro

#Escopo de variáveis globais
Run = 0

# Função para habilitar o menu principal
def menuPrincipal():
    os.system('cls')
    print('***** Batalha Naval *****')
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
    print('TRUUUUUUE')
    return True



# Função para a opção "Jogar"
def jogar():
    

    tabuleiro= startTabuleiro()
    tabuleiro.imprimir_tabuleiro()

    print() #linha em branco
    print('Jogadas até agora: 0')
    print('Afundados até agora = Navios 0 de 5 | Submarino 0 de 3')
    print('Digite a posição para tentar (formato linha coluna)')
    posicao = input(' Se quiser desistir digite -1:')
    if posicao=='-1':
        print('PEDE PRA SAIR')
    else:    
        validar_posicao(posicao)


    

# Função para a opção "Ver Melhores Pontuações"
def verMelhoresPontuacoes():
    print('Você escolheu ver as melhores pontuações!')
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



#Continuar, ao digitar linha e coluna preciso marcar no gabarito oque ocorreu.

