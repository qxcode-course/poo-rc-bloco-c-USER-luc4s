class Kid:
    def __init__(self, age: int, name: str):
        self.__age: int
        self.__name: str
    
    def getAge(self) -> int:
        return self.__age
    
    def getName(self) -> str:
        return self.__name

    def setAge(self, age: int) -> int | None:
        return self.__age
    def setName(self, name: str) -> str | None:
        return self.__name
    
    def __str__(self):
        return f"{self.__age}:{self.__name}"
    