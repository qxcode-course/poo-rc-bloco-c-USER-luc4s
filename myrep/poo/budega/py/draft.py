class Cliente:
    def __init__(self, nome: str):
        self._nome: str = nome
    
    def getNome(self):
        return self._nome

    def __str__(self):
        return self._nome

class Mercantil:
    def __init__(self, quantidade_caixas: int):
        self.caixas: list[Cliente | None] = []
        self.fila_espera: list[Cliente] = []
        for _ in range(quantidade_caixas):
            self.caixas.append(None)

    def __str__(self):
        caixa = ", ".join([str(cliente) if cliente else "-----" for cliente in self.caixas])
        espera = ", ".join([str(cliente) for cliente in self.fila_espera])
        return f"Caixas: [{caixa}]\n Espera: [{espera}]"
    
    def arrive(self, pessoa: Cliente):
        self.fila_espera.append(pessoa)
    
    def call(self, index: int):
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")
        elif not self.fila_espera:
            print("fail: sem clientes")