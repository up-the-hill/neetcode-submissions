class Node:
    def __init__(self, key, val): 
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.mem = {}
        self.right = Node(None, None)
        self.left = Node(None, None)
        self.left.next = self.right
        self.right.prev = self.left
    
    def add(self, key, val):
        n = Node(key, val)
        self.mem[key] = n
        n.next = self.right
        n.prev = self.right.prev
        self.right.prev.next = n
        self.right.prev = n

        if len(self.mem) > self.cap:
            n = self.left.next
            n.prev.next, n.next.prev = n.next, n.prev
            self.mem.pop(n.key)

    
    def remove(self, key):
        n = self.mem[key]
        n.prev.next, n.next.prev = n.next, n.prev 
        self.mem.pop(key)

    def get(self, key: int) -> int:
        if key in self.mem:
            val = self.mem[key].val
            self.remove(key)
            self.add(key, val)
            return val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.mem:
            self.remove(key)
        self.add(key, value)
        
