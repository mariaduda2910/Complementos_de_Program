class Pessoa ():
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
    
    def __repr__(self):
        return f""" 
    nome: {self.nome} 
    endereço: {self.endereco}
    telefone: {self.telefone} """

    @classmethod
    def cria_anonimo(cls):
        return cls("John Doe", "Unknown", "Unknown")


if __name__ == "__main__":
    jonh = Pessoa.cria_anonimo()
    print(jonh)
