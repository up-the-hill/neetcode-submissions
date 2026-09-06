# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reach half of linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        h1 = head
        curr = slow.next
        slow.next = None

        # reverse second half
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        h2 = prev

        # create new list, merging one by one:
        while h1 and h2:
            tmp1, tmp2 = h1.next, h2.next
            h1.next = h2
            h2.next = tmp1
            h1, h2 = tmp1, tmp2
        

