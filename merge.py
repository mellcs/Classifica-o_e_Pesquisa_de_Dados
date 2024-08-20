def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2  
        lista_esquerda = lista[:meio]  
        lista_direita = lista[meio:]

        merge_sort(lista_esquerda)
        merge_sort(lista_direita)

        indice_esquerda = 0
        indice_direita = 0
        indice_lista_principal = 0

        while indice_esquerda < len(lista_esquerda) and indice_direita < len(lista_direita):
            if lista_esquerda[indice_esquerda] < lista_direita[indice_direita]:
                lista[indice_lista_principal] = lista_esquerda[indice_esquerda]
                indice_esquerda += 1
            else:
                lista[indice_lista_principal] = lista_direita[indice_direita]
                indice_direita += 1
            indice_lista_principal += 1

        while indice_esquerda < len(lista_esquerda):
            lista[indice_lista_principal] = lista_esquerda[indice_esquerda]
            indice_esquerda += 1
            indice_lista_principal += 1

        while indice_direita < len(lista_direita):
            lista[indice_lista_principal] = lista_direita[indice_direita]
            indice_direita += 1
            indice_lista_principal += 1

def main():
    numeros = [34, 7, 23, 32, 5, 62, 32, 74, 23, 65, 43, 8, 12, 90, 54]
    print("Lista original:", numeros)
    merge_sort(numeros)
    print("Lista ordenada:", numeros)

    lista_inversa = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("\nLista inversa original:", lista_inversa)
    merge_sort(lista_inversa)
    print("Lista inversa ordenada:", lista_inversa)

    lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("\nLista já ordenada original:", lista_ordenada)
    merge_sort(lista_ordenada)
    print("Lista já ordenada:", lista_ordenada)

    lista_repetidos = [5, 1, 5, 3, 5, 2, 5, 4, 5]
    print("\nLista com dados repetidos original:", lista_repetidos)
    merge_sort(lista_repetidos)
    print("Lista com dados repetidos ordenada:", lista_repetidos)

    lista_aleatoria = [12, 7, 5, 3, 8, 2, 10, 15, 1]
    print("\nLista aleatória original:", lista_aleatoria)
    merge_sort(lista_aleatoria)
    print("Lista aleatória ordenada:", lista_aleatoria)

main()
