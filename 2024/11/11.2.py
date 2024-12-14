def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content


def count_stones(stone, blinks, memo) -> int:
  
  if (stone, blinks) in memo:
    return memo[(stone, blinks)]

  if blinks == 0:
    return 1

  s = 0
  sstone = str(stone)
  l = len(sstone)
  if stone == 0:
    s += count_stones(1, blinks-1, memo)
  elif l % 2 == 0:
    s += count_stones(int(sstone[:l//2]), blinks-1, memo)
    s += count_stones(int(sstone[l//2:]), blinks-1, memo)
  else:
    s += count_stones(stone * 2024, blinks-1, memo)

  memo[(stone, blinks)] = s
  return s

def solve():
  while True:
    try:
      line = read_string()
      s = 0
      memo = dict()
      for stone in [int(x) for x in line.split()]:
        s += count_stones(stone, 75, memo)
      print(s)
    except Exception:
      break
  
if __name__ == '__main__':
  solve()