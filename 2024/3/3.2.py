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

def solve_segment(segment: str) -> int:
  sol, i = 0, 0
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


def solve_line(line: str) -> int:
  donts = line.split('don\'t()')
  dos = [donts[0]]
  for part in donts[1:]:
    if 'do()' in part:
      dos.append(part[part.find('do()') + 4:])

  sol = 0
  for do in dos:
    sol += solve_segment(do)
  return sol

def solve():
  lines = []
  while True:
    try:
      lines.append(read_string())
    except Exception:
      break
  print(solve_line(''.join(lines)))

if __name__ == '__main__':
  solve()