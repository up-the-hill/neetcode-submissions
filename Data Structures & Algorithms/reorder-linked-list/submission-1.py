# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        first = head
        second = slow.next
        slow.next = None

        # reverse 2nd half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        second_rev = prev

        # merge 2 lists
        while second_rev:
            temp1 = first.next
            temp2 = second_rev.next
            first.next = second_rev
            second_rev.next = temp1
            first = temp1
            second_rev = temp2
        




        