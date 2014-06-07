class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        A = ''
        llen = max(len(a), len(b))
        overflow = 0
        for i in range(0, llen):
            if i < len(a):
                digitA = int(a[len(a) - i - 1])
            else:
                digitA = 0
            if i < len(b):
                digitB = int(b[len(b) - i - 1])
            else:
                digitB = 0
            result = digitA + digitB + overflow
            if result == 0:
                A = '0' + A
                overflow = 0
            elif result == 1:
                A = '1' + A
                overflow = 0
            elif result == 2:
                A = '0' + A
                overflow = 1
            else:
                A = '1' + A
                overflow = 1
        if overflow == 1:
            A = '1' + A
        return A

if __name__ == '__main__':
    solution = Solution()
    a = '11110'
    b = '10111'
    print a, b
    print solution.addBinary(a, b)
