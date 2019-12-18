# Uses python3
import sys


def optimal_summands(n):
    summands = []
    i = 1
    while (((n-i) not in summands) and ((n-i)>1)):
        summands.append(i)
        n = n - i
        i = i + 1
    if n not in summands:
        summands.append(n)
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
    # for i in range(100):
    #     summands = optimal_summands(i)
    #
    #     print(i, summands)