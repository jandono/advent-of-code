def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] 


def solve_maze(i: int, j: int, maze: list[list[str]]):
  n, m = len(maze), len(maze[0])
  positions = set()
  positions.add((i, j))
  dir_idx = 0
  for _ in range(n*m):
    ii = i + directions[dir_idx % 4][0]
    if not 0 <= ii < n:
      return 0
    jj = j + directions[dir_idx % 4][1]
    if not 0 <= jj < m:
      return 0
    
    if maze[ii][jj] == '#':
      dir_idx += 1
    else:
      i, j = ii, jj
      positions.add((i, j))
  return 1


def solve():
  maze = []
  i, start_i, start_j = 0, 0, 0
  while True:
    try:
      line = read_string()
      for j, c in enumerate(line):
        if c == '^':
          start_i, start_j = i, j
      maze.append(list(line))
      i += 1
    except Exception:
      break

  sol = 0
  for i in range(len(maze)):
    for j in range(len(maze[0])):
      if maze[i][j] == '.':
        maze[i][j] = '#'
        sol += solve_maze(start_i, start_j, maze)
        maze[i][j] = '.'
  print(sol)


if __name__ == '__main__':
  solve()