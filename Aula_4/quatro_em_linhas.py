from jogo import Jogo


class QuatroEmLinhas(Jogo):

    def inicializa_tabuleiro(self):
        self.numero_de_jogadas_realizadas = 0  # conta as jogadas, serve para saber se ainda ha jogadas validas
        self.tabuleiro = {(l, c): ' ' for l in range(6) for c in range(6)}
        # print(self.tabuleiro)

    def mostra_tabuleiro(self):
        print(25 * '-')
        for l in range(6):
            for c in range(6):
                print(f'| {self.tabuleiro[(l, c)]} ', end='')
            print('|\n' + 25 * '-')

    def _le_linha_coluna_valida(self, s):
        """ metodo auxiliar para ler uma posicao que seja 0, 1 ou 2"""
        while True:
            x = input(s)
            if x in ['0', '1', '2', '3', '4', '5']:
                return int(x)

    def joga_humano(self, jogador, i_lista):
        print(f'jogador {jogador} insira a sua jogada')
        while True:

            # linha = self._le_linha_coluna_valida('Linha?')
            coluna = self._le_linha_coluna_valida('Coluna?')
            linha = i_lista[coluna] - 1
            i_lista[coluna] = linha
            print(i_lista)
            # verifica se a posicao nao esta preenchida, i.e., e valida
            try:
                if self.tabuleiro[(linha, coluna)] == ' ':
                    self.tabuleiro[(linha, coluna)] = ['X', 'O'][jogador]
                    self.numero_de_jogadas_realizadas += 1
                    return
                else:
                    print('Jogada invalida. Tente de novo')
            except KeyError:
                print("Coluna cheia")

    def terminou(self):
        lista_posicaoes_ganhadoras = (
            ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)),
            ((1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)),
            ((2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)),
            ((3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)),
            ((4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)),
            ((5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)),
        )
        # Conferir diagonal pra baixo
        for l in range(3):
            for c in range(3):
                if self.tabuleiro[l, c] == self.tabuleiro[l + 1, c + 1] == self.tabuleiro[l + 2, c + 2] == \
                        self.tabuleiro[
                            l + 3, c + 3] and self.tabuleiro[l, c] != ' ':
                    return True  # encontrou posicao ganhadora

        # Conferir diagonal pra cima
        for l in range(3, 6):
            for c in range(3):
                if self.tabuleiro[l, c] == self.tabuleiro[l - 1, c + 1] == self.tabuleiro[l - 2, c + 2] == \
                        self.tabuleiro[
                            l - 3, c + 3] and self.tabuleiro[l, c] != ' ':
                    return True  # encontrou posicao ganhadora

        # para conferir horizontais
        for l in range(6):
            for c in range(3):
                if self.tabuleiro[l, c] == self.tabuleiro[l, c + 1] == self.tabuleiro[l, c + 2] == self.tabuleiro[
                    l, c + 3] and self.tabuleiro[l, c] != ' ':
                    return True  # encontrou posicao ganhadora

        # para verificar colunas
        for l in range(3):
            for c in range(6):
                if self.tabuleiro[l, c] == self.tabuleiro[l + 1, c] == self.tabuleiro[l + 2, c] == self.tabuleiro[
                    l + 3, c] and self.tabuleiro[l, c] != ' ':
                    return True  # encontrou posicao ganhadora

        return False

    def ha_jogadas_possiveis(self):
        return self.numero_de_jogadas_realizadas < 36


jogo = QuatroEmLinhas()
jogo.jogar()
