from jogo import Jogo

class Quatro_em_linhas(Jogo):

    def inicializa_tabuleiro(self):
        self.numero_de_jogadas_realizadas = 0  # conta as jogadas, serve para saber se ainda ha jogadas validas
        self.tabuleiro = {(l, c): ' ' for l in range(6) for c in range(6)}
        print(self.tabuleiro)
    def joga_humano(self, jogador):
        print(f'jogador {jogador} insira a sua jogada')
        while True:
            linha = self._le_linha_coluna_valida('Linha?')
            coluna = self._le_linha_coluna_valida('Coluna?')

            # verifica se a posicao nao esta preenchida, i.e., e valida
            if self.tabuleiro[(linha, coluna)] == ' ':
                self.tabuleiro[(linha, coluna)] = ['X', 'O'][jogador]
                self.numero_de_jogadas_realizadas += 1
                return
            else:
                print('Jogada invalida. Tente de novo')

    def terminou(self):
        pass
    def mostra_tabuleiro(self):
        print(13 * '-=')
        for l in range(6):
            for c in range(6):
                print(f'| {self.tabuleiro[(l, c)]} ', end='')
            print('|\n' + 13 * '-')

    def ha_jogadas_possiveis(self):
        return self.numero_de_jogadas_realizadas < 36
    def jogar(self):
        pass

    mostra_tabuleiro()