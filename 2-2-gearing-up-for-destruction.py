def solution(pegs):
  # Your code here
  print(pegs)

  n = len(pegs)

  isEven = n % 2 == 0

  multipler = -2

  sum = 0

  result = 1

  for i in range(len(pegs)):
    sum = (-1) ** (i) * pegs[i]

    print(sum)

    sum *= 2 if i != 0 and i != len(pegs) - 1 else 1

  result *= multipler * (float(sum)/3 if isEven else sum)

  print(result)


print(solution([4, 30, 50]))