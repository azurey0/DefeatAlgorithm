# python 3

def fib(a,n):
    f =[]
    sum = 0
    f.append(0)
    f.append(1)
    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])
    for i in range(a, n+1):
        #print(f[i])
        sum = sum + f[i]
    return sum % 10

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(fib(a, b))