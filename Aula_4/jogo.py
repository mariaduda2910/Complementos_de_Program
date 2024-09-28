from abc import ABC, abstractmethod
import random


class Jogo(ABC):
    """ implementa uma classe para um jogo com 2 humanos"""

    def __init__(self):
        print('bom jogo...')
        self.inicializa_tabuleiro()

    @abstractmethod
    def joga_humano(self, jogador):
        """ metodo que solicita ao humano :jogador: a proxima jogada e coloca-a no tabuleiro
        :param jogador: numero do jogador (0 ou 1)
        """
        pass

    @abstractmethod
    def terminou(self):
        """ devolve `True` se foi verificada a condicao de paragem, i.e., um jogador ganhou.
        devolve `False` caso contrario """
        pass

    @abstractmethod
    def mostra_tabuleiro(self):
        """desenha o tabuleiro"""
        pass

    @abstractmethod
    def inicializa_tabuleiro(self):
        """ inicializa o tabuleiro de jogo"""
        pass

    @abstractmethod
    def ha_jogadas_possiveis(self):
        """ verifica se ainda ha jogadas possiveis ou se o jogo esta empatado"""
        pass

    def jogar(self):
        """ corre o jogo..."""

        # escolhe quem joga em primeiro
        jogador = random.randint(0, 1)
        # jogador = 1

        while True:
            self.mostra_tabuleiro()
            self.joga_humano(jogador)
            if self.terminou():
                self.mostra_tabuleiro()
                print(f'o jogador {jogador} ganhou!!')
                return
            elif not self.ha_jogadas_possiveis():
                print(f'Empataram!!!')
                return
            # passa ao outro jogador
            jogador = (jogador + 1) % 2


class Galo(Jogo):
    jogo = 4
    def inicializa_tabuleiro(self):
        self.numero_de_jogadas_realizadas = 0  # conta as jogadas, serve para saber se ainda ha jogadas validas
        self.tabuleiro = {(l, c): ' ' for l in range(3) for c in range(3)}  # o tabuleiro e um dicionario!
        # print(self.tabuleiro)

    def _le_linha_coluna_valida(self, s):
        """ metodo auxiliar para ler uma posicao que seja 0, 1 ou 2"""
        while True:
            x = input(s)
            if x in ['0', '1', '2']:
                return int(x)

    def joga_humano(self, jogador, i_lista):
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
        lista_posicaoes_ganhadoras = (
            ((0, 0), (0, 1), (0, 2)),  # linha 0
            ((1, 0), (1, 1), (1, 2)),  # linha 1
            ((2, 0), (2, 1), (2, 2)),  # linha 2
            ((0, 0), (1, 0), (2, 0)),  # coluna 0
            ((0, 1), (1, 1), (2, 1)),  # coluna 1
            ((0, 2), (1, 2), (2, 2)),  # coluna 2
            ((0, 0), (1, 1), (2, 2)),  # diagonal
            ((0, 2), (1, 1), (2, 0)),  # anti-diagonal
        )

        for teste in lista_posicaoes_ganhadoras:
            if self.tabuleiro[teste[0]] == self.tabuleiro[teste[1]] == self.tabuleiro[teste[2]] \
                    and self.tabuleiro[teste[0]] != ' ':
                return True  # encontrou posicao ganhadora
        return False

    def mostra_tabuleiro(self):
        print(13 * '-')
        for l in range(3):
            for c in range(3):
                print(f'| {self.tabuleiro[(l, c)]} ', end='')
            print('|\n' + 13 * '-')

    def ha_jogadas_possiveis(self):
        return self.numero_de_jogadas_realizadas < 9


galo = Galo()
galo.jogar()
