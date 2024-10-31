import time
import math

def busca_binaria_iterativa(lista, alvo):
    comparacoes = 0
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        comparacoes += 1
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio, comparacoes
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1, comparacoes

def pesquisa_por_salto(lista, alvo):
    comparacoes = 0
    n = len(lista)
    salto = int(math.sqrt(n))
    anterior, atual = 0, 0
    while atual < n and lista[atual] < alvo:
        comparacoes += 1
        anterior = atual
        atual += salto
    for i in range(anterior, min(atual, n)):
        comparacoes += 1
        if lista[i] == alvo:
            return i, comparacoes
    return -1, comparacoes

def pesquisa_fibonacci(lista, alvo):
    comparacoes = 0
    n = len(lista)
    fib_m2 = 0
    fib_m1 = 1
    fib_m = fib_m2 + fib_m1
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    offset = -1
    while fib_m > 1:
        comparacoes += 1
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
            return i, comparacoes
    if fib_m1 and offset + 1 < n and lista[offset + 1] == alvo:
        return offset + 1, comparacoes
    return -1, comparacoes

# TESTES
lista = list(range(1, 10001))
alvos = [100, 5000, 9999, 10001]

resultados = {
    "Busca Binária": {"tempo": 0, "comparacoes": 0},
    "Pesquisa por Salto": {"tempo": 0, "comparacoes": 0},
    "Pesquisa Fibonacci": {"tempo": 0, "comparacoes": 0},
}

for alvo in alvos:
    inicio = time.time()
    _, comparacoes = busca_binaria_iterativa(lista, alvo)
    tempo = time.time() - inicio
    resultados["Busca Binária"]["tempo"] += tempo
    resultados["Busca Binária"]["comparacoes"] += comparacoes

    inicio = time.time()
    _, comparacoes = pesquisa_por_salto(lista, alvo)
    tempo = time.time() - inicio
    resultados["Pesquisa por Salto"]["tempo"] += tempo
    resultados["Pesquisa por Salto"]["comparacoes"] += comparacoes

    inicio = time.time()
    _, comparacoes = pesquisa_fibonacci(lista, alvo)
    tempo = time.time() - inicio
    resultados["Pesquisa Fibonacci"]["tempo"] += tempo
    resultados["Pesquisa Fibonacci"]["comparacoes"] += comparacoes

for metodo, resultado in resultados.items():
    media_tempo = resultado["tempo"] / len(alvos)
    media_comparacoes = resultado["comparacoes"] / len(alvos)
    print(f"{metodo} - Tempo médio: {media_tempo:.6f} s, Comparações médias: {media_comparacoes:.2f}")
