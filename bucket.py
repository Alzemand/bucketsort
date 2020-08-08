# Bucket Sort usando Python
from random import uniform, normalvariate
try:
    from matplotlib import pyplot as plt
except:
    print("To display the graphics run: pip3 install matplotlib")

elementos = 100000
count = 0
A = []
eixox = []
eixoy = []

def bucket_sort(array):
    bucket = []
    # Criar uma lista vazia
    for i in range(100):
        bucket.append([])
    # Inserir elementos em seus respectivos indices
    for j in array:
        index_b = int(100 * j)
        bucket[index_b].append(j)
    # Classificar os elementos no bucket
    for i in range(100):
        bucket[i] = sorted(bucket[i])
    return bucket

def bucketToArray(array):
    k = 0
    temp = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            temp.append(array[i][j])
            k += 1
    return temp

print('\n')
opt = input("To generate random numbers type 1)Uniform  or 2)Normalvariate: ")

# Gere randomicamente o vetor A de 100000 elementos tipo float 0.0≤x<1.0
if int(opt) == 1:
    for x in range(elementos):
        y = round(uniform(0.0, 0.99999), 5)
        A.append(y)
elif int(opt) == 2:
    for x in range(elementos):
        y = round(normalvariate(0.5, 0.1), 5)
        A.append(y)

# Criar um vetor B, ordenado com bucket sort
B = bucket_sort(A)

# Ordenar o vetor original A
A = bucketToArray(B)

# Exibir o vetor B com a lista encadeada.
for x in B:
    print ("[" + str(count) + "]", x)
    count += 1
    eixox.append(count)
    eixoy.append(len(x))

# Exibir a quantidade de itens nas listas
print("\n")
opt = input("Show len() in B[]? (n/y): ")
count = 0
if opt == "y":
   for x in B:
    print ("[" + str(count) + "]", len(x))
    count += 1

print("\n")
opt = input("Show the new A[] ordered vector? (n/y): ")
if opt == "y":
    for x in A:
        print(x)

# Limpar o vetor
A=[]

print("\n")
opt = input("Show graphics? (n/y): ")
if opt == "y":
    # Exibir o grafico
    plt.bar(eixox, eixoy)
    plt.show()