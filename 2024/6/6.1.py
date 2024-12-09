def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] 

def solve_maze(i, j, maze):
  n, m = len(maze), len(maze[0])
  positions = set()
  positions.add((i, j))
  dir_idx = 0
  while True:
    ii = i + directions[dir_idx % 4][0]
    if not 0 <= ii < n:
      return len(positions)
    jj = j + directions[dir_idx % 4][1]
    if not 0 <= jj < m:
      return len(positions)
    
    if maze[ii][jj] == '#':
      dir_idx += 1
    else:
      i = ii
      j = jj
      positions.add((i, j))


def solve():
  maze = []
  i, start_i, start_j = 0, 0, 0
  while True:
    try:
      line = read_string()
      for j, c in enumerate(line):
        if c == '^':
          start_i, start_j = i, j
      maze.append(line)
      i += 1
    except Exception:
      break
  print(solve_maze(start_i, start_j, maze))


if __name__ == '__main__':
  solve()