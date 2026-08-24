class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        leftans = self.maxDepth(root.left)
        rightans = self.maxDepth(root.right)
        return 1 + max(leftans, rightans)
