class Kid:
    def __init__(self, age: int, name: str):
        self.__age: int
        self.__name: str
    
    def getAge(self) -> int:
        return self.__age
    
    def getName(self) -> str:
        return self.__name

    def setAge(self, age: int) ->  None:
        self.__age = age

    def setName(self, name: str) -> None:
        self.__name = name
    
    def __str__(self):
        return f"{self.__age}:{self.__name}"
    
class Trampoline:
    def __init__(self):
        self.playing = []
        self.waiting = []

    def removeFromList(name: str, list_kids: list) -> kid | None:
        for i, Kid in enumerate(list_kids):
            if kid.name == name:
                