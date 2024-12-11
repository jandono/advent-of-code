from collections import deque

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content


def trail_heads(x: int, y: int, maze: list[list[str]]) -> int:
  n, m = len(maze), len(maze[0])
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  sol = 0
  q = deque()
  q.append((x, y, int(maze[x][y])))
  while q:
    i, j, val = q.popleft()
    if val == 9:
      sol += 1

    for ii, jj in directions:
      new_i, new_j = i + ii, j + jj
      if not (0 <= new_i < n and 0 <= new_j < m):
        continue
      if maze[new_i][new_j] == '.':
        continue

      if int(maze[new_i][new_j]) == val + 1 and (new_i, new_j):
        q.append((new_i, new_j, int(maze[new_i][new_j])))

  return sol

def solve():
  maze = []
  while True:
    try:
      line = read_string()
      maze.append(list(line))
    except Exception:
      break
  
  s = 0
  n, m = len(maze), len(maze[0])
  for i in range(n):
    for j in range(m):
      if maze[i][j] == '0':
        s += trail_heads(i, j, maze)
  print(s)


if __name__ == '__main__':
  solve()