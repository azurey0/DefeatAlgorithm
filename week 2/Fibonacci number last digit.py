#python 3
# 斐波那契数列的个位数：一个60步的循环
# 11235,83145,94370,77415,61785.38190,
# 99875,27965,16730,33695,49325,72910…
def fib(n):
    no = n % 60
    #print(no)
    f =[]
    lst =[1, 2, 3]
    f.append(0)
    f.append(1)
    for i in range(2, 60):
        f.append(f[i-1]+f[i-2])
    #print(len(lst))
    return f[no]%10

if __name__ == '__main__':
    n = int(input())
    print(fib(n))