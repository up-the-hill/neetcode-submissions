class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 1
        for i, d in enumerate(digits):
            if d == 9:
                digits[i] = 0
            else:
                digits[i] = d + 1
                carry = 0
                break
        
        if carry == 1:
            digits.append(1)
            
        digits.reverse()

        return digits