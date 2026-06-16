class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        
        # ["hello", "world"] = 5#hello5#world

    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        res = []
        while r < len(s):
            if s[r] == "#":
                length = int(s[l:r])

                word = s[r + 1: r + 1 + length]

                l = r + length + 1
                r = l

                res.append(word)
            r += 1
        return res
