class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        def isNumber(c):
            return ord("0") <= ord(c) and ord(c) <= ord("9")
        l, r = 0, 0
        while l < len(s):
            while isNumber(s[r]):
                r += 1
            # get number
            length = s[l:r]
            # skip the hash
            r += 1
            l = r
            # get the word
            r += int(length)
            res.append(s[l:r])
            l = r

        return res

        
            
