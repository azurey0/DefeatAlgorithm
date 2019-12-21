# Uses python3
import sys
import random

def partition3(a, l, r):
   x, j, t = a[l], l, r
   i = j

   while i <= t :
      if a[i] < x:
         a[j], a[i] = a[i], a[j]
         j += 1

      elif a[i] > x:
         a[t], a[i] = a[i], a[t]
         t -= 1
         i -= 1 # remain in the same i in this case
      i += 1
   return j, t


def partition2(a, l, r):
    # print(a,'l',l,'r',r)
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
            # print(a, 'a[i]', a[i],'a[j]',a[j])
    a[l], a[j] = a[j], a[l]
    # print(a,'a[l]', a[l],'a[j]', a[j])
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    # a[l], a[k] = a[k], a[l]
    #use partition3
    # m = partition2(a, l, r)
    j, m = partition3(a, l, r)
    randomized_quick_sort(a, l, j - 1);
    randomized_quick_sort(a, m + 1, r);

def randomized_quick_sort_naive(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    # a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    # m = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
    # stress test
    # for j in range(100):
    #     lst = []
    #     lst_len = random.randint(1, 10)
    #     for i in range(lst_len):
    #         lst.append(random.randint(1, 10))
    #
    #     if (randomized_quick_sort_naive(lst,0,len(lst)-1) != randomized_quick_sort(lst, 0, len(lst)-1)):
    #         print(lst)





