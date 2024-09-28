class Livro:
    def __init__(self, titulo, autor, numero_de_paginas, nacionalidade_do_autor):
        self.titulo = titulo
        self.autor = autor
        self.numero_de_paginas = numero_de_paginas
        self.nacionalidade_do_autor = nacionalidade_do_autor

    def __repr__(self):
        return f'''
                O livro "{self.titulo}",
                Foi escrito por {self.autor},
                Possui {self.numero_de_paginas} páginas,
                O(A) autor(a) nasceu em {self.nacionalidade_do_autor}.
                '''

    @property
    def numero_de_paginas(self):
        return self.__numero_de_paginas

    @numero_de_paginas.setter
    def numero_de_paginas(self, numero_de_paginas):
        assert isinstance(numero_de_paginas, int), "o número de página deve ser um número inteiro"
        assert numero_de_paginas > 0, "o livro deve possuir ao menos uma página."
        self.__numero_de_paginas = numero_de_paginas

    @property
    def nacionalidade_do_autor(self):
        return self.__nacionalidade_do_autor

    @nacionalidade_do_autor.setter
    def nacionalidade_do_autor(self, nacionalidade_do_autor):
        lista_de_paises = ["Portugal", "França", "Espanha"]
        assert nacionalidade_do_autor.title() in lista_de_paises, f'''a nacionalida do autor não faz parte da lista de países aceitos.
        Os países disponíveis são: 
        {lista_de_paises}'''
        self.__nacionalidade_do_autor = nacionalidade_do_autor.title()

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        assert isinstance(autor, str), "o nome do autor não é uma palavra"
        self.__autor = autor.title()

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        assert isinstance(titulo, str), "o nome do livro não é uma palavra"
        self.__titulo = titulo.title()


if __name__ == "__main__":

    try:
        livro = Livro("Turma da monica", "Mauricio de souza", 0, "Brasil")
        print(livro)
    except AssertionError as e:
        print(f"Os dados introduzidos não são válidos, pois {e} ")
    print(100 * "_")
    try:
        livro = Livro("O mundo", "Magda", 5, "portugal")
        print(livro)
    except AssertionError as e:
        print(f"Os dados introduzidos não são válidos, pois {e} ")
    print(100 * "_")
    try:
        livro = Livro("Magda", 5, "portugal")
        print(livro)
    except AssertionError as e:
        print(f"Os dados introduzidos não são válidos, pois {e} ")

    except TypeError as e:
        print(f"Quantidade de argumentos insuficiente '{e}' ")
    print(100 * "_")
