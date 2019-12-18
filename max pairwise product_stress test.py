#python 3
# stress test
import time
import random
#start = time.process_time()
def maxPairwiseQuick(a):
    product = 0
    #n = int(input())
    #a = [int(x) for x in input().split()]

    biggest = max(a)
    a.remove(biggest)
    second_big = max(a)
    return (biggest * second_big)
    #print(biggest * second_big)

#end = time.process_time()
#print("code runs in :", end-start)
def maxPairwiseNaive(n, a):
    product = 0
    #n = int(input())
    #a = [int(x) for x in input().split()]

    for i in range(n):
        for j in range(i+1, n):
            product = max(product, a[i]*a[j])

    return (product)

def stressTest():
    testTime = 0
    while(True):
        print('Test time: ', testTime)
        testTime = testTime + 1
        n = random.randint(2, 11)
        #print('n: ',n)
        a = []
        for i in range(n):
            a.append(random.randint(0, 20000))
        #print(a)
        res1 = maxPairwiseNaive(n, a)
        res2 = maxPairwiseQuick(a)
        if (res1!=res2):
            print('n: ',n, 'a: ',a, 'res1: ', res1, 'res2: ', res2)
            break

stressTest()