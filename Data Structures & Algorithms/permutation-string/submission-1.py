class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm1 = [0] * 26
        hm2 = [0] * 26
        for c in s1:
            hm1[ord('a') - ord(c)] += 1
        
        for i in range(len(s2)):
            l, r = i - len(s1), i
            hm2[ord('a') - ord(s2[r])] += 1
            if l >= 0:
                hm2[ord('a') - ord(s2[l])] -= 1
            if hm1 == hm2:
                return True
        
        return False

            

