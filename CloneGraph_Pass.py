# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.cloneSet = {}
        self.printSet = {}

    def cloneGraph(self, node):
        if not node:
            return None
        cloneNode = UndirectedGraphNode(node.label)
        self.cloneSet[node.label] = cloneNode
        for neighbor in node.neighbors:
            if not neighbor.label in self.cloneSet:
                neighborClone = self.cloneGraph(neighbor)
            else:
                neighborClone = self.cloneSet[neighbor.label]
            cloneNode.neighbors.append(neighborClone)
        return cloneNode

    def printGraph(self, node):
        neighborList = [n.label for n in node.neighbors]
        print node.label, ":", neighborList
        
        self.printSet[node.label] = node
        for neighbor in node.neighbors:
            if not neighbor.label in self.printSet:
                self.printGraph(neighbor)

if __name__ == '__main__':
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)
    node3 = UndirectedGraphNode(3)
    node4 = UndirectedGraphNode(4)

    node1.neighbors = [node2, node3, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node1, node2, node4]
    node4.neighbors = [node1, node3]

    solution = Solution()
    cloneGraph = solution.cloneGraph(node3)
    solution.printGraph(cloneGraph)    
