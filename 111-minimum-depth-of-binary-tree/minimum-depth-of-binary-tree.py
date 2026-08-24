class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        leftans = self.minDepth(root.left)
        rightans = self.minDepth(root.right)
        if root.left == None:
            return rightans + 1
        elif root.right == None:
            return leftans + 1
        else:
            return 1 + min(leftans, rightans)