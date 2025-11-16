class Grafite:
    def __init__(self, dureza: str, calibre: float, size: int):
        self.__dureza = dureza
        self.__calibre = calibre
        self.__size = size
    
    def getCalibre(self):
        return self.__calibre

    def __str__(self):
        return f"[{self.__calibre}:{self.__dureza}:{self.__size}]"
class Lapiseira:
    def __init__(self, calibre: float):
        self.__calibre: float = calibre
        self.__bico: Grafite | None = []
        self.__tambor: list[Grafite] = []
        
    def getCalibre(self) -> float:
        return self.__calibre
    def getBico(self) -> Grafite | None:
        return self.__bico
    def getTambor(self) -> list[Grafite]:
        return self.__tambor
    
    def insert(self, lead: Grafite):
        if lead.getCalibre() == self.getCalibre():
            self.__tambor.append(lead)
            return True
        else:
            print("fail: calibre incompatível")
            return False
        
    def puxar_grafite(self):
        
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
        if self.__size <= 10:
            return False
        elif self.__size < 2:
            return None
        else: 
            self.__self -= 2
            return True
    
    def __str__(self):
        return f"[{self.__calibre}:{self.__dureza}:{self.__size}]"
    
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
            if bico is None:
                bico_str = "[]"
            tambor = lapiseira.getTambor()
            bico_str = str(bico) if bico is not None else "None"
            
            if len(tambor) == 0:
                tambor_str = "<>"
            else:
                tambor_str = "<" + "".join(str(g) for g in tambor) + ">"
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

main()