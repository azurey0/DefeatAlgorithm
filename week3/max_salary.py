# Uses python3
import random
import sys

# 63 633?
def largest_number(a):

    res = ""
    while (len(a)>0):
        a.sort(reverse=True)
        maxDigit = -1
        for digit in a:
            # print(digit,a)
            if ((cmp(digit, maxDigit)) == 1):
                maxDigit = digit
        # print('maxDigit', maxDigit)
        res = res + str(maxDigit)
        # print('res',res)
        a.pop(a.index(maxDigit))
                # print('a',a)
    return res

def naive_largest_number(b):
    first = str(b[0])
    second = str(b[1])
    return max(int(first+second), int(second+first))

#1. 比较首位，首位大的大。
# 2. 当首位一样时，比较下一位，下一位大的大。如果其中一个数只有一位了，那就比较这一位。
#  IsGreaterOrEqual(2, 21) should return True ,(3, 21) True, (254, 231)
def is_greater_or_equal(digit, maxDigit):
    digit = str(digit)
    maxDigit = str(maxDigit)
    # l = min(len(digit),len(maxDigit))
    if len(digit) <= len(maxDigit):
        short = digit
        long = maxDigit
        l = len(digit)
    else:
        short = maxDigit
        long = digit
        l = len(maxDigit)

    for i in range(l):
        if (digit[i]) > (maxDigit[i]):
            # print((digit[i]),(maxDigit[i]))
            return True
        if (digit[i]) < (maxDigit[i]):
            return False
        if( (len(digit)!= len(maxDigit)) and(i+1 == l) and (digit[i] == maxDigit[i]) ):
            if (short[i] <= long[i+1]):
                return False
            else:
                return True
    return True #两数相等


def cmp(a, b):
    str_a = str(a)
    str_b = str(b)

    len_a = len(str_a)
    len_b = len(str_b)
    cmp_len = min(len_a, len_b)

    for i in range(cmp_len):
        if str_a[i] < str_b[i]:
            return -1
        elif str_a[i] > str_b[i]:
            return 1
        else:
            continue
    # 如果前几项全部相等，那么当长度相等时
    if len_a == len_b:
        return 0
    # 当a更长时,比较a的前半段和后半段哪个更大
    if len_a > len_b:
        pre_half = int(str_a[:cmp_len])
        post_half = int(str_a[cmp_len:])
        new_cmp = cmp(pre_half, post_half)
        # 当new_cmp = 1，a的前半段大于a的后半段，也就是b大于a的后半段，应该放在后面，所以要return -new_cmp
        # 例如a = 34422,b = 344时，34422344 < 34434422 此时应该是ba组合大
        # 同理推得其他结论
        return -new_cmp
    if len_a < len_b:
        pre_half = int(str_b[:cmp_len])
        post_half = int(str_b[cmp_len:])
        new_cmp = cmp(pre_half, post_half)
        # 当new_cmp = 1，b的前半段大于b的后半段，也就是a大于b的后半段，应该放在前面，所以要return new_cmp
        # 例如a = 344,b = 34422时，34434422 > 33422334
        # 同理推得其他结论
        return new_cmp

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    # print(cmp(633,63))
    # for i in range(1000):
    #     a = random.randint(1,1000)
    #     b = random.randint(1,1000)
    #     lst =[a, b]
    #     # print(lst)
    #     if((naive_largest_number(lst) - int(largest_number(lst))) != 0):
    #         print(lst, naive_largest_number(lst),largest_number(lst))
    #     else:
    #         print('yes')

