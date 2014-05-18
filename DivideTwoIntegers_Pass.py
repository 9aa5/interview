class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign = False
        if (dividend < 0 and divisor > 0) or (dividend >= 0 and divisor < 0):
            sign = True
        dividend = abs(int(dividend))
        divisor = abs(int(divisor))
        sum = 0

        largestShift = 0
        while dividend >= (divisor << largestShift):
            largestShift += 1
        largestShift -= 1

        shiftCount = largestShift
        while dividend >= divisor:
            while dividend < (divisor << shiftCount):
                shiftCount -= 1
                if shiftCount == 0:
                    break

            sum += (1 << shiftCount)
            if shiftCount == 0:
                break
            dividend -= (divisor << shiftCount)
        if sign:
            return -sum
        else:
            return sum

if __name__ == '__main__':
    dividend = 238492 
    divisor = 17 
    print 'Result should be %d' % (dividend / divisor)
    solution = Solution()
    print 'Computed: %d' % solution.divide(dividend, divisor)
