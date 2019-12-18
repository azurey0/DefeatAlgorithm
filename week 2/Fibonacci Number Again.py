# python 3

def fib(a, b):

    f =[0,1]
    yushu=[0,1]
    i = 1
    #print(yushu)
    while((i<2) | ((yushu[i-1]==0) & (yushu[i]!=1)) | ((yushu[i-1]!=0) & (yushu[i]==1)) | ((yushu[i-1]!=0) & (yushu[i]!=1))):
        i = i + 1
        f.append(f[i-1]+f[i-2])
        yushu.append(f[i] % b)
        #(yushu[i - 1] != 0 & yushu[i] != 1)
    del yushu[i]
    del yushu[i-1]
    loop = len(yushu)
    #print(i, yushu,loop )
    noYushu = a % loop
    return yushu[noYushu]

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(fib(a,b))