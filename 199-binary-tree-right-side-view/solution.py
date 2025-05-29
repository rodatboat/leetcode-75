# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []

        while queue:
            right = None
            qLen = len(queue)

            # Get most right value in queue
            for i in range(qLen):
                node = queue.popleft()
                if node:
                    right = node
                    queue.append(node.left)
                    queue.append(node.right)

            if right:
                res.append(right.val)

        return res

        