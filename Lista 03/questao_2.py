import time
import random

def insertion_sort(lista):
    for index_atual in range(1, len(lista)):
        valor_chave = lista[index_atual]
        indice_anterior = index_atual - 1
        while indice_anterior >= 0 and valor_chave < lista[indice_anterior]:
            lista[indice_anterior + 1] = lista[indice_anterior]
            indice_anterior -= 1
        lista[indice_anterior + 1] = valor_chave

def selection_sort(lista):
    for indice_atual in range(len(lista)):
        indice_minimo = indice_atual
        for indice_comparacao in range(indice_atual + 1, len(lista)):
            if lista[indice_comparacao] < lista[indice_minimo]:
                indice_minimo = indice_comparacao
        lista[indice_atual], lista[indice_minimo] = lista[indice_minimo], lista[indice_atual]

def bubble_sort(lista):
    tamanho_lista = len(lista)
    for indice_externo in range(tamanho_lista):
        for indice_interno in range(0, tamanho_lista - indice_externo - 1):
            if lista[indice_interno] > lista[indice_interno + 1]:
                lista[indice_interno], lista[indice_interno + 1] = lista[indice_interno + 1], lista[indice_interno]

def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        lista_esquerda = lista[:meio]
        lista_direita = lista[meio:]

        merge_sort(lista_esquerda)
        merge_sort(lista_direita)

        indice_esquerda = indice_direita = indice_lista = 0

        while indice_esquerda < len(lista_esquerda) and indice_direita < len(lista_direita):
            if lista_esquerda[indice_esquerda] < lista_direita[indice_direita]:
                lista[indice_lista] = lista_esquerda[indice_esquerda]
                indice_esquerda += 1
            else:
                lista[indice_lista] = lista_direita[indice_direita]
                indice_direita += 1
            indice_lista += 1

        while indice_esquerda < len(lista_esquerda):
            lista[indice_lista] = lista_esquerda[indice_esquerda]
            indice_esquerda += 1
            indice_lista += 1

        while indice_direita < len(lista_direita):
            lista[indice_lista] = lista_direita[indice_direita]
            indice_direita += 1
            indice_lista += 1

def medir_tempo(funcao_ordenacao, lista):
    inicio = time.time()
    funcao_ordenacao(lista)
    return time.time() - inicio

def gerar_lista_ordenada(tamanho):
    return list(range(tamanho))

def gerar_lista_reversa_ordenada(tamanho):
    return list(range(tamanho, 0, -1))

def gerar_lista_com_repeticoes(tamanho):
    return [random.choice(range(tamanho // 2)) for _ in range(tamanho)]

def gerar_lista_aleatoria(tamanho):
    return [random.randint(0, tamanho) for _ in range(tamanho)]

#testes
tamanhos = [100, 500, 1000] 

for tamanho in tamanhos:
    print(f"Tamanho da lista: {tamanho}")
    
    lista_ordenada = gerar_lista_ordenada(tamanho)
    lista_reversa_ordenada = gerar_lista_reversa_ordenada(tamanho)
    lista_com_repeticoes = gerar_lista_com_repeticoes(tamanho)
    lista_aleatoria = gerar_lista_aleatoria(tamanho)
    
    for funcao_ordenacao, nome_algoritmo in [(insertion_sort, "Insertion Sort"), 
                                              (selection_sort, "Selection Sort"), 
                                              (bubble_sort, "Bubble Sort"), 
                                              (merge_sort, "Merge Sort")]:
        
        print(f"\n{nome_algoritmo}:")
        
        tempo_ordenacao = medir_tempo(funcao_ordenacao, lista_ordenada[:])
        print("Lista já ordenada:", tempo_ordenacao, "segundos")
        
        tempo_ordenacao = medir_tempo(funcao_ordenacao, lista_reversa_ordenada[:])
        print("Lista ordenada de maneira inversa:", tempo_ordenacao, "segundos")
        
        tempo_ordenacao = medir_tempo(funcao_ordenacao, lista_com_repeticoes[:])
        print("Lista com dados repetidos:", tempo_ordenacao, "segundos")
        
        tempo_ordenacao = medir_tempo(funcao_ordenacao, lista_aleatoria[:])
        print("Lista com dados aleatórios:", tempo_ordenacao, "segundos")
