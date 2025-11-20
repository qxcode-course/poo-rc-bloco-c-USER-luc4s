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
        return f"{self.__name}:{self.__age}"
    
class Trampoline:
    def __init__(self):
        self.playing = []
        self.waiting = []

    def arrive(self, name: str, age: int):
        self.waiting.insert(0,Kid(age, name))
                
    def enter(self):
        if not self.waiting:
            return
        kid = self.waiting.pop(0)
        self.playing.insert(0, kid)

    def leave(self):
        if not self.playing:
            return
        kid = self.playing.pop(0)
        self.waiting.insert(0, kid)

    def remove(self, name: str):
        for i, kid in enumerate(self.waiting):
            if kid.getName() == name:
                self.waiting.pop(i)
                return
            
        for i, kid in enumerate(self.playing):
            if kid.getName() == name:
                self.playing.pop(i)
                return
        print(f"fail: {name} nao esta no pula-pula")
        
    def show(self):
        w = ", ".join(str(kid) for kid in self.waiting)
        p = ", ".join(str(kid) for kid in self.playing)
        print(f"[{w}] => [{p}]")

def main():
    tramp = Trampoline()
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            continue
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "arrive":
            name = args[1]
            age = int(args[2])
            tramp.arrive(name, age)
        
        elif args[0] == "enter":
            tramp.enter()
        elif args[0] == "leave":
            tramp.leave()
        elif args[0] == "remove":
            name = args[1]
            tramp.remove(name)
        elif args[0] == "show":
            tramp.show()
        else:
            print("fail: comando invalido")

main()