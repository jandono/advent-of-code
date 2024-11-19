from collections import deque

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content


def can_go(i, j, new_i, new_j, maze:list[list[str]]):
  nn = neighbors(i, j, maze)
  for ii, jj in nn:
    if (i + ii, j + jj) == (new_i, new_j):
      return True
  return False


def neighbors(i, j, maze):
  neighbors = []
  if maze[i][j] == '7':
    neighbors = [(0, -1), (1, 0)]
  if maze[i][j] == '|':
    neighbors = [(-1, 0), (1, 0)]
  if maze[i][j] == '-':
    neighbors = [(0, -1), (0, 1)]
  if maze[i][j] == 'J':
    neighbors = [(0, -1), (-1, 0)]
  if maze[i][j] == 'L':
    neighbors = [(-1, 0), (0, 1)]
  if maze[i][j] == 'F':
    neighbors = [(1, 0), (0, 1)]
  return neighbors


def bfs(maze: list[list[str]], start):
  q = deque()
  q.append((*start, 0))
  cycle = set()
  sol = 0
  while q:
    i, j, wave = q.popleft()
    sol = max(sol, wave)
    for ii, jj in neighbors(i, j, maze):
      new_i, new_j = i + ii, j + jj
      if 0 <= new_i < len(maze) and 0 <= new_j < len(maze[new_i]) and (new_i, new_j) not in cycle and can_go(new_i, new_j, i, j, maze):
        q.append((new_i, new_j, wave + 1))
    cycle.add((i, j))
  return sol, cycle


def inside(x: int, y: int, cycle: set[tuple[int, int]], maze: list[list[str]]) -> bool:
  cnt = 0
  for j in range(1, y+1):
    if (x, y-j) in cycle and maze[x][y - j] in ['|', 'L', 'J']:
      cnt += 1
  return cnt % 2 == 1


def count_points(maze: list[list[str]], cycle):
  n, m = len(maze), len(maze[0])
  sol = 0
  for i in range(n):
    for j in range(m):
      if (i, j) not in cycle and inside(i, j, cycle, maze):
        sol += 1
  return sol  

def solve():
  maze = []
  start = None
  i = 0
  while True:
    try:
      line = read_string()
      for j, c in enumerate(line):
        if c == 'S':
          start = (i, j)
          # based on the given input S can only be 7.
          # Subbing it here saves an additional check down the line.
          line = line.replace('S', '7')
          break
      maze.append(list(line))
      i += 1
    except Exception:
      break
  cycle = bfs(maze, start)
  sol = count_points(maze, cycle)
  print(sol)


if __name__ == '__main__':
  solve()