# Notes:
# There is no cached used in this solution.  Potentially, we could use cache.
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        return self.restoreIpAddressesInt(s, 4)

    def restoreIpAddressesInt(self, s, NoOfParts):
        resultList = []
        if not s and NoOfParts == 0:
            return ['']
        elif not s and NoOfParts:
            return []
        elif s and NoOfParts == 0:
            return []

        if NoOfParts == 1:
            if int(s) <= 255 and not (s[0] == '0' and len(s) > 1):
                return [s]
            else:
                return []
        else:
            maxLen = 3
            if len(s) < maxLen:
                maxLen = len(s)

            for partLen in range(1, maxLen + 1):
                partStr = s[0:partLen]
                if int(partStr) <= 255:
                    result = self.restoreIpAddressesInt(s[partLen:], NoOfParts - 1)
                    if result:
                        resultList = resultList + self.prefixList(partStr, result)
                if int(partStr) == 0:
                    break;
            
        return resultList

    def prefixList(self, prefix, listOfAddress):
        newList = []
        for address in listOfAddress:
            if address =='':
                newList.append(prefix)
            else:
                newList.append(prefix + '.' + address)

        return newList
            
if __name__ == '__main__':
    inputStr = "25525511135"
    solution = Solution()
    print solution.restoreIpAddresses(inputStr)
