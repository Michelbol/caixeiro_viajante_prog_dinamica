import time

# Matriz quadrada com 11 cidades e as distâncias entre elas
cities = [
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

resultados = []

melhor_solucao = float("inf")
melhor_lista = []
lista_tabu = [{'lista': [0,1,2,3,4,5,6,7,8,9,10], 'custo': float("inf")}]
custo = {}

def troca_elem(lista, pos_x, pos_y):
    lista[pos_x], lista[pos_y] = lista[pos_y], lista[pos_x]

def calc_dist(lista):
    dist = 0
    string = ""

    for index in range(len(lista)):
        elemento_atual = lista[index]
        if index+1 == len(lista):
            proximo_element = lista[0]
        else:
            proximo_element = lista[index+1]
        if index == 0:
            string = str(elemento_atual) + "," + str(proximo_element)
        else:
            string += ","+str(proximo_element)
        if string in custo:
            custo_encontrado = custo[string]
        else:
            custo_encontrado = 0
        if custo_encontrado > 0:
            dist = custo_encontrado
        else:
            dist += cities[elemento_atual][proximo_element]
            custo[string] = dist
    return dist


def melhor_resultado_lista_tabu(lista_tabu, index_tabu):
    melhor_solucao_local = float("inf")
    melhor_index = -1
    for index in range(len(lista_tabu)):
        if index_tabu != index:
            if lista_tabu[index]['custo'] < melhor_solucao_local:
                melhor_index = index
    return melhor_index


def busca_tabu(melhor_solucao, melhor_lista):
    for index in range(5000):
        lista_tabu_atual = []
        lista_tabu_atual = lista_tabu_atual+lista_tabu[index]['lista']
        melhor_solucao_local = float("inf")
        lista_local = []
        lista_solucoes_locais = []
        melhor_index = 0
        for index in range(len(lista_tabu_atual)):
            if index + 1 == len(lista_tabu_atual):
                troca_elem(lista_tabu_atual, index, 0)
            else:
                troca_elem(lista_tabu_atual, index, index + 1)

            dist_atual = calc_dist(lista_tabu_atual)
            lista_solucoes_locais.append({ 'lista': lista_tabu_atual, 'custo': dist_atual })
            if dist_atual < melhor_solucao_local:
                melhor_solucao_local = dist_atual
                lista_local = []
                lista_local = lista_local+lista_tabu_atual
                melhor_index = len(lista_solucoes_locais)-1
        resultado = {'lista': lista_local, 'custo': melhor_solucao_local}
        if resultado in lista_tabu:
            resultado = melhor_resultado_lista_tabu(lista_solucoes_locais,melhor_index)
            resultado = lista_solucoes_locais[resultado]
            lista_tabu.append(resultado)
        else:
            lista_tabu.append(resultado)
        if melhor_solucao > resultado['custo']:
            melhor_solucao = resultado['custo']
            melhor_lista = resultado['lista']

    return [melhor_solucao, melhor_lista]


inicio = time.time()
melhor_galera = busca_tabu(melhor_solucao, melhor_lista)
melhor_solucao = melhor_galera[0]
melhor_lista = melhor_galera[1]
fim = time.time()
print(fim - inicio)
print(melhor_solucao, melhor_lista)