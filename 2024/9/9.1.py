from collections import defaultdict

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content


def solve_line(line: str):
  ID = 0
  ids = []
  for i in range(0, len(line), 2):
    ids.extend([ID] * int(line[i]))
    if i + 1 < len(line):
      ids.extend(['.'] * int(line[i+1]))
    ID += 1

  l, r = 0, len(ids)-1
  while l < r:
    while l < r and ids[l] != '.':
      l += 1
    while l < r and ids[r] == '.':
      r -= 1
    if l < r:
      ids[l] = ids[r]
      ids[r] = '.'
      l += 1
      r -= 1
  return sum(i * int(num) if num !='.' else 0 for i, num in enumerate(ids))


def solve():
  while True:
    try:
      line = read_string()
      print(solve_line(line))
    except Exception:
      break

if __name__ == '__main__':
  solve()