from collections import defaultdict

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def swap(x, y): return y, x

def solve():
  i = 0
  s = 0
  num_copies = defaultdict(int)
  while True:
    try:
      line = read_string()
      s += num_copies[i] + 1
      numbers = line.split(':')[1]
      winning, mine = numbers.split('|')
      win_set = set()
      for num in winning.split():
        win_set.add(num)
      
      matches = 0
      for num in mine.split():
        matches += 1 if num in win_set else 0

      for j in range(matches):
        num_copies[i+j+1] += num_copies[i] + 1
      i += 1
    except Exception:
      break
  print(s)


if __name__ == '__main__':
  solve()