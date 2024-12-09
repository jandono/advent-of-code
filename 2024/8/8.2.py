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


def populate_up(
    x1: int, y1: int, x2: int, y2: int,
    all_antinodes: set[tuple[int, int]],
    n: int, m: int,
):
  while x1 >= 0 and 0 <= y1 < m:
    xx = x1 - (x2 - x1)
    if y1 <= y2:
      yy = y1 - (y2 - y1)
    else:
      yy = y1 + (y1 - y2)

    if  0 <= xx < n and 0 <= yy < m:
      all_antinodes.add((xx, yy))

    x2, y2 = x1, y1
    x1, y1 = xx, yy


def populate_down(
    x1: int, y1: int, x2: int, y2: int,
    all_antinodes: set[tuple[int, int]],
    n: int, m: int,
):
  while x2 < n and 0 <= y2 < m:
    xx = x2 + (x2 - x1)
    if y1 <= y2:
      yy = y2 + (y2 - y1)
    else:
      yy = y2 - (y1 - y2)

    if 0 <= xx < n and 0 <= yy < m:
      all_antinodes.add((xx, yy))

    x1, y1 = x2, y2
    x2, y2 = xx, yy


def find_antinodes(maze: list[list[str]]) -> int:
  n, m = len(maze), len(maze[0])
  all_antinodes = set()
  locations_per_anthena = get_locations(maze, n, m)
  for _, locations in locations_per_anthena.items():
    for i in range(len(locations)):
      for j in range(i+1, len(locations)):
        x1, y1 = locations[i]
        x2, y2 = locations[j]
        all_antinodes.add((x1, y1))
        all_antinodes.add((x2, y2))
        populate_up(x1, y1, x2, y2, all_antinodes, n, m)
        populate_down(x1, y1, x2, y2, all_antinodes, n, m)
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