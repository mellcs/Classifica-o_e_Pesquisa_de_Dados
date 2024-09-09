def heapificar_maximo(lista, tamanho, indice):
    maior_elemento = indice
    indice_esquerdo = 2 * indice + 1
    indice_direito = 2 * indice + 2

    if indice_esquerdo < tamanho and lista[indice] < lista[indice_esquerdo]:
        maior_elemento = indice_esquerdo

    if indice_direito < tamanho and lista[maior_elemento] < lista[indice_direito]:
        maior_elemento = indice_direito

    if maior_elemento != indice:
        lista[indice], lista[maior_elemento] = lista[maior_elemento], lista[indice]
        heapificar_maximo(lista, tamanho, maior_elemento)

def heapSort_maximo(lista):
    tamanho_lista = len(lista)

    for i in range(tamanho_lista // 2 - 1, -1, -1):
        heapificar_maximo(lista, tamanho_lista, i)

    for i in range(tamanho_lista - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapificar_maximo(lista, i, 0)

def main():
  lista_exemplo = [12, 11, 13, 5, 6, 7]
  heapSort_maximo(lista_exemplo)
  print("HeapSort com heap máximo:", lista_exemplo)

main()
