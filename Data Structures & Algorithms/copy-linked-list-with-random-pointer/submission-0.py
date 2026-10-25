"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        known = dict()
        cur = head
        while cur:
            known[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copy = known[cur]

            if cur.next:
                copy.next = known.get(cur.next)
            if cur.random:
                copy.random = known.get(cur.random)
            
            cur = cur.next
        
        return known.get(head)