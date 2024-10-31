def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def swap(x, y): return y, x

def process(line: str) -> int:
  first, second = '', ''
  for c in line:
    if c.isdigit():
      if first == '':
        first = c
      second = c

  return int(first + second)

def solve():
  s = 0
  while True:
    try:
      line = read_string()
      s += process(line)
    except Exception:
      break
  print(s)


if __name__ == '__main__':
  solve()