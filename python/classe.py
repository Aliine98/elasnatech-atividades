class Funcionario:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.salario = 1500.00

    def get_bonificacao(self):
        return self.salario * 0.5

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'