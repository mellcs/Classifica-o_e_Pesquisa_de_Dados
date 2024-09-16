def counting_sort(array):
    if not array:
        return []

    max_value = max(array)
    
    count_array = [0] * (max_value + 1)
    
    for num in array:
        count_array[num] += 1
    
    sorted_array = []
    for value, count in enumerate(count_array):
        sorted_array.extend([value] * count)
    
    return sorted_array

def main():
    livros = [250, 120, 300, 150, 250, 100, 200]
    
    print("Lista de livros antes da ordenação:")
    print(livros)
    
    livros_ordenados = counting_sort(livros)
    
    print("\nLista de livros após a ordenação:")
    print(livros_ordenados)

main()
