# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def __init__(self):
        self.numList = []

    def sumNumbers(self, root):
        if not root:
            return 0
        curNum = 0
        self.sumNumbersInt(root, curNum)
        total = 0
        for x in self.numList:
            total += x
        return total


    def sumNumbersInt(self, root, curNum):
        curNum = curNum * 10 + root.val
        if not root.left and not root.right:
            self.numList.append(curNum)
            return
        else:
            if root.left:
                self.sumNumbersInt(root.left, curNum)
            if root.right:
                self.sumNumbersInt(root.right, curNum)
            
        
if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    solution = Solution()
    print solution.sumNumbers(node1)
