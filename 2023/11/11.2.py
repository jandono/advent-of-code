from collections import defaultdict

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content

def calc_new_columns(galaxy_in_column: dict[int, bool], num_columns: int):
  columns = dict()
  inc = 0
  for j in range(num_columns):
    columns[j] = j + inc
    if not galaxy_in_column[j]:
      inc += 999999
  return columns


def dist(x: tuple[int, int], y: tuple[int, int], rows: dict[int, int], columns: dict[int, int]) -> int:
  return abs(rows[x[0]] - rows[y[0]]) + abs(columns[x[1]] - columns[y[1]])


def solve():
  galaxies = []
  i = 0
  row_inc = 0
  galaxy_in_column = defaultdict(bool)

  rows = dict()
  columns = dict()
  num_columns = 0
  while True:
    try:
      line = read_string()
      num_columns = len(line)
      rows[i] = i + row_inc
      flag = True
      for j, c in enumerate(line):
        if c == '#':
          galaxies.append((i, j))
          galaxy_in_column[j] = True
          flag = False
      if flag:
        row_inc += 999999
      i += 1 
    except Exception:
      break
  
  columns = calc_new_columns(galaxy_in_column, num_columns)
  sol = 0
  n = len(galaxies)
  for i in range(n):
    for j in range(i + 1):
      sol += dist(galaxies[i], galaxies[j], rows, columns)
  print(sol)


if __name__ == '__main__':
  solve()