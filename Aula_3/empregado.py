from pessoa import Pessoa


class Empregado(Pessoa):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto):
        super().__init__(nome, endereco, telefone)
        self.codigo_setor = codigo_setor
        self.salario_base = salario_base
        self.imposto = imposto

    def __repr__(self):
        return f'''
    Empregado> {super().__repr__()} 
    Código do setor: {self.codigo_setor}'''

    def calcular_salario_liquido(self):
        return self.salario_base - (self.imposto * self.salario_base / 100)


if __name__ == "__main__":
    e = Empregado("jose", "rua..", "+351", 45, 800, 15)
    salario_liquido = e.calcular_salario_liquido()
    print(f'O empregado {e.nome} recebe {salario_liquido} euros líquidos.')
    print()
    print(f'''Informações sobre o funcionário:
            {e.__repr__()}
''')
