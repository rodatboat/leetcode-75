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

        dq = deque([(root, root.val)])
        a = []
        while dq:
            node, max_val = dq.pop()

            if node.val >= max_val:
                a.append(node)
                
            new_max = max(max_val, node.val)

            if node.left:
                dq.append((node.left, new_max))
            if node.right:
                dq.append((node.right, new_max))


        return len(a)