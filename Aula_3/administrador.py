from empregado import Empregado


class Administrador(Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, ajuda_de_custo, ):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self.ajuda_de_custo = ajuda_de_custo

    def __repr__(self):
        return f""" 
    Administrador>{super().__repr__()}
    Ajuda De Custo: {self.ajuda_de_custo}
                """

    def calcular_salario_liquido(self):
        return super().calcular_salario_liquido() + self.ajuda_de_custo


if __name__ == "__main__":
    a = Administrador("jose", "rua..", "+351", 45, 800, 15, 200)
    salario_liquido = a.calcular_salario_liquido()
    print(f'O Adm {a.nome} recebe um salário de {salario_liquido} euros. ')
    print()
    print(f'''Informações sobre o adm:
            {a.__repr__()}
    ''')
