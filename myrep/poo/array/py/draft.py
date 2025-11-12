# Criar um array vazio
L1 = []

# Criar um array preenchido
L2: list[int] = [1, 2, 3]
print(L2)

#Obter o tamanho do array
L3: list[int] = [1, 2, 3]
print(len(L2))

# Adicionar e remover elementos ao final
L4: list[int] = [1, 2, 3]
L4.append(4)
print(L4)
ultimo = L4.pop()
print(ultimo)

#Adicionar e remover elementos no início
L5: list[int] = [1, 2, 3]
L5.insert(0, 0)
print(L5)
primeiro = L5.pop(0)
print(primeiro)

#Adicionar e remover elementos em uma posição específica
L6: list[int] = [1, 2, 3]
L6.insert(3, 4)
print(L6)
remover = L6.pop(3)
print(remover)

# Fazer impressão formatada utilizando o método join
L7 = ["Pedro", "Joao", "Maria"]
n = "- ".join(L7)
print(n)

#Criar um array com elementos em sequência de zero a n
x = int(input())
L8 = list(range(x + 1))
print(L8)

#Criar um array com valores aleatórios
import random
L9 = [random.random() for _ in range(10)]
print(L9) 

#Acessar elementos por índice
L10 = [1, 2, 3, 4]
n = int(input("Qual indice você quer?"))
print(L10[n])

#Percorrer os elementos utilizando for-range
L11 = [5, 6, 7, 8]
for i in L11:
    print(L11)

#Percorrer os elementos utilizando for indexado
L12 = [9, 10, 11, 12]
for i in range(len(L12)):
    print(L12)

#Procurar um elemento X usando laço
L13 = [1, 2, 3, 4, 5]
x = int(input())

encontrado = False

for elemento in L13:
    if elemento == x:
        encontrado = True
        break   
if encontrado:
    print(x)
else:
    print("elemento não encontrado")

#Procurar um elemento X usando função nativa
L14 = [10, 20, 30, 40]
y = int(input())

if y in L14:
    print(f"{y} foi encontrado")
else:
    print("elemento nao encontrado")

#Criar um novo array com elementos filtrados, por exemplo, pares
L15 = []
z = int(input())

if z % 2 == 0:
    L15.append(z)
    print(L15)
else:
    print("O elemento nao é par")

#Criar um novo array com elementos transformados, por exemplo, ao quadrado
numeros = [2, 3, 4, 6, 7]
L16 = []
for i in numeros:
    L16.append(i**2)
print(L16)

#Buscar e remover um elemento X
L17 = [1, 2, 3, 4]
print(L17)
r = int(input("Digite um elemento a ser removido: "))

if r in L17:
    L17.remove(r)
    print(f"Elemento removido. Lista atual: {L17}")
else:
    print("Elemento nao encontrado")

# Remover todos os elementos com valor X da lista
