# python 3

def fib(n):
    f =[]
    sum = 0
    f.append(0)
    f.append(1)
    for i in range(2, n+1):
        f.append((f[i-1]+f[i-2]))
    for i in range(n+1):
        #print(i,f[i])
        sum = sum + f[i] **2
        #print('sum',sum)
    return sum % 10

if __name__ == '__main__':
    n = int(input())
    print(fib(n))