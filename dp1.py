import copy

def getCurSolution(coins, solutionList, curSum):
    minSolutionLen = curSum
    minSolutionRec = []
    filtered_coins = [coin for coin in coins if coin <= curSum]
    for coin in filtered_coins:
        valueAfterRemoveCoin = curSum - coin
        if valueAfterRemoveCoin == 0:
            curSolution = [coin]
            return curSolution
        else:
            preSolution = solutionList[valueAfterRemoveCoin]
            if not preSolution:
                continue
            curSolutionRec = copy.deepcopy(preSolution)
            curSolutionRec.append(coin)
        if minSolutionLen > len(curSolutionRec):
            minSolutionLen = len(curSolutionRec)
            minSolutionRec = curSolutionRec
    return minSolutionRec
        


def dpSolution(coins, coinSum):
    solutionList = []
    for curSum in range(0, coinSum + 1):
        coinList = getCurSolution(coins, solutionList, curSum)
        print coinList
        solutionList.append(coinList)

if __name__ == '__main__':
    import sys
    dpSolution([1,2,5], int(sys.argv[1]))
