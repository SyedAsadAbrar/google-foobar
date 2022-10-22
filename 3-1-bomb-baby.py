def solution(m, f):
    # Your code here
    startingTuple = (1, 1)
    
    goalTuple = (int(m), int(f))
    
    levels = 0

    currM, currF = goalTuple

    while currM > 1 or currF > 1:
        if (currF == currM and currF != 1) or currF < 1 or currM < 1:
            return "impossible"
        elif currM > currF:
            levels += int(currM / currF)
            currM = (currM % currF)
        elif currM < currF:
            levels += int(currF / currM)
            currF = (currF % currM)

    if (currF == 1 and currM == 0) or (currM == 1 and currF == 0):
        return str(levels - 1)

    if currM < 1 or currF < 1:
        return "impossible"

    if currF == 1 and currM == 1:
        return str(levels)

print(solution(2, 1))