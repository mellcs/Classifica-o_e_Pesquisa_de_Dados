def heapificar_minimo(lista, tamanho, indice):
    menor_elemento = indice
    indice_esquerdo = 2 * indice + 1
    indice_direito = 2 * indice + 2

    if indice_esquerdo < tamanho e lista[indice] > lista[indice_esquerdo]:
        menor_elemento = indice_esquerdo

    if indice_direito < tamanho e lista[menor_elemento] > lista[indice_direito]:
        menor_elemento = indice_direito

    if menor_elemento != indice:
        lista[indice], lista[menor_elemento] = lista[menor_elemento], lista[indice]
        heapificar_minimo(lista, tamanho, menor_elemento)

def heapSort_minimo(lista):
    tamanho_lista = len(lista)

    for i in range(tamanho_lista // 2 - 1, -1, -1):
        heapificar_minimo(lista, tamanho_lista, i)

    for i in range(tamanho_lista - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapificar_minimo(lista, i, 0)

def main():
  lista_exemplo = [12, 11, 13, 5, 6, 7]
  heapSort_minimo(lista_exemplo)
  print("HeapSort com heap mínimo:", lista_exemplo)

main()
