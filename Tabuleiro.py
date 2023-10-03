class startTabuleiro():
        def __init__(self):
            self.tabuleiro = {
                'A1': ' ', 'A2': ' ', 'A3': ' ', 'A4': ' ', 'A5': ' ', 'A6': ' ',
                'B1': ' ', 'B2': ' ', 'B3': ' ', 'B4': ' ', 'B5': ' ', 'B6': ' ',
                'C1': ' ', 'C2': ' ', 'C3': ' ', 'C4': ' ', 'C5': ' ', 'C6': ' ',
                'D1': ' ', 'D2': ' ', 'D3': ' ', 'D4': ' ', 'D5': ' ', 'D6': ' ',
                'E1': ' ', 'E2': ' ', 'E3': ' ', 'E4': ' ', 'E5': ' ', 'E6': ' ',
                'F1': ' ', 'F2': ' ', 'F3': ' ', 'F4': ' ', 'F5': ' ', 'F6': ' ',
            }

        def imprimir_tabuleiro(self):
            #Cabeçalho numérico alinhado conforme as demais colunas
            print('    1 2 3 4 5 6')
            #For Incrementa as letras correspondentes para as linhas, valores são usados os que foram declarados no tabuleiro
            for linha in 'ABCDEF':
                print(linha,'|', end=' ')
                for coluna in range(1, 7):
                    #print(startTabuleiro.tabuleiro[linha + str(coluna)], end=' ')
                    print('\u25A0', end=' ')
                print()




        

        
