class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if cur.children[ord(c) - ord('a')] == None:
                cur.children[ord(c) - ord('a')] = TrieNode()
            cur = cur.children[ord(c) - ord('a')]
        
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if cur.children[ord(c) - ord('a')] == None:
                return False
            cur = cur.children[ord(c) - ord('a')]

        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if cur.children[ord(c) - ord('a')] == None:
                return False
            cur = cur.children[ord(c) - ord('a')]
            
        return True