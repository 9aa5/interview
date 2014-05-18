# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Review:
# After picking the next node for insertion, make sure it compares the tail node of the current
# sorted list, if it larger, then no insertion is needed. Move to the next item.
# Otherwise, if it always blindly go thru insertion, OJ will give you exceed time limit.
# This optimization seems important
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return None
        curNode = head.next
        curTail = head
        curTail.next = None

        while curNode:
            if curNode.val >= curTail.val:
                temp = curNode
                curNode = curNode.next
                curTail.next = temp
                curTail = temp
                curTail.next = None
            else:
                # curTail won't change
                nextCurNode = curNode.next
                # insert the curNode to the right position
                if curNode.val <= head.val:
                    curNode.next = head
                    head = curNode
                else:
                    prev = head
                    curInsertion = head.next
                    # Will definitely find a postion before reaching None
                    while curInsertion.val < curNode.val:
                        prev = curInsertion
                        curInsertion = curInsertion.next
                    curNode.next = curInsertion
                    prev.next = curNode
                curNode = nextCurNode
        return head

    def printList(self, head):
        while head:
            print head.val
            head = head.next

        
if __name__ == '__main__':
    node1 = ListNode(3)
    node2 = ListNode(1)
    node3 = ListNode(5)
    node4 = ListNode(2)
    node5 = ListNode(7)
    node6 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    solution = Solution()
    solution.printList(node1)
    node1 = solution.insertionSortList(node1)
    solution.printList(node1)

