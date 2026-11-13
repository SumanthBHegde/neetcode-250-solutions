# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head
        prev = temp
        pos = 1
        while pos < left:
            prev = prev.next
            pos += 1
        
        cur = prev.next
        cnt = 0
        while cnt < right - left:
            nxt = cur.next

            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

            cnt+=1
        
        return temp.next
