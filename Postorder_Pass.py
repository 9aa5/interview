# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if not root:
            return []
        flatList = []
        stack = []
        stack.append(root)
        root.flag = 0
        while stack:
            topNode = stack[-1]
            if topNode.flag == 0: # Process left child
                topNode.flag = 1
                if topNode.left:
                    stack.append(topNode.left)
                    topNode.left.flag = 0
            elif topNode.flag == 1: # Process right child
                topNode.flag = 2
                if topNode.right:
                    stack.append(topNode.right)
                    topNode.right.flag = 0
            elif topNode.flag == 2:
                flatList.append(topNode.val)
                stack.pop()
        return flatList

if __name__ == '__main__':
    node7 = TreeNode(7)
    node3 = TreeNode(3)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node6 = TreeNode(6)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node7.left = node3
    node7.right = node6
    node3.left = node1
    node3.right = node2
    node6.left = node4
    node6.right = node5
    solution = Solution()
    print solution.postorderTraversal(node7)
 
