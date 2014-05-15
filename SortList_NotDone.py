tion for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        k = 1
        while self.doOnePass(k, head):
            k *= 2

    def forwardSteps(self, start, size):
        count = 0
        if size == 0:
            return start

        prev = start
        while start.next != None:
            prev = start
            start = start.next
            count += 1
            if count == size:
                break
        if count == size:
            return (start, prev)
        else:
            return (None, start)

    def getPair(self, start, size):
        firstList = start
        second, prev = self.forwardSteps(start, size)
        prev.next = None
        third, prev = self.forwardSteps(second, size)
        prev.next = None
        return (third, firstList, second)

    def doOnePass(self, size, head):
        start = head
        newHead = None
        while True:
            start, firstList, secondList = self.getPair(start, size)
            newHead = self.mergeInto(newHead, firstList, secondList)
            if start == None:
                break;


    def mergeInto(self, headNode, firstList, secondList):
        firstListStep = 0
        secondListStep = 0

        currentHead = headNode
        while True:
            if firstList == None:
                currentHead.next = secondList
            elif secondList == None:
                currentHead.next = firstList
            else:
                if firstList.val <= secondList.val:
                    pick = firstList
                    firstList = firstList.next
                else:
                    pick = secondList
                    secondList = secondList.next
                currentHead.next = pick
                currentHead = current.next
                currentHead.next = None


        while currentHead.next != None:
            currentHead = currentHead.next

        return currentHead
        
