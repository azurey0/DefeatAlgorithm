# python 3

def fib(n):
    f =[]
    sum = 0
    f.append(0)
    f.append(1)
    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])
    for i in range(n+1):
        #print(f[i])
        sum = sum + f[i]
    #print(f)
    return sum % 10, f[n]%10

if __name__ == '__main__':
    #n = int(input())
    #print(fib(n))
    for n in range(50):
        print('n: ',n,'sum: ',fib(n))