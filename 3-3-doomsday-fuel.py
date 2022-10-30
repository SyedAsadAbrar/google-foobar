from fractions import Fraction
import numpy as np
from math import gcd


def lcm(arr):
    n = len(arr)

    result = 1

    for num in arr:
        result = result * num // gcd(result, num)

    return result


def solution(m):
    # Your code here
    matrix = [[(Fraction(num, sum(arr)) if (sum(
        arr) != 0 and num != 0) else num) for num in arr] for arr in m]

    count = 0

    for index in range(len(matrix)):
        arr = matrix[index]
        arrSum = sum(arr)
        if arrSum == 0:
            if index == 0:
                result = [1] + [num for num in arr[1:]]
                result.append(1)
                return result
            count += 1

    q = []
    r = []
    i = []

    n = []

    # make q and r matrix
    for outerIndex in range(0, len(matrix) - count):
        q.append([])
        r.append([])
        arr = matrix[outerIndex]
        for innerIndex in range(0, len(matrix) - count):
            q[outerIndex].append(arr[innerIndex])
        for innerIndex in range(len(matrix) - count, len(matrix)):
            r[outerIndex].append(arr[innerIndex])

    q = np.matrix(q, dtype=float)

    i = np.identity(len(q))

    n = (i - q)

    n = np.linalg.inv(n)

    result = np.dot(n, r)

    result = [[Fraction(decimal).limit_denominator() for decimal in arr]
              for arr in np.asarray(result)]

    denominator = lcm(
        [fraction.denominator for fraction in result[0]])

    print(denominator)
    print("result", result[0])

    numerators = [int(fraction.numerator *
                  (denominator / fraction.denominator)) for fraction in result[0]]

    return numerators + [denominator]


testCase = [[0, 0, 0, 0, 0]]

arr = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [
    0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

arr2 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

print(solution(arr))
