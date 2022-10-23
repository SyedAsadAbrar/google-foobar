infinity = float('inf')


def printMatrix(arr):
    for i in arr:
        print(i)
    print("")


def findMin(position, matrix, isFirstIteration=False):
    minU = minL = minR = minD = infinity

    row, col = position

    cols = len(matrix)
    rows = len(matrix[0])

    if row - 1 >= 0:
        num = matrix[col][row - 1]
        minL = num if num != 'x' else infinity

    if col - 1 >= 0:
        num = matrix[col - 1][row]
        minU = num if num != 'x' else infinity

    if not isFirstIteration:
        if row + 1 < rows:
            num = matrix[col][row + 1]
            minR = num if num != 'x' else infinity

        if col + 1 < cols:
            num = matrix[col + 1][row]
            minD = num if num != 'x' else infinity

    return min(minU, minL, minR, minD)


def solution(map):
    # Your code here
    printMatrix(map)

    inverseMatrix = ([list[::-1] for list in map])[::-1]

    printMatrix(inverseMatrix)

    weightedInverseMatrix = []

    # first iteration
    for col in range(len(inverseMatrix)):
        list = inverseMatrix[col]
        weightedInverseMatrix.append([])
        for row in range(len(list)):
            if row == 0 and col == 0:
                weightedInverseMatrix[col].append(0)
                continue
            minVal = findMin((row, col), weightedInverseMatrix, True)
            isAWall = inverseMatrix[col][row] == 1
            weightedInverseMatrix[col].append(
                'x' if isAWall else minVal + 1)

    printMatrix(weightedInverseMatrix)

    # weightedInverseMatrix = [list[::-1] for list in weightedInverseMatrix]

    for col in range(len(inverseMatrix)):
        list = inverseMatrix[col]
        for row in reversed(range(len(list))):
            if row == 0 and col == 0:
                continue
            minVal = findMin((row, col), weightedInverseMatrix, False)
            isAWall = inverseMatrix[col][row] == 1
            weightedInverseMatrix[col][row] = 'x' if isAWall else minVal + 1

    printMatrix(weightedInverseMatrix)


arr2 = [[1, 2, 3, 4],
        [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

arr = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

solution(arr)
