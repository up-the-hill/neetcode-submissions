class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ht_s = [0] * 26
        ht_t = [0] * 26
        for i in range(len(s)):
            ht_s[ord(s[i]) - ord("a")] += 1
            ht_t[ord(t[i]) - ord("a")] += 1

        return ht_s == ht_t
        