# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, node: TreeNode) -> int:
        while node.left:
            node = node.left
        return node.val


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return
            elif not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                minVal = self.findMin(root.right)
                root.val = minVal
                root.right = self.deleteNode(root.right, minVal)

        return root