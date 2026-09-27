# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxCnt = 0

        def traverse(node,cnt):
            nonlocal maxCnt
            
            if not node:
                return
            
            cnt += 1
            maxCnt = max(maxCnt, cnt)
            
            traverse(node.left, cnt)
            traverse(node.right, cnt)

        traverse(root, 0)
        return maxCnt