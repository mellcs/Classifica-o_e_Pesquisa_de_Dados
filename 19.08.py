def bubble_sort(lista):
    tamanho_lista = len(lista)
    # Loop através de todos os elementos da lista
    for iteracao_externa in range(tamanho_lista - 1):
        # Os últimos iteracao_externa elementos já estão ordenados
        for indice_atual in range(tamanho_lista - iteracao_externa - 1):
            # Troca se o elemento atual for maior que o próximo
            if lista[indice_atual] > lista[indice_atual + 1]:
                lista[indice_atual], lista[indice_atual + 1] = lista[indice_atual + 1], lista[indice_atual]

def main():
  numeros = [9, 3, 5, 2, 8, 6]

  bubble_sort(numeros)
  print("Lista ordenada:", numeros)

#####
