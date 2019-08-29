from itertools import permutations 
import time

# Matriz quadrada com 11 cidades e as distâncias entre elas
cidades = [
  #0    #1  #2  #3  #4  #5  #6  #7  #8  #9  #10
  [0,   29, 20, 21, 16, 31, 100,12, 4, 31,  18],  #0
  [29,  0,  15, 29, 28, 40, 72, 21, 29, 41, 12],  #1
  [20,  15, 0,  15, 14, 25, 81, 9,  23, 27, 13],  #2
  [21,  29, 15, 0,  4,  12, 92, 12, 25, 13, 25],  #3
  [16,  28, 14, 4,  0,  16, 94, 9,  20, 16, 22],  #4
  [31,  40, 25, 12, 16, 0,  95, 24, 36, 3,  37],  #5
  [100, 72, 81, 92, 94, 95, 0,  90, 101,99, 84],  #6
  [12,  21, 9,  12, 9,  24, 90, 0,  15, 25, 13],  #7
  [4,   29, 23, 25, 20, 36, 101,15, 0,  35, 18],  #8
  [31,  41, 27, 13, 16, 3,  99, 25, 35, 0,  38],  #9
  [18,  12, 13, 25, 22, 37, 84, 13, 18, 38, 0]    #10
]

resultados = {}
vetorCidades = [0,1,2,3,4,5,6,7,8,9]

def getChave(lista):
    retorno = ""
    virgula = ""

    for i in range(len(lista)):
        retorno += virgula + str(lista[i])
        virgula = ','

    return retorno

def cortaCaminho(lista):
    chave = ""
    virgula = ""
    penultimaCidade = 0
    ultimaCidade = 0

    for i in range(len(lista)):
        if (i == len(lista) - 2):
            penultimaCidade = lista[i]

        if (i == len(lista) - 1):
            ultimaCidade = lista[i]
        else:
            chave += virgula + str(lista[i])
            virgula = ","

    return [chave,penultimaCidade,ultimaCidade]

def transformaString(lista):
    retorno = ""

    for i in range(len(lista)):
        retorno += str(lista[i])

    return retorno

def calcularDistancia(listaCidades):
    #Se for o caso da permutação de apenas dois valores, deve ser apenas armazenado os valores
    if (len(listaCidades) == 2):
        chave = getChave(listaCidades)
        resultados[chave] = cidades[listaCidades[0]][listaCidades[1]]
    else:
        resultAnterior = cortaCaminho(listaCidades)
        chave = getChave(listaCidades)
        resultados[chave] = resultados[resultAnterior[0]] + cidades[resultAnterior[1]][resultAnterior[2]]  

    return resultados[chave]

def voltaCidade(listaCidades):
   return cidades[listaCidades[0]][listaCidades[len(listaCidades)-1]]

def progDinamica():
    melhorCusto = float('inf')
    melhorLista = {}

    #Conta desde 2 numeros até a quantidade de  cidades
    for countPerm in range(2,len(vetorCidades) + 1):
        #Faz a permutação das cidades o valor da interação
        perm = permutations(vetorCidades,countPerm) 

        #Para cara permutação calcula a distancia
        for itemPerm in list(perm): 
            custoLocal = calcularDistancia(itemPerm)

            if (countPerm == len(vetorCidades)):
                custoLocal += voltaCidade(itemPerm)

                if (melhorCusto > custoLocal):
                    melhorCusto = custoLocal
                    melhorLista = itemPerm

    return [melhorCusto,melhorLista]

inicio = time.time()
melhorResultado = progDinamica()
fim = time.time()
print(fim - inicio)
print(melhorResultado)