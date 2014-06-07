class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        redLen = 0
        whiteLen = 0
        blueLen = 0

        scanCur = 0

        while scanCur < len(A) - blueLen:
            curColor = A[scanCur]
            if curColor == 0:
                if A[redLen] == 0:
                    redLen += 1
                else:
                    A[redLen] = 0
                    A[scanCur] = 1
                    redLen += 1
                scanCur += 1
            elif curColor == 1:
                whiteLen += 1
                scanCur += 1
            elif curColor == 2:
                A[scanCur] = A[len(A) - 1 - blueLen]
                A[len(A) - 1 - blueLen] = 2
                blueLen += 1

if __name__ == '__main__':
    A = [1, 2, 0]
    solution = Solution()
    print A
    solution.sortColors(A)
    print A
