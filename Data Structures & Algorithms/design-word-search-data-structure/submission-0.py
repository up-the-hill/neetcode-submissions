class TrieNode:
    def __init__(self, c):
        self.value = c
        self.children = [None] * 26
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode('*')

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = TrieNode(c)
            curr = curr.children[ord(c) - ord('a')]
        
        curr.end = True
        

    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root

            for j in range(i, len(word)):

                if word[j] == '.':
                    for child in curr.children:
                        if child is not None:
                            if dfs(j+1, child): return True
                    return False
                else:
                    if curr.children[ord(word[j]) - ord('a')] == None:
                        return False
                    curr = curr.children[ord(word[j]) - ord('a')]
            
            return curr.end

        return dfs(0, self.root)