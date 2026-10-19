# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        q = deque()
        q.append(root)

        while q:
            level_size = len(q) - 1
            for i in range(len(q)):
                n = q.popleft()
                if n:
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                    if i == level_size:
                        res.append(n.val)
        
        return res

                
                

        