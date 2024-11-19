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
    if maze[i][j] == 'S':
      neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
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
  sol = 0
  q = deque()
  q.append((*start, 0))

  while q:
    i, j, wave = q.popleft()
    sol = max(sol, wave)

    for ii, jj in neighbors(i, j, maze):
      new_i, new_j = i + ii, j + jj
      if 0 <= new_i < len(maze) and 0 <= new_j < len(maze[new_i]) and maze[new_i][new_j] != '.' and can_go(new_i, new_j, i, j, maze):
        q.append((new_i, new_j, wave + 1))
    
    maze[i][j] = '.'

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
          break
      maze.append(list(line))
      i += 1
    except Exception:
      break
  print(bfs(maze, start))
if __name__ == '__main__':
  solve()