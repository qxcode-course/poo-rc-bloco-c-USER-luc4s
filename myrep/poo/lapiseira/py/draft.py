class Grafite:
    def __init__(self, dureza: str, calibre: float, size: int):
        self.__dureza = dureza
        self.__calibre = calibre
        self.__size = size
    
    def getCalibre(self):
        return self.__calibre
    
    def getSize(self):
        return self.__size
    
    def gastar(self, valor):
        self.__size -= valor
        if self.__size < 0:
            self.__size = 0
    def usagePerSheet(self):
        return 4
    def __str__(self):
        return f"[{self.__calibre}:{self.__dureza}:{self.__size}]"
    
class Lapiseira:
    def __init__(self, calibre: float):
        self.__calibre: float = calibre
        self.__bico: Grafite | None = None
        self.__tambor: list[Grafite] = []
        
    def getCalibre(self) -> float:
        return self.__calibre
    def getBico(self) -> Grafite | None:
        return self.__bico
    def getTambor(self) -> list[Grafite]:
        return self.__tambor
    
    def insert(self, lead: Grafite):
        if lead.getCalibre() != self.__calibre:
            print("fail: calibre incompatível")
            return False
        self.__tambor.append(lead)
        return True
        
    def puxar_grafite(self):
        if self.__bico is not None:
            print("fail: ja existe grafite no bico")
            return
        if len(self.__tambor) == 0:
            print("fail: tambor vazio")
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

        if self.__bico.getSize() <= 10:
            print("fail: tamanho insuficiente")
            return

        gasto = self.__bico.usagePerSheet()
        
        if self.__bico.getSize() - gasto < 10:
            print("fail: folha incompleta")
            self.__bico.gastar(self.__bico.getSize() - 10)
            return

        self.__bico.gastar(gasto)

    def __str__(self):
        return f"calibre {self.__calibre}"
    
def main():
    lapiseira = None
    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "init":
            lapiseira = Lapiseira(float(args[1]))
            continue

        elif args[0] == "show":
            calibre = lapiseira.getCalibre()
            bico = lapiseira.getBico()
            tambor = lapiseira.getTambor()

            bico_str = str(bico) if bico is not None else "[]"
            tambor_str = "<" + "".join(str(g) for g in tambor) + ">" if len(tambor) else "<>"

            print(f"calibre: {calibre}, bico: {bico_str}, tambor: {tambor_str}")
        
        elif args[0] == "insert":
            calibre = float(args[1])
            dureza = args[2]
            tamanho = int(args[3])
            lead = Grafite(dureza, calibre, tamanho)
            lapiseira.insert(lead)

        elif args[0] == "pull":
            lapiseira.puxar_grafite()

        elif args[0] == "remove":
            lapiseira.remover()

        elif args[0] == "write":
            lapiseira.escrevendo()
        elif args[0] == "show":
            print(lapiseira)
main()