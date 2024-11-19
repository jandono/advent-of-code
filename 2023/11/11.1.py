from collections import defaultdict

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content


def expand_columns(space: list[list[str]], columns: dict[int, bool]):
  new_space = []
  for row in space:
    new_row = []
    for j, c in enumerate(row):
      if not columns[j]:
        new_row.append(c)
      new_row.append(c)
    new_space.append(new_row)
  return new_space


def get_galaxies(space: list[list[str]]):
  galaxies = []
  for i, row in enumerate(space):
    for j, c in enumerate(row):
      if c == '#':
        galaxies.append((i, j))
  return galaxies


def dist(x: tuple[int, int], y: tuple[int, int]) -> int:
  return abs(x[0] - y[0]) + abs(x[1] - y[1])

def solve():
  space = []
  i = 0
  columns = defaultdict(bool)
  while True:
    try:
      line = read_string()
      flag = True
      for j, c in enumerate(line):
        if c == '#':
          columns[j] = True
          flag = False
      if flag:
        space.append(list(line))
      space.append(list(line))
      i += 1 
    except Exception:
      break
  
  space = expand_columns(space, columns)
  
  sol = 0
  galaxies = get_galaxies(space)
  n = len(galaxies)
  for i in range(n):
    for j in range(i + 1):
      sol += dist(galaxies[i], galaxies[j])
  print(sol)


if __name__ == '__main__':
  solve()