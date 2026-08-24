# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trav = head
        rev = None
        while trav:
            temp = trav.next
            trav.next = rev
            rev = trav
            trav = temp

        return rev
        
