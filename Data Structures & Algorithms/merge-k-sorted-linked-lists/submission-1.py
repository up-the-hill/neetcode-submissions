# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(list1, list2):
            dummy = curr = ListNode()
            while list1 and list2:
                if list1.val > list2.val:
                    curr.next = list2
                    list2 = list2.next
                else: 
                    curr.next = list1
                    list1 = list1.next
                curr = curr.next
                
            curr.next = list1 if list1 else list2
            
            return dummy.next
        
        def merge(li, l, r):
            if l == r:
                return li[l]
            
            mid = (l + r) // 2
            left = merge(li, l, mid)
            right = merge(li, mid + 1, r)

            return merge2Lists(left, right)

        if len(lists) == 0:
            return None
        return merge(lists, 0, len(lists) - 1)