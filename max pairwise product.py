#python3

product = 0
n = int(input())
a = [int(x) for x in input().split()]

biggest = max(a)
a.remove(biggest)
second_big = max(a)

print(biggest * second_big)