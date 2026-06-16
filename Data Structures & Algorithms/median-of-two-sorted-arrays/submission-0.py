class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1

        while True:
            m = l + (r - l) // 2 
            n = half - m - 2

            Aleft = A[m] if m >= 0 else float("-infinity")
            Aright = A[m + 1] if m+1 < len(A) else float("infinity")
            Bleft = B[n] if n >= 0 else float("-infinity")
            Bright = B[n + 1] if n+1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright: # division done
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
            elif Aleft > Bright:
                r = m - 1
            elif Bleft > Aright:
                l = m + 1
            