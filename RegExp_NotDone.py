
def parsePattern(pattern):
    parts = []
    cur = 0
    i = 0
    patternLen = len(pattern)
    while i < patternLen:
        if pattern[i] == '.':
            if pattern[i + 1] == '*':
                parts.append('.*')
                i = i + 2
                continue
            else:
                parts.append('.')
                i += 1
                continue
        else:
            cur = i
            while i < patternLen:
                if pattern[i] != '.' and pattern[i] != '*':
                    i += 1
                    continue
                else:
                    break
            if pattern[i] == '.':
                parts.append(pattern[cur:i])
                # Let the next loop to take care of '.'
                continue
            else:
                if i - 1 > cur:
                    parts.append(pattern[cur:i-1])
                rep = pattern[i - 1]
                parts.append(rep + '*')
                i += 1
                continue  
    return parts
                
def getAllMatches(inputStr, part):
    allMatches = []
    if part == '.': # .
        allMatches.append(inputStr[0:1])
    elif part == '.*': # .*
        for j in range(0, len(inputStr)):
            allMatches.append(inputStr[0:j])
    elif len(part) >= 2 and part[1] == '*': # L*
        for j in range(0, len(inputStr) + 1):
            expanded = part[0] * j
            if inputStr.startswith(expanded):
                allMatches.append(inputStr[0:j])
    else:
        if inputStr.startswith(part):
            allMatches.append(part)

    return allMatches
            
def isMatchInt(inputStr, parts):
    print 'Input String in this itor:%s' % inputStr
    print 'Parts in this itor: %s' % parts
    if not inputStr and not parts:
        return True
    elif (inputStr and not parts) or (not inputStr and parts):
        print 'Either string or pattern is empty, return false'
        return False
    part = parts[0]
    matchResultList = getAllMatches(inputStr, part)
    if not matchResultList:
        print 'No matchlist'
        return False
    else:
        print 'matchlist found. %s ' % str(matchResultList)
        for match in matchResultList:
            remain = inputStr[len(match):]
            if isMatchInt(remain, parts[1:]):
                print "Remaining match, return True."
                return True
        print "Remaining doesn't match, return false"
        return False

def isMatch(inputStr, pattern):
    parts = parsePattern(pattern)
    return isMatchInt(inputStr, parts)

if __name__ == '__main__':
    pattern = 'abc*de..ef.*ghk*'
    inputStr = 'abcccdeppefpghkk'
    # pattern = 'k*'
    # inputStr = 'kk'
    print 'Pattern: %s' % pattern
    print 'String: %s' % inputStr
    parts = parsePattern(pattern)
    print 'Break down:'
    for part in parts:
        print part
    print '============================'
    print inputStr
    if isMatch(inputStr, pattern):
        print 'Final Result: Match'
    else:
        print 'Final Result: Not Match'

