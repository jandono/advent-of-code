def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def swap(x, y): return y, x

nums = {}


def process_schema(schema: list[str]) -> int:
  s = 0
  n= len(schema)
  for i in range(n):
    num = 0
    connected = False
    for j, c in enumerate(schema[i]):
      if c.isdigit():
        num = num * 10 + int(schema[i][j])
        for ii in [-1, 0, 1]:
          for jj in [-1, 0, 1]:
            m = len(schema[i])
            new_i, new_j= i + ii, j + jj
            if new_i < 0 or new_i >= n:
              continue
            if new_j < 0 or new_j >= m:
              continue
            if not schema[new_i][new_j].isdigit() and schema[new_i][new_j] != '.':
              connected = True
      else:
        if connected:
          s += num
        connected = False
        num = 0
    if connected:
      s += num
  return s

def solve():
  schema = []
  while True:
    try:
      schema.append(read_string())
    except Exception as e:
      break
    
  s = process_schema(schema)
  print(s)

if __name__ == '__main__':
  solve()