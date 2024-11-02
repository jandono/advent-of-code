def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def swap(x, y): return y, x

def solve():
  s = 0
  while True:
    try:
      line = read_string()
      numbers = line.split(':')[1]
      winning, mine = numbers.split('|')
      win_set = set(winning)
      val = 0
      for num in mine.split():
        if num in win_set:
          if val == 0:
            val = 1
          else:
            val *= 2
      s += val
    except Exception:
      break
  print(s)
if __name__ == '__main__':
  solve()