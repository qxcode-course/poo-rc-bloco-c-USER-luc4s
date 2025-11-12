class Grafite:
    def __init__(self, dureza: str, calibre: float, size: int):
        self.__dureza = dureza
        self.__calibre = calibre
        self.__size = size
    
    def getCalibre(self):
        return self.__calibre

    def __str__(self):
        return f"{self.__calibre}:{self.__dureza}:{self.__size}mm"
class Lapiseira:
    def __init__(self, calibre: float):
        self.__calibre: float = calibre
        self.__bico: Grafite | None
        self.__tambor: list[Grafite | None] = []
        
    def getCalibre(self) -> float:
        return self.__calibre
    def getBico(self) -> Grafite | None:
        return self.__bico
    def getTambor(self) -> list[Grafite | None]:
        return self.__tambor
    
    def insert(self, lead: Grafite):
        if lead.getCalibre() == self.getCalibre():
            self.__tambor.append(lead)
        else:
            print("fail: calibre incompatível")

    def puxar_grafite(self):
        if self.__bico is not None:
            print("fail: já existe grafite no bico")
            return
        if len(self.__tambor) == 0:
            print("fail: tambor fazio")
            return
        self.__bico =self.__tambor.pop(0)

    def remover(self):
        if self.__bico is None:
            print("fail: nao existe grafite no bico")
            return
        self.__bico = None

    def escrevendo(self):
        if self.__bico is None:
            print("fail: nao existe grafite no bico")
            return
def main():
    lapiseira = 0
    while True:
        line = input()
        print(f"$ {line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            lapiseira = Lapiseira(int(args[1]))