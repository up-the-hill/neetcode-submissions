# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = start = ListNode()
        while True:
            lowest = (-1, float('inf'))
            for i, l in enumerate(lists):
                if l: 
                    if l.val < lowest[1]: lowest = (i, l.val)
            if lowest[0] == -1: break
            curr.next = lists[lowest[0]]
            curr = curr.next
            # if lists[lowest[0]].next:
            lists[lowest[0]] = lists[lowest[0]].next 
        curr.next = None
        return start.next

