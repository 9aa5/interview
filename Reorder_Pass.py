# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head:
            return
        right = self.splitList(head)
        right = self.reverseList(right)
        self.mergeLists(head, right)

    def splitList(self, head):
        p1 = head
        p2 = head
        prev = None
        while p2:
            prev = p1
            p1 = p1.next
            p2 = p2.next
            if p2:
                p2 = p2.next
        prev.next = None
        return p1
        
    def mergeLists(self, left, right):
        while right:
            insert = right
            right = right.next
            insert.next = left.next
            left.next = insert
            left = insert.next
            
    def reverseList(self, head):
        prev = None
        cur = head
        while True:
            if cur == None:
                return prev
            else:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
    def printList(self, head):
        while head:
            print '%d ' % head.val
            head = head.next

if __name__ == '__main__':
    node1 = ListNode(1)    
    node2 = ListNode(2)    
    node3 = ListNode(3)    
    node4 = ListNode(4)    
    node5 = ListNode(5)    
    node6 = ListNode(6)    
    node7 = ListNode(7)    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    solution = Solution()
    solution.printList(node1)
    solution.reorderList(node1)
    solution.printList(node1)
