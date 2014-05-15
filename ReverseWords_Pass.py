class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        tokenList = s.split()
        reverseList = []
        while tokenList:
            a = tokenList.pop()
            reverseList.append(a)
        return ' '.join(reverseList)
        

if __name__ == '__main__':
    inputStr =  'the sky is blue'
    solution = Solution()
    outputStr = solution.reverseWords(inputStr)
    print inputStr
    print outputStr
