class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def __repr__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Preço: {self.preco}"

class NoBST:
    def __init__(self, produto):
        self.produto = produto
        self.esquerda = None
        self.direita = None

class BSTProdutos:
    def __init__(self):
        self.raiz = None

    def inserir(self, produto):
        if self.raiz is None:
            self.raiz = NoBST(produto)
        else:
            self._inserir(self.raiz, produto)

    def _inserir(self, no, produto):
        if produto.id < no.produto.id:
            if no.esquerda is None:
                no.esquerda = NoBST(produto)
            else:
                self._inserir(no.esquerda, produto)
        elif produto.id > no.produto.id:
            if no.direita is None:
                no.direita = NoBST(produto)
            else:
                self._inserir(no.direita, produto)
        else:
            print("Produto com ID já existente.")

    def buscar(self, id):
        return self._buscar(self.raiz, id)

    def _buscar(self, no, id):
        if no is None:
            return None
        if id == no.produto.id:
            return no.produto
        elif id < no.produto.id:
            return self._buscar(no.esquerda, id)
        else:
            return self._buscar(no.direita, id)

    def remover(self, id):
        self.raiz = self._remover(self.raiz, id)

    def _remover(self, no, id):
        if no is None:
            return no
        if id < no.produto.id:
            no.esquerda = self._remover(no.esquerda, id)
        elif id > no.produto.id:
            no.direita = self._remover(no.direita, id)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            temp = self._minimo(no.direita)
            no.produto = temp.produto
            no.direita = self._remover(no.direita, temp.produto.id)
        return no

    def _minimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

    def listar_ordem(self):
        produtos = []
        self._in_order_traversal(self.raiz, produtos)
        return produtos

    def _in_order_traversal(self, no, produtos):
        if no is not None:
            self._in_order_traversal(no.esquerda, produtos)
            produtos.append(no.produto)
            self._in_order_traversal(no.direita, produtos)

# testes
bst_produtos = BSTProdutos()
bst_produtos.inserir(Produto(30, "Produto A", "Descrição A", 100.0))
bst_produtos.inserir(Produto(20, "Produto B", "Descrição B", 50.0))
bst_produtos.inserir(Produto(40, "Produto C", "Descrição C", 150.0))

produto = bst_produtos.buscar(20)
print("Produto encontrado:", produto)

bst_produtos.remover(20)
print("Produto removido. Nova listagem:")

produtos_ordenados = bst_produtos.listar_ordem()
print("Produtos em ordem crescente de ID:")
for produto in produtos_ordenados:
    print(produto)
