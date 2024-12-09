from collections import defaultdict

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content


def solve_line(line: str):
  ID = 0
  l = [int(num) for num in line]
  if len(l) % 2 == 0:
    l.pop()

  ids = []
  for i in range(0, len(l), 2):
    ids.append((ID, l[i]))
    if i + 1 < len(line):
      ids.append(('.', l[i+1]))
    ID += 1

  l, r = 0, len(ids)-1
  while l < r:
    while l < r and ids[r][0] == '.':
      r -= 1

    while l < r and (ids[l][0] != '.' or ids[l][1] < ids[r][1]):
      l += 1

    if l < r and ids[l][1] >= ids[r][1]:
      left = ids[l][1] - ids[r][1]
      ids[l] = ids[r]
      ids[r] = ('.', ids[r][1])
      if left:
        ids = ids[:l+1] + [('.', left)] + ids[l+1:]

    l = 0
    r -= 1
  
  s, i = 0, 0
  for elem in ids:
    for _ in range(elem[1]):
      if elem[0] != '.':
        s += i * elem[0]
      i += 1
 
  return s


def solve():
  while True:
    try:
      line = read_string()
      print(solve_line(line))
    except Exception:
      break

if __name__ == '__main__':
  solve()