class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)
        for s in strs:
            char_count = {}
            for c in s:
                char_count[c] = 1 + char_count.get(c, 0)
            buckets[tuple(sorted(char_count.items()))].append(s)
        return list(buckets.values())