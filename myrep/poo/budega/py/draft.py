class Cliente:
    def __init__(self, nome: str):
        self._nome: str = nome
    
    def getNome(self):
        return self._nome

    def __str__(self):
        return self._nome

class Mercantil:
    def __init__(self, num_caixas: int):
        self.num_caixas = num_caixas
        self.caixas = [None] * num_caixas
        self.fila_espera = []
    
    def __str__(self):
        