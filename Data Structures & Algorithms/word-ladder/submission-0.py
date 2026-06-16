class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
            
        # make adjacency list 
        adjList = collections.defaultdict(list)

        for w in wordList:
            for i in range(len(w)):
                key = w[:i] + '*' + w[i+1:len(w)]
                adjList[key].append(w)

        # traverse graph in BFS
        visited = set()
        q = deque()
        q.append(beginWord)
        distance = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return distance
                for i in range(len(w)):
                    key = w[:i] + '*' + w[i+1:len(w)]
                    for path in adjList[key]:
                        if path in visited:
                            continue
                        visited.add(path)
                        q.append(path)
            distance += 1
        
        return 0 




