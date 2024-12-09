from collections import defaultdict

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content


def get_locations(
    maze: list[list[str]],
    n: int,
    m: int,
) -> dict[str, list[tuple[int, int]]]:
  locations = defaultdict(list)
  for i in range(n):
    for j in range(m):
      if maze[i][j] != '.':
        locations[maze[i][j]].append((i, j))
  return locations

def find_antinodes(maze: list[list[str]]) -> int:
  n, m = len(maze), len(maze[0])
  all_antinodes = set()
  locations_per_anthena = get_locations(maze, n, m)
  for _, locations in locations_per_anthena.items():
    for i in range(len(locations)):
      for j in range(i+1, len(locations)):
        x1, y1 = locations[i]
        x2, y2 = locations[j]
        
        xx1 = x1 - (x2 - x1)
        xx2 = x2 + (x2 - x1)
        if y1 <= y2:
          yy1 = y1 - (y2 - y1)
          yy2 = y2 + (y2 - y1)
        else:
          yy1 = y1 + (y1 - y2)
          yy2 = y2 - (y1 - y2)

        if  0 <= xx1 < n and 0 <= yy1 < m:
          all_antinodes.add((xx1, yy1))
        if 0 <= xx2 < n and 0 <= yy2 < m:
          all_antinodes.add((xx2, yy2))

  return len(all_antinodes)


def solve():
  maze = []
  while True:
    try:
      line = read_string()
      maze.append(list(line))
    except Exception:
      break
  
  print(find_antinodes(maze))

if __name__ == '__main__':
  solve()