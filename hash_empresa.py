class Arquivo:
    def __init__(self, nome, caminho, tamanho):
        self.nome = nome
        self.caminho = caminho
        self.tamanho = tamanho

    def __repr__(self):
        return f"Arquivo(Nome: {self.nome}, Caminho: {self.caminho}, Tamanho: {self.tamanho} KB)"

class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def funcao_hash(self, chave):
        return sum(ord(c) for c in chave) % self.tamanho

    def adicionar(self, arquivo):
        indice = self.funcao_hash(arquivo.nome)
        for item in self.tabela[indice]:
            if item.nome == arquivo.nome:
                print(f"Arquivo com o nome '{arquivo.nome}' já existe.")
                return
        self.tabela[indice].append(arquivo)

    def buscar(self, nome):
        indice = self.funcao_hash(nome)
        for arquivo in self.tabela[indice]:
            if arquivo.nome == nome:
                return arquivo
        return None

    def remover(self, nome):
        indice = self.funcao_hash(nome)
        for arquivo in self.tabela[indice]:
            if arquivo.nome == nome:
                self.tabela[indice].remove(arquivo)
                print(f"Arquivo '{nome}' removido com sucesso.")
                return
        print(f"Arquivo '{nome}' não encontrado.")

    def listar_arquivos(self):
        arquivos = []
        for lista in self.tabela:
            arquivos.extend(lista)
        return arquivos

#testes
tabela = TabelaHash()

tabela.adicionar(Arquivo("relatorio.pdf", "/documentos/relatorio.pdf", 1024))
tabela.adicionar(Arquivo("foto.jpg", "/imagens/foto.jpg", 2048))
tabela.adicionar(Arquivo("dados.csv", "/planilhas/dados.csv", 512))
tabela.adicionar(Arquivo("backup.zip", "/backup/backup.zip", 4096))

darq = tabela.buscar("dados.csv")
if darq:
    print(f"Arquivo encontrado: {darq}")
else:
    print("Arquivo 'dados.csv' não encontrado.")

tabela.remover("foto.jpg")

print("Arquivos armazenados:")
for arquivo in tabela.listar_arquivos():
    print(arquivo)
