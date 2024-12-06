from collections import defaultdict

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content

def count(s):
  sol, i = 0, 0
  while True:
    i = s.find('XMAS', i)
    if i == -1:
      break
    i += 1
    sol += 1
  return sol


def solve():
  rows = []
  cols = defaultdict(list)
  mdiags = defaultdict(list)
  sdiags = defaultdict(list)
  i = 0
  m = None
  while True:
    try:
      line = read_string()
      if m == None:
        m = len(line)
      rows.append(line)
      for j, c in enumerate(line):
        cols[j].append(c)
        mdiags[m - j + i - 1].append(c)
        sdiags[i+j].append(c)
      i += 1
    except Exception:
      break
  
  sol = 0
  for row in rows:
    sol += count(row) + count(row[::-1])

  for v in cols.values():
    col = ''.join(v)
    sol += count(col) + count(col[::-1])

  for d in mdiags.values():
    dia = ''.join(d)
    sol += count(dia) + count(dia[::-1])
  
  for d in sdiags.values():
    dia = ''.join(d)
    sol += count(dia) + count(dia[::-1])

  print(sol)

if __name__ == '__main__':
  solve()


# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33

# i   j 
# 0   3 = 0
# 0   2 = 1 
# 1   3 = 1     m - j + i - 1
# 0   1 = 2
# 1   2 = 2
