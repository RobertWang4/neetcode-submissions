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
        nodemap = {None : None}
        old = head

        while old:
            nodemap[old] = Node(old.val)
            old = old.next
        
        cur = head
        while cur:
            new = nodemap[cur]
            new.next = nodemap[cur.next]
            new.random = nodemap[cur.random]
            cur = cur.next
        
        return nodemap[head]