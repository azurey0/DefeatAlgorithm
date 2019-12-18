# Uses python3
import sys
import math
import random

def binary_search(a, x):
    left, right = 0, len(a)-1
    while (left <= right):
        mid = math.floor((left + right)/2)
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
    # pressure test
    # lst = []
    # for i in range(100):
    #     n = random.randint(0,30000)
    #     for j in range(n):
    #         num = random.randint(1, 1000000000)
    #         lst.append(num)
    #     x = random.randint(1, 1000000000)
    #     if (binary_search(lst, x) != linear_search(lst, x)):
    #         print(lst, x)

