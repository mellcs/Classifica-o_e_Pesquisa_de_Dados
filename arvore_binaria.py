class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class ABB:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._min_value_node(node.right)
            node.key = min_larger_node.key
            node.right = self._delete(node.right, min_larger_node.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node is not None
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def pre_order(self):
        self._pre_order(self.root)
        print()

    def _pre_order(self, node):
        if node is not None:
            print(node.key, end=' ')
            self._pre_order(node.left)
            self._pre_order(node.right)

    def in_order(self):
        self._in_order(self.root)
        print()

    def _in_order(self, node):
        if node is not None:
            self._in_order(node.left)
            print(node.key, end=' ')
            self._in_order(node.right)

    def post_order(self):
        self._post_order(self.root)
        print()

    def _post_order(self, node):
        if node is not None:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node.key, end=' ')

# TESTES
if __name__ == "__main__":
    arvore = ABB()

    valores = [50, 30, 20, 40, 70, 60, 80]
    for valor in valores:
        arvore.insert(valor)

    print("Árvore após inserções iniciais (Ordem simétrica):")
    arvore.in_order()  

    print("\nÁrvore em diferentes ordens de percurso:")

    print("Pré-ordem:")
    arvore.pre_order()  

    print("Ordem simétrica:")
    arvore.in_order() 

    print("Pós-ordem:")
    arvore.post_order()  

    print("\nBuscas:")
    print(f"Busca por 40: {'Encontrado' if arvore.search(40) else 'Não encontrado'}") 
    print(f"Busca por 25: {'Encontrado' if arvore.search(25) else 'Não encontrado'}")  

    print("\nDeleção:")
    arvore.delete(20)
    print("Árvore após deletar 20 (Ordem simétrica):")
    arvore.in_order()  

    arvore.delete(30)
    print("Árvore após deletar 30 (Ordem simétrica):")
    arvore.in_order()  

    arvore.delete(50)
    print("Árvore após deletar 50 (Ordem simétrica):")
    arvore.in_order() 
