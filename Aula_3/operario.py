from empregado import Empregado


class Operario(Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, valor_producao, comissao):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self.valor_producao = valor_producao
        self.comissao = comissao

    def __repr__(self):
        return f"""   Operário>{super().__repr__()}  
    Valor de produção: {self.valor_producao}
    Comissão: {self.comissao}"""

    def calcular_salario_liquido(self):
        return (self.comissao * self.valor_producao / 100) + super().calcular_salario_liquido()

    def calcular_produtividade(self, salario):
        return salario - self.valor_producao


if __name__ == "__main__":
    o = Operario("jose", "rua..", "+351", 45, 800, 15, 100, 5)
    salario_liquido = o.calcular_salario_liquido()
    produtividade = o.calcular_produtividade(salario_liquido)
    print(f'O salário do operário {o.nome} é {salario_liquido} euros. \n Sua produtividade foi de: {produtividade}')
    print()
    print(f'Informações sobre o operário: \n {o.__repr__()}')
