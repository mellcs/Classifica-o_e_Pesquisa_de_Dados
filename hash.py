#vetores simples
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = {i: [] for i in range(size)}

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None 

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False 

#listas encadeadas
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableWithLinkedLists:
    def __init__(self, size):
        self.size = size
        self.table = {i: None for i in range(size)}

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  

    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False 




#teste com vetores simples
htable = HashTable(10)
htable.insert(1, 100)
htable.insert(2, 200)
htable.insert(3, 300)
print("Busca chave 1 (Vetores Simples):", htable.search(1)) 
htable.delete(1)
print("Busca chave 1 após deleção (Vetores Simples):", htable.search(1)) 

#teste com listas encadeadas
htable_ll = HashTableWithLinkedLists(10)
htable_ll.insert(4, 400)
htable_ll.insert(5, 500)
htable_ll.insert(6, 600)
print("Busca chave 4 (Listas Encadeadas):", htable_ll.search(4))  
htable_ll.delete(4)
print("Busca chave 4 após deleção (Listas Encadeadas):", htable_ll.search(4)) 
