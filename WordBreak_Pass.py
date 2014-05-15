class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def __init__(self):
        self.cached = {}

    def wordBreak(self, s, words):
        if not s:
            return True
        for word in words:
            if s.startswith(word):
                newS = s[len(word):]
                if newS in self.cached:
                    result = self.cached[newS]
                else:
                    result = self.wordBreak(newS, words)
                    self.cached[newS] = result
                if result:
                    return result
        return False

if __name__ == '__main__':
    # s = 'bitsword'
    # words = ['bits', 'sword']

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    solution = Solution()
    print solution.wordBreak(s, words)
