def busca_binaria_recursiva(lista, alvo, esquerda=0, direita=None):
    if direita is None:
        direita = len(lista) - 1
    
    if esquerda > direita:
        return -1

    meio = (esquerda + direita) // 2

    if lista[meio] == alvo:
        return meio 
    
    elif lista[meio] < alvo:
        return busca_binaria_recursiva(lista, alvo, meio + 1, direita)
    
    else:
        return busca_binaria_recursiva(lista, alvo, esquerda, meio - 1)

lista_exemplo = [1, 3, 5, 7, 9, 11, 13, 15]
alvo = 7  

indice = busca_binaria_recursiva(lista_exemplo, alvo)

if indice != -1:
    print(f"Elemento encontrado no índice {indice}")
else:
    print("Elemento não encontrado")
