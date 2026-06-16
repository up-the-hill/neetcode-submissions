class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            hashtable = [0] * 26
            for char in s:
                hashtable[ord(char) - ord("a")] += 1
            res[tuple(hashtable)].append(s)
        return res.values()