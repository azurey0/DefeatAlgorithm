# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    starts = []
    ends =[]
    points = []
    for s in segments:
        starts.append(s.start)
        ends.append(s.end)
    Z = zip(ends, starts)
    Z = sorted(Z)
    ends, starts = zip(*Z)
    # print(ends, starts)
    flag = [0 for i in range(len(starts))]
    for index in range(len(starts)):
        if (flag[index] ==0):
            flag[index] = 1
            # print(flag)
            end = ends[index]
            for i in range(len(starts)):
                # print('start: ',starts[i], 'end: ',ends[i])
                if ((starts[i] <= end) & (ends[i] >= end)):
                   flag[i] = 1
                   # print(flag)
            points.append(end)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
