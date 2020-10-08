def maxProfitWithKTransactions(prices, k):
    # listofprofits = []
    # dictionary = {}
    # counter1 = 1
    # for i in prices:
    #     dictionary[counter1] = i
    #     counter1 += 1
    #
    # for i in range(len(prices)):
    #     for x in range(len(prices)):
    #
    #         profit = prices[x] - prices[i]
    #
    #         listofprofits.append(profit)
    #
    # listofprofits.sort()
    # print(listofprofits)

    profits = [[0 for i in prices] for x in range(k+1)]
    if k == 0:
        return 0

    for i in range(1, k + 1):
        previousnumber = 0
        for x in range(1, len(prices)):
            for d in range(x):

                profits[i][x] = max(previousnumber, prices[x] + ((profits[i-1][d]) - prices[d]))
                if profits[i][x] > previousnumber:
                    previousnumber = profits[i][x]


    maxs = 0
    for i in range(len(profits)):
        for y in profits[i]:
            if y > maxs:
                maxs = y

    return maxs

def main():

    prices = [5,11,3,50,60,90]
    k = 2
    maxProfitWithKTransactions(prices, k)
main()
