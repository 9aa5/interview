class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                result = self.evalTop(token, stack.pop(), stack.pop())
                stack.append(result)
            else:
                stack.append(int(token))

        return stack.pop()

    def evalTop(self, op, second, first):
        if op == '+':
            return first + second
        elif op == '-':
            return first - second
        elif op == '*':
            return first * second
        elif op == '/':
            # In python 2.x, -1/2 = -1
            # So, we need to make is float(-1) / 2 = -0.5, and int(-0.5) = 0
            return int(float(first) / second)
        

if __name__ == '__main__':
    solution = Solution()
    expression = ["2", "1", "+", "3", "*"]
    print expression
    print solution.evalRPN(expression)
    expression = ["4", "13", "5", "/", "+"]
    print expression
    print solution.evalRPN(expression)
    expression = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print expression
    print solution.evalRPN(expression)
