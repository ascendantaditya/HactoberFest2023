for case in range(int(input())):
  N = int(input())
  max_x, peaks = 0, 0
  for x in map(int, input().split()):
    if x > max_x:
      max_x = x
      peaks += 1
  print('BOB' if peaks % 2 else 'ANDY')
