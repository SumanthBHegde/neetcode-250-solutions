# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True
        def traverse(node):
            nonlocal flag
            if not node:
                return 0
            
            left  = traverse(node.left)
            right = traverse(node.right)

            # if (not left and not right):
            #     print()
            # if (left == right +1 or left == right or left +1 == right):
            #     flag = True
            if abs(left - right) >1:
                flag = False

            hgt = max(left, right) + 1
            return hgt
        
        traverse(root)
        return flag

