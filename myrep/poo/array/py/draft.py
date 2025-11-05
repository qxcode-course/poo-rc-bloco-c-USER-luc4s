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




#Acessar elementos por índice
L9 = [1, 2, 3, 4]
n = int(input("Qual indice você quer?"))
print(L9[n])

#Percorrer os elementos utilizando for-range
L10 = [5, 6, 7, 8]
for i in L10:
    print(L10)

#Percorrer os elementos utilizando for indexado
L11 = [9, 10, 11, 12]
for i in range(len(L11)):
    print(L11)

#Procurar um elemento X usando laço
