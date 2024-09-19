import os
import heapq

def ordenar_e_salvar_bloco(dados, indice_bloco):
    """Ordena uma parte dos dados e salva em um arquivo temporário."""
    dados.sort()  # Ordena a parte dos dados
    with open(f'bloco_temp_{indice_bloco}.txt', 'w') as arquivo:
        for item in dados:
            arquivo.write(f"{item}\n")  # Salva cada item em uma linha

def merge_sort_externo(arquivo_entrada, tamanho_bloco):
    """Divide um arquivo grande em blocos menores, ordena cada bloco e salva em arquivos temporários."""
    indice_bloco = 0
    with open(arquivo_entrada, 'r') as arquivo:
        bloco = []
        for linha in arquivo:
            bloco.append(int(linha.strip()))
            if len(bloco) >= tamanho_bloco:
                ordenar_e_salvar_bloco(bloco, indice_bloco)
                indice_bloco += 1
                bloco = []
        if bloco:  # Ordena e salva o último bloco, se houver
            ordenar_e_salvar_bloco(bloco, indice_bloco)
    
    return indice_bloco  # Número de arquivos temporários gerados

def mesclar_blocos(num_blocos, arquivo_saida):
    """Mescla arquivos de blocos ordenados em um único arquivo ordenado."""
    arquivos = [open(f'bloco_temp_{i}.txt', 'r') for i in range(num_blocos)]
    heap = []
    
    # Inicializa a heap com o primeiro item de cada arquivo
    for i, arquivo in enumerate(arquivos):
        linha = arquivo.readline().strip()
        if linha:
            heapq.heappush(heap, (int(linha), i))
    
    with open(arquivo_saida, 'w') as arquivo:
        while heap:
            menor, indice_arquivo = heapq.heappop(heap)
            arquivo.write(f"{menor}\n")
            linha = arquivos[indice_arquivo].readline().strip()
            if linha:
                heapq.heappush(heap, (int(linha), indice_arquivo))
    
    # Fecha e remove todos os arquivos temporários
    for a in arquivos:
        a.close()
        os.remove(a.name)  # Remove o arquivo temporário

def principal(arquivo_entrada, arquivo_saida, tamanho_bloco):
    """Executa o Merge Sort Externo."""
    num_blocos = merge_sort_externo(arquivo_entrada, tamanho_bloco)
    mesclar_blocos(num_blocos, arquivo_saida)

if __name__ == "__main__":
    arquivo_entrada = 'arquivo_grande.txt'  # Nome do arquivo de entrada
    arquivo_saida = 'arquivo_ordenado.txt'  # Nome do arquivo de saída
    tamanho_bloco = 1000  # Tamanho do bloco em número de linhas
    principal(arquivo_entrada, arquivo_saida, tamanho_bloco)
