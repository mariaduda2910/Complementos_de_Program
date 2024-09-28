from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


#Window.size = (2000, 600)

class Jogo:
    def __init__(self):
        pass
class MyJogo(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def marcarPosicao(self):
        self.jogador = []

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





class MyJogoApp(App):
    def build(self):
        return MyJogo()


MyJogoApp().run()
