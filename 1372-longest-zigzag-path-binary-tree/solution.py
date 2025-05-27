# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.zPath = 0

        def dfs(node: TreeNode, currPathLen: int, goRight: bool):
            if node is None:
                return

            self.zPath = max(self.zPath, currPathLen)

            if goRight:
                dfs(node.left, 1, True)
                dfs(node.right, currPathLen + 1, False)
            if not goRight:
                dfs(node.left, currPathLen + 1, True)
                dfs(node.right, 1, False)

        dfs(root, 0, True)

        return self.zPath
