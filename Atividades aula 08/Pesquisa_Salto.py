import math

def pesquisa_por_salto(lista, alvo):
    n = len(lista)
    salto = int(math.sqrt(n))

    anterior, atual = 0, 0
    while atual < n and lista[atual] < alvo:
        anterior = atual
        atual += salto
    
    for i in range(anterior, min(atual, n)):
        if lista[i] == alvo:
            return i  
    
    return -1  

lista_exemplo = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
alvo = 13 

indice = pesquisa_por_salto(lista_exemplo, alvo)

if indice != -1:
    print(f"Elemento encontrado no índice {indice}")
else:
    print("Elemento não encontrado")
