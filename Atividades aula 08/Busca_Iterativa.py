def busca_binaria_iterativa(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        if lista[meio] == alvo:
            return meio  
        
        elif lista[meio] < alvo:
            esquerda = meio + 1
        
        else:
            direita = meio - 1
    
    return -1

lista_exemplo = [1, 3, 5, 7, 9, 11, 13, 15]
alvo = 7  

indice = busca_binaria_iterativa(lista_exemplo, alvo)

if indice != -1:
    print(f"Elemento encontrado no índice {indice}")
else:
    print("Elemento não encontrado")
