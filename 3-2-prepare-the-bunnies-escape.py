def printMatrix(arr):
    for i in arr:
        print(i)


def solution(map):
    # Your code here
    printMatrix(map)

    print("")

    inverseMatrix = ([list[::-1] for list in map])[::-1]

    printMatrix(inverseMatrix)

    weightedInverseMatrix = []

    # first iteration
    for list in inverseMatrix:
        for num in list:


arr = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

solution(arr)
