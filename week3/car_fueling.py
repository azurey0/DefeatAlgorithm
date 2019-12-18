# python3
import sys


def compute_min_refills(distance, tank, stops):
    stops.insert(0,0)
    stops.append(distance)
    numRefills = 0
    lastRefill = 0
    currentRefill = 0
    while (currentRefill <= (len(stops)-2)):
        lastRefill = currentRefill
        while ((currentRefill <= (len(stops)-2)) and (stops[currentRefill + 1] - stops[lastRefill] <= tank)):
            currentRefill += 1
        if (currentRefill == lastRefill):
            return -1
        if (currentRefill <= (len(stops)-2)):
            numRefills += 1
    #print(distance,tank, stops)
    return numRefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    # d = 10
    # m = 3
    # stops =[1, 2, 5, 9]
    print(compute_min_refills(d, m, stops))
