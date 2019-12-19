# Uses python3
import sys

def get_majority_element(a, left, right):
    # （Sort）先对数组进行排序，因为多数元素一定存在，且个数超过总个数的一半，那么排序后最中间的那个元素一定是多数元素。
    a.sort()
    return a[int(len(a)/2)] if a.count(a[int(len(a)/2)]) > len(a)/2 else -1

def get_majority_element_1(a, left, right):
    # 用一个set记录所有出现过的元素及其个数
    # time exceeds requirement
    nums_set = set(a)
    # print(nums_set)
    for i in nums_set:
        if (a.count(i) > (len(a)/2)) :
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
