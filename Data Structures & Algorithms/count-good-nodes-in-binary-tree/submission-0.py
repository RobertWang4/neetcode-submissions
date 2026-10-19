# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        def dfs(node,g_val):
            nonlocal count
            if node.val >= g_val:
                count += 1
            if node.left:
                dfs(node.left, max(node.val,g_val))
            if node.right:
                dfs(node.right, max(node.val,g_val))
        
        dfs(root,root.val)
        return count