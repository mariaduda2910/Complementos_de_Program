from pessoa import Pessoa


class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, telefone, valor_credito, valor_divida):
        super().__init__(nome, endereco, telefone)
        self.valor_credito = valor_credito
        self.valor_divida = valor_divida

    def __repr__(self):
        return f""" 
    Fornecedor:
    {super().__repr__()}     
                """

    def obter_saldo(self):
        return self.valor_credito - self.valor_divida


if __name__ == "__main__":
    f = Fornecedor("maria", "Rua das flores...", 1414, 500, 200)
    saldo = f.obter_saldo()
    print(f'O valor do saldo de {f.nome} é de {saldo} euros')
