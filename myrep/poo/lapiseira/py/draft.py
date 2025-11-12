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
    
    def insert(lead: Grafite):
        if lead.getCalibre == self.getCalibre:
            self.__tambor.append(lead)
        print("fail: calibre incompatível")
        
        
class Grafite:
    def __init__(self):
        self