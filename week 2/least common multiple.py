#python 3
def leastCommonMultiple(a,b):
    aMultipleb = a*b
    while b!= 0:
        t = b
        b = a % b
        a = t
    leaseCommonMultiple = aMultipleb / a
    return int(leaseCommonMultiple)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(leastCommonMultiple(a, b))