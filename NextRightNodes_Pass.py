# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        nodeList = [root, None]
        while nodeList:
            item = nodeList.pop(0)
            if not item:
                if len(nodeList):
                    nodeList.append(None)
                    continue
                else:
                    break
            if len(nodeList):
                item.next = nodeList[0]
            else:
                item.next = None
            if item.left:
                nodeList.append(item.left)
            if item.right:
                nodeList.append(item.right)
