def countingSort(lista):
    valor_maximo = max(lista)
    valor_minimo = min(lista)
    intervalo_valores = valor_maximo - valor_minimo + 1
    contagem_frequencia = [0] * intervalo_valores
    lista_ordenada = [0] * len(lista)

    for i in range(len(lista)):
        contagem_frequencia[lista[i] - valor_minimo] += 1

    for i in range(1, len(contagem_frequencia)):
        contagem_frequencia[i] += contagem_frequencia[i - 1]

    for i in range(len(lista) - 1, -1, -1):
        lista_ordenada[contagem_frequencia[lista[i] - valor_minimo] - 1] = lista[i]
        contagem_frequencia[lista[i] - valor_minimo] -= 1

    for i in range(len(lista)):
        lista[i] = lista_ordenada[i]

def main():
  lista_exemplo = [4, 2, 2, 8, 3, 3, 1]
  countingSort(lista_exemplo)
  print("CountingSort:", lista_exemplo)
  
main()
