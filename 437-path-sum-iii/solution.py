# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0
        self.pathSums = defaultdict(int) # initialize empty dict with value of 0 for any key
        self.pathSums[0] = 1

        def dfs(node: TreeNode, currSum: int):
            if node is None:
                return
            
            currSum += node.val

            self.paths += self.pathSums[currSum - targetSum]
            self.pathSums[currSum] += 1

            if node.right:
                dfs(node.right, currSum)
            if node.left:
                dfs(node.left, currSum)

            self.pathSums[currSum] -= 1
        
        dfs(root, 0)
        return self.paths