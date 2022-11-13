def solution(entrances, exits, path):
    # Your code here

    intermediate = [num for num in range(
        len(path)) if (num not in exits and num not in entrances)]

    print("entrances", entrances)
    print("intermediate", intermediate)
    print("exits", exits)
    for arr in path:
        print(arr)

    wantToEnter = [0 for arr in path]

    lastRooms = []

    for roomNumber in exits:
        for index in range(len(path)):
            if path[index][roomNumber] > 0 and index not in lastRooms:
                lastRooms.append(index)

    print("lastRooms", lastRooms)

    for row in range(len(path)):
        arr = path[row]
        for col in intermediate:
            number = arr[col]
            wantToEnter[col] += number

    print("wantToEnter", wantToEnter)

    maxPossible = [sum(
        path[index]) if index in intermediate else 0 for index in range(len(path))]

    answer = [num for num in maxPossible]

    print("maxPossible", maxPossible)

    for index in range(len(wantToEnter)):
        actualColumnSum = wantToEnter[index]
        maximumPossible = maxPossible[index]
        answer[index] = min(actualColumnSum, maximumPossible)

    print("answer", answer)

    return sum([answer[roomNumber] for roomNumber in lastRooms])


def solution2(entrances, exits, path):
    le = len(entrances)
    lp = len(path)
    lx = len(exits)

    print("lengths", le, lp, lx)
    bunn_count = 0
    # To find all intermediate rooms
    inter_paths = path[le:(lp-lx)]
    print("inter_paths", inter_paths)
    # Loop through range of length of intermediate rooms
    for i in range(lp - le - lx):
        print("i", i)
        # Sum of an intermediate room's possible number of bunnies allowed
        sum_range = sum(inter_paths[i])
        print("sum_range", sum_range)
        sum_enter = 0                             # Sum of bunnies that enter that room
        for j in entrances:
            # Get all bunnies that enter a room
            sum_enter += path[j][le + i]
        print("sum_enter", sum_enter)
        bunn_count += min(sum_enter, sum_range)
    return bunn_count


testCase1 = {"entrances": [0], "exits": [3], "path": [
    [0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]}
testCase2 = {"entrances": [0, 1], "exits": [4, 5], "path": [[0, 0, 4, 6, 0, 0], [
    0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]}

print(solution(testCase1["entrances"], testCase1["exits"], testCase1["path"]))
print("----")
print(solution(testCase2["entrances"], testCase2["exits"], testCase2["path"]))
