import math

lista = []
graus = []
simples = True
completo = True
regular = True
bipartido = True
bipartido_completo = True
laço = False
resposta = "Nulo"
grau = 0
arestas = 0

arquivo = open("A.txt", "r")

for x in arquivo.readlines():
    lista.append(x.replace("\n", "").split(" "))

print("\nElemento(s) do grupo:\n")
print("Nome: Luan Petroucic Moreno")
print("R.A: 22.122.076-7\n")
print("Nome: Thiago Monteiro Tinonin")
print("R.A: 22.122.044-5\n")
print("Nome: Fábio Martins Botelho")
print("R.A: 22.122.068-4\n")

print("Representação Matricial: ")

for linha in range(len(lista)):
    for coluna in range(len(lista[linha])):
        lista[linha][coluna] = int(lista[linha][coluna])
        print(f"{lista[linha][coluna]}", end=" ")
    print("")

# Cálculo grafo simples     

for linha in range(len(lista)):
    if(lista[linha][linha] > 0): #Verifica laço
            simples = False
            laço = True
            print(f"\nHá um laço no vértice {linha+1}")
    for coluna in range(len(lista[linha])):
            if(lista[linha][coluna] >= 2): #Verifica aresta multipla
                simples = False
                print(f"\nHá aresta múltipla entre o vértice {linha+1} e o {coluna+1}")  

if(simples == False):
    resposta = "Não."
else:
    resposta = "Sim."

print(f"\nO grafo é simples? Resposta: {resposta}\n")

# Cálculo dos graus e arestas  

for linha in range(len(lista)):
    graus.append(grau)
    grau = 0
    if(lista[linha][linha] > 0):
        grau += 1
    for coluna in range(len(lista[linha])):
        grau += lista[linha][coluna]

graus.append(grau)
graus.remove(0)

print("Os graus dos vértices são:")
for x in range(len(graus)):
    print(graus[x], end=" ")
    arestas += graus[x]

arestas /= 2

print(f"\nO número de arestas é: {arestas}")

# Cálculo grafo completo e regular

for linha in range(len(lista)):
    for coluna in range(len(lista[linha])):
        if(coluna != linha):
            if(lista[linha][coluna] != 1):
                completo = False

if(completo == False):
    resposta = "Não."
else:
    resposta = "Sim."

print(f"\nO grafo é completo? Resposta: {resposta}")

for x in range(len(graus)):
    if(graus[x] != graus[0]):
        regular = False

if(regular == False): 
    resposta = "Não."
else:
    resposta = "Sim."

print(f"\nO grafo é regular? Resposta: {resposta}\n")

vertices = []

# preenchemos uma matriz com os vertices que cada vertice se liga
for linha in range(len(lista)):
    v = []
    for coluna in range(len(lista[linha])):
        if lista[linha][coluna] == 0:
            continue
        v.append('v' + str(coluna))
    vertices.append(v)

fator = False

for vertice in range(len(vertices)):
    # fator que quebra o loop caso não seja bipartido
    if fator:
        break
    for indece in range(len(vertices[vertice])):
        # caso chege no ultimo indice, não sera mais necessario comprarar
        if vertice == (len(vertices) - 1):
            break
        # compara se o x se liga com um x, caso sim, não é bipartido
        if vertices[vertice][indece] == vertices[vertice+1][indece]:
            bipartido = False
            fator = True
            break

if(laço):
    bipartido = False

if not bipartido: 
    resposta = "Não."
else:
    resposta = "Sim."

print(f"O grafo é bipartido? Resposta: {resposta}\n")

# um grafo bipartido completo contém Km,n. O numero de arestas é m*n
count = 0
for vertice in range(len(vertices)):
    count +=1

if count % 2 == 0:
    count = count / 2
    m = count
    n = count

if not count % 2 == 0:
    count = count / 2
    m = math.floor(count)
    n = math.ceil(count)

if (m*n) == arestas:
    resposta = "Sim."
if (m*n) != arestas:
    resposta = "Não."

print(f"O grafo é bipartido completo? Resposta: {resposta}\n")