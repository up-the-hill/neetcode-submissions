class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = Counter(text)
        
        chars = ['b', 'a', 'l', 'o', 'n']
        res = 99999999
        for c in chars:
            if c == 'l' or c == 'o':
                res = min(dic[c] // 2, res)
            else:
                res = min(dic[c], res)
        return res
