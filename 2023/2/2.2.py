def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def swap(x, y): return y, x



def process(line: str) -> int:
  all_cubes = {
  'red': 0,
  'green': 0,
  'blue': 0,
  }
  turns = line.split(';')
  for turn in turns:
    cubes = turn.split(',')
    for cube in cubes:
      parts = cube.split()
      num = int(parts[0])
      color = parts[1]
      all_cubes[color] = max(all_cubes[color], num)

  return all_cubes['blue'] * all_cubes['red'] * all_cubes['green']

def solve():
  s = 0
  while True:
    try:
      parts = read_string().split(':')
      s += process(parts[1])
    except Exception:
      break
  print(s)

if __name__ == '__main__':
  solve()