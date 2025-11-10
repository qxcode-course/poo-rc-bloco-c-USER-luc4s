class Pessoa:
    def __init__(self, nome: str):
        self._nome: str = nome
    
    def getNome(self):
        return self._nome

    def __str__(self):
        return self._nome

class Mercantil:
    def __init__(self, quantidade_caixas: int):
        self.caixas: list[Pessoa | None] = []
        self.fila_espera: list[Pessoa] = []
        for _ in range(quantidade_caixas):
            self.caixas.append(None)

    def __str__(self):
        caixa = ", ".join([str(cliente) if cliente else "-----" for cliente in self.caixas])
        espera = ", ".join([str(cliente) for cliente in self.fila_espera])
        return f"Caixas: [{caixa}]\nEspera: [{espera}]"
    
    def arrive(self, pessoa: Pessoa):
        self.fila_espera.append(pessoa)
    
    def call(self, index: int):
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")
        elif not self.fila_espera:
            print("fail: sem clientes")
        else:
            cliente = self.fila_espera.pop(0)
            self.caixas[index] = cliente

    def finish(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return None
        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return None
        cliente = self.caixas[index]
        self.caixas[index] = None
        return cliente
    
def main():
    mercantil = None
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            mercantil = Mercantil(int(args[1]))
        elif args[0] == "arrive":
            nome = args[1]
            mercantil.arrive(Pessoa(nome))
        elif args[0] == "call":
            index = int(args[1])
            mercantil.call(index)
        elif args[0] == "finish":
            index = int(args[1])
            mercantil.finish(index)
        elif args[0] == "show":
            print(mercantil)
main()