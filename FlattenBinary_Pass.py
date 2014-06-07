# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.flatternInt(root)
        

    def flatternInt(self, root):
        if not root:
            return None, None
        leftFlattened, leftLast = self.flatternInt(root.left)
        rightFlattened, rightLast  = self.flatternInt(root.right)
        root.left = None
        root.right = None
        if leftFlattened:
            root.right = leftFlattened
        else:
            leftLast = root
        if rightFlattened:
            leftLast.right = rightFlattened
        if rightLast:
            last = rightLast
        elif leftLast:
            last = leftLast
        else:
            last = root
        return root, last
