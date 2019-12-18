# python 3

def moneyChange(m):
    coins = [1, 5, 10]
    i = 0
    # while m > 0:
    #     while m >= 10:
    #         i = i + 1
    #         m = m - 10
    #     while m >= 5:
    #         i = i + 1
    #         m = m - 5
    #     while m >=1:
    #         i = i + 1
    #         m = m -1
    while (m > 0) & (len(coins)>0):
        biggestCoin = coins[-1]
        #print(biggestCoin)
        if (m >= biggestCoin):
            m = m - biggestCoin
            i = i + 1
            #print('m: ',m, 'i: ', i)
        else:
            coins.pop()
            #print(coins)
    return i

if __name__ == '__main__':
    m = int(input())
    print(moneyChange(m))