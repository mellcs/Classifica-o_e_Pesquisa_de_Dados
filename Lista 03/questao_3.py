def heapify(lista, tamanho_heap, indice_raiz):
    maior_elemento = indice_raiz
    indice_esquerda = 2 * indice_raiz + 1
    indice_direita = 2 * indice_raiz + 2

    if indice_esquerda < tamanho_heap and lista[indice_esquerda] > lista[maior_elemento]:
        maior_elemento = indice_esquerda

    if indice_direita < tamanho_heap and lista[indice_direita] > lista[maior_elemento]:
        maior_elemento = indice_direita

    if maior_elemento != indice_raiz:
        lista[indice_raiz], lista[maior_elemento] = lista[maior_elemento], lista[indice_raiz]
        heapify(lista, tamanho_heap, maior_elemento)

def heap_sort(lista):
    tamanho_lista = len(lista)

    for i in range(tamanho_lista // 2 - 1, -1, -1):
        heapify(lista, tamanho_lista, i)

    for i in range(tamanho_lista - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

def main():
    lista_original = [33, 10, 68, 19, 42, 27, 8]

    lista_ordenada_heap_sort = lista_original.copy()
    heap_sort(lista_ordenada_heap_sort)
    print("Lista ordenada com Heap Sort:", lista_ordenada_heap_sort)

main()
