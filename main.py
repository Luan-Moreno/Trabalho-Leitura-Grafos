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
resposta = "Nulo"
grau = 0
arestas = 0

arquivo = open("A.txt", "r");

for x in arquivo.readlines():
    lista.append(x.replace("\n", "").split(" "))

print("\nElemento(s) do grupo:\n")
print("Nome: Luan Petroucic Moreno")
print("R.A: 22.122.076-7\n")

print("Representação Matricial: ")

for e in range(len(lista)):
    for ee in range(len(lista[e])):
        lista[e][ee] = int(lista[e][ee])
        print(f"{lista[e][ee]}", end=" ")
    print("")

#teste grafo simples#

#simples: não tem laço ou aresta multipla

#como o laço aparece na matriz? e a aresta multipla?

#aresta multipla entre v8 e v10 
# [1 2 3 4 5 6 7 8 9 10 11]
# [0 0 0 0 0 0 0 0 1 *2* 0]
# algum elemento se relaciona 2 vezes com outro

#laço em v5
# [1 2 3 4 5 6 7 8 9 10 11]
# [0 0 0 1 1 *1* 0 0 0 0 0]
# o 5 elemento se relaciona consigo mesmo, então há laço

#agora, vamos verificar se há aresta múltipla ou laço:

for e in range(len(lista)):
    if(lista[e][e] > 0): #Verifica laço
            simples = False
            print(f"\nHá um laço no vértice {e+1}")
    for ee in range(len(lista[e])):
            if(lista[e][ee] >= 2): #Verifica aresta multipla
                simples = False
                print(f"\nHá aresta múltipla entre o vértice {e+1} e o {ee+1}")  

if(simples == False):
    resposta = "Não."
else:
    resposta = "Sim."

print(f"\nO grafo é simples? Resposta: {resposta}\n")

#################################
#Cálculo dos graus e das arestas#
#################################
for e in range(len(lista)):
    graus.append(grau)
    grau = 0
    if(lista[e][e] > 0):
        grau += 1
    for ee in range(len(lista[e])):
        grau += lista[e][ee]

graus.append(grau)
graus.remove(0)

print("Os graus dos vértices são:")
for x in range(len(graus)):
    print(graus[x], end=" ")
    arestas += graus[x]

arestas /= 2

print(f"\nO número de arestas é: {arestas}")
#################################
'''
4-o grafo é completo? ////
5-o grafo é regular?  ////
6-o grafo é bipartido? Em caso afirmativo dê uma bipartição dos vértices do grafo.
7-o grafo é bipartido completo? Em caso afirmativo dê uma bipartição dos vértices do grafo

No código poderá ser usada, no máximo, uma função.
[1 2 3 4 5 6 7 8 9 10 11]
'''

for e in range(len(lista)):
    for ee in range(len(lista[e])):
        if(ee != e):
            if(lista[e][ee] != 1):
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