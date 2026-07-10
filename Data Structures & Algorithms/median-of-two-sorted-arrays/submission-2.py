class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft  = A[i]     if i >= 0         else float("-infinity")
            Aright = A[i + 1] if i < len(A) - 1 else float("infinity")
            Bleft  = B[j]     if j >= 0         else float("-infinity")
            Bright = B[j + 1] if j < len(B) - 1 else float("infinity")
            
            if Aleft > Bright:
                r = i - 1
                continue
            elif Bleft > Aright:
                l = i + 1
                continue
            
            # found middle!
            if total % 2:
                return min(Aright, Bright)
            else:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
