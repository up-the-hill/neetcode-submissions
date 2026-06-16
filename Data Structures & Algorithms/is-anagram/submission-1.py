class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_val(char: str):
            return ord(char) - ord("a")
        hashtable_s = [0] * 26
        hashtable_t = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hashtable_s[get_val(s[i])] += 1
            hashtable_t[get_val(t[i])] += 1
        
        return hashtable_s == hashtable_t

