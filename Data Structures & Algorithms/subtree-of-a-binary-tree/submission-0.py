# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(a,b):

            if (not a and not b):
                return True

            if (not a or not b): 
                return False
            if (a.val != b.val):
                return False
            
            return (
                check(a.left, b.left) and check(a.right, b.right)
            )

        def traverse(node):
            if not node:
                return False
            if check(node, subRoot):
                return True
            return(
                traverse(node.left) or traverse(node.right)
            )
        
        return traverse(root)
            

            