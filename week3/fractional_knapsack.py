#python 3
import sys
import numpy as np

def get_optimal_value(capacity, weights, values):
    # outputValue = 0
    # for i in range(len(values)):
    #     if capacity == 0:
    #         return outputValue
    #
    #     valuesPerUnit = []
    #     for value, weight in zip(values, weights):
    #         # print('value:',value,'weight:',weight)
    #         if weight > 0:
    #             valuesPerUnit.append(value/weight)
    #             # print(valuesPerUnit)
    #         else:
    #             weightIndex = weights.index(weight)
    #             weights.pop(weightIndex)
    #             values.pop(weightIndex)
    #         # print('end for loop')
    #     maxValuePerUnit = max(valuesPerUnit)
    #     maxIndex = valuesPerUnit.index(maxValuePerUnit)
    #     addAmount = min(weights[maxIndex], capacity)
    #     # print('maxValuePerUnit: ', maxValuePerUnit, 'maxIndex: ', maxIndex, 'addAmount: ', addAmount, 'value: ', outputValue, 'addAmount * maxValuePerUnit: ',addAmount * maxValuePerUnit)
    #     outputValue = outputValue + (addAmount * maxValuePerUnit)
    #     # print('value: ', outputValue)
    #     capacity = capacity - addAmount
    #     weights[maxIndex] = weights[maxIndex] - addAmount
    #     # print(capacity, weights, outputValue)
    value = 0.
    indices = np.argsort([-v / w for w, v in zip(weights, values)])
   #print(indices)
    for idx in indices:
        if capacity <= 0:
            break
        weight = min(capacity, weights[idx])
        capacity -= weight
        value += weight * (values[idx] / weights[idx])
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
