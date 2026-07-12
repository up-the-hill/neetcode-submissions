class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        buckets = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                buckets[word[:i] + "*" + word[i+1:]].append(word)

        seen = set(beginWord)
        q = deque([beginWord])
        distance = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return distance
                for i in range(len(word)):
                    for nei in buckets[word[:i] + "*" + word[i+1:]]:
                        if nei in seen:
                            continue
                        q.append(nei)
                        seen.add(nei)

            distance += 1
        return 0