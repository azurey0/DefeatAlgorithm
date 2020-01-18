# Uses python3
import sys
from collections import deque

def optimal_sequence(n):
    # Perform a BFS
    successor = {} # map number to next number in shortest path
    queue = deque() # queue with number pairs (curr, next)
    queue.append((n,None)) # start at n
    while True:
        curr, succ = queue.popleft()
        if not curr in successor:
            successor[curr] = succ
            if curr == 1:
                break
            if curr%3 == 0: queue.append((curr//3, curr))
            if curr%2 == 0: queue.append((curr//2, curr))
            queue.append((curr-1, curr))
    # Create list from successor chain
    result = []
    i = 1
    while i:
        result.append(i)
        i = successor[i]
    return result



input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
