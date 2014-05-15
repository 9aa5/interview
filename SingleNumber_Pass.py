class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        num = int(0)
        for p in A:
            num ^= int(p)
        return num

if __name__ == '__main__':
    numList = [1,2,3,3,4,4,5,6,1,6,5]
    solution = Solution()
    print solution.singleNumber(numList)
