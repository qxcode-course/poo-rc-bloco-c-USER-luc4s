class Kid:
    def __init__(self, age: int, name: str):
        self.__age = age
        self.__name = name
    
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

    def arrive(self, name: str, age: int):
        self.waiting.insert(0, kid(age, name))
                
    def enter(self):
        if not self.waiting:
            return
        kid = self.waiting.pop(0)
        self.playing.insert(0, kid)

    def remove(self, name: str):
        for i, kid in enumerate(self.waiting):
            if kid.name == name:
                self.waiting.pop(i)
                return
            
        for i, kid in enumerate(self.playing):
            if kid.name == name:
                self.playing.pop(i)
                return
        print(f"fail: {name} nao esta no pula-pula") 