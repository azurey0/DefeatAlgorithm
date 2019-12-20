# Uses python3
import sys
import math

def get_majority_element(a, left, right):
    # （Sort）先对数组进行排序，因为多数元素一定存在，且个数超过总个数的一半，那么排序后最中间的那个元素一定是多数元素。
    a.sort()
    return a[int(len(a)/2)] if a.count(a[int(len(a)/2)]) > len(a)/2 else -1

def get_majority_element_1(a, left, right):
    # 用一个set记录所有出现过的元素及其个数
    # time exceeds requirement, set?
    nums_set = set(a)
    # print(nums_set)
    for i in nums_set:
        if (a.count(i) > (len(a)/2)) :
            return i
    return -1

def get_majority_element_2(a, left, right):
    #divide and conquer
    #（Divide and Conquer）分治法。每次将数组分成左右两半，在两半中分别找出现次数最多的元素，若找到的两个元素相同则此元素即为所求，
    # 否则在整个数组中分别计算这两个元素出现的次数，取较大的那个。
    if (left == right):
        return a[left]
    mid = math.floor((left+right)/2)
    major_l = get_majority_element_2(a, left, mid)
    major_r = get_majority_element_2(a, mid+1, right)
    if (major_l == major_r):
        return major_l
    if (major_l != major_r) and (a[left: right+1].count(major_l) > (len(a)/2)):
        return major_l
    if (major_l != major_r) and (a[left: right+1].count(major_r) > (len(a)/2)):
        return major_r
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element_2(a, 0, n-1) != -1: # the length of a is 1 + index of a
        print(1)
    else:
        print(0)
    # if get_majority_element(a, 0, n) != -1:
    #     print(1)
    # else:
    #     print(0)
