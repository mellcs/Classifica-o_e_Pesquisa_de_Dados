def pesquisa_fibonacci(lista, alvo):
    fib_m2 = 0  # Fibonacci (m-2)
    fib_m1 = 1  # Fibonacci (m-1)
    fib_m = fib_m2 + fib_m1  # Fibonacci (m)
  
    n = len(lista)
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)

        if lista[i] < alvo:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i

        elif lista[i] > alvo:
            fib_m = fib_m2
            fib_m1 -= fib_m2
            fib_m2 = fib_m - fib_m1

        else:
            return i

    if fib_m1 and offset + 1 < n and lista[offset + 1] == alvo:
        return offset + 1

    return -1

lista_exemplo = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
alvo = 13

indice = pesquisa_fibonacci(lista_exemplo, alvo)

if indice != -1:
    print(f"Elemento encontrado no índice {indice}")
else:
    print("Elemento não encontrado")
