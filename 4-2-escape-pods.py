def solution(entrances, exits, path):
    # Your code here
    intermediate = [num for num in range(
        len(path)) if (num not in exits and num not in entrances)]

    # For visualization purposes
    # print("entrances", entrances)
    # print("intermediate", intermediate)
    # print("exits", exits)
    # for arr in path:
    #     print(arr)

    wantToEnter = [0 for _ in path]

    for row in entrances:
        arr = path[row]
        for col in intermediate:
            number = arr[col]
            wantToEnter[col] += number

    maxPossible = [sum(
        path[index]) if index in intermediate else 0 for index in range(len(path))]

    answer = [num for num in maxPossible]

    for index in range(len(wantToEnter)):
        actualColumnSum = wantToEnter[index]
        maximumPossible = maxPossible[index]
        answer[index] = min(actualColumnSum, maximumPossible)

    return sum([answer[roomNumber] for roomNumber in intermediate])


testCase1 = {"entrances": [0], "exits": [3], "path": [
    [0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]}
testCase2 = {"entrances": [0, 1], "exits": [4, 5], "path": [[0, 0, 4, 6, 0, 0], [
    0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]}

print(solution(testCase1["entrances"], testCase1["exits"], testCase1["path"]))
print("----")
print(solution(testCase2["entrances"], testCase2["exits"], testCase2["path"]))
