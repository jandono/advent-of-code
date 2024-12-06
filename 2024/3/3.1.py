def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content

def valid(num: str) -> bool:
  if not (1 <= len(num) <= 3):
    return False

  for d in num:
    if not d.isnumeric():
      return False
  return True

def solve_line(segment: str) -> int:
  sol = 0
  i = 0
  while True:
    l = segment.find('mul(', i)
    r = segment.find(')', l)
    if l == -1 or r == -1:
      break
    i = l + 4
    parts = segment[l+4:r].split(',')
    if len(parts) != 2:
      continue
    
    if not valid(parts[0]) or not valid(parts[1]):
      continue

    sol += int(parts[0]) * int(parts[1])
  return sol

def solve():
  sol = 0
  while True:
    try:
      line = read_string()
      sol += solve_line(line)
    except Exception:
      break
  print(sol)

if __name__ == '__main__':
  solve()