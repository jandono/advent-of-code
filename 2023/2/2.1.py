def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def swap(x, y): return y, x

all_cubes = {
  'red': 12,
  'green': 13,
  'blue': 14,
}

def valid(line: str) -> bool:
  turns = line.split(';')
  for turn in turns:
    cubes = turn.split(',')
    for cube in cubes:
      parts = cube.split()
      num = int(parts[0])
      color = parts[1]
      if num > all_cubes[color]:
        return False 
  return True

def solve():
  s = 0
  while True:
    try:
      parts = read_string().split(':')
      game_id = int(parts[0].split()[-1])
      s += game_id if valid(parts[1]) else 0
    except Exception:
      break
  print(s)

if __name__ == '__main__':
  solve()