class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def charCode(c):
            return ord(c) - ord("a")
        d = defaultdict(list)
        for s in strs:
            ht = [0] * 26
            for c in s:
                ht[charCode(c)] += 1
            d[tuple(ht)].append(s)
        return list(d.values())

