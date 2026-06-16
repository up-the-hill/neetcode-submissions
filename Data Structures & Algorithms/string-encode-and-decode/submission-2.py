class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        a = 0
        while a < len(s):
            b = a
            while s[b] != "#":
                b += 1
            l = int(s[a:b])
            a = b + 1
            word = s[a:a+l]
            res.append(word)
            a = a + l
                
        return res

            
