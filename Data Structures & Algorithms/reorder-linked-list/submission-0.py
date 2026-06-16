# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find halfway point
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # split at half
        half1 = head
        half2 = slow.next
        slow.next = None
        # reverse second half
        curr = half2
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        half2 = prev
        # zipper merge the two lists
        while half2:
            tmp1, tmp2 = half1.next, half2.next
            half1.next = half2
            half2.next = tmp1
            half1, half2 = tmp1, tmp2
        return

        