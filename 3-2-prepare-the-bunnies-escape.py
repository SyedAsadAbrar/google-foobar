infinity = float('inf')


def printMatrix(arr):
    for i in arr:
        print(i)
    print("")


def findNavigableNeighbours(position, matrix):
    cols = len(matrix)
    rows = len(matrix[0])

    col, row = position

    navigableNeighbours = []

    if col - 1 >= 0 and matrix[col - 1][row] != 1:
        navigableNeighbours.append((col - 1, row))

    if row - 1 >= 0 and matrix[col][row - 1] != 1:
        navigableNeighbours.append((col, row - 1))

    if col + 1 < cols and matrix[col + 1][row] != 1:
        navigableNeighbours.append((col + 1, row))

    if row + 1 < rows and matrix[col][row + 1] != 1:
        navigableNeighbours.append((col, row + 1))

    return navigableNeighbours


def solution(map):
    # Your code here
    printMatrix(map)

    matrix = [[num for num in arr] for arr in map]

    lengths = [[infinity for num in arr] for arr in map]
    lengths[0][0] = 0
    visited = [[False for num in arr] for arr in map]

    temp = [(0, 0)]

    while len(temp) != 0:
        print("temp", temp)
        col, row = temp[0]
        if not visited[col][row] and matrix[col][row] != 1:
            visited[col][row] = True
            navigableNeigbours = findNavigableNeighbours((col, row), matrix)
            for neighbour in navigableNeigbours:
                neighbourCol, neighbourRow = neighbour
                lengths[neighbourCol][neighbourRow] = lengths[col][row] + 1 if lengths[col][row] + \
                    1 < lengths[neighbourCol][neighbourRow] else lengths[neighbourCol][neighbourRow]
            temp.extend(navigableNeigbours)
            print("temp after append", temp)
        temp.pop(0)

    printMatrix(matrix)
    printMatrix(lengths)
    printMatrix(visited)


arr = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
       [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

arr2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

solution(arr)
