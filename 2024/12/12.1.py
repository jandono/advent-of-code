from collections import deque

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(i, j, visited, maze, n, m):
  q = deque()
  q.append((i, j))
  area, perimeter = 0, 0
  while q:
    i, j = q.popleft()
    if (i, j) in visited:
      continue
    visited.add((i, j))
    area += 1

    for di, dj in directions:
      ii, jj = i + di, j + dj
      if 0 <= ii < n and 0 <= jj < m and maze[ii][jj] == maze[i][j]:
        q.append((ii, jj))
      else:
        perimeter += 1

  return area * perimeter


def solve_maze(maze) -> int:
  n, m = len(maze), len(maze[0])
  visited = set()
  s = 0
  for i in range(n):
    for j in range(m):
      if (i, j) not in visited:
        s += bfs(i, j, visited, maze, n, m)
  return s

def solve():
  maze = []
  while True:
    try:
      line = read_string()
      maze.append(list(line))
    except Exception:
      break
  
  print(solve_maze(maze))


if __name__ == '__main__':
  solve()