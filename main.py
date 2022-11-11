'''
0 1 0 0 0 0 0 0 1 1 0
1 0 1 0 0 0 0 0 0 1 0
0 1 0 1 0 0 0 0 0 2 1
0 0 1 0 1 0 0 0 0 0 1
0 0 0 1 1 1 0 0 0 0 0
0 0 0 0 1 0 1 0 0 0 1
0 0 0 0 0 1 0 0 0 1 1
0 0 0 0 0 0 0 0 1 2 0
1 0 0 0 0 0 0 1 0 0 0
1 1 2 0 0 0 1 2 0 0 0
0 0 1 1 0 1 1 0 0 0 0
'''
'''
1-o grafo é simples? Por quê? ////
Indique se há arestas múltiplas  ou laços. ////
em que vértices ocorrem laços. ////
Indique, também, entre que vértices as arestas múltipas ocorrem;  ////

2-qual sequência dos graus do grafo? ////
3-qual o número de arestas do grafo? ////
4-o grafo é completo? ////
5-o grafo é regular? ////
6-o grafo é bipartido? Em caso afirmativo dê uma bipartição dos vértices do grafo.
7-o grafo é bipartido completo? Em caso afirmativo dê uma bipartição dos vértices do grafo

No código poderá ser usada, no máximo, uma função.
[1 2 3 4 5 6 7 8 9 10 11]
'''

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

#      Cálculo grafo simples     

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

#   Cálculo dos graus e arestas  

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

'''
6-o grafo é bipartido? Em caso afirmativo dê uma bipartição dos vértices do grafo.
7-o grafo é bipartido completo? Em caso afirmativo dê uma bipartição dos vértices do grafo

Um grafo é dito ser bipartido quando seu conjunto de vértices V puder ser particionado em dois 
subconjuntos V1 e V2, tais que toda aresta de G une um vértice de V1 a outro de V2.

-pegar a lista
-dividir em duas (subconjuntos)
- (Como testar TODAS as possíveis combinações de subconjuntos???) talvez eu não precise testar TODAS...

-Ao pegar o primeiro vértice por exemplo, todos que ele se liga são de outro grupo
-Teoricamente, todos os vértices em sequência seguem a mesma regra, o que liga neles não pode ser o mesmo grupo
-Se essa ordem for quebrada, o grafo não é bipartido.
-toda a aresta de um deve se unir a um vertice do outro

V1    0 1 0 0 0 0 0 0 1 1 0

Tenho que salvar em uma lista diferente, G2 = [V2, V9 E V10]

V2    1 0 1 0 0 0 0 0 0 *1* 0

V2 não pode se unir a nenhum vértice do G2.
V2 se liga em V1, V3 E V10.
V10 é um vértice do G2, logo o grafo não é bipartido

Entre V2 e V10
V2    1 0 1 0 0 0 0 0 0 *1* 0
V10   1 *1* 2 0 0 0 1 2 0 0 0

'''

if(laço):
    bipartido = False

print(f"O grafo é bipartido? Resposta: {resposta}\n")
print(f"O grafo é bipartido completo? Resposta: {resposta}\n")