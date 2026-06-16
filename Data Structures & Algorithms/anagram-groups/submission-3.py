class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def charCode(c):
            return ord(c) - ord("a")
        d = defaultdict(list)
        for word in strs:
            ht = [0] * 26
            for char in word:
                ht[charCode(char)] += 1
            d[tuple(ht)].append(word)
        return list(d.values())