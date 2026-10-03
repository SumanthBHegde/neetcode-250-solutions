# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        flag = True
        def traverse(node1, node2):
            nonlocal flag
            if not node1 and not node2:
                return

            if not node1 or not node2:
                flag = False
                return  
            
            if node1.val != node2.val:
                flag = False
                return
            
            traverse(node1.left, node2.left)
            traverse(node1.right, node2.right)
        
        traverse(p,q)

        return flag