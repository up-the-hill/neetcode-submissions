# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        prev, curr = None, head
        while curr:
            if prev != None:
                a, b = prev.val, curr.val
                g = gcd(a, b)
                prev.next = ListNode(g, curr)
                prev = prev.next
            prev = curr
            curr = curr.next
        return head