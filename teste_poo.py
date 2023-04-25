class Valor:
    def __init__(self, nome, valor, valorb = 0):
        self.nome = nome
        self.valora = valor
        self.valorb = valorb
    def inverso(self):
        self.valora, self.valorb = self.valorb, self.valora