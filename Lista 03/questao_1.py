def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        elemento_pivo = lista[len(lista) // 2]
        elementos_menores = [elemento for elemento in lista if elemento < elemento_pivo]
        elementos_iguais = [elemento for elemento in lista if elemento == elemento_pivo]
        elementos_maiores = [elemento for elemento in lista if elemento > elemento_pivo]
        return quick_sort(elementos_menores) + elementos_iguais + quick_sort(elementos_maiores)

def shell_sort(lista):
    intervalo_de_divisao = len(lista) // 2
    while intervalo_de_divisao > 0:
        for indice in range(intervalo_de_divisao, len(lista)):
            valor_temporario = lista[indice]
            posicao_atual = indice
            while posicao_atual >= intervalo_de_divisao and lista[posicao_atual - intervalo_de_divisao] > valor_temporario:
                lista[posicao_atual] = lista[posicao_atual - intervalo_de_divisao]
                posicao_atual -= intervalo_de_divisao
            lista[posicao_atual] = valor_temporario
        intervalo_de_divisao //= 2

def main():
    lista_original = [33, 10, 68, 19, 42, 27, 8]
    
    lista_ordenada_quick_sort = quick_sort(lista_original.copy())
    print("Lista ordenada com Quick Sort:", lista_ordenada_quick_sort)
    
    lista_ordenada_shell_sort = lista_original.copy()
    shell_sort(lista_ordenada_shell_sort)
    print("Lista ordenada com Shell Sort:", lista_ordenada_shell_sort)

main()
