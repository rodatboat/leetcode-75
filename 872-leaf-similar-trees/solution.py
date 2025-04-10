from typing import Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        r1_leaves = self.get_leaves(root1)
        r2_leaves = self.get_leaves(root2)

        return r1_leaves == r2_leaves

    def get_leaves(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        leaf_nodes = []
        while queue:
            node = queue.pop()
            
            if not node.left and not node.right:
                leaf_nodes.append(node.val)
                
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return leaf_nodes
        