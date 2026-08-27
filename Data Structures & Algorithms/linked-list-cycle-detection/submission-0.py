# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        trav = head
        while fast and fast.next:
            
            trav = trav.next
            fast = fast.next.next
            if trav == fast:
                return True
        return False
