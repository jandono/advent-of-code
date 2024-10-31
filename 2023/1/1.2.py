def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def swap(x, y): return y, x


nums = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9'
}

def process(line: str) -> int:
  first, second = '', ''
  for i, c in enumerate(line):
    if c.isdigit():
      if first == '':
        first = c
      second = c
    else:
      for num, val in nums.items():
        if line[i:].startswith(num):
          if first == '':
            first = val
          second = val
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