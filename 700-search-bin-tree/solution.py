# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BST
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def bst(node: TreeNode):
            if not node:
                return

            if node.val == val:
                return node
            
            if val > node.val:
                return bst(node.right)
            elif val < node.val:
                return bst(node.left)


        return bst(root)