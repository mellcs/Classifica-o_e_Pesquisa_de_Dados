def bubble_sort(lista):
    tamanho_lista = len(lista)
    for iteracao_externa in range(tamanho_lista - 1):
        for indice_atual in range(tamanho_lista - iteracao_externa - 1):
            if lista[indice_atual] > lista[indice_atual + 1]:
                lista[indice_atual], lista[indice_atual + 1] = lista[indice_atual + 1], lista[indice_atual]

def main():
    numeros = [9, 3, 5, 2, 8, 6]
    bubble_sort(numeros)
    print("Lista ordenada:", numeros)

    lista_inversa = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubble_sort(lista_inversa)
    print("Lista inversa ordenada:", lista_inversa)

    lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bubble_sort(lista_ordenada)
    print("Lista já ordenada:", lista_ordenada)

    lista_repetidos = [5, 1, 5, 3, 5, 2, 5, 4, 5]
    bubble_sort(lista_repetidos)
    print("Lista com dados repetidos ordenada:", lista_repetidos)

    lista_aleatoria = [12, 7, 5, 3, 8, 2, 10, 15, 1]
    bubble_sort(lista_aleatoria)
    print("Lista aleatória ordenada:", lista_aleatoria)

main()

########
