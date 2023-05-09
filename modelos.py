class Valor:
    def __init__(self, nome, valor, valorb = 0):
        self.nome = nome
        self.valora = valor
        self.valorb = valorb
    def inverso(self):
        self.valora, self.valorb = self.valorb, self.valora

class Explicação:
    def __init__(self):
        self.escolha = False
        self.mensagem = 'desativadas'

    def ativa(self):
        if not self.escolha:
            self.escolha = True
            self.mensagem = 'ativadas'
        else:
            self.escolha = False
            self.mensagem = 'desativadas'