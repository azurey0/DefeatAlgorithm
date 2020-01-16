# Uses python3
import sys

def get_change(money):
    MinNumCoins = {0:0}
    coins = [1, 3, 4]

    for m in range(1, money + 1):
        j = 0
        MinNumCoins[m] = float("inf")
        for i in coins:
            if m >= coins[j]:
                NumCoins = MinNumCoins[m - coins[j]] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
            j += 1
    return MinNumCoins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
